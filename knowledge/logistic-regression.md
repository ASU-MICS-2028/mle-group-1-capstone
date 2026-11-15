---
summary: Logistic regression is a linear classifier that turns its score into a probability with the sigmoid.
type: concept
tags: [linear-models, classification]
sources: [lecture-06 recording, lecture-07 recording, lec4 slides, MIT 6.390 ch4]
---
# Logistic regression

Despite the name, logistic regression is a **classifier**. It:

1. computes a linear score z = θᵀx + θ₀;
2. squashes it into (0, 1) with the **sigmoid** σ(z) = 1 / (1 + e^(−z)). σ(0) = 0.5; big positive z gives nearly 1; big negative z nearly 0;
3. reads the result as P(y = 1 | x), the probability of the positive class;
4. predicts class 1 if that probability is above a **threshold** (0.5 by default, but it is a choice).

It is trained by minimising **log loss** (negative log-likelihood, binary cross-entropy), which is the same as the logistic loss from class written for 0/1 labels. The loss is convex but has **no closed-form solution**, so solvers use gradient descent or similar methods. The gradient has a neat form: (prediction − label) × input, just like linear regression.

Why it is a good first model:
- fast, stable and convex;
- interpretable: each weight shows how a feature moves the log-odds;
- gives probabilities that are often reasonably calibrated.

Weak points: a straight-line boundary only (unless you add features), needs scaled features when regularised, and needs regularisation if the classes are perfectly separable.

The derivation from maximum likelihood is in a separate note.

## For the capstone
Our main interpretable model. Standardise features first and tune the regularisation strength C on 2023.

## Related
- [Logistic regression derivation](logistic-regression-derivation.md)
- [Logistic regression needs regularisation](logistic-regression-needs-regularisation.md)
- [Choosing a classification threshold](classification-threshold.md)
- [Classification loss functions compared](classification-loss-functions-compared.md)
- [Beat a naive baseline first](beat-a-naive-baseline-first.md)
