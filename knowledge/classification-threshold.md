---
summary: A probability becomes a yes/no via a threshold; lower it when misses are costly, raise it when false alarms are.
type: concept
tags: [classification, threshold, decision, lecturer-emphasis]
sources: [lecture-10 recording, neural networks slides, lecture-06 recording, MIT 6.390 ch4]
---
# Choosing a classification threshold

A sigmoid output (or any classifier's probability) is a number between 0 and 1. To act, you need a yes or no. The **threshold** does that: predict 1 if the probability is at or above it, else 0. The default is 0.5, but the lecturer spent time on when to move it.

**Lower threshold** when missing a positive is very costly. Cancer screening: if the model sees even a 30% chance of cancer, flag the image for a doctor. You accept more false alarms to miss fewer real cases.

**Higher threshold** when a false alarm is very costly. Fraud flagging (the transcript garbles the word): before blocking a customer's transaction, the model should be, say, 70% sure. Otherwise honest customers get blocked all the time.

The transcript is muddled on the numbers here (it says "a lower threshold, say 0.7, which is 30%"). The intended meaning is a threshold of about 0.3 for cancer and 0.7 for fraud.

In the linear-classifier lecture the threshold was hidden inside sign(score): a score of 0 is the same as probability 0.5. The MIT notes frame moving it as decision theory: if one error type is much worse, shift the threshold away from it.

The threshold is a **decision**, not part of the model. Choose it on validation data, never on the test set.

## For the capstone
A missed flood is worse than a wasted readiness check, so our alert threshold will sit well below 0.5. Choose it on 2023, freeze it, then test on 2024–2025.

## Related
- [Cost-based threshold derivation](cost-threshold-derivation.md)
- [Output-layer activation](output-layer-activation.md)
- [Accuracy misleads on imbalanced data](accuracy-misleads-on-imbalanced-data.md)
- [Logistic regression](logistic-regression.md)
- [Probability calibration](probability-calibration.md)
- [Precision and recall](precision-and-recall.md)
