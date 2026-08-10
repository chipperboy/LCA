# -*- coding: utf-8 -*-

from __future__ import annotations

import json

from datetime import datetime
from typing import Any, Callable, Dict, List, Optional, Tuple

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from market_schemas import (
    MarketAdminPackageDetail,
    MarketAdminPackageDetailResponse,
    MarketAdminPackageListResponse,
    MarketAdminPackageVersionSummary,
    MarketDownloadTokenResponse,
    MarketPackageAccessResponse,
    MarketPackageDeleteResponse,
    MarketPackageListResponse,
    MarketPackagePublishRequest,
    MarketPackageStatusUpdateRequest,
    MarketPackageStatusUpdateResponse,
    MarketPackageUploadTicketRequest,
    MarketPackageUploadTicketResponse,
    MarketPackageReviewRequest,
    MarketPackageVersionSummary,
    MarketReviewHistoryItem,
)


_ALLOWED_REVIEW_ACTIONS = {"draft", "submitted", "released", "rejected"}


def build_market_router(
    get_db: Callable[[], Session],
    market_models: Dict[str, object],
    build_download_url: Optional[Callable[[str, str], str]] = None,
    admin_guard: Optional[Callable[[Request, Session], object]] = None,
    release_package: Optional[Callable[[str, str, str, int, str], Dict[str, Any]]] = None,
    author_guard: Optional[Callable[[Request, Session, bool], object]] = None,
    encrypt_payload_key: Optional[Callable[[str], str]] = None,
    decrypt_payload_key: Optional[Callable[[str], str]] = None,
    sign_upload_ticket: Optional[Callable[[str, str, int, int], str]] = None,
    delete_package_storage: Optional[Callable[[str, str], Dict[str, Any]]] = None,
):
    router = APIRouter(prefix="/api/market", tags=["market"])

    MarketPackage = market_models["MarketPackage"]
    MarketPackageVersion = market_models["MarketPackageVersion"]
    MarketReviewRecord = market_models["MarketReviewRecord"]

    def _make_download_url(package_id: str, version: str) -> str:
        if callable(build_download_url):
            return str(build_download_url(package_id, version) or "")
        return f"/market/release/{package_id}/{version}/package.lca_market.zip"

    def _require_admin(request: Request, db: Session):
        if not callable(admin_guard):
            raise HTTPException(status_code=500, detail="market_admin_guard_not_configured")
        return admin_guard(request, db)

    def _resolve_author(request: Request, db: Session, required: bool = False):
        if not callable(author_guard):
            if required:
                raise HTTPException(status_code=500, detail="market_author_guard_not_configured")
            return None
        return author_guard(request, db, required)

    def _parse_manifest_json(raw_value: Any) -> Dict[str, Any]:
        manifest_text = str(raw_value or "").strip()
        if not manifest_text:
            return {}
        try:
            parsed = json.loads(manifest_text)
        except Exception:
            return {"_raw": manifest_text}
        if isinstance(parsed, dict):
            return parsed
        return {"value": parsed}

    def _get_package_version_or_404(db: Session, package_id: str, version: str) -> Tuple[object, object]:
        package_row = db.query(MarketPackage).filter(MarketPackage.package_id == package_id).first()
        if package_row is None:
            raise HTTPException(status_code=404, detail="package_not_found")

        version_row = (
            db.query(MarketPackageVersion)
            .filter(MarketPackageVersion.package_id_fk == package_row.id)
            .filter(MarketPackageVersion.version == version)
            .first()
        )
        if version_row is None:
            raise HTTPException(status_code=404, detail="package_version_not_found")
        return package_row, version_row

    def _is_owned_by_current_user(package_row, current_user) -> bool:
        if current_user is None:
            return False
        try:
            owner_user_id = int(getattr(package_row, "owner_user_id", 0) or 0)
            current_user_id = int(getattr(current_user, "id", 0) or 0)
        except Exception:
            return False
        return owner_user_id > 0 and owner_user_id == current_user_id

    def _can_manage_package(package_row, current_user) -> bool:
        if current_user is None:
            return False
        if bool(getattr(current_user, "is_admin", False)):
            return True
        owner_user_id = getattr(package_row, "owner_user_id", None)
        if owner_user_id in (None, 0, ""):
            return False
        try:
            return int(owner_user_id) == int(getattr(current_user, "id", 0) or 0)
        except Exception:
            return False

    def _extract_manifest_protection(manifest: Dict[str, Any]) -> Dict[str, Any]:
        protection = manifest.get("protection") if isinstance(manifest.get("protection"), dict) else {}
        return dict(protection) if isinstance(protection, dict) else {}

    def _require_protected_payload_key(payload: MarketPackagePublishRequest) -> tuple[str, str]:
        manifest = payload.manifest if isinstance(payload.manifest, dict) else {}
        protection = _extract_manifest_protection(manifest)
        protection_enabled = bool(protection.get("enabled"))
        protection_scheme = str(protection.get("scheme") or "").strip()
        payload_key = str(payload.protection_payload_key or "").strip()
        if protection_enabled:
            if not protection_scheme:
                raise HTTPException(status_code=400, detail="invalid_market_protection_scheme")
            if not payload_key:
                raise HTTPException(status_code=400, detail="market_protection_payload_key_required")
        return protection_scheme, payload_key

    def _decrypt_version_payload_key(version_row) -> str:
        encrypted_value = str(getattr(version_row, "protection_payload_key", "") or "").strip()
        if not encrypted_value:
            return ""
        if not callable(decrypt_payload_key):
            raise HTTPException(status_code=500, detail="market_payload_key_decryptor_not_configured")
        return str(decrypt_payload_key(encrypted_value) or "").strip()

    def _extract_author_name(payload: MarketPackagePublishRequest, current_user) -> str:
        manifest = payload.manifest if isinstance(payload.manifest, dict) else {}
        author_name = str(manifest.get("author") or "").strip()
        if author_name:
            return author_name
        return str(getattr(current_user, "username", "") or "").strip()

    def _normalize_version_status(version_row) -> str:
        return str(getattr(version_row, "status", "") or "").strip().lower()

    def _can_delete_version(version_row, package_row, current_user) -> bool:
        return _can_manage_package(package_row, current_user) and _normalize_version_status(version_row) != "released"

    def _refresh_package_state(db: Session, package_row) -> bool:
        version_rows = (
            db.query(MarketPackageVersion)
            .filter(MarketPackageVersion.package_id_fk == package_row.id)
            .all()
        )
        if not version_rows:
            package_row.latest_version = ""
            package_row.is_active = False
            package_row.updated_at = datetime.utcnow()
            return False

        sorted_rows = sorted(
            version_rows,
            key=lambda row: (
                getattr(row, "published_at", None) or datetime.min,
                getattr(row, "created_at", None) or datetime.min,
                int(getattr(row, "id", 0) or 0),
            ),
            reverse=True,
        )
        released_rows = [row for row in sorted_rows if _normalize_version_status(row) == "released"]
        preferred_row = released_rows[0] if released_rows else sorted_rows[0]
        package_row.latest_version = str(getattr(preferred_row, "version", "") or "")
        package_row.is_active = bool(released_rows)
        package_row.updated_at = datetime.utcnow()
        return True

    def _delete_package_version_record(
        db: Session,
        package_row,
        version_row,
        package_id: str,
        version: str,
    ) -> MarketPackageDeleteResponse:
        db.query(MarketReviewRecord).filter(MarketReviewRecord.package_id == package_id).filter(
            MarketReviewRecord.version == version
        ).delete(synchronize_session=False)
        db.delete(version_row)
        db.flush()

        deleted_package = False
        if not _refresh_package_state(db, package_row):
            db.delete(package_row)
            deleted_package = True

        db.commit()

        if callable(delete_package_storage):
            try:
                delete_package_storage(package_id, version)
            except Exception:
                pass

        return MarketPackageDeleteResponse(
            success=True,
            package_id=package_id,
            version=version,
            deleted_package=deleted_package,
        )

    def _build_public_summary(version_row, package_row, current_user=None) -> MarketPackageVersionSummary:
        normalized_status = _normalize_version_status(version_row)
        can_run = normalized_status == "released"
        return MarketPackageVersionSummary(
            package_id=package_row.package_id,
            version=version_row.version,
            title=package_row.title,
            category=package_row.category,
            summary=package_row.summary,
            author_name=str(getattr(package_row, "author_name", "") or ""),
            status=version_row.status,
            latest_version=package_row.latest_version,
            visibility=package_row.visibility,
            cover_url=version_row.cover_path,
            download_url=_make_download_url(package_row.package_id, version_row.version) if can_run else "",
            can_edit=_is_owned_by_current_user(package_row, current_user),
            can_delete=_can_delete_version(version_row, package_row, current_user),
            can_run=can_run,
        )

    def _build_admin_summary(version_row, package_row) -> MarketAdminPackageVersionSummary:
        download_url = ""
        if str(version_row.status or "").strip().lower() == "released":
            download_url = _make_download_url(package_row.package_id, version_row.version)
        return MarketAdminPackageVersionSummary(
            package_id=package_row.package_id,
            version=version_row.version,
            title=package_row.title,
            category=package_row.category,
            summary=package_row.summary,
            author_name=str(getattr(package_row, "author_name", "") or ""),
            owner_user_id=getattr(package_row, "owner_user_id", None),
            status=version_row.status,
            latest_version=package_row.latest_version,
            visibility=package_row.visibility,
            cover_url=version_row.cover_path,
            download_url=download_url,
            review_comment=version_row.review_comment,
            storage_path=version_row.storage_path,
            file_sha256=version_row.file_sha256,
            file_size=int(version_row.file_size or 0),
            created_at=version_row.created_at,
            reviewed_at=version_row.reviewed_at,
            published_at=version_row.published_at,
        )

    def _build_admin_detail(version_row, package_row, review_rows: List[object]) -> MarketAdminPackageDetail:
        download_url = ""
        if str(version_row.status or "").strip().lower() == "released":
            download_url = _make_download_url(package_row.package_id, version_row.version)
        return MarketAdminPackageDetail(
            package_id=package_row.package_id,
            version=version_row.version,
            title=package_row.title,
            category=package_row.category,
            summary=package_row.summary,
            author_name=str(getattr(package_row, "author_name", "") or ""),
            owner_user_id=getattr(package_row, "owner_user_id", None),
            status=version_row.status,
            latest_version=package_row.latest_version,
            visibility=package_row.visibility,
            cover_url=version_row.cover_path,
            download_url=download_url,
            review_comment=version_row.review_comment,
            storage_path=version_row.storage_path,
            file_sha256=version_row.file_sha256,
            file_size=int(version_row.file_size or 0),
            created_at=version_row.created_at,
            reviewed_at=version_row.reviewed_at,
            published_at=version_row.published_at,
            manifest=_parse_manifest_json(version_row.manifest_json),
            changelog=str(version_row.changelog or ""),
            release_notes=str(version_row.release_notes or ""),
            review_history=[
                MarketReviewHistoryItem(
                    reviewer=str(getattr(row, "reviewer", "") or ""),
                    action=str(getattr(row, "action", "") or ""),
                    comment=str(getattr(row, "comment", "") or ""),
                    created_at=getattr(row, "created_at", None),
                )
                for row in review_rows
            ],
        )

    @router.get("/packages", response_model=MarketPackageListResponse)
    def list_packages(request: Request, db: Session = Depends(get_db)):
        current_user = _resolve_author(request, db, required=False)
        rows = (
            db.query(MarketPackageVersion, MarketPackage)
            .join(MarketPackage, MarketPackageVersion.package_id_fk == MarketPackage.id)
            .filter(MarketPackageVersion.status == "released")
            .order_by(MarketPackage.updated_at.desc(), MarketPackageVersion.published_at.desc(), MarketPackageVersion.id.desc())
            .all()
        )
        items = [_build_public_summary(version_row, package_row, current_user=current_user) for version_row, package_row in rows]
        return MarketPackageListResponse(items=items, total=len(items))

    @router.get("/my/packages", response_model=MarketPackageListResponse)
    def list_my_packages(request: Request, db: Session = Depends(get_db)):
        current_user = _resolve_author(request, db, required=True)
        rows = (
            db.query(MarketPackageVersion, MarketPackage)
            .join(MarketPackage, MarketPackageVersion.package_id_fk == MarketPackage.id)
            .filter(MarketPackage.owner_user_id == int(getattr(current_user, "id", 0) or 0))
            .order_by(MarketPackage.updated_at.desc(), MarketPackageVersion.created_at.desc(), MarketPackageVersion.id.desc())
            .all()
        )
        items = [_build_public_summary(version_row, package_row, current_user=current_user) for version_row, package_row in rows]
        return MarketPackageListResponse(items=items, total=len(items))

    @router.get("/admin/packages", response_model=MarketAdminPackageListResponse)
    def list_admin_packages(
        request: Request,
        status: str = "",
        db: Session = Depends(get_db),
    ):
        _require_admin(request, db)
        query = (
            db.query(MarketPackageVersion, MarketPackage)
            .join(MarketPackage, MarketPackageVersion.package_id_fk == MarketPackage.id)
        )
        normalized_status = str(status or "").strip().lower()
        if normalized_status:
            query = query.filter(MarketPackageVersion.status == normalized_status)
        rows = query.order_by(MarketPackage.updated_at.desc(), MarketPackageVersion.created_at.desc(), MarketPackageVersion.id.desc()).all()
        items = [_build_admin_summary(version_row, package_row) for version_row, package_row in rows]
        return MarketAdminPackageListResponse(items=items, total=len(items))

    @router.get("/admin/packages/{package_id}/{version}", response_model=MarketAdminPackageDetailResponse)
    def get_admin_package_detail(
        package_id: str,
        version: str,
        request: Request,
        db: Session = Depends(get_db),
    ):
        _require_admin(request, db)
        package_row, version_row = _get_package_version_or_404(db, package_id, version)
        review_rows = (
            db.query(MarketReviewRecord)
            .filter(MarketReviewRecord.package_id == package_id)
            .filter(MarketReviewRecord.version == version)
            .order_by(MarketReviewRecord.created_at.desc(), MarketReviewRecord.id.desc())
            .all()
        )
        return MarketAdminPackageDetailResponse(
            success=True,
            package=_build_admin_detail(version_row, package_row, review_rows),
        )

    @router.post("/packages/upload-ticket", response_model=MarketPackageUploadTicketResponse)
    def create_upload_ticket(
        payload: MarketPackageUploadTicketRequest,
        request: Request,
        db: Session = Depends(get_db),
    ):
        current_user = _resolve_author(request, db, required=True)
        if not callable(sign_upload_ticket):
            raise HTTPException(status_code=500, detail="market_upload_ticket_signer_not_configured")

        package_id = str(payload.package_id or "").strip()
        version = str(payload.version or "").strip()
        package_row = db.query(MarketPackage).filter(MarketPackage.package_id == package_id).first()
        if package_row is not None and not _can_manage_package(package_row, current_user):
            raise HTTPException(status_code=403, detail="package_id_owned_by_other_author")

        expires_in = 300
        upload_ticket = str(
            sign_upload_ticket(
                package_id,
                version,
                int(getattr(current_user, "id", 0) or 0),
                expires_in,
            ) or ""
        ).strip()
        if not upload_ticket:
            raise HTTPException(status_code=500, detail="market_upload_ticket_sign_failed")
        return MarketPackageUploadTicketResponse(
            success=True,
            package_id=package_id,
            version=version,
            upload_ticket=upload_ticket,
            expires_in=expires_in,
        )

    @router.post("/packages/publish")
    def publish_package(
        payload: MarketPackagePublishRequest,
        request: Request,
        db: Session = Depends(get_db),
    ):
        current_user = _resolve_author(request, db, required=True)
        now = datetime.utcnow()
        package_row = db.query(MarketPackage).filter(MarketPackage.package_id == payload.package_id).first()
        resolved_author_name = _extract_author_name(payload, current_user)
        protection_mode, protection_payload_key = _require_protected_payload_key(payload)

        if package_row is None:
            package_row = MarketPackage(
                package_id=payload.package_id,
                title=payload.title,
                category=payload.category,
                summary=payload.summary,
                author_name=resolved_author_name,
                owner_user_id=int(getattr(current_user, "id", 0) or 0),
                latest_version="",
                visibility="private",
                is_active=True,
                created_at=now,
                updated_at=now,
            )
            db.add(package_row)
            db.flush()
        else:
            owner_user_id = getattr(package_row, "owner_user_id", None)
            if owner_user_id in (None, 0, ""):
                package_row.owner_user_id = int(getattr(current_user, "id", 0) or 0)
            elif not _can_manage_package(package_row, current_user):
                raise HTTPException(status_code=403, detail="package_id_owned_by_other_author")
            package_row.title = payload.title
            package_row.category = payload.category
            package_row.summary = payload.summary
            package_row.author_name = resolved_author_name or str(getattr(package_row, "author_name", "") or "")
            package_row.updated_at = now

        version_row = (
            db.query(MarketPackageVersion)
            .filter(MarketPackageVersion.package_id_fk == package_row.id)
            .filter(MarketPackageVersion.version == payload.version)
            .first()
        )
        if version_row is None:
            version_row = MarketPackageVersion(
                package_id_fk=package_row.id,
                version=payload.version,
                created_at=now,
            )
            db.add(version_row)

        if not str(package_row.latest_version or "").strip():
            package_row.latest_version = payload.version

        version_row.status = "submitted"
        version_row.manifest_json = json.dumps(payload.manifest, ensure_ascii=False)
        version_row.storage_path = payload.storage_path
        version_row.file_sha256 = payload.file_sha256
        version_row.file_size = int(payload.file_size or 0)
        version_row.protection_mode = protection_mode
        if protection_payload_key:
            if not callable(encrypt_payload_key):
                raise HTTPException(status_code=500, detail="market_payload_key_encryptor_not_configured")
            version_row.protection_payload_key = str(encrypt_payload_key(protection_payload_key) or "")
        else:
            version_row.protection_payload_key = ""
        version_row.cover_path = payload.cover_path
        version_row.changelog = payload.changelog
        version_row.release_notes = payload.release_notes
        version_row.review_comment = ""
        version_row.reviewed_at = None
        version_row.published_at = None

        _refresh_package_state(db, package_row)
        db.commit()
        return {
            "success": True,
            "package_id": payload.package_id,
            "version": payload.version,
            "status": version_row.status,
            "author_name": package_row.author_name,
            "can_edit": True,
        }

    @router.delete("/packages/{package_id}/{version}", response_model=MarketPackageDeleteResponse)
    def delete_package_version(package_id: str, version: str, request: Request, db: Session = Depends(get_db)):
        package_row, version_row = _get_package_version_or_404(db, package_id, version)
        current_user = _resolve_author(request, db, required=True)
        if not _can_manage_package(package_row, current_user):
            raise HTTPException(status_code=403, detail="package_delete_forbidden")
        if _normalize_version_status(version_row) == "released":
            raise HTTPException(status_code=409, detail="package_delete_not_allowed")

        return _delete_package_version_record(db, package_row, version_row, package_id, version)

    @router.post("/packages/{package_id}/{version}/status", response_model=MarketPackageStatusUpdateResponse)
    def update_package_version_status(
        package_id: str,
        version: str,
        payload: MarketPackageStatusUpdateRequest,
        request: Request,
        db: Session = Depends(get_db),
    ):
        package_row, version_row = _get_package_version_or_404(db, package_id, version)
        current_user = _resolve_author(request, db, required=True)
        if not _can_manage_package(package_row, current_user):
            raise HTTPException(status_code=403, detail="package_edit_forbidden")

        action = str(payload.action or "").strip().lower()
        if action not in {"offline", "released"}:
            raise HTTPException(status_code=400, detail="invalid_market_package_status_action")

        current_status = _normalize_version_status(version_row)
        if action == current_status:
            return MarketPackageStatusUpdateResponse(
                success=True,
                package=_build_public_summary(version_row, package_row, current_user=current_user),
            )

        if action == "offline":
            if current_status != "released":
                raise HTTPException(status_code=409, detail="package_status_transition_not_allowed")
            version_row.status = "offline"
        else:
            if current_status != "offline":
                raise HTTPException(status_code=409, detail="package_status_transition_not_allowed")
            version_row.status = "released"
            version_row.published_at = getattr(version_row, "published_at", None) or datetime.utcnow()

        package_row.updated_at = datetime.utcnow()
        _refresh_package_state(db, package_row)
        db.commit()
        db.refresh(version_row)
        db.refresh(package_row)
        return MarketPackageStatusUpdateResponse(
            success=True,
            package=_build_public_summary(version_row, package_row, current_user=current_user),
        )

    @router.delete("/admin/packages/{package_id}/{version}", response_model=MarketPackageDeleteResponse)
    def delete_admin_package_version(package_id: str, version: str, request: Request, db: Session = Depends(get_db)):
        _require_admin(request, db)
        package_row, version_row = _get_package_version_or_404(db, package_id, version)
        if _normalize_version_status(version_row) == "released":
            raise HTTPException(status_code=409, detail="package_delete_not_allowed")
        return _delete_package_version_record(db, package_row, version_row, package_id, version)

    @router.post("/admin/review")
    def review_package(
        payload: MarketPackageReviewRequest,
        request: Request,
        db: Session = Depends(get_db),
    ):
        admin_user = _require_admin(request, db)
        action = str(payload.action or "").strip().lower()
        if action not in _ALLOWED_REVIEW_ACTIONS:
            raise HTTPException(status_code=400, detail="invalid_market_review_action")

        package_row, version_row = _get_package_version_or_404(db, payload.package_id, payload.version)

        now = datetime.utcnow()
        release_result: Dict[str, Any] = {}
        if action == "released":
            if not callable(release_package):
                raise HTTPException(status_code=500, detail="market_release_callback_not_configured")
            try:
                release_result = release_package(
                    payload.package_id,
                    payload.version,
                    str(version_row.file_sha256 or ""),
                    int(version_row.file_size or 0),
                    str(version_row.storage_path or ""),
                ) or {}
            except HTTPException:
                raise
            except Exception as exc:
                raise HTTPException(status_code=502, detail=f"market_release_failed: {exc}") from exc

        version_row.status = action
        version_row.review_comment = str(payload.comment or "")
        version_row.reviewed_at = now
        package_row.updated_at = now

        if action == "released":
            release_storage_path = str(release_result.get("storage_path") or "").strip()
            release_cover_path = str(release_result.get("cover_path") or "").strip()
            if release_storage_path:
                version_row.storage_path = release_storage_path
            if release_cover_path:
                version_row.cover_path = release_cover_path
            version_row.published_at = now
            package_row.latest_version = payload.version
            package_row.is_active = True
        else:
            version_row.published_at = None

        reviewer_name = str(getattr(admin_user, "username", "admin") or "admin")
        db.add(
            MarketReviewRecord(
                package_id=payload.package_id,
                version=payload.version,
                reviewer=reviewer_name,
                action=action,
                comment=version_row.review_comment,
                created_at=now,
            )
        )
        _refresh_package_state(db, package_row)
        db.commit()
        return {"success": True, "status": version_row.status}

    @router.get("/packages/{package_id}/{version}/download", response_model=MarketDownloadTokenResponse)
    def get_download_token(package_id: str, version: str, db: Session = Depends(get_db)):
        package_row, version_row = _get_package_version_or_404(db, package_id, version)
        if str(version_row.status or "").strip().lower() != "released":
            raise HTTPException(status_code=404, detail="package_version_not_found")

        return MarketDownloadTokenResponse(
            package_id=package_id,
            version=version,
            download_url=_make_download_url(package_id, version),
            expires_in=300,
        )

    @router.post("/packages/{package_id}/{version}/runtime-access", response_model=MarketPackageAccessResponse)
    def get_runtime_access(package_id: str, version: str, db: Session = Depends(get_db)):
        _package_row, version_row = _get_package_version_or_404(db, package_id, version)
        if str(version_row.status or "").strip().lower() != "released":
            raise HTTPException(status_code=404, detail="package_version_not_found")
        payload_key = _decrypt_version_payload_key(version_row)
        if not payload_key:
            raise HTTPException(status_code=409, detail="market_package_not_protected")
        return MarketPackageAccessResponse(
            success=True,
            package_id=package_id,
            version=version,
            access_mode="run",
            payload_key=payload_key,
            expires_in=120,
        )

    @router.post("/packages/{package_id}/{version}/edit-access", response_model=MarketPackageAccessResponse)
    def get_edit_access(package_id: str, version: str, request: Request, db: Session = Depends(get_db)):
        package_row, version_row = _get_package_version_or_404(db, package_id, version)
        current_user = _resolve_author(request, db, required=True)
        if not _can_manage_package(package_row, current_user):
            raise HTTPException(status_code=403, detail="package_edit_forbidden")
        payload_key = _decrypt_version_payload_key(version_row)
        if not payload_key:
            raise HTTPException(status_code=409, detail="market_package_not_protected")
        return MarketPackageAccessResponse(
            success=True,
            package_id=package_id,
            version=version,
            access_mode="edit",
            payload_key=payload_key,
            expires_in=120,
        )

    return router
