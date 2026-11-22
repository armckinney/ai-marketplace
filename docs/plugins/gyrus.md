# `gyrus` Plugin

- **Version**: `1.0.0`
- **License**: `Apache-2.0`
- **Source**: [`plugins/gyrus/`](../../plugins/gyrus)
- **Upstream Project**: [`armckinney/gyrus`](https://github.com/armckinney/gyrus)

## Purpose

Equips AI coding assistants to discover, query, traverse, and maintain structured OKF (Open Knowledge Format) architectural context through the **Gyrus Context Control Plane** (MCP primary, with CLI fallback) without duplicating low-level code diffs.

## What's Included

| Component | Path | Summary |
| :--- | :--- | :--- |
| **Ruleset** | [`rules/AGENTS.md`](../../plugins/gyrus/rules/AGENTS.md) | Always-on documentation strategy, dependency graph, Read/Write scoping, and OKF governance rules (auto-loaded in Antigravity). |
| **Skills (2)** | [`skills/`](../../plugins/gyrus/skills) | Operational workflows for Gyrus MCP context discovery/authoring and repository priming. |
| **MCP Server** | [`mcp.json`](../../plugins/gyrus/mcp.json), [`.mcp.json`](../../plugins/gyrus/.mcp.json) | Launches local stdio server `gyrus mcp serve`. |
| **Subagents** | — | None included. |

## Top-Level Ruleset (`rules/AGENTS.md`)

1. **Core Principles**: Source code owns implementation; Gyrus owns architectural intent, contracts, and rationale. Resolve context via MCP before designing, debugging, or changing architecture/contracts; update owning concepts in the same change as behavior shifts; avoid link-only stubs; right-size documentation to the change.
2. **Document Dependency Graph (Internal Development Flow)**: Enforces progression from `prd` → `improvement-proposal` → `specification` / `adr` / `standards` → `technical-reference` / `guide` → `product` → `release-note` (when publishing a release).
3. **11 Document Types, Mutability & Read/Write Scoping**: Defines living types (`prd`, `specification`, `standards`, `technical-reference`, `guide`, `product`, `glossary`, `freeform`) vs. historical immutable types (`improvement-proposal`, `adr`, `release-note`). Defaults reads/discovery to `scope: "all"` (catching shared `reference` docs alongside repo-specific `projects/<project>` docs) while requiring explicit `project` vs. `reference` scope on writes.
4. **Identity, Links & Immutability**: Enforces lowercase local IDs (`^[a-z0-9-_]+$`), qualified names (`<tenant>/reference/<id>` or `<tenant>/projects/<project>/<id>`), minimal typed links (`depends_on`, `implements`, `supersedes`, `mitigates`), superseding protocol for accepted ADRs/proposals, and repository-relative body links.

## Skills

| Skill | When to Use | Key Details | References |
| :--- | :--- | :--- | :--- |
| **`gyrus`** | Discovering/querying architectural context, traversing concept dependencies/backlinks, authoring or linking concepts, or switching Git initiative branches (`gyrus_git_switch`). | Covers the MCP-first discovery & graph workflow (`gyrus_suggest_context`, `gyrus_search`, `gyrus_get`, `gyrus_neighbors`, `gyrus_traverse`), Read/Write scoping, authoring & ADR checklists, User Discovery Flow, schema tools, Git branching sessions, and a 1-line CLI fallback. | [`okf-schemas.md`](../../plugins/gyrus/skills/gyrus/references/okf-schemas.md) |
| **`gyrus-index`** | Onboarding a new or existing repository into Gyrus for the first time. | Surveys repo structure, proposes project- or reference-scoped living docs (`specification`, `standards`, `technical-reference`, `guide`, optional `glossary`), confirms with the user, creates concepts via MCP/CLI, and verifies retrieval and validation. | — |

## Prerequisites

- The `gyrus` CLI binary must be installed and available on `PATH` to run `gyrus mcp serve` (and optional CLI fallback); see the [`armckinney/gyrus` installation instructions](https://github.com/armckinney/gyrus#get-started).
