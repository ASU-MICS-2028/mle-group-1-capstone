---
summary: The negative binomial is a count model that lets the rate vary, so it handles over-dispersion.
type: concept
tags: [probability, count-data]
sources: [lecture-03 recording, probability & sampling slides]
---
# Negative binomial distribution

The negative binomial models the same kind of counts as the Poisson, but it allows the underlying rate to **vary** between units. It has two parameters: a mean and a **dispersion** parameter. When the dispersion shrinks to zero, it becomes the Poisson again.

Typical uses: insurance claims, hospital admissions, disease case counts.

Practical advice from the lecture: fit both Poisson and negative binomial and compare. If the negative binomial fits clearly better, that is evidence the rate really varies. Library functions are fine; no need to code it from scratch.

Caution: textbooks and software write its formula in different ways (e.g. "failures before the n-th success" with p and 1 − p swapped). The slide's typeset formula was garbled. Check which version your library uses before reading its parameters.

General idea from the slides: when one fixed parameter is not enough, put a distribution on that parameter.

## Related
- [Over-dispersion](over-dispersion.md)
- [Poisson distribution](poisson-distribution.md)
- [Choosing a distribution](choosing-a-distribution.md)
