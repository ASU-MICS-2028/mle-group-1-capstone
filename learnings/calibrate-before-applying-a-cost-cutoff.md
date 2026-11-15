---
summary: A cost-derived cut-off is only valid on calibrated probabilities; class weights break them
type: lesson
tags: [calibration, threshold, class-imbalance]
sources: [prosit-2 ADR 0007, prosit-2 ADR 0013, prosit-2 ADR 0017]
---
# Calibrate before applying a cost cut-off

The decision rule "act when probability > cost FP ÷ (cost FP + cost FN)" assumes the probability means what it says. Ours didn't always.

- **Class weights inflate scores.** In Prosit 2, a "balanced" logistic regression had Brier 0.166 against 0.088 unweighted, with the same ranking (PR-AUC 0.154 vs 0.158). Platt scaling repaired it (0.088), isotonic did slightly worse on the small calibration set.
- **Ranking and calibration are separate.** A constant "everyone gets the base rate" model had a slightly better Brier than our first model but couldn't rank anyone, so we reported both kinds of metric.
- **Check with a reliability curve and the Platt slope.** The final unweighted model's Platt slope was 0.99, meaning plain logistic regression was already honest.

So the order is: rank (PR-AUC), calibrate (Brier, log loss, reliability curve), *then* apply the cost cut-off.

## For the capstone
Flood weeks are rare, so class weights or resampling are tempting. If used, calibrate afterwards on out-of-fold training predictions, and check the reliability curve on 2023 before setting the alert threshold. Report Brier next to PR-AUC.

## Related
- [calibration-data-must-span-all-periods.md](calibration-data-must-span-all-periods.md)
- [derive-the-cutoff-from-a-cost-matrix.md](derive-the-cutoff-from-a-cost-matrix.md)
- [../knowledge/probability-calibration.md](../knowledge/probability-calibration.md)
