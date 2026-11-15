---
summary: ROC-AUC is the chance a random positive is scored above a random negative; it flatters rare-class models.
type: concept
tags: [metrics, evaluation, classification]
sources: [lec5 slides, lecture-07 recording]
---
# ROC curve and ROC-AUC

The **ROC curve** plots, for every possible threshold:
- y-axis: true positive rate (recall) = TP / (TP + FN);
- x-axis: false positive rate = FP / (FP + TN).

A threshold of 1 sits at (0, 0) (no alerts); a threshold of 0 sits at (1, 1) (alert everything). A good model's curve hugs the top-left corner.

**ROC-AUC** is the area under that curve. It has a neat meaning: the probability that a randomly picked positive gets a higher score than a randomly picked negative. 0.5 = coin flip, 1.0 = perfect ranking.

Good points: does not depend on a threshold; measures ranking quality.

The catch with rare positives: the false positive rate divides by the huge number of negatives. Example: 40 floods and 10,000 non-flood weeks. 200 false alarms is only a 2% FPR, so the ROC looks excellent, even though 200 false alarms against at most 40 true alerts means most alerts are wrong. ROC-AUC can be high while precision is poor.

So for imbalanced problems, report PR-AUC as the main ranking metric and ROC-AUC as a secondary one.

ROC-AUC also says nothing about whether the scores are good probabilities (calibration).

## Related
- [Precision-recall AUC](precision-recall-auc.md)
- [Precision and recall](precision-and-recall.md)
- [Probability calibration](probability-calibration.md)
