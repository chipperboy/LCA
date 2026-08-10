# -*- coding: utf-8 -*-

from __future__ import annotations

from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship


def register_market_models(base_cls):
    class MarketPackage(base_cls):
        __tablename__ = "market_packages"

        id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
        package_id: Mapped[str] = mapped_column(String(128), unique=True, index=True, nullable=False)
        title: Mapped[str] = mapped_column(String(255), nullable=False)
        category: Mapped[str] = mapped_column(String(64), default="", nullable=False)
        summary: Mapped[str] = mapped_column(Text, default="", nullable=False)
        author_name: Mapped[str] = mapped_column(String(128), default="", nullable=False)
        owner_user_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("users.id"), nullable=True, index=True)
        latest_version: Mapped[str] = mapped_column(String(64), default="", nullable=False)
        visibility: Mapped[str] = mapped_column(String(32), default="private", nullable=False)
        is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
        created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
        updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

        versions = relationship("MarketPackageVersion", back_populates="package", cascade="all, delete-orphan")

    class MarketPackageVersion(base_cls):
        __tablename__ = "market_package_versions"

        id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
        package_id_fk: Mapped[int] = mapped_column(Integer, ForeignKey("market_packages.id"), nullable=False, index=True)
        version: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
        status: Mapped[str] = mapped_column(String(32), default="draft", nullable=False)
        manifest_json: Mapped[str] = mapped_column(Text, default="{}", nullable=False)
        changelog: Mapped[str] = mapped_column(Text, default="", nullable=False)
        release_notes: Mapped[str] = mapped_column(Text, default="", nullable=False)
        storage_path: Mapped[str] = mapped_column(String(512), default="", nullable=False)
        file_sha256: Mapped[str] = mapped_column(String(128), default="", nullable=False)
        file_size: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
        protection_mode: Mapped[str] = mapped_column(String(64), default="", nullable=False)
        protection_payload_key: Mapped[str] = mapped_column(Text, default="", nullable=False)
        cover_path: Mapped[str] = mapped_column(String(512), default="", nullable=False)
        review_comment: Mapped[str] = mapped_column(Text, default="", nullable=False)
        created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
        reviewed_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
        published_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)

        package = relationship("MarketPackage", back_populates="versions")

    class MarketUserAsset(base_cls):
        __tablename__ = "market_user_assets"

        id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
        user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False, index=True)
        package_version_id: Mapped[int] = mapped_column(Integer, ForeignKey("market_package_versions.id"), nullable=False, index=True)
        grant_type: Mapped[str] = mapped_column(String(32), default="owned", nullable=False)
        created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
        expires_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    class MarketDownloadLog(base_cls):
        __tablename__ = "market_download_logs"

        id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
        user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=True, index=True)
        package_id: Mapped[str] = mapped_column(String(128), nullable=False, index=True)
        version: Mapped[str] = mapped_column(String(64), nullable=False)
        hardware_id: Mapped[str] = mapped_column(String(255), default="", nullable=False)
        ip_address: Mapped[str] = mapped_column(String(128), default="", nullable=False)
        created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    class MarketReviewRecord(base_cls):
        __tablename__ = "market_review_records"

        id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
        package_id: Mapped[str] = mapped_column(String(128), nullable=False, index=True)
        version: Mapped[str] = mapped_column(String(64), nullable=False)
        reviewer: Mapped[str] = mapped_column(String(128), default="", nullable=False)
        action: Mapped[str] = mapped_column(String(32), nullable=False)
        comment: Mapped[str] = mapped_column(Text, default="", nullable=False)
        created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    return {
        "MarketPackage": MarketPackage,
        "MarketPackageVersion": MarketPackageVersion,
        "MarketUserAsset": MarketUserAsset,
        "MarketDownloadLog": MarketDownloadLog,
        "MarketReviewRecord": MarketReviewRecord,
    }
