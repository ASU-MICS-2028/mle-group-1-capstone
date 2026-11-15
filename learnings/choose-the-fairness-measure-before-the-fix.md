---
summary: Decide which fairness criterion comes first, then compare mitigations against it
type: lesson
tags: [fairness, calibration, decision]
sources: [prosit-2 ADR 0020, prosit-2 learnings/11_fairness]
---
# Choose the fairness measure before the fix

The three common criteria can't all hold when base rates differ, and in Prosit 2 they did (first loans defaulted 10.9% vs 1.3%). We ranked them explicitly:

1. **Sufficiency first:** a given score means the same risk for everyone. Checked with calibration by group. No group was priced unfairly high.
2. **Separation second, and the harm we acted on:** equal error rates, especially good payers wrongly declined. First loans: 53% vs 8%, so this was the gap to fix.
3. **Independence reported only:** equal approval rates would ignore a real 8× difference in risk.

That ordering ruled options out. **Reweighing** narrowed the gap but priced first loans at 0.28× their real risk, breaking sufficiency, and raised harm for others (8% → 12%). **Group-specific cut-offs** cost more and still didn't equalise. We tested 11 options with costs and bootstrap ranges, then a 1,224-scenario grid, and chose a feature drop plus a policy change (small starter loans), not a modelling trick.

## For the capstone
State the priority in the Model Card before testing fixes. A reasonable order for floods: per-region calibration first (a 30% alert means 30% everywhere), per-region recall second (missed floods are the harm), alert-rate parity reported only. Then test mitigations against that order.

## Related
- [hiding-a-column-does-not-hide-the-group.md](hiding-a-column-does-not-hide-the-group.md)
- [write-pass-rules-before-the-stress-test.md](write-pass-rules-before-the-stress-test.md)
- [../knowledge/fairness-definitions.md](../knowledge/fairness-definitions.md)
