from skills.models import SkillConfig
from skills.names import MAV_LOCAL_VERIFICATION

CONFIG = SkillConfig(
    name=MAV_LOCAL_VERIFICATION,
    user_invocable=False,
    disable_model_invocation=False,
    depends_on=[],
)
