---
summary: MAP combines the likelihood with a prior belief; with a Gaussian prior it equals L2 regularisation.
type: concept
tags: [statistics, estimation, regularisation]
sources: [intro slides]
---
# Maximum a posteriori (MAP) estimation

MAP picks the parameter that is most probable **after** seeing the data, combining the data with a **prior** (what you believed before seeing data):

θ* = the θ that maximises P(θ | data).

By Bayes' rule, P(θ | data) is proportional to P(data | θ) × P(θ), so MAP = likelihood × prior. (The slide gives only the first formula; the Bayes step is the standard next line.)

Useful fact: MAP with a normal (Gaussian) prior centred on zero is the same as MLE plus an **L2 (ridge)** penalty; a Laplace prior gives **L1 (lasso)**. So regularisation is a prior belief that weights should be small.

Example: you saw 3 floods in 3 weeks. MLE says p = 1. A prior saying floods are rare pulls the MAP estimate down to something more sensible.

## Related
- [Maximum likelihood estimation](maximum-likelihood-estimation.md)
- [Ridge regression](ridge-regression.md)
- [Lasso regression](lasso-regression.md)
