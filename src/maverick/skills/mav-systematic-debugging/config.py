from skills.models import SkillConfig
from skills.names import MAV_SYSTEMATIC_DEBUGGING

CONFIG = SkillConfig(
    name=MAV_SYSTEMATIC_DEBUGGING,
    description=(
        "Use when encountering any bug, test failure, or unexpected behaviour during implementation. Requires root cause investigation before proposing fixes."
    ),
)
