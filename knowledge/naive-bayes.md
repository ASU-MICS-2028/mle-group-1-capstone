---
summary: Naive Bayes applies Bayes' rule assuming features are independent given the class; fast but poorly calibrated.
type: concept
tags: [naive-bayes, classification, probability]
sources: [lec5 slides]
---
# Naive Bayes

Naive Bayes classifies with Bayes' theorem:

P(class | features) ∝ P(class) × P(features | class)
(posterior ∝ prior × likelihood)

The **naive** assumption: features are independent of each other *once you know the class*. Then P(features | class) is just the product of one-feature probabilities, which are easy to count from training data. Predict the class with the largest posterior.

Example from the slides, an email containing "free" and "offer":
- spam: 0.4 × 0.6 × 0.4 = 0.096
- not spam: 0.6 × 0.1 × 0.2 = 0.012
- normalise: 0.096 / 0.108 ≈ 0.89 → spam.

Variants: **Gaussian** (continuous features, assumed bell-shaped per class), **multinomial** (word counts), **Bernoulli** (yes/no features).

Practical details:
- multiplying many small probabilities underflows to zero, so add logs instead;
- **Laplace smoothing**: add 1 to every count so a word never seen with a class does not zero out the whole product;
- training is just counting, so it is very fast and works with tiny datasets and huge vocabularies.

Limits: the independence assumption is almost never true. The ranking of classes still often works, but **the probabilities are poorly calibrated** (often pushed towards 0 or 1). It also ignores interactions, and loses to logistic regression or boosting when features are correlated.

## For the capstone
Not in our model list: rainfall and soil-moisture features are strongly correlated, which breaks the naive assumption. Could serve as an extra simple baseline.

## Related
- [Probability calibration](probability-calibration.md)
- [Beat a naive baseline first](beat-a-naive-baseline-first.md)
