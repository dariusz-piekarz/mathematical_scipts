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
BASELINE = Path(__file__).resolve().parents[1] / "config/pending_reference_baseline.json"


def load_pending_baseline() -> dict:
    """Return exact source-and-target exceptions, never a fake label owner.

    The lists are audit obligations, not resolutions. New missing/ambiguous
    references are NOT allowed merely because their book is incomplete.
    """
    data = json.loads(BASELINE.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        raise ValueError("Unsupported pending-reference baseline schema")
    return data



def triage(db: Path) -> dict:
    baseline = load_pending_baseline()
    forward = baseline["documented_forward_references"]
    incomplete_dg = baseline["incomplete_dg_scope_manual_review"]
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
        source = row["source_document"]
        target = row["target_label"]
        source_dg = source.startswith("DG-")
        known_forward = (
            row["status"] == "missing" and target in forward.get(source, {})
        )
        known_dg = (
            row["status"] == "missing" and source_dg and not dg_complete
            and target in incomplete_dg.get(source, [])
        )
        row["known_pending"] = bool(known_forward or known_dg)
        row["pending_kind"] = (
            "documented_future_reference" if known_forward else
            "incomplete_DG_scope_review" if known_dg else None
        )
        row["review_queue"] = (
            "documented_future_chapter_not_yet_imported"
            if known_forward else
            "DG_incomplete_scope_manual_target_check"
            if source_dg and not dg_complete else
            "ambiguous_target_manual_review"
            if row["status"] == "ambiguous" else
            "missing_target_manual_review"
            if row["status"] == "missing" else
            "unknown_status_manual_review"
        )
        if known_forward:
            row["planned_target"] = forward[source][target]
        row["requires_mathematical_review"] = True
        unresolved.append(row)
    pending_count = sum(bool(r["known_pending"]) for r in unresolved)
    return {
        "dg_scope_complete": dg_complete,
        "unresolved_occurrences": len(unresolved),
        "documented_pending_occurrences": pending_count,
        "unclassified_unresolved_occurrences": len(unresolved) - pending_count,
        "items": unresolved,
        "policy": ("Documented pending targets are NOT resolved. Every occurrence "
                   "requires source-level review; any newly missing or ambiguous "
                   "reference fails the CI guard until reviewed. Incomplete DG "
                   "imports never justify inventing a target label."),
    }


def markdown(report: dict) -> str:
    out = [
        "# Nierozwiązane odsyłacze — kolejka audytu matematycznego",
        "",
        f"Wystąpienia: **{report['unresolved_occurrences']}**. "
        f"Import DG 01–36 kompletny: **{'tak' if report['dg_scope_complete'] else 'nie'}**.",
        f"Udokumentowane, nadal nierozwiązane: **{report['documented_pending_occurrences']}**. "
        f"Nowe / wymagające klasyfikacji: **{report['unclassified_unresolved_occurrences']}**.",
        "",
        "| Rozdział i wiersz | Plik | Komenda | Etykieta | Status | Kolejka | Znany zaległy? |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in report["items"]:
        vals = [f"{r['source_document']}:{r['line']}", r["source_path"],
                "\\\\" + r["command"], r["target_label"], r["status"],
                r["review_queue"], "tak" if r["known_pending"] else "nie"]
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
    parser.add_argument(
        "--fail-on-unclassified", action="store_true",
        help="Exit 3 if newly missing/ambiguous targets occur outside the "
             "exact reviewed pending-reference baseline."
    )
    args = parser.parse_args()
    report = triage(args.db)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.with_suffix(".json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    args.out.with_suffix(".md").write_text(markdown(report), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    if args.fail_on_unclassified and report["unclassified_unresolved_occurrences"]:
        for item in report["items"]:
            if not item["known_pending"]:
                print("UNCLASSIFIED REFERENCE:",
                      item["source_document"], item["line"],
                      item["target_label"], item["status"])
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
