"""Fake region-week table with the exact shape of decision 0003.

Lets the harness (W05), models (W06) and dashboard (W10) be built before the
real data exists. Numbers are made up: never report results from this file.

    python src/synthetic.py [out_path]     # default data/processed/table_synthetic.parquet
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

# ISO 3166-2:GH codes for the 16 regions = geoBoundaries gbOpen GHA ADM1 shapeISO (checked 2026-11-15).
REGIONS = {
    "GH-AA": "Greater Accra", "GH-AH": "Ashanti", "GH-AF": "Ahafo", "GH-BO": "Bono",
    "GH-BE": "Bono East", "GH-CP": "Central", "GH-EP": "Eastern", "GH-NP": "Northern",
    "GH-NE": "North East", "GH-SV": "Savannah", "GH-UE": "Upper East", "GH-UW": "Upper West",
    "GH-TV": "Volta", "GH-OT": "Oti", "GH-WP": "Western", "GH-WN": "Western North",
}
WEEKS = pd.date_range("2015-01-05", "2025-12-29", freq="W-MON")


def make(seed: int = 553) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    df = pd.MultiIndex.from_product([list(REGIONS), WEEKS], names=["region_id", "week_start"]).to_frame(index=False)
    df["region_name"] = df.region_id.map(REGIONS)
    df["month"] = df.week_start.dt.month
    wet = df.month.isin([5, 6, 9, 10]).to_numpy()  # two rainy seasons
    for k in (1, 3, 7, 14, 30):
        df[f"rain_{k}d_mm"] = rng.gamma(1.2 + wet, 2.0 * k ** 0.9, len(df)).round(1)
    df["soil_moisture"] = (0.15 + 0.2 * wet + rng.normal(0, 0.04, len(df))).clip(0.02, 0.5).round(3)
    df["builtup_share"] = df.region_id.map({r: 0.4 if r == "GH-AA" else rng.uniform(0.01, 0.1) for r in REGIONS})
    logit = -4.2 + 0.03 * df.rain_7d_mm + 4 * df.builtup_share
    df["flood"] = (rng.random(len(df)) < 1 / (1 + np.exp(-logit))).astype(int)
    df["n_events"] = df.flood * rng.integers(1, 4, len(df))
    df["floods_prev_4w"] = df.groupby("region_id").flood.transform(lambda s: s.shift(1).rolling(4, min_periods=1).sum()).fillna(0)
    return df


if __name__ == "__main__":
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "data/processed/table_synthetic.parquet")
    df = make()
    assert len(df) == 16 * len(WEEKS) and not df.duplicated(["region_id", "week_start"]).any()
    assert set(df.flood.unique()) <= {0, 1} and 0.02 < df.flood.mean() < 0.15
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(out, index=False)
    print(f"passed: {len(df)} rows, {len(WEEKS)} weeks, positive rate {df.flood.mean():.3f} -> {out}")
