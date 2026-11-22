---
name: writing-standards
description: >-
  Guides clear, concise, visual-first technical writing for humans and agents
  across persistent documentation (READMEs, docs/, Gyrus concepts, specs, ADRs,
  guides) and conversational outputs (architecture walkthroughs, debugging
  summaries, PR descriptions). Use when drafting or editing docs, explaining
  systems or changes, or summarizing technical decisions.
---

# Writing Standards

Write concisely so both humans and agents comprehend content quickly—without sacrificing context a human reader needs to understand it independently.

## Core Principles

1. **Visual-First, Detail-Second**: Default to diagrams, tables, and structured bullets for architectures, flows, lifecycles, and comparisons. Follow visuals with **minimal prose** that adds only significant details not easily inferred from the visual (invariants, failure modes, tradeoffs, exact paths/commands).
2. **Concise Without Context Loss**: Cut filler and narration of the obvious, never essential rationale or prerequisites. Every document or explanation must make sense to a human reader who does not share the agent's hidden conversation context.
3. **Define Unfamiliar Terms**:
   - **1–3 domain terms or acronyms**: Define inline on first use (e.g., *Open Knowledge Format (OKF)*).
   - **4+ recurring specialized terms**: Add a concise `## Glossary` table (or link to a Gyrus `glossary` concept when Gyrus is active).
4. **Evidence-Grounded**: Verify every file path, symbol, CLI flag, config key, and output example against the actual repository. Explicitly separate verified facts from inferences or assumptions.

## Visual Selection Guide

| Information Type | Preferred Format | Follow-Up Details to Include |
| :--- | :--- | :--- |
| Architecture, pipelines, dependencies | `flowchart TD` / `flowchart LR` | Ownership boundaries, failure paths, non-obvious ordering |
| API, service, or agent interactions | `sequenceDiagram` | Sync vs. async semantics, retries, auth boundaries |
| Lifecycles or status transitions | `stateDiagram-v2` | Immutability rules, illegal transitions, triggers |
| Data schemas or entity models | `erDiagram` | Cardinality invariants, required keys, constraints |
| Tradeoffs, config options, before/after | Markdown table | Decision criteria, defaults, breaking impacts |
| Ordered procedures or caveats | Numbered / bulleted lists | Exact verified commands, preconditions, edge cases |

### Mermaid Syntax Safety

- Quote node labels containing parentheses, brackets, slashes, or colons (e.g., `api["API Gateway (v2)"]`, not `api[API Gateway (v2)]`).
- Never use raw HTML tags (`<br/>`, `<b>`) inside node labels.
- Keep graphs scannable (~5–12 nodes); split larger systems into layered diagrams.

## Surface Guidelines

### Conversational Outputs (Explanations, Walkthroughs, PR Summaries)

- Lead with a 1–2 sentence **TL;DR** stating the core takeaway or change.
- Present the visual or comparison table, then brief grouped bullets with verified file paths/symbols and non-inferable caveats.

### Persistent Docs (`README.md`, `docs/`, Gyrus Concepts)

- State scope and audience upfront when non-obvious.
- Keep `README.md` focused on value, quickstart, setup, and navigation rather than duplicating code internals.
- Use repository-relative links (never machine-specific `file://` URLs) in committed documentation.
- **Gyrus Boundary**: When `gyrus` is active, place architectural intent, specs, ADRs, standards, and guides in Gyrus concepts instead of competing ad-hoc markdown files; never mirror routine code diffs into docs.
