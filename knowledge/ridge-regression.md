---
summary: Ridge adds a penalty on squared weights to the loss, shrinking them and stabilising the fit.
type: concept
tags: [regularisation, linear-models]
sources: [MIT 6.390 ch2, lecture-06 recording]
---
# Ridge regression (L2 regularisation)

Ridge regression is linear regression with an extra penalty for large weights:

loss = MSE + λ · (θ₁² + θ₂² + … + θ_d²)

- λ ≥ 0 is a hyperparameter. λ = 0 is plain least squares. Bigger λ pushes all weights towards zero.
- The intercept θ₀ is normally not penalised.

**Why do this?**
1. **Overfitting:** small weights mean a smoother, simpler model that chases noise less.
2. **Correlated features:** if two features nearly copy each other (say, rainfall today and 3-day rainfall), plain least squares has no single best answer and gives huge, unstable weights of opposite signs. The penalty picks a stable compromise. In the closed form it adds λ to the diagonal of XᵀX, which makes it always invertible when λ > 0.

Ridge shrinks weights but almost never makes them exactly zero, so all features stay in the model.

**Scale first.** The penalty treats every weight the same, so features must be on comparable scales (standardised). Otherwise a feature measured in large units gets an unfairly small weight and little penalty.

Choose λ by cross-validation. The same L2 penalty is the default in scikit-learn's logistic regression, where `C` is roughly 1/λ (small C = strong penalty).

## For the capstone
Our rainfall features (1-day, 3-day, 7-day totals) are strongly correlated, so L2-regularised logistic regression is the sensible default.

## Related
- [Ridge regression derivation](ridge-regression-derivation.md)
- [Lasso regression](lasso-regression.md)
- [Logistic regression needs regularisation](logistic-regression-needs-regularisation.md)
- [Bias-variance trade-off](bias-variance-tradeoff.md)
