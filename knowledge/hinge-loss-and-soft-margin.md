---
summary: The soft-margin SVM uses hinge loss; C sets how strictly margin violations are punished.
type: concept
tags: [svm, loss, hyperparameters]
sources: [lec5 slides]
---
# Hinge loss and the soft margin

A **hard-margin** SVM demands that every point is on the right side with room to spare. It only works on perfectly separable data, and one outlier can wreck it.

The **soft margin** allows violations. Each point gets a slack ξ ≥ 0 measuring how far it breaks the margin. The SVM minimises:

½‖w‖² + C · Σ ξᵢ

The penalty per point is the **hinge loss**: max(0, 1 − y·(w·x + b)).
- correct and outside the margin (margin z ≥ 1): loss 0;
- inside the margin or wrong: loss grows in a straight line.

Unlike logistic loss, hinge loss is exactly zero for comfortably correct points, which is why only the support vectors matter.

**C is the strictness knob:**
- **large C:** violations are expensive → narrow margin, few training errors, risk of overfitting;
- **small C:** violations are cheap → wide margin, more training errors allowed, smoother boundary.

Choose C by cross-validation (with γ if using an RBF kernel). Note scikit-learn's C here is like logistic regression's C: bigger means *less* regularisation.

## Related
- [Support vector machine](support-vector-machine.md)
- [Classification margin](classification-margin.md)
- [Kernel trick](kernel-trick.md)
