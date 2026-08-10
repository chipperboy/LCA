# LCAA 单机双 IP 部署结果

部署时间：

- `2026-04-15`

服务器结构：

- 物理主机：`kvm-admin`
- 管理 SSH：`223.254.149.225:15048`
- 公网业务入口：`103.115.41.200`
- 授权公网入口：`223.254.149.225`
- 域名：`www.lcaa.top`、`lcaa.top`

对外访问分配：

- 官网首页：`https://www.lcaa.top/`
- 更新清单：`https://www.lcaa.top/updates/manifest.json`
- 安装包：`https://www.lcaa.top/updates/LCA_Setup_v1.2.6.2.exe`
- 新授权入口：`https://lcaa.top:8000`
- 兼容授权入口：`https://www.lcaa.top:8000`

监听分配：

- `103.115.41.200:80` -> Nginx，跳转到 HTTPS
- `103.115.41.200:443` -> Nginx，官网与下载分发
- `223.254.149.225:8000` -> Nginx，授权主入口
- `103.115.41.200:8000` -> Nginx，旧包兼容入口
- `127.0.0.1:18000` -> 授权服务后端，仅本机可访问
- `*:15048` -> SSH

目录分配：

- 官网目录：`/var/www/lcaa-site`
- 下载目录：`/var/www/updates`
- 授权服务目录：`/opt/lcaa-auth`
- 证书目录：`/etc/nginx/ssl/lcaa.top`
- 授权环境变量：`/etc/lcaa-auth.env`

服务分配：

- Web 服务：`nginx`
- 授权服务：`lcaa-auth`
- 授权服务启动命令：
  - `/opt/lcaa-auth/pyenv/bin/python /opt/lcaa-auth/start_server.py --host 127.0.0.1 --port 18000 --no-ssl --log-level info`

已迁移内容：

- 旧授权数据库：`jw3_auth.db`、`jw3_auth.db-shm`、`jw3_auth.db-wal`
- 管理员会话文件：`admin_sessions.json`
- 旧服务关键环境：
  - `SECRET_KEY`
  - `MARKET_UPDATE_SERVER_TOKEN`
  - `MARKET_UPLOAD_TICKET_SECRET`
- 通信密钥文件：`/opt/lcaa-auth/config/build_auth_secret.b64x2`

已验证结果：

- `https://www.lcaa.top/` 可访问
- `https://www.lcaa.top/updates/manifest.json` 可访问
- `https://www.lcaa.top/updates/LCA_Setup_v1.2.6.2.exe` 可访问
- `https://lcaa.top:8000/` 可访问
- `https://lcaa.top:8000/api/ping_auth` 可访问，并返回认证缺失，说明授权链路正常
- `https://www.lcaa.top:8000/api/ping_auth` 可访问，并返回认证缺失，说明兼容链路正常
- 授权后端仅监听 `127.0.0.1:18000`
- `223.254.149.225` 不承载官网首页，只承载授权入口
- 官网首页已移除版本号、授权入口和目录等敏感展示
- `www.lcaa.top` 已解析到 `103.115.41.200`
- `lcaa.top` 已解析到 `223.254.149.225`

当前注意事项：

- 现在服务器侧已经完成迁移
- 本地源码授权地址已切到 `lcaa.top:8000`
- 本地打包证书 `certs/server.pem` 已同步为 `lcaa.top` 新证书
- 当前下载包仍是 `2026-04-12` 的旧构建，如需让客户端内置地址也切到新域名，需要重新打包一次
