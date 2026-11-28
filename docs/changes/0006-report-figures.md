---
id: 0006
date: 2026-11-28
issue: "#13"
owner: Joseph
---
# 0006 · Report figures in the report colours

## What we did
- `src/report_figures.py` draws Figure 1 (flood reports per year, % of weeks flooded by month and by region) from `labels.parquet`, and Figure 2 (the pipeline diagram). It uses the report colours and font, and asserts the key numbers (123 and 333 reports in 2015 and 2022, June peak, Ahafo lowest) before saving.
- The figures go into the technical report in Drive. The report itself stays out of the repo.

## Files
- `src/report_figures.py`
- `learnings/figures/report_fig1_labels.png`, `learnings/figures/report_fig2_pipeline.png`, `learnings/results_index.md`

## AI use
| Part | Tool | What the AI did | What the human checked |
|---|---|---|---|
| Figures | Claude Code | Wrote the script, rendered and checked both figures | Joseph: rerun `python src/report_figures.py`; check the figures read correctly in the report |
