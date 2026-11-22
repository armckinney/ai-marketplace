---
name: gyrus-index
description: >-
  Gyrus Repository Primer skill. Surveys codebase architecture, dependencies,
  and standards, proposes scope-aligned baseline living documents (spec,
  standards, technical reference, guide, and optional product/glossary),
  confirms with the developer, and creates validated Gyrus concepts.
applyTo:
  - "**"
---

# Gyrus Repository Primer Skill (`/gyrus-index`)

Survey a new or existing repository and prime Gyrus with high-level living concepts aligned to the Gyrus documentation strategy—without duplicating low-level code implementations.

## Primer Workflow

### Step 1: Survey Codebase Architecture

- Inspect root layout, package manifests (`go.mod`, `package.json`, `Cargo.toml`, `pyproject.toml`), `README.md`, build/test configs, and entry points.
- Identify project slug, primary language/runtime, architectural style, public interfaces, and external dependencies.

### Step 2: Propose Baseline Living Documents

Propose a focused set of project-scoped living concepts (use `reference` scope only for standards or decisions shared across multiple repositories):

| Suggested Local ID | Type | Scope | Captures |
| :--- | :--- | :--- | :--- |
| `spec-001-architecture` | `specification` | `project` | System topology, component boundaries, core contracts, data flows |
| `standards-001-guidelines` | `standards` | `project` or `reference` | Engineering quality rules, testing strategy, repo/git conventions |
| `tech-ref-001-interfaces` | `technical-reference` | `project` | Public CLI commands, API/MCP contracts, configuration parameters |
| `guide-001-onboarding` | `guide` | `project` | Environment setup, build/test workflow, common runbooks |
| `glossary-001-domain` *(optional)* | `glossary` | `project` or `reference` | Shared domain terms when the codebase introduces dense jargon |

### Step 3: Developer Review & Confirmation

- Present the proposed document table (local IDs, types, scope/project, and high-level outline) to the developer.
- Confirm tenant, project slug, and any additions/omissions before creating concepts.

### Step 4: Create Confirmed Concepts

- Prefer `gyrus_create` MCP tool (or `gyrus create` CLI) with explicit `tenant`, `scope`, and `project` so Gyrus enforces schema validation and canonical paths:
  - Project scope: `.gyrus/concepts/<tenant>/projects/<project>/<id>.md`
  - Reference scope: `.gyrus/concepts/<tenant>/reference/<id>.md`
- Ensure valid OKF frontmatter (`id`, `title`, `category`, `type`, `tenant`, `version: 1`, `status: active`) and omit derived fields (`name`, `scope`, `project`).
- Capture **high-level intent, boundaries, and rationale**; add typed links (`depends_on`, `implements`) between related baseline concepts using qualified names.

### Step 5: Verify Retrieval & Schema Compliance

- List indexed concepts via `gyrus_search` (empty query) or `gyrus search --query "" --scope all --max-results 0 --json` and confirm every created qualified name appears.
- Run `gyrus validate <filepath> --json` on any manually written files.
- Report created qualified names and confirmed validation output to the developer.
