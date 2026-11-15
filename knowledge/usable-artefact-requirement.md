---
summary: The capstone must ship something a non-expert can use by following written instructions
type: rule
tags: [capstone, brief, deployment]
sources: [capstone brief §3.2, §5, §11]
---
# Usable artefact requirement

Deployment is mandatory but modest. The brief accepts a script, an API endpoint, a simple app/UI or a dashboard. It does **not** need to be production-ready or public, and a production-grade cloud service is explicitly out of scope. The test is that **a non-expert can use it by following your instructions**.

The artefact is worth its own rubric line (F, 10 points), is shown in presentation slot 5 together with a **stakeholder explainer** (plain-language guide for the intended user), and its code belongs in the repo with reproduction steps in the README.

Suggested tools in the brief: joblib (saving models), Streamlit or Gradio (apps).

## For the capstone
A Streamlit dashboard for NADMO regional offices: each region's risk this week, the recent rainfall behind it, uncertainty, and a clear caveat that the label is *reported* floods, not actual risk, plus a list of things it must not be used for.

## Related
- [End-to-end pipeline requirement](end-to-end-pipeline-requirement.md)
- [Flood decision and stakeholders](flood-decision-and-stakeholders.md)
- [Flood ethics concerns](flood-ethics-concerns.md)
