---
summary: Golden rule — split first, learn every preprocessing statistic from training data, apply unchanged elsewhere.
type: rule
tags: [leakage, preprocessing, lecturer-emphasis]
sources: [preprocessing & leakage slides, lecture-04 recording, lecture-02 recording]
---
# Split first, fit on train

The golden rule of the preprocessing and leakage lecture:

**Raw data → split → fit on train → apply to validation/test → evaluate.**

Every number a preprocessing step needs – means, medians, mins, maxes, category lists, encodings, selected features, imputation models – is learned **only from the training data**. The same fitted step is then applied, unchanged, to validation data, test data and new real-world inputs.

The slide's test: *if the test set could influence any number used during training, that is leakage.*

The lecturer's framing: think of preprocessing as **part of the model**, not something done before it. Preprocessing and leakage prevention are one discipline.

Prevention checklist from the slides:
1. Split before you preprocess.
2. Fit scalers, imputers and encoders on train only.
3. Use pipelines (preprocessing + model in one object).
4. Respect time order.
5. Check for duplicates across splits.
6. Question great results.

## For the capstone
One scikit-learn `Pipeline` per model, fitted on 2015–2022; the dashboard uses the same saved pipeline for new weeks.

## Related
- [Train-test contamination](train-test-contamination.md)
- [Preprocessing inside cross-validation](preprocessing-inside-cross-validation.md)
- [Train, validation and test sets](train-validation-test-split.md)
