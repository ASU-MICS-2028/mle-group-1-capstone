---
summary: For time-ordered data, train on the past and test on the future, never a random shuffle.
type: rule
tags: [splitting, leakage, time-series]
sources: [preprocessing & leakage slides, lecture-04 recording]
---
# Temporal split

When rows are ordered in time, split the data **by date**: train on earlier periods, validate on a later one, test on the latest. Never shuffle time-ordered rows randomly into train and test.

Why:
- A random split puts weeks from the same storm on both sides, so the model "sees" the test period (temporal leakage).
- It tests the real use case: predicting the future from the past.
- It reveals **drift** – whether the patterns change over time.

The slides list "respect time order (chronological splits, never random shuffles for time data)" in the leakage prevention checklist.

Trade-off: the test period may differ from training (e.g. an unusually wet year), so one test window gives a noisy estimate. Report intervals and, if possible, check several forward windows.

## For the capstone
Train 2015–2022, tune 2023, test 2024–2025. Preprocessing is fitted on 2015–2022 only. The test years are opened once, after all choices are frozen.

## Related
- [Temporal leakage](temporal-leakage.md)
- [Temporal leakage in cross-validation](temporal-leakage-in-cross-validation.md)
- [Train, validation and test sets](train-validation-test-split.md)
- [Generalisation](generalisation.md)
