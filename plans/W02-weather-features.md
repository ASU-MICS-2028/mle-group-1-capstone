---
workstream: W02
issue: "#TBD"
owner: unassigned (suggested role: Data lead / Modelling lead)
status: Not started
needs: none (region polygons come from geoBoundaries directly if W01's src/regions.py isn't ready)
due: 2026-11-19
---
# W02 · Weather features: rain and soil wetness per region-week

## Goal
`data/processed/weather.parquet` keyed on `region_id, week_start`. Every value is computed **only from days before `week_start`**.

## Why it matters
Rain is the main signal. The mid-check needs a rainfall baseline, and the honest question this project asks is whether a model beats a simple rainfall rule.

## Inputs
- CHIRPS daily rainfall (v2, or v3: check which, since v2 production ends Dec 2026).
- ERA5-Land daily soil moisture.
- Both are available through **Google Earth Engine**, which needs registered accounts (do this first: it can take a day).
- The fallback, if Earth Engine is slow, is the CHIRPS direct download from UCSB CHC.

## Outputs
- **`src/weather.py`** (or `notebooks/02_weather_ee.ipynb` plus an export script). It produces the region-mean daily series `data/interim/weather_daily.parquet`, then the weekly features:
  - `rain_1d_mm`, `rain_3d_mm`, `rain_7d_mm`, `rain_14d_mm`, `rain_30d_mm`, `rain_max1d_7d_mm`;
  - `soil_moisture`, which is the mean of the 7 days before.
- **Rows in `data/README.md`** listing each column, its unit and how it's computed.
- **A separate, clearly named forecast experiment:** `rain_thisweek_mm`. It isn't used in the main model ([decision 0004](../docs/decisions/0004-temporal-split.md)).

## Steps
- [ ] Register Earth Engine accounts, and note in the issue who has access.
- [ ] Pull region-mean daily CHIRPS for 2014-12 to 2025-12.
- [ ] Pull ERA5-Land soil moisture.
- [ ] Compute the lagged weekly features. Add an `assert` that no feature uses a date ≥ `week_start`.
- [ ] Sanity plots: monthly rain per region should show the two rainy seasons.

## Read first
- [knowledge/forecast-leakage.md](../knowledge/forecast-leakage.md)
- [knowledge/chirps.md](../knowledge/chirps.md)
- [knowledge/era5-land.md](../knowledge/era5-land.md)
