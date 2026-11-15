---
summary: PR-AUC summarises the precision-recall trade-off over all thresholds; the honest ranking metric for rare events.
type: concept
tags: [metrics, evaluation, imbalance]
sources: [lec5 slides]
---
# Precision-recall curve and PR-AUC

The **precision-recall (PR) curve** plots precision (y) against recall (x) for every threshold. **PR-AUC** is the area under it. scikit-learn's `average_precision_score` is the usual way to compute it.

Why it suits rare events: neither precision nor recall uses true negatives. The thousands of easy "no flood" weeks cannot inflate the score the way they inflate accuracy or ROC-AUC.

**Its baseline is the positive rate, not 0.5.** A random model has precision equal to the share of positives at every recall. If 4% of region-weeks are floods, random PR-AUC ≈ 0.04. So a PR-AUC of 0.30 is modest in absolute terms but more than seven times better than chance. Always state the base rate next to it.

The survey slides name PR-AUC (with F1) as the fix when "accuracy lies" on imbalanced data.

Things to watch:
- PR-AUC changes if the positive rate changes, so compare models only on the same test period;
- with few positives it is noisy; a bootstrap confidence interval helps;
- it measures ranking, not calibration.

## For the capstone
Our headline metric on 2023 (model choice) and 2024–2025 (final report). Report it with the base flood rate, the "never flood" and rainfall-rule baselines, and a bootstrap interval.

## Related
- [ROC curve and ROC-AUC](roc-auc.md)
- [Precision and recall](precision-and-recall.md)
- [Accuracy misleads on imbalanced data](accuracy-misleads-on-imbalanced-data.md)
- [Class imbalance](class-imbalance.md)
