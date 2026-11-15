---
summary: For a logistic model, weight × (value − reference) gives exact, checkable reasons
type: procedure
tags: [explainability, logistic-regression, deployment]
sources: [prosit-2 ADR 0017, prosit-2 learnings/08_reason_codes]
---
# Faithful reason codes from a linear model

Prosit 2 had to give each decision its top 3 reasons in plain words, true to the model and stable. What we built:

1. **Push per feature** = model weight × (applicant's value − reference value), on the log-odds scale. The pushes add up exactly to the score minus the reference score, and they matched standard SHAP for this linear model, so they could be checked by hand.
2. **Reference = the average applicant.** "Average approved" agreed 98%; "best possible" made one feature the top reason for everyone, so it was rejected.
3. **Group features into themes** (5 themes from 13 features). Single features produced contradicting pairs (8.7% of reasons mostly cancelled by a partner); themes removed that and lifted top-3 stability after refitting from 53% to 94%.
4. **Minimum push 0.2 log-odds** before a theme is shown; stability rose from 63% to 94%, and nobody was left with no reason.
5. **Word reasons with the person's own numbers.**

The reason audit also surfaced a fairness problem: "you haven't borrowed recently" appeared in 31% of declined lists, which led to dropping those features.

## For the capstone
The Streamlit dashboard can show, per region-week, the top drivers of the alert (e.g. "7-day rainfall well above this region's usual"), with themes such as recent rain, soil wetness, terrain and built-up area. If a tree model is chosen, use SHAP and test stability the same way.

## Related
- [simple-models-held-up-better-over-time.md](simple-models-held-up-better-over-time.md)
- [scorer-tests-catch-what-metrics-miss.md](scorer-tests-catch-what-metrics-miss.md)
- [../knowledge/black-box-models-and-explainability.md](../knowledge/black-box-models-and-explainability.md)
