---
summary: Out-of-bag error tests each tree on the rows its bootstrap missed; it leaks on time or grouped data.
type: concept
tags: [ensembles, validation]
sources: [lecture-07 recording, lec5 slides]
---
# Out-of-bag (OOB) error

Each tree in a random forest is trained on a bootstrap sample that leaves out about 37% of the rows. Those left-out rows are that tree's **out-of-bag** rows. Score every row using only the trees that did not see it, and average: that is the OOB score. It behaves roughly like a cross-validated score, and it comes free with training (`oob_score=True` in scikit-learn).

The lecturer described this as the forest having a kind of built-in validation, so that a separate validation set is not needed.

**Caution — this does not hold for our kind of data.** OOB treats every row as independent and picks left-out rows at random. If rows are ordered in time or grouped:
- a tree can train on the week before and the week after a left-out week, which is temporal leakage;
- repeated entities (the same region, the same customer) sit on both sides.

So OOB will look too optimistic. It is fine as a quick sanity check on i.i.d. data, but it does not replace a proper time-ordered validation.

## For the capstone
Do not report OOB scores as our validation result. Use the 2023 tuning year. If we print OOB at all, note that it is optimistic because region-weeks are not independent.

## Related
- [Bagging](bagging.md)
- [Random forest](random-forest.md)
- [Temporal leakage in cross-validation](temporal-leakage-in-cross-validation.md)
