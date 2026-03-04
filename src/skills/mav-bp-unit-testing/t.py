from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
if str(PARENT) not in sys.path:
    sys.path.append(str(PARENT))

from generator import SkillTemplateRenderer  # type: ignore
from names import MAV_BP_UNIT_TESTING  # type: ignore

SKILL_NAME = MAV_BP_UNIT_TESTING


def main() -> None:
    renderer = SkillTemplateRenderer(HERE)
    context = {"SKILL_NAME": SKILL_NAME}
    renderer.render(template_name="SKILL.md.template", output_name="SKILL.md", context=context)


if __name__ == "__main__":
    main()
