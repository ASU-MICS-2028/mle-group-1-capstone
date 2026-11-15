---
summary: Plot k-means loss against k and pick the k where extra clusters stop helping much.
type: procedure
tags: [unsupervised, k-means, model-selection]
sources: [unsupervised slides, lecture-08 recording]
---
# Choosing k with the elbow method

You cannot pick k by minimising J. J always falls as k grows. With one cluster per point, J is zero, which is useless.

The elbow heuristic:

1. Run k-means for k = 1, 2, 3, ... (with k-means++).
2. Record J for each k.
3. Plot J against k.
4. Pick the k after which adding clusters gives only a small drop. The curve bends like an elbow there.

Board example from the lecture: J falls steeply up to about k = 5 (J ≈ 90), then flattens (k = 6 → 85, k = 7 → 80). So pick k ≈ 5.

The slides call choosing k the **biggest problem** with k-means. The elbow is a judgement call; sometimes there is no clear bend. Treat it like hyperparameter tuning done before the final run.

## Related
- [K-means clustering](k-means-clustering.md)
- [K-means limitations](k-means-limitations.md)
