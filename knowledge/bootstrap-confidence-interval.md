---
summary: Resample your data with replacement many times to see how much a statistic varies.
type: procedure
tags: [statistics, uncertainty, evaluation]
sources: [probability & sampling slides]
---
# Bootstrap confidence interval

The **bootstrap** estimates uncertainty without a formula:

1. From your n data points, draw n points **with replacement** (some appear twice, some not at all).
2. Compute the statistic (a mean, a recall, an AUC) on this resample.
3. Repeat many times (e.g. 2,000).
4. Take the 2.5th and 97.5th percentiles of the results → a 95% CI.

Why it works: resampling from your sample mimics the variation you would get from drawing new samples from the population.

Tiny example: test-set predictions on 100 weeks give recall 0.70. Bootstrapping the 100 weeks 2,000 times gives recalls from 0.55 to 0.83 in the middle 95%. Report "0.70 (0.55–0.83)".

**The catch:** resampling must copy how the data were really collected. Resampling single rows assumes rows are independent. If they come in groups, resample groups – see [Cluster bootstrap](cluster-bootstrap.md).

## For the capstone
Bootstrap the 2024–2025 test predictions to get CIs on recall, precision and PR-AUC, using whole weeks (or blocks of weeks) as the resampling unit.

## Related
- [Confidence interval](confidence-interval.md)
- [Cluster bootstrap](cluster-bootstrap.md)
- [Defend every number](defend-every-number.md)
