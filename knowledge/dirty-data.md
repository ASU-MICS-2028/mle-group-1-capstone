---
summary: Real data is dirty in three ways: incomplete, noisy and inconsistent.
type: concept
tags: [preprocessing, data-quality, cleaning]
sources: [preprocessing & leakage slides, lecture-04 recording, Terms notes]
---
# Dirty data

Data is "dirty" in three ways:

- **Incomplete** – missing values or whole missing fields (a sensor failed, a form question was skipped, a record was lost).
- **Noisy** – errors, typos and outliers. Lecture example: an age of 600 in a class of 18–30 year olds.
- **Inconsistent** – the same fact recorded differently in different places: codes, units or names (e.g. "M"/"Male"/1; cm vs m).

**Data cleaning** is fixing these: fill or drop missing values, smooth noise, handle outliers, and make formats consistent. Also remove exact duplicates.

The Prosit 1 dataset was deliberately tweaked to contain such problems, so finding them was part of the task.

## For the capstone
Expect: missing satellite values in some weeks, region names spelled differently across sources (and the 2018–2019 change from 10 to 16 regions), and several news reports of one flood counted as separate events.

## Related
- [Missing value imputation](missing-value-imputation.md)
- [Outlier detection](outlier-detection.md)
- [Smoothing noisy data by binning](smoothing-by-binning.md)
- [Data integration](data-integration.md)
