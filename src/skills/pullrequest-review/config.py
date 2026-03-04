from skills.models import SkillConfig
from skills.names import PULLREQUEST_REVIEW

CONFIG = SkillConfig(
    name=PULLREQUEST_REVIEW,
    user_invocable=False,
    disable_model_invocation=False,
    depends_on=[],
)
