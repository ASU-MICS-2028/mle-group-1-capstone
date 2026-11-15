---
summary: A statistic varies from sample to sample; its spread is the standard error (precision, not correctness).
type: concept
tags: [sampling, statistics, uncertainty]
sources: [probability & sampling slides]
---
# Sampling distribution and standard error

Imagine repeating the whole study many times, each time with a fresh sample. Each run gives a slightly different statistic (say, a different average). The spread of those values is the **sampling distribution** of the statistic. Its standard deviation is the **standard error (SE)**.

- Small SE → the estimate is repeatable (precise).
- SE says nothing about whether the sample was fair. A biased sample can have a tiny SE and still be wrong.

The slides put it as: precision is not correctness.

Example: two surveys both report 70% ± 1%. If one only visited towns, its small SE hides that it is aimed at the wrong target.

## For the capstone
A model's test recall is a statistic with its own SE. With only a few dozen flood weeks in 2024–2025, that SE will be large, so small gaps between models may be noise.

## Related
- [Population, sample, parameter, statistic](population-sample-parameter-statistic.md)
- [Confidence interval](confidence-interval.md)
- [Bootstrap confidence interval](bootstrap-confidence-interval.md)
- [Sampling bias](sampling-bias.md)
