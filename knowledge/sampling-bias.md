---
summary: Selection, coverage and non-response bias do not shrink with more data; ask who is missing.
type: concept
tags: [sampling, bias, fairness]
sources: [probability & sampling slides, lecture-02 recording]
---
# Sampling bias

Three common kinds:
- **Selection bias** – the way you pick units favours some of them.
- **Coverage bias** – part of the population is not on the list you sample from at all.
- **Non-response bias** – those who do not respond differ from those who do.

The key lesson from the slides: **bias does not shrink as the sample grows.** Averaging more of the wrong thing only makes you confidently wrong. Always ask: *who is missing, and would they look different?*

The Prosit 1 data made this concrete: rural and border communities were under-represented in surveys. Groups you never sampled are invisible in every metric, which is where fairness work starts.

Slide checkpoint example: a model trained only on two big referral hospitals misses rural clinics and people who never reach a hospital.

## For the capstone
Groundsource labels come from news reports, so this is coverage bias: floods in places with little media attention are under-counted. More years of news data will not fix that. State it as a limitation and check model errors per region.

## Related
- [Population, sample, parameter, statistic](population-sample-parameter-statistic.md)
- [Ethics is required in every project](ethics-is-required-in-every-project.md)
- [Types of supervision](types-of-supervision.md)
