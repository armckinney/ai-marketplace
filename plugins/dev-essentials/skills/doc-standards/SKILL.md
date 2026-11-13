---
name: doc-standards
description: >-
  Enforces concise, accurate code comments, docstrings, and repository
  documentation while keeping architectural SDLC docs cleanly separated when
  Gyrus is active. Use when writing or updating docs, comments, or READMEs.
---

# Documentation Standards

Keep documentation high-signal, accurate to the current code, and appropriately scoped.

## Code Comments & Docstrings

1. **Document *Why*, Not *What***:
   - Use inline comments to explain non-obvious invariants, ordering constraints, edge-case guards, or workarounds.
   - Avoid narrating obvious syntax or line-by-line control flow.
2. **Concise Public Contracts**:
   - Give new public functions, classes, and CLI scripts a brief docstring covering purpose, inputs/outputs, and notable side effects.
3. **Preserve Documentation Integrity**:
   - Keep existing comments and docstrings that are unrelated to your changes intact.
   - Update or remove comments that your code change renders inaccurate.

## Repository Docs (`README.md` & `docs/`)

- Ground every documented file path, CLI flag, config key, and output example in what actually exists in the repository.
- Keep `README.md` focused on purpose, quickstart, setup, and links rather than duplicating code internals.
- Prefer tables and copy-pasteable commands over long narrative sections.

## Gyrus Boundary

- When `gyrus` is active in a repository, architectural intent, specifications, ADRs, and guides belong in Gyrus concepts—do not duplicate routine code diffs or function logic into Gyrus, and do not scatter competing ADR/spec silos across ad-hoc markdown files.
