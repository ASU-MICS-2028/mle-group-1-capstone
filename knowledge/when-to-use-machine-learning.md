---
summary: Use ML when rules are too hard to write and data is plentiful; skip it otherwise.
type: concept
tags: [foundations]
sources: [intro slides, Terms notes]
---
# When to use machine learning

ML is not always the right tool. The intro slides give a simple test.

**ML is worth it when:**
- there is a lot of data to learn from;
- the problem is too complex to write rules for (recognising faces, speech, handwriting);
- the world keeps changing, so a fixed rule would go stale.

**ML is not worth it when:**
- a simple rule already works (a calculator, a payroll formula, sorting numbers);
- there is very little data, or the data is poor quality.

Example: deciding if a number is even needs one rule, not a model. Deciding if a photo shows a cat has no simple rule, so learn it from examples.

## For the capstone
Floods depend on rain, soil wetness, terrain and land use in ways that are hard to write as one rule, and we have years of weekly data. That justifies ML. But a simple rule ("flag a region when weekly rain is above a threshold") is a fair baseline, and the ML model must beat it to be worth using.

## Related
- [What machine learning is](what-is-machine-learning.md)
- [Problem formulation](problem-formulation.md)
