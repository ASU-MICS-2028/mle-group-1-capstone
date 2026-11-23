---
id: 0007
status: Proposed
date: 2026-11-23
owner: Joseph (W01) · team to accept
issue: "#2"
---
# 0007 · Label rule: centroid region, start week, keep all polygons

## Context
[Decision 0003](0003-region-week-table-contract.md) fixed `flood` = at least one Groundsource event in the region that week. It left three choices to W01: how an event is assigned to a region, which date counts, and whether to drop very large polygons. Ghana has 2,725 events whose polygon touches a region; 2,688 have their centroid inside one (2,305 starting in 2015–2025). These counts match the options report.

## Options we tested
All eight combinations, 9,184 region-weeks each. Table: [`learnings/tables/w01_label_options.csv`](../../learnings/tables/w01_label_options.csv).

| Assign | Dates | Polygons | Positives | Rate | Train 2015–22 | Test 2024–25 | Regions with 0 positives |
|---|---|---|---|---|---|---|---|
| **centroid** | **start** | **keep all** | **585** | **6.37%** | **5.74%** | **6.61%** | **1 (Ahafo)** |
| centroid | start | drop > 500 km² | 556 | 6.05% | 5.52% | 6.19% | 1 |
| centroid | any day | keep all | 604 | 6.58% | 5.91% | 6.79% | 1 |
| centroid | any day | drop > 500 km² | 574 | 6.25% | 5.68% | 6.31% | 1 |
| intersects | start | keep all | 725 | 7.89% | 7.13% | 8.10% | 0 |
| intersects | start | drop > 500 km² | 591 | 6.44% | 5.82% | 6.85% | 0 |
| intersects | any day | keep all | 749 | 8.16% | 7.33% | 8.39% | 0 |
| intersects | any day | drop > 500 km² | 611 | 6.65% | 5.98% | 7.08% | 0 |

## Decision
Use **centroid + start week + keep all polygons** for the main model. Rerun the final model with **intersects + drop > 500 km²** as a robustness check (W06).

## Why
- Six of the eight options land between 6.0% and 6.7%. The label is not sensitive to these choices, except one combination.
- That combination is **intersects + keep all**, which adds about 140 positives. Almost all of them come from polygons over 500 km², which are mentions of a whole district or region. They mark several regions at once from one vague report, so they're the noisiest labels.
- "Any day" adds only about 19 weeks over "start": 27% of events span more than one day, but few cross a Monday.
- The centroid rule gives one event one region, so a single storm isn't counted several times. It is also the rule the options report and the 6.4% figure used.

## Consequences
- **Ahafo has no positive week** under this rule (it gets 0 of 574). The model will give it low scores whatever the rain, so the label audit (W04) and the fairness pack (W09) should report Ahafo, Oti, Bono and Western North separately.
- Events rise from ~120 a year (2015) to 333 (2022). Part of that is likely more news coverage, not more floods ([reporting drift](../../knowledge/reporting-drift.md)). The time split already tests for this, and the label audit should look at it.
- If W04's audit finds the large polygons are mostly real, revisit with a new decision.

## Links
[plan W01](../../plans/W01-labels.md) · `src/labels.py` · [EDA figure](../../learnings/figures/w01_label_eda.png)
