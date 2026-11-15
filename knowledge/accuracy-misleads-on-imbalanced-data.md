---
summary: When one class is rare, a useless model can still score high accuracy.
type: concept
tags: [evaluation, imbalance, metrics, lecturer-emphasis]
sources: [lecture-11 recording, lecture-09 recording, lec5 slides]
---
# Accuracy misleads on imbalanced data

If only 10 in 1,000 transactions are fraud, a model that always says "not fraud" is 99% accurate. It has learned nothing. The lecturer made the point that even an *untrained* network with random weights can show high accuracy on such data, simply because one class outweighs the other.

So on imbalanced data:

- compare against the "always majority class" baseline;
- report metrics that focus on the rare class: recall (how many real positives you caught), precision (how many alarms were real), F1, PR-AUC;
- look at the confusion matrix, not one number.

Binary cross-entropy, the usual training loss, can also drift toward the majority class on imbalanced data. Class weights or resampling are common fixes.

The supervised-learning survey slides list this as a top pitfall in two words: "accuracy lies". Their fixes: F1 or PR-AUC, class weights, resampling.

Class imbalance and rare events is one of the four literature-review themes the lecturer set (topics include threshold tuning vs resampling, and imbalance in disease outbreak / early warning prediction).

## For the capstone
Flood region-weeks are rare. "Never flood" will have very high accuracy and zero value to NADMO. Lead with recall, precision and PR-AUC against that baseline and the rainfall-threshold baseline.

## Related
- [Choosing a classification threshold](classification-threshold.md)
- [Binary cross-entropy](binary-cross-entropy.md)
- [Beat a naive baseline first](beat-a-naive-baseline-first.md)
- [Class imbalance](class-imbalance.md)
- [Zero-one loss](zero-one-loss.md)
