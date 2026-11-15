---
summary: Suspiciously high scores or one dominant feature usually mean leakage, not a great model.
type: concept
tags: [leakage, evaluation]
sources: [preprocessing & leakage slides]
---
# Leakage red flags

Signs that a model may be leaking:

1. **Suspiciously perfect scores** – 99%+ on a hard, noisy, real problem.
2. **One feature dominates** the feature importance.
3. **Real-world performance drops sharply** compared with test results.
4. **A feature would not exist yet** at prediction time.

The slides' last advice: question great results. When a score looks too good, investigate it as leakage first, before celebrating.

Small example: a flood model where "number of flood-related articles this week" has 80% of the importance is reading the label, not forecasting.

## For the capstone
After each model, look at feature importances and check: does any single feature explain almost everything? Does test performance beat what flood forecasting papers report? If yes, audit.

## Related
- [Data leakage](data-leakage.md)
- [Target leakage](target-leakage.md)
- [Leakage audit with before/after numbers](leakage-audit-before-after.md)
