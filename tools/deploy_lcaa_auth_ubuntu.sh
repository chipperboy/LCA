#!/usr/bin/env bash
set -Eeuo pipefail

APP_DIR="${APP_DIR:-/opt/lcaa-auth}"
VENV_DIR="${VENV_DIR:-${APP_DIR}/venv}"
ENV_FILE="${ENV_FILE:-/etc/lcaa-auth.env}"
SERVICE_NAME="${SERVICE_NAME:-lcaa-auth}"
RUN_USER="${RUN_USER:-root}"
LISTEN_HOST="${LISTEN_HOST:-0.0.0.0}"
LISTEN_PORT="${LISTEN_PORT:-8000}"

if [[ "${EUID}" -ne 0 ]]; then
  echo "This script must run as root." >&2
  exit 1
fi

export DEBIAN_FRONTEND=noninteractive

apt-get update
apt-get install -y python3 python3-venv python3-pip

install -d -m 0755 "${APP_DIR}"
install -d -m 0755 "${APP_DIR}/static" "${APP_DIR}/templates" "${APP_DIR}/config" "${APP_DIR}/logs"

if [[ ! -d "${VENV_DIR}" ]]; then
  python3 -m venv "${VENV_DIR}"
fi

"${VENV_DIR}/bin/python" -m pip install --upgrade pip setuptools wheel
"${VENV_DIR}/bin/pip" install -r "${APP_DIR}/requirements.txt"

cat > "/etc/systemd/system/${SERVICE_NAME}.service" <<EOF
[Unit]
Description=LCAA Authorization Service
After=network.target

[Service]
Type=simple
User=${RUN_USER}
WorkingDirectory=${APP_DIR}
EnvironmentFile=-${ENV_FILE}
Environment=PYTHONPATH=${APP_DIR}
ExecStart=${VENV_DIR}/bin/python ${APP_DIR}/start_server.py --host ${LISTEN_HOST} --port ${LISTEN_PORT} --no-ssl --log-level info
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable "${SERVICE_NAME}"
systemctl restart "${SERVICE_NAME}"

echo "Authorization service deployed."
echo "Service: ${SERVICE_NAME}"
echo "App dir: ${APP_DIR}"
echo "Env file: ${ENV_FILE}"
