from skills.models import SkillConfig
from skills.names import MAV_BP_CICD_GITLAB

CONFIG = SkillConfig(
    name=MAV_BP_CICD_GITLAB,
    description=(
        "Monitoring GitLab CI/CD pipelines after pushing. Covers checking pipeline status, diagnosing job failures, and respecting pipeline boundaries. Used as a dependency from workflow skills."
    ),
    user_invocable=False,
    disable_model_invocation=False,
    depends_on=[],
)
