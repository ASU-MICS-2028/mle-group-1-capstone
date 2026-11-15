---
workstream: W06
issue: "#TBD"
owner: unassigned (suggested role: Modelling lead)
status: Not started
needs: W05 harness (explicit). W01 + W02 real data for final numbers; can start tuning code on the synthetic table now.
due: 2026-11-27
---
# W06 · Compare at least 4 models

## Goal
Compare logistic regression (plain, and with L1/L2), random forest, LightGBM and SVM against the baselines. Use the W05 harness, tune on 2023, and calibrate. The brief needs at least 4 models by Week 12.

## Steps
- [ ] One notebook or script per model family, all through `src/evaluate.py`.
- [ ] Use class weights against resampling, and compare how calibrated each is ([Prosit 2 lesson](../learnings/README.md)).
- [ ] Put all results in one table with CIs. Pick the winner on the 2023 tune set and record the choice as a decision.
- [ ] Choose the alert budget and threshold with the cost of errors ([knowledge/flood-cost-of-errors.md](../knowledge/flood-cost-of-errors.md)), and record that as a decision.
- [ ] Run the test on 2024–2025 **once**, at the end, and save it.
- [ ] Diagnostics: calibration curve, PR curve, feature importance or SHAP, errors by region and by season.

## Read first
The supervised-learning notes in [knowledge/README.md](../knowledge/README.md).
