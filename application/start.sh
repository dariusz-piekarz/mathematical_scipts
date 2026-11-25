#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python -m pip install -r requirements.txt
python scripts/install_math_renderer.py || echo "Math renderer unavailable; source view remains available." >&2
exec python -m backend.desktop
