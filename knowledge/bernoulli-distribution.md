---
summary: Bernoulli(p) models one yes/no outcome; its log gives the log-loss used in classification.
type: concept
tags: [probability, classification]
sources: [lecture-03 recording, probability & sampling slides]
---
# Bernoulli distribution

A Bernoulli variable is a single yes/no trial. X = 1 ("success") with probability p, and X = 0 with probability 1 − p.

P(X = x) = p^x (1 − p)^(1 − x), for x in {0, 1}.

- Mean = p
- Variance = p(1 − p)

"Success" just means the outcome you chose to call 1. If you care about the bad outcome, call that the success.

Example from the slides: 70.96% of surveyed households own at least one net, so p ≈ 0.71.

Why it matters for ML: binary classification is built on it. A classifier like logistic regression predicts p for each row. Taking minus the log of the Bernoulli probability of the true label gives the **log-loss** (cross-entropy) that the model minimises.

## For the capstone
Each region-week label is Bernoulli: flood (1) or no flood (0). Floods are rare, so p is small, which means classes are imbalanced and accuracy is a misleading metric.

## Related
- [Binomial distribution](binomial-distribution.md)
- [Regression vs classification](regression-vs-classification.md)
- [Maximum likelihood estimation](maximum-likelihood-estimation.md)
