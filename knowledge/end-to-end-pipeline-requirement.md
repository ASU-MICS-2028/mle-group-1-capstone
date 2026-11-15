---
summary: The capstone must run the whole ML pipeline, from problem to defensible story, not stop at a score
type: rule
tags: [capstone, brief, scope]
sources: [capstone brief §1, lecture-01 recording]
---
# The capstone must be end-to-end

The Final Capstone is the course's examination (40% of the grade). Unlike the prosits, where the instructor framed the problem, here the team picks the problem, turns it into an ML task, and then builds, evaluates, documents and defends a complete system.

"End-to-end" is the key word. A notebook that ends with a good accuracy number counts as **incomplete**. The brief lists the chain every project must walk through:

problem → ML task → data → preprocessing → features → models → validation → metrics → fairness and ethics review → documentation → usable artefact → defensible story.

Each link should leave visible evidence in the repo or the talk. If a link is weak (for example, no artefact, or no fairness review), the project is judged as unfinished regardless of how good the model is.

The lecturer said the same thing in the very first lecture: many people learning ML stop when the model runs in a notebook, but that is not the end of the process. An end-to-end project ends in deployment, such as a web or mobile app. MLOps (running models in production) is touched on near the end of the course.

## For the capstone
Use the chain as a checklist for the flood classifier: Groundsource labels → region-week table → rainfall/soil/terrain features → baselines + 4 models → temporal split → PR-AUC/alert-budget recall/calibration → per-region fairness audit → Datasheet + Model Card → Streamlit dashboard → defence.

## Related
- [Capstone learning outcomes](capstone-learning-outcomes.md)
- [Capstone deliverables](capstone-deliverables.md)
- [Usable artefact requirement](usable-artefact-requirement.md)
- [Flood problem formulation](flood-problem-formulation.md)
