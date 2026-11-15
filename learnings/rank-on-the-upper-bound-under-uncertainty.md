---
summary: When data is thin and stakes are high, rank on the upper bound so doubt favours the vulnerable
type: lesson
tags: [decision, uncertainty, equity]
sources: [prosit-1 notebook §11, prosit-1 reflection, prosit-1 panel_qa]
---
# Rank on the upper bound under uncertainty

In Prosit 1 we ranked districts for bed nets on the **upper end of the 95% interval** of their unprotected burden, not the mean. A remote district with erratic reporting has a wide interval; ranking on the mean treats it like a well-measured district and quietly penalises it for poor data. Ranking on the upper bound gives it the benefit of the doubt. Our panel line: "waiting for certainty means serving only places that report well."

It didn't make the list unstable: mean and upper-bound rankings shared 9 or 10 of the top 10 districts, so the choice mattered at the margin, where it should.

We also kept priority (rate) separate from quantity (count): a small district could be first in priority while a populous one received more nets in total, and we showed nets per person to check equity.

## For the capstone
For the dashboard, consider showing each region's alert probability with its interval, and flag regions whose interval crosses the alert threshold as "watch" rather than silently not alerting. That matters most for regions with few reported floods, where the model is least certain.

## Related
- [missing-is-not-zero.md](missing-is-not-zero.md)
- [bootstrap-by-the-correlated-unit.md](bootstrap-by-the-correlated-unit.md)
- [data-gaps-moved-decisions-more-than-models.md](data-gaps-moved-decisions-more-than-models.md)
