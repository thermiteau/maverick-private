from skills.models import SkillConfig
from skills.names import MAV_CLAUDE_CODE_RECOVERY

CONFIG = SkillConfig(
    name=MAV_CLAUDE_CODE_RECOVERY,
    user_invocable=False,
    disable_model_invocation=False,
    depends_on=[],
)
