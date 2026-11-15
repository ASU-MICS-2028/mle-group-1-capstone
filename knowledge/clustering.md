---
summary: Clustering groups unlabelled points so that close points share a group.
type: concept
tags: [unsupervised, clustering]
sources: [unsupervised slides, lecture-08 recording]
---
# Clustering

Clustering puts data points into groups (clusters). Points in the same group should be similar. Points in different groups should be different. Nobody tells the algorithm the right groups; it infers them. That is why the slides describe the goal as "infer labels".

"Similar" usually means "close" under a distance measure:

- **Euclidean distance**: the straight-line distance from school maths. For (1,1) and (4,5) it is √(3² + 4²) = 5.
- **Manhattan distance**: add the absolute differences, like walking city blocks. For the same points it is 3 + 4 = 7.

Because everything depends on distance, two practical rules follow:

1. **Scale features first.** If one feature runs 0–10,000 and another 0–1, the big one decides every distance.
2. **Encode non-numbers.** Text categories must become numbers before you can measure distance.

A related task is **anomaly detection**: points that sit far from every cluster may be errors or rare events.

Example: a folder of unlabelled photos of birds, landscapes and lions. A good clustering recovers those three groups without being told they exist.

## For the capstone
Clustering the 16 regions by rainfall and terrain could show which regions behave alike. That is useful for EDA and for explaining results to NADMO, not as the classifier.

## Related
- [Unsupervised learning](unsupervised-learning.md)
- [K-means clustering](k-means-clustering.md)
- [Feature scaling for distance-based methods](feature-scaling-for-distance-based-methods.md)
