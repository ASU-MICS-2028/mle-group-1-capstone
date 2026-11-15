---
summary: K-means alternates between assigning points to the nearest centre and moving centres to the mean.
type: procedure
tags: [unsupervised, clustering, k-means, exam]
sources: [unsupervised slides, lecture-08 recording]
---
# K-means clustering

K-means splits data into **k** groups. You choose k before you start, so k is a hyperparameter. Each group is represented by one point, its **centroid** (centre).

The algorithm (Lloyd's algorithm):

1. **Initialise**: place k centroids (randomly, or better with k-means++).
2. **Assign**: give every point to its nearest centroid. Each point belongs to exactly one cluster.
3. **Update**: move each centroid to the mean of the points assigned to it. Average the x values and the y values separately; a centroid is a coordinate, not one number.
4. **Repeat** steps 2 and 3 until the assignments stop changing. This is convergence.

The lecturer's analogy: the government builds 3 markets at random spots. Each resident goes to the nearest market. Each market then moves to the centre of its customers. Some residents now find another market closer and switch. The markets move again, until nobody switches.

The regions that end up belonging to each centroid form a **Voronoi partition**: each region is the set of points closer to that centroid than to any other.

A learning objective of the unit is to do these steps **by hand** (distances, assignment, centroid update). See the worked example note.

## For the capstone
Not our classifier. Could be used in EDA to group region-weeks into "dry", "wet", "extreme" rainfall regimes.

## Related
- [K-means worked example](k-means-worked-example.md)
- [K-means objective and convergence](k-means-objective-and-convergence.md)
- [K-means++ initialisation](k-means-plus-plus-initialisation.md)
- [Choosing k with the elbow method](elbow-method.md)
- [K-means limitations](k-means-limitations.md)
