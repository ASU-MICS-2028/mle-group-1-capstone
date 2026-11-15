---
summary: The same or near-identical record in both train and test lets the model memorise answers.
type: concept
tags: [leakage, data-quality]
sources: [preprocessing & leakage slides]
---
# Duplicate leakage

**Duplicate (or near-duplicate) leakage** is when the same record, or an almost identical one, appears in both the training and test sets. The model memorises it instead of learning, and the test score is inflated.

It is common with:
- images and augmented copies of images;
- resampled data (e.g. oversampling the rare class *before* splitting);
- records scraped again over time;
- one entity (a customer, a patient) with many rows split across train and test.

Fixes: remove duplicates before splitting; resample only inside the training data; split by group (all rows of one entity on the same side).

## For the capstone
One flood is often reported by many news articles, sometimes across weeks or neighbouring regions. Deduplicate events before labelling, and remember that a time split (not random) keeps near-identical neighbouring weeks on the same side.

## Related
- [Data leakage](data-leakage.md)
- [Data integration](data-integration.md)
- [Temporal split](temporal-split.md)
