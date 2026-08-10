# Update Server Redeploy

External mapping in use:

- `222.186.21.45:21669 -> 22/tcp`
- `222.186.21.45:6565 -> 3000/tcp`

The client update path is fixed to:

- `http://222.186.21.45:6565/manifest.json`
- `http://222.186.21.45:6565/LCA_Setup_v<version>.exe`

## Server bootstrap

Copy and run the bootstrap script after the server is reinstalled:

```bash
scp -P 21669 tools/redeploy_update_server_ubuntu.sh root@222.186.21.45:/root/
ssh -p 21669 root@222.186.21.45 "bash /root/redeploy_update_server_ubuntu.sh"
```

What the script does:

- installs `nginx`
- creates `/var/www/updates`
- configures `nginx` to listen on `3000`
- enables and restarts `nginx`
- opens `3000/tcp` in `ufw` when `ufw` is active

## Publish files

Build locally, then upload the release files:

```bash
scp -P 21669 build_assets/packaging/release_output/manifest.json root@222.186.21.45:/var/www/updates/
scp -P 21669 build_assets/packaging/release_output/LCA_Setup_v<version>.exe root@222.186.21.45:/var/www/updates/
ssh -p 21669 root@222.186.21.45 "chown www-data:www-data /var/www/updates/*"
```

## Verify

Check on the server:

```bash
ss -lntp | grep :3000
systemctl status nginx --no-pager
curl http://127.0.0.1:3000/manifest.json
```

Check from outside:

```bash
curl http://222.186.21.45:6565/manifest.json
```

If the external check fails, verify the NAT rule still maps `6565 -> 3000`.
