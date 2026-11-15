---
summary: K-fold CV rotates which slice of the training data is held out, then averages the K scores.
type: procedure
tags: [model-selection, cross-validation]
sources: [lecture-06 recording, lecture-07 recording, lec4 slides, MIT 6.390 ch2]
---
# K-fold cross-validation

When data is limited, a single validation set wastes rows and gives a noisy score. K-fold cross-validation uses all the training data for both fitting and checking:

1. Keep the test set locked away.
2. Cut the remaining data into K equal parts (folds).
3. Train on K − 1 folds, score on the one left out.
4. Repeat K times so every fold is left out once.
5. Average the K scores. Pick the model or setting with the best average.

**Leave-one-out (LOOCV)** is the extreme case K = number of examples: each round leaves out a single row. Useful for tiny datasets, but expensive.

**Choosing K** (a trade-off the lecturer discussed):
- small K (2 or 3): each model trains on little data, so the estimate is pessimistic and rough;
- large K (say 100): each model sees almost all the data, but you pay for 100 fits;
- K = 5 or 10 is the usual compromise.

The lecturer recommended k-fold CV for hyperparameter tuning and model selection throughout the course.

**Warning:** plain k-fold shuffles rows randomly. That is wrong when rows are ordered in time or grouped (same customer, same region), because information leaks between folds.

## For the capstone
Do not use shuffled k-fold on our region-weeks. Use the fixed 2023 tuning year, or a forward-chaining time-series split inside 2015–2022.

## Related
- [Temporal leakage in cross-validation](temporal-leakage-in-cross-validation.md)
- [Cross-validation evaluates the algorithm](cross-validation-evaluates-the-algorithm.md)
- [Nested cross-validation](nested-cross-validation.md)
- [Train, validation and test sets](train-validation-test-split.md)
