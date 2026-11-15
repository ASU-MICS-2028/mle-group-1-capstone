---
summary: Mitigations act before (reweighting), during (constraints) or after training (group thresholds)
type: concept
tags: [fairness, mitigation]
sources: [Barocas, Hardt & Narayanan, FML ch. 3, prosit-2 fairness_reading.md, Flood options report §7]
---
# Fairness mitigation options

Three families:
- **Pre-processing:** reweight or resample training rows so groups and outcomes are better balanced, or fix the labels (e.g. audit and correct a sample).
- **In-processing:** add a fairness constraint or penalty to the training objective.
- **Post-processing:** change decisions after scoring, typically **group-specific thresholds** chosen to equalise recall and/or false-positive rate.

Whichever is used, report **before and after**: the fairness metric, overall PR-AUC, expected cost or alert count, and per-group alert rates. LO5 asks for at least one concrete mitigation.

## For the capstone
Mitigations proposed in the options report:
1. **Audit coverage** against satellite records (Global Flood Database) to measure under-reporting by region.
2. **Per-region alert thresholds** so rural regions are not permanently below the cut-off.
3. **Show uncertainty** on the dashboard.
4. **Write out prohibited uses** (e.g. a low score is not "safe"; not for eviction or enforcement maps).
Per-region thresholds are the simplest to evaluate with before/after numbers.

## Related
- [Fairness impossibility](fairness-impossibility.md)
- [Flood ethics concerns](flood-ethics-concerns.md)
- [Cost-based threshold derivation](cost-threshold-derivation.md)
- [Global Flood Database](global-flood-database.md)
