#!/usr/bin/env python3
"""Validate marketplace catalogs, plugin manifests, skills, agents, and Antigravity compliance."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
EXPECTED_MARKETPLACE_NAME = "ai-marketplace"
EXPECTED_LICENSE = "Apache-2.0"
NAME_RE = re.compile(r"^[a-z0-9]([a-z0-9.-]*[a-z0-9])?$")


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str | None]:
    """Extract simple YAML frontmatter key/value pairs without third-party dependencies."""
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    if not text.startswith("---\n"):
        return {}, "missing opening '---' YAML frontmatter delimiter"
    rest = text[4:]
    end_idx = rest.find("\n---\n")
    if end_idx == -1:
        return {}, "missing closing '---' YAML frontmatter delimiter"
    fm_block = rest[:end_idx]

    meta: dict[str, str] = {}
    current_key: str | None = None
    multiline_parts: list[str] = []

    def flush() -> None:
        nonlocal current_key, multiline_parts
        if current_key is not None:
            meta[current_key] = " ".join(part.strip() for part in multiline_parts if part.strip())
        current_key = None
        multiline_parts = []

    for line in fm_block.splitlines():
        if not line.strip():
            continue
        if line[0].isspace():
            if current_key is not None:
                multiline_parts.append(line.strip())
            continue
        flush()
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        key = key.strip()
        val = val.strip()
        if val in (">-", ">", "|", "|-"):
            current_key = key
            multiline_parts = []
        else:
            meta[key] = val.strip('"').strip("'")
    flush()
    return meta, None


def load_json(path: Path, errors: list[str]) -> dict | None:
    """Read and parse JSON, recording an error on failure."""
    if not path.is_file():
        errors.append(f"Missing required file: {path.relative_to(REPO_ROOT)}")
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"Invalid JSON in {path.relative_to(REPO_ROOT)}: {exc}")
        return None


def validate_marketplaces(plugin_dirs: dict[str, Path], errors: list[str]) -> None:
    """Validate marketplace manifests and cross-marketplace consistency."""
    agy_cfg = load_json(REPO_ROOT / ".agents" / "plugins.json", errors)
    if agy_cfg is not None:
        entries = agy_cfg.get("entries", [])
        if not any(e.get("path") == "plugins" for e in entries if isinstance(e, dict)):
            errors.append(".agents/plugins.json must include entry {\"path\": \"plugins\"}")

    codex_mp = load_json(REPO_ROOT / ".agents" / "plugins" / "marketplace.json", errors)
    copilot_mp = load_json(REPO_ROOT / ".github" / "plugin" / "marketplace.json", errors)
    claude_mp = load_json(REPO_ROOT / ".claude-plugin" / "marketplace.json", errors)

    catalogs = [
        ("Codex (.agents/plugins/marketplace.json)", codex_mp, "codex"),
        ("Copilot (.github/plugin/marketplace.json)", copilot_mp, "copilot"),
        ("Claude (.claude-plugin/marketplace.json)", claude_mp, "claude"),
    ]

    for label, data, kind in catalogs:
        if data is None:
            continue
        if data.get("name") != EXPECTED_MARKETPLACE_NAME:
            errors.append(
                f"{label}: expected marketplace name '{EXPECTED_MARKETPLACE_NAME}', got '{data.get('name')}'"
            )

        listed: dict[str, dict] = {}
        for entry in data.get("plugins", []):
            pname = entry.get("name")
            if not pname:
                errors.append(f"{label}: plugin entry missing 'name'")
                continue
            listed[pname] = entry
            src = entry.get("source")
            if kind == "codex":
                if not isinstance(src, dict) or src.get("source") != "local" or not src.get("path"):
                    errors.append(f"{label}: plugin '{pname}' must declare local source object")
                else:
                    target = (REPO_ROOT / src["path"]).resolve()
                    if not target.is_dir():
                        errors.append(f"{label}: source path missing for '{pname}': {src['path']}")
            else:
                if isinstance(src, str):
                    target = (REPO_ROOT / src).resolve()
                    if not target.is_dir():
                        errors.append(f"{label}: source path missing for '{pname}': {src}")
                elif not isinstance(src, dict):
                    errors.append(f"{label}: plugin '{pname}' has invalid source type")

        for pname in plugin_dirs:
            if pname not in listed:
                errors.append(f"{label}: missing local plugin '{pname}'")


def validate_plugins(plugin_dirs: dict[str, Path], errors: list[str], warnings: list[str]) -> None:
    """Validate individual plugin manifests, skills, agents, and JSON files."""
    for name, pdir in sorted(plugin_dirs.items()):
        if not NAME_RE.match(name) or "--" in name or ".." in name:
            errors.append(f"plugins/{name}: invalid plugin directory name")

        if (pdir / "commands").exists():
            warnings.append(f"plugins/{name}/commands exists; prefer skills/ for cross-harness support")

        # Validate all JSON files in the plugin
        for json_file in sorted(pdir.rglob("*.json")):
            load_json(json_file, errors)

        root_manifest = load_json(pdir / "plugin.json", errors)
        claude_manifest = load_json(pdir / ".claude-plugin" / "plugin.json", errors)
        codex_manifest = load_json(pdir / ".codex-plugin" / "plugin.json", errors)

        versions = set()
        for mlabel, manifest in (
            ("plugin.json", root_manifest),
            (".claude-plugin/plugin.json", claude_manifest),
            (".codex-plugin/plugin.json", codex_manifest),
        ):
            if manifest is None:
                continue
            if manifest.get("name") != name:
                errors.append(f"plugins/{name}/{mlabel}: name '{manifest.get('name')}' != '{name}'")
            if manifest.get("license") != EXPECTED_LICENSE:
                errors.append(
                    f"plugins/{name}/{mlabel}: license '{manifest.get('license')}' != '{EXPECTED_LICENSE}'"
                )
            if manifest.get("version"):
                versions.add(manifest["version"])

        if len(versions) > 1:
            errors.append(f"plugins/{name}: version mismatch across manifests: {sorted(versions)}")

        # Validate skills
        skills_dir = pdir / "skills"
        if skills_dir.is_dir():
            for skill_dir in sorted(d for d in skills_dir.iterdir() if d.is_dir()):
                skill_md = skill_dir / "SKILL.md"
                if not skill_md.is_file():
                    errors.append(f"plugins/{name}/skills/{skill_dir.name}: missing SKILL.md")
                    continue
                meta, fm_err = parse_frontmatter(skill_md)
                if fm_err:
                    errors.append(f"{skill_md.relative_to(REPO_ROOT)}: {fm_err}")
                    continue
                if meta.get("name") != skill_dir.name:
                    errors.append(
                        f"{skill_md.relative_to(REPO_ROOT)}: frontmatter name '{meta.get('name')}' != '{skill_dir.name}'"
                    )
                if not meta.get("description"):
                    errors.append(f"{skill_md.relative_to(REPO_ROOT)}: missing frontmatter description")

        # Validate agents (when present)
        agents_dir = pdir / "agents"
        if agents_dir.is_dir():
            for agent_md in sorted(agents_dir.glob("*.md")):
                meta, fm_err = parse_frontmatter(agent_md)
                if fm_err:
                    errors.append(f"{agent_md.relative_to(REPO_ROOT)}: {fm_err}")
                    continue
                if not meta.get("name") or not meta.get("description"):
                    errors.append(
                        f"{agent_md.relative_to(REPO_ROOT)}: frontmatter requires non-empty name and description"
                    )


def validate_with_agy(plugin_dirs: dict[str, Path], errors: list[str], warnings: list[str]) -> None:
    """Run `agy plugin validate --json` if Antigravity CLI is installed."""
    agy_bin = shutil.which("agy")
    if not agy_bin:
        warnings.append("agy CLI not found on PATH; skipping `agy plugin validate`")
        return

    for name, pdir in sorted(plugin_dirs.items()):
        proc = subprocess.run(
            [agy_bin, "plugin", "validate", "--json", str(pdir)],
            capture_output=True,
            text=True,
            check=False,
        )
        try:
            report = json.loads(proc.stdout)
        except json.JSONDecodeError:
            errors.append(
                f"plugins/{name}: failed to parse `agy plugin validate --json` output (exit {proc.returncode}): {proc.stdout or proc.stderr}"
            )
            continue

        for finding in report.get("findings", []):
            sev = finding.get("severity", "")
            msg = finding.get("message", "")
            fpath = finding.get("file", "")
            formatted = f"plugins/{name} ({fpath}): {msg}" if fpath else f"plugins/{name}: {msg}"
            if sev == "error":
                errors.append(f"[agy] {formatted}")
            elif sev == "warning":
                # Allow missing external binary on PATH in validation environments, report as warning
                if "isn't on this machine's PATH" in msg:
                    warnings.append(f"[agy] {formatted}")
                else:
                    errors.append(f"[agy warning] {formatted}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate ai-marketplace catalogs and plugins.")
    parser.add_argument("--skip-agy", action="store_true", help="Skip `agy plugin validate` even if installed")
    args = parser.parse_args()

    plugins_root = REPO_ROOT / "plugins"
    if not plugins_root.is_dir():
        print("Error: plugins/ directory does not exist", file=sys.stderr)
        return 1

    plugin_dirs = {
        d.name: d
        for d in sorted(plugins_root.iterdir())
        if d.is_dir() and not d.name.startswith(".")
    }

    errors: list[str] = []
    warnings: list[str] = []

    validate_marketplaces(plugin_dirs, errors)
    validate_plugins(plugin_dirs, errors, warnings)
    if not args.skip_agy:
        validate_with_agy(plugin_dirs, errors, warnings)

    for w in warnings:
        print(f"WARN: {w}")
    for e in errors:
        print(f"ERROR: {e}", file=sys.stderr)

    if errors:
        print(f"\nValidation failed with {len(errors)} error(s) and {len(warnings)} warning(s).", file=sys.stderr)
        return 1

    print(f"✓ Validated {len(plugin_dirs)} plugin(s) cleanly ({len(warnings)} warning(s)).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
