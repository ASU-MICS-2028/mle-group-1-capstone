---
summary: Train fits the model, validation picks between models, test grades the final choice once.
type: concept
tags: [model-selection, evaluation, splitting]
sources: [lecture-06 recording, lec4 slides, lec5 slides, intro slides]
---
# Train, validation and test sets

Grading a model on the data it trained on tells you nothing about new data. The lecturer compared it to memorising past exam questions when you know they will be reused: it is **cheating**, a form of leakage.

So split the data three ways:

| set | used for |
|---|---|
| training | fit each candidate model's parameters |
| validation | compare candidates and tune hyperparameters |
| test | grade the single chosen model, once, at the very end |

Why a separate validation set? If you try ten models and keep the one with the best *test* score, you have indirectly tuned on the test set, and that score is now too optimistic.

The workflow:
1. Lock the test set away.
2. Choose models and hyperparameters using the validation set (or k-fold CV inside the training data).
3. Refit the winner on train + validation.
4. Score it on the test set once and report that number.

The intro slides suggest rough sizes: 70–80% training, 10–15% validation, 15–30% test. Those are for a random split; for time-ordered data, split by date instead.

With small data a fixed split wastes rows (100 rows split 40/30/30 leaves only 40 to train on), which is where k-fold cross-validation helps.

Anything that learns from data (scalers, imputers, encoders, feature selection) must be fitted on the training part only.

## For the capstone
Ours is a time-ordered split: train 2015–2022, tune 2023, test 2024–2025. The test years are opened once, after all choices are frozen.

## Related
- [Temporal split](temporal-split.md)
- [K-fold cross-validation](k-fold-cross-validation.md)
- [Never tune on the test set](never-tune-on-the-test-set.md)
- [Generalisation](generalisation.md)
