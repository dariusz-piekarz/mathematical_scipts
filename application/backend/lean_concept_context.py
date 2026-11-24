"""L1.5.5c: exact indexed definition anchors, not approved translations.

Read-only access to the index. Never infer a scope from a chapter title,
a keyword or an unverified source_hint. No Lean execution or generation.
"""
from __future__ import annotations

import hashlib
import re
import sqlite3

from backend import latex_parser, lean_concepts

ANCHOR_VERSION = "0.1.0"
MAX_DOCUMENT_CHARS = 1_000_000

# Exact source snapshots, deliberately not fuzzy matches. A changed
# definition requires fresh review of its context mapping.
_ANCHORS = [
    {
        "module": "LST-01",
        "path": "pl/logic_and_set_theory/01-zdania-i-spojniki-logiczne.tex",
        "label": "def:propositional-grammar-xli",
        "scope": "logic.syntax",
        "aliases": [
            [
                "formuła",
                "logic.syntax.formula"
            ]
        ],
        "source": "\\begin{definicja}[Skończona budowa formuł rachunku zdań]\n\\label{def:propositional-grammar-xli}\nWybierzmy litery zdaniowe $p_1,p_2,\\ldots$.\n\\emph{Formuły rachunku zdań} powstają według następujących reguł:\n\\begin{enumerate}[label=(\\roman*)]\n\\item każda litera zdaniowa jest formułą;\n\\item jeżeli $\\alpha$ jest formułą, to $\\neg\\alpha$ jest formułą;\n\\item jeżeli $\\alpha,\\beta$ są formułami, to\n      $(\\alpha\\land\\beta)$, $(\\alpha\\lor\\beta)$,\n      $(\\alpha\\Rightarrow\\beta)$ i\n      $(\\alpha\\Leftrightarrow\\beta)$ są formułami;\n\\item formułami są tylko napisy otrzymane przez skończoną liczbę\n      zastosowań reguł (i)--(iii).\n\\end{enumerate}\nJest to \\emph{definicja indukcyjna składni}: mówimy, z jakich\nprostych napisów buduje się poprawne napisy, jeszcze bez pytania\no ich prawdziwość. Umowy dotyczące opuszczania nawiasów\npodamy w sekcji~\\ref{sec:biconditional}.\n\\end{definicja}"
    },
    {
        "module": "LST-01",
        "path": "pl/logic_and_set_theory/01-zdania-i-spojniki-logiczne.tex",
        "label": "def:tautology",
        "scope": "logic.syntax",
        "aliases": [
            [
                "tautologia",
                "logic.syntax.tautology"
            ],
            [
                "równoważność",
                "logic.syntax.equivalent"
            ]
        ],
        "source": "\\begin{definicja}[Tautologia, sprzeczność, spełnialność]\\label{def:tautology}\nFormułę nazywamy \\emph{tautologią}, gdy przy \\emph{każdym}\nwartościowaniu jest prawdziwa. Jest \\emph{sprzeczna}, gdy\nprzy każdym wartościowaniu jest fałszywa.\nJest \\emph{spełnialna}, gdy istnieje \\emph{przynajmniej jedno}\nwartościowanie, w którym jest prawdziwa. Formuły\n$\\varphi$ i $\\psi$ są \\emph{logicznie równoważne},\ngdy przy każdym wspólnym wartościowaniu mają taką samą\nwartość logiczną; zapisujemy $\\varphi\\equiv\\psi$.\nSymbol $\\equiv$ opisuje relację między formułami;\nnie jest kolejnym spójnikiem tworzącym zdanie złożone.\nPrzy porównywaniu dwóch formuł wartościowanie obejmuje\n\\emph{wszystkie} litery występujące w którejkolwiek z nich,\ntakże jeśli część liter występuje tylko w jednej formule.\n\\end{definicja}"
    },
    {
        "module": "LA-01",
        "path": "pl/linear_algebra/01-przestrzenie-wektorowe.tex",
        "label": "def:lin-podprzestrzen",
        "scope": "linear_algebra",
        "aliases": [
            [
                "podprzestrzeń liniowa",
                "linear_algebra.submodule"
            ]
        ],
        "source": "\\begin{definicja}[Podprzestrzeń]\n\\label{def:lin-podprzestrzen}\nPodzbiór \\(W\\subseteq V\\) nazywamy \\emph{podprzestrzenią wektorową},\njeśli \\(W\\) z działaniami odziedziczonymi z \\(V\\)\njest przestrzenią wektorową nad tym samym ciałem \\(K\\).\n\\end{definicja}"
    },
    {
        "module": "LA-01",
        "path": "pl/linear_algebra/01-przestrzenie-wektorowe.tex",
        "label": "def:lin-niezaleznosc",
        "scope": "linear_algebra",
        "aliases": [
            [
                "niezależność liniowa",
                "linear_algebra.independent"
            ]
        ],
        "source": "\\begin{definicja}[Niezależność liniowa]\n\\label{def:lin-niezaleznosc}\nRodzinę wektorów \\((v_i)_{i\\in I}\\) nazywamy\n\\emph{liniowo niezależną}, jeżeli dla dowolnych parami\nróżnych \\(i_1,\\ldots,i_m\\in I\\) i skalarów\n\\(a_1,\\ldots,a_m\\in K\\) równość\n\\(a_1v_{i_1}+\\cdots+a_mv_{i_m}=0_V\\)\npociąga \\(a_1=\\cdots=a_m=0_K\\).\nJeśli ten warunek nie zachodzi, rodzina jest\n\\emph{liniowo zależna}.\nPusta rodzina jest liniowo niezależna.\n\\end{definicja}"
    },
    {
        "module": "LA-03",
        "path": "pl/linear_algebra/03-odwzorowania-liniowe-jadro-i-obraz.tex",
        "label": "def:lin3-odwzorowanie-liniowe",
        "scope": "linear_algebra",
        "aliases": [
            [
                "odwzorowanie liniowe",
                "linear_algebra.linear_map"
            ]
        ],
        "source": "\\begin{definicja}[Odwzorowanie liniowe]\n\\label{def:lin3-odwzorowanie-liniowe}\nNiech \\(V,W\\) będą przestrzeniami wektorowymi nad \\(K\\).\nOdwzorowanie \\(T\\colon V\\to W\\) nazywamy\n\\emph{liniowym}, jeżeli dla dowolnych \\(v,w\\in V\\)\ni \\(a\\in K\\) zachodzą\n\\[\n T(v+w)=T(v)+T(w),\\qquad T(av)=aT(v).\n\\]\nPierwszy warunek nazywamy \\emph{addytywnością},\na drugi \\emph{jednorodnością}.\n\\end{definicja}"
    }
]


def _sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def resolve_definition(con: sqlite3.Connection, module: str, label: str,
                       expected_source_sha256: str) -> dict:
    result = {"status": "unsupported", "anchor_version": ANCHOR_VERSION,
              "dictionary_sha256": lean_concepts.dictionary_sha256(),
              "source_scope": "indexed_snapshot_only", "source": None,
              "candidates": [], "trace": [], "statement_status": "unreviewed",
              "proof_status": "not_run", "candidate_status": "not_generated",
              "certificate": False, "lean_code": None,
              "external_transfer_allowed": False}
    if (type(module) is not str or type(label) is not str
            or len(module) > 64 or len(label) > 128
            or type(expected_source_sha256) is not str
            or not re.fullmatch(r"[0-9a-f]{64}", expected_source_sha256)):
        return {**result, "status": "invalid_input"}
    anchor = next((a for a in _ANCHORS if
                   (a["module"], a["label"]) == (module, label)), None)
    if anchor is None:
        return result
    try:
        # Refuse older/incomplete schemas, duplicate labels, and synthetic owners.
        rows = con.execute(
            "SELECT document_id,entity_id,offset,line FROM label_occurrences "
            "WHERE name=? LIMIT 2", (label,)).fetchall()
        if len(rows) != 1:
            return {**result, "status": "ambiguous_label" if rows else "missing_label"}
        if con.execute("SELECT 1 FROM label_conflicts WHERE name=? LIMIT 1",
                       (label,)).fetchone() is not None:
            return {**result, "status": "ambiguous_label"}
        owner_module, entity_id, offset, line = rows[0]
        legacy = con.execute("SELECT document_id,entity_id,offset,line FROM labels "
                             "WHERE name=?", (label,)).fetchone()
        if owner_module != module or legacy is None or tuple(legacy) != tuple(rows[0]):
            return {**result, "status": "invalid_binding"}
        entity = con.execute("SELECT kind,start_offset,end_offset,start_line,end_line "
                             "FROM entities WHERE id=? AND document_id=?",
                             (entity_id, module)).fetchone()
        doc = con.execute("SELECT path,sha256,content FROM documents WHERE id=? "
                          "AND length(content)<=?", (module, MAX_DOCUMENT_CHARS)).fetchone()
        if entity is None or doc is None:
            return {**result, "status": "invalid_binding"}
        kind, start, end, first, last = entity
        path, digest, source = doc
        if (kind != "definition" or path != anchor["path"]
                or type(source) is not str or _sha(source) != digest
                or not all(type(i) is int for i in (start, end, offset, line, first, last))
                or not 0 <= start <= offset < end <= len(source)):
            return {**result, "status": "invalid_binding"}
        fragment = source[start:end]
        if _sha(fragment) != expected_source_sha256 or fragment != anchor["source"]:
            return {**result, "status": "stale_source"}
        # Reparse the whole document so that comments, nested environments,
        # shifted boundaries and reassigned labels cannot masquerade as anchors.
        parsed = latex_parser.parse_document(source, path)
        local = [l for l in parsed.labels if l.name == label]
        if len(local) != 1 or (local[0].offset, local[0].line) != (offset, line):
            return {**result, "status": "invalid_binding"}
        owners = [e for e in parsed.entities if e.id == local[0].entity_id]
        if (len(owners) != 1 or
                (owners[0].kind, owners[0].start, owners[0].end,
                 owners[0].start_line, owners[0].end_line) != tuple(entity)):
            return {**result, "status": "invalid_binding"}
        candidates, trace = [], []
        for alias, concept_id in anchor["aliases"]:
            match = lean_concepts.lookup(alias, anchor["scope"])
            selected = match["selected"]
            if match["status"] != "matched_candidate" or selected["id"] != concept_id:
                return {**result, "status": "dictionary_mismatch"}
            candidates.append(selected)
            trace.append({"rule": "exact_definition_anchor", "concept_id": concept_id,
                          "alias": alias, "scope": anchor["scope"]})
        return {**result, "status": "context_candidates", "candidates": candidates,
                "trace": trace, "source": {"module": module, "label": label,
                "entity_id": entity_id, "document_sha256": digest,
                "source_sha256": expected_source_sha256, "start": start, "end": end}}
    except (sqlite3.Error, UnicodeError, TypeError, ValueError, RecursionError):
        return {**result, "status": "invalid_index"}
