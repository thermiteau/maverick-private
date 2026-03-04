from skills.models import SkillConfig
from skills.names import MAV_GITHUB_ISSUE_WORKFLOW

CONFIG = SkillConfig(
    name=MAV_GITHUB_ISSUE_WORKFLOW,
    user_invocable=False,
    disable_model_invocation=False,
    depends_on=[],
)
