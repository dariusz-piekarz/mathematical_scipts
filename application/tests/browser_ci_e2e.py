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
        env={**os.environ, "MATLIB_LEAN_RUN": "0"},
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
                # Verify actual KaTeX output, not merely the presence of script tags.
                assert page.evaluate("typeof window.renderMathInElement") == "function"
                assert page.evaluate(r"() => previewMacros('MOD-01')['\\Q']") == r"\mathrm Q"
                assert page.evaluate(r"() => previewMacros('DG-01')['\\Q']") == r"\mathbb{Q}"
                assert page.evaluate(r"() => previewMacros('KAT-01')['\\Hom']") == r"\operatorname{Hom}"
                page.locator("#togglePreview").click()
                page.evaluate(r"() => renderSimplified('Inline $\\R^2$; \\[\\frac{1}{2}\\] \\begin{align}x&=1\\\\y&=2\\end{align}', 'DG-01')")
                assert page.locator("#simplified .katex").count() == 3
                assert page.locator("#simplified .katex-display").count() == 2
                assert page.locator("#mathPreviewStatus").is_hidden()
                page.evaluate(r"() => renderSimplified('$\\unknownAtlasMacro$ $x^2$')")
                assert page.locator("#mathPreviewStatus").is_visible()
                assert page.locator("#simplified .katex").count() == 1
                # Deterministic API response, real UI and real renderer.
                page.route("**/api/labels/atlas-math-preview-test", lambda route: route.fulfill(json={"entity_title": "Test", "document_id": "TEST", "line": 1, "latex": r"Test $x^2$ and \[\frac{1}{2}\]"}))
                page.evaluate("() => previewLabel('atlas-math-preview-test', document.getElementById('docTitle'))")
                page.locator("#tipBody .tip-code .katex").first.wait_for(state="attached", timeout=10000)
                assert page.locator("#tipBody .tip-code .katex").count() == 2
                page.evaluate("() => closeTip()")
                page.unroute("**/api/labels/atlas-math-preview-test")
                # Ground performance measurements in actual indexed mathematical text.
                samples = []
                with sqlite3.connect(ROOT / "data" / "biblioteka.db") as math_db:
                    for module, label in (
                        ("DG-01", "def dyfeo"),
                        ("KAT-03", "cat:ex:spec-functor"),
                    ):
                        row = math_db.execute(
                            "SELECT d.content,e.start_offset,e.end_offset "
                            "FROM label_occurrences l JOIN entities e ON e.id=l.entity_id "
                            "JOIN documents d ON d.id=l.document_id "
                            "WHERE l.document_id=? AND l.name=?", (module, label)
                        ).fetchone()
                        assert row is not None, (module, label)
                        latex = row[0][row[1]:row[2]]
                        result = page.evaluate("""([latex, module]) => {
                            const start = performance.now();
                            renderSimplified(latex, module);
                            const box = document.getElementById('simplified');
                            return {elapsed_ms: performance.now()-start,
                                formulas: box.querySelectorAll('.katex').length,
                                message: document.getElementById('mathPreviewStatus').textContent};
                        }""", [latex, module])
                        assert result["formulas"] > 0, (module, label, result)
                        samples.append({"module": module, "label": label, "characters": len(latex), **result})
                print(json.dumps({"math_preview_samples": samples}, ensure_ascii=False), flush=True)
                page.locator("#togglePreview").click()
                # Full browser-to-API Lean contract: exact indexed theorem,
                # exact whole-line selection, missing partial span and safe runner.
                with sqlite3.connect(ROOT / "data" / "biblioteka.db") as db:
                    theorem = db.execute("""
                        SELECT e.id,e.start_line,e.end_line,e.start_offset,e.end_offset,
                               d.content
                        FROM entities e
                        JOIN labels l ON l.entity_id=e.id
                        JOIN documents d ON d.id=e.document_id
                        WHERE d.id='LST-01' AND l.name='thm:de-morgan-logic'
                        LIMIT 1
                    """).fetchone()
                assert theorem is not None, "Registered Lean source theorem missing"
                entity_id, first, last, begin, finish, source = theorem
                assert first < last, "Expected multiline theorem for negative selection"
                page.evaluate("(entity) => openEntity(entity, true)", entity_id)
                page.wait_for_function(
                    "(entity) => state.currentEntity===entity && !!state.currentData",
                    arg=entity_id, timeout=15000,
                )
                page.locator("#openLeanCurrent").click()
                page.wait_for_function(
                    "() => state.leanFragment?.formalization_id==='lst01-de-morgan'",
                    timeout=15000,
                )
                assert page.locator("#leanLatex").text_content() == source[begin:finish]
                assert "inductive Formula" in page.locator("#leanCode").text_content()
                assert page.evaluate("state.leanFragment.formalization_status") == "ready"
                assert page.evaluate("state.leanFragment.statement_status") == "approved"
                assert page.evaluate("state.leanFragment.certificate") is False
                assert page.locator("#leanRun").is_disabled()
                # L1.5.2: prepare an offline package even with runner disabled.
                old_code = page.locator("#leanCode").text_content()
                assert page.locator("#leanTranscriptionPrepare").is_disabled()
                assert not page.locator("#leanTranscriptionConsent").is_checked()
                page.locator("#leanTranscriptionConsent").check()
                page.locator("#leanTranscriptionPrepare").click()
                page.wait_for_function(
                    "() => document.querySelector('#leanTranscriptionStatus').textContent.includes('Nie wygenerowano kodu Lean')",
                    timeout=20000,
                )
                packet = page.evaluate("JSON.parse(document.querySelector('#leanTranscriptionPackage').textContent)")
                assert packet["source_entity"] == entity_id
                assert packet["source_latex"] == source[begin:finish]
                assert packet["source_sha256"] == page.evaluate("state.leanFragment.source_sha256")
                assert packet["candidate_status"] == "not_generated"
                assert packet["certificate"] is False
                assert packet["external_transfer_allowed"] is False
                assert packet["external_cost_minor_units"] == 0
                assert page.locator("#leanCode").text_content() == old_code
                assert page.locator("#leanRun").is_disabled()
                assert not page.locator("#leanTranscriptionConsent").is_checked()
                assert page.locator("#leanTranscriptionPrepare").is_disabled()
                page.evaluate("(entity) => loadLeanFragment({entity_id:entity})", entity_id)
                page.wait_for_function(
                    "() => state.leanFragment?.formalization_id==='lst01-de-morgan'",
                    timeout=15000,
                )
                assert page.locator("#leanTranscriptionPackage").text_content() == ""
                assert not page.locator("#leanTranscriptionConsent").is_checked()
                # L1.5.2 acceptance: unregistered theorem and labelled non-theorem.
                with sqlite3.connect(ROOT / "data" / "biblioteka.db") as db:
                    def labelled_candidates(kind):
                        return db.execute("""
                            SELECT e.id, e.start_offset, e.end_offset, d.content
                            FROM entities e
                            JOIN labels l ON l.entity_id=e.id
                            JOIN documents d ON d.id=e.document_id
                            WHERE e.kind=? AND e.id != ?
                              AND (SELECT count(*) FROM labels ll
                                   WHERE ll.entity_id=e.id)=1
                            ORDER BY CASE WHEN d.id='LST-01' THEN 0
                                          WHEN d.id='LST-02' THEN 1
                                          WHEN d.id='LA-01' THEN 2 ELSE 3 END,
                                     d.id, e.start_line, e.id
                            LIMIT 100
                        """, (kind, entity_id)).fetchall()
                    theorem_candidates = labelled_candidates("theorem")
                    other_candidates = labelled_candidates("definition")

                def unregistered_exact(candidates):
                    for candidate_id, start, end, document in candidates:
                        candidate_source = document[start:end]
                        if len(candidate_source.encode("utf-8")) > 32768:
                            continue
                        response = page.request.get(URL + "/api/lean/fragment",
                                                    params={"entity_id": candidate_id})
                        if not response.ok:
                            continue
                        fragment = response.json()
                        if (fragment["source_linkage"] == "exact_entity"
                                and fragment["source_entity"] == candidate_id
                                and fragment["formalization_status"] == "missing"
                                and len(fragment["source_labels"]) == 1):
                            return candidate_id, candidate_source
                    raise AssertionError("No suitable labelled unregistered canonical object")

                new_id, new_source = unregistered_exact(theorem_candidates)
                definition_id, _ = unregistered_exact(other_candidates)
                posts = []
                def record_lean_post(request):
                    if request.method == "POST" and "/api/lean/" in request.url:
                        posts.append(request.url)
                page.on("request", record_lean_post)
                # Consent attached to A must not survive the switch to B.
                page.locator("#leanTranscriptionConsent").check()
                page.evaluate("(id) => { void loadLeanFragment({entity_id:id}); }", new_id)
                page.wait_for_function(
                    "(id) => state.leanFragment?.source_entity===id",
                    arg=new_id, timeout=15000,
                )
                assert page.evaluate("state.leanFragment.formalization_id") is None
                assert page.locator("#leanLatex").text_content() == new_source
                assert page.locator("#leanTranscriptionPackage").text_content() == ""
                assert not page.locator("#leanTranscriptionConsent").is_checked()
                assert page.locator("#leanTranscriptionPrepare").is_disabled()
                assert not page.locator("#leanTranscriptionConsent").is_disabled()
                page.locator("#leanTranscriptionConsent").check()
                page.locator("#leanTranscriptionPrepare").click()
                page.wait_for_function(
                    "() => document.querySelector('#leanTranscriptionStatus').textContent.includes('Nie wygenerowano kodu Lean')",
                    timeout=20000,
                )
                new_packet = page.evaluate("JSON.parse(document.querySelector('#leanTranscriptionPackage').textContent)")
                assert new_packet["source_entity"] == new_id
                assert new_packet["source_latex"] == new_source
                assert new_packet["candidate_status"] == "not_generated"
                assert page.evaluate("state.leanFragment.lean_code") is None
                assert page.locator("#leanRun").is_disabled()
                page.evaluate("(id) => { void loadLeanFragment({entity_id:id}); }", definition_id)
                page.wait_for_function(
                    "(id) => state.leanFragment?.source_entity===id",
                    arg=definition_id, timeout=15000,
                )
                assert page.locator("#leanTranscriptionPackage").text_content() == ""
                assert not page.locator("#leanTranscriptionConsent").is_checked()
                # UI permits an exact labelled object; backend must fail closed.
                page.locator("#leanTranscriptionConsent").check()
                page.locator("#leanTranscriptionPrepare").click()
                page.wait_for_function(
                    "() => document.querySelector('#leanTranscriptionStatus').textContent.includes('Eksperyment wymaga pełnego twierdzenia')",
                    timeout=20000,
                )
                assert page.locator("#leanTranscriptionPackage").text_content() == ""
                assert posts == [URL + "/api/lean/transcription/prepare"] * 2, posts
                page.remove_listener("request", record_lean_post)
                page.evaluate("(id) => { void loadLeanFragment({entity_id:id}); }", entity_id)
                page.wait_for_function(
                    "() => state.leanFragment?.formalization_id==='lst01-de-morgan'",
                    timeout=15000,
                )
                # L1.4: real read-only chapter report, separate from proof status.
                page.locator("#leanChapterReportCurrent").click()
                page.wait_for_function(
                    "() => document.querySelector('#leanChapterReportSummary').textContent.includes('nie jest certyfikatem')",
                    timeout=20000,
                )
                assert page.locator("#leanChapterModule").input_value() == "LST-01"
                actual_report = page.request.get(URL + "/api/lean/chapter-report?module_id=LST-01")
                assert actual_report.ok
                report = actual_report.json()
                assert report["certificate"] is False
                assert report["proof_status_included"] is False
                summary = page.locator("#leanChapterReportSummary").inner_text()
                assert report["source_document_sha256"] in summary
                assert str(report["total"]) + " rejestracji" in summary
                assert page.locator("#leanChapterReportItems p").count() == report["total"]
                page.locator("#leanChapterModule").fill("NONEXISTENT-999")
                assert page.locator("#leanChapterReportItems p").count() == 0
                page.locator("#leanChapterReportLoad").click()
                page.wait_for_function(
                    "() => document.querySelector('#leanChapterReportSummary').textContent.includes('Nie można wczytać raportu')",
                    timeout=20000,
                )
                assert page.locator("#leanChapterReportItems p").count() == 0
                page.locator("#leanChapterReportCurrent").click()
                page.wait_for_function(
                    "() => document.querySelector('#leanChapterReportSummary').textContent.includes('nie jest certyfikatem')",
                    timeout=20000,
                )
                blocked = page.request.post(URL + "/api/lean/run",
                                            data={"formalization_id": "lst01-de-morgan"})
                assert blocked.status == 200
                assert blocked.json()["proof_status"] == "blocked"
                assert blocked.json()["certificate"] is False

                # Actual DOM text selection exercises the shared coordinate
                # adapter, including the entity-relative -> module-absolute map.
                page.evaluate("() => activateTab('reader')")
                page.evaluate("""() => {
                    const sourceNode = document.getElementById('latexSource');
                    const selected = document.createRange();
                    selected.selectNodeContents(sourceNode);
                    const selection = window.getSelection();
                    selection.removeAllRanges();
                    selection.addRange(selected);
                    openLeanSelection();
                }""")
                page.wait_for_function(
                    "() => state.leanFragment?.formalization_id==='lst01-de-morgan' && state.leanFragment?.source_linkage==='contains_theorem'",
                    timeout=15000,
                )
                expected_entity_lines = "".join(source.splitlines(keepends=True)[first-1:last])
                assert page.locator("#leanLatex").text_content() == expected_entity_lines
                assert page.locator("#leanTranscriptionConsent").is_disabled()
                assert page.locator("#leanTranscriptionPrepare").is_disabled()
                assert page.locator("#leanTranscriptionPackage").text_content() == ""
                assert page.evaluate("state.leanFragment.certificate") is False

                page.evaluate("() => openModule('LST-01', true)")
                page.wait_for_function(
                    "() => state.currentModule==='LST-01' && state.currentEntity===null && !!state.currentData",
                    timeout=15000,
                )
                page.locator("#rangeStart").fill(str(first))
                page.locator("#rangeEnd").fill(str(last))
                page.locator("#openLeanCurrent").click()
                page.wait_for_function(
                    "() => state.leanFragment?.formalization_id==='lst01-de-morgan' && state.leanFragment?.source_linkage==='contains_theorem'",
                    timeout=15000,
                )
                expected_lines = "".join(source.splitlines(keepends=True)[first-1:last])
                assert page.locator("#leanLatex").text_content() == expected_lines
                assert page.evaluate("state.leanFragment.certificate") is False

                page.evaluate("() => openModule('LST-01', true)")
                page.wait_for_function(
                    "() => state.currentModule==='LST-01' && state.currentEntity===null && !!state.currentData",
                    timeout=15000,
                )
                page.locator("#rangeStart").fill(str(first))
                page.locator("#rangeEnd").fill(str(last-1))
                page.locator("#openLeanCurrent").click()
                page.wait_for_function(
                    "() => state.leanFragment?.formalization_status==='missing'",
                    timeout=15000,
                )
                assert page.evaluate("state.leanFragment.lean_code") is None
                assert page.evaluate("state.leanFragment.certificate") is False
                assert page.locator("#leanRun").is_disabled()
                # Last-line selection must not offer an inexistent line after
                # a canonical TeX file ending with a terminal newline.
                page.evaluate("() => openModule('BT-00', true)")
                page.wait_for_function(
                    "() => state.currentModule === 'BT-00' && state.currentData && !state.currentData.truncated",
                    timeout=15000,
                )
                line_count = page.evaluate("""() => {
                    const text = state.currentData.latex;
                    return text.split('\\n').length - (text.endsWith('\\n') ? 1 : 0);
                }""")
                assert int(page.locator("#rangeStart").input_value()) == 1
                assert int(page.locator("#rangeEnd").input_value()) == line_count
                page.locator("#addRange").click()
                assert "Dodano wycinek" in page.locator("#toast").inner_text()
                page.locator('[data-tab="graph"]').click()
                page.locator("#view-graph").wait_for(state="visible", timeout=15000)
                assert page.locator("#graphLeft option").count() > 0
                assert page.locator("#graphRight option").count() > 0
                # Full-index thematic coverage and real navigation into a pair.
                with page.expect_response(
                    lambda response: response.url.endswith("/api/graph/coverage"),
                    timeout=60000,
                ) as coverage_response:
                    page.locator("#globalGraphCoverage").click()
                coverage = coverage_response.value
                assert coverage.ok, (coverage.status, coverage.text()[:1000])
                payload = coverage.json()
                assert payload["summary"]["indexed_chapters"] == stats["documents"]
                assert payload["catalog"] is not None
                assert not payload["catalog"]["missing"], payload["catalog"]["missing"]
                assert not payload["catalog"]["path_mismatches"]
                assert payload["reading_audit"]["checked"] >= 67
                assert payload["reading_audit"]["invalid"] == 0, payload["reading_audit"]
                page.locator("#globalReadingAudit").wait_for(state="visible", timeout=15000)
                assert "błędne: 0" in page.locator("#globalReadingAudit").inner_text()
                measure = next(p for p in payload["domain_pairs"]
                               if {p["left"], p["right"]} == {"teoria miary", "analiza funkcjonalna"})
                assert measure["reading"] > 0, measure
                pair_button = page.locator(".global-graph-pairs button").filter(
                    has_text=f'{measure["left"]} ↔ {measure["right"]} · {measure["references"]}'
                )
                page.locator("#graphMin").fill("1")
                with page.expect_response(
                    lambda response: "/api/graph?left=" in response.url,
                    timeout=60000,
                ) as pair_response:
                    pair_button.click()
                pair = pair_response.value
                assert pair.ok, (pair.status, pair.text()[:1000])
                pair_payload = pair.json()
                assert pair_payload["edges"], pair_payload
                assert {pair_payload["left"], pair_payload["right"]} == {
                    "teoria miary", "analiza funkcjonalna"}
                page.wait_for_function("() => !document.getElementById('globalReadingAudit')",
                                       timeout=15000)
                assert "par powiązanych" in page.locator("#graphSummary").inner_text()
                # Concept graph must work in real Chromium without a graph CDN.
                # Reuse the global search as a shortcut into the new graph view.
                page.locator("#searchInput").fill("Zorn")
                page.locator("#searchResults .search-concept-action").wait_for(
                    state="visible", timeout=15000
                )
                # The search action already invokes openConceptSearch(), which
                # loads the graph. Do not start a redundant concurrent request.
                # Observe the response from this actual user action and retain
                # diagnostics if rendering fails (no retries or synthetic data).
                with page.expect_response(
                    lambda response: "/api/concepts/graph?" in response.url
                    and response.request.method == "GET", timeout=60000,
                ) as graph_response:
                    page.locator("#searchResults .search-concept-action").click()
                page.locator("#view-concepts").wait_for(state="visible", timeout=15000)
                response = graph_response.value
                assert response.ok, (response.status, response.url, response.text()[:1000])
                graph_payload = response.json()
                assert graph_payload["occurrences_shown"] > 0, graph_payload
                try:
                    page.locator("#conceptEvidence .concept-occurrence").first.wait_for(
                        state="visible", timeout=20000
                    )
                except Exception as exc:
                    raise AssertionError(
                        "Concept response not rendered: "
                        f"summary={page.locator('#conceptSummary').text_content()!r}, "
                        f"query={page.locator('#conceptSearch').input_value()!r}, "
                        f"errors={errors!r}, response={response.url}"
                    ) from exc
                assert "Lemat Zorna" in page.locator("#conceptEvidence").inner_text()
                assert "Równoważne nad ZF" in page.locator("#conceptRelations").inner_text()
                assert page.locator("#conceptCanvas svg").count() == 1
                equivalent_count = sum(e["type"] == "equivalent" for e in graph_payload["edges"])
                assert equivalent_count > 0
                assert page.locator('#conceptCanvas path[marker-start="url(#concept-arrow)"][marker-end="url(#concept-arrow)"]').count() == equivalent_count
                page.locator("#conceptEvidence .concept-occurrence").first.click()
                page.locator("#view-reader").wait_for(state="visible", timeout=15000)
                assert page.locator("#docTitle").inner_text().strip()
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
                # Allow the previous clicked ref to finish navigation and
                # consume its pending hover/leave events before the next preview.
                page.mouse.move(0, 0)
                page.wait_for_timeout(450)
                page.evaluate("() => closeTip()")
                anchor_id = "docTitle"
                page.evaluate(
                    "([label, anchorId]) => previewLabel(label, document.getElementById(anchorId))",
                    [ambiguous_label, anchor_id],
                )
                page.wait_for_timeout(500)
                debug = page.evaluate("""() => ({
                    tip: document.getElementById('tipBody').textContent,
                    hidden: document.getElementById('referenceTip').classList.contains('hidden'),
                    candidates: document.querySelectorAll('#tipBody .ref-choice').length,
                    openDisabled: document.getElementById('tipOpen').disabled,
                    errors: [],
                })""")
                print(json.dumps({"ambiguous_label": ambiguous_label, "preview_debug": debug},ensure_ascii=False),flush=True)
                assert debug["candidates"] >= 2, debug
                page.locator("#tipBody .ref-choice").first.wait_for(state="visible",timeout=5000)
                assert "Etykieta występuje w kilku rozdziałach" in page.locator("#tipBody").inner_text()
                assert page.locator("#tipOpen").is_disabled()
                assert page.locator("#tipBody .ref-choice").count() >= 2
                selected_owner = page.locator("#tipBody .ref-choice").first.inner_text().split(": ",1)[0]
                page.locator("#tipBody .ref-choice").first.click()
                page.wait_for_function(
                    "(id) => document.getElementById('docBreadcrumb').textContent.includes(id)",
                    arg=selected_owner, timeout=15000,
                )
                page.evaluate(
                    "([label, anchorId]) => previewLabel(label, document.getElementById(anchorId))",
                    [missing_label, anchor_id],
                )
                page.locator("#referenceTip").wait_for(state="visible")
                assert "Nie znaleziono cytowanej etykiety" in page.locator("#tipBody").inner_text()
                assert missing_label in page.locator("#tipBody").inner_text()
                assert page.locator("#tipOpen").is_disabled()
                # Isolate the out-of-order-response check from previous
                # navigation/hover timers: use a fresh, fully loaded page.
                page.goto(URL, wait_until="networkidle", timeout=30000)
                # This second load is only an isolation boundary for the
                # race test; the chapter count was asserted on the first load.
                page.wait_for_function(
                    "() => typeof previewLabel === 'function' && document.getElementById('docTitle') !== null",
                    timeout=15000,
                )
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
                page.wait_for_function(
                    "(label) => document.getElementById('tipBody').textContent.includes('Nie znaleziono cytowanej etykiety') && document.getElementById('tipBody').textContent.includes(label)",
                    arg=missing_label, timeout=5000,
                )
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
