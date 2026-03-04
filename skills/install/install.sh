#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLUGIN_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

# --- 1. Check uv is available ---

if ! command -v uv &>/dev/null; then
  echo "Error: uv is required but not installed." >&2
  echo "Install it with:  curl -LsSf https://astral.sh/uv/install.sh | sh" >&2
  exit 1
fi

# --- 2. Check pyproject.toml exists ---

if [[ ! -f "$PLUGIN_ROOT/pyproject.toml" ]]; then
  echo "Error: pyproject.toml not found at $PLUGIN_ROOT" >&2
  echo "This script must be run from a complete maverick plugin directory." >&2
  exit 1
fi

# --- 3. Install the CLI ---

echo "Installing maverick CLI from $PLUGIN_ROOT ..."
uv tool install --force "$PLUGIN_ROOT"

# --- 4. Verify maverick is on PATH ---

if command -v maverick &>/dev/null; then
  echo "maverick installed successfully: $(command -v maverick)"
else
  echo ""
  echo "Warning: maverick was installed but is not on your PATH." >&2
  echo "Add ~/.local/bin to your PATH:" >&2
  echo '  export PATH="$HOME/.local/bin:$PATH"' >&2
  echo ""
  echo "Then restart your shell or run the export command above." >&2
fi

# --- 5. Update ~/.claude/settings.json permissions ---

SETTINGS_FILE="$HOME/.claude/settings.json"
PERM_ENTRY="Read(~/.claude/plugins/cache/thermite/maverick/**)"

update_permissions() {
  python3 -c "
import json, sys
from pathlib import Path

settings_path = Path('$SETTINGS_FILE')

if settings_path.exists():
    settings = json.loads(settings_path.read_text())
else:
    settings_path.parent.mkdir(parents=True, exist_ok=True)
    settings = {}

permissions = settings.setdefault('permissions', {})
allow = list(permissions.get('allow', []))

entry = '$PERM_ENTRY'
if entry not in allow:
    allow.append(entry)
    permissions['allow'] = allow
    permissions.setdefault('deny', [])
    settings['permissions'] = permissions
    settings_path.write_text(json.dumps(settings, indent=2) + '\n')
    print('Updated ' + str(settings_path) + ' with read permission for plugin cache.')
else:
    print('Permission already present in ' + str(settings_path) + '.')
"
}

update_permissions

# --- 6. Create default system config ---

MAVERICK_DIR="$HOME/.maverick"
MAVERICK_CONFIG="$MAVERICK_DIR/settings.json"

if [[ -f "$MAVERICK_CONFIG" ]]; then
  echo "System config already exists at $MAVERICK_CONFIG."
else
  mkdir -p "$MAVERICK_DIR"
  cat > "$MAVERICK_CONFIG" <<'CONFIGEOF'
{
  "aws": {
    "ec2_description": "Maverick pre-configured instance",
    "ec2_iam_profile": "",
    "ec2_instance_type": "t3.medium",
    "ec2_key_pair": "",
    "ec2_security_group": "",
    "ec2_ssm_parameter": "/aws/service/canonical/ubuntu/server/24.04/stable/current/amd64/hvm/ebs-gp3/ami-id",
    "ec2_subnet": "",
    "parameter_store_arn": "",
    "region": "us-east-1",
    "sqs_max_receive_count": 3,
    "sqs_message_retention": 345600,
    "sqs_queue_url": "",
    "sqs_visibility_timeout": 3600
  },
  "gcp": {},
  "worker": {
    "webhook_label": "maverik-solo",
    "cloudwatch_log_group": "/maverick/worker",
    "prompt_template": "Complete GitHub issue #{issue_number} using the maverick-solo skill",
    "work_dir": "/tmp/maverick-work",
    "user": "maverick"
  }
}
CONFIGEOF
  echo "Created default system config at $MAVERICK_CONFIG."
  echo "Edit it with your AWS/GCP values as needed."
fi

echo ""
echo "Done."
