"""W02: rain and soil-moisture features per region-week, from Earth Engine.

    python src/weather.py        # needs `earthengine authenticate` and EE_PROJECT in .env

Writes
  data/interim/weather_daily.parquet          region_id, date, rain_mm, soil_moisture
  data/processed/weather.parquet              region_id, week_start, features (all from days BEFORE week_start)
  data/processed/weather_forecast_experiment.parquet   rain_thisweek_mm (uses the week itself: NOT for the main model)
Earth Engine pulls are cached per quarter in data/interim/ee_cache/, so a rerun only fetches what is missing.
"""
import os
import sys
from pathlib import Path

import ee
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from regions import load as load_regions  # noqa: E402
from synthetic import WEEKS  # noqa: E402

INTERIM, PROCESSED = ROOT / "data" / "interim", ROOT / "data" / "processed"
CACHE = INTERIM / "ee_cache"
START, END = "2014-12-01", "2026-01-05"  # 30+ days before the first week, through the last week
SOURCES = {  # name: (collection, band, native scale in m, output column, unit conversion)
    "chirps": ("UCSB-CHG/CHIRPS/DAILY", "precipitation", 5566, "rain_mm", 1.0),
    "era5": ("ECMWF/ERA5_LAND/DAILY_AGGR", "volumetric_soil_water_layer_1", 11132, "soil_moisture", 1.0),
}
RAIN_WINDOWS = [1, 3, 7, 14, 30]


def project() -> str:
    env = ROOT / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            k, _, v = line.partition("=")
            os.environ.setdefault(k.strip(), v.strip())
    return os.environ["EE_PROJECT"]


def region_fc() -> ee.FeatureCollection:
    # ponytail: 0.01° (~1 km) simplification keeps the request small; region means barely move.
    g = load_regions()
    g["geometry"] = g.geometry.simplify(0.01)
    return ee.FeatureCollection(g[["region_id", "geometry"]].__geo_interface__)


def pull(name: str, fc: ee.FeatureCollection) -> pd.DataFrame:
    coll_id, band, scale, col, mult = SOURCES[name]
    CACHE.mkdir(parents=True, exist_ok=True)
    out = []
    edges = sorted({pd.Timestamp(START), *pd.date_range(START, END, freq="QS"), pd.Timestamp(END)})
    for a, b in zip(edges[:-1], edges[1:]):  # quarters: ~92 days × 16 regions < 5000-feature limit
        f = CACHE / f"{name}_{a:%Y%m%d}_{b:%Y%m%d}.parquet"
        if not f.exists():
            coll = ee.ImageCollection(coll_id).select(band).filterDate(str(a.date()), str(b.date()))

            def per_day(img):
                d = img.date().format("YYYY-MM-dd")
                return img.reduceRegions(fc, ee.Reducer.mean(), scale).map(
                    lambda ft: ft.set("date", d).setGeometry(None))

            feats = coll.map(per_day).flatten().getInfo()["features"]
            pd.DataFrame([{"region_id": x["properties"]["region_id"], "date": x["properties"]["date"],
                           col: x["properties"].get("mean")} for x in feats]).to_parquet(f)
            print(f"  {name} {a.date()}: {len(feats)} rows")
        out.append(pd.read_parquet(f))
    df = pd.concat(out, ignore_index=True)
    df["date"] = pd.to_datetime(df["date"])
    days = pd.date_range(START, pd.Timestamp(END) - pd.Timedelta(days=1))
    assert len(df) == 16 * len(days) and set(df.date) == set(days), f"{name}: {len(df)} rows, gaps in dates"
    df[col] = df[col] * mult
    return df


def weekly(daily: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Features for week w use days w-k .. w-1 only (shift(1) drops the day itself)."""
    rain = daily.pivot(index="date", columns="region_id", values="rain_mm").asfreq("D")
    soil = daily.pivot(index="date", columns="region_id", values="soil_moisture").asfreq("D")
    past = rain.shift(1)  # value at date d now describes d-1
    feats = {f"rain_{k}d_mm": past.rolling(k, min_periods=k).sum() for k in RAIN_WINDOWS}
    feats["rain_max1d_7d_mm"] = past.rolling(7, min_periods=7).max()
    feats["soil_moisture"] = soil.shift(1).rolling(7, min_periods=7).mean()
    weeks = pd.DatetimeIndex(WEEKS)
    long = [f.reindex(weeks).stack().rename(n) for n, f in feats.items()]
    w = pd.concat(long, axis=1).rename_axis(["week_start", "region_id"]).reset_index()
    w = w[["region_id", "week_start", *feats]].sort_values(["region_id", "week_start"]).reset_index(drop=True)

    this_week = rain.rolling(7, min_periods=7).sum().shift(-6)  # days w .. w+6: the future, experiment only
    fx = this_week.reindex(weeks).stack().rename("rain_thisweek_mm").rename_axis(["week_start", "region_id"]).reset_index()
    return w, fx[["region_id", "week_start", "rain_thisweek_mm"]]


def check(w: pd.DataFrame, daily: pd.DataFrame, n: int = 200, seed: int = 553) -> None:
    assert len(w) == 16 * len(WEEKS) and not w.duplicated(["region_id", "week_start"]).any()
    assert w.drop(columns=["region_id", "week_start"]).notna().all().all(), "missing feature values"
    assert (w.filter(like="rain_") >= 0).all().all()
    # Leakage check: recompute a sample straight from days strictly before week_start.
    d = daily.set_index(["region_id", "date"]).sort_index()
    for _, r in w.sample(n, random_state=seed).iterrows():
        s = d.loc[r.region_id]
        before = s[s.index < r.week_start]
        assert np.isclose(before.rain_mm.iloc[-7:].sum(), r.rain_7d_mm)
        assert np.isclose(before.rain_mm.iloc[-30:].sum(), r.rain_30d_mm)
        assert np.isclose(before.soil_moisture.iloc[-7:].mean(), r.soil_moisture)
        assert before.index.max() == r.week_start - pd.Timedelta(days=1)


def main() -> None:
    ee.Initialize(project=project())
    fc = region_fc()
    daily = pull("chirps", fc).merge(pull("era5", fc), on=["region_id", "date"], how="outer")
    daily = daily.sort_values(["region_id", "date"]).reset_index(drop=True)
    INTERIM.mkdir(parents=True, exist_ok=True)
    PROCESSED.mkdir(parents=True, exist_ok=True)
    daily.to_parquet(INTERIM / "weather_daily.parquet")
    w, fx = weekly(daily)
    check(w, daily)
    w.to_parquet(PROCESSED / "weather.parquet")
    fx.to_parquet(PROCESSED / "weather_forecast_experiment.parquet")
    print(f"passed: {len(w)} rows, {w.week_start.nunique()} weeks, columns {list(w.columns[2:])}")


if __name__ == "__main__":
    main()
