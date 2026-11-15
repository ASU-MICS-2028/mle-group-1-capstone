@AGENTS.md

## Claude Code specifics
- **Follow `AGENTS.md`.** Before starting work, find the issue and the plan file for it. If neither exists, propose one and don't start.
- **When you finish a change,** write the change file, including your own row in the AI-use table that says what you did and what the human should check. Then update each index you touched and the plan's status.
- **Never print real data rows.** Run Python on files in `data/` with `-I` and pass paths as arguments.
- **Explain like a patient teacher.** The humans will be questioned without you, so add a small made-up example whenever an idea is abstract.
- **Subagents** are fine for reading course material and searching. Don't give them raw data rows, and review what they write before committing it.
- **Check `knowledge/` before explaining a concept,** and cite the note. Add new course knowledge as a new atomic note.
