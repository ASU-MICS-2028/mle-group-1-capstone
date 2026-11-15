---
summary: Research add-on F2 — measure how much land-cover change improves prediction beyond rainfall
type: concept
tags: [flood, research-question, land-use]
sources: [Flood options report §4 F2, proposal Option B "Research Focus"]
---
# Land-change added value (F2)

The team's original idea: geography changing over time, plus flood reports and weather, together. Operationalised as an **ablation**:

1. Fit the F1 model with rainfall, soil moisture, season and static terrain only.
2. Add built-up growth (GHSL) and land-cover change (Dynamic World).
3. Measure the improvement on the 2024–2025 test set (PR-AUC, alert-budget recall), with bootstrap CIs.
4. Also compare the rainfall associated with reported floods in fast-changing vs stable areas.

**Decision it informs:** where planners and assemblies should target drainage, wetland protection or building enforcement. It speaks to the Accra literature on structural causes (Amoako & Inkoom 2017; Amoako & Frimpong Boamah 2014).

**Main limitation:** this is **association, not cause**. Places that urbanise also attract more news coverage, so an apparent "land effect" could be a reporting effect. State that plainly, and check whether the gain survives within regions or after the coverage audit.

Effort: medium, on top of F1. Add land features only **after** the baseline pipeline works (Week 12).

## For the capstone
A small, honest gain (or none) is a valid finding; report it with CIs either way.

## Related
- [GHSL built-up](ghsl-built-up.md)
- [Dynamic World](dynamic-world.md)
- [Proxy variables](proxy-variables.md)
- [Flood problem formulation](flood-problem-formulation.md)
