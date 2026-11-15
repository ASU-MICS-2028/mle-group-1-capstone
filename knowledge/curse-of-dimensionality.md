---
summary: With many features, data gets sparse, distances blur and you need far more rows.
type: concept
tags: [preprocessing, dimensionality]
sources: [preprocessing & leakage slides, lecture-04 recording, lec5 slides, lecture-06 recording, lecture-08 recording]
---
# Curse of dimensionality

As you add features (dimensions), the space the data lives in grows very fast, and the data becomes **sparse**:

- To keep the same density of points, the number of rows must grow **exponentially** with each new feature.
- **Distances blur** – in high dimensions almost every point is about the same distance from every other, so "nearest neighbour" means little.
- **Everything looks unusual** – almost any point can look like an outlier.

Example: 10 points cover a 1-D line well. To cover a 2-D square equally densely you need 100; a 3-D cube needs 1,000.

The lecturer's practical rule: the number of features should only grow along with the number of records. Adding features endlessly leads to overfitting. Remedies: feature selection or dimensionality reduction.

The supervised-learning lectures returned to this twice: distance-based models such as kNN (and k-means) suffer most, and with thousands of features many are just noise the model still tries to learn. The survey slides add feature weighting as a remedy, and models that choose features themselves (trees, lasso) are less affected.

## For the capstone
Many rainfall lags × windows × sources can quickly give dozens of features for a few hundred flood weeks. Keep the feature set lean.

## Related
- [Feature selection](feature-selection.md)
- [Dimensionality reduction](dimensionality-reduction.md)
- [Overfitting](overfitting.md)
- [K-nearest neighbours](k-nearest-neighbours.md)
