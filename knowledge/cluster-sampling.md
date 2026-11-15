---
summary: Cluster sampling picks whole groups; units inside a group are alike, so not independent.
type: concept
tags: [sampling, uncertainty]
sources: [probability & sampling slides, lecture-03 recording]
---
# Cluster sampling

In **cluster sampling** you split the population into groups (clusters, also called primary sampling units), randomly pick some of the groups (e.g. 10 of 20 villages), and measure everyone inside the chosen groups.

It is cheap: the survey team visits fewer places. The cost is that units in the same cluster **resemble each other** (same weather, same health facility, same net campaign). They are **not independent**, so each extra household from the same village adds less new information than a household from a new village.

Slide example: in the Ghana survey, net ownership per cluster ranged from about 20% to nearly 100%.

If you ignore clustering, standard errors and confidence intervals come out too small.

## For the capstone
Our data are clustered too: the 16 regions in the same week share a weather system, and weeks in one season share conditions. Treat weeks (or blocks of weeks) as clusters when estimating uncertainty.

## Related
- [Stratified sampling](stratified-sampling.md)
- [Design effect](design-effect.md)
- [Cluster bootstrap](cluster-bootstrap.md)
