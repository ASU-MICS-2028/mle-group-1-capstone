---
summary: Shuffled CV on time-ordered data lets the model peek at the future; splits must keep time order.
type: rule
tags: [cross-validation, leakage, time-series, lecturer-emphasis]
sources: [lecture-06 recording, lec5 slides]
---
# Temporal leakage in cross-validation

A student asked what to do when the order of the data matters (a time sequence). The lecturer's answer: ordinary shuffled cross-validation **may introduce temporal leakage**, so the split must preserve the sequence. (The recording is partly garbled here, but the point is clear.)

What goes wrong with shuffling: a fold might train on March 2020 and July 2020 and be validated on May 2020. The model has effectively seen the "future" around the validation week. Weather and floods are strongly linked from week to week, so the validation score looks far better than real forecasting would be.

Fixes:
- **Forward-chaining (expanding window) CV:** train on 2015–2017, validate on 2018; train on 2015–2018, validate on 2019; and so on. scikit-learn's `TimeSeriesSplit` does this.
- **A single held-out later period** for tuning (like our 2023) and a later one for testing.
- Optionally leave a **gap** between train and validation so lagged features do not overlap.

Related traps: features built with information from after the prediction date (for example a rolling mean centred on the week instead of trailing behind it), and random-forest out-of-bag scores, which also treat rows as independent.

## For the capstone
This is the core reason for our train 2015–2022 / tune 2023 / test 2024–2025 split. Expect a defence question on it.

## Related
- [Temporal split](temporal-split.md)
- [Temporal leakage](temporal-leakage.md)
- [K-fold cross-validation](k-fold-cross-validation.md)
- [Out-of-bag error](out-of-bag-error.md)
- [Leakage audit](leakage-audit-before-after.md)
