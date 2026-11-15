---
summary: Class weights shift every predicted log-odds by log(w₁/w₀), so weighted models are miscalibrated
type: derivation
tags: [derivation, classification, imbalance, calibration]
sources: [prosit-2 derivations.md §b.6–b.7, scikit-learn class_weight docs]
---
# Class weights distort probabilities (derivation)

**Weighted loss.** With weight $w_1$ on positives and $w_0$ on negatives,
$$\text{NLL}_w=-\sum_i\big[w_1y_i\log p_i+w_0(1-y_i)\log(1-p_i)\big],$$
gradient $X^T\Omega(p-y)$ with $\Omega=\text{diag}(w_{y_i})$. scikit-learn's `class_weight="balanced"` uses $w_c=n/(2n_c)$, so $w_1/w_0=(1-\pi)/\pi$ for base rate $\pi$.

**Best prediction at a point.** Let the true probability at $x$ be $q$. Expected weighted loss $g(p)=-[w_1q\log p+w_0(1-q)\log(1-p)]$. Setting $g'(p)=0$:
$$w_1q(1-p)=w_0(1-q)p\;\Rightarrow\;\operatorname{logit}(p)=\operatorname{logit}(q)+\log\frac{w_1}{w_0}.$$
Unweighted, $p=q$ (log-loss rewards honest probabilities). Weighted, **every log-odds is inflated by the same constant**.

**Consequences.**
- Ranking is (almost) unchanged: adding a constant to all log-odds keeps the order, so ROC-AUC and PR-AUC barely move.
- Probabilities, Brier score, log-loss, reliability curves and cost-based thresholds are all wrong.
- Fixes: subtract $\log(w_1/w_0)$ analytically; recalibrate on held-out data (Platt or isotonic, fitted inside validation, never on test); or train unweighted and handle imbalance through the threshold.
- Same effect in boosting (`scale_pos_weight`, `is_unbalance`) and neural nets (`pos_weight`).

**Worked number.** With $\pi=0.064$ (our region-week rate), $w_1/w_0=0.936/0.064\approx14.6$, $\log\approx2.68$. A balanced model's "50%" corresponds to true odds $1/14.6$, i.e. $q\approx6.4\%$ — the base rate.

## For the capstone
The dashboard shows probabilities to NADMO officers, so any weighted model must be recalibrated (on 2023) before display, and reliability diagrams reported before and after.

## Related
- [Logistic regression derivation](logistic-regression-derivation.md)
- [Cost-based threshold derivation](cost-threshold-derivation.md)
- [Gradient boosting derivation](gradient-boosting-derivation.md)
