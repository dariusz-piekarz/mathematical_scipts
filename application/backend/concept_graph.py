"""Read-only concept and occurrence graph over canonical indexed TeX sources.

A catalog relation is a curated mathematical statement, never inferred from
the co-occurrence of terms. An occurrence edge only states that a phrase was
found at a source offset. Unknown queries get occurrence edges, not invented
mathematical implications.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
import math
import re
import sqlite3
from typing import Any

from backend.latex_parser import masked_source

@dataclass(frozen=True)
class Concept:
    key: str
    label: str
    aliases: tuple[str, ...]
    patterns: tuple[str, ...]

CATALOG: dict[str, Concept] = {
    "zorn": Concept("zorn", "Lemat Zorna",
        ("zorn", "zorna", "lemat zorna", "lemat kuratowskiego zorna"),
        (r"(?<!\w)Zorn\w*",)),
    "choice": Concept("choice", "Aksjomat wyboru (AC)",
        ("ac", "aksjomat wyboru", "aksjomatu wyboru", "zasada wyboru"),
        (r"\baksjomat\w*\s+wyboru\b", r"(?<![\w\\])AC(?!\w)")),
    "hausdorff_max": Concept("hausdorff_max", "Zasada maksymalności Hausdorffa",
        ("zasada maksymalności hausdorffa", "twierdzenie hausdorffa o maksymalności",
         "hausdorffa zasada maksymalności"),
        (r"\b(?:zasad\w*|twierdzeni\w*)\s+(?:o\s+)?maksymalno\w*\s+Hausdorff\w*",
         r"\bmaksymalno\w*\s+Hausdorff\w*",
         r"\bHausdorff\w*\s+(?:zasad\w*|twierdzeni\w*)\s+(?:o\s+)?maksymalno\w*")),
    "hamel": Concept("hamel", "Istnienie bazy Hamela",
        ("hamel", "hamela", "baza hamela", "bazy hamela", "istnienie bazy hamela"),
        (r"\bbaz\w*\s+Hamel\w*", r"\bHamel\w*")),
    "well_order": Concept("well_order", "Twierdzenie o dobrym uporządkowaniu",
        ("twierdzenie o dobrym uporządkowaniu", "dobre uporządkowanie",
         "twierdzenie o dobrym uporzadkowaniu"),
        (r"\b(?:twierdzeni\w*\s+o\s+)?dobr\w*\s+uporządkowan\w*",)),
    "hahn_banach": Concept("hahn_banach", "Twierdzenie Hahna–Banacha",
        ("hahn banach", "hahna banacha", "twierdzenie hahna banacha"),
        (r"\bHahn\w*\s*(?:--?|–|—)\s*Banach\w*",)),
}

# Every relationship is over ZF or an explicitly specified use of choice.
# Keep orientation even when the user opens the target as the central concept.
RELATIONS = (
    ("zorn", "choice", "equivalent", "Równoważne nad ZF",
     "Nad ZF lemat Zorna i aksjomat wyboru są równoważne."),
    ("zorn", "hausdorff_max", "equivalent", "Równoważne nad ZF",
     "Zasada maksymalności Hausdorffa i lemat Zorna są równoważne nad ZF."),
    ("zorn", "well_order", "equivalent", "Równoważne nad ZF",
     "Twierdzenie o dobrym uporządkowaniu jest równoważne lematowi Zorna nad ZF."),
    ("zorn", "hamel", "implies", "Implikuje",
     "Lemat Zorna zastosowany do częściowo uporządkowanej rodziny zbiorów liniowo niezależnych daje bazę Hamela."),
    ("zorn", "hahn_banach", "implies", "Używany w dowodzie",
     "Standardowy dowód przedłużania funkcjonału metodą elementów maksymalnych korzysta z lematu Zorna."),
)

PREFERRED_KINDS = {
    "theorem": 0, "definition": 1, "example": 2, "proof": 3,
    "lemma": 3, "corollary": 3, "section": 4, "subsection": 5,
    "subsubsection": 5, "chapter": 6,
}
MAX_MATCHES_PER_DOCUMENT = 80
MAX_OCCURRENCES_PER_DOCUMENT_AND_CONCEPT = 3

# Identifier arguments and comments are not textual occurrences. Keep every
# offset unchanged so evidence links still point into the canonical source.
INDEX_ONLY_COMMANDS = re.compile(
    r"\\(?:label|ref|eqref|pageref|autoref|nameref|cref|Cref|vref|Vref|"
    r"cite|citep|citet)\s*\{[^{}]*\}"
)


def searchable_source(content: str) -> str:
    cleaned = list(masked_source(content))
    for match in INDEX_ONLY_COMMANDS.finditer("".join(cleaned)):
        for offset in range(match.start(), match.end()):
            if cleaned[offset] != "\n":
                cleaned[offset] = " "
    return "".join(cleaned)



def normalize(text: str) -> str:
    return " ".join(re.findall(r"\w+", text.casefold(), re.UNICODE))


def resolve_concept(query: str) -> Concept:
    term = normalize(query)
    for concept in CATALOG.values():
        if term == normalize(concept.label) or any(term == normalize(a) for a in concept.aliases):
            return concept
    # Only literal text, never user-provided regular expressions.
    words = query.strip().split()
    expression = r"\s+".join(re.escape(w) for w in words)
    if len(words) == 1 and len(words[0]) >= 3:
        expression += r"\w*"  # Polish inflected forms of a single stem.
    return Concept("query", query.strip(), (query.strip(),),
                   (r"(?<!\w)" + expression + r"(?!\w)",))


def pattern_for(concept: Concept) -> re.Pattern[str]:
    return re.compile("|".join("(?:" + s + ")" for s in concept.patterns), re.IGNORECASE)


def locate_owner(entities: list[dict[str, Any]], offset: int) -> dict[str, Any] | None:
    containing = (e for e in entities
                  if e["start_offset"] <= offset < e["end_offset"])
    return min(containing, key=lambda e: (
        PREFERRED_KINDS.get(e["kind"], 8),
        e["end_offset"] - e["start_offset"],
        e["id"],
    ), default=None)


def occurrence_snippet(source: str, begin: int, end: int) -> str:
    start = max(0, begin - 105)
    finish = min(len(source), end + 135)
    text = " ".join(source[start:finish].split())
    return ("…" if start else "") + text + ("…" if finish < len(source) else "")


def build_concept_graph(con: sqlite3.Connection, query: str,
                        max_occurrences: int = 36) -> dict[str, Any]:
    if not query.strip() or len(query) > 100 or not 1 <= max_occurrences <= 80:
        raise ValueError("Nieprawidłowe parametry grafu pojęć.")
    root = resolve_concept(query)
    adjacent = [r for r in RELATIONS if root.key in r[:2]]
    keys = [root.key] + sorted({k for r in adjacent for k in r[:2]} - {root.key})
    concepts = {key: CATALOG[key] for key in keys if key in CATALOG}
    concepts[root.key] = root
    patterns = {key: pattern_for(concepts[key]) for key in keys}

    # One SQLite read of each source; do not change the canonical corpus/index.
    documents = [dict(d) for d in con.execute(
        "SELECT id, title, domain, content FROM documents ORDER BY id"
    )]
    owners: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entity in con.execute(
        "SELECT id,document_id,kind,title,start_offset,end_offset,start_line "
        "FROM entities ORDER BY document_id,start_offset"
    ):
        owners[entity["document_id"]].append(dict(entity))

    all_candidates: dict[str, list[dict[str, Any]]] = {key: [] for key in keys}
    match_counts = {key: 0 for key in keys}
    module_counts: dict[str, set[str]] = {key: set() for key in keys}
    for doc in documents:
        content = doc["content"]
        surface = searchable_source(content)
        for key in keys:
            matches = list(patterns[key].finditer(surface))
            if not matches:
                continue
            match_counts[key] += len(matches)
            module_counts[key].add(doc["id"])
            seen_owners: set[str] = set()
            local: list[dict[str, Any]] = []
            for match in matches[:MAX_MATCHES_PER_DOCUMENT]:
                owner = locate_owner(owners[doc["id"]], match.start())
                owner_id = owner["id"] if owner else doc["id"]
                if owner_id in seen_owners:
                    continue
                seen_owners.add(owner_id)
                local.append({
                    "id": f"occ:{key}:{doc['id']}:{match.start()}",
                    "type": "occurrence", "concept": key,
                    "label": owner["title"] if owner and owner["title"] else doc["title"],
                    "module": doc["id"], "module_title": doc["title"],
                    "domain": doc["domain"],
                    "entity_id": owner["id"] if owner else None,
                    "entity_kind": owner["kind"] if owner else "module",
                    "line": content.count("\n", 0, match.start()) + 1,
                    "matched": match.group(0),
                    "snippet": occurrence_snippet(content, match.start(), match.end()),
                })
            local.sort(key=lambda x: (
                PREFERRED_KINDS.get(x["entity_kind"], 8), x["line"]
            ))
            all_candidates[key].extend(local[:MAX_OCCURRENCES_PER_DOCUMENT_AND_CONCEPT])

    # Fair round-robin allocation: even a very common term cannot erase
    # the sources for related concepts. Stable order for reproducible results.
    selected: dict[str, list[dict[str, Any]]] = {key: [] for key in keys}
    per_key_budget = max(4, math.ceil(max_occurrences / len(keys)))
    remaining = {
        key: iter(sorted(all_candidates[key], key=lambda x: (
            PREFERRED_KINDS.get(x["entity_kind"], 8), x["module"], x["line"]
        ))) for key in keys
    }
    while sum(map(len, selected.values())) < max_occurrences:
        advanced = False
        for key in keys:
            if sum(map(len, selected.values())) >= max_occurrences:
                break
            if len(selected[key]) >= per_key_budget:
                continue
            candidate = next(remaining[key], None)
            if candidate is not None:
                selected[key].append(candidate)
                advanced = True
        if not advanced:
            break

    nodes = [{
        "id": key, "type": "concept", "label": concepts[key].label,
        "term": concepts[key].label, "root": key == root.key,
        "matches_total": match_counts[key],
        "modules_total": len(module_counts[key]),
        "shown": len(selected[key]),
    } for key in keys]
    edges = [{
        "source": source, "target": target, "type": relation,
        "label": label, "explanation": explanation,
        "evidence": "curated_mathematical_relation",
    } for source, target, relation, label, explanation in adjacent]
    for key in keys:
        for occurrence in selected[key]:
            nodes.append(occurrence)
            edges.append({
                "source": key, "target": occurrence["id"],
                "type": "occurrence", "label": "Wystąpienie w źródle",
                "evidence": "indexed_tex_source",
            })
    return {
        "query": query, "root": root.key, "nodes": nodes, "edges": edges,
        "relationships": len(adjacent),
        "occurrences_shown": sum(map(len, selected.values())),
        "matches_total": sum(match_counts.values()),
        "truncated": any(len(all_candidates[k]) > len(selected[k]) for k in keys),
        "notes": ("Powiązania między pojęciami pochodzą z jawnego katalogu; "
                  "wystąpienia wskazują faktyczny fragment LaTeX. "
                  "Współwystępowanie terminów samo w sobie nie tworzy implikacji."),
    }
