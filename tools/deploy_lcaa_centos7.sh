#!/usr/bin/env bash
set -Eeuo pipefail

SITE_PUBLIC_IP="${SITE_PUBLIC_IP:-103.115.41.200}"
AUTH_PUBLIC_IP="${AUTH_PUBLIC_IP:-223.254.149.225}"
SITE_DOMAIN="${SITE_DOMAIN:-www.lcaa.top}"
AUTH_DOMAIN="${AUTH_DOMAIN:-lcaa.top}"
SITE_ROOT="${SITE_ROOT:-/var/www/lcaa-site}"
UPDATES_ROOT="${UPDATES_ROOT:-/var/www/updates}"
AUTH_APP_DIR="${AUTH_APP_DIR:-/opt/lcaa-auth}"
AUTH_ENV_FILE="${AUTH_ENV_FILE:-/etc/lcaa-auth.env}"
AUTH_SERVICE_NAME="${AUTH_SERVICE_NAME:-lcaa-auth}"
AUTH_BACKEND_HOST="${AUTH_BACKEND_HOST:-127.0.0.1}"
AUTH_BACKEND_PORT="${AUTH_BACKEND_PORT:-18000}"
CONDA_ROOT="${CONDA_ROOT:-/opt/miniconda3}"
CONDA_ENV_PATH="${CONDA_ENV_PATH:-${AUTH_APP_DIR}/pyenv}"
SSL_DIR="${SSL_DIR:-/etc/nginx/ssl/lcaa.top}"

if [[ "${EUID}" -ne 0 ]]; then
  echo "This script must run as root." >&2
  exit 1
fi

ensure_conda() {
  if [[ -x "${CONDA_ROOT}/bin/conda" ]]; then
    return 0
  fi

  local installer="/tmp/Miniconda3-py310_23.3.1-0-Linux-x86_64.sh"
  curl -L "https://repo.anaconda.com/miniconda/Miniconda3-py310_23.3.1-0-Linux-x86_64.sh" -o "${installer}"
  bash "${installer}" -b -p "${CONDA_ROOT}"
}

ensure_python_env() {
  if [[ ! -x "${CONDA_ENV_PATH}/bin/python" ]]; then
    "${CONDA_ROOT}/bin/conda" create -y -p "${CONDA_ENV_PATH}" python=3.10 pip
  fi
  "${CONDA_ENV_PATH}/bin/python" -m pip install --upgrade pip setuptools wheel
  "${CONDA_ENV_PATH}/bin/pip" install -r "${AUTH_APP_DIR}/requirements.txt"
}

install_system_packages() {
  if [[ -f /etc/yum.repos.d/CentOS-Base.repo ]] && ! grep -q 'vault.centos.org/7.9.2009' /etc/yum.repos.d/CentOS-Base.repo; then
    cp -f /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak.$(date +%Y%m%d%H%M%S)
    cat > /etc/yum.repos.d/CentOS-Base.repo <<'EOF'
[base]
name=CentOS-7.9.2009 - Base
baseurl=https://vault.centos.org/7.9.2009/os/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

[updates]
name=CentOS-7.9.2009 - Updates
baseurl=https://vault.centos.org/7.9.2009/updates/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

[extras]
name=CentOS-7.9.2009 - Extras
baseurl=https://vault.centos.org/7.9.2009/extras/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

[centosplus]
name=CentOS-7.9.2009 - Plus
baseurl=https://vault.centos.org/7.9.2009/centosplus/$basearch/
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
EOF
  fi

  yum clean all
  yum install -y epel-release
  yum install -y nginx curl
}

write_systemd_service() {
  cat > "/etc/systemd/system/${AUTH_SERVICE_NAME}.service" <<EOF
[Unit]
Description=LCAA Authorization Service
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=${AUTH_APP_DIR}
EnvironmentFile=-${AUTH_ENV_FILE}
Environment=PYTHONPATH=${AUTH_APP_DIR}
ExecStart=${CONDA_ENV_PATH}/bin/python ${AUTH_APP_DIR}/start_server.py --host ${AUTH_BACKEND_HOST} --port ${AUTH_BACKEND_PORT} --no-ssl --log-level info
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF
}

write_nginx_conf() {
  mkdir -p "${SSL_DIR}"

  if [[ -f /etc/nginx/nginx.conf ]]; then
    "${CONDA_ENV_PATH}/bin/python" - <<'PY'
from pathlib import Path

path = Path('/etc/nginx/nginx.conf')
text = path.read_text(encoding='utf-8')
old_block = """    server {
        listen       80;
        listen       [::]:80;
        server_name  _;
        root         /usr/share/nginx/html;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        error_page 404 /404.html;
        location = /404.html {
        }

        error_page 500 502 503 504 /50x.html;
        location = /50x.html {
        }
    }

"""
loopback_block = """    server {
        listen       127.0.0.1:80;
        listen       [::1]:80;
        server_name  _;
        root         /usr/share/nginx/html;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        error_page 404 /404.html;
        location = /404.html {
        }

        error_page 500 502 503 504 /50x.html;
        location = /50x.html {
        }
    }

"""
if old_block in text:
    text = text.replace(old_block, '')
if loopback_block in text:
    text = text.replace(loopback_block, '')
path.write_text(text, encoding='utf-8')
PY
  fi

  cat > /etc/nginx/conf.d/lcaa.conf <<EOF
server {
    listen ${SITE_PUBLIC_IP}:80;
    server_name ${SITE_DOMAIN};
    return 301 https://${SITE_DOMAIN}\$request_uri;
}

server {
    listen ${SITE_PUBLIC_IP}:443 ssl;
    server_name ${SITE_DOMAIN};

    server_tokens off;

    ssl_certificate ${SSL_DIR}/lcaa.top.pem;
    ssl_certificate_key ${SSL_DIR}/lcaa.top.key;

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
    listen ${AUTH_PUBLIC_IP}:8000 ssl;
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
        proxy_connect_timeout 30s;
        proxy_read_timeout 120s;
    }
}
EOF
}

install -d -m 0755 "${SITE_ROOT}" "${UPDATES_ROOT}" "${AUTH_APP_DIR}" "${AUTH_APP_DIR}/config" "${AUTH_APP_DIR}/logs" "${SSL_DIR}"

install_system_packages
ensure_conda
ensure_python_env
write_systemd_service
write_nginx_conf

nginx -t
systemctl daemon-reload
systemctl enable nginx
systemctl enable "${AUTH_SERVICE_NAME}"
systemctl restart "${AUTH_SERVICE_NAME}"
systemctl restart nginx

echo "LCAA single-host deployment prepared."
echo "Site IP: ${SITE_PUBLIC_IP}"
echo "Auth IP: ${AUTH_PUBLIC_IP}"
echo "Site domain: ${SITE_DOMAIN}"
echo "Auth domain: ${AUTH_DOMAIN}"
echo "Auth backend: ${AUTH_BACKEND_HOST}:${AUTH_BACKEND_PORT}"
