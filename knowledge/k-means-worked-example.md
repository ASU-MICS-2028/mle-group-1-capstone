---
summary: A two-cluster k-means run by hand on five points, converging after two iterations.
type: procedure
tags: [unsupervised, k-means, exam, worked-example]
sources: [unsupervised slides, lecture-08 recording, prosit-2 lecture notes]
---
# K-means worked example

Points: A(1,1), B(2,1), C(4,3), D(5,4), E(1,2). k = 2. Start with μ₁ = (1,1) and μ₂ = (5,4).

(The slide uses μ₂ = (5,5); the recording's board work only makes sense with (5,4). The result is the same either way.)

**Iteration 1: squared distances**

| Point | to μ₁ | to μ₂ | Cluster |
|---|---|---|---|
| A | 0 | 25 | 1 |
| B | 1 | 18 | 1 |
| C | 13 | 2 | 2 |
| D | 25 | 0 | 2 |
| E | 1 | 20 | 1 |

Comparing squared distances gives the same winner as comparing distances, and saves square roots.

**Update**

- μ₁ = mean(A, B, E) = ((1+2+1)/3, (1+1+2)/3) ≈ (1.33, 1.33)
- μ₂ = mean(C, D) = (4.5, 3.5)

**Iteration 2**: recompute distances. Every point keeps its cluster (for example, C is about 0.71 from μ₂ and 3.14 from μ₁). Nothing changed, so the algorithm has converged.

Final clusters: {A, B, E} and {C, D}. Objective J (sum of squared distances to own centroid) ≈ 0.22 + 0.56 + 0.56 + 0.50 + 0.50 ≈ 2.33.

Exam tip: show the distance table, the assignment, and the centroid as an (x, y) pair. The lecturer stressed the centroid is a coordinate.

## Related
- [K-means clustering](k-means-clustering.md)
- [K-means objective and convergence](k-means-objective-and-convergence.md)
