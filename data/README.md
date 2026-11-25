# Data: where it comes from (the data itself is never committed)

The repo is public, so this folder is gitignored and only this note is committed ([decision 0005](../docs/decisions/0005-public-repo-and-data-handling.md)). Anyone can rebuild every file from the instructions below.

```
data/raw/         downloads, untouched
data/interim/     per-source tables (e.g. region-mean daily rain)
data/processed/   region-week files from decision 0003 (labels, weather, static, table)
```

## Quick start: download the built tables

You can skip the 667 MB Groundsource download and the Earth Engine setup. The built files are in the team Google Drive: **[final project → data](https://drive.google.com/drive/folders/1dR6fG05fACSeCf_11TTVHr6ED-e9oJYv)** (team members only; ask Joseph for access).

1. Download the `processed` and `interim` folders.
2. Put them inside this `data/` folder, so you end up with `data/processed/table.parquet`.
3. Run your code. `table.parquet` is the main table: one row per region per week, with the flood label and the rain features.

| File | What it holds |
|---|---|
| `processed/table.parquet` | The model table: labels + weather + region and month (9,184 rows) |
| `processed/labels.parquet` | Flood label per region-week ([decision 0007](../docs/decisions/0007-label-rule.md)) |
| `processed/weather.parquet` | Rain and soil-moisture features per region-week |
| `processed/weather_forecast_experiment.parquet` | Rain during the week itself, for the forecast experiment only |
| `interim/groundsource_ghana.parquet` | The 2,725 Groundsource flood events in Ghana, with their regions |
| `interim/weather_daily.parquet` | Daily rain and soil moisture per region |

Built on 23 Nov 2026 from the code in PRs #17–#19. If the code changes, Joseph rebuilds and replaces these files.

## Sources
Whoever adds a source fills in its row: version or date, and the fetch command or script.

| Source | Used for | Licence | Version / date pulled | How to fetch | Status |
|---|---|---|---|---|---|
| [Groundsource](https://zenodo.org/records/18647054) ([note](../knowledge/groundsource-dataset.md)) | labels (W01) | CC BY 4.0 | `groundsource_2026.parquet`, 667,122,400 bytes, md5 cd1b5de6508f7aad8e1d1d0dd4cecea6, published 2026-02-15; pulled 2026-11-22 | download into `data/raw/groundsource/` from the Zenodo record, then `python src/labels.py` | downloaded |
| [geoBoundaries GHA ADM1](https://www.geoboundaries.org/api/current/gbOpen/GHA/ADM1/) | 16 region polygons | CC BY-SA 2.0 (from OSM; verified via API 2026-11-15) | boundaryID GHA-ADM1-69750345, 2021 boundaries, build Dec 12 2023; pulled 2026-11-22 | `python src/regions.py` | downloaded |
| CHIRPS daily | rain features (W02) | v2 public domain · v3 CC BY 4.0 (re-check on the CHC page) | | Earth Engine `UCSB-CHG/CHIRPS/DAILY` (v2; ID checked 2026-11-22, data 1981-01-01 to 2026-09-30) or the CHC server for v3. **v2 stops on 31 Dec 2026** | `python src/weather.py`; pulled 2026-11-22 |
| ERA5-Land daily | soil moisture (W02) | Copernicus licence, attribution | | Earth Engine `ECMWF/ERA5_LAND/DAILY_AGGR` (ID verified), band `volumetric_soil_water_layer_1` | `python src/weather.py`; pulled 2026-11-22 |
| Copernicus DEM, HydroSHEDS, JRC GSW, GHSL, WorldPop | static features (W03) | see each knowledge note | | Earth Engine | |
| Global Flood Database | label audit (W04) | CC BY-NC 4.0 | | Earth Engine `GLOBAL_FLOOD_DB/MODIS_EVENTS/V1` (ID verified; 913 events 2000–2018) | |

## Columns
Each column, its unit, and how it's computed without seeing the future (decision 0003). Add a row whenever you add a column.

| Column | File | Unit | Computed from | Made by |
|---|---|---|---|---|
| `region_id` | all | ISO 3166-2:GH code | geoBoundaries `shapeISO` | W01 |
| `week_start` | all | date (Monday) | | W01 |
| `flood` | labels | 0/1 | ≥1 Groundsource event whose polygon centroid is in the region and whose start date is in that week (decision 0007) | W01 |
| `n_events` | labels | count | number of such events (one storm can produce many) | W01 |
| `rain_1d_mm`, `rain_3d_mm`, `rain_7d_mm`, `rain_14d_mm`, `rain_30d_mm` | weather | mm | sum of region-mean CHIRPS daily rain over the k days **before** `week_start` | W02 |
| `rain_max1d_7d_mm` | weather | mm | wettest single day in the 7 days before `week_start` | W02 |
| `soil_moisture` | weather | m³/m³ | mean ERA5-Land top-layer (0–7 cm) volumetric soil water over the 7 days before `week_start` | W02 |
| `rain_thisweek_mm` | weather_forecast_experiment | mm | rain over `week_start` to +6 days. **Uses the future: forecast experiment only, never in the main model** | W02 |
| `region_name`, `month` | table | text, 1–12 | lookup from `region_id`; month of `week_start` | W05 |
| `floods_prev_4w` | table | count | `flood` summed over the 4 weeks before `week_start` (shift 1, never the current week) | W05 |

## Synthetic stand-in
`python src/synthetic.py` writes `data/processed/table_synthetic.parquet` (fake numbers, real shape). Use it to build code, and never to report results.
