---
summary: Keep a one-line action log and an AI-use log daily; they become the declaration
type: procedure
tags: [process, ai-use, documentation]
sources: [prosit-2 docs/log.md, prosit-2 docs/ai_use.md, prosit-2 AGENTS.md rule 7, prosit-1 notebook §14]
---
# Log actions and AI use as you go

The course requires an AI-use declaration in the report and in each reflection. In Prosit 1 it was written at the end, from memory. In Prosit 2 we kept two tables from day one:

- `docs/log.md`: date · who · what · where, one line per action (e.g. "reran notebooks 03 and 04 from a fresh clone; 27 of 31 tables identical").
- `docs/ai_use.md`: date · who · tool · what the AI did · **what the human checked or changed**.

The second column is the important one. "AI built the step; the owner is to review each part in a walkthrough" is honest but also a to-do; several lines read like that, and the reflections had to own it. Empty rows ("please add") showed where a member's AI use wasn't logged yet.

Benefits: the declaration, the reflections and the "who did what" table were assembled from the logs in minutes, and they showed even contribution without relying on commit counts.

## For the capstone
Create both files on day one. Every member adds their own lines the same day, including chat-based tools, and fills in the "what I checked" column with something specific (reran, compared to source, rewrote).

## Related
- [record-decisions-as-adrs.md](record-decisions-as-adrs.md)
- [never-show-raw-rows-to-an-ai-tool.md](never-show-raw-rows-to-an-ai-tool.md)
- [defend-every-number-without-ai.md](defend-every-number-without-ai.md)
