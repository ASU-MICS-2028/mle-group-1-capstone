# Data: where it comes from (the data itself is never committed)

The repo is public, so this folder is gitignored and only this note is committed ([decision 0005](../docs/decisions/0005-public-repo-and-data-handling.md)). Anyone can rebuild every file from the instructions below.

```
data/raw/         downloads, untouched
data/interim/     per-source tables (e.g. region-mean daily rain)
data/processed/   region-week files from decision 0003 (labels, weather, static, table)
```

## Sources
Whoever adds a source fills in its row: version or date, and the fetch command or script.

| Source | Used for | Licence | Version / date pulled | How to fetch | Status |
|---|---|---|---|---|---|
| [Groundsource](https://zenodo.org/records/18647054) ([note](../knowledge/groundsource-dataset.md)) | labels (W01) | CC BY 4.0 | `groundsource_2026.parquet`, 667,122,400 bytes, md5 cd1b5de6508f7aad8e1d1d0dd4cecea6, published 2026-02-15; pulled 2026-11-22 | download into `data/raw/groundsource/` from the Zenodo record, then `python src/labels.py` | downloaded |
| [geoBoundaries GHA ADM1](https://www.geoboundaries.org/api/current/gbOpen/GHA/ADM1/) | 16 region polygons | CC BY-SA 2.0 (from OSM; verified via API 2026-11-15) | | `src/regions.py` | to download |
| CHIRPS daily | rain features (W02) | v2 public domain · v3 CC BY 4.0 (re-check on the CHC page) | | Earth Engine `UCSB-CHG/CHIRPS/DAILY` (v2; ID checked 2026-11-22, data 1981-01-01 to 2026-09-30) or the CHC server for v3. **v2 stops on 31 Dec 2026** | Earth Engine account needed |
| ERA5-Land daily | soil moisture (W02) | Copernicus licence, attribution | | Earth Engine `ECMWF/ERA5_LAND/DAILY_AGGR` (ID verified) | Earth Engine account needed |
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

## Synthetic stand-in
`python src/synthetic.py` writes `data/processed/table_synthetic.parquet` (fake numbers, real shape). Use it to build code, and never to report results.
