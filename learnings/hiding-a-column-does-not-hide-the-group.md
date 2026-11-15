---
summary: Dropping a sensitive column rarely removes the group; other features act as proxies
type: result
tags: [fairness, proxies, features]
sources: [prosit-2 learnings/11_fairness §3, prosit-2 ADR 0020]
---
# Hiding a column does not hide the group

In Prosit 2 we tested whether the remaining features could predict each group (a proxy check: fit a classifier for group membership, report AUC):

- country: AUC 1.00 with all features, 0.90–0.94 even after removing the obvious ones;
- first-time borrower: 1.00;
- lender: 0.98 from loan type alone, although lender ID was never a feature.

Then the mitigation test: **dropping the three tenure features backfired**. First-loan good payers wrongly declined went from 53% to 57%, because the other features still revealed tenure and the model lost useful signal. What worked was different: dropping three "borrow often" features that produced a harmful message, which cost nothing within noise, plus a policy fix (small starter loans). Even the free fix moved harm elsewhere: one lender's good payers went from 80% to 87% wrongly declined. We reported that too.

## For the capstone
Region is both the fairness group and the unit of prediction, and rainfall, terrain and built-up features will identify it almost perfectly. Don't claim fairness by dropping a region feature. Instead measure recall and false-alarm rate per region, and consider per-region calibration or thresholds as mitigations, checking whom each one moves harm to.

## Related
- [choose-the-fairness-measure-before-the-fix.md](choose-the-fairness-measure-before-the-fix.md)
- [normalise-by-exposure-before-comparing-regions.md](normalise-by-exposure-before-comparing-regions.md)
- [../knowledge/fairness-definitions.md](../knowledge/fairness-definitions.md)
