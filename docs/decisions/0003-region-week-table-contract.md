---
id: 0003
status: Proposed
date: 2026-11-15
owner: Joseph (proposed) · W01 owner to confirm
issue: "W01"
---
# 0003 · The shared contract: one row per region per week

## Context
Labels (W01), weather (W02), land and terrain (W03), models (W05/W06) and the dashboard (W10) are separate workstreams. If each one waits for the previous one, nobody starts until the data joins are done, and joining is the biggest job in the project. A fixed table shape lets every stream build now.

## Decision
**Unit:** region × week.
- **Regions:** the 16 regions in geoBoundaries `GHA` `ADM1` (gbOpen, <https://www.geoboundaries.org/api/current/gbOpen/GHA/ADM1/>). Key `region_id` = geoBoundaries `shapeISO` (e.g. `GH-AA`; all 16 present and verified 2026-11-15; licence CC BY-SA 2.0); `region_name` for display.
- **Weeks:** Monday to Sunday. Key `week_start` = the Monday (a date). The forecast is issued at the start of Monday, so it may use only data from before `week_start` (see [0004](0004-temporal-split.md)).
- **Years:** 2015-01-05 (the first Monday) to 2025-12-29.

**Files** (in `data/processed/`, never committed). Each is Parquet keyed on `region_id`, `week_start`:

| File | Made by | Columns besides the keys |
|---|---|---|
| `labels.parquet` | W01 | `flood` (0/1: ≥1 Groundsource event in the region that week), `n_events` |
| `weather.parquet` | W02 | `rain_1d_mm`, `rain_3d_mm`, `rain_7d_mm`, `rain_14d_mm`, `rain_30d_mm`, `soil_moisture`, … (all computed from days **before** `week_start`) |
| `static.parquet` | W03 | keyed on `region_id` (+ `year` for features that change over time): `elev_mean_m`, `slope_mean`, `river_density`, `builtup_share`, `pop_density`, … |
| `table.parquet` | W05 `src/build_table.py` | labels ⋈ weather ⋈ static, plus `region_name`, `month`, `floods_prev_4w` |

**While a real file is missing**, `python src/synthetic.py` writes a fake `table_synthetic.parquet` with the same keys and columns (9,184 rows, the real count), so that models, the evaluation harness and the dashboard can be built and tested now.

**Adding a column:** whoever adds one lists it in `data/README.md` (name, unit, source, and how it's computed without seeing the future). Keys and the label never change without a new decision.

## Why
- Region-week gives a 6.4% positive rate (585 of 9,184 rows, 2015–2025). That's workable.
- Region-week also matches the decision: prepare staff and supplies for the week.
- Region-day (1.3%) is too rare. District level is noisier still.

## Open choices for W01 to test and record
- **How an event is assigned to a region:** its polygon centroid (as in the options report) or every region its polygon touches.
- **The event date:** its start date, or any day it covers.
- **Very large polygons** (about 11% exceed 500 km²): keep them or drop them.

## Consequences
- District-level prediction is out of scope until region level works.
- A week counts as positive once, however many events it has, so one storm doesn't count many times.
