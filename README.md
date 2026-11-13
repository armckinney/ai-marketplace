# ai-marketplace

Personal AI Marketplace for plugins, skills, rules, subagents, hooks, and MCP servers across **OpenAI Codex CLI**, **Google Antigravity CLI**, **GitHub Copilot CLI**, and **Claude Code CLI**.

Licensed under [Apache-2.0](LICENSE).

## Plugins

| Plugin | Version | Description | Docs |
| :--- | :--- | :--- | :--- |
| [`gyrus`](plugins/gyrus) | `1.0.0` | Gyrus: Unified Context Control Plane & Memory Engine for AI Agents | [Plugin Guide](docs/plugins/gyrus.md) |
| [`dev-essentials`](plugins/dev-essentials) | `0.1.0` | Core personal development workflow, visual explanations, documentation standards, and engineering guardrails | [Plugin Guide](docs/plugins/dev-essentials.md) |

## Native Installation

Install directly from GitHub using each harness's native commands:

### OpenAI Codex CLI (`codex`)

```bash
codex plugin marketplace add armckinney/ai-marketplace
codex plugin add gyrus@ai-marketplace
codex plugin add dev-essentials@ai-marketplace
```

### Google Antigravity CLI (`agy`)

```bash
agy plugin install https://github.com/armckinney/ai-marketplace/tree/main/plugins/gyrus
agy plugin install https://github.com/armckinney/ai-marketplace/tree/main/plugins/dev-essentials
```

### GitHub Copilot CLI (`copilot`)

```bash
copilot plugin marketplace add armckinney/ai-marketplace
copilot plugin install gyrus@ai-marketplace
copilot plugin install dev-essentials@ai-marketplace
```

### Claude Code CLI (`claude`)

```bash
claude plugin marketplace add armckinney/ai-marketplace
claude plugin install gyrus@ai-marketplace
claude plugin install dev-essentials@ai-marketplace
```

## Authoring & Validation

Scaffold a new multi-harness plugin (automatically registered in all marketplace catalogs):

```bash
make new-plugin NAME=git-workflow DESC="Git branch, commit, and PR workflow helpers"
# Optional flags: WITH_MCP=1 WITH_HOOKS=1 CATEGORY=Productivity
```

Validate all marketplace catalogs, plugin manifests, `SKILL.md` / `agents/*.md` frontmatter, and run `agy plugin validate` when `agy` is installed:

```bash
make validate
```

List registered plugins:

```bash
make list
```

## Documentation

- [Plugin Guide: `gyrus`](docs/plugins/gyrus.md)
- [Plugin Guide: `dev-essentials`](docs/plugins/dev-essentials.md)
- [Harness Compatibility Matrix](docs/harness-compatibility.md)
- [Plugin Authoring & Artifact Scoping Guide](docs/authoring-plugins.md)
