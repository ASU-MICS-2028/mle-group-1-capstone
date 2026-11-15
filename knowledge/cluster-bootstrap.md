---
summary: When data come in groups, bootstrap whole groups, or the interval is falsely narrow.
type: procedure
tags: [statistics, uncertainty, evaluation]
sources: [probability & sampling slides]
---
# Cluster bootstrap

A plain bootstrap resamples individual rows, which assumes the rows are independent. When rows come in **clusters** that resemble each other, that assumption is false and the interval comes out too narrow (falsely precise).

The fix: resample **whole clusters** with replacement, keeping every row inside each chosen cluster.

Slide example (2,000 resamples of household net ownership):
- naive bootstrap over households → narrow interval;
- cluster bootstrap over survey clusters → much wider, honest interval (design effect about 4.2).

For time series the same idea is a **block bootstrap**: resample blocks of consecutive time steps, so nearby, similar weeks stay together.

## For the capstone
Our test rows are region-weeks. All 16 regions in one week share weather, and nearby weeks are alike. Resample whole weeks, or blocks of several weeks, not single region-weeks.

## Related
- [Bootstrap confidence interval](bootstrap-confidence-interval.md)
- [Cluster sampling](cluster-sampling.md)
- [Design effect](design-effect.md)
