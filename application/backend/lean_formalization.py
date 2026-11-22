"""Read-only links from indexed LaTeX fragments to trusted, registered Lean files.

No client-supplied Lean code or filesystem path is executed. The runner is opt-in and
is intended for a local, trusted application process, not an internet-exposed service.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
from typing import Any
import sqlite3

from fastapi import HTTPException

from backend import lean_cgroup, lean_results, lean_process, lean_run_lock, lean_windows_job

LEAN_ROOT = Path(__file__).resolve().parents[1] / "lean"
MAX_SOURCE_CHARS = 30000
MAX_LEAN_CHARS = 60000
TIMEOUT_SECONDS = 40
VALID_ID = re.compile(r"^[a-zA-Z0-9_-]{1,100}$")
VALID_THEOREM = re.compile(r"^[a-zA-Z_][a-zA-Z0-9_'.]*$")


def _registry(lean_root: Path = LEAN_ROOT) -> list[dict[str, Any]]:
    file = lean_root / "manifest.json"
    if not file.is_file():
        return []
    try:
        raw = json.loads(file.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise HTTPException(503, f"Nie można odczytać rejestru formalizacji: {exc}") from exc
    if not isinstance(raw, dict) or not isinstance(raw.get("items"), list):
        raise HTTPException(503, "Niepoprawny format rejestru formalizacji.")
    results: list[dict[str, Any]] = []
    seen: set[str] = set()
    for item in raw["items"]:
        if not isinstance(item, dict) or not VALID_ID.fullmatch(str(item.get("id", ""))):
            raise HTTPException(503, "Niepoprawny identyfikator formalizacji.")
        if item["id"] in seen:
            raise HTTPException(503, "Powtórzony identyfikator formalizacji.")
        seen.add(item["id"])
        rel = item.get("lean_file")
        if not isinstance(rel, str) or not rel.endswith(".lean"):
            raise HTTPException(503, "Niepoprawny plik Lean.")
        target = (lean_root / rel).resolve()
        if not target.is_relative_to((lean_root / "src").resolve()) or not target.is_file():
            raise HTTPException(503, "Plik Lean musi istnieć w katalogu src/ rejestru.")
        if not isinstance(item.get("source_module"), str) or not isinstance(item.get("source_label"), str):
            raise HTTPException(503, "Brak identyfikatora źródła LaTeX.")
        if not VALID_THEOREM.fullmatch(str(item.get("lean_theorem", ""))):
            raise HTTPException(503, "Niepoprawna nazwa twierdzenia Lean.")
        members = item.get("lean_theorems", [item["lean_theorem"]])
        if (not isinstance(members, list) or not members
                or not all(isinstance(n, str) and VALID_THEOREM.fullmatch(n) for n in members)
                or len(members) != len(set(members)) or item["lean_theorem"] not in members):
            raise HTTPException(503, "Niepoprawna lista twierdzeń składających się na formalizację.")
        if item.get("statement_status") == "approved" and item.get("source_document_sha256") is None:
            raise HTTPException(503, "Zatwierdzone powiązanie wymaga przypiętego SHA256 źródła.")
        if item.get("statement_status") not in {"unreviewed", "needs_review", "approved"}:
            raise HTTPException(503, "Niepoprawny status zgodności stwierdzenia.")
        source_path = item.get("source_document_path")
        if source_path is not None and (
                not isinstance(source_path, str) or not source_path.startswith("chapters/pl/")
                or not source_path.endswith(".tex")):
            raise HTTPException(503, "Niepoprawna ścieżka kanonicznego źródła LaTeX.")
        digest = item.get("source_document_sha256")
        if digest is not None and not re.fullmatch(r"[0-9a-f]{64}", str(digest)):
            raise HTTPException(503, "Niepoprawny SHA256 źródła LaTeX.")
        results.append({**item, "_file": target})
    return results


def _find_source(con: sqlite3.Connection, *, entity_id: str | None,
                 module_id: str | None, start_line: int | None, end_line: int | None):
    if entity_id:
        if module_id is not None or start_line is not None or end_line is not None:
            raise HTTPException(400, "Wybierz obiekt albo zakres wierszy, nie oba.")
        e = con.execute(
            "SELECT id,document_id,kind,title,start_line,end_line,start_offset,end_offset "
            "FROM entities WHERE id=?", (entity_id,)
        ).fetchone()
        if e is None:
            raise HTTPException(404, "Nieznany obiekt matematyczny.")
        d = con.execute("SELECT id,title,sha256,content FROM documents WHERE id=?",
                        (e["document_id"],)).fetchone()
        if d is None:
            raise HTTPException(404, "Nie znaleziono rozdziału.")
        if not isinstance(d["content"], str):
            raise HTTPException(409, "Brak tekstowej treści rozdziału w indeksie.")
        content = d["content"][e["start_offset"]:e["end_offset"]]
        labels = [row[0] for row in con.execute(
            "SELECT name FROM labels WHERE entity_id=? ORDER BY offset", (entity_id,))]
        linkage = "exact_entity"
        # In a conventional TeX source, a proof immediately follows its theorem.
        # Never link a proof to an unrelated earlier theorem across other text.
        if e["kind"] == "proof" and not labels:
            previous = con.execute(
                "SELECT id,end_offset FROM entities WHERE document_id=? AND kind='theorem' "
                "AND end_offset<=? ORDER BY end_offset DESC LIMIT 1",
                (d["id"], e["start_offset"])).fetchone()
            if previous and not d["content"][previous["end_offset"]:e["start_offset"]].strip():
                labels = [row[0] for row in con.execute(
                    "SELECT name FROM labels WHERE entity_id=? ORDER BY offset",
                    (previous["id"],))]
                if labels:
                    linkage = "proof_of_adjacent_theorem"
        return d, content, labels, e["start_line"], e["end_line"], entity_id, linkage
    if not module_id or start_line is None or end_line is None:
        raise HTTPException(400, "Podaj entity_id albo module_id wraz z start_line i end_line.")
    if not (1 <= start_line <= end_line and end_line - start_line <= 300):
        raise HTTPException(400, "Zakres musi zawierać od 1 do 301 pełnych wierszy.")
    d = con.execute("SELECT id,title,sha256,content FROM documents WHERE id=?",
                    (module_id,)).fetchone()
    if d is None:
        raise HTTPException(404, "Nieznany moduł.")
    if not isinstance(d["content"], str):
        raise HTTPException(409, "Brak tekstowej treści rozdziału w indeksie.")
    lines = d["content"].splitlines(keepends=True)
    if end_line > len(lines):
        raise HTTPException(400, "Zakres wykracza poza rozdział.")
    content = "".join(lines[start_line-1:end_line])
    # Link only if the selected range contains the COMPLETE source theorem.
    entities = con.execute(
        "SELECT id FROM entities WHERE document_id=? AND kind='theorem' "
        "AND start_line>=? AND end_line<=?",
        (module_id, start_line, end_line)).fetchall()
    ids = [row["id"] for row in entities]
    labels = []
    for eid in ids:
        labels.extend(row[0] for row in con.execute(
            "SELECT name FROM labels WHERE entity_id=? ORDER BY offset", (eid,)))
    return d, content, labels, start_line, end_line, None, "contains_theorem"


def _source_file_current(item: dict[str, Any], digest: str, lean_root: Path) -> bool:
    """Recheck checked-out canonical TeX, even when the SQLite index was not rebuilt."""
    rel = item.get("source_document_path")
    if rel is None:
        return True  # Legacy unpinned test manifests; CI requires path for approved entries.
    repo = lean_root.resolve().parents[1]
    allowed = (repo / "chapters" / "pl").resolve()
    path = (repo / rel).resolve()
    if not path.is_relative_to(allowed) or not path.is_file():
        return False
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest() == digest
    except OSError:
        return False


def _matches(item: dict[str, Any], d: sqlite3.Row, labels: list[str]) -> bool:
    return item["source_module"] == d["id"] and item["source_label"] in labels


def _results_override(lean_root: Path, results_root: Path | None) -> Path | None:
    """Keep alternate Lean roots in tests isolated from the application run history."""
    if results_root is not None:
        return results_root
    return lean_root.parent / "lean_runs" if lean_root.resolve() != LEAN_ROOT.resolve() else None


def fragment(con: sqlite3.Connection, *, entity_id: str | None = None,
             module_id: str | None = None, start_line: int | None = None,
             end_line: int | None = None, lean_root: Path = LEAN_ROOT,
             results_root: Path | None = None) -> dict[str, Any]:
    d, content, labels, first, last, eid, linkage = _find_source(
        con, entity_id=entity_id, module_id=module_id,
        start_line=start_line, end_line=end_line)
    if len(content) > MAX_SOURCE_CHARS:
        raise HTTPException(413, "Fragment LaTeX jest zbyt duży. Wybierz mniejszy zakres.")
    # Do not present a mapping as current when the indexed source is corrupted.
    if (not isinstance(d["content"], str) or
            hashlib.sha256(d["content"].encode("utf-8")).hexdigest() != d["sha256"]):
        raise HTTPException(409, "Niezgodność treści rozdziału z SHA256 w indeksie.")
    matches = [r for r in _registry(lean_root) if _matches(r, d, labels)]
    if len(matches) > 1:
        raise HTTPException(409, "Wiele formalizacji pasuje do tego fragmentu; wymagane rozstrzygnięcie.")
    base = {"source_module": d["id"], "source_entity": eid, "source_linkage": linkage,
            "source_labels": labels, "start_line": first, "end_line": last,
            "source_latex": content, "source_sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
            "formalization_status": "missing", "statement_status": "unreviewed",
            "proof_status": "not_run", "lean_code": None, "formalization_id": None,
            "lean_theorem": None, "certificate": False}
    if not matches:
        return base
    item = matches[0]
    sha_ok = item.get("source_document_sha256") == d["sha256"] if item.get("source_document_sha256") else None
    if sha_ok is not False and not _source_file_current(item, d["sha256"], lean_root):
        sha_ok = False
    content_lean = item["_file"].read_text(encoding="utf-8")
    if len(content_lean) > MAX_LEAN_CHARS:
        raise HTTPException(413, "Zarejestrowany plik Lean jest zbyt duży.")
    base.update({"formalization_id": item["id"], "lean_theorem": item["lean_theorem"],
                 "lean_theorems": item.get("lean_theorems", [item["lean_theorem"]]),
                 "source_document_sha256": item.get("source_document_sha256"),
                 "lean_code": content_lean,
                 "statement_status": "needs_review" if sha_ok is False else item["statement_status"],
                 "formalization_status": "stale" if sha_ok is False else "ready" if sha_ok else "draft",
                 "source_pinned": sha_ok is not None,
                 "lean_file": item["lean_file"]})
    if sha_ok is False:
        return base
    try:
        fingerprint = lean_results.fingerprint(d["sha256"], item["_file"], lean_root)
        run_info = lean_results.last_run(
            item["id"], fingerprint,
            results_root=_results_override(lean_root, results_root))
        base.update(run_info)
    except (OSError, ValueError) as exc:
        base["run_record_invalid"] = True
        base["run_record_error"] = str(exc)[:300]
    return base


def availability(lean_root: Path = LEAN_ROOT) -> dict[str, Any]:
    lake = shutil.which("lake")
    enabled = os.environ.get("MATLIB_LEAN_RUN") == "1"
    try:
        memory_mb = lean_process.configured_memory_limit_mb()
        memory_error = None
    except ValueError as exc:
        memory_mb, memory_error = None, str(exc)
    memory_supported = lean_process.memory_limit_supported()
    memory_ready = memory_error is None and (memory_mb is None or memory_supported)
    try:
        total_mb = lean_cgroup.configured_total_memory_mb()
        total_error = None
    except ValueError as exc:
        total_mb, total_error = None, str(exc)
    total_supported = lean_cgroup.available() or lean_windows_job.available()
    total_ready = total_error is None and (total_mb is None or total_supported)
    return {"runner_enabled": enabled, "lake_available": bool(lake),
            "ready": enabled and bool(lake) and memory_ready and total_ready
            and (lean_root / "lakefile.toml").is_file(),
            "memory_limit_mb": memory_mb,
            "memory_limit_enforced": memory_mb is not None and memory_supported,
            "memory_limit_supported": memory_supported,
            "total_memory_limit_mb": total_mb,
            "total_memory_limit_supported": total_supported,
            "total_memory_limit_error": total_error if total_error is not None else
            ("Brak cgroup v2 lub Windows Job Objects dla łącznego limitu pamięci." if total_mb is not None
             and not total_supported else None),
            "memory_limit_error": memory_error if memory_error is not None else
            ("Nieobsługiwany system limitu pamięci." if memory_mb is not None
             and not memory_supported else None),
            "toolchain": (lean_root / "lean-toolchain").read_text(encoding="utf-8").strip()
            if (lean_root / "lean-toolchain").exists() else None,
            "registered_formalizations": len(_registry(lean_root))}


def run(con: sqlite3.Connection, formalization_id: str,
        lean_root: Path = LEAN_ROOT,
        results_root: Path | None = None) -> dict[str, Any]:
    if not VALID_ID.fullmatch(formalization_id):
        raise HTTPException(400, "Niepoprawny identyfikator.")
    matches = [i for i in _registry(lean_root) if i["id"] == formalization_id]
    if not matches:
        raise HTTPException(404, "Nieznana formalizacja.")
    item = matches[0]
    d = con.execute("SELECT id,sha256,content FROM documents WHERE id=?",
                    (item["source_module"],)).fetchone()
    if d is None:
        raise HTTPException(409, "Rozdział źródłowy nie znajduje się w indeksie.")
    # An index SHA alone is not proof that the indexed bytes still match it.
    # Fail closed before spawning Lean if the database is inconsistent.
    if (not isinstance(d["content"], str) or
            hashlib.sha256(d["content"].encode("utf-8")).hexdigest() != d["sha256"]):
        return {"formalization_id": formalization_id, "proof_status": "blocked",
                "detail": "Niezgodność treści rozdziału z SHA256 w indeksie.",
                "certificate": False}
    if ((item.get("source_document_sha256") and item["source_document_sha256"] != d["sha256"])
            or not _source_file_current(item, d["sha256"], lean_root)):
        return {"formalization_id": formalization_id, "proof_status": "blocked",
                "detail": "Źródło LaTeX zmieniło się od czasu powiązania formalizacji.",
                "certificate": False}
    if os.environ.get("MATLIB_LEAN_RUN") != "1":
        return {"formalization_id": formalization_id, "proof_status": "blocked",
                "detail": "Uruchamianie lokalne jest wyłączone. Ustaw MATLIB_LEAN_RUN=1.",
                "certificate": False}
    try:
        memory_mb = lean_process.configured_memory_limit_mb()
    except ValueError as exc:
        return {"formalization_id": formalization_id, "proof_status": "blocked",
                "detail": str(exc), "certificate": False}
    if memory_mb is not None and not lean_process.memory_limit_supported():
        return {"formalization_id": formalization_id, "proof_status": "blocked",
                "detail": "Nie można wymusić limitu pamięci na tym systemie.",
                "certificate": False}
    try:
        total_mb = lean_cgroup.configured_total_memory_mb()
    except ValueError as exc:
        return {"formalization_id": formalization_id, "proof_status": "blocked",
                "detail": str(exc), "certificate": False}
    if total_mb is not None and not (
            lean_cgroup.available() or lean_windows_job.available()):
        return {"formalization_id": formalization_id, "proof_status": "blocked",
                "detail": "Brak cgroup v2 lub Windows Job Objects dla łącznego limitu pamięci.",
                "certificate": False}
    if shutil.which("lake") is None:
        return {"formalization_id": formalization_id, "proof_status": "toolchain_unavailable",
                "detail": "Nie znaleziono polecenia lake (Lean 4).", "certificate": False}
    # A registered path is trusted only if local repository authors have reviewed it.
    # This is NOT a security boundary against a malicious .lean file.
    try:
        fingerprint = lean_results.fingerprint(d["sha256"], item["_file"], lean_root)
    except (OSError, ValueError) as exc:
        raise HTTPException(503, f"Nie można obliczyć wersji formalizacji: {exc}") from exc

    def finish(status: str, detail: str, log: str = "") -> dict[str, Any]:
        result = {"formalization_id": formalization_id, "proof_status": status,
                  "detail": detail, "log": log, "statement_status": item["statement_status"],
                  "certificate": False}
        try:
            after = lean_results.fingerprint(d["sha256"], item["_file"], lean_root)
            if after != fingerprint or not _source_file_current(item, d["sha256"], lean_root):
                return {**result, "proof_status": "blocked",
                        "detail": "Zmiana plików formalizacji podczas pracy Lean; wynik unieważniony."}
            saved = lean_results.save_run(
                formalization_id, fingerprint, proof_status=status, detail=detail,
                log=log, results_root=_results_override(lean_root, results_root))
            result["run_record_saved"] = True
            result["last_run_at"] = saved["finished_at"]
        except (OSError, ValueError) as exc:
            result["run_record_saved"] = False
            result["run_record_warning"] = "Nie udało się zapisać historii uruchomienia: " + str(exc)[:250]
        return result

    command = ["lake", "env", "lean", str(item["_file"].relative_to(lean_root))]
    try:
        # Lock spans execution and persistence. Multiple workers in one checkout
        # must not start overlapping memory-intensive compilers or race on results.
        with lean_run_lock.exclusive(lean_root):
            try:
                returncode, log, timed_out = lean_process.execute_registered(
                    command, lean_root, timeout=TIMEOUT_SECONDS,
                    memory_limit_mb=memory_mb, total_memory_mb=total_mb)
            except (lean_cgroup.CgroupUnavailable, lean_windows_job.JobUnavailable,
                    lean_process.MemoryLimitUnavailable) as exc:
                return {"formalization_id": formalization_id, "proof_status": "blocked",
                        "detail": str(exc), "certificate": False}
            except RuntimeError as exc:
                return finish("failed", "Niekompletny odczyt wyniku procesu Lean.",
                              str(exc)[:500])
            except OSError as exc:
                return {"formalization_id": formalization_id,
                        "proof_status": "toolchain_unavailable",
                        "detail": str(exc), "certificate": False}
            if timed_out:
                return finish("timeout", f"Lean przekroczył limit {TIMEOUT_SECONDS} s.",
                              log)
            # Success does not prove statement equivalence or absence of axioms.
            return finish("compiled" if returncode == 0 else "failed",
                          f"Lean zakończył pracę z kodem {returncode}.", log)
    except (lean_run_lock.RunnerBusy, lean_run_lock.RunnerLockUnavailable) as exc:
        return {"formalization_id": formalization_id, "proof_status": "blocked",
                "detail": str(exc), "certificate": False}
