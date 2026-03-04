.PHONY: generate-skills generate-topics build

generate-skills: ## Render all SKILL.md files from templates
	rm -rf skills/*/SKILL.md
	cd src && python -m skills.registry

generate-topics: ## Generate skills/upskill/topics.json from upskill config
	cd src && python -m skills.generate_topics

build: generate-skills generate-topics
