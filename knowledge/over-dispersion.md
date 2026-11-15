---
summary: Count data whose variance exceeds the mean break the Poisson; check variance/mean first.
type: concept
tags: [probability, count-data]
sources: [lecture-03 recording, lecture-02 recording, probability & sampling slides]
---
# Over-dispersion

**Over-dispersion** means Var(X) > E[X]. Real count data almost always have it.

Quick check: compute sample variance ÷ sample mean.
- about 1 → Poisson is plausible;
- much bigger than 1 → over-dispersed; use a negative binomial.

The lecturer called this mean-variance comparison "the first check you have to do" before choosing a count distribution. No formal test is needed; a plot plus the ratio is enough.

Where the extra spread comes from:
- **Clustering** – observations come in groups that share conditions.
- **Heterogeneity** – the underlying rate differs between units.

If you fit a Poisson anyway, your intervals come out **too narrow** and your conclusions **over-confident**.

Example: nets per household had mean 1.70 and variance 2.59. The ratio is 2.59 / 1.70 ≈ 1.52. (The lecturer said 1.59 and another summary says 1.53; the arithmetic gives 1.52.)

## For the capstone
Before modelling any counts (e.g. reports per region-week), print variance/mean. Region and season differences make strong over-dispersion likely.

## Related
- [Poisson distribution](poisson-distribution.md)
- [Negative binomial distribution](negative-binomial-distribution.md)
- [Design effect](design-effect.md)
