#!/usr/bin/env python3
"""Scaffold a new multi-harness plugin under plugins/<name>/ and register it in all marketplaces."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
NAME_RE = re.compile(r"^[a-z0-9]([a-z0-9-]*[a-z0-9])?$")

DEFAULT_LOGO_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none">
  <rect width="64" height="64" rx="14" fill="#0F172A"/>
  <circle cx="32" cy="32" r="14" stroke="#38BDF8" stroke-width="4"/>
  <circle cx="32" cy="32" r="5" fill="#F8FAFC"/>
</svg>
"""


def validate_name(name: str) -> None:
    """Ensure plugin name conforms to Agent Plugins 1.0.0 naming rules."""
    if not NAME_RE.match(name) or "--" in name or ".." in name:
        raise ValueError(
            f"Invalid plugin name '{name}'. Use lowercase alphanumeric words separated by single hyphens."
        )


def write_json(path: Path, data: dict) -> None:
    """Write formatted JSON with a trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def register_in_marketplaces(name: str, description: str, category: str) -> None:
    """Add plugin entries to Codex, Copilot, and Claude marketplace catalogs."""
    codex_mp = REPO_ROOT / ".agents" / "plugins" / "marketplace.json"
    copilot_mp = REPO_ROOT / ".github" / "plugin" / "marketplace.json"
    claude_mp = REPO_ROOT / ".claude-plugin" / "marketplace.json"

    for mp_path in (codex_mp, copilot_mp, claude_mp):
        data = json.loads(mp_path.read_text(encoding="utf-8"))
        if any(p.get("name") == name for p in data.get("plugins", [])):
            raise ValueError(f"Plugin '{name}' is already registered in {mp_path}")

    # 1. Codex (.agents/plugins/marketplace.json)
    codex_data = json.loads(codex_mp.read_text(encoding="utf-8"))
    codex_data.setdefault("plugins", []).append(
        {
            "name": name,
            "source": {"source": "local", "path": f"./plugins/{name}"},
            "policy": {"installation": "AVAILABLE"},
            "category": category,
        }
    )
    write_json(codex_mp, codex_data)

    # 2. Copilot (.github/plugin/marketplace.json)
    copilot_data = json.loads(copilot_mp.read_text(encoding="utf-8"))
    copilot_data.setdefault("plugins", []).append(
        {
            "name": name,
            "source": f"./plugins/{name}",
            "description": description,
            "version": "0.1.0",
        }
    )
    write_json(copilot_mp, copilot_data)

    # 3. Claude Code (.claude-plugin/marketplace.json)
    claude_data = json.loads(claude_mp.read_text(encoding="utf-8"))
    claude_data.setdefault("plugins", []).append(
        {
            "name": name,
            "description": description,
            "version": "0.1.0",
            "author": {"name": "Andrew McKinney"},
            "category": category.lower(),
            "source": f"./plugins/{name}",
            "repository": "https://github.com/armckinney/ai-marketplace",
            "license": "Apache-2.0",
        }
    )
    write_json(claude_mp, claude_data)


def scaffold_plugin(
    name: str,
    description: str,
    category: str,
    with_mcp: bool,
    with_hooks: bool,
) -> Path:
    """Create plugin directory structure and manifests across all target harnesses."""
    plugin_dir = REPO_ROOT / "plugins" / name
    if plugin_dir.exists():
        raise FileExistsError(f"Plugin directory already exists: {plugin_dir}")

    display_name = " ".join(part.capitalize() for part in name.split("-"))

    # Root Agent Plugins 1.0.0 + Antigravity manifest
    write_json(
        plugin_dir / "plugin.json",
        {
            "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
            "name": name,
            "version": "0.1.0",
            "description": description,
            "author": {
                "name": "Andrew McKinney",
                "url": "https://github.com/armckinney",
            },
            "repository": "https://github.com/armckinney/ai-marketplace",
            "license": "Apache-2.0",
            "logo": "assets/logo.svg",
            "keywords": [name],
        },
    )

    # Claude Code manifest
    claude_manifest: dict = {
        "name": name,
        "version": "0.1.0",
        "description": description,
        "author": {
            "name": "Andrew McKinney",
            "url": "https://github.com/armckinney",
        },
        "repository": "https://github.com/armckinney/ai-marketplace",
        "license": "Apache-2.0",
        "skills": "./skills/",
        "agents": [f"./agents/{name}-reviewer.md"],
        "keywords": [name],
    }
    if with_hooks:
        claude_manifest["hooks"] = "./hooks.json"
    write_json(plugin_dir / ".claude-plugin" / "plugin.json", claude_manifest)

    # Codex manifest
    codex_manifest: dict = {
        "name": name,
        "version": "0.1.0",
        "description": description,
        "author": {"name": "Andrew McKinney"},
        "repository": "https://github.com/armckinney/ai-marketplace",
        "license": "Apache-2.0",
        "skills": "./skills/",
        "interface": {
            "displayName": display_name,
            "shortDescription": description,
            "developerName": "Andrew McKinney",
            "category": category,
            "logo": "./assets/logo.svg",
        },
    }
    if with_mcp:
        codex_manifest["mcpServers"] = "./.mcp.json"
    write_json(plugin_dir / ".codex-plugin" / "plugin.json", codex_manifest)

    # Assets
    assets_dir = plugin_dir / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)
    (assets_dir / "logo.svg").write_text(DEFAULT_LOGO_SVG, encoding="utf-8")

    # Rules
    rules_dir = plugin_dir / "rules"
    rules_dir.mkdir(parents=True, exist_ok=True)
    (rules_dir / "AGENTS.md").write_text(
        f"# {display_name} Rules\n\nDefine always-on rules and guardrails for `{name}` here.\n",
        encoding="utf-8",
    )

    # Subagents (scaffolded for devs to implement)
    agents_dir = plugin_dir / "agents"
    agents_dir.mkdir(parents=True, exist_ok=True)
    (agents_dir / f"{name}-reviewer.md").write_text(
        f"""---
name: {name}-reviewer
description: Specialized subagent for {name} tasks and reviews.
license: Apache-2.0
---

# {display_name} Reviewer

Define the persona, scope, and output rubric for this subagent.
""",
        encoding="utf-8",
    )

    # Starter skill (skills-first, no commands/)
    skill_dir = plugin_dir / "skills" / name
    skill_dir.mkdir(parents=True, exist_ok=True)
    (skill_dir / "SKILL.md").write_text(
        f"""---
name: {name}
description: >-
  Guides {name} workflows. Replace this description with specific triggers
  explaining when the agent should activate this skill.
---

# {display_name}

## Procedure

1. Describe the first step here.
2. Describe verification steps here.
""",
        encoding="utf-8",
    )

    if with_mcp:
        write_json(
            plugin_dir / "mcp.json",
            {
                "$schema": "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json",
                "mcpServers": {},
            },
        )
        write_json(plugin_dir / ".mcp.json", {"mcpServers": {}})
        write_json(plugin_dir / "mcp_config.json", {"mcpServers": {}})

    if with_hooks:
        write_json(
            plugin_dir / "hooks.json",
            {
                f"{name}-hook": {
                    "enabled": False,
                    "PostToolUse": [
                        {
                            "matcher": "write_file|edit_file",
                            "hooks": [
                                {
                                    "type": "command",
                                    "command": "echo 'Replace with hook command'",
                                    "timeout": 10,
                                }
                            ],
                        }
                    ],
                }
            },
        )

    register_in_marketplaces(name, description, category)
    return plugin_dir


def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold a new multi-harness plugin.")
    parser.add_argument("--name", required=True, help="Kebab-case plugin name (e.g., git-workflow)")
    parser.add_argument("--description", default="", help="Short plugin description")
    parser.add_argument("--category", default="Productivity", help="Marketplace category")
    parser.add_argument("--with-mcp", action="store_true", help="Include MCP config templates")
    parser.add_argument("--with-hooks", action="store_true", help="Include disabled hook templates")
    args = parser.parse_args()

    try:
        validate_name(args.name)
        description = args.description.strip() or f"{args.name} plugin"
        plugin_dir = scaffold_plugin(
            name=args.name,
            description=description,
            category=args.category,
            with_mcp=args.with_mcp,
            with_hooks=args.with_hooks,
        )
    except (ValueError, FileExistsError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(f"Created plugin at {plugin_dir.relative_to(REPO_ROOT)}")
    print("Registered in .agents/plugins/marketplace.json, .github/plugin/marketplace.json, and .claude-plugin/marketplace.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
