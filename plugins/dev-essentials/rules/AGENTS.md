# Personal Development Engineering Rules

Lean, always-on guidelines applied across repositories when `dev-essentials` is active.

## Core Principles

1. **Clarify Blatant Ambiguities**: Ask 2–4 targeted questions with recommended defaults when requirements are materially ambiguous, breaking, or irreversible. For minor local details, pick a safe default and state the assumption.
2. **Validation-Driven Development**: Before implementing non-trivial changes, write or define a failing test, schema check, or reproducible validation command so work is verified against explicit pass/fail criteria.
3. **Evidence-First Verification**: Read or search files before citing paths, symbols, or behavior. Run linters, builds, and tests *after* the final edit, and report only directly observed results and exact scope.
4. **Visual & Structured Explanations**: Prefer Mermaid diagrams, comparison tables, and crisp bullet points over walls of prose when explaining architectures, flows, or tradeoffs.
5. **Documentation Standards**: Document *why* (invariants, side effects, non-obvious tradeoffs) rather than narrating *what*. Preserve unrelated comments/docstrings, keep `README.md` accurate, and defer architectural/SDLC docs to `gyrus` when active.
6. **Safe-Ops Guardrails**: Never commit secrets or credentials, never disable or weaken failing tests/linters to force a pass, and confirm before destructive git or filesystem operations.
7. **Minimal, Focused Diffs**: Reuse existing repository helpers and conventions; avoid unrelated refactors or formatting churn.
