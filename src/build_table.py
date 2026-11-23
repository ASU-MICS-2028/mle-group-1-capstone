"""W05: join labels ⋈ weather ⋈ static into data/processed/table.parquet (decision 0003).

    python src/build_table.py
A missing input is skipped with a warning, except labels.
"""
import sys
import warnings
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from synthetic import REGIONS, WEEKS  # noqa: E402

P = ROOT / "data" / "processed"
KEYS = ["region_id", "week_start"]


def build() -> pd.DataFrame:
    df = pd.read_parquet(P / "labels.parquet")
    for name in ["weather", "static"]:
        f = P / f"{name}.parquet"
        if not f.exists():
            warnings.warn(f"{f.name} missing: skipped")
            continue
        x = pd.read_parquet(f)
        if "week_start" in x:
            df = df.merge(x, on=KEYS, how="left", validate="1:1")
        elif "year" in x:  # time-varying static features: use the previous year's value
            df = df.assign(year=df.week_start.dt.year - 1).merge(x, on=["region_id", "year"], how="left").drop(columns="year")
        else:
            df = df.merge(x, on="region_id", how="left", validate="m:1")
    df["region_name"] = df.region_id.map(REGIONS)
    df["month"] = df.week_start.dt.month
    # floods reported in the 4 weeks before this one (shift(1): never this week's label)
    df = df.sort_values(KEYS).reset_index(drop=True)
    df["floods_prev_4w"] = df.groupby("region_id").flood.transform(lambda s: s.shift(1).rolling(4, min_periods=1).sum()).fillna(0)
    return df


if __name__ == "__main__":
    df = build()
    assert len(df) == 16 * len(WEEKS) and not df.duplicated(KEYS).any()
    assert df.drop(columns=["n_events"]).notna().all().all(), df.isna().sum()[lambda s: s > 0]
    df.to_parquet(P / "table.parquet", index=False)
    print(f"passed: {len(df)} rows, {df.shape[1]} columns, positive rate {df.flood.mean():.3f}")
