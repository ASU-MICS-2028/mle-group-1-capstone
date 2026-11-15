---
summary: The mean of many independent observations is roughly normal, even if the data are not.
type: concept
tags: [sampling, statistics]
sources: [probability & sampling slides]
---
# Central limit theorem

The **central limit theorem (CLT)** says that the *average* of a sample becomes approximately normally distributed as the sample grows, even when the individual data points are not normal.

Slide example: nets per household is right-skewed, but if you take the mean of 30 households, 5,000 times, those means form a near-bell shape.

Key points:
- The CLT is about the **estimator** (the average), **not the data**. Your data stay skewed.
- It needs observations that are independent, each with limited influence.
- Skewed or heavy-tailed data need a bigger n before it kicks in.
- It is why standard errors, t-tests and averaged metrics work.

## For the capstone
Rainfall is very skewed; normal-based intervals on averages need enough weeks. Region-weeks in the same week are not independent (one storm hits many regions), which weakens the CLT's assumptions – a reason to prefer a block bootstrap.

## Related
- [Normal distribution](normal-distribution.md)
- [Law of large numbers](law-of-large-numbers.md)
- [Cluster bootstrap](cluster-bootstrap.md)
