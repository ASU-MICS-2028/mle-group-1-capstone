---
id: 0001
date: 2026-11-15
issue: "#1, #14"
owner: Joseph
---
# 0001 · Repo scaffold, working method, plans and first knowledge base

## What we did
- **Set up the working method** ([decision 0001](../decisions/0001-working-method.md)):
  - `AGENTS.md`, `CLAUDE.md` and the templates;
  - an issue template;
  - an index for each folder.
- **Recorded decisions 0001–0005:** method, project choice, the region-week contract, the time split and data handling.
- **Wrote 16 workstream plans (W00–W15)** so that most can start today without waiting ([plans/README.md](../../plans/README.md)).
- **Added `src/synthetic.py`:** a fake region-week table in the real shape (9,184 rows), so the harness and the dashboard can be built now.
- **Drafted the first atomic notes:**
  - `knowledge/`, from the lecture recordings and slides, the capstone brief, the flood options report and Prosit 2's knowledge files;
  - `learnings/`, from Prosits 1 and 2.

## Files
`AGENTS.md`, `CLAUDE.md`, `README.md`, `.gitignore`, `requirements.txt`, `.github/ISSUE_TEMPLATE/task.md`, `docs/templates/*`, `docs/decisions/0001–0005`, `plans/*`, `data/README.md`, `src/synthetic.py`, `tools/index_notes.py`, `tools/check_notes.py`, `knowledge/*` (229 notes), `learnings/*` (40 notes)

## AI use
| Part | Tool | What the AI did | What the human checked |
|---|---|---|---|
| Structure, rules, templates, decisions, plans | Claude Code (Claude Opus 5.5) | Drafted all of it from Joseph's description of the working method, the capstone brief, the flood options report and Prosit 2's setup | **To do:** Joseph reviews; the team accepts or changes decisions 0001 and 0003 |
| `src/synthetic.py` | Claude Code | Wrote it, plus a self-check (`passed: 9184 rows …`) | **To do:** a reviewer reruns it |
| `knowledge/` and `learnings/` notes | Claude Code subagents | Summarised lecture transcripts, slides, the brief and the Prosit repos into atomic notes in their own words | **To do:** each member reads the notes for their workstream and fixes errors (W13). The notes are unverified until then. |

No data rows were given to the AI. The lecture transcripts were summarised, not published.

## Checked against the web (2026-11-15)
| Claim | Result |
|---|---|
| NADMO's statute is Act 927 (2016) | **Confirmed** (FAOLEX/UNEP LEAP, judy.legal): gazetted 22 Sep 2016, repealed Act 517 (1996). Section numbers still need reading. |
| Groundsource Zenodo record, licence, size | **Confirmed** via the Zenodo API: `groundsource_2026.parquet`, 667 MB, CC BY 4.0 |
| Groundsource accuracy "75%" | **The sources conflict:** Google's blog says 60% correct in both location and time; the EGU abstract says about 75%. Both are now in the note. |
| geoBoundaries GHA ADM1 region codes and licence | **Confirmed** via the API: 16 regions whose `shapeISO` matches our codes; licence **CC BY-SA 2.0** (was "not confirmed") |
| CHIRPS v2 ends Dec 2026 | **Confirmed:** 31 Dec 2026 (CHC newsletter); move to v3 |
| Earth Engine IDs for ERA5-Land daily and the Global Flood Database | **Confirmed** |
| CHIRPS licences | **Not confirmed** by search; re-check the CHC page |
| CHIRPS Earth Engine ID `UCSB-CHG/CHIRPS/DAILY` | **Confirmed 2026-11-22** by a live query: data runs 1981-01-01 to 2026-09-30 |
