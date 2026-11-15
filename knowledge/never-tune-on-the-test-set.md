---
summary: Touching the test set during model selection is cheating and makes the reported score too optimistic.
type: rule
tags: [evaluation, model-selection, lecturer-emphasis]
sources: [lecture-06 recording, lecture-07 recording, lec5 slides]
---
# Never tune on the test set

The lecturer was blunt about this: training or selecting on the same data you test on is **cheating**. The model (or you) has already seen the answers.

What counts as "touching" the test set:
- picking the best model by its test score;
- choosing hyperparameters, thresholds or features after looking at test results;
- using the test set for early stopping in boosting;
- fitting a scaler, imputer or encoder on data that includes the test rows.

Each of these makes the test score an **optimistic** estimate. It no longer tells you how the model will do on truly new data.

The rule in practice:
1. Do every choice on training/validation data or inside cross-validation.
2. Freeze the whole pipeline.
3. Score on the test set once and report that number, even if it is disappointing.

If you need an honest estimate *and* tuning with little data, use nested cross-validation.

## For the capstone
Freeze the model, its hyperparameters and the alert threshold using 2023 only. Open 2024–2025 once. Record in the results index the date the test set was first used, and keep failed runs too.

## Related
- [Train, validation and test sets](train-validation-test-split.md)
- [Nested cross-validation](nested-cross-validation.md)
- [Choosing a classification threshold](classification-threshold.md)
