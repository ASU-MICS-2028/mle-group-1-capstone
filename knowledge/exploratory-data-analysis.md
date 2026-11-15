---
summary: EDA means summarising and plotting data to find patterns and problems before modelling.
type: procedure
tags: [eda, pipeline]
sources: [intro slides, Terms notes, lecture-02 recording]
---
# Exploratory data analysis (EDA)

**EDA** is the step where you look hard at the data before building any model. The goal is to spot relationships and problems early.

Typical EDA:
- **Summary statistics** – mean, median, standard deviation, min/max, counts of missing values per column.
- **Plots** – histograms (shape of one variable), scatter plots (two variables together), box plots, time plots.
- **Outlier checks** – values far from the rest.
- **Class balance** – how rare is the positive class?
- **Coverage** – which groups, places or periods have little data?

In Prosit 1 the lecturer asked for an EDA "something to show" in week 2, including a map that shaded districts by how much data they had, so under-sampled rural and border areas stood out.

EDA guides later choices: a skewed histogram suggests a log transform; many missing values suggest an imputation plan; a rare class suggests different metrics.

Careful: if EDA results drive feature choices, do the decisive EDA on training data only, so test data does not shape the model.

## For the capstone
Plot flood weeks per region per year, rainfall distributions, a map of reported floods per region (to show media-coverage gaps), and the flood rate by month (rainy-season pattern).

## Related
- [Descriptive statistics](descriptive-statistics.md)
- [Outlier detection](outlier-detection.md)
- [Sampling bias](sampling-bias.md)
- [The ML pipeline](ml-pipeline.md)
