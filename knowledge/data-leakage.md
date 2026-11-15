---
summary: Leakage is information unavailable at prediction time sneaking into training, inflating scores.
type: concept
tags: [leakage, evaluation]
sources: [preprocessing & leakage slides, lecture-04 recording, lecture-02 recording]
---
# Data leakage

**Data leakage** happens when information that would **not be available at the moment of prediction** – often from the target itself or from the test set – gets into training. The model looks brilliant in testing because it is quietly cheating. Nothing crashes; the results are simply false.

The lecturer called leakage the "key hazard" of Prosit 1: a leaky model looks highly accurate (e.g. 98–99%) because it has effectively seen the test data.

Why it is dangerous:
- scores look amazing, better than the problem allows;
- performance collapses in real use, where the leaked information does not exist;
- teams waste time and trust on a model that was never good;
- it hides inside ordinary-looking preprocessing.

Four common types (each has its own note): target leakage, train-test contamination, temporal leakage, duplicate leakage.

The fix is almost always the same: split first, fit everything on training data only, respect time order, and be suspicious of great results.

## For the capstone
A flood classifier with near-perfect recall would be a red flag, not a win. Check every feature against the question "would NADMO have this value at the start of the week?"

## Related
- [Target leakage](target-leakage.md)
- [Train-test contamination](train-test-contamination.md)
- [Temporal leakage](temporal-leakage.md)
- [Duplicate leakage](duplicate-leakage.md)
- [Leakage red flags](leakage-red-flags.md)
- [Leakage audit with before/after numbers](leakage-audit-before-after.md)
