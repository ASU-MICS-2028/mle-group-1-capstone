---
id: 0005
date: 2026-11-28
issue: "#3"
owner: Joseph
---
# 0005 · Forecast experiment: what a perfect rain forecast would add

## What we did
- `src/forecast_experiment.py` scores two models with and without `rain_thisweek_mm`, the rain that fell during the predicted week (decision 0004 keeps it out of the main model). The models are logistic regression on rain and soil moisture, and a random forest on rain, region, month and floods in the previous 4 weeks.
- Each pair is scored on 2023, on 2023 without the Akosombo spill weeks, and on the rolling origin 2018–2023. The gain has a 95% range from resampling weeks, using the same resamples for both scores. **The 2024–25 test set was not touched.**
- Self-check: a fake feature equal to the label must give PR-AUC above 0.95 and a clearly positive gain.

## Result
PR-AUC on 2023 rises from 0.18 to 0.24 (logistic) and from 0.28 to 0.32 (forest). Both gains have 95% ranges that include zero, and the gain is positive in all six rolling years. See [the learning note](../../learnings/perfect-rain-forecast-adds-little.md).

## Files
- `src/forecast_experiment.py`
- `learnings/tables/forecast_experiment.csv`, `learnings/tables/forecast_experiment_rolling_origin.csv`
- `learnings/perfect-rain-forecast-adds-little.md`, `learnings/results_index.md`, `plans/W02-weather-features.md`

## AI use
| Part | Tool | What the AI did | What the human checked |
|---|---|---|---|
| Experiment code | Claude Code | Designed the paired comparison, wrote and ran the script and its self-check | Joseph: rerun `python src/forecast_experiment.py` and compare with the saved CSV |
| Interpretation | Claude Code | Drafted the learning note from the saved tables | Joseph and the team: agree with the reading before it goes in the report |

## Decisions / learnings this produced
- learnings/perfect-rain-forecast-adds-little.md
