---
summary: AI tools see shapes, counts, aggregates and made-up rows, never real data rows
type: lesson
tags: [ai-use, data-handling, ethics]
sources: [prosit-2 ADR 0003, prosit-2 AGENTS.md data rules, prosit-1 README, prosit-1 reflection AI declaration]
---
# Never show raw rows to an AI tool

The course rule and the data licences forbid uploading provided datasets to generative AI. In Prosit 1 the rule was in the README, yet during a first file inspection an AI assistant displayed the header and first two rows of the survey extract, and we had to declare it. Inspection is exactly when it slips.

In Prosit 2 we made it mechanical:
- AI coding agents must not run `df.head()`, `df.sample()` or print individual records. Shapes, counts, value counts, summary statistics and scores are fine.
- To explain or test logic, use a **made-up row** (we had a fictional applicant in the feature module's self-checks).
- `data/` is in `.gitignore`; the repo is public, so no course files, personal data or staff contacts either.
- Each AI-use log line says "only aggregates were shown".
- For Colab, data came from each member's own Drive, never through an AI tool.

## For the capstone
Groundsource and the climate data are public, but news-derived flood records can name places and people, and the repo is public. Keep the same rule: inspect with `df.shape`, `df.dtypes`, `df.describe()` and counts; never paste records into a chat or commit them.

## Related
- [log-actions-and-ai-use-as-you-go.md](log-actions-and-ai-use-as-you-go.md)
- [check-the-data-against-the-brief-first.md](check-the-data-against-the-brief-first.md)
