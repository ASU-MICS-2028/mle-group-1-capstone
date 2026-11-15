---
summary: Each component's share of total variance, used to decide how many PCA components to keep.
type: concept
tags: [pca, model-selection]
sources: [unsupervised slides]
---
# Explained variance ratio

Rank eigenvalues from largest to smallest: λ₁ ≥ λ₂ ≥ λ₃ ≥ … ≥ λ_p.

The **explained variance ratio (EVR)** of component i is its share of the total:

EVR_i = λ_i / (λ₁ + λ₂ + … + λ_p)

Add the ratios from the top to get the **cumulative** explained variance. Keep enough components to reach a level you are happy with. A common rule of thumb (ours, not from the slides) is 90–95%.

Example: eigenvalues 4, 2, 1, 0.5, 0.5 (total 8). EVRs are 50%, 25%, 12.5%, 6.25%, 6.25%. Three components keep 87.5% of the variance with 3 columns instead of 5.

A plot of EVR against component number is called a scree plot. Like the k-means elbow, you look for where the curve flattens.

Slide error: the slide writes the ranking as "λ₁ ≥ λ₁ ≥ λ₁". It should read λ₁ ≥ λ₂ ≥ λ₃.

## Related
- [Eigenvectors and eigenvalues in PCA](eigenvectors-and-eigenvalues-in-pca.md)
- [Principal component analysis](principal-component-analysis.md)
- [Choosing k with the elbow method](elbow-method.md)
