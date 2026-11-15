---
summary: A confidence interval is a range of plausible values for a parameter at a stated coverage.
type: concept
tags: [statistics, uncertainty]
sources: [probability & sampling slides, lecture-02 recording]
---
# Confidence interval

A **confidence interval (CI)** is a range of plausible values for an unknown population number, with a stated **coverage**, usually 95%.

Meaning of "95%": if we repeated the whole study many times and built an interval each time, about 95% of those intervals would contain the true value. It is not "95% chance the truth is in this particular interval", though people often say it that way.

Ways to get one:
- a formula, e.g. estimate ± 2 × standard error (works when the CLT applies);
- the **bootstrap** (resample your data).

An interval is only honest if its assumptions hold. Ignoring clustering or over-dispersion gives intervals that are too narrow.

Slide checkpoint: "30% ownership, 95% CI 29.4–30.6%" from 200 villages × 15 households is suspicious – probably computed as if households were independent.

The lecturer asked for CIs on estimates in Prosit 1, not bare numbers.

## For the capstone
Report every headline test metric with a 95% CI. If two models' CIs overlap heavily, do not claim one is better.

## Related
- [Bootstrap confidence interval](bootstrap-confidence-interval.md)
- [Sampling distribution and standard error](sampling-distribution-and-standard-error.md)
- [Defend every number](defend-every-number.md)
