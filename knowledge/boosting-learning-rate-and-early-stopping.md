---
summary: In boosting, a small learning rate needs more trees; early stopping on validation data picks the count.
type: procedure
tags: [boosting, hyperparameters, regularisation]
sources: [lec5 slides]
---
# Boosting: learning rate, tree count and early stopping

In gradient boosting the main knobs work together:

- **Learning rate η (shrinkage)**, between 0 and 1: how much of each new tree is added. Small η is safer but needs many trees. Typical: 0.01–0.1 with hundreds to thousands of trees.
- **Number of trees M:** too few underfits, too many overfits.
- **Tree depth:** depth 1 (stumps) gives an additive model with no interactions; deeper trees capture interactions.
- **Subsample:** train each tree on a random fraction of rows (stochastic gradient boosting). Adds randomness that reduces overfitting.
- **min_samples_leaf / min_child_samples:** stops leaves fitting a handful of rows.

Rule of thumb from the slide: many weak trees with a small step ≈ few strong trees with a big step, but the first usually generalises better.

**Early stopping:** set M large, watch the score on a validation set after each tree, and stop when it has not improved for a set number of rounds. That picks M automatically.

The validation set for early stopping must **not** be the test set; otherwise you have tuned on the test set.

## For the capstone
LightGBM: `learning_rate≈0.05`, large `n_estimators`, `early_stopping` on the 2023 tuning year with log loss or PR-AUC as the metric. Then refit with the found number of trees.

## Related
- [Gradient boosting](gradient-boosting.md)
- [Learning rate](learning-rate.md)
- [Never tune on the test set](never-tune-on-the-test-set.md)
