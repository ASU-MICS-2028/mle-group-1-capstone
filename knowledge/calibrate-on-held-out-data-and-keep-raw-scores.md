---
summary: Fit probability calibration on a separate held-out set, and store the uncalibrated scores too.
type: lesson
tags: [calibration, evaluation, prosit-2, leakage]
sources: [lab-session-1 discussion]
---
# Calibrate on held-out data and keep raw scores

A model is **calibrated** when its probabilities mean what they say: of all cases given 10%, about 10% really are positive.

What went wrong in Prosit 2: after calibration, the model predicted an average default rate of 5.25% when the actual rate was 9.41%. It underestimated risk. The team traced this to how calibration was done. Two lessons came out of the review:

1. **Fit the calibrator on its own held-out data.** A calibrator (Platt scaling or isotonic regression) is itself a fitted model. Fitting it on the training data, or tuning it on the final test set, gives misleading probabilities or a leaked test score. Use a separate calibration/validation split.
2. **Store the raw (uncalibrated) probabilities.** We had not saved them, so we could not compare before and after or redo calibration cheaply.

Quick check: compare mean predicted probability with the actual positive rate, and draw a reliability curve, on held-out data.

## For the capstone
Fit any calibration on the 2023 tuning year, never on 2024–2025. Save raw and calibrated scores per region-week. Calibration matters because NADMO will read the dashboard's percentages literally.

## Related
- [Class weights and calibration derivation](class-weights-calibration-derivation.md)
- [Cost-based threshold derivation](cost-threshold-derivation.md)
- [Train, validation and test sets](train-validation-test-split.md)
