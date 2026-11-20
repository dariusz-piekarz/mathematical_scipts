"""Cross-volume source audit: algebraic topology, differential and algebraic geometry.

No labels are renamed. Same-label occurrences in distinct source files are
REVIEW CANDIDATES, never automatic declarations of theorem equivalence.

Usage:
  python application/scripts/audit_cross_volume_geometry_topology.py \
      --out application/docs/generated/cross_volume_geometry_topology.json
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
BOOKS = {
    "AT": ROOT / "books/pl/algebraic_topology.tex",
    "DG": ROOT / "books/pl/differential_geometry_and_topology.tex",
    "AG": ROOT / "books/pl/algebraic_geometry.tex",
}
INPUT_RE = re.compile(r"\\(?:input|include)\s*\{([^}]+)\}")
LABEL_RE = re.compile(r"\\label\s*\{([^}]+)\}")
REF_RE = re.compile(r"\\(?:ref|eqref|autoref|pageref|nameref|cref|Cref)\s*\{([^}]+)\}")

# Review-only alignment of subject matter: no proof of mathematical identity.
REVIEW_PAIRS = (
    ("AT-02", "DG-05", "Grupy, pierścienie i moduły"),
    ("AT-03", "DG-06", "Kompleksy, funktory homologiczne i dokładność"),
    ("AT-04", "DG-07", "Homotopia, nakrycia, CW"),
    ("AT-05", "DG-08", "Homologia przestrzeni"),
    ("AT-06", "DG-09", "Wyższe grupy homotopii"),
    ("AT-09", "DG-10", "Formy i kohomologia de Rhama"),
    ("AT-11", "DG-17", "Dualność i klasy charakterystyczne"),
    ("AT-18", "DG-18", "Homologia Morse'a i przepływy"),
    ("AT-28", "AG-10", "Słaby i silny Lefschetz, przecięcia, rozdmuchania"),
    ("AT-28", "AG-09", "Kähler i twierdzenia Hodge'a"),
    ("AT-28", "AG-06", "Rozdmuchanie i powierzchnie"),
    ("AT-30", "DG-01", "Rozmaitości, przestrzenie styczne"),
    ("AT-30", "DG-03", "Algebra zewnętrzna"),
    ("AT-30", "DG-15", "Sard i transwersalność"),
    ("AT-30", "DG-16", "Otoczenia tubularne"),
)

SHARED = {
    "slabe_twierdzenie_lefschetza.tex",
    "rozdmuchanie_punktu_normalna.tex",
    "rozdmuchanie_punktu_kohomologia.tex",
}


def strip_tex_comments(src: str) -> str:
    """Remove comments but retain an escaped percent and line boundaries."""
    out = []
    for line in src.splitlines():
        stop = len(line)
        for pos, char in enumerate(line):
            if char == "%":
                backslashes = 0
                j = pos - 1
                while j >= 0 and line[j] == "\\":
                    backslashes += 1
                    j -= 1
                if backslashes % 2 == 0:
                    stop = pos
                    break
        out.append(line[:stop])
    return "\n".join(out)


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_sources(book: Path) -> list[dict]:
    """Expand all literal TeX inclusions in actual book order.

    Paths such as ../../shared/pl/X are relative to the working directory
    books/pl in the canonical book, NOT to the chapter directory.
    """
    stack = set()
    files = []

    def visit(path: Path):
        path = path.resolve()
        if path in stack:
            raise RuntimeError(f"Cyclic TeX include: {relative(path)}")
        if not path.is_file():
            raise FileNotFoundError(f"Missing canonical TeX dependency: {path}")
        if not path.is_relative_to(ROOT):
            raise ValueError(f"External include forbidden: {path}")
        stack.add(path)
        data = strip_tex_comments(path.read_text(encoding="utf-8-sig"))
        files.append({
            "path": relative(path),
            "labels": [m.group(1) for m in LABEL_RE.finditer(data)],
            "refs": [
                {"label": m.group(1),
                 "line": data.count("\n", 0, m.start()) + 1}
                for m in REF_RE.finditer(data)
            ],
        })
        for match in INPUT_RE.finditer(data):
            name = match.group(1)
            child = (book.parent / name).resolve()
            if child.suffix == "":
                child = child.with_suffix(".tex")
            visit(child)
        stack.remove(path)

    visit(book)
    return files


def _chapter_id(path: str, volume: str) -> str:
    if path.startswith("chapters/pl/"):
        file = path.rsplit("/", 1)[-1]
        num = file.partition("-")[0]
        if num.isdigit():
            return f"{volume}-{num}"
    return path


def audit() -> dict:
    books = {}
    all_owners = defaultdict(set)
    file_owners = defaultdict(set)
    for vol, book in BOOKS.items():
        files = read_sources(book)
        own = defaultdict(set)
        seen = Counter()
        for file in files:
            seen[file["path"]] += 1
            for label in file["labels"]:
                own[label].add(file["path"])
                all_owners[label].add(file["path"])
                file_owners[file["path"]].add(vol)
        books[vol] = {
            "book": relative(book),
            "files": files,
            "label_sources": own,
            "repeated_files": {
                path: n for path, n in seen.items() if n > 1
            },
            "chapter_count": sum(
                file["path"].startswith(f"chapters/pl/{folder}/")
                for file in files
                for folder in [{
                    "AT": "algebraic_topology",
                    "DG": "differential_geometry_and_topology",
                    "AG": "algebraic_geometry",
                }[vol]]
            ),
        }
    collisions = []
    for label, origins in sorted(all_owners.items()):
        if len(origins) > 1:
            byvol = {
                vol: sorted(p for p in origins if
                            any(f["path"] == p for f in books[vol]["files"]))
                for vol in BOOKS
            }
            collisions.append({
                "label": label,
                "source_files": sorted(origins),
                "volume_owners": {k: v for k, v in byvol.items() if v},
                "status": "requires_manual_mathematical_disambiguation",
            })

    result = {
        "policy": {
            "rename_labels": False,
            "merge_copies_automatically": False,
            "same_label_different_files_implies_same_theorem": False,
            "shared_source_path_is_intentional_reuse": True,
            "unimported_DG_chapters": "DG canonically imports 20 of 36 source chapters; unresolved labels require review",
        },
        "volumes": {},
        "cross_volume_conflicts": collisions,
        "shared_source_reuse": {},
        "overlap_candidates": [],
    }
    for path, vols in sorted(file_owners.items()):
        if len(vols) > 1:
            result["shared_source_reuse"][path] = sorted(vols)

    for vol, obj in books.items():
        local = obj["label_sources"]
        missing = []
        foreign = []
        ref_count = 0
        for f in obj["files"]:
            for ref in f["refs"]:
                ref_count += 1
                name = ref["label"]
                if name in local:
                    continue
                global_paths = sorted(all_owners.get(name, ()))
                item = {
                    "from": f["path"],
                    "line": ref["line"],
                    "label": name,
                    "external_candidates": global_paths,
                }
                if global_paths:
                    item["status"] = (
                        "external_unique_unlinked"
                        if len(global_paths) == 1 else "external_ambiguous_unlinked"
                    )
                    foreign.append(item)
                else:
                    item["status"] = (
                        "not_in_imported_DG_scope"
                        if vol == "DG" else "missing_in_three_imported_volumes"
                    )
                    missing.append(item)
        local_collisions = [
            {"label": label, "paths": sorted(paths)}
            for label, paths in sorted(local.items()) if len(paths) > 1
        ]
        result["volumes"][vol] = {
            "book": obj["book"],
            "chapter_count": obj["chapter_count"],
            "unique_files": len(set(f["path"] for f in obj["files"])),
            "unique_labels": len(local),
            "refs": ref_count,
            "local_label_collisions": local_collisions,
            "unlinked_external_references": foreign,
            "unresolved_references": missing,
            "repeated_source_files": obj["repeated_files"],
        }

    chapters = defaultdict(dict)
    for vol, b in books.items():
        for f in b["files"]:
            if not f["path"].startswith("chapters/"):
                continue
            cid = _chapter_id(f["path"], vol)
            chapters[cid] = {"path": f["path"], "volume": vol}
    for a, b, subject in REVIEW_PAIRS:
        if a in chapters and b in chapters:
            result["overlap_candidates"].append({
                "left": a, "right": b, "subject": subject,
                "sources": [chapters[a]["path"], chapters[b]["path"]],
                "decision": "review_and_preserve_union_of_unique_content",
            })
    result["summary"] = {
        "chapters": {v: obj["chapter_count"] for v, obj in result["volumes"].items()},
        "cross_volume_conflict_labels": len(collisions),
        "shared_source_files": len(result["shared_source_reuse"]),
        "overlap_candidates": len(result["overlap_candidates"]),
        "unresolved": {
            v: len(obj["unresolved_references"])
            for v, obj in result["volumes"].items()
        },
        "external_unlinked": {
            v: len(obj["unlinked_external_references"])
            for v, obj in result["volumes"].items()
        },
        "within_volume_duplicate_labels": {
            v: len(obj["local_label_collisions"])
            for v, obj in result["volumes"].items()
        },
    }
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    data = audit()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(data, indent=2, ensure_ascii=False)
                        + "\n", encoding="utf-8")
    print(json.dumps(data["summary"], ensure_ascii=False))
    print("Shared source reuse:", data["shared_source_reuse"])
    for vol, info in data["volumes"].items():
        for item in info["unresolved_references"][:15]:
            print(f"Unresolved {vol}: {item['from']}:{item['line']} "
                  f"{item['label']} ({item['status']})")
        for item in info["unlinked_external_references"][:10]:
            print(f"External unlinked {vol}: {item['from']}:{item['line']} "
                  f"{item['label']} candidates={item['external_candidates']}")


if __name__ == "__main__":
    main()
