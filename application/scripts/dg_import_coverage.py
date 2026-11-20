"""Read-only coverage audit for the canonical 36-chapter differential geometry book.

Chapter identity matters: 36 documents do not imply DG-01 through DG-36
are present. This audit never fabricates missing chapters, labels or links.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sqlite3

EXPECTED = 36
EXPECTED_IDS = tuple(f"DG-{i:02d}" for i in range(1, EXPECTED + 1))
ID_PATTERN = re.compile(r"^DG-(\\d+)$")
RESOLVED = frozenset({"resolved", "external_resolved", "alias_resolved",
                      "included_resolved"})


def coverage(db: Path) -> dict:
    with sqlite3.connect(f"file:{db.resolve()}?mode=ro", uri=True) as con:
        con.row_factory = sqlite3.Row
        imported = [r["id"] for r in con.execute(
            "SELECT id FROM documents WHERE id LIKE 'DG-%' ORDER BY id"
        )]
        refs = [dict(r) for r in con.execute("""
            SELECT source_document, target_label, command, status, line
            FROM references_tex
            WHERE source_document LIKE 'DG-%'
            ORDER BY source_document, line, offset
        """)]
    expected = set(EXPECTED_IDS)
    present = set(imported)
    missing_ids = [name for name in EXPECTED_IDS if name not in present]
    unexpected_ids = sorted(present - expected)
    unresolved = [r for r in refs if r["status"] not in RESOLVED]
    status_counts = {}
    for r in refs:
        status_counts[r["status"]] = status_counts.get(r["status"], 0) + 1
    complete = not missing_ids and not unexpected_ids
    return {
        "expected_chapters": EXPECTED,
        "expected_ids": list(EXPECTED_IDS),
        "imported_chapters": len(imported),
        "imported_ids": imported,
        "missing_ids": missing_ids,
        "unexpected_ids": unexpected_ids,
        "not_yet_imported": len(missing_ids),
        "scope_complete": complete,
        "unresolved_refs_in_imported_scope": unresolved,
        "unresolved_count": len(unresolved),
        "reference_status_counts": dict(sorted(status_counts.items())),
        "assessment": ("ready_for_full_36_chapter_reference_audit"
                       if complete else "awaiting_remaining_chapter_import"),
        "warning": ("Static coverage is not a mathematical or TeX compilation audit. "
                    "A currently missing label may occur in a chapter not yet imported. "
                    "Even 36 imported chapters require separate reference and proof checks."),
    }


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--db", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    result = coverage(args.db)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n",
                        encoding="utf-8")
    print(json.dumps({key: result[key] for key in (
        "expected_chapters", "imported_chapters", "missing_ids",
        "unexpected_ids", "scope_complete", "unresolved_count", "assessment"
    )}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
