from skills.models import SkillConfig
from skills.names import MAV_SCOPE_BOUNDARIES

CONFIG = SkillConfig(
    name=MAV_SCOPE_BOUNDARIES,
    user_invocable=False,
    disable_model_invocation=False,
    depends_on=[],
)
