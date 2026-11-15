---
summary: Counts across units of different size mostly measure size; model or map rates instead
type: lesson
tags: [features, geospatial, count-models]
sources: [prosit-1 notebook §3, §10, §12 and §15A, prosit-1 personal notes §3]
---
# Normalise by exposure before comparing regions

In Prosit 1, ranking districts on raw case counts and on rates shared only half the top 10: populous districts dominate counts. A map of counts is a population map. We used rates for maps (with quantile colour bins) and a log(population) **offset** in the Negative Binomial model, so the model described cases per person. Leaving the offset out made the model predict population size, and changed the fitted dispersion (0.34 instead of 0.42), because size differences were mixed into the "extra variance".

Also noted: once region was added as a covariate, dispersion fell from 0.42 to 0.14. Much of the between-district spread was regional.

## For the capstone
The chance that at least one flood is *reported* in a region-week grows with region area, population, urbanisation and media presence, not only with flood hazard. Consider exposure features (population, built-up share, area) and check whether the model is mostly learning "big urban region" (e.g. Greater Accra). Show per-region base rates next to predictions in the dashboard so a high probability isn't mistaken for high hazard alone.

## Related
- [missing-is-not-zero.md](missing-is-not-zero.md)
- [harmonise-boundaries-before-joining.md](harmonise-boundaries-before-joining.md)
- [hiding-a-column-does-not-hide-the-group.md](hiding-a-column-does-not-hide-the-group.md)
