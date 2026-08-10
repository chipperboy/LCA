# -*- coding: utf-8 -*-

from __future__ import annotations

import hashlib
import base64
import hmac
import time
import json
import os
import shutil
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict

from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field


APP_ROOT = Path(__file__).resolve().parent
STORAGE_ROOT = Path(os.getenv("MARKET_UPDATE_STORAGE_ROOT", str(APP_ROOT / "data"))).expanduser().resolve()
MARKET_ROOT = STORAGE_ROOT / "market"
STAGING_ROOT = MARKET_ROOT / "staging"
RELEASE_ROOT = MARKET_ROOT / "release"
UPDATE_SERVER_TOKEN = str(os.getenv("MARKET_UPDATE_SERVER_TOKEN", "") or "").strip()
MARKET_UPLOAD_TICKET_SECRET = str(os.getenv("MARKET_UPLOAD_TICKET_SECRET", "") or "").strip()
SAFE_SEGMENT_CHARS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-")
PACKAGE_FILENAME = "package.lca_market.zip"
MANIFEST_FILENAME = "manifest.json"
RELEASE_MANIFEST_FILENAME = "release_manifest.json"

for root in (STORAGE_ROOT, MARKET_ROOT, STAGING_ROOT, RELEASE_ROOT):
    root.mkdir(parents=True, exist_ok=True)

app = FastAPI(title="LCA 共享平台更新服务", version="1.0.0")
app.mount("/market", StaticFiles(directory=str(MARKET_ROOT)), name="market")


class ReleaseRequest(BaseModel):
    file_sha256: str = Field(default="")
    file_size: int = Field(default=0)
    storage_path: str = Field(default="")


def _validate_segment(name: str, value: str) -> str:
    text = str(value or "").strip()
    if not text:
        raise HTTPException(status_code=400, detail=f"{name}_required")
    if any(char not in SAFE_SEGMENT_CHARS for char in text):
        raise HTTPException(status_code=400, detail=f"invalid_{name}")
    return text


def _normalize_archive_member_path(member_path: Any) -> str:
    normalized = str(member_path or "").replace("\\", "/").strip("/")
    if not normalized:
        return ""
    parts = []
    for part in normalized.split("/"):
        clean_part = str(part or "").strip()
        if not clean_part or clean_part == ".":
            continue
        if clean_part == "..":
            raise HTTPException(status_code=400, detail="invalid_archive_member_path")
        parts.append(clean_part)
    return "/".join(parts)


def _build_storage_path(stage: str, package_id: str, version: str, filename: str) -> str:
    return f"/market/{stage}/{package_id}/{version}/{filename}"


def _calculate_sha256(file_path: Path) -> str:
    digest = hashlib.sha256()
    with file_path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            if chunk:
                digest.update(chunk)
    return digest.hexdigest()


def _load_manifest_from_archive(archive_path: Path) -> Dict[str, Any]:
    try:
        with zipfile.ZipFile(archive_path, "r") as archive:
            manifest_bytes = archive.read(MANIFEST_FILENAME)
    except KeyError as exc:
        raise HTTPException(status_code=400, detail="manifest_missing") from exc
    except zipfile.BadZipFile as exc:
        raise HTTPException(status_code=400, detail="invalid_archive") from exc

    try:
        manifest = json.loads(manifest_bytes.decode("utf-8"))
    except Exception as exc:
        raise HTTPException(status_code=400, detail="manifest_invalid") from exc
    if not isinstance(manifest, dict):
        raise HTTPException(status_code=400, detail="manifest_invalid")
    return manifest


def _extract_cover_from_archive(archive_path: Path, manifest: Dict[str, Any], output_dir: Path) -> str:
    cover_member = _normalize_archive_member_path(manifest.get("cover_image"))
    if not cover_member:
        return ""

    cover_name = Path(cover_member).name
    if not cover_name:
        return ""

    try:
        with zipfile.ZipFile(archive_path, "r") as archive:
            cover_bytes = archive.read(cover_member)
    except KeyError:
        return ""
    except zipfile.BadZipFile as exc:
        raise HTTPException(status_code=400, detail="invalid_archive") from exc

    cover_path = output_dir / cover_name
    cover_path.write_bytes(cover_bytes)
    return cover_name


def _build_release_manifest(package_id: str, version: str, manifest: Dict[str, Any], file_size: int, sha256: str, cover_name: str) -> Dict[str, Any]:
    return {
        "package_id": package_id,
        "version": version,
        "title": str(manifest.get("title") or package_id),
        "file_name": PACKAGE_FILENAME,
        "file_size": int(file_size or 0),
        "sha256": str(sha256 or ""),
        "cover": cover_name,
        "manifest": MANIFEST_FILENAME,
        "released_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    }


def _get_upload_ticket_secret() -> str:
    secret_value = str(MARKET_UPLOAD_TICKET_SECRET or "").strip()
    if secret_value:
        return secret_value
    return str(UPDATE_SERVER_TOKEN or "").strip()


def _b64decode_urlsafe_text(text: str) -> bytes:
    raw = str(text or "").strip()
    if not raw:
        raise HTTPException(status_code=401, detail="invalid_market_upload_ticket")
    padding = "=" * (-len(raw) % 4)
    try:
        return base64.urlsafe_b64decode((raw + padding).encode("utf-8"))
    except Exception as exc:
        raise HTTPException(status_code=401, detail="invalid_market_upload_ticket") from exc


def _validate_upload_ticket(ticket_text: str, package_id: str, version: str) -> Dict[str, Any]:
    secret_value = _get_upload_ticket_secret()
    if not secret_value:
        raise HTTPException(status_code=500, detail="market_upload_ticket_secret_not_configured")

    normalized_ticket = str(ticket_text or "").strip()
    try:
        encoded_payload, encoded_signature = normalized_ticket.split('.', 1)
    except ValueError as exc:
        raise HTTPException(status_code=401, detail="invalid_market_upload_ticket") from exc

    expected_signature = hmac.new(
        secret_value.encode("utf-8"),
        encoded_payload.encode("utf-8"),
        hashlib.sha256,
    ).digest()
    actual_signature = _b64decode_urlsafe_text(encoded_signature)
    if not hmac.compare_digest(expected_signature, actual_signature):
        raise HTTPException(status_code=401, detail="invalid_market_upload_ticket")

    try:
        payload = json.loads(_b64decode_urlsafe_text(encoded_payload).decode("utf-8"))
    except Exception as exc:
        raise HTTPException(status_code=401, detail="invalid_market_upload_ticket") from exc
    if not isinstance(payload, dict):
        raise HTTPException(status_code=401, detail="invalid_market_upload_ticket")

    payload_package_id = _validate_segment("ticket_package_id", payload.get("package_id"))
    payload_version = _validate_segment("ticket_version", payload.get("version"))
    if payload_package_id != package_id or payload_version != version:
        raise HTTPException(status_code=401, detail="market_upload_ticket_mismatch")

    expires_at = int(payload.get("exp") or 0)
    now_ts = int(time.time())
    if expires_at <= now_ts:
        raise HTTPException(status_code=401, detail="market_upload_ticket_expired")
    return payload


def _require_release_token(token_header: str) -> None:
    if not UPDATE_SERVER_TOKEN:
        return
    if str(token_header or "").strip() != UPDATE_SERVER_TOKEN:
        raise HTTPException(status_code=401, detail="invalid_market_update_token")


@app.get("/health")
def health() -> Dict[str, Any]:
    return {
        "success": True,
        "service": "market_update_server",
        "storage_root": str(STORAGE_ROOT),
    }


@app.post("/api/market/packages/upload")
async def upload_package(
    request: Request,
    x_market_package_id: str = Header(default=""),
    x_market_package_version: str = Header(default=""),
    x_market_upload_ticket: str = Header(default=""),
) -> Dict[str, Any]:
    safe_package_id = _validate_segment("package_id", x_market_package_id)
    safe_version = _validate_segment("version", x_market_package_version)
    _validate_upload_ticket(x_market_upload_ticket, safe_package_id, safe_version)

    staging_dir = STAGING_ROOT / safe_package_id / safe_version
    if staging_dir.exists():
        shutil.rmtree(staging_dir, ignore_errors=True)
    staging_dir.mkdir(parents=True, exist_ok=True)

    archive_path = staging_dir / PACKAGE_FILENAME
    file_size = 0
    digest = hashlib.sha256()
    try:
        with archive_path.open("wb") as output_handle:
            async for chunk in request.stream():
                if not chunk:
                    continue
                output_handle.write(chunk)
                digest.update(chunk)
                file_size += len(chunk)

        manifest = _load_manifest_from_archive(archive_path)
        manifest_package_id = _validate_segment("manifest_package_id", manifest.get("package_id"))
        manifest_version = _validate_segment("manifest_version", manifest.get("version"))
        if manifest_package_id != safe_package_id or manifest_version != safe_version:
            raise HTTPException(status_code=400, detail="manifest_identity_mismatch")

        manifest_path = staging_dir / MANIFEST_FILENAME
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
        cover_name = _extract_cover_from_archive(archive_path, manifest, staging_dir)
    except Exception:
        shutil.rmtree(staging_dir, ignore_errors=True)
        raise

    return {
        "success": True,
        "package_id": safe_package_id,
        "version": safe_version,
        "title": str(manifest.get("title") or safe_package_id),
        "storage_path": _build_storage_path("staging", safe_package_id, safe_version, PACKAGE_FILENAME),
        "manifest_path": _build_storage_path("staging", safe_package_id, safe_version, MANIFEST_FILENAME),
        "cover_path": _build_storage_path("staging", safe_package_id, safe_version, cover_name) if cover_name else "",
        "file_sha256": digest.hexdigest(),
        "file_size": file_size,
    }


@app.post("/api/market/packages/{package_id}/{version}/release")
def release_package(
    package_id: str,
    version: str,
    payload: ReleaseRequest,
    x_market_update_token: str = Header(default=""),
) -> Dict[str, Any]:
    _require_release_token(x_market_update_token)
    safe_package_id = _validate_segment("package_id", package_id)
    safe_version = _validate_segment("version", version)

    staging_dir = STAGING_ROOT / safe_package_id / safe_version
    if not staging_dir.exists():
        raise HTTPException(status_code=404, detail="staging_package_not_found")

    archive_path = staging_dir / PACKAGE_FILENAME
    manifest_path = staging_dir / MANIFEST_FILENAME
    if not archive_path.exists() or not manifest_path.exists():
        raise HTTPException(status_code=404, detail="staging_package_invalid")

    actual_file_size = int(archive_path.stat().st_size)
    actual_file_sha256 = _calculate_sha256(archive_path)
    expected_sha256 = str(payload.file_sha256 or "").strip()
    expected_file_size = int(payload.file_size or 0)
    if expected_sha256 and expected_sha256 != actual_file_sha256:
        raise HTTPException(status_code=409, detail="staging_sha256_mismatch")
    if expected_file_size and expected_file_size != actual_file_size:
        raise HTTPException(status_code=409, detail="staging_file_size_mismatch")

    release_dir = RELEASE_ROOT / safe_package_id / safe_version
    if release_dir.exists():
        raise HTTPException(status_code=409, detail="release_version_already_exists")
    release_dir.mkdir(parents=True, exist_ok=False)

    try:
        shutil.copy2(archive_path, release_dir / PACKAGE_FILENAME)
        shutil.copy2(manifest_path, release_dir / MANIFEST_FILENAME)

        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        cover_name = ""
        for child in staging_dir.iterdir():
            if child.is_file() and child.name not in {PACKAGE_FILENAME, MANIFEST_FILENAME}:
                shutil.copy2(child, release_dir / child.name)
                if not cover_name:
                    cover_name = child.name

        release_manifest = _build_release_manifest(
            package_id=safe_package_id,
            version=safe_version,
            manifest=manifest,
            file_size=actual_file_size,
            sha256=actual_file_sha256,
            cover_name=cover_name,
        )
        (release_dir / RELEASE_MANIFEST_FILENAME).write_text(
            json.dumps(release_manifest, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    except Exception:
        shutil.rmtree(release_dir, ignore_errors=True)
        raise

    return {
        "success": True,
        "package_id": safe_package_id,
        "version": safe_version,
        "storage_path": _build_storage_path("release", safe_package_id, safe_version, PACKAGE_FILENAME),
        "manifest_path": _build_storage_path("release", safe_package_id, safe_version, MANIFEST_FILENAME),
        "cover_path": _build_storage_path("release", safe_package_id, safe_version, cover_name) if cover_name else "",
        "release_manifest_path": _build_storage_path("release", safe_package_id, safe_version, RELEASE_MANIFEST_FILENAME),
        "file_sha256": actual_file_sha256,
        "file_size": actual_file_size,
    }


@app.delete("/api/market/packages/{package_id}/{version}")
def delete_package_storage(
    package_id: str,
    version: str,
    x_market_update_token: str = Header(default=""),
) -> Dict[str, Any]:
    _require_release_token(x_market_update_token)
    safe_package_id = _validate_segment("package_id", package_id)
    safe_version = _validate_segment("version", version)

    staging_dir = STAGING_ROOT / safe_package_id / safe_version
    release_dir = RELEASE_ROOT / safe_package_id / safe_version
    deleted_staging = False
    deleted_release = False

    if staging_dir.exists():
        shutil.rmtree(staging_dir, ignore_errors=True)
        deleted_staging = True
    if release_dir.exists():
        shutil.rmtree(release_dir, ignore_errors=True)
        deleted_release = True

    for parent_dir in (STAGING_ROOT / safe_package_id, RELEASE_ROOT / safe_package_id):
        try:
            if parent_dir.exists() and not any(parent_dir.iterdir()):
                parent_dir.rmdir()
        except Exception:
            pass

    return {
        "success": True,
        "package_id": safe_package_id,
        "version": safe_version,
        "deleted_staging": deleted_staging,
        "deleted_release": deleted_release,
    }
