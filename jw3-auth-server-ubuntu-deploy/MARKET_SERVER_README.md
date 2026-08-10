# 共享平台认证服务端说明

当前目录已经是可部署版本，不再是仅有骨架的半成品。

已接入能力：

- 共享平台作者注册、登录、资料读取、退出登录
- 共享平台包列表、我的发布、发布票据、发布登记
- 运行授权、编辑授权、版本删除
- 共享平台表自动建表

关键文件：

- `auth_server.py`：主服务入口，已挂载共享平台路由
- `market_router.py`：共享平台接口路由
- `market_models.py`：共享平台相关表模型
- `market_schemas.py`：共享平台接口数据结构

部署要点：

1. 将上述 4 个文件同步到服务端工作目录
2. 使用服务端虚拟环境执行编译检查
3. 重启 `jw3-auth-server.service`
4. 验证以下接口不再返回 404

建议验证：

- `GET /api/market/packages`
- `GET /api/market/my/packages`
- `POST /api/market/packages/upload-ticket`
- `POST /api/market/packages/publish`

说明：

- 包文件存储与下载仍由更新服务器负责
- 认证服务端负责元数据、作者权限、运行授权、编辑授权
