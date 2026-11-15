---
summary: A split can be grouped by cluster and still lose marks if it isn't stratified
type: lesson
tags: [validation, grading, sampling]
sources: [prosit-1 grade (B2/B3, −1), prosit-1 notebook §7]
---
# Stratify and group the split

In Prosit 1 we held out 20% of survey clusters with `GroupShuffleSplit`, so no village was on both sides. That's correct for leakage, but we lost a point on the split criterion. Our reading (the marker left no comments): the split wasn't **stratified by region**, so some regions could be thin or missing in the test part. `StratifiedGroupKFold` does both at once: it keeps groups intact and balances the strata across folds.

The general lesson is that a split has several jobs, and the rubric checks each:
- no unit on both sides (grouping);
- every important subgroup represented (stratification);
- no future information (time order), where that applies.

State in the write-up which jobs your split does, and why any it skips don't apply.

## For the capstone
The main split is temporal, so stratification can't be forced. Instead, report how many flood-weeks each region has in train, tune and test, and flag regions with almost none in 2023 or 2024–2025. For any cross-validation inside 2015–2022, use blocked folds by year and say so explicitly.

## Related
- [report-the-named-subgroup-separately.md](report-the-named-subgroup-separately.md)
- [time-split-must-respect-when-labels-are-known.md](time-split-must-respect-when-labels-are-known.md)
- [../knowledge/temporal-split.md](../knowledge/temporal-split.md)
