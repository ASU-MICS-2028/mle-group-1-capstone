---
summary: Poisson(λ) models event counts in a window; its mean equals its variance.
type: concept
tags: [probability, count-data]
sources: [lecture-03 recording, probability & sampling slides]
---
# Poisson distribution

The Poisson counts events in a fixed window of time or space, e.g. malaria cases per day at a clinic. λ is the average rate per window.

P(X = x) = e^(−λ) λ^x / x!, for x = 0, 1, 2, …

Its defining property: **mean = variance = λ**.

Assumptions:
- events happen independently;
- the rate is constant across the window;
- two events cannot happen at exactly the same instant.

With λ = 1 most mass is at small counts (P(0) ≈ 0.37, P(1) ≈ 0.37, P(2) ≈ 0.18). As λ grows, the shape becomes a symmetric bell.

If any assumption breaks, real counts usually have variance bigger than the mean (over-dispersion), and Poisson then gives intervals that are too narrow.

## For the capstone
The number of flood reports per region-week could be modelled as a count, but floods cluster in rainy seasons and in some regions, so expect over-dispersion. Our binary label sidesteps this.

## Related
- [Over-dispersion](over-dispersion.md)
- [Negative binomial distribution](negative-binomial-distribution.md)
- [Choosing a distribution](choosing-a-distribution.md)
