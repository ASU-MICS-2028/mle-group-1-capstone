---
summary: News-derived labels measure where reporters are as well as where floods are; silence is not "no flood"
type: concept
tags: [flood, labels, bias, fairness]
sources: [Flood options report summary, §3, §6, §7; proposal Option B]
---
# News label bias

Groundsource labels come from news. Three consequences:

1. **A missing report is not a missing flood.** Negatives are uncertain: a quiet week may only mean no journalist covered it.
2. **Coverage is unequal.** Greater Accra has 38% of Ghana's events; Oti, Bono, Ahafo and Western North together have 56. Part of that is real exposure, part is where media are. A model can learn **where journalists are** as well as where floods happen.
3. **Language and channel gaps.** Local-language and radio reports may be missed; Ghana's language coverage in the dataset is **unconfirmed**.

Further label noise: estimated precision varies (75% in one abstract); 27% of events span more than one day and news dates may lag the flood; ~11% of polygons exceed 500 km² (town- or district-level mentions).

**Responses:** hand-audit a sample (~100 events) for accuracy and dates; compare region-weeks against the Global Flood Database (2015–2018) to estimate under-reporting by region; report per-region results; test built-up share and population as proxies; set per-region thresholds; state throughout that the model predicts **reported** floods.

## For the capstone
This is the project's central weakness and its strongest ethics material. Raise it first in the defence rather than waiting to be asked.

## Related
- [Groundsource dataset](groundsource-dataset.md)
- [Reporting drift](reporting-drift.md)
- [Proxy variables](proxy-variables.md)
- [Global Flood Database](global-flood-database.md)
- [Flood ethics concerns](flood-ethics-concerns.md)
