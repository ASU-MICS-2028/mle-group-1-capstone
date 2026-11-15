---
summary: K-means lowers the within-cluster squared distance every step, so it stops, but often at a local optimum.
type: derivation
tags: [unsupervised, k-means, optimisation, exam]
sources: [unsupervised slides, lecture-08 recording]
---
# K-means objective and convergence

K-means minimises the **within-cluster sum of squares** (WCSS):

J = Σᵢ ‖xᵢ − μ_{zᵢ}‖²

In words: for every point, take the squared distance to its own centroid, and add them all up. Small J means tight clusters. Large J means spread-out clusters.

**Why it always stops**

- The *assign* step moves each point to its closest centroid. That can only lower J or leave it the same.
- The *update* step moves each centroid to the mean of its points. The mean is exactly the point that minimises the sum of squared distances to a set. So J again can only go down.
- J never rises, and there are only finitely many ways to assign points. So the loop must end.

**Why "stopped" is not "best"**

It ends at a **local optimum**. Picture three true groups. A bad start puts two centroids inside the big group and one centroid between the two small groups. Neither step can fix this, yet it is clearly worse than one centroid per group.

**Other facts from the slides**

- Worst-case number of iterations can be exponential, but in practice it converges fast.
- The slides' verdict: local optima and iteration count are not big issues in practice. Choosing k is the biggest problem.

## Related
- [K-means clustering](k-means-clustering.md)
- [K-means++ initialisation](k-means-plus-plus-initialisation.md)
- [Choosing k with the elbow method](elbow-method.md)
