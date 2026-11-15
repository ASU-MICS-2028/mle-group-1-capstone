---
workstream: W04
issue: "#5"
owner: unassigned (suggested role: Ethics & communication lead)
status: Not started
needs: none (works on the raw Ghana subset of Groundsource; doesn't need labels.parquet)
due: 2026-11-27
---
# W04 · How good are the labels? Hand audit and satellite check

## Goal
- An honest estimate of how often a Groundsource "flood in Ghana" is a real flood, on the right date, in the right region.
- How much rural under-reporting there is.

## Why it matters
The labels come from the news. A model could learn where journalists are as well as where floods happen. This audit is the core of the ethics section (rubric LO5) and makes the limitations honest.

## Steps
- [ ] Draw a random sample of 100 Ghana events (2015–2025), stratified by region, with a fixed seed.
- [ ] For each event, check the source article. Record whether it was a flood, whether the date is right (with the lag in days), whether the location is right, and the type: rain, river, dam spill or other. The audit sheet lives in `data/` and isn't committed; only the aggregate results are.
- [ ] Measure precision overall and by region, with bootstrap confidence intervals.
- [ ] Compare against the Global Flood Database for 2015–2018: which satellite-seen floods have no news report, by region.
- [ ] Write a decision on how the audit changes the label rule (e.g. a date lag window), and learning notes.

## Read first
- [knowledge/news-label-bias.md](../knowledge/news-label-bias.md)
- [knowledge/global-flood-database.md](../knowledge/global-flood-database.md)
