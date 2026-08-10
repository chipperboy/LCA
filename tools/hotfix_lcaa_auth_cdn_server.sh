#!/usr/bin/env bash
set -Eeuo pipefail

AUTH_DOMAIN="${AUTH_DOMAIN:-lcaa.top}"
AUTH_BACKEND_HOST="${AUTH_BACKEND_HOST:-127.0.0.1}"
AUTH_BACKEND_PORT="${AUTH_BACKEND_PORT:-18000}"
SSL_DIR="${SSL_DIR:-/etc/nginx/ssl/lcaa.top}"
NGINX_CONF="${NGINX_CONF:-/etc/nginx/conf.d/lcaa-auth-cdn.conf}"
AUTH_SERVICE_NAME="${AUTH_SERVICE_NAME:-lcaa-auth}"

if [[ "${EUID}" -ne 0 ]]; then
  echo "This script must run as root." >&2
  exit 1
fi

cat > "${NGINX_CONF}" <<EOF
server {
    listen 443 ssl;
    listen [::]:443 ssl;
    server_name ${AUTH_DOMAIN};

    server_tokens off;

    ssl_certificate ${SSL_DIR}/lcaa.top.pem;
    ssl_certificate_key ${SSL_DIR}/lcaa.top.key;

    client_max_body_size 100m;

    location / {
        proxy_pass http://${AUTH_BACKEND_HOST}:${AUTH_BACKEND_PORT};
        proxy_http_version 1.1;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto https;
        proxy_set_header X-Forwarded-Host \$host;
        proxy_set_header X-Forwarded-Port 443;
        proxy_no_cache 1;
        proxy_cache_bypass 1;
        add_header Cache-Control "no-store, no-cache, must-revalidate, max-age=0, s-maxage=0" always;
        proxy_connect_timeout 30s;
        proxy_read_timeout 120s;
    }
}
EOF

nginx -t
systemctl reload nginx
systemctl restart "${AUTH_SERVICE_NAME}" || systemctl restart jw3-auth-server

echo "Checking auth API..."
curl -k -i "https://${AUTH_DOMAIN}/api/get_csrf_for_client" | head -n 20
