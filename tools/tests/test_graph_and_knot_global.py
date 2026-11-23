#!/usr/bin/env python3
"""Global structural audit for the entire 44-source graph-and-knot textbook.

This is a *structural* and duplicate-risk audit, not a mathematical proof.
Writes a machine-readable report for independently inspecting the findings.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
import argparse
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
BOOK_PATH = Path("books/pl/graph_and_knot_theory.tex")
CATALOG_PATH = Path("catalog/books.json")
SOURCE_DIRECTORY = Path("chapters/pl/graph_and_knot_theory")
REPORT_PATH = Path("audit_output/graph_knot_global_audit.json")

INPUT = re.compile(r"\\input\{\.\./\.\./(chapters/pl/graph_and_knot_theory/[^}]+)\}")
LABEL = re.compile(r"\\label\{([^{}]+)\}")
REFERENCE = re.compile(r"\\(?:ref|eqref|pageref|autoref|cref|Cref)\{([^{}]+)\}")
ENV = re.compile(r"\\(begin|end)\{([a-zA-Z*]+)\}")
KEYWORDS = {
    "podstawy": ("graf", "krawędź", "wierzchołek"),
    "algorytmy": ("algorytm", "złożoność", "bfs", "dfs"),
    "laplasjan": ("laplasjan", "spektraln", "wartości własne"),
    "węzły": ("węzeł", "splot", "kirby"),
    "rozmaitości": ("rozmaitość", "chirurgia", "homologia"),
}
FORBIDDEN = {
    "zwartościowanie": re.compile(r"zwartościowani\w*", re.I),
    "zbieżność zwarta": re.compile(r"zbieżnoś\w*\s+zwar\w*", re.I),
    "tensorowanie": re.compile(r"tensorowani\w*", re.I),
    "pierwszo-przeliczalny": re.compile(r"(?:pierwszo|drugo)-przeliczal\w*", re.I),
    "samodzielne angielskie dual": re.compile(r"(?<![a-zA-Z])dual(?![a-zA-Z])", re.I),
}


def clean_comments(text: str) -> str:
    """Remove LaTeX % comments unless the percent is escaped by an odd count of \\."""
    lines = []
    for line in text.splitlines():
        result = []
        for index, ch in enumerate(line):
            if ch == "%":
                slash_count = 0
                back = index - 1
                while back >= 0 and line[back] == "\\":
                    slash_count += 1
                    back -= 1
                if slash_count % 2 == 0:
                    break
            result.append(ch)
        lines.append("".join(result))
    return "\n".join(lines)


def environment_errors(text: str) -> list[dict]:
    stack: list[tuple[str, int]] = []
    problems = []
    for match in ENV.finditer(text):
        kind, name = match.groups()
        lineno = text.count("\n", 0, match.start()) + 1
        if kind == "begin":
            stack.append((name, lineno))
        elif not stack:
            problems.append({"kind": "unmatched_end", "name": name, "line": lineno})
        elif stack[-1][0] != name:
            problems.append({"kind": "mismatch", "name": name, "line": lineno,
                             "expected": stack[-1][0]})
            # Remove matching inner entry if possible; otherwise continue.
            if any(x[0] == name for x in stack):
                while stack and stack[-1][0] != name:
                    stack.pop()
                stack.pop()
        else:
            stack.pop()
    problems.extend({"kind": "unclosed_begin", "name": name, "line": lineno}
                    for name, lineno in stack)
    return problems


def shingles(text: str, width: int = 18) -> set[tuple[str, ...]]:
    # Compare textual passages after removing TeX commands, math markup and comments.
    stripped = re.sub(r"\\[a-zA-Z]+\*?", " ", text)
    stripped = re.sub(r"[^a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ]+", " ", stripped.lower())
    words = stripped.split()
    return set(tuple(words[i:i+width])
               for i in range(max(0, len(words)-width+1)))


def audit() -> dict:
    catalog = json.loads((ROOT / CATALOG_PATH).read_text(encoding="utf-8"))
    book_entry = next(b for b in catalog["books"] if b["id"] == "graph_and_knot_theory")
    book_text = (ROOT / BOOK_PATH).read_text(encoding="utf-8")
    chapter_paths = INPUT.findall(book_text)
    chapter_ids = [Path(x).name.split("-", 1)[0] for x in chapter_paths]
    listed = list(book_entry["chapters"])
    actual = sorted(str(p.relative_to(ROOT))
                    for p in (ROOT / SOURCE_DIRECTORY).glob("*.tex"))
    results = {
        "book": str(BOOK_PATH),
        "source_count": len(chapter_paths),
        "catalog_count": len(listed),
        "catalog_matches_book": listed == chapter_paths,
        "source_paths_match_directory": sorted(chapter_paths) == actual,
        "sources": [],
        "duplicate_labels": [],
        "unresolved_references": [],
        "forbidden_language": [],
        "environment_errors": [],
        "unclosed_proofs": [],
        "forward_references": [],
        "duplicate_passage_candidates": [],
        "chapter_ids": chapter_ids,
        "chapter_ids_unique": len(chapter_ids) == len(set(chapter_ids)),
    }
    all_labels = defaultdict(list)
    all_references = []
    shingles_by_file = {}
    theorem_envs = ("twierdzenie", "lemat", "stwierdzenie", "wniosek")
    total_proofs = total_theorems = total_figures = 0
    for i, path in enumerate(chapter_paths):
        raw = (ROOT / path).read_text(encoding="utf-8")
        text = clean_comments(raw)
        labels = LABEL.findall(text)
        references = REFERENCE.findall(text)
        for item in labels:
            all_labels[item].append({"source": path, "index": i})
        for item in references:
            all_references.append({"label": item, "source": path, "index": i})
        enverr = environment_errors(text)
        if enverr:
            results["environment_errors"].append({"source": path, "errors": enverr})
        bad_terms = []
        for word, pattern in FORBIDDEN.items():
            for match in pattern.finditer(text):
                bad_terms.append({"term": word, "excerpt":
                                  text[max(0, match.start()-50):match.end()+50]})
        if bad_terms:
            results["forbidden_language"].append({"source": path, "matches": bad_terms[:30]})
        theorem_count = sum(len(re.findall(r"\\begin\{" + name + r"\}", text))
                            for name in theorem_envs)
        proof_count = len(re.findall(r"\\begin\{proof\}", text))
        figure_count = len(re.findall(r"\\begin\{(?:figure|tikzpicture)\}", text))
        total_theorems += theorem_count
        total_proofs += proof_count
        total_figures += figure_count
        # Not every theorem is proved here: accepted external results are allowed.
        results["sources"].append({
            "source": path,
            "bytes": len(raw.encode("utf-8")),
            "labels": len(labels),
            "references": len(references),
            "theorems_and_lemmas": theorem_count,
            "proofs": proof_count,
            "figures_and_tikz": figure_count,
            "sections": len(re.findall(r"\\section(?:\[[^\]]*\])?\{", text)),
            "has_chapter_heading": bool(re.search(r"\\chapter\*?\{", text[:700])),
        })
        shingles_by_file[path] = shingles(text)

    results["total"] = {
        "theorems_and_lemmas": total_theorems,
        "proofs": total_proofs,
        "figures_and_tikz": total_figures,
        "labels": sum(len(v) for v in all_labels.values()),
        "references": len(all_references),
    }

    for label, positions in all_labels.items():
        if len(positions) > 1:
            results["duplicate_labels"].append({"label": label, "locations": positions})
    results["unresolved_references"] = [
        item for item in all_references if item["label"] not in all_labels
    ]
    for item in all_references:
        defs = all_labels.get(item["label"], [])
        if len(defs) == 1 and defs[0]["index"] > item["index"]:
            results["forward_references"].append({
                "source": item["source"],
                "target": defs[0]["source"],
                "label": item["label"],
            })

    for a, b in combinations(chapter_paths, 2):
        shared = shingles_by_file[a] & shingles_by_file[b]
        if len(shared) >= 6:
            results["duplicate_passage_candidates"].append({
                "source_a": a, "source_b": b, "matching_18_word_windows": len(shared),
                "example": " ".join(next(iter(sorted(shared))))
            })
    results["duplicate_passage_candidates"].sort(
        key=lambda item: -item["matching_18_word_windows"]
    )
    return results


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true",
                        help="fail on structural integrity violations")
    parser.add_argument("--output", default=str(REPORT_PATH))
    args = parser.parse_args()
    result = audit()
    output = ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n",
                      encoding="utf-8")
    print("GLOBAL GRAPH/KNOT AUDIT")
    print("sources/catalog:", result["source_count"], result["catalog_count"])
    print("catalog matches inputs:", result["catalog_matches_book"])
    print("directory matches:", result["source_paths_match_directory"])
    print("unique source IDs:", result["chapter_ids_unique"])
    print("totals:", result["total"])
    for key in ("duplicate_labels", "unresolved_references",
                "environment_errors", "forbidden_language",
                "forward_references", "duplicate_passage_candidates"):
        print(key, len(result[key]))
        for item in result[key][:15]:
            print("  ", json.dumps(item, ensure_ascii=False)[:400])
    print("Saved machine-readable audit:", output.relative_to(ROOT))
    structural = ("catalog_matches_book", "source_paths_match_directory",
                  "chapter_ids_unique")
    errors = any(not result[k] for k in structural)
    errors |= any(result[k] for k in ("duplicate_labels",
                                      "unresolved_references",
                                      "environment_errors"))
    return int(args.strict and errors)


if __name__ == "__main__":
    sys.exit(main())
