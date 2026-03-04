from __future__ import annotations

import sys
from pathlib import Path

from generator import SkillTemplateRenderer  # type: ignore
from names import (  # type: ignore
    CREATE_IMPLEMENTATION_PLAN,
    CREATE_SOLUTION_DESIGN,
    DO_ISSUE_SOLO,
    MAV_BP_ALERTING,
    MAV_BP_CICD,
    MAV_BP_LOGGING,
    MAV_CLAUDE_CODE_RECOVERY,
    MAV_GIT_WORKFLOW,
    MAV_GITHUB_ISSUE_WORKFLOW,
    MAV_LOCAL_VERIFICATION,
    MAV_PLAN_EXECUTION,
    MAV_SCOPE_BOUNDARIES,
    MAV_SYSTEMATIC_DEBUGGING,
    PULLREQUEST_REVIEW,
)

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
if str(PARENT) not in sys.path:
    sys.path.append(str(PARENT))


SKILL_NAME = DO_ISSUE_SOLO

DEPENDS_ON = [
    MAV_SCOPE_BOUNDARIES,
    MAV_GIT_WORKFLOW,
    MAV_GITHUB_ISSUE_WORKFLOW,
    CREATE_SOLUTION_DESIGN,
    CREATE_IMPLEMENTATION_PLAN,
    MAV_PLAN_EXECUTION,
    MAV_LOCAL_VERIFICATION,
    MAV_BP_CICD,
    MAV_CLAUDE_CODE_RECOVERY,
    MAV_BP_LOGGING,
    MAV_BP_ALERTING,
    MAV_SYSTEMATIC_DEBUGGING,
    PULLREQUEST_REVIEW,
]


def main() -> None:
    renderer = SkillTemplateRenderer(HERE)
    depends_on_str = ", ".join(DEPENDS_ON)
    context = {
        "SKILL_NAME": SKILL_NAME,
        "DEPENDS_ON": depends_on_str,
    }
    renderer.render(
        template_name="SKILL.md.template", output_name="SKILL.md", context=context
    )


if __name__ == "__main__":
    main()
