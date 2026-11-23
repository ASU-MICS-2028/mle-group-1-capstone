---
id: 0004
date: 2026-11-23
issue: "#6"
owner: Joseph
---
# 0004 · Table builder, evaluation harness and three baselines

## What we did
- `src/build_table.py` joins labels and weather (static is skipped until W03 lands) and adds `region_name`, `month` and `floods_prev_4w` (floods in the 4 weeks before, never the current week).
- `src/evaluate.py` holds the split from decision 0004, `score()` (PR-AUC, ROC-AUC, recall@top-3 per week, Brier, 95% CIs from resampling weeks), `rolling_origin()` (2018–2023, asserts it never reaches the test years), `leave_one_region_out()` and `without_akosombo()`. Self-checks: the splits are disjoint and ordered, a perfect predictor scores 1.0, a random predictor's CI covers 0.5 in most tries, and the test years are untouched.
- `src/baselines.py` runs the seasonal rate, the rain rule and the logistic regression. Results are scored on 2023 only; **the 2024–25 test set has not been touched.**
- `src/synthetic.py` now has `rain_max1d_7d_mm`, so it matches the real columns.

## Files
- `src/build_table.py`, `src/evaluate.py`, `src/baselines.py`, `src/synthetic.py`, `data/README.md`
- `learnings/tables/baselines*.csv`, two learning notes

## AI use
| Part | Tool | What the AI did | What the human checked |
|---|---|---|---|
| Harness, table builder, baselines | Claude Code | Wrote and ran the code; fixed a flaky self-check (a single random run can miss 0.5 by chance) | Joseph: rerun `python src/build_table.py && python src/evaluate.py && python src/baselines.py`; check a metric by hand |
| Interpretation | Claude Code | Drafted the learning notes from the saved tables | Joseph and the team: agree with the reading before the mid-check |

## Decisions / learnings this produced
- learnings/where-and-when-beat-rain-alone.md · learnings/recall-at-k-has-a-chance-level.md
