---
summary: The covariance matrix holds every feature's variance and every pair's co-movement; PCA starts from it.
type: concept
tags: [pca, statistics, linear-algebra]
sources: [unsupervised slides]
---
# Covariance matrix

**Covariance** measures whether two features move together:

Cov(X, Y) = Σ (X − X̄)(Y − Ȳ) / (n − 1)

- Positive: when X is above its mean, Y tends to be above its mean too.
- Negative: they move in opposite directions.
- Near zero: no linear link.

**Variance** is just a feature's covariance with itself: how spread out it is.

The **covariance matrix** puts all of these in a square table. For two features:

| | X₁ | X₂ |
|---|---|---|
| X₁ | Var(X₁) | Cov(X₁, X₂) |
| X₂ | Cov(X₂, X₁) | Var(X₂) |

Variances sit on the diagonal. The matrix is symmetric, because Cov(X₁, X₂) = Cov(X₂, X₁). With d features it is d × d.

Tiny example: rainfall and soil moisture over five weeks, both standardised. If wet weeks have wet soil, the off-diagonal entry is large and positive. PCA will then merge them into one strong component.

If the data is standardised first, the covariance matrix equals the correlation matrix.

## Related
- [Principal component analysis](principal-component-analysis.md)
- [Eigenvectors and eigenvalues in PCA](eigenvectors-and-eigenvalues-in-pca.md)
