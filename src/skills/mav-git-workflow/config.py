from skills.models import SkillConfig
from skills.names import MAV_GIT_WORKFLOW

CONFIG = SkillConfig(
    name=MAV_GIT_WORKFLOW,
    user_invocable=False,
    disable_model_invocation=False,
    depends_on=[],
)
