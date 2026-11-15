---
summary: A time split must train only on outcomes known before the test period starts
type: lesson
tags: [validation, temporal-split, leakage]
sources: [prosit-2 ADR 0014, prosit-2 ADR 0015, prosit-2 docs/log.md 26 Oct]
---
# A time split must respect when labels are known

Our first "older → newer" test in Prosit 2 was still slightly optimistic, and a reviewer's stricter split exposed it. Two faults:

1. **Learning from unfinished outcomes.** Training rows were older loans, but some were due *after* the test period began, so their outcome couldn't have been known on deployment day. That was 37% of the training rows in the first fold, then 13%, 10% and 5%.
2. **Days split across blocks.** The cut sometimes fell mid-day, putting the same customers on both sides.

The fix: whole days go into one block, and the training part keeps only rows whose outcome date is before the first day of the test block. We wrote both rules as asserts in the shared feature code. After the fix LightGBM's future-loan lift dropped from 7.16 to 6.08 while logistic barely moved (8.14 → 8.07), so the preference for the simple model became clear.

We also tested the assumption about *when* an outcome is known (grace periods of 0, 7, 30 days) rather than just asserting it.

## For the capstone
A news report of a flood may appear days after the event, and Groundsource dates may be publication dates. Decide which date defines the label week, check the lag, and make sure features for week *t* use only data available by the end of week *t−1*. Never let a split cut through a week.

## Related
- [shuffled-validation-inflates-scores.md](shuffled-validation-inflates-scores.md)
- [review-by-rerunning-from-a-fresh-clone.md](review-by-rerunning-from-a-fresh-clone.md)
- [../knowledge/temporal-split.md](../knowledge/temporal-split.md)
