#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python -m pip install -r requirements.txt
python scripts/install_math_renderer.py || echo "Math renderer unavailable; source view remains available." >&2
python -m uvicorn backend.api:app --host 127.0.0.1 --port 8765
