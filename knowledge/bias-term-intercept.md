---
summary: The intercept is the prediction when all features are zero; a constant feature 1 absorbs it.
type: concept
tags: [linear-models]
sources: [lecture-05 recording, lecture-06 recording, lec4 slides]
---
# Bias term (intercept)

In ŷ = θ₀ + θ₁x₁ + … the constant θ₀ is called the **bias** or **intercept**.

**Meaning:** it is the prediction when every feature is zero. In the lecturer's salary example (feature = years of experience), a new hire with zero experience still earns a base salary. That base is the intercept. The bias moves the line up or down; it does not change the slope.

**The bias trick:** add a fake feature x₀ = 1 to every example. Then θ₀·x₀ = θ₀, and the whole model becomes one tidy sum from j = 0 to d, or ŷ = θᵀx in vector form. This is why data matrices often start with a column of ones.

Two practical points:
- In regularised models (ridge, lasso, regularised logistic regression) the intercept is normally **not** penalised. It just sets the overall level.
- If features are standardised (mean 0), the intercept becomes the prediction for an "average" example. In logistic regression it is then the baseline log-odds of the positive class.

## For the capstone
In our logistic regression with standardised features, the intercept reflects the base flood rate per region-week. A very negative intercept is expected because floods are rare.

## Related
- [Linear regression](linear-regression.md)
- [Logistic regression](logistic-regression.md)
- [Ridge regression](ridge-regression.md)
