---
summary: Target leakage is a feature that exists or takes its value because of the outcome.
type: concept
tags: [leakage]
sources: [preprocessing & leakage slides]
---
# Target leakage

**Target leakage** is when a feature only exists, or only takes its value, **because of the outcome** you are trying to predict.

Slide example: predicting whether a patient *will be* diagnosed with diabetes using "took diabetes medication". That field is only filled in after the diagnosis, so the model is reading the answer.

The test to apply to every feature:
**"Would I actually know this value at the moment I need to make the prediction?"**
If not, drop it.

Common forms: status fields updated after the event, totals that include the outcome period, IDs or codes assigned after the outcome, and target encoding computed on all data.

## For the capstone
Suspects: anything derived from news reports themselves (e.g. a count of flood articles that week), damage or rescue figures, and rainfall summed over the *same* week if the alert is meant to be issued at the start of that week.

## Related
- [Data leakage](data-leakage.md)
- [Temporal leakage](temporal-leakage.md)
- [Problem formulation](problem-formulation.md)
- [Categorical encoding](categorical-encoding.md)
