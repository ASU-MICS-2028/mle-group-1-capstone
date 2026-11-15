---
summary: Find outliers with z-scores, the IQR rule or clustering; then decide if they are errors.
type: procedure
tags: [preprocessing, cleaning, eda]
sources: [intro slides, preprocessing & leakage slides, lecture-04 recording]
---
# Outlier detection

An **outlier** is a point far from the rest of the data. It can distort learning, but it can also be the most important point you have.

**Detect:**
- **Z-score** – how many standard deviations from the mean; flag |z| > 3.
- **IQR rule** – flag values below Q1 − 1.5·IQR or above Q3 + 1.5·IQR (1.5 is the usual convention; the slide does not state it).
- **Clustering** – group points by closeness; points near no cluster centre are suspects.

**Then decide what to do** (a separate step):
- remove it (if it is clearly an error, like age 600, and there are few);
- **cap** it at a limit (winsorising);
- transform the feature (e.g. log) so extremes matter less;
- keep it, if it is real.

The lecturer suggested checking feature importance if you are not sure whether an outlier matters.

## For the capstone
Extreme rainfall weeks are exactly the flood weeks we want to predict. Do **not** drop them as outliers; check only for impossible values (negative rain, sensor errors).

## Related
- [Descriptive statistics](descriptive-statistics.md)
- [Smoothing noisy data by binning](smoothing-by-binning.md)
- [Clustering](clustering.md)
