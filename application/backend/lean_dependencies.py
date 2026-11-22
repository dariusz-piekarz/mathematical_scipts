"""Conservative read-only graph: indexed source ↔ manifest ↔ Lean file imports.

Edges express *registration* or syntactically declared module imports, never
proof dependencies, use of a particular Mathlib lemma, or verification.
"""
from __future__ import annotations

import re
import sqlite3
from pathlib import Path

from fastapi import HTTPException
from backend import lean_catalog, lean_formalization as lean

MAX_IMPORTS = 80
MAX_DECLARATIONS = 80
MAX_LEAN_BYTES = 60000
MODULE_PATTERN = re.compile(r"[A-Za-z_][A-Za-z0-9_'.]*\Z")
IMPORT_PATTERN = re.compile(r"[ \t]*import[ \t]+([^\r\n]+)\Z")


def _strip_comments(source: str) -> str:
    """Strip nested Lean block and line comments, preserving all line breaks.

    String and character contents are masked too, so a textual 'import'
    inside a quotation is not misread as a command.
    """
    output: list[str] = []
    depth = 0
    quote = False
    escaped = False
    i = 0
    while i < len(source):
        c = source[i]
        next_c = source[i + 1] if i + 1 < len(source) else ""
        if depth:
            if c == "/" and next_c == "-":
                depth += 1
                output.extend("  ")
                i += 2
            elif c == "-" and next_c == "/":
                depth -= 1
                output.extend("  ")
                i += 2
            else:
                output.append("\n" if c == "\n" else " ")
                i += 1
        elif quote:
            if c == "\n":
                # Preserve line structure; malformed strings aren't import commands.
                output.append("\n")
            else:
                output.append(" ")
            if escaped:
                escaped = False
            elif c == "\\":
                escaped = True
            elif c == '"':
                quote = False
            i += 1
        elif c == "/" and next_c == "-":
            depth = 1
            output.extend("  ")
            i += 2
        elif c == "-" and next_c == "-":
            while i < len(source) and source[i] != "\n":
                output.append(" ")
                i += 1
        elif c == '"':
            quote = True
            output.append(" ")
            i += 1
        else:
            output.append(c)
            i += 1
    return "".join(output)


def declared_imports(source: str) -> list[str]:
    """Read literal import commands only; no transitive/proof dependency claims."""
    if len(source.encode("utf-8")) > MAX_LEAN_BYTES:
        raise ValueError("Lean module exceeds dependency preview limit")
    found: set[str] = set()
    for line in _strip_comments(source).splitlines():
        match = IMPORT_PATTERN.fullmatch(line)
        if not match:
            continue
        for name in match[1].split():
            if not MODULE_PATTERN.fullmatch(name):
                raise ValueError("Unsupported Lean import syntax")
            found.add(name)
            if len(found) > MAX_IMPORTS:
                raise ValueError("Too many Lean imports")
    return sorted(found)


def graph(con: sqlite3.Connection, formalization_id: str, *,
          lean_root: Path = lean.LEAN_ROOT) -> dict:
    """Return a bounded graph for one registered ID with live source integrity."""
    if not lean.VALID_ID.fullmatch(formalization_id):
        raise HTTPException(400, "Niepoprawny identyfikator formalizacji.")
    registered = lean._registry(lean_root)
    matches = [item for item in registered if item["id"] == formalization_id]
    if not matches:
        raise HTTPException(404, "Nieznana formalizacja.")
    item = matches[0]
    records = lean_catalog.list_formalizations(con, lean_root=lean_root)
    source = next(entry for entry in records["items"]
                  if entry["formalization_id"] == formalization_id)
    theorems = item.get("lean_theorems", [item["lean_theorem"]])
    if len(theorems) > MAX_DECLARATIONS:
        raise HTTPException(503, "Za dużo deklaracji Lean w powiązaniu.")
    try:
        data = item["_file"].read_bytes()
        if len(data) > MAX_LEAN_BYTES:
            raise ValueError("Lean file exceeds dependency preview limit")
        imports = declared_imports(data.decode("utf-8"))
    except (OSError, UnicodeError, ValueError) as exc:
        raise HTTPException(503, "Nie można odczytać importów Lean: " +
                            str(exc)[:180]) from exc

    source_id = "latex:" + item["id"]
    file_id = "file:" + item["lean_file"]
    nodes = [
        {"id": source_id, "kind": "latex_statement",
         "label": source["source_module"] + " · " + source["source_label"]},
        {"id": file_id, "kind": "lean_file", "label": item["lean_file"]},
    ]
    edges = []
    for index, theorem in enumerate(theorems):
        theorem_id = "declaration:" + str(index)
        nodes.append({"id": theorem_id, "kind": "registered_declaration",
                      "label": theorem})
        edges.append({"from": source_id, "to": theorem_id,
                      "kind": "manifest_correspondence"})
        edges.append({"from": theorem_id, "to": file_id,
                      "kind": "manifest_file"})
    for index, module in enumerate(imports):
        import_id = "import:" + str(index)
        nodes.append({"id": import_id, "kind": "imported_module", "label": module})
        edges.append({"from": file_id, "to": import_id,
                      "kind": "declared_import"})
    return {
        "formalization_id": formalization_id,
        "source_module": source["source_module"],
        "source_label": source["source_label"],
        "source_entity_id": source["source_entity_id"],
        "formalization_status": source["formalization_status"],
        "statement_status": source["statement_status"],
        "index_status": source["index_status"],
        "nodes": nodes, "edges": edges, "declared_imports": imports,
        "limitations": ("Powiązania ze źródłem i deklaracjami pochodzą z manifestu. "
                        "Importy to wyłącznie jawne polecenia w pliku Lean. "
                        "Nie wykryto zależności na poziomie lematów, importów "
                        "przechodnich ani wyników kompilacji."),
        "proof_status_included": False, "certificate": False,
    }
