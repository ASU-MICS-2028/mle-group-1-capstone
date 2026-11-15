---
workstream: W01
issue: "#TBD"
owner: unassigned (suggested role: Data lead)
status: Not started
needs: none
due: 2026-11-18
---
# W01 · Flood labels: Groundsource → region-week

## Goal
`data/processed/labels.parquet`, with one row per region per week from 2015 to 2025 and a 0/1 `flood` label, in the shape set by [decision 0003](../docs/decisions/0003-region-week-table-contract.md).

## Why it matters
Everything else needs these labels: the mid-check (data in hand, EDA) and rubric A (problem framing) and E (code).

## Inputs
- Groundsource (CC BY 4.0, 667 MB), from Zenodo: see [knowledge/groundsource-dataset.md](../knowledge/groundsource-dataset.md).
- geoBoundaries GHA ADM1.

## Outputs
- **`src/labels.py`.** Running `python src/labels.py data/raw/groundsource/... data/raw/geoboundaries/...` writes `labels.parquet` with `region_id, week_start, flood, n_events`.
- **`src/regions.py`**, which downloads the 16 region polygons. W02 and W03 use it too.
- **Rows `data/README.md` needs:** sources, versions, licence and fetch steps.

## Steps
- [ ] Download Groundsource and geoBoundaries into `data/raw/`, and record versions and checksums in `data/README.md`.
- [ ] Filter to Ghana, then check the count against the options report: 2,688 events (Jun 2006–Jan 2026), 2,305 in 2015–2025.
- [ ] Test each choice open in decision 0003, recording positive rates and row counts for each option in a table:
  - centroid vs intersects;
  - start date vs any covered day;
  - keeping vs dropping polygons over 500 km².
- [ ] Write a decision file for the chosen rule.
- [ ] Self-check, ending in an `assert`: 16 regions × 574 weeks; no duplicate keys; `flood` in {0, 1}.
- [ ] EDA figures: events per year, per month and per region. Save them and index them.

## Done when
Standard checklist (see the template). The label rule is a decision file, and the EDA is saved.

## Read first
- [knowledge/groundsource-dataset.md](../knowledge/groundsource-dataset.md)
- [knowledge/news-label-bias.md](../knowledge/news-label-bias.md)
- [knowledge/reporting-drift.md](../knowledge/reporting-drift.md)
