---
summary: Which laws and licences bear on the flood model — data protection, disaster management, data licences
type: rule
tags: [ethics, regulation, ghana]
sources: [capstone brief §5, Data Protection Act 2012 (Act 843) via prosit-2 regulation.md, dataset licence pages in Flood options report]
---
# Regulatory mapping for the flood project

The ethics pack must map the system to the rules that apply. For our project:

- **Data Protection Act, 2012 (Act 843)** — Ghana's data-protection law, still in force as far as the team found (a 2025 bill was reported in draft). It governs personal data. Our inputs (news-derived event polygons, gridded rainfall, terrain, aggregated population) are **not personal data**, and outputs are per region, so the Act mostly does not bite. It would apply if we obtained incident records naming people (e.g. from NADMO), and it supports keeping row-level personal data out of the public repo. Act 843 also restricts processing of special categories of personal data (race, religion, politics etc.); we collect none.
- **Disaster-management mandate** — NADMO is the national body responsible for disaster preparedness and response; the dashboard supports, not replaces, its decisions. The governing statute is the **National Disaster Management Organisation Act, 2016 (Act 927)**, gazetted 22 Sep 2016. It repealed the 1996 Act (Act 517) and sets up NADMO with national, regional and district offices and disaster-management committees, which are exactly the levels our region-week alert serves. *Checked 2026-11-15 against FAOLEX/UNEP LEAP (https://leap.unep.org/en/countries/gh/national-legislation/national-disaster-management-organisation-act-2016-act-927) and judy.legal (https://www.judy.legal/legislation/akn/gh/act/2016/927). The section numbers have not been read yet: read the Act itself before quoting a section.*
- **Data licences** — Groundsource CC BY 4.0 (attribution); Global Flood Database CC BY-NC 4.0 (non-commercial); EM-DAT free for non-commercial use after registration; OpenStreetMap ODbL (share-alike for derived databases); Copernicus products need attribution. Re-read each licence page before submission.
- **Course rules** — no personal data to AI tools; AI-use declaration.

## For the capstone
Present this as a table in the ethics pack (rule → what it requires → how we comply → gaps). Name the gap honestly: no agreement with NADMO yet.

## Related
- [Ethics and fairness review pack](ethics-and-fairness-review-pack.md)
- [Groundsource dataset](groundsource-dataset.md)
- [Flood ethics concerns](flood-ethics-concerns.md)
- [AI-use policy](ai-use-policy.md)
