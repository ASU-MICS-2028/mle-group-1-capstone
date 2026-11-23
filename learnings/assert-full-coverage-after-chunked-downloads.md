---
summary: Chunked API pulls can silently skip days; assert the full date range after joining
type: lesson
tags: [data, earth-engine, testing, w02]
sources: [W02 run 2026-11-22]
---
# Assert full coverage after a chunked download

Earth Engine returns at most 5,000 features per request, so W02 pulls the data one quarter at a time. The first version worked out each chunk's end date with `pd.offsets.QuarterBegin()`. That offset jumps to the next quarter start counted from March (Mar, Jun, Sep, Dec), not to the next calendar quarter, so each chunk stopped a month early. `pd.date_range(..., freq="QS")` also skipped the opening December. The code still ran and returned plenty of rows (992 per quarter where a full quarter is 1,472).

What caught it was the later check that every feature value is present. The fix keeps the chunk edges as a list, so each chunk ends where the next one starts, and adds an `assert` that the joined table has exactly 16 regions × every day in the range.

## For the capstone
Any script that downloads in pieces (Earth Engine, CHC files, Zenodo) should assert the complete set of keys after joining, not only that there were no errors.

## Related
- [Missing is not zero](missing-is-not-zero.md)
- [Scorer tests catch what metrics miss](scorer-tests-catch-what-metrics-miss.md)
