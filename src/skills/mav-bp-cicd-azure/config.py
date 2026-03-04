from skills.models import SkillConfig
from skills.names import MAV_BP_CICD_AZURE

CONFIG = SkillConfig(
    name=MAV_BP_CICD_AZURE,
    user_invocable=False,
    disable_model_invocation=False,
    depends_on=[],
)
