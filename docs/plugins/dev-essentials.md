# `dev-essentials` Plugin

- **Version**: `0.1.0`
- **License**: `Apache-2.0`
- **Source**: [`plugins/dev-essentials/`](../../plugins/dev-essentials)

## Purpose

Provides minimal, high-leverage engineering guardrails and workflows for AI-driven development—encouraging agents to clarify blatant ambiguities upfront, validate changes against explicit checks before/during implementation, ground claims in observed evidence, and communicate changes visually.

## What's Included

| Component | Path | Summary |
| :--- | :--- | :--- |
| **Ruleset** | [`rules/AGENTS.md`](../../plugins/dev-essentials/rules/AGENTS.md) | 7 always-on behavioral principles (1,566 bytes; auto-loaded in Antigravity). |
| **Skills (3)** | [`skills/`](../../plugins/dev-essentials/skills) | Cross-harness procedures for validation-driven development, visual explanations, and docs. |
| **Subagent (1)** | [`agents/code-reviewer.md`](../../plugins/dev-essentials/agents/code-reviewer.md) | Read-only code review persona with severity-ranked output. |
| **Hooks** | [`hooks.json`](../../plugins/dev-essentials/hooks.json) | Disabled-by-default (`"enabled": false`) `PostToolUse` template for project lint/format checks. |
| **MCP Config** | [`mcp.json`](../../plugins/dev-essentials/mcp.json), [`.mcp.json`](../../plugins/dev-essentials/.mcp.json) | Empty templates (no MCP servers bundled). |

## Top-Level Ruleset (`rules/AGENTS.md`)

1. **Clarify Blatant Ambiguities**: Ask 2–4 targeted questions with recommended defaults for materially ambiguous, breaking, or irreversible choices; state assumptions for minor defaults.
2. **Validation-Driven Development**: Write or define a failing test, schema check, or reproducible validation command before implementing non-trivial changes.
3. **Evidence-First Verification**: Read/search before citing paths or symbols; run linters/builds/tests *after* the final edit; report only directly observed results and exact scope.
4. **Visual & Structured Explanations**: Prefer Mermaid diagrams, comparison tables, and crisp bullets over walls of prose.
5. **Documentation Standards**: Explain *why* (invariants, side effects, tradeoffs) rather than *what*; preserve unrelated comments; keep `README.md` accurate; defer SDLC/architectural docs to `gyrus` when active.
6. **Safe-Ops Guardrails**: Never commit secrets, never disable/weaken failing tests or linters, and confirm before destructive git/filesystem operations.
7. **Minimal, Focused Diffs**: Reuse existing repository patterns and avoid unrelated churn.

## Skills

| Skill | When to Use | Key Details | References |
| :--- | :--- | :--- | :--- |
| **`dev-workflow`** | Starting a feature, bugfix, refactor, or pre-commit check. | Enforces a 4-step loop: **Clarify Scope -> Define Validation First -> Implement Minimal Diff -> Verify Against Evidence** (`git diff`, tests, and checklist). | [`checklist.md`](../../plugins/dev-essentials/skills/dev-workflow/references/checklist.md) |
| **`visual-explainer`** | Explaining a codebase, architecture, multi-step flow, debugging root cause, or PR/diff. | Leads with a 1–2 sentence TL;DR, selects an appropriate Mermaid diagram (`flowchart`, `sequenceDiagram`, `stateDiagram-v2`, `erDiagram`) or table, enforces Mermaid label quoting, and follows with file-linked bullets. | — |
| **`doc-standards`** | Writing or updating inline comments, public docstrings, `README.md`, or `docs/`. | Focuses comments on *why*, keeps public contracts concise, preserves unrelated existing comments, grounds docs in verified commands/paths, and respects the Gyrus boundary. | — |

## Subagent (`agents/code-reviewer.md`)

- **Role**: Read-only senior reviewer for diffs and changed files.
- **Rubric**: Correctness & edge cases, validation/test coverage (flags skipped or weakened assertions), safe-ops & security, documentation integrity, and maintainability.
- **Output**: Findings grouped by **Critical**, **Major**, **Minor**, and **Nit** with exact file paths/line numbers and uninspected scope noted.
