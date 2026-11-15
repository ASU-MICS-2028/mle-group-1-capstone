---
summary: Nested CV tunes in an inner loop and scores in an outer loop, giving an honest estimate.
type: procedure
tags: [cross-validation, model-selection]
sources: [lec5 slides]
---
# Nested cross-validation

Problem: if you use cross-validation to pick hyperparameters and then report that same CV score, the score is too optimistic. You picked the setting that happened to do best on those folds.

Nested CV fixes it with two loops:
- the **outer loop** splits data into K outer folds. Each outer fold is held out as a mini test set;
- the **inner loop** runs ordinary CV on the remaining outer-training data to choose hyperparameters;
- the chosen setting is refitted on the outer-training data and scored on the held-out outer fold;
- the average of the outer scores is the honest estimate.

Example: 5 outer × 3 inner folds, 10 settings → 5 × 3 × 10 = 150 inner fits plus 5 outer refits. It is expensive.

Note the outer score describes the whole procedure "tune then fit", not one particular final model.

When you have a separate untouched test set (as we do), a single validation period plus that test set does the same job more cheaply.

## For the capstone
Not needed: our 2023 tuning year plus untouched 2024–2025 test years already separate tuning from scoring. If time allows, a forward-chaining nested scheme inside 2015–2023 would show how stable our model choice is.

## Related
- [K-fold cross-validation](k-fold-cross-validation.md)
- [Never tune on the test set](never-tune-on-the-test-set.md)
- [Cross-validation evaluates the algorithm](cross-validation-evaluates-the-algorithm.md)
