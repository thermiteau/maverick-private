"""Skill template registry — discovers skill configs and renders templates."""

from __future__ import annotations

import importlib.util
from pathlib import Path

from skills.generator import SkillGenerator
from skills.models import GlobalConfig, SkillConfig

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
TEMPLATES_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = PROJECT_ROOT / "skills"

GLOBAL_CONFIG = GlobalConfig()


def _load_skill_config(config_path: Path) -> SkillConfig:
    """Dynamically load a SkillConfig from a config.py file."""
    spec = importlib.util.spec_from_file_location("_skill_config", config_path)
    module = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    spec.loader.exec_module(module)  # type: ignore[union-attr]
    return module.CONFIG


def discover_skills(templates_dir: Path = TEMPLATES_DIR) -> list[SkillConfig]:
    """Find all skill directories that contain a config.py and load them."""
    configs: list[SkillConfig] = []
    for config_path in sorted(templates_dir.glob("*/config.py")):
        configs.append(_load_skill_config(config_path))
    return configs


def render_skill(
    skill: SkillConfig,
    global_config: GlobalConfig = GLOBAL_CONFIG,
    templates_dir: Path = TEMPLATES_DIR,
    output_dir: Path = OUTPUT_DIR,
) -> Path:
    """Render a single skill template into its SKILL.md."""
    generator = SkillGenerator(templates_dir / skill.name)
    context: dict[str, str] = {
        **global_config.extra_context,
        "SKILL_NAME": skill.name,
        "USER_INVOCABLE": skill.user_invocable,
        "DISABLE_MODEL_INVOCATION": skill.disable_model_invocation,
    }
    if skill.depends_on:
        context["DEPENDS_ON"] = ", ".join(skill.depends_on)
    return generator.render(
        template_name="SKILL.md.template",
        output_name="SKILL.md",
        output_dir=output_dir / skill.name,
        context=context,
    )


def render_all(
    global_config: GlobalConfig = GLOBAL_CONFIG,
    templates_dir: Path = TEMPLATES_DIR,
    output_dir: Path = OUTPUT_DIR,
) -> list[Path]:
    """Discover all skill configs and render their templates."""
    skills = discover_skills(templates_dir)
    return [render_skill(s, global_config, templates_dir, output_dir) for s in skills]


def main() -> None:
    for output in render_all():
        print(f"Generated {output}")


if __name__ == "__main__":
    main()
