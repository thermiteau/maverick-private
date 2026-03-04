from skills.models import SkillConfig
from skills.names import MAVERICK_ALIGNMENT

CONFIG = SkillConfig(
    name=MAVERICK_ALIGNMENT,
    description=(
        "Analyze a project's codebase against Maverick standard practices and write a findings report. Checks linting, unit tests, integration tests, documentation, and CI/CD. Run when onboarding an existing project or on demand."
    ),
    user_invocable=True,
    disable_model_invocation=False,
)
