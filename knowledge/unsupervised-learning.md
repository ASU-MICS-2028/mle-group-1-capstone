---
summary: Unsupervised learning finds structure in data that has no labels.
type: concept
tags: [foundations, types-of-learning]
sources: [intro slides, Terms notes, unsupervised slides, lecture-08 recording]
---
# Unsupervised learning

Unsupervised learning works with inputs only. There are no labels and no "right answer" to compare against. The model looks for structure on its own.

Common tasks:
- **Clustering** – group similar points (e.g. customer segments).
- **Anomaly detection** – find points that look unusual (e.g. a strange bank transaction).
- **Dimensionality reduction** – squeeze many features into fewer while keeping the important information.

The slides nickname clustering "unsupervised classification" and dimensionality reduction "unsupervised regression". A common pattern is to reduce dimensions without labels first, then train a supervised model on the smaller feature set.

Because there is no ground truth, judging an unsupervised result is harder: you check whether the groups make sense to a domain expert.

## For the capstone
Not our main task, but clustering regions by climate or terrain could help EDA, and clustering is one way to spot outliers in the feature data.

## Related
- [Types of supervision](types-of-supervision.md)
- [Supervised learning](supervised-learning.md)
- [Outlier detection](outlier-detection.md)
- [Curse of dimensionality](curse-of-dimensionality.md)
- [Clustering](clustering.md)
- [Dimensionality reduction](dimensionality-reduction.md)
