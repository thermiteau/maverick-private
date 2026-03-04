from skills.models import SkillConfig
from skills.names import MAV_BP_UNIT_TESTING

CONFIG = SkillConfig(
    name=MAV_BP_UNIT_TESTING,
    user_invocable=False,
    disable_model_invocation=False,
    depends_on=[],
)
