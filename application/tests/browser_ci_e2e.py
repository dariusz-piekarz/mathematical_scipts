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
import sqlite3
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
                # Choose an existing, unambiguous reference actually displayed
                # in the first 32,000 characters of a canonical chapter.
                with sqlite3.connect(ROOT / "data" / "biblioteka.db") as db:
                    reference = db.execute("""
                        SELECT r.source_document, r.target_label
                        FROM references_tex AS r
                        WHERE r.status='resolved' AND r.target_document IS NOT NULL
                          AND r.offset < 30000
                          AND NOT EXISTS (
                              SELECT 1 FROM label_conflicts AS c
                              WHERE c.name=r.target_label
                          )
                          AND EXISTS (
                              SELECT 1 FROM labels AS l
                              WHERE l.name=r.target_label
                          )
                        ORDER BY r.source_document, r.offset
                        LIMIT 1
                    """).fetchone()
                assert reference is not None, "No unambiguous visible reference"
                source_id, target_label = reference
                page.evaluate("(moduleId) => openModule(moduleId)", source_id)
                source_ref = page.locator("#latexSource .ref-link").filter(
                    has_text=target_label
                ).first
                source_ref.wait_for(state="visible", timeout=15000)
                source_ref.hover()
                tip = page.locator("#referenceTip")
                tip.wait_for(state="visible", timeout=15000)
                assert target_label in page.locator("#tipBody").inner_text()
                assert page.locator("#tipBody .tip-code").inner_text().strip()
                page.locator("#tipOpen").click()
                page.locator("#docTitle").wait_for(state="visible", timeout=15000)
                assert page.locator("#docTitle").inner_text().strip()
                # Negative paths: use actual ambiguity and missing-label evidence
                # from the freshly built canonical index; never invent owners.
                with sqlite3.connect(ROOT / "data" / "biblioteka.db") as db:
                    ambiguous = db.execute("""
                        SELECT name FROM label_conflicts
                        GROUP BY name HAVING COUNT(DISTINCT document_id)>1
                        ORDER BY name LIMIT 1
                    """).fetchone()
                    missing = db.execute("""
                        SELECT r.target_label FROM references_tex AS r
                        WHERE r.target_document IS NULL
                          AND NOT EXISTS (SELECT 1 FROM labels l WHERE l.name=r.target_label)
                          AND NOT EXISTS (SELECT 1 FROM label_conflicts c WHERE c.name=r.target_label)
                        ORDER BY r.target_label LIMIT 1
                    """).fetchone()
                assert ambiguous is not None, "No ambiguous labels in indexed corpus"
                assert missing is not None, "No missing labels in indexed corpus"
                ambiguous_label, missing_label = ambiguous[0], missing[0]
                anchor_id = "docTitle"
                page.evaluate(
                    "([label, anchorId]) => previewLabel(label, document.getElementById(anchorId))",
                    [ambiguous_label, anchor_id],
                )
                page.locator("#tipBody .ref-choice").first.wait_for(state="visible",timeout=15000)
                assert "Etykieta występuje w kilku rozdziałach" in page.locator("#tipBody").inner_text()
                assert page.locator("#tipOpen").is_disabled()
                assert page.locator("#tipBody .ref-choice").count() >= 2
                selected_owner = page.locator("#tipBody .ref-choice").first.inner_text().split(": ",1)[0]
                page.locator("#tipBody .ref-choice").first.click()
                page.wait_for_function(
                    "(id) => document.getElementById('docBreadcrumb').textContent.includes(id)",
                    selected_owner, timeout=15000,
                )
                page.evaluate(
                    "([label, anchorId]) => previewLabel(label, document.getElementById(anchorId))",
                    [missing_label, anchor_id],
                )
                page.locator("#referenceTip").wait_for(state="visible")
                assert "Nie znaleziono cytowanej etykiety" in page.locator("#tipBody").inner_text()
                assert missing_label in page.locator("#tipBody").inner_text()
                assert page.locator("#tipOpen").is_disabled()
                # Hold the first successful fetch artificially; an immediate
                # 404 must win and the late successful response must be ignored.
                page.evaluate("""(slowLabel) => {
                    const originalFetch = window.fetch.bind(window);
                    window.fetch = async (...args) => {
                        const response = await originalFetch(...args);
                        if (String(args[0]).includes('/api/labels/' + encodeURIComponent(slowLabel))) {
                            await new Promise(resolve => setTimeout(resolve, 400));
                        }
                        return response;
                    };
                }""", target_label)
                page.evaluate("""async ([slow, fast]) => {
                    const anchor = document.getElementById('docTitle');
                    const first = previewLabel(slow, anchor);
                    const second = previewLabel(fast, anchor);
                    await Promise.allSettled([first, second]);
                }""", [target_label, missing_label])
                assert "Nie znaleziono cytowanej etykiety" in page.locator("#tipBody").inner_text()
                assert missing_label in page.locator("#tipBody").inner_text()
                assert target_label not in page.locator("#tipBody").inner_text()
                assert not errors, errors
                print(json.dumps({
                    "result": "passed", "indexed_chapters": stats["documents"],
                    "rendered_chapters": displayed, "opened_title": chapter_title,
                    "graph_domains": page.locator("#graphLeft option").count(),
                    "reference_preview": {"source": source_id, "label": target_label},
                    "ambiguous_label": ambiguous_label, "missing_label": missing_label,
                    "stale_response_suppressed": True,
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
