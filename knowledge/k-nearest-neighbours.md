---
summary: kNN stores the training data and predicts from the k closest examples by vote or average.
type: concept
tags: [knn, classification, regression]
sources: [lec5 slides, lecture-07 recording]
---
# k-nearest neighbours (kNN)

kNN learns nothing in advance. It just stores the training set (a **lazy learner**). To predict for a new point:
1. measure its distance to every training point (Euclidean by default; Manhattan is more robust to outliers; Hamming for categories);
2. take the k closest;
3. classification: majority vote. Regression: average. (A weighted version lets closer neighbours count more.)

Its assumption is simply that similar points have similar labels. It makes no assumption about the data's distribution (**non-parametric**).

**Choosing k** (a hyperparameter, by cross-validation):
- small k (1 or 3): wiggly boundary that follows noise → overfitting;
- large k: smooth boundary that misses local detail → underfitting;
- use an odd k for two classes to avoid ties.

Practical issues:
- **scale features first**, or the feature with the biggest units dominates the distance;
- prediction is slow, since every query compares with all n training points;
- irrelevant features and high dimensions hurt it (curse of dimensionality);
- with a **rare class**, the nearest neighbours are almost always from the majority class, so kNN rarely predicts the rare class.

## For the capstone
Not in our model list. The rare-class problem and slow prediction are fair reasons to give if asked why we skipped it. A "same week last year" or "most similar past week" lookup is a kNN-like baseline we could mention.

## Related
- [Curse of dimensionality](curse-of-dimensionality.md)
- [Feature scaling for distance-based methods](feature-scaling-for-distance-based-methods.md)
- [Class imbalance](class-imbalance.md)
