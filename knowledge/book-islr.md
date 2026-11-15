---
summary: ISLR/ISLP — the main free textbook; chapters 2–9 mapped to capstone steps
type: source
tags: [book, textbook]
sources: [James, Witten, Hastie, Tibshirani & Taylor, ISLR 2nd ed. / ISLP 2023; prosit-2 books.md]
---
# Book: ISLR (An Introduction to Statistical Learning)

James, Witten, Hastie, Tibshirani (and Taylor for the Python edition, ISLP, 2023). Primary course text. Free and legal from the authors at https://www.statlearning.com. Chapters 2–9 have the same numbering in ISLR 2nd ed. (R) and ISLP (Python).

| Chapter | Key ideas (our paraphrase) | Capstone use |
|---|---|---|
| 2 Statistical learning | Test vs training error; bias–variance; Bayes classifier; KNN | Why accuracy fails at 6.4% positives; model-family choice |
| 3 Linear regression | Least squares; dummies (k−1); residual plots; collinearity (VIF) | Collinear rainfall windows; [linear derivation](linear-regression-derivation.md) |
| 4 Classification | Logistic regression, odds ratios, ML fitting; thresholds; confusion matrix; ROC; confounding | Main interpretable model; threshold trade-off |
| 5 Resampling | Validation set, k-fold CV, bootstrap; preprocessing inside folds | Bootstrap CIs on PR-AUC across test weeks; rolling-origin validation extends the chapter's logic |
| 6 Regularisation | Ridge, lasso, choosing λ by CV, standardise first | L2 logistic regression; [ridge derivation](ridge-regression-derivation.md) |
| 8 Trees | Gini/entropy, pruning, bagging, random forests, importance, boosting (Alg. 8.2) | Random forest and LightGBM; [tree derivation](decision-tree-split-derivation.md), [boosting](gradient-boosting-derivation.md) |
| 9 SVMs | Margins, C, kernels, hinge-loss view, scores not probabilities | SVM model; [SVM note](svm-derivation.md) |

Not well covered: probability calibration in depth, SHAP, fairness metrics, and temporal/spatial CV — use scikit-learn docs, Molnar, FML and Roberts et al. (2017).

## For the capstone
Chapters 4, 5 and 8 carry most of the work; cite eq. numbers in the Methods section derivations.

## Related
- [Book: HOMLP](book-homlp.md)
- [Book: Interpretable Machine Learning](book-molnar-iml.md)
- [Capstone resources](capstone-resources.md)
