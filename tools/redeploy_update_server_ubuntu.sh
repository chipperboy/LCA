#!/usr/bin/env bash
set -Eeuo pipefail

NGINX_SITE_NAME="${NGINX_SITE_NAME:-lca-updates}"
NGINX_SITE_PATH="/etc/nginx/sites-available/${NGINX_SITE_NAME}"
NGINX_ENABLED_PATH="/etc/nginx/sites-enabled/${NGINX_SITE_NAME}"
WEB_ROOT="${WEB_ROOT:-/var/www/updates}"
LISTEN_PORT="${LISTEN_PORT:-3000}"

if [[ "${EUID}" -ne 0 ]]; then
  echo "This script must run as root." >&2
  exit 1
fi

if ! command -v apt-get >/dev/null 2>&1; then
  echo "Unsupported system: apt-get not found." >&2
  exit 1
fi

export DEBIAN_FRONTEND=noninteractive

apt-get update
apt-get install -y nginx

install -d -m 0755 "${WEB_ROOT}"

cat > "${NGINX_SITE_PATH}" <<EOF
server {
    listen ${LISTEN_PORT} default_server;
    listen [::]:${LISTEN_PORT} default_server;
    server_name _;

    root ${WEB_ROOT};

    location = /manifest.json {
        add_header Cache-Control "no-cache, no-store, must-revalidate";
        add_header Pragma "no-cache";
        add_header Expires "0";
        try_files \$uri =404;
    }

    location / {
        try_files \$uri =404;
    }
}
EOF

ln -sfn "${NGINX_SITE_PATH}" "${NGINX_ENABLED_PATH}"
rm -f /etc/nginx/sites-enabled/default

nginx -t
systemctl enable nginx
systemctl restart nginx

if command -v ufw >/dev/null 2>&1; then
  UFW_STATUS="$(ufw status | head -n 1 || true)"
  if [[ "${UFW_STATUS}" == "Status: active" ]]; then
    ufw allow "${LISTEN_PORT}/tcp"
  fi
fi

echo "Update server is ready."
echo "Web root: ${WEB_ROOT}"
echo "Listen port: ${LISTEN_PORT}"
echo "Self-check: curl http://127.0.0.1:${LISTEN_PORT}/manifest.json"
