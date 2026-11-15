---
summary: A random variable is a numeric outcome; its distribution gives each value's probability.
type: concept
tags: [probability, foundations]
sources: [lecture-03 recording, probability & sampling slides]
---
# Random variable and distribution

A **random variable** (written with a capital letter, X) is a number that describes the outcome of something that varies. The lecturer's phrasing: the random variable is the *question*; the observed value (small x) is the *answer*.

Examples: "how many nets does this household own?" or "did this household have a flood this week? (1/0)".

A **distribution** is the rule that says how likely each value of X is. A distribution has **parameters**: the knobs that set its shape, such as p (chance of success), λ (rate), μ (mean) or σ (standard deviation). The lecturer compared parameters to the settings of an ML model.

Two summaries of any distribution:
- **Expectation** E[X]: the long-run average.
- **Variance** Var(X): the average *squared* distance from the mean. Squaring stops positive and negative deviations cancelling out. Its square root is the standard deviation, in the original units.

The lecture's first guiding question was: *what process produced this data?* Picking a distribution is answering that question.

## For the capstone
Our label is a random variable: Y = 1 if a region has a reported flood that week. Rainfall is another (a continuous one).

## Related
- [PMF vs PDF](pmf-vs-pdf.md)
- [Bernoulli distribution](bernoulli-distribution.md)
- [Choosing a distribution](choosing-a-distribution.md)
