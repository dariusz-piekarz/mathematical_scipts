"""Optional Chromium smoke test for draft generation and X-close cleanup.

Requires playwright+Chromium. Run: python tests/browser_workspace_e2e.py
"""
from __future__ import annotations

import os
import sys
import sys
from pathlib import Path
import subprocess
import tempfile
import time
import urllib.request

from playwright.sync_api import sync_playwright

APP = Path(__file__).resolve().parents[1]


def main():
    with tempfile.TemporaryDirectory() as temp:
        drafts = Path(temp) / "drafts"
        saved = Path(temp) / "saved"
        env = dict(os.environ, MATLIB_DRAFTS_ROOT=str(drafts), MATLIB_SAVED_ROOT=str(saved))
        server = subprocess.Popen([sys.executable, "-m", "uvicorn", "backend.api:app", "--host", "127.0.0.1", "--port", "18765"],
                                  cwd=APP, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        try:
            for i in range(50):
                try:
                    with urllib.request.urlopen("http://127.0.0.1:18767/api/health", timeout=1) as res:
                        if res.status == 200:
                            break
                except (OSError, TimeoutError):
                    time.sleep(0.15)
            else:
                raise RuntimeError("FastAPI failed to start")
            with sync_playwright() as playwright:
                browser = playwright.chromium.launch(headless=True, args=["--no-sandbox"])
                try:
                    page = browser.new_page()
                    page.goto("http://127.0.0.1:18767/", wait_until="networkidle")
                    page.locator("#openFirst").click()
                    page.locator("#addCurrent").click()
                    page.locator('[data-tab="selection"]').click()
                    page.locator("#generatorTitle").fill("Browser close test")
                    page.locator("#createDraft").click()
                    page.locator("#draftResult strong").wait_for(timeout=15000)
                    assert list(drafts.glob("*/project.zip")), "No temporary draft created"
                    page.locator("#draftResult button", has_text="Zapisz na stałe").click()
                    page.locator("#savedProjects .saved-project-item").first.wait_for(timeout=15000)
                    assert list(saved.glob("*.zip")), "Saved project not persisted"
                    page.close(run_before_unload=True)  # Exercise the browser tab-close lifecycle
                    for _ in range(50):
                        if not list(drafts.glob("*/project.zip")):
                            break
                        time.sleep(0.1)
                    assert not list(drafts.glob("*/project.zip")), "X-close failed to delete draft"
                    assert list(saved.glob("*.zip")), "Closing tab removed saved project"
                finally:
                    browser.close()
        finally:
            server.terminate()
            try:
                server.communicate(timeout=8)
            except subprocess.TimeoutExpired:
                server.kill()
        print("PASS: create draft, save project, close browser X, remove draft, retain saved ZIP")


if __name__ == "__main__":
    main()
