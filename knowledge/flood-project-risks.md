---
summary: Register of flood-project risks and planned responses, from the options report
type: concept
tags: [flood, risks, planning]
sources: [Flood options report §6, §4 F1]
---
# Flood project risks

| Risk | Why it matters | Planned response |
|---|---|---|
| Forecast leakage | Rain from the predicted week inflates scores | Only rain up to the prediction date; forecast rain tested separately |
| Report date vs flood date | News may lag; 27% of events span > 1 day | Hand-audit a sample; leave a gap around the prediction date |
| Reporting drift | More online news looks like more flooding | Train from 2015, no year feature, temporal validation |
| Missing reports | A quiet week may mean no reporter | Treat negatives as uncertain; compare with Global Flood Database 2015–2018 |
| Non-rain floods | Dam spillage breaks the rain→flood link (Akosombo 2023) | Flag known spill periods; report results with and without them |
| Event clusters | One storm creates many events | Region-week unit; a week counts once |
| Joining many sources | Biggest time cost | Region-week table fixed by Week 11; land features only after baseline works |
| Little value over rain rule | Model may not beat a threshold baseline | Always report the baseline; say so honestly if it wins |
| Data or scope problems | Brief requires a fallback | F3 Greater Accra map, or Greater Accra only; galamsey as topic fallback |

## For the capstone
Revisit this table at the mid-check and the clinic; record outcomes (including failures) in the results index.

## Related
- [Forecast leakage](forecast-leakage.md)
- [Reporting drift](reporting-drift.md)
- [News label bias](news-label-bias.md)
- [Fallback plans](fallback-plans.md)
- [Capstone timeline](capstone-timeline.md)
