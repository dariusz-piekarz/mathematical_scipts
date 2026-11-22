"""Bounded, opt-in inspection of elaborated Lean constant references.

Uses only a registered local Lean file and manifest-validated names.
This is not a theorem certificate or an isolated sandbox for untrusted files.
"""
from __future__ import annotations

import hashlib
import os
from pathlib import Path
import re
import secrets
import sqlite3
import tempfile

from fastapi import HTTPException
from backend import (lean_catalog, lean_cgroup, lean_formalization as lean,
                     lean_process, lean_results, lean_run_lock, lean_source_provenance, lean_windows_job)

MAX_THEOREMS = 16
MAX_CONSTANTS = 160
MAX_OUTPUT_BYTES = 128 * 1024
TOKEN_RE = re.compile(r"[0-9a-f]{32}\Z")
NAME_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_'.]*\Z")


def make_instrumentation(names: list[str], token: str, *, classified: bool = False) -> str:
    """MetaM commands with identifiers from the trusted manifest only."""
    if (not TOKEN_RE.fullmatch(token) or not 1 <= len(names) <= MAX_THEOREMS
            or len(names) != len(set(names))
            or any(not lean.VALID_THEOREM.fullmatch(n) for n in names)):
        raise ValueError("Invalid Lean introspection identifiers")
    lines = ["\n\n-- ATLAS generated inspection; never a certificate.",
             "open Lean Meta"]
    for name in names:
        lines.extend([
            "run_meta do",
            f"  let info ← getConstInfo {chr(96)}{name}",
            "  let constants := info.getUsedConstantsAsSet.toList",
            f'  logInfo m!"{token} BEGIN {name} {{constants.length}}"',
            "  for constant in constants do",
            f'    logInfo m!"{token} CONST {name} {{constant}}"',
            f'  logInfo m!"{token} END {name}"',
        ])
        if classified:
            lines.extend([
                "  let typeConstants : List Name := info.type.getUsedConstantsAsSet.toList",
                "  let valueConstants : List Name := match info.value? true with",
                "    | some value => value.getUsedConstantsAsSet.toList",
                "    | none => []",
                f'  logInfo m!"{token} TYPE_BEGIN {name} {{typeConstants.length}}"',
                "  for constant in typeConstants do",
                f'    logInfo m!"{token} TYPE_CONST {name} {{constant}}"',
                f'  logInfo m!"{token} TYPE_END {name}"',
                f'  logInfo m!"{token} VALUE_BEGIN {name} {{toString valueConstants.length}}"',
                "  for constant in valueConstants do",
                f'    logInfo m!"{token} VALUE_CONST {name} {{constant}}"',
                f'  logInfo m!"{token} VALUE_END {name}"',
            ])
    return "\n".join(lines) + "\n"


def parse_inspection(log: str, token: str, names: list[str]) -> dict[str, list[str]]:
    """Require unique BEGIN/CONST/END events and a complete, bounded transcript."""
    # The subprocess collector retains only a tail. A full buffer may have
    # silently discarded earlier diagnostics even if the last events look valid.
    # Fail closed at the exact capacity boundary, not just above it.
    if (not TOKEN_RE.fullmatch(token) or len(log.encode("utf-8")) >= MAX_OUTPUT_BYTES
            or not 1 <= len(names) <= MAX_THEOREMS
            or len(names) != len(set(names))
            or any(not NAME_RE.fullmatch(name) for name in names)):
        raise ValueError("Invalid declarations or saturated Lean output")
    expected = set(names)
    counts: dict[str, int] = {}
    found: dict[str, set[str]] = {}
    completed: set[str] = set()
    for line in log.splitlines():
        offset = line.find(token + " ")
        if offset < 0:
            continue
        fields = line[offset:].strip().split()
        if len(fields) not in (3, 4) or fields[0] != token:
            raise ValueError("Malformed Lean inspection output")
        _, action, name, *tail = fields
        if name not in expected:
            raise ValueError("Unexpected Lean declaration")
        if action == "BEGIN" and len(tail) == 1:
            if name in counts or not tail[0].isdecimal():
                raise ValueError("Invalid Lean declaration start")
            number = int(tail[0])
            if number > MAX_CONSTANTS:
                raise ValueError("Too many constants for one Lean declaration")
            counts[name] = number
            found[name] = set()
        elif action == "CONST" and len(tail) == 1:
            if name not in counts or name in completed:
                raise ValueError("Unopened or closed declaration")
            if not NAME_RE.fullmatch(tail[0]) or tail[0] in found[name]:
                raise ValueError("Invalid or duplicated Lean constant")
            found[name].add(tail[0])
        elif action == "END" and not tail:
            if name not in counts or name in completed or len(found[name]) != counts[name]:
                raise ValueError("Incomplete declaration")
            completed.add(name)
        else:
            raise ValueError("Invalid Lean inspection event")
    if completed != expected:
        raise ValueError("Not all declarations were inspected")
    return {name: sorted(found[name]) for name in names}


def parse_classified_inspection(log: str, token: str,
                                names: list[str]) -> dict:
    """Require type and value events for every registered declaration.

    Preserve the legacy complete constant list while attributing each direct
    expression reference to its origin. This is not a transitive proof graph.
    """
    if len(log.encode("utf-8")) >= MAX_OUTPUT_BYTES:
        raise ValueError("Saturated classified Lean output")
    streams: dict[str, list[str]] = {"total": [], "type": [], "value": []}
    for line in log.splitlines():
        offset = line.find(token + " ")
        if offset < 0:
            continue
        fields = line[offset:].strip().split()
        if len(fields) < 3 or fields[0] != token:
            raise ValueError("Malformed classified Lean output")
        event = fields[1]
        if event in ("BEGIN", "CONST", "END"):
            streams["total"].append(line)
        elif event.startswith("TYPE_") or event.startswith("VALUE_"):
            origin, event_name = event.split("_", 1)
            if origin not in ("TYPE", "VALUE") or event_name not in (
                    "BEGIN", "CONST", "END"):
                raise ValueError("Unknown classified Lean event")
            streams[origin.lower()].append(
                line[:offset] + token + " " + event_name + " " +
                " ".join(fields[2:]))
        else:
            raise ValueError("Unexpected classified Lean event")
    total = parse_inspection("\n".join(streams["total"]), token, names)
    types = parse_inspection("\n".join(streams["type"]), token, names)
    values = parse_inspection("\n".join(streams["value"]), token, names)
    if any(set(total[name]) != set(types[name]) | set(values[name])
           for name in names):
        raise ValueError("Type/value references disagree with Lean total")
    edges = [
        {"declaration": name, "constant": value, "origin": origin}
        for name in names
        for origin, refs in (("type", types[name]), ("value", values[name]))
        for value in refs
    ]
    return {"constants": total, "type_constants": types,
            "value_constants": values, "reference_edges": edges}


# Backward-compatible names; the catalog, runner and inspector now share
# exactly one verifier for indexed label owners and TeX command locations.
_indexed_binding = lean_source_provenance.indexed_binding
_valid_indexed_binding = lean_source_provenance.valid_binding


def _empty(identifier: str, status: str, detail: str) -> dict:
    return {"formalization_id": identifier, "inspection_status": status,
            "detail": detail, "constants": {}, "certificate": False}


def inspect(con: sqlite3.Connection, identifier: str, *,
            lean_root: Path = lean.LEAN_ROOT, classified: bool = False) -> dict:
    if not lean.VALID_ID.fullmatch(identifier):
        raise HTTPException(400, "Niepoprawny identyfikator.")
    item = next((i for i in lean._registry(lean_root) if i["id"] == identifier), None)
    if item is None:
        raise HTTPException(404, "Nieznana formalizacja.")
    names = item.get("lean_theorems", [item["lean_theorem"]])
    if len(names) > MAX_THEOREMS:
        return _empty(identifier, "blocked", "Zbyt dużo deklaracji Lean.")
    if os.environ.get("MATLIB_LEAN_RUN") != "1":
        return _empty(identifier, "blocked", "Ustaw MATLIB_LEAN_RUN=1.")
    try:
        config = lean.availability(lean_root)
    except (OSError, ValueError) as exc:
        return _empty(identifier, "blocked", "Niepoprawna konfiguracja: " + str(exc)[:160])
    if not config["lake_available"]:
        return _empty(identifier, "toolchain_unavailable", "Brak lake/Lean.")
    if not config["ready"]:
        return _empty(identifier, "blocked", "Brak bezpiecznych warunków uruchomienia.")

    try:
        with lean_run_lock.exclusive(lean_root):
            record = next((i for i in lean_catalog.list_formalizations(
                con, lean_root=lean_root)["items"] if i["formalization_id"] == identifier), None)
            # The manifest was loaded before obtaining the runner lock.
            # Reject an ID whose catalog binding has changed in that gap.
            if (record is None or record["formalization_status"] != "ready"
                    or any(record.get(key) != item.get(key) for key in (
                        "source_module", "source_label", "lean_file", "lean_theorem"))
                    or record.get("lean_theorems") != names):
                return _empty(identifier, "blocked", "Nieaktualne przypięcie źródła.")
            binding_before = _indexed_binding(
                con, item["source_module"], item["source_label"],
                record["source_entity_id"])
            if binding_before is None:
                return _empty(identifier, "blocked",
                              "Nie można jednoznacznie przypiąć indeksowanego twierdzenia.")
            doc = con.execute("SELECT sha256,content FROM documents WHERE id=?",
                              (item["source_module"],)).fetchone()
            if (doc is None or not isinstance(doc["content"], str)
                    or hashlib.sha256(doc["content"].encode("utf-8")).hexdigest() != doc["sha256"]
                    or not lean._source_file_current(item, doc["sha256"], lean_root)):
                return _empty(identifier, "blocked", "Źródło LaTeX nie jest spójne.")
            if not _valid_indexed_binding(
                    binding_before, doc["content"], item["source_label"]):
                return _empty(identifier, "blocked",
                              "Błędne granice twierdzenia lub położenie etykiety w indeksie.")
            try:
                binding_sha256 = lean_source_provenance.binding_sha256(
                    item["source_module"], item["source_label"], binding_before)
                before = lean_results.fingerprint(
                    doc["sha256"], item["_file"], lean_root, binding_sha256)
                original = item["_file"].read_bytes()
                if hashlib.sha256(original).hexdigest() != before["lean_sha256"]:
                    return _empty(identifier, "blocked", "Zmieniono kod przed uruchomieniem.")
            except (OSError, ValueError):
                return _empty(identifier, "blocked", "Nie można zweryfikować zależności.")
            token = secrets.token_hex(16)
            try:
                generated = make_instrumentation(names, token, classified=classified).encode("utf-8")
                work = lean_root.parent / "data" / "lean_runs"
                work.mkdir(mode=0o700, parents=True, exist_ok=True)
                with tempfile.TemporaryDirectory(prefix="inspection-", dir=work) as directory:
                    target = Path(directory) / "Inspect.lean"
                    target.write_bytes(original + b"\n" + generated)
                    code, output, timeout = lean_process.execute_registered(
                        ["lake", "env", "lean", str(target)], lean_root,
                        timeout=lean.TIMEOUT_SECONDS, log_limit=MAX_OUTPUT_BYTES,
                        memory_limit_mb=config["memory_limit_mb"],
                        total_memory_mb=config["total_memory_limit_mb"])
            except (lean_cgroup.CgroupUnavailable, lean_windows_job.JobUnavailable,
                    lean_process.MemoryLimitUnavailable) as exc:
                return _empty(identifier, "blocked", str(exc)[:180])
            except OSError as exc:
                return _empty(identifier, "toolchain_unavailable", str(exc)[:180])
            except RuntimeError as exc:
                return _empty(identifier, "failed", "Błąd diagnostyki: " + str(exc)[:180])
            if timeout:
                return _empty(identifier, "timeout", "Przekroczony czas inspekcji.")
            if code != 0:
                return _empty(identifier, "failed", "Lean zwrócił błąd: " + output[-400:])
            try:
                sections = (parse_classified_inspection(output, token, names)
                            if classified else None)
                constants = (sections["constants"] if sections is not None else
                             parse_inspection(output, token, names))
                after = lean_results.fingerprint(
                    doc["sha256"], item["_file"], lean_root, binding_sha256)
            except (OSError, ValueError) as exc:
                return _empty(identifier, "blocked",
                              "Niekompletny wynik lub zmiana zależności: " + str(exc)[:160])
            # The SQLite index may be rebuilt by another process while Lean is
            # running. Re-read the current row instead of trusting the old
            # sqlite3.Row object captured before execution.
            current_doc = con.execute(
                "SELECT sha256,content FROM documents WHERE id=?",
                (item["source_module"],)).fetchone()
            if (current_doc is None or
                    current_doc["sha256"] != doc["sha256"] or
                    not isinstance(current_doc["content"], str) or
                    hashlib.sha256(current_doc["content"].encode("utf-8")).hexdigest()
                    != doc["sha256"]):
                return _empty(identifier, "blocked",
                              "Indeks rozdziału zmienił się podczas inspekcji.")
            # A parser rebuild can change a label -> entity relation without
            # touching the document's bytes or SHA. Recheck the catalog mapping.
            current_record = next((i for i in lean_catalog.list_formalizations(
                con, lean_root=lean_root)["items"] if i["formalization_id"] == identifier), None)
            if (current_record is None or current_record["formalization_status"] != "ready"
                    or current_record["source_entity_id"] != record["source_entity_id"]
                    or current_record["index_status"] != record["index_status"]):
                return _empty(identifier, "blocked",
                              "Powiązanie etykiety zmieniło się podczas inspekcji.")
            if (_indexed_binding(
                    con, item["source_module"], item["source_label"],
                    current_record["source_entity_id"]) != binding_before):
                return _empty(identifier, "blocked",
                              "Granice indeksowanego twierdzenia zmieniły się podczas pracy.")
            if (before != after or
                    not lean._source_file_current(item, doc["sha256"], lean_root)):
                return _empty(identifier, "blocked", "Źródło zmieniło się podczas pracy.")
            return {
                **(sections or {}),
                "formalization_id": identifier, "inspection_status": "complete",
                "detail": ("Stałe z typów i wartości deklaracji z rzeczywistego procesu Lean. "
                           "To nie minimalny graf przesłanek ani certyfikat."),
                "constants": constants,
                "extraction_method": "Lean.ConstantInfo.getUsedConstantsAsSet",
                "source_document_sha256": doc["sha256"],
                "source_binding_sha256": binding_sha256,
                "lean_sha256": before["lean_sha256"],
                "toolchain_sha256": before["toolchain_sha256"],
                "certificate": False,
            }
    except (lean_run_lock.RunnerBusy, lean_run_lock.RunnerLockUnavailable) as exc:
        return _empty(identifier, "blocked", str(exc))
