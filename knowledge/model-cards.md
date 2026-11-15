---
summary: A Model Card reports a model's intended use and its performance per group, like a nutrition label
type: source
tags: [fairness, documentation, reading]
sources: [Mitchell et al. 2019, Model Cards for Model Reporting, FAT* 2019, doi:10.1145/3287560.3287596, https://arxiv.org/abs/1810.03993]
---
# Model cards (Mitchell et al. 2019)

A trained model should ship with a short document stating what it is for, what it is **not** for, and how well it works **for each relevant group**, not only on average. The paper's examples are a smile detector and a toxicity classifier, but the format is general.

**Nine sections:** Model details (who, when, version, type, algorithm, features, any fairness constraints, licence, contact) · Intended use (primary uses, users, **out-of-scope uses**) · Factors (*relevant* factors where performance might differ vs *evaluation* factors actually reported, with reasons for any gap) · Metrics (which, why, **decision thresholds**, how uncertainty was measured) · Evaluation data · Training data (at least the distribution across factors) · Quantitative analyses (**unitary** and **intersectional** results) · Ethical considerations · Caveats and recommendations.

**What we take from it:** break results down by the chosen factors; report intersections (problems hide where groups overlap); report several error types (FPR, FNR, false discovery, false omission rates); compare score distributions, not just yes/no outcomes; give confidence intervals, which matter more the finer you slice; state the threshold and why.

## For the capstone
Factors: region, urban vs rural, season, and coverage era. Intended use: weekly preparation by NADMO regional offices. Out of scope: district- or household-level decisions, insurance or land-use enforcement, reading a low score as "safe". Intersections: region × rainy season. Bootstrap CIs are essential — small regions have only a handful of positive weeks.

## Related
- [Datasheets for datasets](datasheets-for-datasets.md)
- [Disaggregated evaluation](disaggregated-evaluation.md)
- [Ethics and fairness review pack](ethics-and-fairness-review-pack.md)
- [Flood ethics concerns](flood-ethics-concerns.md)
