---
summary: Ordinary least squares has an exact formula for the best weights, theta = (XᵀX)⁻¹Xᵀy.
type: concept
tags: [linear-models, optimisation]
sources: [lecture-06 recording, lec4 slides, MIT 6.390 ch2]
---
# Normal equation (closed-form least squares)

For linear regression with MSE there is a formula that gives the best weights in one step, with no training loop:

θ = (XᵀX)⁻¹ Xᵀ y

X is the data matrix (one row per example, a column of ones for the bias) and y is the vector of labels. This is called **ordinary least squares (OLS)**.

**Why it works:** MSE is convex (a single bowl). Its lowest point is where the slope (gradient) is zero. Write the gradient, set it to zero, solve for θ, and you get the formula.

**Normal equation vs gradient descent** (from the slide comparison):
- The normal equation is exact and needs no learning rate. It copes with many rows.
- But inverting XᵀX costs roughly the cube of the number of features, so it gets slow with very many features.
- It breaks down if features are strongly correlated, because XᵀX is then nearly impossible to invert and the weights become huge and unstable. Ridge regression fixes this.
- It only exists for this special case. Logistic regression, trees and neural networks have no closed form, so they need iterative methods like gradient descent.

The lecturer said students will not be asked to prove it. The step-by-step derivation lives in a separate note.

## Related
- [Linear regression](linear-regression.md)
- [Gradient descent](gradient-descent.md)
- [Ridge regression](ridge-regression.md)
- [Linear regression derivation](linear-regression-derivation.md)
