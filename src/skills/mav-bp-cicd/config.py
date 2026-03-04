from skills.models import SkillConfig
from skills.names import MAV_BP_CICD

CONFIG = SkillConfig(
    name=MAV_BP_CICD,
    user_invocable=False,
    disable_model_invocation=False,
    depends_on=[],
)
