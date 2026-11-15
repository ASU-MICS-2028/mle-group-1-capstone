---
summary: MLE picks the parameter values that make the observed data most probable.
type: concept
tags: [statistics, estimation, foundations]
sources: [intro slides, probability & sampling slides]
---
# Maximum likelihood estimation (MLE)

MLE answers: *which parameter value makes the data we actually saw most probable?*

Given data x₁ … xₙ and a model with parameter θ, the **likelihood** is the probability of the data under θ:

L(θ) = p(x₁, …, xₙ | θ).

The MLE is the θ that makes L(θ) largest. Intuition from the slides: among all explanations of how your data were made, pick the one under which the data look least surprising.

In practice (standard, not on the slide): if the points are independent, L(θ) is a product of probabilities, and we maximise the **log-likelihood** (a sum) instead, because sums are easier to work with.

Example: 7 floods in 10 weeks with a Bernoulli model. Trying p = 0.5 gives likelihood 0.5¹⁰ ≈ 0.001; p = 0.7 gives 0.7⁷·0.3³ ≈ 0.002. The best value is p = 7/10, the observed share.

Links to models: logistic regression is fitted by maximising the Bernoulli likelihood (= minimising log-loss); linear regression with squared error is MLE under normal noise.

## Related
- [Maximum a posteriori estimation](maximum-a-posteriori-estimation.md)
- [Bernoulli distribution](bernoulli-distribution.md)
- [Normal distribution](normal-distribution.md)
