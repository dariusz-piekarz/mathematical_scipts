"""Actual Chromium smoke check of Explorer, reader and graph against the canonical index.

Run after building data/biblioteka.db: python tests/browser_ci_e2e.py.
Requires: pip install playwright; python -m playwright install chromium.
No changes to chapter sources or database are made.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
import urllib.request

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
PORT = int(os.environ.get("MATLIB_E2E_PORT", "18766"))
URL = f"http://127.0.0.1:{PORT}"


def wait_for_server(proc: subprocess.Popen, timeout: float = 30.0) -> dict:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if proc.poll() is not None:
            raise RuntimeError(f"API terminated before readiness (exit {proc.returncode})")
        try:
            with urllib.request.urlopen(URL + "/api/stats", timeout=1.0) as response:
                if response.status == 200:
                    return json.load(response)
        except (OSError, TimeoutError):
            time.sleep(0.15)
    raise RuntimeError("API did not respond on localhost before deadline")


def main() -> None:
    proc = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "backend.api:app", "--host", "127.0.0.1",
         "--port", str(PORT), "--log-level", "warning"],
        cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
    )
    try:
        stats = wait_for_server(proc)
        assert stats["documents"] > 0, stats
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            try:
                page = browser.new_page(viewport={"width": 1360, "height": 900})
                errors: list[str] = []
                page.on("pageerror", lambda err: errors.append(str(err)))
                response = page.goto(URL, wait_until="networkidle", timeout=30000)
                assert response is not None and response.status == 200
                page.locator("#statPill").filter(
                    has_text=re.compile(r"^\d+ rozdziałów$")
                ).wait_for(timeout=20000)
                displayed = page.locator("#statPill").inner_text()
                assert displayed == f"{stats['documents']} rozdziałów", displayed
                page.locator("#openFirst").click()
                page.locator("#docTitle").wait_for(state="visible", timeout=20000)
                chapter_title = page.locator("#docTitle").inner_text()
                assert chapter_title.strip()
                assert page.locator("#latexSource").inner_text().strip()
                page.locator('[data-tab="graph"]').click()
                page.locator("#view-graph").wait_for(state="visible", timeout=15000)
                assert page.locator("#graphLeft option").count() > 0
                assert page.locator("#graphRight option").count() > 0
                assert not errors, errors
                print(json.dumps({
                    "result": "passed", "indexed_chapters": stats["documents"],
                    "rendered_chapters": displayed, "opened_title": chapter_title,
                    "graph_domains": page.locator("#graphLeft option").count(),
                    "javascript_errors": errors,
                }, ensure_ascii=False))
            finally:
                browser.close()
    finally:
        proc.terminate()
        try:
            proc.communicate(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.communicate(timeout=5)


if __name__ == "__main__":
    main()
