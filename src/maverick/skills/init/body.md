
# Init Maverick Project

Set up the current repository for Maverick by creating the project-level config directory and settings file.

## Dispatch

Dispatch the **maverick** agent with task `init` and any user-provided arguments. The agent will follow the process below and return a structured result.

## Process

1. Create the `.maverick/` directory in the project root (the git repository root)
2. Write `.maverick/settings.json` containing `{}` (empty object — project-specific overrides go here)
