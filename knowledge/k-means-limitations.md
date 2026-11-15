---
summary: K-means needs k fixed in advance, likes round blobs, and is pulled by outliers and unscaled features.
type: concept
tags: [unsupervised, k-means, limitations]
sources: [unsupervised slides, lecture-08 recording]
---
# K-means limitations

1. **k is fixed in advance.** If the data has five natural groups and you ask for three, k-means forces them into three.
2. **Choosing k is hard.** The slides call this the biggest problem.
3. **Local optima.** Results depend on the start; use k-means++ and several restarts.
4. **Round clusters only.** Each point goes to its nearest centre, so clusters come out as compact, similar-sized blobs. A ring shape or a long curved band gets cut up badly.
5. **Outliers pull centroids.** A centroid is a mean, and one far-away point drags the mean toward it.
6. **Scale and encoding matter.** Distances are meaningless if one feature has a much larger range, or if categories are not turned into numbers.

Our slides did not cover alternatives (hierarchical clustering, DBSCAN). Those methods exist partly to fix points 1 and 4.

## Related
- [K-means clustering](k-means-clustering.md)
- [Choosing k with the elbow method](elbow-method.md)
- [Feature scaling for distance-based methods](feature-scaling-for-distance-based-methods.md)
