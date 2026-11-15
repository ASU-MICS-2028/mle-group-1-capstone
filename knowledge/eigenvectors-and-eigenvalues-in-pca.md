---
summary: In PCA, eigenvectors of the covariance matrix give component directions; eigenvalues give their variance.
type: concept
tags: [pca, linear-algebra, exam]
sources: [unsupervised slides]
---
# Eigenvectors and eigenvalues in PCA

An **eigenvector** v of a matrix C is a direction that C only stretches, never turns:

C v = λ v

The stretch factor λ is the **eigenvalue**.

In PCA, C is the covariance matrix of the standardised data. Then:

- each **eigenvector** is the direction of a principal component;
- its **eigenvalue** is the amount of variance the data has along that direction, so it measures the component's importance.

Sort eigenvalues from largest to smallest. The eigenvector with the largest eigenvalue is PC1, the next is PC2, and so on. Because C is symmetric, the eigenvectors are at right angles to each other, which is why the PCs are orthogonal and uncorrelated.

Small example: for two perfectly standardised features with correlation 0.8, the covariance matrix is [[1, 0.8], [0.8, 1]]. Its eigenvalues are 1.8 and 0.2. The first eigenvector points along the diagonal (1, 1)/√2. PC1 alone keeps 1.8 / 2 = 90% of the variance.

In practice scikit-learn computes this for you (using SVD, a numerically safer route to the same answer).

## Related
- [Covariance matrix](covariance-matrix.md)
- [Explained variance ratio](explained-variance-ratio.md)
- [Principal component analysis](principal-component-analysis.md)
