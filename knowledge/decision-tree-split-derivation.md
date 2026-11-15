---
summary: Trees split greedily to maximise impurity decrease (RSS, Gini, entropy) and are pruned by cost complexity
type: derivation
tags: [derivation, trees, lo3]
sources: [ISLR 8.1 eq. 8.1, 8.4–8.7, 8.2.2, HOMLP ch 5, prosit-2 derivations.md §d]
---
# Decision tree split criteria and pruning (derivation)

**Growing.** A tree cuts feature space into boxes and predicts a constant per box (mean for regression, class share for classification). CART tries every feature $j$ and cut $s$ and greedily picks the split maximising
$$\Delta I=I(P)-\tfrac{n_L}{n_P}I(L)-\tfrac{n_R}{n_P}I(R).$$

**Regression.** With $I$ = within-node variance, $n_P\Delta I=\text{RSS}(P)-[\text{RSS}(L)+\text{RSS}(R)]$. The parent RSS is fixed, so maximising variance reduction = minimising children's RSS (ISLR 8.1). Leaves predict the mean because it minimises squared error.

**Classification.** With class shares $\hat p_k$: error $1-\max_k\hat p_k$; Gini $\sum_k\hat p_k(1-\hat p_k)$ (two classes: $2\hat p(1-\hat p)$); entropy $-\sum_k\hat p_k\log\hat p_k$. All are 0 when pure and maximal at 50/50.

**Why not error rate.** Node of 1,000 rows, 18 positives. Split: 100 rows (15 positive) vs 900 rows (3 positive). Both children are still majority-negative, so error decrease is **0**; Gini falls from 0.0354 to 0.0315 (decrease 0.0039). Gini rewards isolating a 15%-risk group; error rate cannot see it. This matters with rare positives.

**Cost-complexity pruning.** Grow large $T_0$, then for each $\alpha$ find the subtree minimising
$$C_\alpha(T)=\sum_{m=1}^{|T|}\sum_{x_i\in R_m}(y_i-\hat y_{R_m})^2+\alpha|T| .$$
Weakest link: for internal node $t$, $g(t)=\frac{R(t)-R(T_t)}{|T_t|-1}$ (error added per leaf removed); repeatedly collapse the smallest, giving a nested sequence; choose $\alpha$ by validation (`ccp_alpha`).

**Importance caveat.** Impurity-based importance (MDI) is computed on training data, favours many-valued features and splits credit between correlated features. Confirm with permutation importance on held-out data or SHAP.

## For the capstone
Our candidate second LO3 derivation (random forest and LightGBM are built from these trees). With ~6.4% positive region-weeks, use Gini/entropy, and check permutation importance to see whether built-up share is acting as a proxy.

## Related
- [Gradient boosting derivation](gradient-boosting-derivation.md)
- [Proxy variables](proxy-variables.md)
- [Logistic regression derivation](logistic-regression-derivation.md)
