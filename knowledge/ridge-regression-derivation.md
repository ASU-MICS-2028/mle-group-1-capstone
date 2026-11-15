---
summary: Adding λ‖β‖² gives β = (XᵀX+λI)⁻¹Xᵀy, always invertible; lasso instead soft-thresholds
type: derivation
tags: [derivation, linear-models, regularisation, lo3]
sources: [ISLR 6.2.1–6.2.2 eq. 6.5, 6.7, 6.14–6.15, HOMLP ch 4, prosit-2 derivations.md §a.6]
---
# Ridge regression derivation

Centre $y$ and standardise the features so the intercept drops out and is not penalised. Ridge minimises
$$J(\beta)=\lVert y-X\beta\rVert^2+\lambda\lVert\beta\rVert^2,\qquad\lambda\ge0 .$$

**Gradient.** As for OLS, plus $\partial(\lambda\beta^T\beta)/\partial\beta=2\lambda\beta$:
$$-2X^Ty+2X^TX\beta+2\lambda\beta=0\;\Rightarrow\;\hat\beta_{\text{ridge}}=(X^TX+\lambda I)^{-1}X^Ty .$$

**Always invertible for $\lambda>0$.** For $v\ne0$: $v^T(X^TX+\lambda I)v=\lVert Xv\rVert^2+\lambda\lVert v\rVert^2>0$. Ridge adds $\lambda$ to every eigenvalue of $X^TX$, lifting the flat directions that collinearity creates.

**Orthonormal intuition ($X^TX=I$).** $\hat\beta_j=\hat\beta_j^{OLS}/(1+\lambda)$: uniform shrinkage, never exactly zero.

**Contrast: lasso.** Penalty $\lambda\sum_j|\beta_j|$. With orthonormal features each coordinate solves $(\beta_j-b_j)^2+\lambda|\beta_j|$, giving the soft threshold $\hat\beta_j=\text{sign}(b_j)(|b_j|-\lambda/2)_+$: small coefficients become exactly zero (variable selection). No general closed form because $|\beta_j|$ is not differentiable at 0; solved by coordinate descent.

**Practical points.** Standardise first (the penalty depends on units). Choose $\lambda$ by CV on the *correct* folds. Ridge = MAP estimate under a Gaussian prior on $\beta$; lasso = Laplace prior. In logistic regression the same L2 penalty appears; scikit-learn's `C` is roughly $1/\lambda$.

## For the capstone
The rainfall windows (1, 3, 7, 14, 30 days) and soil moisture are strongly correlated; an L2-penalised logistic regression keeps their coefficients stable. Tune $\lambda$ (or `C`) on the 2023 tuning year, never on 2024–2025.

## Related
- [Linear regression derivation](linear-regression-derivation.md)
- [Logistic regression derivation](logistic-regression-derivation.md)
- [Normal equation](normal-equation.md)
