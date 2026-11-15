---
summary: Report every metric per group and per intersection, with confidence intervals, not just overall
type: concept
tags: [fairness, evaluation]
sources: [Mitchell et al. 2019 §4.7, Buolamwini & Gebru 2018, capstone brief §5]
---
# Disaggregated evaluation

A single overall score can hide a model that works well for the majority and badly for a minority. Disaggregated evaluation means computing each metric **separately per group** (and for important **intersections** of groups), alongside the overall figure. The capstone brief requires disaggregated fairness results in the ethics pack.

How to do it well:
- **Count first.** Rows and positives per group, before modelling. Small groups give noisy metrics.
- **Several metrics per group.** Recall (TPR), false positive rate, precision (PPV), and for scores, calibration and score distribution.
- **Confidence intervals.** Bootstrap each per-group metric; the finer the slice, the wider the interval. Without CIs, apparent gaps may be noise.
- **At the operating threshold.** Fairness of the raw score and fairness of the yes/no decision can differ.
- **Before and after mitigation.** Show what changed and what it cost overall.

## For the capstone
Groups = the 16 regions, urban vs rural, and rainy vs dry season; key intersection region × season. Report per-region recall at the alert budget, false-alert rate and calibration, with bootstrap CIs over test weeks. Expect very wide intervals for regions with few positive weeks, and say so.

## Related
- [Gender Shades](gender-shades.md)
- [Model cards](model-cards.md)
- [Fairness definitions](fairness-definitions.md)
- [Ethics and fairness review pack](ethics-and-fairness-review-pack.md)
