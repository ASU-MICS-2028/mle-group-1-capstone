---
summary: When one class is rare, use class weights, resampling or threshold tuning, and rare-class metrics.
type: concept
tags: [imbalance, classification, evaluation]
sources: [lec5 slides, lecture-07 recording]
---
# Class imbalance and what to do about it

A dataset is **imbalanced** when one class is much rarer than the other (the lecturer gave 80/20, and about 10% anomalies in anomaly detection, as examples). Most models then lean towards the common class, and accuracy hides it.

Main remedies, roughly in order of simplicity:
1. **Pick the right metrics:** recall, precision, F1, PR-AUC, the confusion matrix. Not accuracy.
2. **Move the threshold:** keep the model, but alert at a lower probability than 0.5. Often the simplest and most effective fix.
3. **Class weights:** make mistakes on the rare class cost more in the loss (`class_weight="balanced"` in scikit-learn, `scale_pos_weight` in LightGBM/XGBoost). Side effect: probabilities get shifted, so recalibrate.
4. **Resampling:** undersample the common class or oversample the rare one (randomly, or with synthetic points such as SMOTE). Only ever resample the training data inside each fold, never the validation or test data.

Model notes from the slides: decision tree splits do not need equal class counts (a student asked; the aim is separating classes), but kNN struggles because a rare point's neighbours are mostly from the big class.

Always compare with the "always predict the common class" baseline.

## For the capstone
Flood region-weeks are a small fraction of all region-weeks. Our plan: threshold tuning on 2023 as the main tool, class weights as an option to test, recalibrate afterwards, and lead with PR-AUC and recall.

## Related
- [Accuracy misleads on imbalanced data](accuracy-misleads-on-imbalanced-data.md)
- [Choosing a classification threshold](classification-threshold.md)
- [Precision-recall AUC](precision-recall-auc.md)
- [Probability calibration](probability-calibration.md)
