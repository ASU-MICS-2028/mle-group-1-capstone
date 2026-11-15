---
summary: RMSE and MAE report regression error in the target's own units; RMSE weights big errors more.
type: concept
tags: [metrics, regression]
sources: [lecture-05 recording, lec5 slides, lecture-11 recording, neural networks slides]
---
# RMSE and MAE

Two readable regression metrics, both in the same units as the target:

- **RMSE (root mean squared error)** = √MSE. Square the errors, average them, take the square root.
- **MAE (mean absolute error)** = average of |y − ŷ|.

Example with three predictions of rainfall that are off by 1, 1 and 10 mm:
- MAE = (1 + 1 + 10) / 3 = 4 mm;
- RMSE = √((1 + 1 + 100) / 3) ≈ 5.8 mm.

RMSE is bigger because squaring makes the one large miss count more. So:
- use **RMSE** when big misses are especially bad;
- use **MAE** when you want a typical error that outliers do not dominate.

The lecturer's point was that the evaluation metric should be human-readable and in the target's units. MSE is fine to train on, but report RMSE or MAE. The slides also list R² (share of variance explained) for regression.

## For the capstone
Our main task is classification, so these appear only if we add a side regression (for example, predicting rainfall totals or flood counts) or check feature reconstructions.

**As a training loss (lecture 11).** MSE is smooth and differentiable everywhere, which suits gradient descent; MAE has a kink at zero error. MSE "shouts" at outliers because it squares errors; MAE treats errors proportionally and is robust to outliers. The lecturer's example: predicted electricity demand 80 kW vs actual 100 kW. MAE reports 20 kW directly, in the same unit, which is easy to read. Choose MAE when errors should count at face value or the data has outliers; choose MSE when large errors are especially bad.

## Related
- [Mean squared error](mean-squared-error.md)
- [Training loss vs evaluation metric](training-loss-vs-evaluation-metric.md)
- [Regression vs classification](regression-vs-classification.md)
