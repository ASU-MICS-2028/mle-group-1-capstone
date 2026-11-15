---
summary: Linear regression predicts a number as a weighted sum of the features plus a bias.
type: concept
tags: [linear-models, regression]
sources: [lecture-05 recording, lecture-06 recording, lec4 slides, MIT 6.390 ch2]
---
# Linear regression

Linear regression predicts a number by adding up the features, each multiplied by a weight, plus a constant:

ŷ = θ₀ + θ₁x₁ + θ₂x₂ + … + θ_d x_d

- each **θⱼ** (weight, coefficient or parameter) says how much feature xⱼ pushes the prediction up or down;
- **θ₀** is the bias or intercept;
- d is the number of features.

The model is "a collection of numbers" (the lecturer's phrase). Training means finding the θ values that make the error on the training data as small as possible, usually measured with mean squared error.

Example: salary = 2,000 + 300 × (years of experience). A new hire with 0 years earns 2,000 (the intercept). Each extra year adds 300 (the weight).

In matrix form the whole dataset is predicted at once as ŷ = Xθ, where X has one row per example. Transposes in the formulas are only there to make the matrix sizes line up.

Two ways to find θ: the closed-form **normal equation**, or **gradient descent**.

Correction to the recording: the lecturer said weights are usually between 0 and 1. That is not true in general. Weights can be any real number and their size depends on how the features are scaled.

The relationship need not be a straight line in the raw feature. Adding squared or other transformed features (polynomial regression) still counts as "linear" in the weights.

## Related
- [Bias term and intercept](bias-term-intercept.md)
- [Mean squared error](mean-squared-error.md)
- [Normal equation](normal-equation.md)
- [Gradient descent](gradient-descent.md)
- [Ridge regression](ridge-regression.md)
