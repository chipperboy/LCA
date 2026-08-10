#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
import py_compile
import shutil
import sys
from pathlib import Path

REQUIRED_SOURCE_FILES = (
    "__init__.py",
    "OLAPlugLib.py",
    "UIAutomationClient.py",
    "_00020430_0000_0000_C000_000000000046_0_2_0.py",
)

PYC_INVALIDATION_MODE = getattr(py_compile, "PycInvalidationMode", None)


def _prepare_clean_dir(target_dir: Path) -> None:
    if target_dir.exists():
        shutil.rmtree(target_dir, ignore_errors=True)
    target_dir.mkdir(parents=True, exist_ok=True)


def _compile_source_to_pyc(source_file: Path, output_file: Path) -> None:
    compile_kwargs = {
        "file": str(source_file),
        "cfile": str(output_file),
        "dfile": f"comtypes/gen/{source_file.name}",
        "doraise": True,
    }
    if PYC_INVALIDATION_MODE is not None:
        compile_kwargs["invalidation_mode"] = PYC_INVALIDATION_MODE.UNCHECKED_HASH
    py_compile.compile(**compile_kwargs)


def _validate_source_dir(source_dir: Path) -> None:
    if not source_dir.is_dir():
        raise FileNotFoundError(f"缺少 comtypes 预生成目录: {source_dir}")
    for name in REQUIRED_SOURCE_FILES:
        if not (source_dir / name).is_file():
            raise FileNotFoundError(f"缺少必要的 comtypes 预生成文件: {name}")


def _validate_output_dir(output_dir: Path) -> None:
    for name in REQUIRED_SOURCE_FILES:
        compiled_name = Path(name).with_suffix(".pyc").name
        if not (output_dir / compiled_name).is_file():
            raise FileNotFoundError(f"缺少必要的 comtypes 字节码文件: {compiled_name}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Compile pre-generated comtypes modules into sourceless .pyc files")
    parser.add_argument("--source-dir", required=True, help="Source directory containing generated comtypes .py files")
    parser.add_argument("--dist", required=True, help="Packaged dist directory")
    args = parser.parse_args()

    source_dir = Path(args.source_dir).resolve(strict=False)
    dist_root = Path(args.dist).resolve(strict=False)
    target_dir = dist_root / "comtypes" / "gen"

    _validate_source_dir(source_dir)
    if not dist_root.is_dir():
        raise FileNotFoundError(f"缺少打包输出目录: {dist_root}")

    _prepare_clean_dir(target_dir)

    compiled_files: list[str] = []
    for source_file in sorted(source_dir.glob("*.py")):
        output_file = target_dir / f"{source_file.stem}.pyc"
        _compile_source_to_pyc(source_file, output_file)
        compiled_files.append(output_file.name)

    _validate_output_dir(target_dir)
    print(f"Prepared packaged comtypes bytecode files: {len(compiled_files)}")
    for name in compiled_files:
        print(f"  - {name}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        detail = str(exc).strip() or exc.__class__.__name__
        print(f"ERROR: {detail}", file=sys.stderr)
        raise SystemExit(1)
