---
summary: With calibrated p, act when p > C_FP / (C_FP + C_FN)
type: derivation
tags: [derivation, decision-theory, threshold, classification]
sources: [prosit-2 derivations.md §b.8, ISLR 4.4.2, HOMLP ch 3]
---
# Cost-based threshold derivation

Let $C_{FN}$ be the cost of not acting when the event happens and $C_{FP}$ the cost of acting when it does not; correct decisions cost 0. For a case with **calibrated** probability $p$:
- expected cost of **not acting** $=p\,C_{FN}$;
- expected cost of **acting** $=(1-p)\,C_{FP}$.

Act when not acting is costlier:
$$p\,C_{FN}>(1-p)C_{FP}\iff p>t^*=\frac{C_{FP}}{C_{FP}+C_{FN}} .$$

Example: if a missed flood costs 10× a wasted preparation, $t^*=1/11\approx0.09$ — far below 0.5.

**Caveats.**
- The formula assumes $p$ is a true probability. With weighted or uncalibrated models (SVM scores, balanced class weights), choose the threshold empirically by minimising total cost on validation data.
- Costs are rarely known exactly; show how the decision changes over a range of cost ratios.
- When the user can only act on a fixed number of alerts (an alert budget), the decision becomes "top-$k$ regions this week" instead of a fixed $t^*$; report recall at that $k$.

## For the capstone
NADMO's cost ratio is not known; present a few plausible ratios and the alert-budget view (e.g. top 3 of 16 regions per week), choose on 2023, and freeze before testing on 2024–2025. Per-region thresholds are one fairness mitigation.

## Related
- [Flood cost of errors](flood-cost-of-errors.md)
- [Class weights and calibration derivation](class-weights-calibration-derivation.md)
- [Logistic regression derivation](logistic-regression-derivation.md)
- [Fairness mitigation options](fairness-mitigation-options.md)
