---
workstream: W09
issue: "#10"
owner: unassigned (suggested role: Ethics & communication lead)
status: Not started
needs: none for Datasheet and regulatory mapping; W06 for the fairness numbers and Model Card (explicit)
due: 2026-12-11
---
# W09 · Ethics and fairness review pack (LO5)

## Goal
The brief's pack:
- a Datasheet;
- a Model Card;
- disaggregated results by region (and urban/rural);
- a proxy analysis;
- a regulatory mapping;
- one concrete mitigation, tested.

## Steps
- [ ] **Datasheet** for our region-week dataset (start now): motivation, composition, collection process, and the news-bias caveat. Use the W04 audit numbers when they land.
- [ ] **Regulatory mapping:** NADMO Act 2016 (Act 927, verified; read its sections), Data Protection Act 2012 (Act 843) and data licences. Say what applies and what doesn't (there's no personal data).
- [ ] **Fairness:** recall and calibration per region, comparing Greater Accra with the rural regions (Oti, Bono, Ahafo, Western North).
- [ ] **Proxy test:** retrain without `builtup_share` and `pop_density`, and see how scores change.
- [ ] **Mitigation:** test per-region thresholds or an alert floor so rural regions aren't always below the cut-off. Record the result as a decision.
- [ ] **Model Card** for the final model, including "must not be used for" (e.g. justifying evictions).

## Read first
- [knowledge/flood-ethics-concerns.md](../knowledge/flood-ethics-concerns.md)
- [knowledge/datasheets-for-datasets.md](../knowledge/datasheets-for-datasets.md)
- [knowledge/model-cards.md](../knowledge/model-cards.md)
