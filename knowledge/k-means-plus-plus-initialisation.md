---
summary: K-means++ picks starting centres far apart, chosen with probability proportional to squared distance.
type: procedure
tags: [unsupervised, k-means, initialisation]
sources: [unsupervised slides, lecture-08 recording]
---
# K-means++ initialisation

K-means results depend heavily on where the centroids start. Purely random starts can go wrong in two ways:

- two centroids land in the same true group;
- some true group gets no centroid at all.

Options from the slides: run many random restarts and keep the lowest J; pick points that are far apart (works, but outliers attract it); or use **k-means++**.

**K-means++**

1. Pick the first centre uniformly at random from the data points.
2. For each next centre (2 to k): pick a data point at random, with probability proportional to its **squared distance to the nearest centre already chosen**.

Far-away points are more likely to be picked, so the starting centres spread across the data. This usually means faster convergence and a better final J.

Small example: centre 1 is at (0,0). Point P is 1 away and point Q is 3 away. Q's weight is 9 and P's is 1, so Q is nine times as likely to become centre 2.

The lecturer described it loosely as "equal distances"; the probabilistic squared-distance rule above is the correct version. Scikit-learn's `KMeans` uses k-means++ by default. Fix `random_state` so runs are reproducible.

## Related
- [K-means clustering](k-means-clustering.md)
- [K-means objective and convergence](k-means-objective-and-convergence.md)
