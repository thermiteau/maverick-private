from maverick.models import AgentConfig
from maverick.names import INIT, INSTALL

CONFIG = AgentConfig(
    name="maverick",
    description=(
        "Handles Maverick plugin and CLI management — installation, project"
        " initialisation, and configuration. Dispatched so that CLI internals don't"
        " consume the caller's context."
    ),
    color="magenta",
    skills=[
        INIT,
        INSTALL,
    ],
)
