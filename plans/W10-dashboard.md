---
workstream: W10
issue: "#11"
owner: Alice (@thealiceiris)
status: Not started
needs: none to build (uses the synthetic table); W06's saved model for the real scores
due: 2026-12-11
---
# W10 · Streamlit dashboard (the usable artefact, rubric F)

## Goal
For a NADMO regional officer: a map or list of the 16 regions with this week's risk, the rainfall behind it, and the alert threshold. It also says plainly that the label means *reported* floods and that a low score is not "safe".

## Outputs
- `app/app.py`, run with `streamlit run app/app.py`. It reads `table.parquet` and a saved model or a predictions file.
- A one-page plain-language explainer for the officer, `report/explainer.md`.

## Steps
- [ ] Build against `python src/synthetic.py` output now.
- [ ] Region map: geoBoundaries polygons, colour by risk, with an uncertainty band.
- [ ] Add "Why this week": the region's recent rain compared with its normal.
- [ ] Swap in the real model when W06 saves it, and record the steps in the README.
