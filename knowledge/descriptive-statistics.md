---
summary: Describe data by its centre (mean, median, mode), spread (SD, IQR) and shape (skew, tails).
type: concept
tags: [eda, statistics]
sources: [intro slides]
---
# Descriptive statistics

Descriptive statistics summarise a dataset in a few numbers.

**Centre (where the middle is):**
- **Mean** – the average. Pulled by outliers.
- **Median** – the middle value after sorting. Barely moved by outliers.
- **Mode** – the most common value. Useful for categories.

**Spread (how scattered):**
- **Variance** – average squared distance from the mean; **standard deviation** is its square root, in original units.
- **Range** – max minus min.
- **Interquartile range (IQR)** – Q3 − Q1, the spread of the middle 50%. Used for outlier rules.

**Shape:**
- **Skewness** – lopsidedness. Positive skew = long right tail (incomes, rainfall). Negative = long left tail.
- **Kurtosis** – how heavy the tails are, i.e. how often extreme values appear.

Example: weekly rainfall of 0, 0, 2, 5, 80 mm has mean 17.4 but median 2. The mean is misleading here.

## For the capstone
Report median and IQR for rainfall and soil moisture per region, not just mean and SD.

## Related
- [Mean vs median for skewed data](mean-vs-median-for-skewed-data.md)
- [Exploratory data analysis](exploratory-data-analysis.md)
- [Outlier detection](outlier-detection.md)
