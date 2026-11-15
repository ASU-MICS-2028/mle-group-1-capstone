---
summary: Where two reasonable choices exist, run both and pick with numbers in a saved table
type: procedure
tags: [process, experiments, model-selection]
sources: [prosit-2 AGENTS.md rule 2, prosit-2 ADR 0012, prosit-1 notebook §15]
---
# Test every diverging path in a table

Our strongest habit across both prosits: whenever there was more than one sensible option (a feature, a fill-in rule, a model, a threshold), we ran them all and chose from a table, including the naive or cheating version to show what a mistake would cost.

- **Prosit 1:** a 168-configuration matrix in four blocks (distribution family, interval method × resamples, 64 supervised setups, allocation levers). It showed which choices mattered and which didn't.
- **Prosit 2:** about 1,700 fits for the feature set: all 63 combinations of six feature groups, drop-one-column, leaky vs safe variants, look-back windows, two model families, three validation tests, three seeds plus a bootstrap.

How to keep it manageable:
1. Fix the main score and validation test before running (we used lift on future data).
2. Summarise each option as "average change when added" and "helped in k of n combinations".
3. Save the full grid to `learnings/tables/` even if only one row reaches the report.
4. Write the decision as an ADR that quotes the table.

It also gave us ready answers in the panel Q&A: "we tried that; here is the number."

## For the capstone
Grid over feature groups (rain lags, soil moisture, terrain, built-up), model family and class weighting, on the 2023 tune year only. Keep 2024–2025 untouched until the final run.

## Related
- [features-that-encode-the-period-hurt-on-the-future.md](features-that-encode-the-period-hurt-on-the-future.md)
- [save-every-result-to-a-results-index.md](save-every-result-to-a-results-index.md)
- [record-decisions-as-adrs.md](record-decisions-as-adrs.md)
