#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import argparse
import importlib.machinery
import re
from pathlib import Path


REQUIRED_FRIENDLY_MODULES = (
    "OLAPlugLib.py",
    "UIAutomationClient.py",
)
REQUIRED_BASE_MODULES = (
    "_00020430_0000_0000_C000_000000000046_0_2_0.py",
)
WRAPPER_IMPORT_PATTERN = re.compile(
    r"comtypes\.gen\.(_[0-9A-F_]+_0_\d+_0)",
    flags=re.IGNORECASE,
)


def _module_exists(gen_dir: Path, module_name: str) -> bool:
    suffixes = tuple(importlib.machinery.SOURCE_SUFFIXES + importlib.machinery.BYTECODE_SUFFIXES)
    for suffix in suffixes:
        if (gen_dir / f"{module_name}{suffix}").is_file():
            return True

    pycache_dir = gen_dir / "__pycache__"
    if pycache_dir.is_dir():
        for suffix in importlib.machinery.BYTECODE_SUFFIXES:
            if any(pycache_dir.glob(f"{module_name}.*{suffix}")):
                return True
    return False


def _find_source_module(gen_dir: Path, module_name: str) -> Path | None:
    candidate = gen_dir / f"{module_name}.py"
    if candidate.is_file():
        return candidate
    return None


def _scan_wrapper_modules(gen_dir: Path) -> set[str]:
    wrappers: set[str] = set()
    for root in (gen_dir, gen_dir / "__pycache__"):
        if not root.is_dir():
            continue
        for path in root.iterdir():
            if not path.is_file():
                continue
            stem = path.stem
            if ".cpython-" in stem:
                stem = stem.split(".cpython-", 1)[0]
            if re.fullmatch(r"_[0-9A-F_]+_0_\d+_0", stem, flags=re.IGNORECASE):
                wrappers.add(stem)
    return wrappers


def _extract_wrapper_modules(friendly_module: Path) -> set[str]:
    content = friendly_module.read_text(encoding="utf-8", errors="ignore")
    return {match.group(1) for match in WRAPPER_IMPORT_PATTERN.finditer(content)}


def verify_comtypes_gen(gen_dir: Path) -> list[str]:
    errors: list[str] = []
    if not gen_dir.is_dir():
        return [f"missing comtypes gen directory: {gen_dir}"]

    for name in REQUIRED_BASE_MODULES:
        if not _module_exists(gen_dir, Path(name).stem):
            errors.append(f"missing base module: {name}")

    all_wrapper_modules = _scan_wrapper_modules(gen_dir)
    for filename in REQUIRED_FRIENDLY_MODULES:
        module_name = Path(filename).stem
        if not _module_exists(gen_dir, module_name):
            errors.append(f"missing friendly module: {filename}")
            continue

        friendly_module = _find_source_module(gen_dir, module_name)
        if friendly_module is None:
            if not all_wrapper_modules:
                errors.append(f"{filename} has no source file and no generated wrapper modules were found")
            continue

        wrapper_modules = _extract_wrapper_modules(friendly_module)
        if not wrapper_modules and not all_wrapper_modules:
            errors.append(f"{filename} does not import a generated wrapper module")
            continue

        for wrapper_name in sorted(wrapper_modules):
            if not _module_exists(gen_dir, wrapper_name):
                errors.append(f"{filename} references missing wrapper module: {wrapper_name}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify packaged comtypes.gen files")
    parser.add_argument("--gen-dir", required=True, help="directory containing comtypes.gen *.py files")
    args = parser.parse_args()

    gen_dir = Path(args.gen_dir).resolve()
    errors = verify_comtypes_gen(gen_dir)
    if errors:
        print(f"Invalid comtypes gen directory: {gen_dir}")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"Verified comtypes gen directory: {gen_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
