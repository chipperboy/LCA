#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import importlib
import os
import re
import shutil
import sys
import tempfile
from contextlib import contextmanager
from ctypes import WinDLL, c_int
from pathlib import Path

import comtypes.client
import comtypes.typeinfo
from comtypes.tools import codegenerator


PROGIDS = (
    "OlaPlug.OlaSoft",
    "ola.olasoft",
    "ola",
    "olaplug",
    "ola.ola",
)
UIAUTOMATION_TYPELIB = "UIAutomationCore.dll"


def _prepare_clean_dir(target_dir: Path) -> None:
    if target_dir.exists():
        for item in target_dir.iterdir():
            if item.is_dir():
                shutil.rmtree(item, ignore_errors=True)
            else:
                item.unlink(missing_ok=True)
    else:
        target_dir.mkdir(parents=True, exist_ok=True)


def _init_ola_com(dll_path: Path) -> None:
    if not dll_path.exists():
        raise FileNotFoundError(f"missing OLA dll: {dll_path}")

    dll_dir = str(dll_path.parent.resolve())
    os.environ["PATH"] = dll_dir + os.pathsep + os.environ.get("PATH", "")

    dll = WinDLL(str(dll_path))
    dll.InitCom.argtypes = []
    dll.InitCom.restype = c_int
    result = int(dll.InitCom())
    if result == 0:
        raise RuntimeError("InitCom returned 0")


def _create_ola_object() -> object:
    last_error = None
    for progid in PROGIDS:
        try:
            return comtypes.client.CreateObject(progid)
        except Exception as error:
            last_error = error
    raise RuntimeError(f"CreateObject failed for all ProgID candidates: {last_error}")


def _prepare_ola_typelib(dll_path: Path) -> None:
    errors = []
    try:
        with _isolated_comtypes_gen_dir(Path(str(comtypes.client.gen_dir)), type_library=str(dll_path)):
            comtypes.client.GetModule(str(dll_path))
        return
    except Exception as error:
        errors.append(f"GetModule failed for OLA dll: {error}")

    try:
        com_object = _create_ola_object()
        del com_object
        return
    except Exception as error:
        errors.append(f"CreateObject fallback failed: {error}")

    raise RuntimeError("；".join(errors))


def _collect_candidate_files() -> dict:
    files = {}

    for module_name, module in list(sys.modules.items()):
        if not module_name.startswith("comtypes.gen."):
            continue
        module_file = getattr(module, "__file__", None)
        if not module_file:
            continue
        src = Path(module_file)
        if not src.exists():
            continue
        files[src.name] = src

    try:
        gen_dir = Path(str(comtypes.client.gen_dir))
    except Exception:
        gen_dir = None

    if gen_dir and gen_dir.exists():
        for src in gen_dir.glob("*.py"):
            files[src.name] = src

    return files


def _clear_generated_module_cache(module_names: list[str]) -> None:
    import comtypes.gen

    for module_name in module_names:
        normalized_name = str(module_name or "").strip()
        if not normalized_name:
            continue
        full_name = normalized_name
        if not full_name.startswith("comtypes.gen."):
            full_name = f"comtypes.gen.{normalized_name}"
        stem = full_name.split(".")[-1]
        sys.modules.pop(full_name, None)
        if hasattr(comtypes.gen, stem):
            try:
                delattr(comtypes.gen, stem)
            except Exception:
                pass


def _resolve_typelib_module_names(type_library: str) -> list[str]:
    tlib = comtypes.typeinfo.LoadTypeLibEx(str(type_library))
    module_names = [codegenerator.name_wrapper_module(tlib)]
    friendly_name = codegenerator.name_friendly_module(tlib)
    if friendly_name:
        module_names.append(friendly_name)
    return [str(name).strip() for name in module_names if str(name or "").strip()]


@contextmanager
def _isolated_comtypes_gen_dir(gen_dir: Path, *, type_library: str):
    import comtypes.gen

    target_dir = str(gen_dir.resolve())
    previous_paths = list(getattr(comtypes.gen, "__path__", []))
    module_names = _resolve_typelib_module_names(type_library)
    _clear_generated_module_cache(module_names)
    comtypes.gen.__path__ = [target_dir]
    importlib.invalidate_caches()
    try:
        yield
    finally:
        _clear_generated_module_cache(module_names)
        comtypes.gen.__path__ = previous_paths
        importlib.invalidate_caches()


def _copy_files_to_output(files: dict, output_dir: Path) -> None:
    for name, src in files.items():
        destination = (output_dir / name).resolve()
        source = Path(src).resolve()
        if source == destination:
            continue
        shutil.copy2(source, destination)

    init_file = output_dir / "__init__.py"
    if not init_file.exists():
        init_file.write_text("# auto-generated for build packaging\n", encoding="utf-8")


def _extract_wrapper_module_name(friendly_module: Path) -> str:
    content = friendly_module.read_text(encoding="utf-8", errors="ignore")
    match = re.search(
        r"comtypes\.gen\.(_[0-9A-F_]+_0_\d+_0)",
        content,
        flags=re.IGNORECASE,
    )
    if not match:
        raise RuntimeError(f"{friendly_module.name} does not contain wrapper module import")
    return f"{match.group(1)}.py"


def _validate_output(output_dir: Path) -> None:
    required_files = (
        "_00020430_0000_0000_C000_000000000046_0_2_0.py",
        "OLAPlugLib.py",
        "UIAutomationClient.py",
    )
    for name in required_files:
        if not (output_dir / name).exists():
            raise RuntimeError(f"missing required generated file: {name}")

    for friendly_name in ("OLAPlugLib.py", "UIAutomationClient.py"):
        friendly_module = output_dir / friendly_name
        wrapper_module_file = output_dir / _extract_wrapper_module_name(friendly_module)
        if not wrapper_module_file.exists():
            raise RuntimeError(f"missing wrapper module file: {wrapper_module_file.name}")


def _prepare_uiautomation_typelib() -> None:
    with _isolated_comtypes_gen_dir(
        Path(str(comtypes.client.gen_dir)),
        type_library=UIAUTOMATION_TYPELIB,
    ):
        comtypes.client.GetModule(UIAUTOMATION_TYPELIB)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Pre-generate required comtypes.gen modules and export them for packaging"
    )
    parser.add_argument("--output", required=True, help="output directory for generated comtypes/gen files")
    parser.add_argument("--dll", required=True, help="path to OLAPlug_x64.dll")
    args = parser.parse_args()

    output_dir = Path(args.output).resolve()
    dll_path = Path(args.dll).resolve()
    temp_output_dir = Path(
        tempfile.mkdtemp(prefix=f"{output_dir.name}_tmp_", dir=str(output_dir.parent))
    ).resolve()

    try:
        _prepare_clean_dir(temp_output_dir)

        _init_ola_com(dll_path)
        comtypes.client.gen_dir = str(temp_output_dir)
        _prepare_ola_typelib(dll_path)
        _prepare_uiautomation_typelib()

        collected = _collect_candidate_files()
        _copy_files_to_output(collected, temp_output_dir)
        _validate_output(temp_output_dir)

        _prepare_clean_dir(output_dir)
        _copy_files_to_output(collected, output_dir)
        _validate_output(output_dir)

        exported_files = sorted(p.name for p in output_dir.glob("*.py"))
        print(f"Prepared comtypes gen files: {len(exported_files)}")
        for name in exported_files:
            print(f"  - {name}")
        return 0
    finally:
        shutil.rmtree(temp_output_dir, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())
