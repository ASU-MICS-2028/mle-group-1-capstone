---
summary: Precision asks how many alarms were real; recall asks how many real cases were caught.
type: concept
tags: [metrics, evaluation, classification]
sources: [lec5 slides, lecture-07 recording]
---
# Precision and recall

Both focus on the positive (rare, important) class.

- **Precision** = TP / (TP + FP). Of all the alerts raised, how many were real? "When I shout flood, am I right?"
- **Recall** (also called sensitivity or true positive rate) = TP / (TP + FN). Of all the real floods, how many did we catch? "Did I miss any?"

They pull against each other. Lowering the threshold raises more alerts: recall goes up, precision usually goes down. Raising it does the reverse. A model that alerts every week has 100% recall and terrible precision.

Which matters more depends on the cost of each mistake:
- missing a real case is worse (disease screening, flood warning) → favour recall;
- a false alarm is worse (blocking honest bank customers) → favour precision.

Neither uses true negatives, which is why they stay informative when negatives vastly outnumber positives, unlike accuracy.

The lecturer listed precision, recall, F1 and ROC as the evaluation metrics ("secondary objectives") that matter, as opposed to the training loss.

## For the capstone
For NADMO, a missed flood is worse than a wasted readiness check, so we target high recall and report the precision we pay for it. Say it in words: "catches 3 in 4 floods; about half of alerts are real".

## Related
- [Confusion matrix](confusion-matrix.md)
- [F1 score](f1-score.md)
- [Precision-recall AUC](precision-recall-auc.md)
- [Choosing a classification threshold](classification-threshold.md)
