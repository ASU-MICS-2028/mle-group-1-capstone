---
summary: Least squares equals Gaussian maximum likelihood, and setting the gradient to zero gives the normal equations
type: derivation
tags: [derivation, linear-models, regression, lo3]
sources: [ISLR 3.1.1 eq. 3.4, 3.2.1 eq. 3.22, HOMLP ch 4, prosit-2 derivations.md §a]
---
# Linear regression derivation (MLE → least squares → normal equations)

Notation: $X$ is the $n\times(p+1)$ design matrix with a leading column of ones, $y$ the target, $\beta$ the coefficients (lecture notes write $\theta$). Two rules do the work: $\partial(a^T\beta)/\partial\beta=a$ and $\partial(\beta^TA\beta)/\partial\beta=2A\beta$ for symmetric $A$.

**1. Model.** $y=X\beta+\varepsilon$ with $\varepsilon_i\overset{iid}{\sim}\mathcal N(0,\sigma^2)$.

**2. Log-likelihood.** Each $y_i$ is normal around $x_i^T\beta$, rows are independent, so
$$\ell(\beta,\sigma^2)=-\tfrac n2\log(2\pi\sigma^2)-\tfrac{1}{2\sigma^2}\sum_i(y_i-x_i^T\beta)^2 .$$
The first term has no $\beta$; the second is $-\text{RSS}(\beta)$ times a positive constant. **Maximising likelihood = minimising RSS.** (Also $\hat\sigma^2_{MLE}=\text{RSS}/n$.)

**3. Normal equations.** Expand $\text{RSS}=(y-X\beta)^T(y-X\beta)=y^Ty-2\beta^TX^Ty+\beta^TX^TX\beta$ (the two cross terms are equal scalars). Differentiate:
$$\nabla_\beta\text{RSS}=-2X^Ty+2X^TX\beta=0\;\Rightarrow\;X^TX\hat\beta=X^Ty\;\Rightarrow\;\hat\beta=(X^TX)^{-1}X^Ty .$$

**4. It is a minimum.** Hessian $2X^TX$; $v^TX^TXv=\lVert Xv\rVert^2\ge0$, so RSS is convex.

**5. Geometry.** $X^T(y-X\hat\beta)=0$: residuals are orthogonal ("normal") to every column, so they sum to zero and are uncorrelated with each feature in training data. A pattern in the residual plot therefore means mis-specification.

**6. When $X^TX$ is singular.** Perfect collinearity (all one-hot levels plus intercept), $p+1>n$, constant columns; near-collinearity gives huge, sign-flipping coefficients. Fixes: drop a dummy, use `lstsq`/pseudo-inverse, or ridge.

One-predictor check: $\hat\beta_1=\sum(x_i-\bar x)(y_i-\bar y)/\sum(x_i-\bar x)^2$, $\hat\beta_0=\bar y-\hat\beta_1\bar x$.

## For the capstone
Our target is binary, so OLS is not a final model, but this is the base for the logistic and ridge derivations, and a linear probability model can be a sanity baseline. Watch collinearity among the 1/3/7/14/30-day rainfall sums.

## Related
- [Linear regression](linear-regression.md)
- [Normal equation](normal-equation.md)
- [Ridge regression derivation](ridge-regression-derivation.md)
- [Logistic regression derivation](logistic-regression-derivation.md)
