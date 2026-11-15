---
summary: A cross-validation score rates a learning procedure and its settings, not one particular fitted model.
type: concept
tags: [cross-validation, model-selection]
sources: [MIT 6.390 ch2]
---
# Cross-validation evaluates the algorithm, not the model

Each fold of cross-validation fits a **different** model, on different rows. So the averaged score is not the score of any single model. It is the score of the **learning procedure**: "logistic regression, with this preprocessing, with C = 0.1, trained on about this much data".

That has two consequences:
1. After CV picks the best procedure, you refit it on all the training data. The final model is a new fit that CV never scored directly. Its own performance is measured by the test set.
2. Everything inside the procedure must be redone inside each fold: scaling, imputing, encoding, feature selection, resampling. If you scale once on all the data before CV, the procedure being scored is not the one you will actually run, and information leaks between folds.

The MIT notes also list three sources of variation in test error: which training rows you happened to get, which test rows, and randomness in the algorithm (seeds). CV averages over the first.

## For the capstone
Wrap preprocessing and model in one scikit-learn `Pipeline` so the same procedure is refitted cleanly on each time split.

## Related
- [K-fold cross-validation](k-fold-cross-validation.md)
- [Nested cross-validation](nested-cross-validation.md)
- [Hyperparameters](hyperparameters.md)
