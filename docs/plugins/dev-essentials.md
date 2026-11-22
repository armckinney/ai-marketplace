# `dev-essentials` Plugin

- **Version**: `1.0.0`
- **License**: `Apache-2.0`
- **Source**: [`plugins/dev-essentials/`](../../plugins/dev-essentials)

## Purpose

Provides lean, always-on personal engineering guardrails, visual-first technical writing standards for humans and agents, and a read-only code review subagent across repositories.

## What's Included

| Component | Path | Summary |
| :--- | :--- | :--- |
| **Ruleset** | [`rules/AGENTS.md`](../../plugins/dev-essentials/rules/AGENTS.md) | 6 always-on engineering guardrails (auto-loaded in Antigravity). |
| **Skills (1)** | [`skills/`](../../plugins/dev-essentials/skills) | Cross-harness playbook for concise, visual-first technical writing. |
| **Subagent (1)** | [`agents/code-reviewer.md`](../../plugins/dev-essentials/agents/code-reviewer.md) | Read-only code review persona with severity-ranked output. |
| **Hooks** | [`hooks.json`](../../plugins/dev-essentials/hooks.json) | Disabled-by-default (`"enabled": false`) `PostToolUse` template for project lint/format checks. |
| **MCP Config** | [`mcp.json`](../../plugins/dev-essentials/mcp.json), [`.mcp.json`](../../plugins/dev-essentials/.mcp.json) | Empty templates (no MCP servers bundled). |

## Top-Level Ruleset (`rules/AGENTS.md`)

1. **Clarify Material Ambiguities**: Ask 2–4 targeted questions with recommended defaults for ambiguous, breaking, or irreversible choices; state assumptions for minor defaults.
2. **Validation-Driven Development**: Define a failing test, schema check, or reproducible validation command before implementing non-trivial changes.
3. **Evidence-First Verification**: Read/search before citing paths or symbols; run linters/builds/tests *after* the final edit; report only directly observed results and exact scope.
4. **Writing Standards**: Lead explanations and docs with visuals (Mermaid diagrams, tables, scannable bullets) followed by minimal prose for non-inferable details; keep writing self-contained for humans (define unfamiliar terms inline or via glossary); keep code comments focused on *why*; defer architectural/SDLC docs to `gyrus` when active.
5. **Safe-Ops Guardrails**: Never commit secrets, never disable/weaken failing tests or linters, and confirm before destructive git/filesystem operations.
6. **Minimal, Focused Diffs**: Reuse existing repository helpers and conventions; avoid unrelated churn.

## Skills

| Skill | When to Use | Key Details |
| :--- | :--- | :--- |
| **`writing-standards`** | Drafting or editing persistent docs (`README.md`, `docs/`, Gyrus concepts, specs, ADRs, guides) or conversational outputs (explanations, walkthroughs, PR summaries). | Enforces visual-first communication (Mermaid selection guide & syntax safety, Markdown tables, bullets) paired with minimal non-inferable prose, self-contained human comprehension with inline/glossary definitions, verified repo grounding, and Gyrus boundaries. |

## Subagent (`agents/code-reviewer.md`)

- **Role**: Read-only senior reviewer for diffs and changed files.
- **Rubric**: Correctness & edge cases, validation/test coverage (flags skipped or weakened assertions), safe-ops & security, documentation integrity, and maintainability.
- **Output**: Findings grouped by **Critical**, **Major**, **Minor**, and **Nit** with exact file paths/line numbers and uninspected scope noted.
