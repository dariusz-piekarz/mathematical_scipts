"""One strict provenance contract for registered LaTeX -> Lean mappings.

Checks indexed entity bounds and the actual (unmasked) TeX label command at
the indexed offset. The SQLite index and manifest are not proof certificates.
"""
from __future__ import annotations

import sqlite3
import hashlib
import json

from backend import latex_parser


def indexed_binding(con: sqlite3.Connection, module: str, label: str,
                    entity_id: str) -> tuple | None:
    """Snapshot one exact indexed owner including its kind, span and label offset."""
    rows = con.execute(
        "SELECT e.id,e.kind,e.title,e.start_line,e.end_line,"
        "e.start_offset,e.end_offset,l.offset "
        "FROM labels AS l JOIN entities AS e ON e.id=l.entity_id "
        "WHERE e.document_id=? AND e.id=? AND l.name=? "
        "ORDER BY l.offset LIMIT 2",
        (module, entity_id, label)).fetchall()
    return tuple(rows[0]) if len(rows) == 1 else None


def valid_binding(binding: tuple, source: str, label: str) -> bool:
    """Validate absolute character offsets and the indexed, live label command.

    This mirrors the indexer's masking and argument reader. Text in comments or
    verbatim environments must not turn into trusted labels.
    """
    if not isinstance(binding, tuple) or len(binding) != 8:
        return False
    _, kind, title, first, last, start, end, offset = binding
    # The current registry pins mathematical *theorems*. A label reassigned
    # to a section or definition must never inherit theorem verification.
    if (kind != "theorem" or not isinstance(title, str)
            or not all(type(n) is int for n in (first, last, start, end, offset))
            or not (0 <= start <= offset < end <= len(source))
            or first != source.count("\n", 0, start) + 1
            or last != source.count("\n", 0, end - 1) + 1):
        return False
    masked = latex_parser.masked_source(source)
    command = latex_parser.COMMAND.match(masked, offset)
    if command is None or command.group(1) != "label":
        return False
    argument = latex_parser.read_argument(masked, command.end())
    return argument is not None and argument[0].strip() == label


def owner_status(con: sqlite3.Connection, module: str, label: str,
                 source: str) -> tuple[str, str | None]:
    """Return current local owner, or a specific fail-closed index status.

    The document digest must be checked independently by the caller.
    """
    rows = con.execute(
        "SELECT e.id FROM labels AS l JOIN entities AS e ON e.id=l.entity_id "
        "WHERE e.document_id=? AND l.name=? ORDER BY e.id LIMIT 2",
        (module, label)).fetchall()
    if not rows:
        return "unlinked_label", None
    if len(rows) != 1:
        return "ambiguous_label", None
    # labels is the parser's legacy globally-unique lookup. Duplicates
    # anywhere in the library are recorded in label_conflicts (including the
    # original owner). Never endorse the first owner of a global collision.
    conflicts_table = con.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name='label_conflicts'"
    ).fetchone()
    if conflicts_table is not None and con.execute(
        "SELECT 1 FROM label_conflicts WHERE name=? LIMIT 1", (label,)
    ).fetchone() is not None:
        return "ambiguous_label", None

    entity_id = rows[0][0]
    binding = indexed_binding(con, module, label, entity_id)
    if binding is None or not valid_binding(binding, source, label):
        return "invalid_label_binding", None

    # The canonical parser also retains every original occurrence. Its entry
    # must agree with the legacy label index, not merely share a text name.
    occurrences_table = con.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name='label_occurrences'"
    ).fetchone()
    if occurrences_table is not None:
        occurrences = con.execute(
            "SELECT document_id,entity_id,offset FROM label_occurrences "
            "WHERE name=? LIMIT 2", (label,)
        ).fetchall()
        if len(occurrences) > 1:
            return "ambiguous_label", None
        if (len(occurrences) != 1
                or tuple(occurrences[0]) != (module, entity_id, binding[7])):
            return "invalid_label_binding", None
    return "ok", entity_id


def binding_sha256(module: str, label: str, binding: tuple) -> str:
    """Immutable indexed-owner identity for versioned Lean execution history.

    The document SHA does not change when SQLite reassigns an existing label.
    Include the exact owner and every indexed boundary/metadata field so a
    cached compilation cannot silently migrate to a different source object.
    Caller must first establish owner_status == "ok".
    """
    if (not isinstance(module, str) or not module
            or not isinstance(label, str) or not label
            or not isinstance(binding, tuple) or len(binding) != 8
            or not isinstance(binding[0], str) or not binding[0]
            or not all(type(v) is int for v in binding[3:])):
        raise ValueError("Invalid indexed source binding")
    payload = {
        "schema": 1,
        "source_module": module,
        "source_label": label,
        "entity_id": binding[0],
        "entity_kind": binding[1],
        "entity_title": binding[2],
        "start_line": binding[3],
        "end_line": binding[4],
        "start_offset": binding[5],
        "end_offset": binding[6],
        "label_offset": binding[7],
    }
    return hashlib.sha256(json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")).hexdigest()
