---
summary: Reports must include a leakage audit naming each leak with before-and-after scores.
type: rule
tags: [course-rules, leakage]
sources: [lecture-02 recording, lecture-04 recording]
---
# Leakage audit with before/after numbers

For Prosit 1 the lecturer required a short **leakage audit** section in the report and the presentation. For each leak you found:
1. name it and say what kind it is (target, contamination, temporal, duplicate);
2. show the score **before** the fix and **after** the fix.

The before/after numbers prove the leak was real and show how much it inflated results. A big drop after the fix is not a failure; it is the honest number.

His checklist also said no cell may fit an encoder or scaler on train and test data together. In the preprocessing lecture he asked groups directly whether they had met leakage, and treated temporal leakage (using later data to predict earlier outcomes) as a real problem to find.

## For the capstone
Keep an audit table: e.g. "same-week rainfall used to predict same-week flood", "scaler fitted on all years", "duplicate news reports of one flood". Re-run the model with and without each, and record both scores.

## Related
- [Data leakage](data-leakage.md)
- [Temporal leakage](temporal-leakage.md)
- [Train-test contamination](train-test-contamination.md)
- [Code must run top to bottom from a fresh start](runs-top-to-bottom-from-fresh-clone.md)
