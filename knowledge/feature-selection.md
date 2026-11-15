---
summary: Keep only helpful features via forward, backward, bidirectional or tree-based selection.
type: procedure
tags: [preprocessing, feature-engineering, dimensionality]
sources: [preprocessing & leakage slides, lecture-04 recording, intro slides]
---
# Feature selection

**Feature selection** keeps a subset of the original features. Benefits: faster training, often better accuracy, easier explanation, less overfitting.

Methods from the slides:
1. **Forward selection** – start with none; add the most useful feature one at a time; stop when adding more stops helping (e.g. at 15 of 20). Faster.
2. **Backward elimination** – start with all; remove the least useful one at a time while performance holds. Costs more compute.
3. **Bidirectional** – add and remove as you go.
4. **Tree-based** – use a decision tree's importances to rank features.

It differs from **feature extraction**, which builds *new* features (e.g. PCA) instead of picking from old ones.

Leakage warning: selection "learns" from data. Choose features using training (or validation) data only, never the test set, and redo it inside each CV fold.

## For the capstone
Select features using 2015–2022 (and 2023 for tuning). Never pick lags because they looked good on 2024–2025.

## Related
- [Curse of dimensionality](curse-of-dimensionality.md)
- [Feature engineering](feature-engineering.md)
- [Lasso regression](lasso-regression.md)
- [Split first, fit on train](split-first-fit-on-train.md)
