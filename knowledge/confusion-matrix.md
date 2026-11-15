---
summary: A confusion matrix counts true/false positives and negatives; most classification metrics come from it.
type: concept
tags: [metrics, evaluation, classification]
sources: [lec5 slides, general ML knowledge]
---
# Confusion matrix

For a binary classifier at a fixed threshold, every prediction lands in one of four boxes:

| | predicted flood | predicted no flood |
|---|---|---|
| **actual flood** | true positive (TP) | false negative (FN) – a miss |
| **actual no flood** | false positive (FP) – a false alarm | true negative (TN) |

Made-up example, 1,000 region-weeks with 40 floods. The model raises 60 alerts, 30 of them real:
- TP = 30, FN = 10, FP = 30, TN = 930.

From these four numbers:
- accuracy = (TP + TN) / all = 960/1000 = 96%;
- recall = TP / (TP + FN) = 30/40 = 75%;
- precision = TP / (TP + FP) = 30/60 = 50%;
- false positive rate = FP / (FP + TN) = 30/960 ≈ 3%.

The matrix changes when you move the threshold: a lower threshold moves cases from FN to TP but also from TN to FP.

Always show the matrix (or its counts) next to any single-number metric. It makes the trade-off concrete for non-technical readers: "we caught 30 of 40 floods and raised 30 false alarms".

The lecture slides list accuracy, precision, recall, F1 and ROC-AUC but do not draw the matrix; this note fills that in.

## For the capstone
Show the 2024–2025 confusion matrix at the frozen threshold, per region if possible, in both the report and the dashboard.

## Related
- [Precision and recall](precision-and-recall.md)
- [Accuracy misleads on imbalanced data](accuracy-misleads-on-imbalanced-data.md)
- [Choosing a classification threshold](classification-threshold.md)
