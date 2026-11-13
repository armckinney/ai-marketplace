# Harness Compatibility

`ai-marketplace` targets four agent harnesses from a single repository layout under `plugins/<name>/`, prioritizing **Codex CLI** and **Antigravity CLI**, with full support for **Copilot CLI** and secondary support for **Claude Code CLI**.

## Marketplace Catalog Files

| Harness | Catalog / Discovery Path | Source Format |
| :--- | :--- | :--- |
| **Codex CLI** | `.agents/plugins/marketplace.json` | `{ "source": "local", "path": "./plugins/<name>" }` |
| **Antigravity CLI** | `.agents/plugins.json` | `{ "entries": [{ "path": "plugins" }] }` |
| **Copilot CLI** | `.github/plugin/marketplace.json` | `"./plugins/<name>"` |
| **Claude Code CLI** | `.claude-plugin/marketplace.json` | `"./plugins/<name>"` |

## Per-Plugin Manifest & Config Files

| File | Purpose | Used By |
| :--- | :--- | :--- |
| `plugin.json` | Agent Plugins 1.0.0 + Antigravity root manifest | Antigravity, Copilot |
| `.codex-plugin/plugin.json` | Codex manifest (`skills`, `mcpServers`, `interface`) | Codex |
| `.claude-plugin/plugin.json` | Claude Code manifest (`skills`, `agents`, `hooks`) | Claude Code |
| `mcp.json` | Agent Plugins 1.0.0 MCP server definition | Antigravity, Copilot |
| `.mcp.json` | Claude & Codex MCP server definition | Codex, Claude Code |
| `mcp_config.json` | Antigravity legacy MCP fallback (`enable-agent-plugins-spec` off) | Antigravity |
| `hooks.json` | Root lifecycle hooks config | Antigravity, Claude Code (`"hooks": "./hooks.json"`), Copilot |

## Variable Expansion & Validation Notes

- **Agent Plugins 1.0.0 (`mcp.json`)**: Antigravity's `agy plugin validate` only expands `${PLUGIN_ROOT}` and `${PLUGIN_DATA}` inside `mcp.json`; avoid `${workspaceFolder}` in `mcp.json` (use CWD fallback or put `${workspaceFolder}` only in `.mcp.json` / `mcp_config.json` when needed).
- **Icons (`logo`)**: Include `assets/logo.svg` or `assets/logo.png` and declare `"logo"` in `plugin.json` and `.codex-plugin/plugin.json` so marketplace UIs render an icon and `agy plugin validate` emits no missing-logo note.
- **Skills over Commands**: Prefer `skills/<skill>/SKILL.md` instead of `commands/` so workflows work consistently across Codex, Antigravity, Copilot, and Claude Code.
