---
summary: Pick a distribution from how the data were generated, not from convenience.
type: procedure
tags: [probability, count-data]
sources: [probability & sampling slides, lecture-03 recording]
---
# Choosing a distribution

The slides give a lookup table. Ask how the data were produced:

| If the data is… | Use |
|---|---|
| one yes/no per unit | Bernoulli |
| a count out of a fixed n | Binomial |
| a count out of n, but p varies between units | Beta-binomial |
| a count of events in a window | Poisson |
| a count with variance > mean | Negative binomial |
| one of k categories | Categorical / multinomial |
| a positive, right-skewed measurement | Log-normal |
| a proportion between 0 and 1 | Beta |

Rules from the summary slide:
1. Choose from the data-generating process, not convenience.
2. Always compare mean and variance for counts.
3. Over-dispersion means some parameter varies.
4. Write your assumptions down.

Wrong choice = wrong estimates *and* wrongly confident intervals, and nothing crashes to warn you.

## Related
- [Random variable and distribution](random-variable-and-distribution.md)
- [Over-dispersion](over-dispersion.md)
- [A fitted distribution is a model](fitted-distribution-is-a-model.md)
