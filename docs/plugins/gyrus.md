# `gyrus` Plugin

- **Version**: `1.0.0`
- **License**: `Apache-2.0`
- **Source**: [`plugins/gyrus/`](../../plugins/gyrus)
- **Upstream Project**: [`armckinney/gyrus`](https://github.com/armckinney/gyrus)

## Purpose

Equips AI coding assistants to resolve architectural context, capture engineering decisions, and maintain structured OKF documentation through the **Gyrus Context Control Plane** (via MCP tools or the `gyrus` CLI) without duplicating low-level code diffs.

## What's Included

| Component | Path | Summary |
| :--- | :--- | :--- |
| **Ruleset** | [`rules/AGENTS.md`](../../plugins/gyrus/rules/AGENTS.md) | Always-on SDLC & OKF governance rules (loaded automatically in Antigravity). |
| **Skills (4)** | [`skills/`](../../plugins/gyrus/skills) | Workflows for SDLC context management, repo priming, legacy migration, and release testing. |
| **MCP Server** | [`mcp.json`](../../plugins/gyrus/mcp.json), [`.mcp.json`](../../plugins/gyrus/.mcp.json) | Launches local stdio server `gyrus mcp serve`. |
| **Subagents** | — | None included. |

## Top-Level Ruleset (`rules/AGENTS.md`)

1. **Source vs. Gyrus Boundary**: Source code owns implementation logic and routine bug fixes; Gyrus owns architectural intent and system governance.
2. **3-Phase SDLC Lifecycle**:
   - **Plan**: `prd`, `improvement-proposal`, `specification`, `adr`, `standards`
   - **Implement**: `technical-reference`, `guide` (while source code remains canonical for logic)
   - **Post-Implement**: `release-note`, `product`
3. **Context Resolution First**: Query `gyrus_suggest_context` / `gyrus_search` (or `gyrus suggest-context --prompt "<task>" --json`) before architectural changes.
4. **Mutability Rules**: Living docs (`prd`, `specification`, `standards`, `technical-reference`, `guide`, `product`) are updated in place; accepted decision logs (`adr`, `improvement-proposal`, `release-note`) are immutable and superseded via a new linked record (`--rel-type supersedes`).
5. **OKF Schema & Exit Codes**: Enforces lowercase IDs (`^[a-z0-9-_]+$`), required YAML frontmatter (`id`, `title`, `category`, `type`, `tenant`, `version`, `status`), and standard CLI exit codes (`0`–`5`).

## Skills

| Skill | When to Use | Key Details | References |
| :--- | :--- | :--- | :--- |
| **`gyrus`** | Resolving context, creating/updating/linking concepts, or switching Git initiative branches (`--git-branch` / `gyrus_git_switch`). | Covers primary MCP tools (`gyrus_suggest_context`, `gyrus_search`, `gyrus_get`, `gyrus_create`, `gyrus_update`, `gyrus_link`), CLI fallbacks, qualified names (`tenant/reference/id`), and `okf` / `postgres_fts` / `git` backends. | [`okf-schemas.md`](../../plugins/gyrus/skills/gyrus/references/okf-schemas.md) |
| **`gyrus-index`** | Onboarding a new or existing repository into Gyrus for the first time. | Surveys repo structure, proposes 3–4 baseline living docs (`spec`, `standards`, `technical-reference`, `guide`), confirms with the user, creates `.gyrus/concepts/` docs, and verifies retrieval. | — |
| **`gyrus-migrate-sqlite-to-okf`** | Upgrading legacy Gyrus collections or SQLite graph edges into qualified `{concept, rel}` OKF links. | Read-only preflight, explicit identity mapping, isolated staging/backups, parity checks, and zero-body-mutation guarantees (excludes PostgreSQL exports). | [`sqlite-to-okf.md`](../../plugins/gyrus/skills/gyrus-migrate-sqlite-to-okf/references/sqlite-to-okf.md) |
| **`gyrus-test-lifecycle`** | Verifying an installed `gyrus` binary end-to-end without source code or dev tooling. | Exercises CLI, MCP, and Web UI in an isolated temp workspace/home using `localfs`/OKF, leaving production collections untouched. | [`consumer-lifecycle.md`](../../plugins/gyrus/skills/gyrus-test-lifecycle/references/consumer-lifecycle.md) |

## Prerequisites

- The `gyrus` CLI binary must be installed and available on `PATH` for MCP and CLI operations; see the [`armckinney/gyrus` installation instructions](https://github.com/armckinney/gyrus#get-started).
