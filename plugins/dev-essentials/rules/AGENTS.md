# Personal Development Engineering Rules

Always-on engineering guardrails applied when `dev-essentials` is active.

## Core Principles

1. **Clarify Material Ambiguities**: Ask 2–4 targeted questions with recommended defaults when requirements are ambiguous, breaking, or irreversible. For minor local details, pick a safe default and state the assumption.
2. **Validation-Driven Development**: Before implementing non-trivial changes, define a failing test, schema check, or reproducible validation command so completion is verified against explicit pass/fail criteria.
3. **Evidence-First Verification**: Read or search files before citing paths, symbols, or behavior. Run linters, builds, and tests *after* the final edit, and report only directly observed results and exact scope.
4. **Writing Standards**: Lead explanations and docs with visuals (Mermaid diagrams, tables, scannable bullets) followed by minimal prose for non-inferable details (rationale, invariants, caveats). Stay concise without dropping context a human reader needs—define unfamiliar terms inline or in a glossary. Keep code comments focused on *why* (preserving unrelated comments), ground docs in verified repo state, and defer architectural/SDLC docs to `gyrus` when active. Load the `writing-standards` skill for full formatting and visual-selection rules.
5. **Safe-Ops Guardrails**: Never commit secrets or credentials, never disable or weaken failing tests or linters to force a pass, and confirm before destructive git or filesystem operations.
6. **Minimal, Focused Diffs**: Reuse existing repository helpers and conventions; avoid unrelated refactors or formatting churn.
