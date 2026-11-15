---
summary: Quantify each suspected leak by scoring a leaky and a clean model on one test set
type: procedure
tags: [leakage, evaluation, audit]
sources: [prosit-1 notebook §9, prosit-2 learnings/03_feature_audit, prosit-2 AGENTS.md rule 2]
---
# Audit leaks by building the cheating version

Saying "we avoided leakage" earns little. Showing *how much* each leak would have faked earned full marks on the Prosit 1 leakage criterion (10/10).

Steps that worked:
1. List every suspected leak by type: pooled preprocessing, group leakage (same cluster/customer on both sides), post-treatment features, target encoding on all rows, future information.
2. For each, build the **leaky** pipeline and the **clean** one, differing only in that one thing.
3. Score both on the **same** held-out test set with the same metric.
4. Put them in one table: leak, leaky version, clean version, leaky score, clean score, gap. Save it as a CSV.
5. Explain small gaps too. In Prosit 1 pooled preprocessing changed AUC by only +0.0001, because there were few missing values. We still kept the clean pipeline, and said why.
6. Where a leaky column adds nothing measurable (collinear with another feature), argue the risk in words instead.

## For the capstone
Run this audit for: features computed with the current week's rainfall vs the previous week's, random vs temporal split, region target encoding on all years vs training years only, and any feature derived from the Groundsource reports. Save the table to `learnings/tables/`.

## Related
- [leaky-features-top-the-leaderboard.md](leaky-features-top-the-leaderboard.md)
- [shuffled-validation-inflates-scores.md](shuffled-validation-inflates-scores.md)
- [save-every-result-to-a-results-index.md](save-every-result-to-a-results-index.md)
- [../knowledge/data-leakage.md](../knowledge/data-leakage.md)
