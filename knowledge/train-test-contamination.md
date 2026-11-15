---
summary: Computing preprocessing statistics on all data before splitting lets the test set leak in.
type: concept
tags: [leakage, preprocessing]
sources: [preprocessing & leakage slides, lecture-04 recording, lecture-02 recording]
---
# Train-test contamination

**Train-test contamination** happens when preprocessing uses statistics (mean, min, max, imputation values, encodings, selected features) computed on the **whole dataset before splitting**. The test set has then shaped the training data.

| Leaky order | Correct order |
|---|---|
| 1. scale using stats from ALL data | 1. split into train / test FIRST |
| 2. then split | 2. fit the scaler on train only |
| 3. test already influenced training | 3. apply that fitted scaler to test |

Small example: incomes in train range 12k–90k but the test set contains a 200k earner. Fitting min-max on all data uses 200k as the max, so the training data were scaled using a test value.

The lecturer named "preprocessing before the split" as a common mistake, and the Prosit 1 checklist said no cell may fit an encoder or scaler on train and test data together.

## For the capstone
Fit imputers and scalers on 2015–2022 only, inside a scikit-learn pipeline, then apply to 2023 and 2024–2025.

## Related
- [Split first, fit on train](split-first-fit-on-train.md)
- [Preprocessing inside cross-validation](preprocessing-inside-cross-validation.md)
- [Data leakage](data-leakage.md)
