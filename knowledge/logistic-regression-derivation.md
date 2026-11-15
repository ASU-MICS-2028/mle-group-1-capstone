---
summary: Linear log-odds give the sigmoid; the Bernoulli NLL is log-loss with gradient Xᵀ(p−y) and is convex
type: derivation
tags: [derivation, classification, linear-models, lo3]
sources: [ISLR 4.3 eq. 4.2–4.5, HOMLP ch 4, prosit-2 derivations.md §b.1–b.5]
---
# Logistic regression derivation

**1. Log-odds → sigmoid.** Model $\log\frac{p}{1-p}=x^T\beta=z$. Solving, $p=\frac{e^z}{1+e^z}=\sigma(z)$. A unit increase in $x_j$ multiplies the odds by $e^{\beta_j}$. Useful: $\sigma'(z)=\sigma(z)(1-\sigma(z))$.

**2. Likelihood.** $P(y_i\mid x_i)=p_i^{y_i}(1-p_i)^{1-y_i}$, so $L(\beta)=\prod_ip_i^{y_i}(1-p_i)^{1-y_i}$.

**3. Negative log-likelihood = log-loss.**
$$\text{NLL}(\beta)=-\sum_i\big[y_i\log p_i+(1-y_i)\log(1-p_i)\big].$$
Each row pays $-\log$(probability given to what happened): confident and right costs ~0, confident and wrong costs a lot.

**4. Gradient.** Using $\log p_i=z_i-\log(1+e^{z_i})$ and $\log(1-p_i)=-\log(1+e^{z_i})$, $\ell=\sum_i[y_iz_i-\log(1+e^{z_i})]$. With $\partial z_i/\partial\beta=x_i$:
$$\nabla_\beta\text{NLL}=X^T(p-y).$$
Same shape as linear regression's $X^T(X\beta-y)$, with $\sigma(X\beta)$ replacing $X\beta$.

**5. Calibration-in-the-large.** At the optimum $X^T(y-\hat p)=0$; the ones column gives $\sum_i\hat p_i=\sum_iy_i$ — an unweighted model with intercept predicts the training base rate on average.

**6. No closed form, but convex.** $\beta$ sits inside $\sigma$, so solve numerically. Hessian $X^TWX$ with $W=\text{diag}(p_i(1-p_i))$ is positive semi-definite, so any converged optimiser finds the global minimum. Gradient descent: $\beta\leftarrow\beta-\eta\frac1nX^T(p-y)$. Newton/IRLS: $\beta^{new}=(X^TWX)^{-1}X^TW\tilde z$, $\tilde z=X\beta+W^{-1}(y-p)$ — weighted least squares, re-weighted each round.

**7. Separation.** If a feature perfectly separates classes in training, $|\beta|\to\infty$ and the MLE does not exist; L2 regularisation fixes it (scikit-learn minimises $\frac12\lVert\beta\rVert^2+C\sum\text{loss}_i$).

## For the capstone
One of our two LO3 derivations. With ~6.4% positive region-weeks, separation is possible for rare region one-hots; keep L2 on. The base-rate identity is a quick check that predictions are calibrated before any class weighting.

## Related
- [Class weights and calibration derivation](class-weights-calibration-derivation.md)
- [Cost-based threshold derivation](cost-threshold-derivation.md)
- [Gradient boosting derivation](gradient-boosting-derivation.md)
- [Ridge regression derivation](ridge-regression-derivation.md)
