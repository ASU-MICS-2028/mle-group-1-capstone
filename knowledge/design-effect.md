---
summary: Design effect measures how much clustering shrinks the real information in a sample.
type: concept
tags: [sampling, uncertainty]
sources: [probability & sampling slides]
---
# Design effect

The **design effect (DEFF)** compares the variance of an estimate under the real sampling design to the variance if the same number of units had been drawn by simple random sampling:

DEFF = variance under actual design ÷ variance under simple random sampling.

- DEFF > 1: your sample carries **less** information than its size suggests.
- **Effective sample size** ≈ raw n ÷ DEFF.

Slide example: DEFF ≈ 4.2, so 17,933 clustered households carry about as much information as 17,933 / 4.2 ≈ 4,270 independent ones.

## For the capstone
We have about 16 regions × 52 weeks × 11 years of rows, but rows in the same week are highly correlated, so the effective sample is much smaller, closer to the number of distinct weeks (and the number of distinct flood events). Keep this in mind before trusting small differences.

## Related
- [Cluster sampling](cluster-sampling.md)
- [Cluster bootstrap](cluster-bootstrap.md)
