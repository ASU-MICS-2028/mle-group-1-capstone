---
summary: Counts use a PMF (probabilities); measurements use a PDF (densities, only intervals have probability).
type: concept
tags: [probability]
sources: [lecture-03 recording, probability & sampling slides]
---
# PMF vs PDF

- **Discrete** variables can be counted: nets, patients, flood events. They have a **probability mass function (PMF)**: p(x) = P(X = x). All the probabilities add to 1.
- **Continuous** variables can take any value in a range: temperature, rainfall, waiting time. They have a **probability density function (PDF)** f(x).

The key trap: **a density is not a probability**. For a continuous variable the chance of hitting one exact value is 0. Only an interval has a probability, found by taking the area under the density over that interval.

Example: P(rain is exactly 12.000 mm) = 0, but P(rain between 10 and 15 mm) can be 0.2.

How wide should the interval be? A student asked this; the lecturer said there is no standard, it depends on the domain (e.g. the medical fever threshold for temperature).

Both kinds have a **cumulative distribution function** F(x) = P(X ≤ x).

Also: a number with decimals can still be a count underneath (e.g. cases per 1,000 people).

## For the capstone
Weekly rainfall and soil moisture are continuous; the flood label is discrete (0/1); the number of flood reports in a week would be a count.

## Related
- [Random variable and distribution](random-variable-and-distribution.md)
- [Normal distribution](normal-distribution.md)
