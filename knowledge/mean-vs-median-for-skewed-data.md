---
summary: For skewed data the median is a safer centre than the mean, including for imputation.
type: concept
tags: [eda, statistics, preprocessing]
sources: [intro slides, lecture-04 recording]
---
# Mean vs median for skewed data

The mean uses every value's size, so one huge value drags it. The median only cares about order, so it stays put.

Example: five salaries of 2, 2, 3, 3 and 50 (thousand). Mean = 12, median = 3. The mean describes nobody.

In the preprocessing lecture a student pointed out that filling missing salaries with the mean is distorted by a few high earners; the lecturer agreed and said to **check the distribution first**, then choose the mean, the median or a constant to suit it.

Rule of thumb: roughly symmetric data → mean is fine; skewed data or outliers → median (and IQR for spread).

## For the capstone
Rainfall is strongly right-skewed. Use the median when filling gaps and when summarising regions.

## Related
- [Descriptive statistics](descriptive-statistics.md)
- [Missing value imputation](missing-value-imputation.md)
