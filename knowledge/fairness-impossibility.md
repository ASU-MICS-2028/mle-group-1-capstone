---
summary: With unequal base rates, independence, separation and sufficiency cannot all hold, so pick one and justify it
type: concept
tags: [fairness, reading]
sources: [Barocas, Hardt & Narayanan, FML ch. 3]
---
# Fairness impossibility results

All three results hinge on **unequal base rates**: $P(Y=1\mid A)$ differs between groups.

- **Independence vs sufficiency:** if base rates differ, both cannot hold — equal flag rates force a score to mean different things in different groups.
- **Independence vs separation:** with binary $Y$, unequal base rates and a score that is at all informative, both cannot hold.
- **Separation vs sufficiency:** with unequal base rates (and non-zero false positive rate for a binary classifier), both cannot hold. So **a calibrated, accurate model will usually have unequal error rates across groups with different rates.**

Practical consequence: choose a **primary** criterion, justify it from the decision and the harms, and report the others so the trade-off is visible.

## For the capstone
Base rates differ hugely: Greater Accra has a positive in 21.6% of weeks against 6.4% across all regions. We cannot have both calibrated probabilities and equal recall per region. A defensible choice: keep probabilities calibrated for the dashboard, then use per-region thresholds to lift recall in low-rate regions, reporting the extra false alerts this costs.

## Related
- [Fairness definitions](fairness-definitions.md)
- [Fairness mitigation options](fairness-mitigation-options.md)
- [Groundsource dataset](groundsource-dataset.md)
