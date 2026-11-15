---
summary: Binomial(n, p) counts successes in n independent trials that share the same p.
type: concept
tags: [probability]
sources: [lecture-03 recording, probability & sampling slides]
---
# Binomial distribution

The binomial counts how many successes happen in n Bernoulli trials.

P(X = x) = C(n, x) · p^x · (1 − p)^(n − x), for x = 0 … n,

where C(n, x) is the number of ways to choose x of the n trials.

- Mean = np
- Variance = np(1 − p), largest when p = 0.5.

Two assumptions carry everything:
1. the trials are **independent** (one does not affect another);
2. they **share one p**.

If either breaks, real data are more spread out than the binomial predicts. If p varies from unit to unit, use a beta-binomial instead.

Example: of 30 households, how many own a net, if each owns one with p = 0.71? For "at least k" questions, use the complement: 1 − P(fewer than k).

(The slide's formula has a typo, writing the last exponent as n − r instead of n − x.)

## For the capstone
"Number of flood weeks in a year for one region" looks binomial (52 trials), but weeks in the same rainy season are not independent and p changes by season, so the binomial would understate the spread.

## Related
- [Bernoulli distribution](bernoulli-distribution.md)
- [Over-dispersion](over-dispersion.md)
- [Choosing a distribution](choosing-a-distribution.md)
