---
summary: A random forest is bagged decision trees that also see only a random subset of features at each split.
type: concept
tags: [ensembles, trees]
sources: [lecture-07 recording, lec5 slides, MIT 6.390 ch9]
---
# Random forest

A random forest = **bagging of decision trees + random feature subsets**.

- Each tree trains on its own bootstrap sample of rows.
- At every split, a tree may only consider a **random subset of features** (for example √p of p features) and picks the best among those. A plain tree would consider all of them.
- Predict by majority vote (classification) or average (regression).

The feature randomness makes the trees **different from each other** (decorrelated). Without it, every tree would split first on the same strong feature and they would make the same mistakes. Diverse trees make errors that cancel. The lecturer linked this diversity to better generalisation.

Key hyperparameters (scikit-learn): `n_estimators` (more trees = steadier, with diminishing returns, at a cost in time and memory), `max_features` (how much randomness), `max_depth` and `min_samples_leaf` (tree size), `class_weight="balanced"` for imbalanced classes.

Strengths: robust with little tuning, captures non-linear effects and interactions, no scaling needed, trees train in parallel.

Limits: slower and heavier than one tree; less interpretable; vote fractions are not well-calibrated probabilities; **regression forests cannot extrapolate** — they only average targets seen in training, so they never predict above the training maximum.

## For the capstone
One of our main models. Use `class_weight="balanced"` or tune the threshold, and calibrate the scores before showing them as probabilities on the dashboard.

## Related
- [Bagging](bagging.md)
- [Out-of-bag error](out-of-bag-error.md)
- [Feature importance](feature-importance.md)
- [Probability calibration](probability-calibration.md)
- [Bagging vs boosting](bagging-vs-boosting.md)
