#!/usr/bin/env bash
set -Eeuo pipefail

SITE_DOMAIN="${SITE_DOMAIN:-www.lcaa.top}"
SITE_ROOT="${SITE_ROOT:-/var/www/lcaa-site}"
UPDATES_ROOT="${UPDATES_ROOT:-/var/www/updates}"
AUTH_UPSTREAM_HOST="${AUTH_UPSTREAM_HOST:-223.254.149.225}"
AUTH_UPSTREAM_PORT="${AUTH_UPSTREAM_PORT:-8000}"
NGINX_SITE_NAME="${NGINX_SITE_NAME:-lcaa-entry}"
NGINX_SITE_PATH="/etc/nginx/sites-available/${NGINX_SITE_NAME}"
NGINX_ENABLED_PATH="/etc/nginx/sites-enabled/${NGINX_SITE_NAME}"

if [[ "${EUID}" -ne 0 ]]; then
  echo "This script must run as root." >&2
  exit 1
fi

export DEBIAN_FRONTEND=noninteractive

apt-get update
apt-get install -y nginx

install -d -m 0755 "${SITE_ROOT}" "${UPDATES_ROOT}"

cat > "${NGINX_SITE_PATH}" <<EOF
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name ${SITE_DOMAIN};

    root ${SITE_ROOT};
    index index.html;

    location = /updates/manifest.json {
        alias ${UPDATES_ROOT}/manifest.json;
        add_header Cache-Control "no-cache, no-store, must-revalidate";
        add_header Pragma "no-cache";
        add_header Expires "0";
        try_files \$uri =404;
    }

    location /updates/ {
        alias ${UPDATES_ROOT}/;
        try_files \$uri =404;
    }

    location / {
        try_files \$uri \$uri/ /index.html;
    }
}

server {
    listen 8000;
    listen [::]:8000;
    server_name ${SITE_DOMAIN};

    client_max_body_size 100m;

    location / {
        proxy_pass http://${AUTH_UPSTREAM_HOST}:${AUTH_UPSTREAM_PORT};
        proxy_http_version 1.1;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
        proxy_read_timeout 120s;
        proxy_connect_timeout 30s;
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
    ufw allow 80/tcp
    ufw allow 8000/tcp
  fi
fi

echo "Entry server deployed."
echo "Site root: ${SITE_ROOT}"
echo "Updates root: ${UPDATES_ROOT}"
echo "Auth upstream: ${AUTH_UPSTREAM_HOST}:${AUTH_UPSTREAM_PORT}"
