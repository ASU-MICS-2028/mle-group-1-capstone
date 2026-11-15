---
summary: A model is calibrated when its predicted probabilities match how often the event really happens.
type: concept
tags: [calibration, evaluation, probability]
sources: [lec5 slides, MIT 6.390 ch4, general ML knowledge]
---
# Probability calibration

A classifier is **calibrated** if its probabilities can be taken literally. Of all the region-weeks it gives "20% flood", about 20% should really flood.

Ranking and calibration are different. A model can rank perfectly (every flood scored above every non-flood, ROC-AUC = 1) while saying 0.9 for events that happen 30% of the time. AUC metrics do not check this.

Which models tend to be off (from the survey slides and practice):
- **naive Bayes:** pushed towards 0 and 1 by the independence assumption;
- **SVM:** outputs a distance, not a probability at all;
- **random forest:** vote fractions are squeezed away from 0 and 1;
- **boosting:** can be over-confident;
- **any model trained with class weights or resampling:** probabilities are shifted upwards for the rare class.
Plain logistic regression trained on the real class mix is often close to calibrated.

How to check: a **reliability curve** (bin predictions, plot mean predicted vs observed rate; a calibrated model sits on the diagonal), the mean prediction vs the actual base rate, and the **Brier score** (mean squared error of the probabilities, lower is better).

How to fix: fit a small second model on held-out data that maps raw scores to probabilities. **Platt scaling** fits a sigmoid (good with little data); **isotonic regression** fits a free-form increasing step curve (needs more data). In scikit-learn: `CalibratedClassifierCV`.

## For the capstone
Needed if the dashboard shows percentages to NADMO. Calibrate on 2023 only and report Brier score and a reliability plot on 2024–2025.

## Related
- [Calibrate on held-out data and keep raw scores](calibrate-on-held-out-data-and-keep-raw-scores.md)
- [Class weights and calibration derivation](class-weights-calibration-derivation.md)
- [Choosing a classification threshold](classification-threshold.md)
- [ROC curve and ROC-AUC](roc-auc.md)
