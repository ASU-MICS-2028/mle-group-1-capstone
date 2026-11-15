---
summary: Use paired bootstrap intervals and a noise floor before saying one model beats another
type: procedure
tags: [uncertainty, bootstrap, model-selection]
sources: [prosit-2 AGENTS.md ML rules, prosit-2 learnings/tables/07_noise_floor_comparison.md, prosit-2 ADR 0012]
---
# Measure the noise floor before claiming a win

Prosit 2's brief set a noise floor of ±0.0263 PR-AUC at leaderboard size. Below that, a difference is not a win. How we applied it:

1. **Paired bootstrap of the difference.** Resample the test units (customers, not rows) with replacement, score both models on each resample, and take the 2.5th–97.5th percentile of the *difference*. 300–2,000 replicates.
2. **Compare to the noise floor and to zero.** Logistic minus random forest, pooled: +0.015, 95% CI [+0.001, +0.033]: positive but inside the floor.
3. **Look per block too.** Scored block by block, logistic led in 4 of 4, mean +0.039, above the floor. The pooled number was dominated by one large period. We reported both and explained why they differ.
4. **Run several seeds** to see training noise.
5. **Call ties ties.** Leaderboard gap 0.003 → "a tie", and the simpler model wins ties.

Also useful: report feature-set changes with CIs (e.g. lift 8.15 vs 7.97, paired CI [−0.06, +0.49]: no measurable cost).

## For the capstone
Bootstrap by region-week blocks (or whole weeks across all regions) on 2024–2025, report CIs for PR-AUC, recall at the chosen threshold and Brier, and state for each comparison whether it clears the noise.

## Related
- [bootstrap-by-the-correlated-unit.md](bootstrap-by-the-correlated-unit.md)
- [simple-models-held-up-better-over-time.md](simple-models-held-up-better-over-time.md)
- [../knowledge/bootstrap-confidence-interval.md](../knowledge/bootstrap-confidence-interval.md)
