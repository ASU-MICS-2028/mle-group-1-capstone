---
id: 0002
date: 2026-11-22
issue: "#3"
owner: Joseph
---
# 0002 · Region loader and weather features from Earth Engine

## What we did
- `src/regions.py` downloads the 16 geoBoundaries regions and checks their codes against the contract (decision 0003).
- `src/weather.py` pulls region-mean daily CHIRPS rain and ERA5-Land soil moisture (2014-12-01 to 2026-01-04), caches each quarter, and builds `weather.parquet`: 9,184 rows, 7 features. Every feature uses only days before `week_start`. An `assert` checks this by recomputing 200 random rows from the daily data.
- `rain_thisweek_mm` (uses the target week) goes to a separate file, `weather_forecast_experiment.parquet`, so it can't enter the main model by accident.
- Sanity check: the monthly rain figure shows two rainy seasons in the south and one in the north, as expected.

## Files
- `src/regions.py`, `src/weather.py`, `requirements.txt`, `data/README.md`, `.gitignore`
- `learnings/figures/w02_monthly_rain_by_region.png`, `learnings/tables/w02_monthly_rain_by_region.csv`

## AI use
| Part | Tool | What the AI did | What the human checked |
|---|---|---|---|
| Earth Engine account and project | none | none | Joseph registered the project (noncommercial, Community tier) and authenticated |
| `regions.py`, `weather.py` | Claude Code | Wrote both scripts, ran them, found and fixed the chunking bug | Joseph: rerun `python src/weather.py` from a fresh clone; spot-check one region-week by hand |
| Sanity figure | Claude Code | Made the plot and the table (aggregates only, no raw rows) | Joseph: does the seasonality match what you know of Ghana? |

## Decisions / learnings this produced
- learnings/assert-full-coverage-after-chunked-downloads.md
