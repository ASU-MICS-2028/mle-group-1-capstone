---
summary: Fitting a distribution is modelling; be ready to say what it adds over raw summaries.
type: rule
tags: [probability, presentation, course-rules]
sources: [lecture-03 recording]
---
# A fitted distribution is a model

The lecturer said a fitted distribution is itself a model, just like a linear regression. You fit the data to it, then use it to make estimates, e.g. "about 20% of people in the north had malaria this year", with a measure of uncertainty.

He warned he would ask at the presentations: **how would your numbers differ if you had not fitted a distribution?** In other words, why is a model better than just describing the raw data?

A good answer:
- raw averages from small or noisy groups jump around; a model borrows strength and gives a stable estimate;
- the model gives probabilities of unseen values (e.g. chance of an extreme count) and intervals;
- but only if its assumptions fit – a Poisson on over-dispersed data gives falsely narrow intervals.

## For the capstone
Same logic for our classifier: be ready to say what the model adds over the raw historical flood rate of each region (the baseline). If it adds little, say so.

## Related
- [Choosing a distribution](choosing-a-distribution.md)
- [Defend every number](defend-every-number.md)
- [Over-dispersion](over-dispersion.md)
