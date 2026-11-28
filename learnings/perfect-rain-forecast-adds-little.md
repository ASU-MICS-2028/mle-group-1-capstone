---
summary: Even the rain that actually fell during the week lifts 2023 PR-AUC by only 0.04–0.06, and the 95% range of the gain includes zero
type: result
tags: [forecast, w02, rain, leakage, upper-bound]
sources: [learnings/tables/forecast_experiment.csv, learnings/tables/forecast_experiment_rolling_origin.csv]
---
# A perfect rain forecast adds little

We gave two models the rain that actually fell during the week being predicted (`rain_thisweek_mm`). Nobody has this on Monday, so it is an upper bound: the most a perfect rain forecast could add. Scores on 2023, with the 95% week-bootstrap range of the gain:

| Model | PR-AUC without | PR-AUC with | Gain (95% range) | Recall@3 without → with |
|---|---|---|---|---|
| Logistic regression, rain and soil moisture | 0.18 | 0.24 | +0.06 (−0.01 to +0.16) | 0.18 → 0.21 |
| Random forest, rain + region + month + recent floods | 0.28 | 0.32 | +0.04 (−0.01 to +0.08) | 0.45 → 0.43 |

The gain is positive in all six rolling-origin years (2018–2023) for both models. On average it is +0.05 PR-AUC for the logistic model and +0.03 for the forest. Without the Akosombo spill weeks, the gains are slightly larger (+0.09 and +0.06).

So the week's own rain helps a little, and much less than expected for a rain-driven hazard. Likely reasons: news reports are dated loosely around the flood, some floods have other causes (dam releases, blocked drains), and a region-wide average smooths out the local storms that cause urban flash floods. Where and when still matter more than the week's rain.

## For the capstone
- A real forecast (for example CHIRPS-GEFS) can only do worse than this upper bound, so adding forecast rain is a low priority. Spend the time on the labels and on region-level features instead.
- Report this as the "with perfect forecast" upper bound in Results §6.4. Never use `rain_thisweek_mm` in the main model.

## Related
- [Where and when beat rain alone](where-and-when-beat-rain-alone.md)
- [Large polygons drive label disagreement](large-polygons-drive-label-disagreement.md)
