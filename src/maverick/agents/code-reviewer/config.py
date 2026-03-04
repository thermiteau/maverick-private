from maverick.models import AgentConfig
from maverick.names import MAV_BP_ALERTING, MAV_BP_LOGGING, MAV_SCOPE_BOUNDARIES

CONFIG = AgentConfig(
    name="code-reviewer",
    description=(
        "Autonomous code reviewer that performs two-stage review — spec compliance"
        " first, then code quality. Dispatched after completing implementation steps"
        " or before creating PRs."
    ),
    color="yellow",
    skills=[
        MAV_BP_LOGGING,
        MAV_BP_ALERTING,
        MAV_SCOPE_BOUNDARIES,
    ],
)
