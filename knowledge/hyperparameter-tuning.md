---
summary: Try hyperparameter settings on validation data (grid or random search) and keep the best.
type: procedure
tags: [hyperparameters, model-selection]
sources: [lecture-06 recording, lecture-07 recording, lec5 slides, MIT 6.390 ch2]
---
# Hyperparameter tuning

Hyperparameters (tree depth, C, learning rate, k …) cannot be learned by the model's own training. You find them by trying candidates and scoring each on data the model did not train on.

Ways to search:
- **Grid search:** try every combination from a list (C ∈ {0.01, 0.1, 1, 10} × penalty ∈ {L1, L2} = 8 fits per fold). Simple but explodes with many hyperparameters.
- **Random search:** sample combinations at random for a fixed budget. Usually finds good settings faster than a grid when only a few hyperparameters really matter.
- **Smarter search** (Bayesian optimisation, e.g. Optuna): uses past results to pick promising next tries.
- **Early stopping** for boosting picks the number of trees automatically.

Rules from the lectures:
1. Score candidates on a validation set or with cross-validation, **never on the test set**.
2. Search on a log scale for strength-type knobs (0.001, 0.01, 0.1 …), as the lecturer did for learning rates.
3. Refit the winner on all training + validation data before the final test.
4. If you report the tuning score itself, it is optimistic; nested CV or a separate test set fixes that.

Keep the search proportionate: the survey slides warn that more complexity does not mean better, and that you should add it only if validation scores improve.

## For the capstone
Tune each model on the 2023 tuning year with a modest random search, log every trial (including bad ones) to the results index, then freeze.

## Related
- [Hyperparameters](hyperparameters.md)
- [Never tune on the test set](never-tune-on-the-test-set.md)
- [Nested cross-validation](nested-cross-validation.md)
- [Boosting learning rate and early stopping](boosting-learning-rate-and-early-stopping.md)
