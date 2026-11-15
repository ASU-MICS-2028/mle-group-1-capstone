---
summary: PCA rotates the data onto new uncorrelated axes ordered by how much variance each one captures.
type: concept
tags: [unsupervised, pca, dimensionality-reduction, exam]
sources: [unsupervised slides, prosit-2 lecture notes]
---
# Principal component analysis (PCA)

PCA replaces many correlated features with a few new ones, called **principal components (PCs)**. Each PC is a weighted mix of the original features.

Properties of the PCs:

- **PC1** points in the direction where the data spreads out most (highest variance).
- **PC2** captures the next-most variance, and so on.
- PCs are **orthogonal** (at right angles) and **uncorrelated** with each other.
- They are **ordered by importance**, so you keep the first few and drop the rest.

PCA treats variance as information: a direction where every point has the same value tells you nothing.

Intuition: two standardised features that move together, such as "rain this week" and "rain last week", form a narrow diagonal cloud. PC1 runs along the diagonal. PC2 is the thin direction across it. Keeping only PC1 loses little.

Steps (from the slides):

1. Collect the data.
2. Standardise each feature.
3. Compute the covariance matrix.
4. Find its eigenvalues and eigenvectors.
5. Sort by eigenvalue, largest first.
6. Keep the top k components.
7. Project the data onto them to get the new features.

PCA is unsupervised: it ignores the label. So the direction of most variance is not always the direction that best separates floods from non-floods.

## Related
- [Feature scaling for distance-based methods](feature-scaling-for-distance-based-methods.md)
- [Covariance matrix](covariance-matrix.md)
- [Eigenvectors and eigenvalues in PCA](eigenvectors-and-eigenvalues-in-pca.md)
- [Explained variance ratio](explained-variance-ratio.md)
- [PCA limitations](pca-limitations.md)
