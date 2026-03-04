from skills.models import SkillConfig
from skills.names import TECH_DOCS

CONFIG = SkillConfig(
    name=TECH_DOCS,
    user_invocable=True,
    disable_model_invocation=False,
    depends_on=[],
)
