---
summary: Cases whose outcome is not yet known at the data cutoff must not be treated as negatives.
type: lesson
tags: [labels, data-quality, prosit-2]
sources: [lab-session-1 discussion]
---
# Unresolved outcomes at the data cutoff

In Prosit 2, some loans were neither repaid nor defaulted when the data was pulled. They were simply not due yet. Their label was really "unknown", but it is easy to count them as "did not default". That makes the default rate look lower than it is. The team noticed this but did not fully handle it.

General rule: when a label needs time to appear, check every row had enough time. Options:

- drop rows whose outcome window had not finished at the cutoff;
- or define the label over a fixed window that all kept rows have completed;
- and say in the report which you did.

Statisticians call this right-censoring.

## For the capstone
News reports of floods can appear late, and Groundsource coverage of the newest weeks may be incomplete. Check whether the last weeks of 2025 have fewer reported floods than the same weeks of earlier years. If so, trim or flag them before testing, or the model's recall will look wrong.

## Related
- [Beat a naive baseline first](beat-a-naive-baseline-first.md)
- [Train, validation and test sets](train-validation-test-split.md)
