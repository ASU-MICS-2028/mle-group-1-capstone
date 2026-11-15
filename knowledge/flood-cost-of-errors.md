---
summary: A missed flood leaves people unprepared; a false alert wastes resources and erodes trust in alerts
type: concept
tags: [flood, cost-matrix, problem-formulation]
sources: [Flood options report §4 F1, proposal Option B]
---
# Flood cost of errors

| | Flood reported | No flood reported |
|---|---|---|
| **Alert** | Correct: preparation pays off | **False positive:** staff and supplies moved for nothing; over time, people ignore alerts (alert fatigue) |
| **No alert** | **False negative:** communities and supplies unprepared when the flood comes | Correct |

A false negative is usually far costlier (lives, displacement) than one false positive, which argues for a low threshold. But false positives accumulate: a tool that cries wolf every week gets ignored, which turns future true alerts into effective misses. Capacity is also finite: an office can only prepare for so many regions at once.

So we report both a **cost-ratio view** (threshold $t^*=C_{FP}/(C_{FP}+C_{FN})$ over a range of plausible ratios, since NADMO's real costs are unknown) and an **alert-budget view** (recall when we alert only the top $k$ region-weeks).

Two label caveats: a "false positive" may be a real flood nobody reported (rural under-reporting), and a low score must never be read as "safe".

## For the capstone
This table is the report's cost matrix (Part A). Pick the operating point on 2023 and freeze it before touching 2024–2025.

## Related
- [Cost-based threshold derivation](cost-threshold-derivation.md)
- [News label bias](news-label-bias.md)
- [Flood decision and stakeholders](flood-decision-and-stakeholders.md)
- [Technical report structure](technical-report-structure.md)
