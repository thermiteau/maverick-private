from __future__ import annotations

from pathlib import Path
from string import Template
from typing import Any, Mapping


class SkillGenerator:
    """Render a skill template file into a SKILL.md."""

    def __init__(self, skill_dir: Path) -> None:
        # Directory containing the template + SKILL.md for a single skill
        self.skill_dir = Path(skill_dir)

    def render(
        self,
        template_name: str = "SKILL.template",
        output_name: str = "SKILL.md",
        output_dir: Path | None = None,
        context: Mapping[str, Any] | None = None,
    ) -> Path:
        """Render a template in this directory with the given context.

        Args:
            output_dir: Directory to write the rendered file to.
                        Defaults to the same directory as the template.
        """
        template_path = self.skill_dir / template_name
        target_dir = Path(output_dir) if output_dir else self.skill_dir
        target_dir.mkdir(parents=True, exist_ok=True)
        output_path = target_dir / output_name

        template_text = template_path.read_text()
        tmpl = Template(template_text)

        data = dict(context or {})
        rendered = tmpl.safe_substitute(**data)

        output_path.write_text(rendered)
        return output_path
