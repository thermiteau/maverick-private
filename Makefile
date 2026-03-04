.PHONY: generate-skills

generate-skills: ## Render all SKILL.md files from templates
	cd src && python -m skills.registry
