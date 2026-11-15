---
summary: Feature engineering builds and picks inputs that expose the signal, using domain knowledge.
type: concept
tags: [feature-engineering, preprocessing]
sources: [intro slides, preprocessing & leakage slides, lecture-04 recording]
---
# Feature engineering

**Feature engineering** turns raw data into inputs a model can learn from, and keeps the useful ones. It often improves results more than switching algorithms. It depends on the problem and needs domain knowledge.

Main moves:
- **Construct** new attributes from old ones (*attribute construction*): height × width → area; height and weight → BMI.
- **Transform** a feature: scale it, log it to tame skew, bin it into ranges.
- **Encode** categories as numbers.
- **Extract** a new compact set (e.g. PCA components, aggregates).
- **Select** a subset of the original features.

The lecturer linked good constructed features to **interpretability**: a meaningful feature (like BMI) is easier to explain than raw columns.

When does it hurt? (a slide discussion question) When a feature leaks the target, when it is computed using test data, or when piles of noisy features cause overfitting.

## For the capstone
Candidate features: rainfall over the last 1, 3 and 7 days and previous weeks (lags), rainfall above a region's usual level (anomaly), soil moisture before the week, slope/elevation, built-up share. Each must only use information available at the prediction moment.

## Related
- [Categorical encoding](categorical-encoding.md)
- [Feature selection](feature-selection.md)
- [Feature scaling for distance-based methods](feature-scaling-for-distance-based-methods.md)
- [Temporal leakage](temporal-leakage.md)
