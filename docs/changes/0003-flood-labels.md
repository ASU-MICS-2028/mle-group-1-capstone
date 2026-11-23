---
id: 0003
date: 2026-11-23
issue: "#2"
owner: Joseph
---
# 0003 · Flood labels from Groundsource

## What we did
- `src/labels.py` reads the 2.6M-event Groundsource file, keeps the 2,725 events touching Ghana (cached in `data/interim/`), and writes `labels.parquet`: 9,184 rows, 585 positive (6.4%).
- `--compare` builds all 8 label-rule options from decision 0003 and saves the table and the EDA figure. The chosen rule is in decision 0007.
- The Ghana counts match the options report (2,688 events; 2,305 in 2015–2025; 585 positive region-weeks).

## Files
- `src/labels.py`, `data/README.md`, `docs/decisions/0003-…`, `docs/decisions/0007-label-rule.md`
- `learnings/tables/w01_label_options.csv`, `learnings/figures/w01_label_eda.png`

## AI use
| Part | Tool | What the AI did | What the human checked |
|---|---|---|---|
| `labels.py` and the option comparison | Claude Code | Wrote and ran the script; only counts and rates were printed, never raw rows | Joseph: rerun `python src/labels.py --compare` from a fresh clone; confirm the counts match the options report |
| Decision 0007 | Claude Code | Drafted the recommendation from the table | Joseph and the team: accept or change it |

## Decisions / learnings this produced
- docs/decisions/0007-label-rule.md · learnings/large-polygons-drive-label-disagreement.md
