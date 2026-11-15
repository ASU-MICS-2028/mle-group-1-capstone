---
summary: Géron's HOMLP (Scikit-Learn & PyTorch, 2025) — practical chapters mapped to capstone steps
type: source
tags: [book, textbook]
sources: [Géron, Hands-On Machine Learning with Scikit-Learn and PyTorch, O'Reilly 2025; prosit-2 books.md]
---
# Book: HOMLP (Hands-On Machine Learning, Géron)

Primary course text, *Scikit-Learn and PyTorch* edition (Oct 2025). Not free: use library or O'Reilly access; the companion notebooks are free on the author's GitHub. Our team has only the free online appendix locally, so check notes against a library copy. **Chapter numbers differ from the older TensorFlow 3rd edition** (where SVMs were ch 5, trees ch 6, ensembles ch 7).

| Chapter (2025 ed.) | Key ideas (our paraphrase) | Capstone use |
|---|---|---|
| 2 End-to-end project | Pipelines, data prep, evaluation workflow | Repo structure, `Pipeline` to avoid leakage |
| 3 Classification | Precision/recall, threshold choice, PR vs ROC (prefer PR when positives are rare), `cross_val_predict` | PR-AUC headline, alert threshold |
| 4 Training linear models | Normal equation, gradient descent, learning curves, ridge/lasso/elastic net, logistic regression and log-loss | Logistic model and its derivation |
| 5 Decision trees | CART, Gini vs entropy, regularising depth/leaf size, instability | Tree derivation |
| 6 Ensembles & random forests | Bagging, OOB, random forests, gradient boosting, learning rate, early stopping, histogram boosting | Random forest, LightGBM |
| 7 Dimensionality reduction | PCA, curse of dimensionality | Optional: compress correlated rainfall features |
| 10 Neural nets with PyTorch | MLPs, BCE-with-logits, training loop | Not planned; logistic regression is a one-neuron net |
| Appendix C (online) | SVMs, kernels, hinge loss | SVM model |

## For the capstone
Chapter 3's threshold and PR-curve material maps directly onto alert-budget recall; chapter 6's early stopping onto LightGBM tuning on 2023.

## Related
- [Book: ISLR](book-islr.md)
- [Gradient boosting derivation](gradient-boosting-derivation.md)
- [Cost-based threshold derivation](cost-threshold-derivation.md)
