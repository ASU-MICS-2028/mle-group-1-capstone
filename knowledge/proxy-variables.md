---
summary: Dropping a sensitive attribute fails when other features encode it; test by predicting the attribute
type: concept
tags: [fairness, reading, features]
sources: [Barocas, Hardt & Narayanan, FML ch. 3 (redundant encodings), capstone brief §5]
---
# Proxy variables and redundant encodings

Removing a sensitive attribute from the inputs ("fairness through unawareness") rarely removes it from the model. Many weakly related features together can **redundantly encode** the attribute, so the model still effectively sees it.

**How to test:** train a classifier to predict the attribute from the other features. If it succeeds well (AUC well above 0.5), the attribute is recoverable. Also measure how predictions change when suspected proxies are removed.

**Not every correlate is illegitimate.** A feature may correlate with a group because it carries real causal information. The question is whether it mainly stands in for the group or genuinely informs the outcome. Forcing all features to be uncorrelated with the group can do harm.

The capstone brief requires a **proxy analysis** in the ethics pack.

## For the capstone
Our worry is not a protected trait but **media attention and wealth**. Built-up share and population plausibly raise real flood risk (impervious surfaces, drainage) *and* news coverage. Tests: (1) refit without built-up share and population and compare per-region predictions; (2) check how much these features drive alerts (permutation importance); (3) compare against satellite-observed floods (Global Flood Database, 2015–2018) where possible.

## Related
- [News label bias](news-label-bias.md)
- [Land-change added value](land-change-added-value.md)
- [Fairness definitions](fairness-definitions.md)
- [Book: Interpretable Machine Learning](book-molnar-iml.md)
