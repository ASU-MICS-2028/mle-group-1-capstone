---
summary: Calendar and slow macro features learn which period a row came from, not risk
type: result
tags: [features, temporal-split, drift]
sources: [prosit-2 ADR 0012, prosit-2 ADR 0009, prosit-2 learnings/03_feature_audit]
---
# Features that encode the period hurt on the future

In Prosit 2, 92% of loans came from one quiet half-year with about 1% defaults, while other quarters had 5–15%. Month, weekday and day-of-month clues looked useful on mixed-time tests, but on future loans they **hurt** (average change in lift −0.39, helped in only 3 of 31 combinations). They had learned *which period* a loan came from.

Macro indicators (inflation, exchange rate) were worse in a quieter way: annual figures took only 4 distinct values in training, so each one acted as a year label, and the deployment country's inflation sat far outside the training range. Average effect −0.09: no help.

We found this only because every feature group was tested with and without, on the time split. The audit had flagged the risk a step earlier.

## For the capstone
Week-of-year and "rainy season" flags may be fine because seasonality genuinely repeats, but a year feature, a trend, or any slow-moving indicator with few distinct training values can memorise period-specific reporting volume (Groundsource coverage grows over time). Test each such group with and without on the 2023 tune year.

## Related
- [test-every-diverging-path-in-a-table.md](test-every-diverging-path-in-a-table.md)
- [shuffled-validation-inflates-scores.md](shuffled-validation-inflates-scores.md)
- [../knowledge/model-transfer-across-places.md](../knowledge/model-transfer-across-places.md)
