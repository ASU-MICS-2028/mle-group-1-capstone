---
summary: PCA components are hard to interpret, linear only, sensitive to scale and outliers, and lose some information.
type: concept
tags: [pca, limitations, explainability]
sources: [unsupervised slides, prosit-2 lecture notes]
---
# PCA limitations

From the slides' benefits-and-challenges table:

- **Hard to interpret.** A component is a mix of all features. "PC3 was high" means nothing to a decision-maker.
- **Sensitive to scaling.** Unstandardised data gives components that just follow the biggest-unit feature.
- **Linear only.** PCA finds straight-line directions. Curved structure is missed.
- **Information loss.** Dropped components carry some variance, and sometimes that variance mattered.
- **Outliers distort it.** Variance is driven by squared distances, so a few extreme points can tilt PC1.
- **Ignores the label.** Highest variance is not the same as most useful for prediction.

And a leakage rule: PCA is a *fitted* transform. Fit it on training data only, inside the pipeline, then apply it to validation and test data.

## For the capstone
NADMO officers need reasons such as "heavy rain for three days and saturated soil". Keep original features in the deployed model so explanations stay readable; use PCA, if at all, only for EDA plots.

## Related
- [Principal component analysis](principal-component-analysis.md)
- [Feature scaling for distance-based methods](feature-scaling-for-distance-based-methods.md)
- [Black-box models and explainability](black-box-models-and-explainability.md)
