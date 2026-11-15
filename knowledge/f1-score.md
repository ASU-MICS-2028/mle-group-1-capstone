---
summary: F1 is the harmonic mean of precision and recall; high only when both are high.
type: concept
tags: [metrics, evaluation]
sources: [lec5 slides]
---
# F1 score

F1 combines precision (P) and recall (R) into one number:

F1 = 2 · P · R / (P + R)

It is the **harmonic mean**, which is dragged down by whichever of the two is smaller. Examples:
- P = 0.5, R = 0.5 → F1 = 0.5;
- P = 0.9, R = 0.1 → F1 = 0.18 (the plain average would flatter it at 0.5);
- predicting "positive" for everything gives R = 1 but tiny P, so F1 stays low.

Good for: a single summary at one threshold that, unlike accuracy, cannot be gamed by predicting the majority class.

Limits:
- it depends on the threshold you picked;
- it weights precision and recall equally. If misses cost more than false alarms, use F-beta with β > 1 (F2 counts recall twice as much), or better, an explicit cost;
- it ignores true negatives entirely.

## For the capstone
Report F1 (and F2, since misses matter more) at the frozen threshold, alongside the threshold-free PR-AUC.

## Related
- [Precision and recall](precision-and-recall.md)
- [Precision-recall AUC](precision-recall-auc.md)
