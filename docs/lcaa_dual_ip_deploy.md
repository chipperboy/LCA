# LCAA 双 IP 迁移部署说明

当前目标：

- 官网入口 IP：`103.115.41.200`
- 授权服务 IP：`223.254.149.225`
- 对外域名：`www.lcaa.top`

对外分配：

- `http://www.lcaa.top/`：官网首页
- `http://www.lcaa.top/updates/manifest.json`：更新清单
- `http://www.lcaa.top/updates/LCA_Setup_v<version>.exe`：安装包
- `http://www.lcaa.top:8000/`：授权入口，实际由入口机反代到授权机

证书说明：

- 当前先不处理证书
- 新证书到位后，仅需在入口机给 `443` 和 `8000 ssl` 挂证书
- 授权机继续跑纯 HTTP，TLS 在入口机终止

授权迁移要点：

- 旧授权机真实数据库路径是 `/opt/jw3server/jw3_auth.db*`
- 旧授权机 `SECRET_KEY` 需要原样迁移
- 新版授权服务必须补 `ADMIN_PASSWORD`
- 通信密钥文件使用 `config/build_auth_secret.b64x2`

入口机部署：

1. 上传 `tools/deploy_lcaa_entry_ubuntu.sh`
2. 执行脚本
3. 上传首页文件到 `/var/www/lcaa-site/index.html`
4. 上传 `manifest.json`
5. 将本地安装包上传并命名为 `LCA_Setup_v<version>.exe`

授权机部署：

1. 上传 `jw3-auth-server-ubuntu-deploy/` 全目录到 `/opt/lcaa-auth`
2. 上传 `tools/deploy_lcaa_auth_ubuntu.sh`
3. 写入 `/etc/lcaa-auth.env`
4. 将旧授权机的 `jw3_auth.db*` 迁移到 `/opt/lcaa-auth/`
5. 执行脚本并启动 `lcaa-auth.service`

建议环境变量：

- `DATABASE_URL=sqlite:////opt/lcaa-auth/jw3_auth.db`
- `SECRET_KEY=<沿用旧授权机值>`
- `ADMIN_PASSWORD=<新增强密码，仅作兜底>`
- `MARKET_UPDATE_SERVER_BASE=http://www.lcaa.top/updates`
- `MARKET_UPDATE_SERVER_TOKEN=<沿用旧授权机值>`
- `MARKET_UPLOAD_TICKET_SECRET=<沿用旧授权机值>`
- `LCA_AUTH_SECRET_FILE=/opt/lcaa-auth/config/build_auth_secret.b64x2`
- `CORS_ORIGINS=http://www.lcaa.top,https://www.lcaa.top`

当前阻塞：

- 两台新服务器外网端口未开放，SSH 不通，无法执行实际远程部署
- 新证书尚未就绪，因此 HTTPS 入口暂未落地
