"""W01: Groundsource flood events -> region-week labels (decision 0003).

    python src/labels.py              # writes data/processed/labels.parquet with the chosen rule
    python src/labels.py --compare    # also writes the 8-option comparison table and the EDA figures

Rule options (decision 0003 left these open; the chosen one is RULE below, see decision 0007):
  assign:   "centroid"   event goes to the region holding its polygon's centroid
            "intersects" event goes to every region its polygon touches
  dates:    "start"      the week of start_date only
            "any"        every week from start_date to end_date
  max_area: None, or drop polygons larger than this many km² (whole-district or whole-region mentions)
"""
import sys
from itertools import product
from pathlib import Path

import geopandas as gpd
import pandas as pd
from shapely.geometry import box

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from regions import load as load_regions  # noqa: E402
from synthetic import WEEKS  # noqa: E402

RAW = ROOT / "data" / "raw" / "groundsource" / "groundsource_2026.parquet"
INTERIM, PROCESSED = ROOT / "data" / "interim", ROOT / "data" / "processed"
LEARN = ROOT / "learnings"
UTM = 32630  # UTM zone 30N: metres, for centroids over Ghana
RULE = dict(assign="centroid", dates="start", max_area=None)


def ghana_events() -> gpd.GeoDataFrame:
    """Events whose polygon touches Ghana, with region assignments for both methods. Cached."""
    cache = INTERIM / "groundsource_ghana.parquet"
    if cache.exists():
        return gpd.read_parquet(cache)
    regions = load_regions()
    minx, miny, maxx, maxy = regions.total_bounds
    ev = gpd.read_parquet(RAW)  # no bbox index in this file, so read all 2.6M events once, then cache Ghana
    ev = ev.iloc[ev.sindex.query(box(minx, miny, maxx, maxy))]
    ev = ev[ev.intersects(regions.union_all())].reset_index(drop=True)
    ev["start"] = pd.to_datetime(ev.start_date).dt.normalize()
    ev["end"] = pd.to_datetime(ev.end_date).dt.normalize().fillna(ev.start)
    ev["end"] = ev[["start", "end"]].max(axis=1)
    # centroid region (one or none) and touched regions (one or more)
    cen = gpd.GeoDataFrame(geometry=ev.to_crs(UTM).centroid.to_crs(4326), index=ev.index)
    ev["centroid_region"] = gpd.sjoin(cen, regions, predicate="within")["region_id"].groupby(level=0).first()
    touched = gpd.sjoin(ev[["geometry"]], regions, predicate="intersects")["region_id"]
    ev["touched_regions"] = touched.groupby(level=0).agg(lambda s: ",".join(sorted(s)))
    ev = ev.drop(columns=["start_date", "end_date"])
    INTERIM.mkdir(parents=True, exist_ok=True)
    ev.to_parquet(cache)
    return ev


def event_region_weeks(ev: pd.DataFrame, assign: str, dates: str, max_area: float | None) -> pd.DataFrame:
    """One row per (event, region, week) the event counts towards."""
    e = ev if max_area is None else ev[ev.area_km2 <= max_area]
    if assign == "centroid":
        e = e.dropna(subset=["centroid_region"]).assign(region_id=lambda d: d.centroid_region)
    else:
        e = e.assign(region_id=e.touched_regions.str.split(",")).explode("region_id")
    monday = lambda s: s - pd.to_timedelta(s.dt.weekday, unit="D")  # noqa: E731
    if dates == "start":
        e = e.assign(week_start=monday(e.start))
    else:
        e = e.assign(week_start=[pd.date_range(a, b, freq="D") for a, b in zip(e.start, e.end)]).explode("week_start")
        e["week_start"] = monday(pd.to_datetime(e.week_start))
    e = e[["uuid", "region_id", "week_start"]].drop_duplicates()
    return e[e.week_start.between(WEEKS[0], WEEKS[-1])]


def labels(ev: pd.DataFrame, **rule) -> pd.DataFrame:
    erw = event_region_weeks(ev, **rule)
    n = erw.groupby(["region_id", "week_start"]).uuid.nunique().rename("n_events")
    grid = pd.MultiIndex.from_product([sorted(load_regions().region_id), WEEKS], names=["region_id", "week_start"])
    out = n.reindex(grid, fill_value=0).reset_index()
    out["flood"] = (out.n_events > 0).astype("int8")
    return out[["region_id", "week_start", "flood", "n_events"]]


def check(lab: pd.DataFrame) -> None:
    assert len(lab) == 16 * len(WEEKS) == 9184
    assert not lab.duplicated(["region_id", "week_start"]).any()
    assert set(lab.flood.unique()) <= {0, 1}
    assert (lab.week_start.dt.weekday == 0).all()


def compare(ev: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for assign, dates, max_area in product(["centroid", "intersects"], ["start", "any"], [None, 500]):
        lab = labels(ev, assign=assign, dates=dates, max_area=max_area)
        check(lab)
        ga = lab[lab.region_id == "GH-AA"].flood.mean()
        yr = lab.assign(y=lab.week_start.dt.year).groupby("y").flood.mean()
        rows.append(dict(assign=assign, dates=dates, max_area_km2=max_area or "keep all",
                         positives=int(lab.flood.sum()), rate=round(lab.flood.mean(), 4),
                         greater_accra_rate=round(ga, 3),
                         regions_with_no_positive=int((lab.groupby("region_id").flood.sum() == 0).sum()),
                         train_rate_2015_22=round(lab[lab.week_start.dt.year <= 2022].flood.mean(), 4),
                         test_rate_2024_25=round(lab[lab.week_start.dt.year >= 2024].flood.mean(), 4),
                         min_year_rate=round(yr.min(), 3), max_year_rate=round(yr.max(), 3)))
    return pd.DataFrame(rows)


def eda(ev: pd.DataFrame, lab: pd.DataFrame) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    e = event_region_weeks(ev, **RULE)
    fig, ax = plt.subplots(1, 3, figsize=(15, 4))
    e.week_start.dt.year.value_counts().sort_index().plot.bar(ax=ax[0], color="#2a6f97", title="Events per year (start week)")
    e.week_start.dt.month.value_counts().sort_index().plot.bar(ax=ax[1], color="#2a6f97", title="Events per month")
    lab.groupby("region_id").flood.mean().sort_values().plot.barh(ax=ax[2], color="#2a6f97", title="Share of weeks flagged, by region")
    fig.tight_layout()
    fig.savefig(LEARN / "figures" / "w01_label_eda.png", dpi=110)


def main() -> None:
    ev = ghana_events()
    in_range = ev[ev.start.between("2015-01-01", "2025-12-31")]
    print(f"Ghana events touching any region: {len(ev)}; with centroid in a region: {ev.centroid_region.notna().sum()}; "
          f"centroid in a region and starting 2015-2025: {in_range.centroid_region.notna().sum()}; "
          f"dates {ev.start.min().date()} to {ev.start.max().date()}")
    lab = labels(ev, **RULE)
    check(lab)
    PROCESSED.mkdir(parents=True, exist_ok=True)
    lab.to_parquet(PROCESSED / "labels.parquet")
    print(f"passed: {len(lab)} rows, {int(lab.flood.sum())} positive ({lab.flood.mean():.1%}), rule {RULE}")
    if "--compare" in sys.argv:
        (LEARN / "tables").mkdir(exist_ok=True); (LEARN / "figures").mkdir(exist_ok=True)
        t = compare(ev)
        t.to_csv(LEARN / "tables" / "w01_label_options.csv", index=False)
        print(t.to_string(index=False))
        eda(ev, lab)


if __name__ == "__main__":
    main()
