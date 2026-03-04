from __future__ import annotations

from pathlib import Path
from string import Template
from typing import Mapping, Any


class SkillTemplateRenderer:
    """Render a skill template file into a SKILL.md."""

    def __init__(self, skill_dir: Path) -> None:
        # Directory containing the template + SKILL.md for a single skill
        self.skill_dir = Path(skill_dir)

    def render(
        self,
        template_name: str = "SKILL.template",
        output_name: str = "SKILL.md",
        context: Mapping[str, Any] | None = None,
    ) -> Path:
        """Render a template in this directory with the given context."""
        template_path = self.skill_dir / template_name
        output_path = self.skill_dir / output_name

        template_text = template_path.read_text()
        tmpl = Template(template_text)

        data = dict(context or {})
        rendered = tmpl.safe_substitute(**data)

        output_path.write_text(rendered)
        return output_path

