---
summary: In cross-validation, refit preprocessing inside each fold; scikit-learn Pipelines do this automatically.
type: procedure
tags: [leakage, cross-validation, preprocessing]
sources: [preprocessing & leakage slides]
---
# Preprocessing inside cross-validation

Cross-validation (CV) repeatedly splits the training data into "train folds" and a "validation fold". It does **not** protect you from leakage by itself.

If you scale or impute the whole training set once and then run CV, each validation fold has already influenced the statistics used on its train folds – the same contamination, one level down.

Fix: **refit every preprocessing step inside every fold**, on that fold's training part only, then apply it to its validation part.

The easy way: put preprocessing and model together in a scikit-learn `Pipeline` and pass the whole pipeline to `cross_val_score` or `GridSearchCV`. The pipeline is refitted per fold automatically.

Same rule for resampling (e.g. oversampling the rare class): do it inside the fold, on training rows only.

## For the capstone
If we use time-series CV within 2015–2022 for tuning, the scaler, imputer and any class rebalancing go inside the pipeline.

## Related
- [Split first, fit on train](split-first-fit-on-train.md)
- [K-fold cross-validation](k-fold-cross-validation.md)
- [Temporal leakage in cross-validation](temporal-leakage-in-cross-validation.md)
