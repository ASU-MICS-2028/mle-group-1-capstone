---
summary: Lasso penalises the absolute size of weights and can set some exactly to zero, selecting features.
type: concept
tags: [regularisation, linear-models, feature-selection]
sources: [intro slides, general ML knowledge]
---
# Lasso regression (L1 regularisation)

Lasso is like ridge, but the penalty uses absolute values instead of squares:

loss = MSE + λ · (|θ₁| + |θ₂| + … + |θ_d|)

The key difference: lasso tends to push some weights to **exactly zero**. Those features drop out of the model. So lasso does feature selection as part of training.

Rough intuition: with squares, a weight of 0.01 costs almost nothing (0.0001), so ridge happily keeps many tiny weights. With absolute values, 0.01 still costs 0.01, so lasso prefers to zero it out.

Comparison:
- **Ridge (L2):** keeps all features, shares weight among correlated ones. Good when many features each matter a bit.
- **Lasso (L1):** sparse model, easier to read. With a group of correlated features it tends to pick one fairly arbitrarily.
- **Elastic net:** mixes both penalties.

As with ridge: standardise features first, do not penalise the intercept, and pick λ by cross-validation. In scikit-learn's logistic regression use `penalty="l1"` with a solver that supports it (for example `liblinear` or `saga`).

Correction: the later lectures covered only ridge (L2), but the course's introductory slide deck does name both L1/lasso (can push weights to exactly zero, so it selects features) and L2/ridge (shrinks all weights). The formulas and tips here are standard textbook material.

## For the capstone
An L1 logistic regression is a quick way to see which of our many rainfall and soil-moisture lags actually carry signal.

## Related
- [Ridge regression](ridge-regression.md)
- [Feature importance](feature-importance.md)
