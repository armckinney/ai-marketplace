---
name: dev-workflow
description: >-
  Guides validation-driven personal development workflows: clarifying material
  ambiguities, defining validations before implementation, keeping diffs minimal,
  and verifying results with direct evidence. Use when starting a feature,
  bugfix, refactor, or pre-commit check.
---

# Validation-Driven Development Workflow

Use this procedure to plan, validate, implement, and verify code changes reliably across repositories.

## Procedure

1. **Clarify Scope & Ambiguities**:
   - Inspect target files, callers, and existing tests before proposing or making edits.
   - If requirements are materially ambiguous, breaking, or irreversible, ask 2–4 crisp questions (with recommended defaults) before editing.
   - For minor conventions, adopt existing repository patterns and state any assumptions.

2. **Define Validation First**:
   - Before modifying implementation code, establish a concrete validation target:
     - **Features / Bugfixes**: Write a failing unit or integration test reproducing the bug or asserting the expected contract.
     - **CLI / Config / Scripts**: Define the exact validation command, schema check, or dry-run assertion and capture the baseline failure.
   - Confirm the validation fails for the expected reason before writing the fix.

3. **Implement a Minimal, Focused Diff**:
   - Reuse existing helpers, types, and error-handling patterns in the repository.
   - Keep changes strictly scoped to the task; avoid unrelated refactors or formatting churn.

4. **Verify Against Evidence**:
   - Run the new validation plus the repository's relevant formatter, linter, and test suite *after* the final edit.
   - Inspect `git diff` and complete [checklist.md](references/checklist.md).
   - Report exact commands run, observed pass/fail counts, and any unverified or skipped scope honestly.
