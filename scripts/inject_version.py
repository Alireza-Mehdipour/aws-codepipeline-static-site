import os
from datetime import datetime
from pathlib import Path

def main():
    version = os.getenv("BUILD_VERSION") or datetime.utcnow().strftime("%Y%m%d-%H%M%S-UTC")
    project_root = Path(__file__).resolve().parent.parent
    index_path = project_root / "app" / "index.html"

    html = index_path.read_text(encoding="utf-8")

    marker = 'id="build-version">'
    if marker not in html:
        raise SystemExit("Could not find build-version span in index.html")

    before, after = html.split(marker, 1)
    current_text, rest = after.split("</span>", 1)
    new_after = f"{version}</span>{rest}"
    new_html = before + marker + new_after

    index_path.write_text(new_html, encoding="utf-8")
    print(f"[inject_version] Set build version to: {version}")

if __name__ == "__main__":
    main()