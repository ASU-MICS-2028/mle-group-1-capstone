---
summary: Gender Shades showed good average accuracy hiding large intersectional failures, found by auditing data first
type: source
tags: [fairness, reading, audit]
sources: [Buolamwini & Gebru 2018, Gender Shades, PMLR 81 (FAT* 2018), https://proceedings.mlr.press/v81/buolamwini18a.html]
---
# Gender Shades (Buolamwini & Gebru 2018)

The authors audited three commercial face-analysis services that classify gender. Averages looked good, but split by **gender × skin type**, darker-skinned women had error rates up to about 35% while lighter-skinned men stayed under 1%. Standard benchmarks were mostly lighter-skinned, which is why the gap went unnoticed. They built a balanced benchmark (parliamentarians from three African and three European countries) to measure it properly.

**Lessons we reuse:**
1. **Audit the data before the model** — count rows and positives per group; a group with few positives gives an unreliable error rate.
2. **Aggregate metrics hide subgroup failure** — always disaggregate.
3. **Intersections** — the worst group only appeared when two factors were crossed.
4. **Several metrics per group** — TPR, FPR, PPV, error rate.
5. **Use well-defined, measurable groups** and say what each one stands for.

## For the capstone
Same shape: training labels dominated by one population (Greater Accra, 38% of events), a model that may score well nationally while failing quietly in Oti, Bono, Ahafo and Western North (56 events between them). Step one of our audit is the per-region event and positive-week counts; then cross region with season.

## Related
- [Disaggregated evaluation](disaggregated-evaluation.md)
- [News label bias](news-label-bias.md)
- [Model cards](model-cards.md)
