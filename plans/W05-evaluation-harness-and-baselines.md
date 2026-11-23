---
workstream: W05
issue: "#6"
owner: Joseph (@josetseph)
status: In review
needs: none (builds on the synthetic table; switches to the real one when W01/W02 land)
due: 2026-11-19
---
# W05 · Table builder, evaluation harness and baselines

## Goal
One shared piece of code that every model goes through. It does three things:
- builds the table;
- splits it by time;
- scores a model the same way every time.

It should also report two baselines.

## Outputs
- **`src/build_table.py`:** joins labels, weather and static data into `table.parquet` ([decision 0003](../docs/decisions/0003-region-week-table-contract.md)). Each input may be missing, in which case it's skipped with a warning.
- **`src/evaluate.py`:**
  - `split(df)` returns train / tune / test as in [decision 0004](../docs/decisions/0004-temporal-split.md);
  - `score(y, p, weeks)` returns PR-AUC, ROC-AUC, recall@top-k regions per week, Brier score, and bootstrap CIs (resampling weeks);
  - `rolling_origin(...)`;
  - `leave_one_region_out(...)`.
- **Self-checks** at the bottom (`python src/evaluate.py`): there's no overlap between splits, the test set is untouched, and a perfect predictor scores 1.0.
- **Baselines:**
  1. the seasonal rate (region × month frequency from train);
  2. a rainfall threshold rule tuned on 2023;
  3. logistic regression on the rain features.

  Results go in `learnings/tables/baselines.csv` and are indexed.

## Steps
- [x] Develop against `python src/synthetic.py` output.
- [x] Write the `evaluate.py` functions and the self-checks.
- [x] Write `build_table.py`.
- [x] Run the baselines on real data as soon as W01 and W02 land. This is the mid-check deliverable.

## Read first
- [knowledge/temporal-split.md](../knowledge/temporal-split.md)
- [knowledge/precision-recall-auc.md](../knowledge/precision-recall-auc.md)
- [knowledge/bootstrap-confidence-interval.md](../knowledge/bootstrap-confidence-interval.md)
- [learnings/README.md](../learnings/README.md), for the Prosit 2 lessons on calibration and the noise floor
