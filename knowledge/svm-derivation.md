---
summary: The soft-margin SVM is hinge loss plus a ridge penalty; it outputs distances, not probabilities
type: derivation
tags: [derivation, svm, classification]
sources: [ISLR 9.5 eq. 9.25, 9.3.2, HOMLP online appendix C, prosit-2 derivations.md §e]
---
# SVM as loss + penalty

With labels $y_i\in\{-1,+1\}$ and $f(x)=\beta_0+x^T\beta$, the support vector classifier can be written (ISLR eq. 9.25) as
$$\min_\beta\;\sum_i\max\big[0,\,1-y_if(x_i)\big]+\lambda\lVert\beta\rVert^2 .$$

- **Hinge loss** $\max(0,1-yf)$ is exactly zero for points correctly classified beyond the margin. Only points on or inside the margin — the **support vectors** — affect the solution.
- Logistic regression uses $\log(1+e^{-yf})$, which is never exactly zero but has a similar shape, so the two often perform alike.
- $\lambda$ (or the budget/penalty $C$, roughly its inverse) trades margin width against violations: a bias–variance knob, tuned on validation data.
- **Kernels.** Replacing inner products with $K(x,x')=\exp(-\gamma\lVert x-x'\rVert^2)$ (RBF) gives non-linear boundaries without building features by hand. Because it uses distances, **standardise features first**.
- **Outputs.** An SVC returns a signed distance, not a probability. `SVC(probability=True)` adds Platt scaling with internal CV. Any probability or cost-threshold claim depends on that calibration step.
- Fitting cost grows at least quadratically with $n$.

## For the capstone
SVM (RBF) is one of the four compared models. Our table is small (~9,184 region-weeks), so cost is fine, but calibrate it on the 2023 tuning year before showing probabilities or comparing Brier scores.

## Related
- [Logistic regression derivation](logistic-regression-derivation.md)
- [Ridge regression derivation](ridge-regression-derivation.md)
- [Cost-based threshold derivation](cost-threshold-derivation.md)
