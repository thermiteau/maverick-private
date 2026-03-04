from skills.models import SkillConfig
from skills.names import MAV_GIT_WORKFLOW

CONFIG = SkillConfig(
    name=MAV_GIT_WORKFLOW,
    description=(
        "Git branching strategy, commit conventions, merge conflict handling, and branch lifecycle. Implements a simplified Gitflow with protected branches and conventional commits."
    ),
    user_invocable=False,
    disable_model_invocation=False,
    depends_on=[],
)
