"""Read-only, exhaustive reference/provenance audit of a canonical SQLite index.

Usage: python scripts/audit_reference_provenance.py --db data/biblioteka.db --out data/reference_audit

Never alters the index, original LaTeX, labels, or an existing generated report.
Ambiguities are reported as candidates, NOT automatically resolved.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import sqlite3
from contextlib import closing
from typing import Any


def _single_line(value: Any, limit: int = 170) -> str:
    return " ".join(str(value if value is not None else "").split())[:limit]


def _table_cell(value: Any) -> str:
    return _single_line(value, 10000).replace("|", "\\|").replace("`", "'")


def audit(con: sqlite3.Connection) -> dict[str, Any]:
    con.row_factory = sqlite3.Row
    documents = {r["id"]: dict(r) for r in con.execute(
        "SELECT id,path,domain,title,sha256 FROM documents ORDER BY id"
    )}
    labels = {}
    for row in con.execute("SELECT name,document_id,entity_id,offset,line,excerpt FROM labels ORDER BY name,document_id"):
        labels.setdefault(row["name"], []).append(dict(row))
    for row in con.execute("SELECT name,document_id,entity_id,offset,line,excerpt FROM label_conflicts ORDER BY name,document_id"):
        owners = labels.setdefault(row["name"], [])
        if not any(x["document_id"] == row["document_id"] for x in owners):
            owners.append(dict(row))
    for owners in labels.values():
        owners.sort(key=lambda v: (v["document_id"], v["line"]))

    references = []
    all_references_by_label: dict[str, list[dict]] = {}
    status_counts: Counter[str] = Counter()
    for row in con.execute("""SELECT source_document,source_entity,command,target_label,line,offset,
                              target_document,target_entity,status FROM references_tex
                              ORDER BY source_document,line,offset,id"""):
        item = dict(row)
        all_references_by_label.setdefault(item["target_label"], []).append(item)
        status_counts[item["status"]] += 1
        if item["status"] in {"resolved", "external_resolved", "alias_resolved", "included_resolved"}:
            continue
        item["source_path"] = documents[item["source_document"]]["path"]
        item["source_sha256"] = documents[item["source_document"]]["sha256"]
        candidates = []
        for owner in labels.get(item["target_label"], []):
            doc = documents[owner["document_id"]]
            candidates.append({
                "document_id": owner["document_id"], "path": doc["path"],
                "domain": doc["domain"], "sha256": doc["sha256"],
                "entity_id": owner["entity_id"], "line": owner["line"],
                "excerpt": _single_line(owner["excerpt"], 240),
                "local_to_source": owner["document_id"] == item["source_document"],
            })
        item["candidates"] = candidates
        if item["status"] == "missing":
            item["diagnosis"] = "no_indexed_label_owner"
        elif item["status"] == "ambiguous":
            item["diagnosis"] = "multiple_owners_no_local_precedence"
        else:
            item["diagnosis"] = "unknown_reference_status"
        references.append(item)

    conflict_names = sorted(name for name, owners in labels.items() if len(owners) > 1)
    usage = Counter(r["target_label"] for r in references)
    conflicts = []
    collision_kinds: Counter[str] = Counter()
    for name in conflict_names:
        owners = labels[name]
        all_mentions = all_references_by_label.get(name, [])
        owner_scripts = sorted({o["document_id"].split("-", 1)[0] for o in owners})
        multiple_within_script = len(owner_scripts) < len(owners)
        ambiguous_count = sum(r["status"] == "ambiguous" for r in all_mentions)
        if ambiguous_count:
            collision_class = "ambiguous_reference"
        elif multiple_within_script and all_mentions:
            collision_class = "referenced_same_script_collision"
        elif multiple_within_script:
            collision_class = "unreferenced_same_script_collision"
        elif all_mentions:
            collision_class = "referenced_cross_script_shared_name"
        else:
            collision_class = "unreferenced_cross_script_shared_name"
        collision_kinds[collision_class] += 1
        conflicts.append({
            "label": name, "owner_count": len(owners),
            "owner_scripts": owner_scripts,
            "same_script_collision": multiple_within_script,
            "risk_class": collision_class,
            "all_reference_count": len(all_mentions),
            "resolved_reference_count": sum(
                r["status"] in {"resolved", "external_resolved", "alias_resolved", "included_resolved"}
                for r in all_mentions),
            "ambiguous_reference_count": ambiguous_count,
            "unresolved_reference_count": usage[name],
            "owners": [
                {"document_id": owner["document_id"],
                 "path": documents[owner["document_id"]]["path"],
                 "sha256": documents[owner["document_id"]]["sha256"],
                 "domain": documents[owner["document_id"]]["domain"],
                 "entity_id": owner["entity_id"], "line": owner["line"],
                 "excerpt": _single_line(owner["excerpt"], 240)}
                for owner in owners
            ],
        })

    priority_order = {
        "ambiguous_reference": 0,
        "referenced_same_script_collision": 1,
        "unreferenced_same_script_collision": 2,
        "referenced_cross_script_shared_name": 3,
        "unreferenced_cross_script_shared_name": 4,
    }
    priority_queue = sorted(
        conflicts, key=lambda row: (
            priority_order[row["risk_class"]],
            -row["all_reference_count"],
            -row["owner_count"],
            row["label"]
        )
    )
    missing_labels = sorted({r["target_label"] for r in references if r["status"] == "missing"})
    ambiguous_labels = sorted({r["target_label"] for r in references if r["status"] == "ambiguous"})
    return {
        "schema_version": 1,
        "source": "read-only SQLite index; canonical sources unchanged",
        "counts": {
            "documents": len(documents),
            "indexed_labels": len(labels),
            "reference_statuses": dict(sorted(status_counts.items())),
            "unresolved_occurrences": len(references),
            "missing_label_names": len(missing_labels),
            "ambiguous_label_names": len(ambiguous_labels),
            "conflicting_label_names": len(conflicts),
            "same_script_collision_names": sum(r["same_script_collision"] for r in conflicts),
            "cross_script_only_collision_names": sum(not r["same_script_collision"] for r in conflicts),
            "referenced_collision_names": sum(r["all_reference_count"] > 0 for r in conflicts),
            "ambiguous_colliding_reference_occurrences": sum(r["ambiguous_reference_count"] for r in conflicts),
            "collision_risk_classes": dict(sorted(collision_kinds.items())),
        },
        "unresolved_references": references,
        "label_conflicts": conflicts,
        "collision_priority_queue": [
            {
                "label": item["label"], "risk_class": item["risk_class"],
                "all_reference_count": item["all_reference_count"],
                "owner_scripts": item["owner_scripts"],
                "owners": [(o["document_id"], o["line"]) for o in item["owners"]]
            }
            for item in priority_queue
        ],
        "policy": "No automatic label renaming, owner choice, source modification, or proof merging."
    }


def markdown(report: dict[str, Any]) -> str:
    counts = report["counts"]
    lines = ["# Audyt odsyłaczy — mapa pochodzenia (bez zmian źródeł)", "",
             "Zestaw wygenerowano z indeksu SQLite; każdy cel niejednoznaczny wymaga audytu treści i kontekstu matematycznego.",
             "Nie poprawiano etykiet ani dowodów automatycznie.", "",
             "## Podsumowanie", "",
             f"- Zaindeksowane rozdziały: **{counts['documents']}**.",
             f"- Wystąpienia nierozwiązanych odsyłaczy: **{counts['unresolved_occurrences']}**.",
             f"- Nazwy brakujących etykiet: **{counts['missing_label_names']}**.",
             f"- Nazwy niejednoznacznie cytowanych etykiet: **{counts['ambiguous_label_names']}**.",
             f"- Wszystkie nazwy etykiet o wielu właścicielach: **{counts['conflicting_label_names']}**.",
             f"- Kolizje w jednym skrypcie: **{counts['same_script_collision_names']}**.",
             f"- Kolizje wyłącznie między skryptami: **{counts['cross_script_only_collision_names']}**.",
             f"- Nazwy kolizyjne cytowane w źródłach: **{counts['referenced_collision_names']}**.",
             f"- Niejednoznaczne cytowania kolizyjne: **{counts['ambiguous_colliding_reference_occurrences']}**.",
             f"- Statusy odsyłaczy: `{json.dumps(counts['reference_statuses'], ensure_ascii=False, sort_keys=True)}`.", "",
             "## Nierozwiązane wystąpienia (wszystkie)", "",
             "| Status | Źródło : wiersz | Etykieta docelowa | Kandydaci (rozdział : wiersz) |",
             "|---|---|---|---|"]
    for r in report["unresolved_references"]:
        candidates = "; ".join(f"{o['document_id']}:{o['line']}" for o in r["candidates"]) or "brak właściciela"
        lines.append("| " + " | ".join(_table_cell(x) for x in [r["status"],
            f"{r['source_document']}:{r['line']} ({r['source_path']})", r["target_label"], candidates]) + " |")
    lines.extend(["", "## Kolejka audytu według rzeczywistego wykorzystania — pierwsze 25", "",
                  "| Klasa ryzyka | Etykieta | Skrypty właścicieli | Liczba cytowań | Właściciele |",
                  "|---|---|---|---:|---|"])
    for item in report["collision_priority_queue"][:25]:
        lines.append("| " + " | ".join(_table_cell(x) for x in [
            item["risk_class"], item["label"],
            ", ".join(item["owner_scripts"]),
            item["all_reference_count"],
            "; ".join(f"{doc}:{line}" for doc, line in item["owners"])
        ]) + " |")
    lines.extend(["", "## Powielone nazwy etykiet (wszystkie)", "",
                  "| Etykieta | Liczba właścicieli | Niejednoznaczne cytowania | Właściciele / pliki |",
                  "|---|---:|---:|---|"])
    for item in report["label_conflicts"]:
        owners = "; ".join(f"{o['document_id']}:{o['line']} ({o['path']})" for o in item["owners"])
        lines.append("| " + " | ".join(_table_cell(x) for x in [item["label"],
            item["owner_count"], item["ambiguous_reference_count"], owners]) + " |")
    lines.extend(["", "## Zasady rozstrzygania", "",
                  "1. Otworzyć źródło cytowania oraz wszystkich kandydatów; porównać treść, założenia i dowody.",
                  "2. Nie utożsamiać identycznych nazw etykiet z identycznymi twierdzeniami.",
                  "3. Wskazać docelowy rozdział tylko przy jednoznacznym matematycznym uzasadnieniu; zachować wszystkie różne dowody.",
                  "4. Przed zmianą etykiet sporządzić mapę stara etykieta → nowa etykieta z kontekstem i zachować historię pochodzenia.",
                  "5. Po każdej zaakceptowanej korekcie przebudować indeks i sprawdzić `xr-hyper` i testy przeglądarkowe.", ""])
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True,
                        help="Output prefix without extension; .json and .md are written")
    args = parser.parse_args(argv)
    if not args.db.is_file():
        parser.error(f"No SQLite database: {args.db}")
    with closing(sqlite3.connect(f"file:{args.db.resolve()}?mode=ro", uri=True)) as con:
        con.row_factory = sqlite3.Row
        result = audit(con)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.with_suffix(".json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    args.out.with_suffix(".md").write_text(markdown(result), encoding="utf-8")
    print(json.dumps(result["counts"], ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())