---
summary: Recall@top-3 of 16 regions is 19% by pure chance; always quote it beside that
type: lesson
tags: [evaluation, metrics, w05]
sources: [learnings/tables/baselines.csv]
---
# Recall at an alert budget has a chance level

If each week we flag the top 3 of 16 regions, a coin-flip ranking still catches 3/16 = **18.75%** of flood region-weeks on average. Our first baselines scored 18–30% on 2023, so the rain-only models were barely above chance on this metric. Their PR-AUC was still 1.6–1.7 times the base rate (0.18 against 0.11).

The same goes for PR-AUC: its chance level is the positive rate (10.9% in 2023, 6.4% overall), not 0.

## For the capstone
Every results table quotes the chance level next to the metric: `k/16` for recall@k and the base rate for PR-AUC. Report "× chance", not the raw number alone.

## Related
- [Measure the noise floor before claiming a win](measure-the-noise-floor-before-claiming-a-win.md)
- [Precision-recall AUC](../knowledge/precision-recall-auc.md)
