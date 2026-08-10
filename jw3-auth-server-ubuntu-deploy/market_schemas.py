# -*- coding: utf-8 -*-

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class MarketAuthorCredentialsRequest(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=6, max_length=128)


class MarketAuthorProfile(BaseModel):
    id: int
    username: str
    is_admin: bool = False


class MarketAuthorAuthResponse(BaseModel):
    success: bool = True
    access_token: str = Field(default="")
    token_type: str = Field(default="bearer")
    expires_in: int = Field(default=0)
    user: MarketAuthorProfile


class MarketPackageVersionSummary(BaseModel):
    package_id: str = Field(default="")
    version: str = Field(default="")
    title: str = Field(default="")
    category: str = Field(default="")
    summary: str = Field(default="")
    author_name: str = Field(default="")
    status: str = Field(default="draft")
    latest_version: str = Field(default="")
    visibility: str = Field(default="private")
    cover_url: str = Field(default="")
    download_url: str = Field(default="")
    can_edit: bool = Field(default=False)
    can_delete: bool = Field(default=False)
    can_run: bool = Field(default=True)


class MarketAdminPackageVersionSummary(BaseModel):
    package_id: str = Field(default="")
    version: str = Field(default="")
    title: str = Field(default="")
    category: str = Field(default="")
    summary: str = Field(default="")
    author_name: str = Field(default="")
    owner_user_id: Optional[int] = None
    status: str = Field(default="draft")
    latest_version: str = Field(default="")
    visibility: str = Field(default="private")
    cover_url: str = Field(default="")
    download_url: str = Field(default="")
    review_comment: str = Field(default="")
    storage_path: str = Field(default="")
    file_sha256: str = Field(default="")
    file_size: int = Field(default=0)
    created_at: Optional[datetime] = None
    reviewed_at: Optional[datetime] = None
    published_at: Optional[datetime] = None


class MarketReviewHistoryItem(BaseModel):
    reviewer: str = Field(default="")
    action: str = Field(default="")
    comment: str = Field(default="")
    created_at: Optional[datetime] = None


class MarketAdminPackageDetail(BaseModel):
    package_id: str = Field(default="")
    version: str = Field(default="")
    title: str = Field(default="")
    category: str = Field(default="")
    summary: str = Field(default="")
    author_name: str = Field(default="")
    owner_user_id: Optional[int] = None
    status: str = Field(default="draft")
    latest_version: str = Field(default="")
    visibility: str = Field(default="private")
    cover_url: str = Field(default="")
    download_url: str = Field(default="")
    review_comment: str = Field(default="")
    storage_path: str = Field(default="")
    file_sha256: str = Field(default="")
    file_size: int = Field(default=0)
    created_at: Optional[datetime] = None
    reviewed_at: Optional[datetime] = None
    published_at: Optional[datetime] = None
    manifest: Dict[str, Any] = Field(default_factory=dict)
    changelog: str = Field(default="")
    release_notes: str = Field(default="")
    review_history: List[MarketReviewHistoryItem] = Field(default_factory=list)


class MarketAdminPackageDetailResponse(BaseModel):
    success: bool = True
    package: MarketAdminPackageDetail


class MarketPackageUploadTicketRequest(BaseModel):
    package_id: str = Field(min_length=1)
    version: str = Field(min_length=1)


class MarketPackageUploadTicketResponse(BaseModel):
    success: bool = True
    package_id: str
    version: str
    upload_ticket: str = Field(default="")
    expires_in: int = Field(default=300)


class MarketPackageDeleteResponse(BaseModel):
    success: bool = True
    package_id: str
    version: str
    deleted_package: bool = Field(default=False)


class MarketPackageStatusUpdateRequest(BaseModel):
    action: str = Field(min_length=1)


class MarketPackageStatusUpdateResponse(BaseModel):
    success: bool = True
    package: MarketPackageVersionSummary


class MarketPackagePublishRequest(BaseModel):
    package_id: str = Field(min_length=1)
    version: str = Field(min_length=1)
    title: str = Field(min_length=1)
    category: str = Field(default="")
    summary: str = Field(default="")
    manifest: Dict[str, Any] = Field(default_factory=dict)
    file_sha256: str = Field(default="")
    file_size: int = Field(default=0)
    storage_path: str = Field(default="")
    cover_path: str = Field(default="")
    changelog: str = Field(default="")
    release_notes: str = Field(default="")
    protection_payload_key: str = Field(default="")


class MarketPackageReviewRequest(BaseModel):
    package_id: str = Field(min_length=1)
    version: str = Field(min_length=1)
    action: str = Field(min_length=1)
    comment: str = Field(default="")


class MarketDownloadTokenResponse(BaseModel):
    package_id: str
    version: str
    download_url: str
    expires_in: int = 300


class MarketPackageAccessResponse(BaseModel):
    success: bool = True
    package_id: str
    version: str
    access_mode: str = Field(default="run")
    payload_key: str = Field(default="")
    expires_in: int = Field(default=120)


class MarketPackageListResponse(BaseModel):
    items: List[MarketPackageVersionSummary] = Field(default_factory=list)
    total: int = 0


class MarketAdminPackageListResponse(BaseModel):
    items: List[MarketAdminPackageVersionSummary] = Field(default_factory=list)
    total: int = 0
