---
summary: First baselines: the region-month flood rate beats rain-only models on 2023
type: result
tags: [baselines, w05, rain, seasonality]
sources: [learnings/tables/baselines.csv, learnings/tables/baselines_rolling_origin.csv]
---
# Where and when beat rain alone (first baselines)

On 2023 (base rate 10.9%), with 95% CIs that resample weeks:

| Baseline | PR-AUC | Recall@3 (chance 18.75%) |
|---|---|---|
| Region × month flood rate from 2015–22 | **0.25** (0.16–0.37) | 0.30 |
| Rain rule (14-day rain, window chosen on train) | 0.18 (0.14–0.25) | 0.21 |
| Logistic regression on rain and soil moisture | 0.18 (0.14–0.23) | 0.18 |

In the rolling-origin years 2018–2023 the seasonal rate is best in 4 of 6. Rain on its own carries signal (about 1.7 times chance), but knowing *which region* and *which month* matters more, mostly because reports are concentrated in Greater Accra and the rainy months.

The seasonal rate can't transfer to an unseen region (leave-one-region-out PR-AUC 0.04, as designed). The rain models can (0.14–0.17).

## For the capstone
W06 should combine the two: region and season plus rain. The question to answer is whether rain adds anything over the seasonal rate.

## Related
- [Recall at an alert budget has a chance level](recall-at-k-has-a-chance-level.md)
- [Large polygons drive label disagreement](large-polygons-drive-label-disagreement.md)
