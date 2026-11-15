---
summary: MSE averages the squared gaps between predictions and true values; squaring punishes big errors more.
type: concept
tags: [loss, regression, metrics]
sources: [lecture-05 recording, lecture-06 recording, lec4 slides]
---
# Mean squared error (MSE)

MSE is the usual training loss for regression:

MSE = (1/m) Σ (yᵢ − ŷᵢ)²

For each of the m examples, take the gap between the true value y and the prediction ŷ, square it, then average.

**Why square instead of taking the absolute value?** A student asked this in class. Both are valid. Squaring:
- makes every error positive;
- punishes big errors much more than small ones. True value 3, prediction 5: absolute error 2, squared error 4. An error of 10 becomes 100;
- gives a smooth, bowl-shaped (convex) function with one minimum, which is easy to solve with calculus or gradient descent.

The downside of that heavy penalty is that a few extreme values (outliers) can pull the whole fit towards them.

MSE's units are squared (cedis², mm²), which nobody can read. That is why we usually report its square root (RMSE) or MAE instead.

**Zero training MSE is not the goal.** With few examples or a too-flexible model, you can drive training error to zero by memorising noise. That is overfitting, and it shows up as poor test error.

## Related
- [RMSE and MAE](rmse-and-mae.md)
- [Linear regression](linear-regression.md)
- [Overfitting](overfitting.md)
- [Training loss vs evaluation metric](training-loss-vs-evaluation-metric.md)
