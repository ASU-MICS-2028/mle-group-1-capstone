---
summary: Options for missing values, from dropping rows to predicting them; fit any filler on train only.
type: procedure
tags: [preprocessing, cleaning, missing-data]
sources: [preprocessing & leakage slides, lecture-04 recording, intro slides]
---
# Missing value imputation

*Imputation* means filling in missing values. Options, roughly from crudest to best:

1. **Drop the row** – fine only if very few rows are affected (e.g. 10 of 1,000). If more than half is missing, the lecturer suggested collecting the data again.
2. **Fill in by hand** – only for a handful of records.
3. **Global constant** – e.g. "Unknown", or a fixed floor value.
4. **Column mean** (or **median** if the column is skewed).
5. **Class mean** – the mean within the row's group.
6. **Predict it** – fit a small model (e.g. regression, or k-nearest neighbours) on complete rows to estimate the missing value. The lecturer called this the most accurate option.

Two warnings:
- **"Class mean" can leak.** If "class" means the *target label*, you are using the answer to fill the inputs, and at prediction time the label is unknown. It is only safe when the group is another feature. The slide does not make this clear.
- **Fit the filler on training data only.** The mean, median or imputation model must be computed from the training set, then applied to validation/test.

Tip: the fact that a value is missing can itself be informative; add an "is missing" 0/1 column.

## For the capstone
Use median imputation inside the scikit-learn pipeline (fitted on 2015–2022), plus missing flags for satellite gaps.

## Related
- [Mean vs median for skewed data](mean-vs-median-for-skewed-data.md)
- [Split first, fit on train](split-first-fit-on-train.md)
- [Dirty data](dirty-data.md)
