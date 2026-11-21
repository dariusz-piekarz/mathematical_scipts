"""Validated, ordered excerpts of canonical TeX sources for custom projects.

Only existing indexed documents/entities and exact whole-line ranges can be selected.
The database remains read-only. No LaTeX is supplied by the client.
"""
from __future__ import annotations

from collections import defaultdict
from typing import Any
import re
import sqlite3

MODULE_ID = re.compile(r"^[A-Za-z][A-Za-z0-9]*-[0-9]{2}$")
MAX_ITEMS = 300
MAX_MODULES = 75


def select_ordered_items(con: sqlite3.Connection, items: list[dict[str, Any]]):
    """Return (parts, known, ordered_items), preserving selection order.

    An entire module supersedes excerpts from that module. Contained and
    identical excerpts are suppressed; partial overlap is rejected instead of
    silently changing the user's selection.
    """
    from .generator import GenerationError

    if not items or len(items) > MAX_ITEMS:
        raise GenerationError("Wybierz od 1 do 300 elementów skryptu.")
    known = {r["id"]: dict(r) for r in con.execute(
        "SELECT id,path,title,domain,content,sha256 FROM documents")}
    validated = []
    line_offsets: dict[str, list[int]] = {}
    for item in items:
        if not isinstance(item, dict):
            raise GenerationError("Element zestawu musi być obiektem JSON.")
        kind = item.get("kind")
        module = item.get("id") if kind == "module" else item.get("module")
        if kind == "entity":
            eid = item.get("id")
            if not isinstance(eid, str):
                raise GenerationError("Brak identyfikatora obiektu.")
            entity = con.execute(
                "SELECT id,document_id,start_offset,end_offset,start_line,end_line "
                "FROM entities WHERE id=?", (eid,)).fetchone()
            if entity is None:
                raise GenerationError(f"Nieznany obiekt: {eid}")
            module = entity["document_id"]
        if not isinstance(module, str) or not MODULE_ID.fullmatch(module) or module not in known:
            raise GenerationError(f"Nieznany moduł: {module}")
        source = known[module]["content"]
        if kind == "module":
            start, end = 0, len(source)
            identifier = module
            start_line, end_line = 1, source.count("\n") + 1
        elif kind == "entity":
            start, end = entity["start_offset"], entity["end_offset"]
            identifier = eid
            start_line, end_line = entity["start_line"], entity["end_line"]
        elif kind == "lines":
            start_line, end_line = item.get("start_line"), item.get("end_line")
            if (type(start_line) is not int or type(end_line) is not int
                    or start_line < 1 or end_line < start_line):
                raise GenerationError("Wycinek musi mieć poprawny zakres wierszy.")
            if module not in line_offsets:
                ends = [0]
                for line in source.splitlines(keepends=True):
                    ends.append(ends[-1] + len(line))
                line_offsets[module] = ends
            offsets = line_offsets[module]
            if end_line >= len(offsets):
                raise GenerationError(f"Zakres wierszy wykracza poza moduł {module}.")
            start, end = offsets[start_line - 1], offsets[end_line]
            identifier = f"lines:{module}:{start_line}-{end_line}"
        else:
            raise GenerationError(f"Nieznany typ elementu: {kind}")
        if start < 0 or end > len(source) or end <= start:
            raise GenerationError(f"Pusty lub nieprawidłowy fragment: {identifier}")
        validated.append({"kind": kind, "module": module, "id": identifier,
                          "start": start, "end": end,
                          "start_line": start_line, "end_line": end_line})
    wholes = {x["module"] for x in validated if x["kind"] == "module"}
    candidates = [x for x in validated if x["kind"] == "module" or x["module"] not in wholes]
    excerpts = [x for x in candidates if x["kind"] != "module"]
    groups = defaultdict(list)
    for item in excerpts:
        groups[item["module"]].append(item)
    # Check intervals in source order, independently of user's output order.
    for module, rows in groups.items():
        ordered = sorted(rows, key=lambda x: (x["start"], -x["end"]))
        far_end = -1
        for row in ordered:
            if row["start"] < far_end and row["end"] > far_end:
                raise GenerationError(
                    f"Częściowo zachodzące na siebie fragmenty w {module}; "
                    "wybierz pełny obiekt lub rozłączne wiersze.")
            far_end = max(far_end, row["end"])
    kept = []
    seen_modules = set()
    for position, row in enumerate(candidates):
        module = row["module"]
        if row["kind"] == "module":
            if module in seen_modules:
                continue
            seen_modules.add(module)
        else:
            # Drop exact duplicates and excerpts strictly contained in any
            # selected parent, but retain the parent's chosen position.
            if any(other is not row and other["module"] == module
                   and other["kind"] != "module"
                   and other["start"] <= row["start"] and other["end"] >= row["end"]
                   and (other["start"] < row["start"] or other["end"] > row["end"]
                        or candidates.index(other) < position)
                   for other in excerpts):
                continue
        kept.append(row)
    if len({x["module"] for x in kept}) > MAX_MODULES:
        raise GenerationError("Zbyt wiele modułów (limit 75).")
    parts = {}
    for row in kept:
        module = row["module"]
        if module not in parts:
            parts[module] = {"row": known[module], "content": "", "fragments": [],
                             "spans": [], "whole": module in wholes}
        part = parts[module]
        if row["kind"] == "module":
            part["content"] = known[module]["content"]
            part["spans"] = [(0, len(part["content"]))]
        else:
            part["fragments"].append(row["id"])
            part["spans"].append((row["start"], row["end"]))
            text = known[module]["content"][row["start"]:row["end"]]
            part["content"] = (part["content"] + "\n\n" if part["content"] else "") + text
    if not parts:
        raise GenerationError("Wybierz przynajmniej jeden fragment.")
    return parts, known, kept
