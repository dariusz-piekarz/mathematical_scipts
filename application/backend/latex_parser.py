"""Indeksowanie kanonicznych rozdziałów LaTeX do SQLite.

Standard library only. Pliki .tex pozostają jedynym źródłem prawdy.
Parser jest analizatorem statycznym, NIE kompilatorem TeX-a:
nie rozwija makr i nie wykonuje warunków TeX-a.

Przykłady:
    python backend/latex_parser.py index --source rozdzialy --db data/biblioteka.db
    python backend/latex_parser.py stats --db data/biblioteka.db
    python backend/latex_parser.py search --query 'twierdzenie Lefschetza'
    python backend/latex_parser.py show --label 'ch:pierscienie'
    python backend/latex_parser.py graph --source ALG-00 --format json
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
from collections import Counter
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re
import sqlite3
import sys
from typing import Any

try:
    from .label_registry import Owner, resolve
except ImportError:  # python backend/latex_parser.py ...
    from label_registry import Owner, resolve

SCHEMA_VERSION = 3
SECTION_DEPTH = {
    "part": 0, "chapter": 1, "section": 2, "subsection": 3,
    "subsubsection": 4, "paragraph": 5, "subparagraph": 6,
}
THEOREM_ENVS = {
    "twierdzenie", "theorem", "stwierdzenie", "proposition", "lemat", "lemma",
    "wniosek", "corollary", "fakt", "fact", "claim", "tezа", "teza",
}
DEFINITION_ENVS = {"definicja", "definition", "oznaczenie", "notation"}
EXAMPLE_ENVS = {"przyklad", "example", "kontrprzyklad", "counterexample"}
PROOF_ENVS = {"proof", "dowod", "dowód"}
EXERCISE_ENVS = {"zadanie", "exercise", "problem", "cwiczenie", "ćwiczenie"}
REMARK_ENVS = {"uwaga", "remark", "remarks", "obserwacja", "observation"}
EQUATION_ENVS = {"equation", "align", "gather", "multline", "flalign", "alignat"}
FIGURE_ENVS = {"figure", "tikzpicture", "center"}
CODE_ENVS = {"lstlisting", "minted", "verbatim", "Verbatim"}
VERBATIM_ENVS = CODE_ENVS | {"comment", "filecontents", "filecontents*"}
REF_COMMANDS = {"ref", "eqref", "pageref", "autoref", "nameref", "cref", "Cref", "vref", "Vref"}
PREFIX_DOMAINS = {
    "ALG": "geometria algebraiczna", "AT": "geometria algebraiczna / topologia",
    "TOP": "topologia algebraiczna", "GW": "teoria grafów i węzłów",
    "GA": "teoria Galois", "KAT": "teoria kategorii", "MOD": "teoria modeli",
    "CAL": "teoria całki", "BT": "Banach–Tarski",
    "P1": "rachunek prawdopodobieństwa I", "P2": "procesy stochastyczne",
    "P3": "analiza stochastyczna", "P4": "statystyka matematyczna",
    "ME": "teoria miary",
    "DG": "geometria i topologia różniczkowa",
    "FA": "analiza funkcjonalna",
    "PDE": "równania różniczkowe cząstkowe",
}
COMMAND = re.compile(r"\\([A-Za-z@]+|.)")
RE_WS = re.compile(r"\s+")


@dataclass
class Entity:
    id: str
    document_id: str
    kind: str
    subtype: str
    title: str
    start: int
    end: int
    content_start: int
    starred: bool
    parent_id: str | None = None
    start_line: int = 0
    end_line: int = 0
    excerpt: str = ""


@dataclass
class Label:
    name: str
    document_id: str
    offset: int
    line: int = 0
    entity_id: str | None = None
    excerpt: str = ""


@dataclass
class Reference:
    command: str
    target: str
    document_id: str
    offset: int
    line: int = 0
    entity_id: str | None = None


@dataclass
class Document:
    id: str
    path: str
    domain: str
    title: str
    source: str
    digest: str
    entities: list[Entity]
    labels: list[Label]
    references: list[Reference]
    warnings: list[str]


def mask_span(chars: list[str], start: int, end: int) -> None:
    for k in range(start, end):
        if chars[k] != "\n":
            chars[k] = " "


def is_escaped(source: str, position: int) -> bool:
    k = position - 1
    while k >= 0 and source[k] == "\\":
        k -= 1
    return (position - 1 - k) % 2 == 1


def masked_source(source: str) -> str:
    """Usuń komentarze i treści verbatim, nie zmieniając offsetów ani nowych linii."""
    chars = list(source)
    pos, total = 0, len(source)
    inside: str | None = None
    while pos < total:
        if inside is not None:
            end_match = re.search(r"\\end\s*\{\s*" + re.escape(inside) + r"\s*\}", source[pos:])
            if end_match is None:
                mask_span(chars, pos, total)
                break
            end_start = pos + end_match.start()
            mask_span(chars, pos, end_start)
            pos = end_start + len(end_match.group(0))
            inside = None
            continue
        if source[pos] == "%" and not is_escaped(source, pos):
            end = source.find("\n", pos)
            end = total if end < 0 else end
            mask_span(chars, pos, end)
            pos = end
            continue
        if source[pos] == "\\":
            m = re.match(r"\\begin\s*\{\s*([^}]+)\s*\}", source[pos:])
            if m and m.group(1).strip() in VERBATIM_ENVS:
                inside = m.group(1).strip()
                pos += len(m.group(0))
                continue
            v = re.match(r"\\verb\*?([^A-Za-z\s])", source[pos:])
            if v:
                delim = v.group(1)
                end = source.find(delim, pos + len(v.group(0)))
                if end >= 0:
                    mask_span(chars, pos, end+1)
                    pos = end + 1
                    continue
        pos += 1
    return "".join(chars)


def skip_space(text: str, pos: int) -> int:
    while pos < len(text) and text[pos].isspace():
        pos += 1
    return pos


def grouped(text: str, pos: int, opener: str = "{", closer: str = "}") -> tuple[str, int] | None:
    if pos >= len(text) or text[pos] != opener:
        return None
    depth = 0
    for idx in range(pos, len(text)):
        c = text[idx]
        if c == opener and not is_escaped(text, idx):
            depth += 1
        elif c == closer and not is_escaped(text, idx):
            depth -= 1
            if depth == 0:
                return text[pos+1:idx], idx+1
    return None


def read_argument(text: str, pos: int, opening: str = "{") -> tuple[str, int] | None:
    pos = skip_space(text, pos)
    return grouped(text, pos, opening, "}" if opening == "{" else "]")


def heading_args(text: str, pos: int) -> tuple[str, int, bool] | None:
    pos = skip_space(text, pos)
    starred = False
    if pos < len(text) and text[pos] == "*":
        starred = True
        pos += 1
    pos = skip_space(text, pos)
    opt = read_argument(text, pos, "[")
    if opt:
        pos = opt[1]
    arg = read_argument(text, pos)
    if not arg:
        return None
    return arg[0], arg[1], starred


def env_kind(name: str) -> str | None:
    base = name.rstrip("*")
    if base in THEOREM_ENVS: return "theorem"
    if base in DEFINITION_ENVS: return "definition"
    if base in EXAMPLE_ENVS: return "example"
    if base in PROOF_ENVS: return "proof"
    if base in EXERCISE_ENVS: return "exercise"
    if base in REMARK_ENVS: return "remark"
    if base in EQUATION_ENVS: return "equation"
    if base in FIGURE_ENVS: return "figure"
    if base in CODE_ENVS: return "code"
    return None


def plain_excerpt(source: str, limit: int = 360) -> str:
    source = re.sub(r"\\label\s*\{[^}]*\}", "", source)
    source = re.sub(r"\\(?:begin|end)\s*\{[^}]*\}", "", source)
    source = re.sub(r"\\(?:chapter|section|subsection|subsubsection|paragraph)\*?\s*\{", "", source)
    source = re.sub(r"\\[A-Za-z@]+\*?", "", source)
    source = source.replace("{", "").replace("}", "")
    return RE_WS.sub(" ", source).strip()[:limit]


REPOSITORY_CATEGORIES = {
    "differential_geometry_and_topology": "DG",
    "functional_analysis": "FA",
    "measure_theory": "ME",
    "partial_differential_equations": "PDE",
    "algebraic_geometry": "ALG", "algebraic_topology": "TOP",
    "banach_tarski": "BT", "category_theory": "KAT",
    "galois_theory": "GA", "graph_and_knot_theory": "GW",
    "integration_theory": "CAL", "model_theory": "MOD",
    "probability_volume_i": "P1", "probability_volume_ii": "P2",
    "probability_volume_iii": "P3", "probability_volume_iv": "P4",
}


def module_id(path: Path) -> str:
    """Provide stable IDs for both flat app snapshots and nested repository chapters."""
    parts = path.parts
    if "pl" in parts:
        pos = parts.index("pl")
        if pos + 1 < len(parts):
            prefix = REPOSITORY_CATEGORIES.get(parts[pos + 1])
            if prefix:
                found = re.match(r"(\d{2}[AB]?)-", path.name)
                if found:
                    return f"{prefix}-{found.group(1)}"
    base = path.name
    if "--" in base:
        return base.split("--", 1)[0]
    return path.stem


def parse_document(source: str, path: str) -> Document:
    filename = Path(path)
    file_id = module_id(filename)
    masked = masked_source(source)
    newlines = [-1] + [m.start() for m in re.finditer("\n", source)]
    line_at = lambda offset: bisect_right(newlines, offset)
    headings: list[tuple[int, int, str, str, bool, int]] = []
    envs: list[tuple[int, int, int, str, str, str, bool]] = []
    env_stack: list[tuple[str, int, int, str]] = []
    raw_labels: list[tuple[str, int]] = []
    raw_refs: list[tuple[str, str, int]] = []
    warnings: list[str] = []
    pos = 0
    while True:
        match = COMMAND.search(masked, pos)
        if not match: break
        name = match.group(1)
        p = match.end()
        next_pos = p
        if name in SECTION_DEPTH:
            res = heading_args(masked, p)
            if res:
                title, end, star = res
                headings.append((match.start(), end, name, title, star, SECTION_DEPTH[name]))
                next_pos = end
        elif name == "begin":
            res = read_argument(masked, p)
            if res:
                env_name, end = res
                env_name = env_name.strip()
                title = ""
                opt = read_argument(masked, end, "[")
                if opt:
                    title, end = opt
                env_stack.append((env_name, match.start(), end, title))
                next_pos = end
        elif name == "end":
            res = read_argument(masked, p)
            if res:
                env_name, end = res
                env_name = env_name.strip()
                index = next((k for k in range(len(env_stack)-1, -1, -1) if env_stack[k][0] == env_name), -1)
                if index >= 0:
                    if index != len(env_stack)-1:
                        warnings.append(f"Line {line_at(match.start())}: non-LIFO closing environment {env_name}")
                    for orphan in env_stack[index+1:]:
                        warnings.append(f"Line {line_at(orphan[1])}: unmatched environment {orphan[0]}")
                    name0, start0, body_start, title = env_stack[index]
                    kind = env_kind(name0)
                    if kind:
                        envs.append((start0, end, body_start, kind, name0, title, name0.endswith("*")))
                    del env_stack[index:]
                next_pos = end
        elif name == "label":
            res = read_argument(masked, p)
            if res:
                label, end = res
                if label.strip(): raw_labels.append((label.strip(), match.start()))
                next_pos = end
        elif name in REF_COMMANDS:
            res = read_argument(masked, p)
            if res:
                targets, end = res
                for target in targets.split(","):
                    if target.strip(): raw_refs.append((name, target.strip(), match.start()))
                next_pos = end
        elif name == "hyperref":
            res = read_argument(masked, p, "[")
            if res:
                targets, end = res
                if targets.strip(): raw_refs.append((name, targets.strip(), match.start()))
                next_pos = end
        # Skanujemy także argumenty nagłówków i środowisk: mogą zawierać \ref.
        pos = match.end()
    # End of file: report orphaned TeX environments (not necessarily syntactically invalid source).
    for name, start, _, _ in env_stack:
        warnings.append(f"Line {line_at(start)}: unterminated environment {name}")
    entities: list[Entity] = []
    for i, (start, content_start, kind, title, star, depth) in enumerate(headings):
        end = len(source)
        for next_start, _, _, _, _, next_depth in headings[i+1:]:
            if next_depth <= depth:
                end = next_start
                break
        entities.append(Entity("", file_id, kind, kind, title, start, end, content_start, star))
    for start, end, content_start, kind, subtype, title, star in envs:
        entities.append(Entity("", file_id, kind, subtype, title, start, end, content_start, star))
    entities.sort(key=lambda x: (x.start, -x.end, x.kind))
    kinds = Counter()
    for entity in entities:
        kinds[entity.kind] += 1
        entity.id = f"{file_id}/{entity.kind}/{kinds[entity.kind]:04d}"
        entity.start_line = line_at(entity.start)
        entity.end_line = line_at(max(entity.start, entity.end-1))
        entity.excerpt = plain_excerpt(source[entity.content_start:min(entity.end, entity.content_start+700)])
    # Obiekty mające lokalną etykietę blisko początku dostają trwały klucz
    # oparty na \label; pozostałe używają technicznego ID pozycyjnego.
    # Zagnieżdżone środowisko jest właścicielem własnej etykiety, nie sekcja.
    anchored: set[int] = set()
    for label_name, offset in raw_labels:
        candidates = [e for e in entities if e.content_start <= offset < e.end]
        if not candidates:
            continue
        owner = min(candidates, key=lambda e: (e.end-e.start, -e.start))
        if offset - owner.content_start <= 220 and id(owner) not in anchored:
            owner.id = "label:" + label_name
            anchored.add(id(owner))
    # Tree containment: chapter/section hierarchy and nested environments.
    stack: list[Entity] = []
    for entity in entities:
        while stack and not (stack[-1].start <= entity.start and entity.end <= stack[-1].end):
            stack.pop()
        if stack:
            entity.parent_id = stack[-1].id
        stack.append(entity)
    def owner_at(offset: int) -> str | None:
        owner: Entity | None = None
        for e in entities:
            if e.start > offset: break
            if e.start <= offset < e.end and (owner is None or e.start >= owner.start and e.end <= owner.end):
                owner = e
        return owner.id if owner else None
    labels = [Label(x, file_id, off, line_at(off), owner_at(off),
                    plain_excerpt(source[max(0, off-110):min(len(source), off+210)], 270))
              for x, off in raw_labels]
    references = [Reference(cmd, target, file_id, off, line_at(off), owner_at(off))
                  for cmd, target, off in raw_refs]
    chapter = next((e.title for e in entities if e.kind == "chapter"), None)
    title = chapter or next((e.title for e in entities if e.kind in SECTION_DEPTH), filename.stem)
    return Document(file_id, path.replace("\\", "/"), PREFIX_DOMAINS.get(file_id.split("-", 1)[0], "inne"),
                    title, source, hashlib.sha256(source.encode("utf-8")).hexdigest(),
                    entities, labels, references, warnings)


SCHEMA = """
PRAGMA foreign_keys = ON;
CREATE TABLE schema_info (version INTEGER NOT NULL, created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE documents (
  id TEXT PRIMARY KEY, path TEXT NOT NULL UNIQUE, domain TEXT NOT NULL,
  title TEXT NOT NULL, sha256 TEXT NOT NULL, content TEXT NOT NULL,
  bytes INTEGER NOT NULL, warnings_json TEXT NOT NULL
);
CREATE TABLE entities (
  id TEXT PRIMARY KEY, document_id TEXT NOT NULL REFERENCES documents(id),
  parent_id TEXT REFERENCES entities(id), kind TEXT NOT NULL, subtype TEXT NOT NULL,
  title TEXT NOT NULL, start_offset INTEGER NOT NULL, end_offset INTEGER NOT NULL,
  start_line INTEGER NOT NULL, end_line INTEGER NOT NULL,
  excerpt TEXT NOT NULL, starred INTEGER NOT NULL
);
CREATE INDEX idx_entities_doc_start ON entities(document_id,start_offset);
CREATE INDEX idx_entities_kind ON entities(kind);
CREATE TABLE labels (
  name TEXT PRIMARY KEY, document_id TEXT NOT NULL REFERENCES documents(id),
  entity_id TEXT REFERENCES entities(id), offset INTEGER NOT NULL,
  line INTEGER NOT NULL, excerpt TEXT NOT NULL
);
CREATE INDEX idx_labels_document ON labels(document_id);
CREATE TABLE label_conflicts (
  name TEXT NOT NULL, document_id TEXT NOT NULL REFERENCES documents(id),
  entity_id TEXT REFERENCES entities(id), offset INTEGER NOT NULL,
  line INTEGER NOT NULL, excerpt TEXT NOT NULL,
  PRIMARY KEY(name,document_id)
);
CREATE INDEX idx_label_conflicts_name ON label_conflicts(name);
CREATE TABLE label_occurrences (
  occurrence_id TEXT PRIMARY KEY, name TEXT NOT NULL,
  document_id TEXT NOT NULL REFERENCES documents(id),
  entity_id TEXT REFERENCES entities(id), line INTEGER NOT NULL,
  offset INTEGER NOT NULL, concept_id TEXT,
  UNIQUE (document_id,name,line,offset)
);
CREATE INDEX idx_label_occurrences_name ON label_occurrences(name);
CREATE INDEX idx_label_occurrences_doc ON label_occurrences(document_id);
CREATE TABLE references_tex (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  source_document TEXT NOT NULL REFERENCES documents(id),
  source_entity TEXT REFERENCES entities(id),
  command TEXT NOT NULL, target_label TEXT NOT NULL, offset INTEGER NOT NULL,
  line INTEGER NOT NULL, target_document TEXT REFERENCES documents(id),
  target_entity TEXT REFERENCES entities(id), status TEXT NOT NULL
);
CREATE INDEX idx_ref_source ON references_tex(source_document);
CREATE INDEX idx_ref_target ON references_tex(target_label);
CREATE INDEX idx_ref_target_document ON references_tex(target_document);
CREATE TABLE historical_aliases (
  old_label TEXT NOT NULL, new_label TEXT NOT NULL, scope_document TEXT NOT NULL DEFAULT '',
  reason TEXT NOT NULL DEFAULT '', PRIMARY KEY (old_label,new_label,scope_document)
);
CREATE VIEW dependency_edges AS
SELECT source_document, target_document, count(*) AS references_count
FROM references_tex WHERE status IN ('resolved','external_resolved','alias_resolved') AND target_document IS NOT NULL
GROUP BY source_document,target_document;
"""


def connect(db: Path) -> sqlite3.Connection:
    if not db.is_file():
        raise FileNotFoundError(f"Baza nie istnieje: {db}. Uruchom komendę 'index'.")
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON")
    return con


def load_historical_aliases(con: sqlite3.Connection, alias_file: Path | None) -> None:
    if not alias_file or not alias_file.is_file(): return
    obj = json.loads(alias_file.read_text(encoding="utf-8-sig"))
    rows: list[tuple[str,str,str,str]] = []
    for item in obj.get("rewritten_xr_prefixes", []):
        rows.append((item["old"], item["new"], "", "rewritten_xr_prefix"))
    for item in obj.get("renamed_collisions", []):
        rows.append((item["old"], item["new"], item.get("chapter", ""), "collision_rename"))
    for item in obj.get("lost_labels_restored", []):
        rows.append((item["label"], item["maps_to_chapter_label"], item.get("module", ""), "restored_label"))
    con.executemany("INSERT OR IGNORE INTO historical_aliases VALUES(?,?,?,?)", rows)


def read_curated_aliases(alias_file: Path | None) -> dict[tuple[str, str], tuple[str, str]]:
    """Explicit, versioned aliases. Never infer equivalence from matching names.

    Optional JSON: {"label_aliases":[{"source_document":"TOP-05",
      "original_label":"old", "target_document":"TOP-03",
      "target_label":"thm:homotopia-homologia"}]}.
    An alias must resolve to an actual indexed original label.
    """
    if alias_file is None or not alias_file.is_file():
        return {}
    data = json.loads(alias_file.read_text(encoding="utf-8-sig"))
    result: dict[tuple[str, str], tuple[str, str]] = {}
    for row in data.get("label_aliases", []):
        key = (row["source_document"], row["original_label"])
        target = (row["target_document"], row["target_label"])
        if key in result and result[key] != target:
            raise ValueError(f"Sprzeczne aliasy dla {key}")
        result[key] = target
    return result


def build_database(source_dir: Path, db_path: Path, alias_file: Path | None = None, *, recursive: bool = False) -> dict[str, Any]:
    # Domyślnie tylko kanoniczne, bezpośrednie pliki w płaskim folderze rozdzialy/.
    # Inne podfoldery mogą być roboczymi projektami.
    files = sorted(source_dir.rglob("*.tex") if recursive else source_dir.glob("*.tex"))
    if recursive:
        files = [f for f in files if "supplements" not in f.relative_to(source_dir).parts]
    if not files:
        raise ValueError(f"Brak plików .tex w katalogu {source_dir}")
    db_path.parent.mkdir(parents=True, exist_ok=True)
    tmp = db_path.with_suffix(db_path.suffix + ".tmp")
    if tmp.exists(): tmp.unlink()
    con = sqlite3.connect(tmp)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON")
    con.executescript(SCHEMA)
    con.execute("INSERT INTO schema_info(version) VALUES (?)", (SCHEMA_VERSION,))
    fts = True
    try:
        con.executescript("CREATE VIRTUAL TABLE document_fts USING fts5(document_id UNINDEXED, title, domain, content, tokenize='unicode61');"
                          "CREATE VIRTUAL TABLE entity_fts USING fts5(entity_id UNINDEXED, title, excerpt, tokenize='unicode61');")
    except sqlite3.OperationalError:
        fts = False
    total = Counter()
    all_documents: list[Document] = []
    seen_ids: set[str] = set()
    seen_entity_ids: set[str] = set()
    for file in files:
        path = file.relative_to(source_dir.parent).as_posix()
        doc = parse_document(file.read_text(encoding="utf-8-sig"), path)
        if doc.id in seen_ids:
            con.close(); tmp.unlink(missing_ok=True)
            raise ValueError(f"Powielony identyfikator modułu {doc.id} w pliku {path}")
        seen_ids.add(doc.id)
        # Multiple books can intentionally reuse mathematical labels. Entity IDs
        # are storage IDs, not LaTeX labels, so disambiguate without rewriting TeX.
        changed: dict[str, str] = {}
        for e in doc.entities:
            if e.id in seen_entity_ids:
                candidate = f"{doc.id}::{e.id}"
                if candidate in seen_entity_ids:
                    raise ValueError(f"Duplicate entity in one chapter: {candidate}")
                changed[e.id] = candidate
                e.id = candidate
            seen_entity_ids.add(e.id)
        if changed:
            for e in doc.entities:
                if e.parent_id in changed:
                    e.parent_id = changed[e.parent_id]
            for label in doc.labels:
                if label.entity_id in changed:
                    label.entity_id = changed[label.entity_id]
            for ref in doc.references:
                if ref.entity_id in changed:
                    ref.entity_id = changed[ref.entity_id]
        all_documents.append(doc)
        con.execute("INSERT INTO documents VALUES (?,?,?,?,?,?,?,?)", (
            doc.id, doc.path, doc.domain, doc.title, doc.digest, doc.source,
            len(doc.source.encode("utf-8")), json.dumps(doc.warnings, ensure_ascii=False)))
        con.executemany("INSERT INTO entities VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", [
            (e.id, e.document_id, e.parent_id, e.kind, e.subtype, e.title,
             e.start, e.end, e.start_line, e.end_line, e.excerpt, int(e.starred)) for e in doc.entities
        ])
        if fts:
            con.execute("INSERT INTO document_fts VALUES (?,?,?,?)", (doc.id, doc.title, doc.domain, doc.source))
            con.executemany("INSERT INTO entity_fts VALUES (?,?,?)",
                            [(e.id, e.title, e.excerpt) for e in doc.entities])
        total["documents"] += 1
        total["entities"] += len(doc.entities)
        total["parse_warnings"] += len(doc.warnings)
    duplicate_labels: list[dict[str, Any]] = []
    label_owners: dict[str, str] = {}
    label_locations: dict[str, dict[str, Label]] = {}
    for document in all_documents:
        for label in document.labels:
            label_locations.setdefault(label.name, {})[document.id] = label
    for doc in all_documents:
        for label in doc.labels:
            if label.name in label_owners:
                duplicate_labels.append({"label": label.name, "first": label_owners[label.name], "other": doc.id})
                con.execute("INSERT OR IGNORE INTO label_conflicts VALUES (?,?,?,?,?,?)", (
                    label.name,label.document_id,label.entity_id,label.offset,label.line,label.excerpt))
                first = label_locations[label.name][label_owners[label.name]]
                con.execute("INSERT OR IGNORE INTO label_conflicts VALUES (?,?,?,?,?,?)", (
                    first.name,first.document_id,first.entity_id,first.offset,first.line,first.excerpt))
                continue
            label_owners[label.name] = doc.id
            con.execute("INSERT INTO labels VALUES (?,?,?,?,?,?)", (
                label.name, label.document_id, label.entity_id, label.offset, label.line, label.excerpt))
            total["labels"] += 1
    curated_aliases = read_curated_aliases(alias_file)
    # Separate every original occurrence from the legacy globally-unique index.
    # Entity identities stay distinct even when the LaTeX strings coincide.
    all_owners: list[Owner] = []
    for document in all_documents:
        for label in document.labels:
            all_owners.append(Owner(document.id, label.name, label.entity_id))
            con.execute("INSERT INTO label_occurrences VALUES (?,?,?,?,?,?,NULL)",
                        (f"{document.id}::{label.name}", label.name, document.id,
                         label.entity_id, label.line, label.offset))
    for doc in all_documents:
        for ref in doc.references:
            decision = resolve(doc.id, ref.target, all_owners, aliases=curated_aliases)
            dst = decision.owner.document_id if decision.owner else None
            resolved_id = decision.owner.entity_id if decision.owner else None
            status = decision.status
            con.execute("INSERT INTO references_tex(source_document,source_entity,command,target_label,offset,line,target_document,target_entity,status) VALUES (?,?,?,?,?,?,?,?,?)",
                        (doc.id, ref.entity_id, ref.command, ref.target, ref.offset, ref.line,
                         dst, resolved_id, status))
            total["references"] += 1
            total[status + "_references"] += 1
    load_historical_aliases(con, alias_file)
    for k in ("documents", "entities", "labels", "references", "resolved_references", "external_resolved_references", "alias_resolved_references", "ambiguous_references", "missing_references", "parse_warnings"):
        total.setdefault(k, 0)
    total["duplicate_labels"] = len(duplicate_labels)
    total["cross_document_edges"] = con.execute("SELECT count(*) FROM dependency_edges WHERE source_document != target_document").fetchone()[0]
    total["cross_document_references"] = con.execute("SELECT sum(references_count) FROM dependency_edges WHERE source_document != target_document").fetchone()[0] or 0
    total["fts_enabled"] = fts
    report = {"schema_version": SCHEMA_VERSION, "source": str(source_dir.resolve()),
              "database": str(db_path.resolve()), **dict(total), "duplicate_labels_detail": duplicate_labels,
              "missing_targets": [dict(r) for r in con.execute("SELECT source_document,target_label,line FROM references_tex WHERE status='missing' LIMIT 100").fetchall()]}
    # row_factory needs to be set for mapping.
    con.commit()
    con.execute("PRAGMA wal_checkpoint(TRUNCATE)")
    con.close()
    if db_path.exists(): db_path.unlink()
    tmp.replace(db_path)
    return report


def default_source() -> Path:
    root = Path(__file__).resolve().parents[1]
    for candidate in (root.parent / "chapters" / "pl", root / "rozdzialy", root.parent / "rozdzialy"):
        if candidate.is_dir(): return candidate
    return root.parent / "rozdzialy"


def default_database() -> Path:
    return Path(__file__).resolve().parents[1] / "data" / "biblioteka.db"


def get_stats(con: sqlite3.Connection) -> dict[str, int]:
    result = {key: con.execute(f"SELECT count(*) FROM {table}").fetchone()[0] for key, table in {
        "documents":"documents", "entities":"entities", "labels":"labels",
        "references":"references_tex", "missing_references":"references_tex WHERE status='missing'",
        "cross_document_edges":"dependency_edges WHERE source_document != target_document"}.items()}
    result["label_occurrences"] = con.execute("SELECT count(*) FROM label_occurrences").fetchone()[0]
    result["external_resolved_references"] = con.execute("SELECT count(*) FROM references_tex WHERE status='external_resolved'").fetchone()[0]
    result["alias_resolved_references"] = con.execute("SELECT count(*) FROM references_tex WHERE status='alias_resolved'").fetchone()[0]
    result["duplicate_labels"] = con.execute("SELECT count(DISTINCT name) FROM label_conflicts").fetchone()[0]
    result["ambiguous_references"] = con.execute("SELECT count(*) FROM references_tex WHERE status='ambiguous'").fetchone()[0]
    result["theorems"] = con.execute("SELECT count(*) FROM entities WHERE kind='theorem'").fetchone()[0]
    result["definitions"] = con.execute("SELECT count(*) FROM entities WHERE kind='definition'").fetchone()[0]
    result["proofs"] = con.execute("SELECT count(*) FROM entities WHERE kind='proof'").fetchone()[0]
    return result


def search(con: sqlite3.Connection, query: str, limit: int = 20) -> list[dict[str, Any]]:
    try:
        rows = con.execute("SELECT d.id AS document_id,d.title,d.domain,snippet(document_fts,3,'[',']','…',14) AS fragment FROM document_fts JOIN documents d ON d.id=document_fts.document_id WHERE document_fts MATCH ? LIMIT ?",
                           ('"'+query.replace('"','""')+'"',limit)).fetchall()
        return [dict(r) for r in rows]
    except sqlite3.OperationalError:
        rows = con.execute("SELECT id AS document_id,title,domain,substr(content,1,200) AS fragment FROM documents WHERE content LIKE ? OR title LIKE ? LIMIT ?",
                           (f"%{query}%",f"%{query}%",limit)).fetchall()
        return [dict(r) for r in rows]


def show_label(con: sqlite3.Connection, label: str, max_chars: int = 1300, *,
               document_id: str | None = None) -> dict[str, Any] | None:
    if document_id is None:
        row = con.execute("SELECT l.name,l.document_id,l.line,l.offset,l.entity_id,d.title,d.content FROM labels l JOIN documents d ON d.id=l.document_id WHERE l.name=?",(label,)).fetchone()
    else:
        row = con.execute("SELECT l.name,l.document_id,l.line,l.offset,l.entity_id,d.title,d.content FROM label_occurrences l JOIN documents d ON d.id=l.document_id WHERE l.name=? AND l.document_id=?",(label,document_id)).fetchone()
    if not row:
        return None
    result = {k: row[k] for k in ("name","document_id","line","offset","entity_id","title")}
    if row["entity_id"]:
        entity = con.execute("SELECT kind,subtype,title,start_offset,end_offset FROM entities WHERE id=?",(row["entity_id"],)).fetchone()
        if entity:
            result.update({"kind":entity["kind"],"subtype":entity["subtype"],"entity_title":entity["title"]})
            result["latex"] = row["content"][entity["start_offset"]:min(entity["end_offset"],entity["start_offset"]+max_chars)]
            return result
    result["latex"] = row["content"][max(0,row["offset"]-150):row["offset"]+max_chars]
    return result


def graph_edges(con: sqlite3.Connection, source: str | None = None) -> list[dict[str, Any]]:
    sql = "SELECT source_document,target_document,references_count FROM dependency_edges WHERE source_document != target_document"
    params: tuple[str,...] = ()
    if source:
        sql += " AND (source_document=? OR target_document=?)"
        params = (source,source)
    sql += " ORDER BY references_count DESC, source_document,target_document"
    return [dict(r) for r in con.execute(sql,params).fetchall()]


def analyze_selection(con: sqlite3.Connection, modules: list[str]) -> dict[str, Any]:
    """Audyt wybranego skryptu: referencje wewnętrzne i cele wymagające xr-hyper.

    Sam plan NIE generuje plików .aux i NIE gwarantuje kompilowalności.
    """
    selected = list(dict.fromkeys(modules))
    known = {r[0] for r in con.execute("SELECT id FROM documents").fetchall()}
    absent_modules = [m for m in selected if m not in known]
    selected_set = set(selected) & known
    if not selected_set:
        return {"selected": selected, "unknown_modules": absent_modules,
                "internal_references": 0, "external_references": 0,
                "missing_global": [], "external_targets": []}
    placeholders = ",".join("?" for _ in selected_set)
    rows = con.execute(f"SELECT source_document, target_document, target_label, status, line "
                       f"FROM references_tex WHERE source_document IN ({placeholders}) ORDER BY source_document,line",
                       tuple(sorted(selected_set))).fetchall()
    internal, external, globally_missing = 0, 0, []
    dests: dict[str, dict[str, Any]] = {}
    for r in rows:
        destination = r["target_document"]
        if destination is None:
            globally_missing.append({"source":r["source_document"], "label":r["target_label"], "line":r["line"]})
        elif destination in selected_set:
            internal += 1
        else:
            external += 1
            record = dests.setdefault(destination,{"module":destination,"references_count":0,"labels":set()})
            record["references_count"] += 1
            record["labels"].add(r["target_label"])
    external_targets = [{**x,"labels":sorted(x["labels"])} for x in sorted(dests.values(),key=lambda r:r["module"])]
    return {"selected":selected,"unknown_modules":absent_modules,
            "internal_references":internal,"external_references":external,
            "missing_global":globally_missing,"external_targets":external_targets,
            "requires_xr_hyper":bool(external_targets)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Parser Biblioteki matematycznej / indeks SQLite")
    sub = parser.add_subparsers(dest="action",required=True)
    idx = sub.add_parser("index",help="Zbuduj bazę SQLite z .tex")
    idx.add_argument("--source",type=Path,default=default_source())
    idx.add_argument("--db",type=Path,default=default_database())
    idx.add_argument("--aliases",type=Path,default=None)
    idx.add_argument("--report",type=Path,default=None)
    idx.add_argument("--recursive",action="store_true",help="Uwzględnij także podfoldery (domyślnie tylko główny katalog)")
    for cmd in ("stats","search","show","graph","audit","plan"):
        p = sub.add_parser(cmd)
        p.add_argument("--db",type=Path,default=default_database())
        if cmd=="search":
            p.add_argument("--query",required=True);p.add_argument("--limit",type=int,default=15)
        if cmd=="show":
            p.add_argument("--label",required=True);p.add_argument("--max-chars",type=int,default=1300)
        if cmd=="graph":
            p.add_argument("--source",default=None);p.add_argument("--format",choices=["json","tsv"],default="json")
        if cmd=="plan":
            p.add_argument("--modules",required=True,nargs="+",help="Identyfikatory modułów, np. ALG-00 ALG-01")
    a = parser.parse_args(argv)
    if a.action == "index":
        report = build_database(a.source,a.db,a.aliases,recursive=a.recursive)
        print(json.dumps(report,indent=2,ensure_ascii=False))
        if a.report:
            a.report.parent.mkdir(parents=True,exist_ok=True)
            a.report.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
        return 2 if report["missing_references"] or report["duplicate_labels"] else 0
    con = connect(a.db)
    if a.action=="stats": value = get_stats(con)
    elif a.action=="search": value = search(con,a.query,a.limit)
    elif a.action=="show": value = show_label(con,a.label,a.max_chars)
    elif a.action=="graph":
        edges=graph_edges(con,a.source)
        if a.format=="tsv":
            print("source\ttarget\treferences_count")
            for e in edges: print(f"{e['source_document']}\t{e['target_document']}\t{e['references_count']}")
            return 0
        value = {"directed":True,"edges":edges}
    elif a.action=="audit":
        missing = [dict(x) for x in con.execute("SELECT source_document, target_label, line FROM references_tex WHERE status='missing'").fetchall()]
        value={"passed":not missing,"missing_count":len(missing),"missing":missing}
    elif a.action=="plan":
        value = analyze_selection(con, a.modules)
    else: raise AssertionError
    print(json.dumps(value,indent=2,ensure_ascii=False))
    if a.action=="audit" and not value["passed"]: return 2
    if a.action=="plan" and (value["unknown_modules"] or value["missing_global"]): return 2
    if a.action=="show" and value is None: return 1
    return 0

if __name__=="__main__":
    sys.exit(main())
