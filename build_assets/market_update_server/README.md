# 更新服务器共享平台包目录规范

更新服务器只负责共享平台包文件分发与暂存，不负责业务审核。

目录约定：

- `market/staging/<package_id>/<version>/package.lca_market.zip`
- `market/staging/<package_id>/<version>/manifest.json`
- `market/staging/<package_id>/<version>/cover.png`
- `market/release/<package_id>/<version>/package.lca_market.zip`
- `market/release/<package_id>/<version>/manifest.json`
- `market/release/<package_id>/<version>/cover.png`
- `market/release/<package_id>/<version>/release_manifest.json`

规则：

- `staging`：仅上传和审核阶段使用，不对普通客户端展示
- `release`：审核通过后对客户端下载开放
- 已发布版本不可覆盖，只能新增版本目录
- 授权服务器审核通过后调用发布接口，把 `staging` 提升到 `release`

内置服务文件：

- `server.py`

环境变量：

- `MARKET_UPDATE_STORAGE_ROOT`：共享平台包存储根目录，默认 `server.py` 同级 `data`
- `MARKET_UPDATE_SERVER_TOKEN`：发布接口令牌，可空；为空时仅上传开放，发布不校验令牌

最小接口：

- `GET /health`
- `POST /api/market/packages/upload`
  - 请求体使用 `multipart/form-data`，文件字段为 `file`，内容为共享平台包 zip 文件
  - 请求头需携带 `X-Market-Package-Id` 和 `X-Market-Package-Version`
- `POST /api/market/packages/{package_id}/{version}/release`
- `GET /market/...` 静态分发共享平台包文件

启动示例：

```bash
uvicorn server:app --host 0.0.0.0 --port 6565
```
