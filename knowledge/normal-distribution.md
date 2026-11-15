---
summary: The normal is the symmetric bell curve; 68% within 1 SD, 95% within 2 SD.
type: concept
tags: [probability]
sources: [lecture-03 recording, probability & sampling slides]
---
# Normal (Gaussian) distribution

The normal distribution N(μ, σ) is the bell curve: symmetric around the mean μ, with spread set by the standard deviation σ, and no upper or lower limit.

- About **68%** of values lie within 1σ of the mean.
- About **95%** lie within 2σ.

Why it shows up everywhere:
- measurement error is often the sum of many small effects;
- the Central Limit Theorem makes *averages* roughly normal;
- linear regression with squared error is the same as assuming normal noise (minimising MSE = maximising the normal likelihood).

The lecturer's local example: exam grading "on a curve", where fixed shares of candidates get each grade, so a score of 89 can get a lower grade if the top slice is filled by 90s.

Other continuous shapes from the slides: **uniform** (flat, all values equally likely), **exponential** (waiting times, e.g. until the next trotro), **log-normal** (positive and right-skewed, like incomes), **beta** (values between 0 and 1, like proportions).

## For the capstone
Weekly rainfall is not normal: it is positive, has many near-zero weeks and a long right tail. Expect to log-transform it for linear models.

## Related
- [Central limit theorem](central-limit-theorem.md)
- [PMF vs PDF](pmf-vs-pdf.md)
- [Mean vs median for skewed data](mean-vs-median-for-skewed-data.md)
