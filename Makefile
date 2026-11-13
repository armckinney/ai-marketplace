.PHONY: help new-plugin validate list

NAME ?=
DESC ?=
CATEGORY ?= Productivity
WITH_MCP ?= 0
WITH_HOOKS ?= 0

help:
	@echo "ai-marketplace targets:"
	@echo "  make validate                                Validate catalogs, manifests, skills, agents, and agy compliance"
	@echo "  make list                                    List plugins registered across marketplaces"
	@echo "  make new-plugin NAME=<name> [DESC=...]       Scaffold a new multi-harness plugin under plugins/<name>/"
	@echo "    Optional flags: CATEGORY=Productivity WITH_MCP=1 WITH_HOOKS=1"

new-plugin:
	@if [ -z "$(NAME)" ]; then \
		echo "Error: NAME is required. Usage: make new-plugin NAME=my-plugin [DESC='...']"; \
		exit 1; \
	fi
	@python3 scripts/new-plugin.py \
		--name "$(NAME)" \
		--description "$(DESC)" \
		--category "$(CATEGORY)" \
		$(if $(filter 1 true yes,$(WITH_MCP)),--with-mcp,) \
		$(if $(filter 1 true yes,$(WITH_HOOKS)),--with-hooks,)

validate:
	@python3 scripts/validate.py

list:
	@python3 -c 'import json, pathlib; mp=json.loads(pathlib.Path(".github/plugin/marketplace.json").read_text()); [print("- {} ({}): {}".format(p["name"], p.get("version", "?"), p.get("description", ""))) for p in mp.get("plugins", [])]'
