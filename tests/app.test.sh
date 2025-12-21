#!/usr/bin/env bash
set -euo pipefail

echo "[TEST] Checking required files exist..."

if [ ! -f "app/index.html" ]; then
  echo "[TEST] ❌ app/index.html not found"
  exit 1
fi

if [ ! -f "app/style.css" ]; then
  echo "[TEST] ❌ app/style.css not found"
  exit 1
fi

if ! grep -q 'id="build-version"' app/index.html; then
  echo "[TEST] ❌ build-version span not found in index.html"
  exit 1
fi

echo "[TEST] ✅ All basic checks passed."