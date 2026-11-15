---
summary: Inspect the delivered data and dictionary against the brief before writing any model code
type: lesson
tags: [data, eda, process]
sources: [prosit-1 notebook §1, prosit-1 reflection, prosit-2 docs/01_data.md, prosit-2 docs/log.md 20 Oct]
---
# Check the data against the brief first

In Prosit 1 the brief described weather variables (rainfall, temperature, elevation) in the district file and child blood-test results in the survey. The delivered files didn't have them. We found this only after starting, and the reflection's main "do differently" was: read the data dictionary and check the columns before touching code; it would have saved hours.

In Prosit 2 we did it first, as steps 1–2:
- checked row counts and totals against the numbers quoted in the brief (all matched);
- found that shared IDs were one loan split across lenders, not duplicates;
- found units differed by country (amounts about 7× apart in US$) and the macro file stopped a year early;
- wrote it all up in `docs/01_data.md` before any modelling.

Several of these findings shaped later decisions.

## For the capstone
Before features: count Groundsource reports per region and year, check the date field (event vs publication), check how location is given and how it maps to the 16 regions, look for coverage growth over time, and confirm each climate source covers 2015–2025 at weekly resolution. Write a `docs/01_data.md` and a datasheet section from it.

## Related
- [harmonise-boundaries-before-joining.md](harmonise-boundaries-before-joining.md)
- [missing-is-not-zero.md](missing-is-not-zero.md)
- [never-show-raw-rows-to-an-ai-tool.md](never-show-raw-rows-to-an-ai-tool.md)
