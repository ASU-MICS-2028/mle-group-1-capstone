---
summary: Bagging trains many models on bootstrap resamples and averages them to cut variance.
type: concept
tags: [ensembles, trees]
sources: [lec5 slides, MIT 6.390 ch9]
---
# Bagging (bootstrap aggregating)

Single deep trees are unstable: small data changes give very different trees (high variance). Bagging averages that instability away.

1. Make B **bootstrap samples**: each one draws n rows from the n training rows *with replacement*. Some rows appear twice, some not at all.
2. Train one model (usually a deep tree) on each sample.
3. Combine: **average** for regression, **majority vote** for classification.

A bootstrap sample contains about **63%** of the distinct rows. The chance a given row is never picked is (1 − 1/n)ⁿ ≈ e⁻¹ ≈ 0.37. The left-out 37% are the "out-of-bag" rows.

Why it works: if the models make errors that do not line up, averaging cancels them. Bias stays about the same; variance drops.

Cost: you lose the easy interpretability of a single tree. Training parallelises well because the models are independent.

Example: 100 trees each say "flood" with probability scores; the bagged score is the average, which is much steadier than any one tree's.

## Related
- [Random forest](random-forest.md)
- [Out-of-bag error](out-of-bag-error.md)
- [Bagging vs boosting](bagging-vs-boosting.md)
- [Bias-variance trade-off](bias-variance-tradeoff.md)
