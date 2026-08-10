"""
Generate the release manifest for the packaged installer.
The version is read from app_core/app_config.py.
"""

import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, PROJECT_ROOT)

from app_core.app_config import APP_VERSION
from utils.generate_manifest import ManifestGenerator


RELEASE_OUTPUT_DIRNAME = "release_output"


def main():
    packaging_dir = os.path.dirname(os.path.abspath(__file__))
    release_dir = os.path.join(packaging_dir, RELEASE_OUTPUT_DIRNAME)

    if not os.path.exists(release_dir):
        print(f"Error: release output directory not found: {release_dir}")
        print(r"Run build_assets\packaging\build_release.bat first.")
        sys.exit(1)

    print(f"Version: {APP_VERSION}")
    print(f"Release dir: {release_dir}")
    print()

    print("Enter changelog lines, then submit an empty line:")
    changelog = []
    while True:
        line = input().strip()
        if not line:
            break
        changelog.append(line)

    if not changelog:
        changelog = [f"Version {APP_VERSION} update"]
        print("No changelog provided, using default entry.")

    generator = ManifestGenerator(release_dir=release_dir, version=APP_VERSION)
    output_file = os.path.join(release_dir, "manifest.json")
    generator.generate_manifest(changelog=changelog, output_file=output_file)


if __name__ == "__main__":
    main()
