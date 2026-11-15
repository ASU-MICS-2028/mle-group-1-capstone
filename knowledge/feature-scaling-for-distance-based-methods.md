---
summary: Standardise features before k-means, PCA or any distance-based method, or big-range features dominate.
type: rule
tags: [preprocessing, scaling, unsupervised, pca, k-means]
sources: [unsupervised slides, lecture-08 recording, lecture-04 recording, preprocessing & leakage slides, lec5 slides]
---
# Feature scaling for distance-based methods

K-means, PCA and other distance- or variance-based methods treat a feature with a big range as more important, just because of its units.

Slide example: income runs 0–10,000 and age runs 18–70. A difference of 500 in income swamps a difference of 40 years in age. Clusters would be "income bands", and PC1 would just be income.

Fix: **standardise** each feature to a z-score,

z = (x − μ) / σ

where μ is the feature's mean and σ its standard deviation. After this every feature has mean 0 and spread 1. Min-max scaling to 0–1 is an alternative the lecturer also mentioned.

The preprocessing lecture made the same point for k-nearest neighbours, linear regression and gradient descent: scaling changes the range, not the information. Min-max maps to [0, 1] with (x − min) / (max − min); z-score gives mean 0, spread 1. Which works better is mostly found by trying. If you scale the *target*, map predictions back to real units at inference (de-normalise).

Two cautions:

- Compute μ and σ on the **training data only**, then apply them to validation and test data. Otherwise test information leaks into the model.
- Tree models (random forest, LightGBM) do not need scaling. Logistic regression and SVM do, for the same distance/size reasons. The survey slides list "forgetting to scale" as a top pitfall: SVM (especially RBF kernels) and kNN need it; for regularised logistic regression the penalty is unfair across features otherwise.

## For the capstone
Rainfall (mm), soil moisture (fraction), elevation (m) and built-up share (%) have very different ranges. Put a `StandardScaler` inside the scikit-learn pipeline for logistic regression and SVM, fitted on 2015–2022 only.

## Related
- [Clustering](clustering.md)
- [Principal component analysis](principal-component-analysis.md)
- [K-means limitations](k-means-limitations.md)
- [Support vector machine](support-vector-machine.md)
- [K-nearest neighbours](k-nearest-neighbours.md)
- [Ridge regression](ridge-regression.md)
