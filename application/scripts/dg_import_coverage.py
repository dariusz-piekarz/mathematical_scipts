"""Read-only coverage gate for the 36-chapter differential-geometry source.

Reports what can be checked now; re-run automatically after importing the
remaining canonical chapters. Never fabricates an absent label or chapter.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sqlite3

EXPECTED = 36

def coverage(db: Path) -> dict:
    with sqlite3.connect(f"file:{db.resolve()}?mode=ro",uri=True) as con:
        con.row_factory=sqlite3.Row
        imported=[r[0] for r in con.execute(
            "SELECT id FROM documents WHERE id LIKE 'DG-%' ORDER BY id")]
        missing=[dict(r) for r in con.execute("""
            SELECT source_document, target_label, line FROM references_tex
            WHERE source_document LIKE 'DG-%' AND status='missing'
            ORDER BY source_document,line,offset""")]
    return {
        "expected_chapters": EXPECTED,
        "imported_chapters": len(imported),
        "imported_ids": imported,
        "not_yet_imported": max(0,EXPECTED-len(imported)),
        "scope_complete": len(imported)>=EXPECTED,
        "unresolved_refs_in_imported_scope": missing,
        "unresolved_count": len(missing),
        "assessment": ("ready_for_full_36_chapter_reference_audit"
                       if len(imported)>=EXPECTED else "awaiting_remaining_chapter_import"),
        "warning": ("A missing label among the currently imported chapters does not prove"
                    " the target is absent from the complete 36-chapter script."),
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--db",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True)
    args=p.parse_args()
    output=coverage(args.db)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(output,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:output[k] for k in (
        "expected_chapters","imported_chapters","not_yet_imported",
        "scope_complete","unresolved_count","assessment")},ensure_ascii=False))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
