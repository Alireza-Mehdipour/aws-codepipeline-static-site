import os
import sys
from datetime import datetime, timezone
from pathlib import Path


def main():
    version = os.getenv("BUILD_VERSION") or datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S-UTC")

    project_root = Path(__file__).resolve().parent.parent

    # Target the built output by default, not the source.
    # Pass a path as the first argument to override.
    if len(sys.argv) > 1:
        index_path = Path(sys.argv[1])
    else:
        index_path = project_root / "dist" / "index.html"

    if not index_path.exists():
        raise SystemExit(f"[inject_version] File not found: {index_path}")

    html = index_path.read_text(encoding="utf-8")

    marker = 'id="build-version">'
    if marker not in html:
        raise SystemExit(f"[inject_version] Could not find build-version span in {index_path}")

    before, after = html.split(marker, 1)
    _current_text, rest = after.split("</span>", 1)
    new_html = f"{before}{marker}{version}</span>{rest}"

    index_path.write_text(new_html, encoding="utf-8")
    print(f"[inject_version] Set build version to {version} in {index_path}")


if __name__ == "__main__":
    main()
