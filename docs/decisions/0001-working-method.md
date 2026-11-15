---
id: 0001
status: Proposed
date: 2026-11-15
owner: Joseph (proposed) · whole team to accept
issue: "#1"
---
# 0001 · Working method: issues + plan files + atomic logs

## Context
In Prosit 2 we kept one long log, one long AI-use file and one learnings file per step. They worked, but they were hard to search, and the AI-use record was kept apart from the change it described. For the capstone, rubric line G (process and contribution, 10 pts) and the individual contribution statements both need us to show who did what and where AI helped.

## Options we considered
| Option | Verdict |
|---|---|
| Keep the Prosit 2 setup: one log, one AI-use file, step learnings | Rejected: big files, AI use separated from the change |
| **GitHub issues + one plan file per task; one file per decision, change and note, each with an index** | **Chosen** |
| Issues only, no files in the repo | Rejected: the record would live outside the repo we submit |

## Decision
- Every task is a GitHub issue with a plan file in `plans/`.
- Every decision is a file in `docs/decisions/`.
- Every change is a file in `docs/changes/`, recording who was in charge and an AI-use table.
- Knowledge and learnings are atomic notes, one idea per file.
- Each folder has a `README.md` index.

## Why
- Small files are easy to link, review and cite in the report.
- Keeping the AI use inside each change makes the declaration accurate.
- Separate workstreams with explicit inputs ([0003](0003-region-week-table-contract.md)) let us work without waiting on each other.

## Consequences
- There's a bit more paperwork per change; the templates in `docs/templates/` keep it short.
- Indexes must be updated by hand when files are added.

## Links
[AGENTS.md](../../AGENTS.md) · [change 0001](../changes/0001-repo-scaffold-and-knowledge-base.md)
