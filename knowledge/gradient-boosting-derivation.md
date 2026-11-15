---
summary: Boosting is gradient descent in function space — each tree fits the negative gradient of the loss
type: derivation
tags: [derivation, ensembles, trees, boosting, lo3]
sources: [ISLR 8.2.3 Algorithm 8.2, HOMLP ch 6, Friedman 2001, Chen & Guestrin 2016 (XGBoost), prosit-2 derivations.md §c]
---
# Gradient boosting derivation

**Additive model.** $F_M(x)=F_0+\nu\sum_{m=1}^Mh_m(x)$: a constant start, many shallow trees $h_m$, learning rate $0<\nu\le1$.

**Pseudo-residuals.** Treat the current predictions $F_{m-1}(x_i)$ as free numbers. The steepest descent direction for each is
$$r_{im}=-\left[\frac{\partial L(y_i,F)}{\partial F}\right]_{F=F_{m-1}(x_i)} .$$
Each round: compute $r_{im}$; fit a small regression tree to $(x_i,r_{im})$ so the step generalises to unseen $x$; optionally reset each leaf to its best constant $\gamma_{jm}=\arg\min_\gamma\sum_{i\in R_{jm}}L(y_i,F_{m-1}(x_i)+\gamma)$; update $F_m=F_{m-1}+\nu h_m$.

**Squared loss.** $L=\frac12(y-F)^2\Rightarrow r=y-F$: ordinary residuals (ISLR Algorithm 8.2). $F_0=\bar y$.

**Log-loss (classification).** $F$ is a log-odds, $p=\sigma(F)$, $L=\log(1+e^F)-yF$, so $\partial L/\partial F=p-y$ and $r_{im}=y_i-p_i$. Start at $F_0=\operatorname{logit}(\bar y)$. Second derivative $p(1-p)$; one Newton step per leaf gives $\gamma_{jm}=\sum(y_i-p_i)/\sum p_i(1-p_i)$.

**XGBoost / LightGBM (second order).** With $g_i=\partial L/\partial F$, $h_i=\partial^2L/\partial F^2$ and leaf penalty $\frac12\lambda w^2$, a leaf's loss is approximately $Gw+\frac12(H+\lambda)w^2$, so
$$w^*=-\frac{G}{H+\lambda},\qquad\text{gain}=\tfrac12\Big[\tfrac{G_L^2}{H_L+\lambda}+\tfrac{G_R^2}{H_R+\lambda}-\tfrac{(G_L+G_R)^2}{H_L+H_R+\lambda}\Big]-\gamma .$$

**Knobs.** Smaller $\nu$ needs more trees but generalises better. Unlike random forests, boosting overfits with too many trees: use early stopping on a validation set. Tree depth sets interaction order (stumps = additive). Row/column subsampling regularises. Boosting mainly cuts bias; forests mainly cut variance. Class weights scale $g_i,h_i$ and inflate probabilities, so recalibrate.

## For the capstone
LightGBM is one of our four models. Early-stop on the 2023 tuning year (not a random split), and check whether it beats the rainfall-threshold baseline before claiming value.

## Related
- [Decision tree split derivation](decision-tree-split-derivation.md)
- [Logistic regression derivation](logistic-regression-derivation.md)
- [Class weights and calibration derivation](class-weights-calibration-derivation.md)
