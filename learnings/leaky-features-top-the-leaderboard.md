---
summary: When many configurations are compared, the top scorers are usually the leaky ones
type: result
tags: [leakage, evaluation, model-selection]
sources: [prosit-1 notebook §9 and §15C, prosit-1 outputs/tables/leakage_audit.csv, prosit-2 learnings/03_feature_audit]
---
# Leaky features top the leaderboard

In both prosits the highest scores came from models that were cheating.

- **Prosit 1 (bed-net ownership):** of 64 supervised configurations, only 4 were free of leakage, and none of the top 10 was clean. A post-treatment column ("children slept under a net last night", which needs a net to exist) lifted test ROC-AUC from 0.660 to 0.750 (+0.09). Target-encoding the survey cluster on all rows added +0.06. We chose the honest 0.66 model.
- **Prosit 2 (loan default):** two repayment columns included post-default penalties. With them, PR-AUC jumped from 0.20 to 0.91, and price alone separated defaulters at ROC-AUC 0.991.

The pattern: a score that looks too good for the problem is a symptom to investigate, not a result to report. Sort any comparison table by score and then audit the top rows first, because that's where the leaks collect.

## For the capstone
Flood labels come from news reports, so any feature built from news counts, report text, or post-event damage would leak. If a weekly model scores far above the persistence and climatology baselines, audit the top features before celebrating. Expect honest PR-AUC to be modest.

## Related
- [audit-leaks-by-building-the-cheating-version.md](audit-leaks-by-building-the-cheating-version.md)
- [fit-preprocessing-inside-the-fold.md](fit-preprocessing-inside-the-fold.md)
- [../knowledge/data-leakage.md](../knowledge/data-leakage.md)
