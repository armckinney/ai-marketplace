---
name: visual-explainer
description: >-
  Structures technical explanations using Mermaid diagrams, Markdown tables, and
  concise bullet points instead of walls of prose. Use when explaining a
  codebase, architecture, multi-step flow, debugging root cause, or PR/diff.
---

# Visual & Structured Explanations

Translate complex codebases, changes, and design tradeoffs into scannable visuals and crisp summaries.

## Format Guidelines

1. **Lead with a TL;DR**: Open with 1–2 sentences summarizing the takeaway or change.
2. **Pick the Right Visual**:
   - **Architecture, pipelines, or dependencies**: `flowchart TD` or `flowchart LR`
   - **Agent, API, or service interactions**: `sequenceDiagram`
   - **Lifecycles or status transitions**: `stateDiagram-v2`
   - **Data schemas or entities**: `erDiagram`
   - **Tradeoffs, config matrices, or before/after comparisons**: Markdown tables
3. **Follow with Scannable Bullets**:
   - Group bullets by component or impact.
   - Link exact verified file paths and symbol names (e.g., `path/to/file.go#L42`).
   - Distinguish verified facts from inferences explicitly.

## Mermaid Syntax Safety

- Quote node labels containing parentheses, brackets, slashes, or colons:
  - Good: `api["API Gateway (v2)"]`
  - Avoid: `api[API Gateway (v2)]`
- Avoid raw HTML tags (such as `<br/>` or `<b>`) inside node labels.
- Keep diagrams focused (roughly 5–12 nodes); split larger systems into layered diagrams rather than one unreadable graph.
