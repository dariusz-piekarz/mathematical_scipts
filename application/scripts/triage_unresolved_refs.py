"""Emit a compact, actionable inventory of unresolved LaTeX references.

This script classifies *review priority*, not the mathematical correctness of
a proposed target. It does not modify canonical sources or the SQLite index.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sqlite3
from contextlib import closing

RESOLVED = frozenset({"resolved", "external_resolved",
                      "alias_resolved", "included_resolved"})


def triage(db: Path) -> dict:
    with closing(sqlite3.connect(f"file:{db.resolve()}?mode=ro", uri=True)) as con:
        con.row_factory = sqlite3.Row
        ids = {r["id"] for r in con.execute("SELECT id FROM documents")}
        records = [dict(r) for r in con.execute("""
            SELECT r.source_document, d.path AS source_path,
                   r.command, r.target_label, r.line, r.status
            FROM references_tex AS r
            JOIN documents AS d ON d.id = r.source_document
            ORDER BY r.source_document, r.line, r.offset, r.target_label
        """)]
    dg_complete = all(f"DG-{i:02d}" in ids for i in range(1, 37))
    unresolved = []
    for row in records:
        if row["status"] in RESOLVED:
            continue
        source_dg = row["source_document"].startswith("DG-")
        row["review_queue"] = (
            "DG_incomplete_scope_manual_target_check"
            if source_dg and not dg_complete else
            "ambiguous_target_manual_review"
            if row["status"] == "ambiguous" else
            "missing_target_manual_review"
            if row["status"] == "missing" else
            "unknown_status_manual_review"
        )
        row["requires_mathematical_review"] = True
        unresolved.append(row)
    return {
        "dg_scope_complete": dg_complete,
        "unresolved_occurrences": len(unresolved),
        "items": unresolved,
        "policy": ("No automatic renaming, no inferred theorem equivalence, "
                   "no assumption that a missing DG label exists in an unimported chapter."),
    }


def markdown(report: dict) -> str:
    out = [
        "# Nierozwiązane odsyłacze — kolejka audytu matematycznego",
        "",
        f"Wystąpienia: **{report['unresolved_occurrences']}**. "
        f"Import DG 01–36 kompletny: **{'tak' if report['dg_scope_complete'] else 'nie'}**.",
        "",
        "| Rozdział i wiersz | Plik | Komenda | Etykieta | Status | Kolejka |",
        "|---|---|---|---|---|---|",
    ]
    for r in report["items"]:
        vals = [f"{r['source_document']}:{r['line']}", r["source_path"],
                "\\\\" + r["command"], r["target_label"], r["status"],
                r["review_queue"]]
        out.append("| " + " | ".join(
            str(v).replace("|", "\\|").replace("\n", " ") for v in vals
        ) + " |")
    out.extend(["", "**Zasada:** " + report["policy"],
                "", "Żadna pozycja nie jest uznana za rozwiązaną bez kontroli źródła i celu.",
                ""])
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path,
                        help="Output prefix for .json and .md")
    args = parser.parse_args()
    report = triage(args.db)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.with_suffix(".json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    args.out.with_suffix(".md").write_text(markdown(report), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
