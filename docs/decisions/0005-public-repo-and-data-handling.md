---
id: 0005
status: Accepted
date: 2026-11-15
owner: Team (repo created public in the course org)
issue: "W00"
---
# 0005 · Public repo: no data, no slides, no transcripts committed

## Decision
- **`data/` is gitignored.** `data/README.md` records each source's link, licence, version and fetch steps, so anyone can rebuild the data.
- **Course material** (slides, PDFs, books, lecture transcripts) is not committed. `knowledge/` holds only our own-words notes about it.
- **No contact details, student IDs or private correspondence.** Decisions quote the instructor's reply only where it settles scope.
- **Licences** (Groundsource CC BY 4.0, CHIRPS, ERA5-Land, GHSL, WorldPop, etc.) are credited in `data/README.md`, the Datasheet and the report.

## Why
- The brief: "do not commit private data".
- The course AI policy.
- Copyright on course material.
- The same rule worked in Prosit 2.
