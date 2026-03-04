from skills.models import SkillConfig
from skills.names import MAV_SCOPE_BOUNDARIES

CONFIG = SkillConfig(
    name=MAV_SCOPE_BOUNDARIES,
    description=(
        "Defines what Claude Code must refuse to do without explicit authorisation. Covers infrastructure, auth, destructive git, and production systems. Applied automatically to all workflows."
    ),
    user_invocable=False,
    disable_model_invocation=False,
    depends_on=[],
)
