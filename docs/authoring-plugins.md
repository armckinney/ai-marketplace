# Plugin Authoring & Artifact Scoping

All artifacts in `ai-marketplace` live inside self-contained plugin bundles under `plugins/<plugin-name>/`.

## Artifact Types Inside a Plugin

| Artifact | Path | Use When |
| :--- | :--- | :--- |
| **Skills** | `skills/<skill>/SKILL.md` (+ `references/`, `scripts/`, `examples/`) | Teaching repeatable procedures, runbooks, checklists, and progressive-disclosure docs across all 4 harnesses. |
| **Rules** | `rules/AGENTS.md` | Always-on behavioral guardrails, standards, and constraints (`≤24 KB` per file in Antigravity). |
| **Subagents** | `agents/<agent>.md` | Specialized isolated personas (e.g., code reviewer, security auditor). Scaffolded for new personal-dev plugins; omit when not needed (e.g., `gyrus`). |
| **Hooks** | `hooks.json` | Deterministic shell scripts on lifecycle events (`PreToolUse`, `PostToolUse`, `SessionStart`, `Stop`). Place `hooks.json` at the plugin root for Antigravity and reference `"./hooks.json"` in `.claude-plugin/plugin.json`. Keep template hooks `"enabled": false` until needed. |
| **MCP Servers** | `mcp.json`, `.mcp.json`, `mcp_config.json` | Bundled external tool servers. |

## Creating a New Plugin

1. Run the generator:
   ```bash
   make new-plugin NAME=my-plugin DESC="Short description"
   ```
   Add `WITH_MCP=1` and/or `WITH_HOOKS=1` if the plugin needs MCP server configs or lifecycle hooks.
2. Implement your skills under `plugins/<name>/skills/`, rules in `plugins/<name>/rules/AGENTS.md`, and subagents under `plugins/<name>/agents/`.
3. Add a single-page guide at `docs/plugins/<name>.md` and link it from [README.md](../README.md).
4. Run `make validate` and verify there are zero errors.
5. Test locally with `agy plugin install ./plugins/<name>` or `codex plugin marketplace add .`.
