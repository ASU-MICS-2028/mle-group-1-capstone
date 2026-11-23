---
summary: Label-rule choices barely matter, except big polygons under an "any region touched" rule
type: result
tags: [labels, groundsource, w01]
sources: [learnings/tables/w01_label_options.csv]
---
# Large polygons drive most of the label disagreement

We built the region-week label 8 ways: centroid vs every touched region, start week vs every week covered, and keeping vs dropping polygons over 500 km². Six options give a positive rate between 6.0% and 6.7%. The outlier is "every touched region + keep large polygons" at 7.9%: one vague report of a flood "in the north" marks several regions at once.

So the label definition is not where the uncertainty is. Whether the news report is right at all matters more (60–75% accuracy, see the Groundsource note), and so does which regions get reported (Ahafo has none).

## For the capstone
Main model: centroid + start + keep all (decision 0007). Robustness check: intersects + drop > 500 km².

## Related
- [Source or stress-test every assumed number](source-or-stress-test-every-assumed-number.md)
- [Test every diverging path in a table](test-every-diverging-path-in-a-table.md)
