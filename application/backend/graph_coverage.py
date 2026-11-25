"""Repository-wide reference inventory; no inferred mathematical links."""
from collections import Counter, defaultdict
from itertools import combinations
import json
from pathlib import Path

from .latex_parser import module_id
from .label_registry import qualified_occurrence



def reading_reference_issues(con):
    """Validate all indexed atlasref rows, not just selected chapter fixtures."""
    rows = con.execute("""
        SELECT r.id, r.source_document, r.target_label, r.line, r.status,
               r.target_document, r.target_entity, e.document_id
        FROM references_tex r LEFT JOIN entities e ON e.id=r.target_entity
        WHERE r.command='atlasref'
        ORDER BY r.source_document,r.line,r.id
    """).fetchall()
    occurrences = defaultdict(list)
    for doc, label, entity in con.execute(
            "SELECT document_id,name,entity_id FROM label_occurrences"):
        occurrences[(doc, label)].append(entity)
    issues = []
    for reference_id, source, label, line, status, target, entity, entity_owner in rows:
        qualified = qualified_occurrence(label)
        reason = None
        if status not in {"resolved", "external_resolved", "alias_resolved"}:
            reason = "unresolved"
        elif not target or not entity or entity_owner != target:
            reason = "target_entity_owner_mismatch"
        elif qualified is not None:
            expected_doc, expected_label = qualified
            if len(occurrences[qualified]) > 1:
                reason = "qualified_occurrence_ambiguous"
            elif target != expected_doc or occurrences[qualified] != [entity]:
                reason = "qualified_occurrence_mismatch"
        if reason:
            issues.append({"reference_id": reference_id, "source": source, "label": label, "line": line,
                           "status": status, "target": target, "reason": reason})
    return {"checked": len(rows), "invalid": len(issues), "issues": issues}


def reading_reference_inventory(con):
    """Inventory legacy reading links without automatically changing their targets."""
    counts = Counter()
    legacy = []
    for source, label, line, status, target in con.execute(
            "SELECT source_document,target_label,line,status,target_document "
            "FROM references_tex WHERE command='atlasref' "
            "ORDER BY source_document,line,id"):
        counts["total"] += 1
        if qualified_occurrence(label) is not None:
            counts["qualified"] += 1
        else:
            counts["legacy"] += 1
            legacy.append({"source": source, "label": label, "line": line,
                           "status": status, "target": target})
    return {"total": counts["total"], "qualified": counts["qualified"],
            "legacy": counts["legacy"], "legacy_references": legacy}


def graph_coverage(con, catalog_path=None):
    docs = {r[0]: {"id": r[0], "domain": r[1], "title": r[2], "path": r[3]}
            for r in con.execute("SELECT id,domain,title,path FROM documents")}
    domains = sorted({d["domain"] for d in docs.values()})
    outgoing, incoming, internal, unresolved = Counter(), Counter(), Counter(), Counter()
    pairs = defaultdict(Counter)
    module_pairs = defaultdict(Counter)
    neighbors = defaultdict(set)
    cross_neighbors = defaultdict(set)
    reading_audit = reading_reference_issues(con)
    invalid_reading_ids = {issue["reference_id"] for issue in reading_audit["issues"]}
    for reference_id, s, t, cmd, status in con.execute(
            "SELECT id,source_document,target_document,command,status FROM references_tex"):
        if reference_id in invalid_reading_ids:
            unresolved[s] += 1
            continue
        if status not in {"resolved", "external_resolved", "alias_resolved", "included_resolved"} or t not in docs:
            unresolved[s] += 1
            continue
        if s not in docs or s == t:
            continue
        if docs[s]["domain"] == docs[t]["domain"]:
            internal[s] += 1
            internal[t] += 1
        else:
            cross_neighbors[s].add(t)
            cross_neighbors[t].add(s)
            outgoing[s] += 1
            incoming[t] += 1
            pairs[tuple(sorted((docs[s]["domain"], docs[t]["domain"])))][cmd] += 1
        module_pairs[(s, t)][cmd] += 1
        neighbors[s].add(t)
        neighbors[t].add(s)
    chapters = [{**d, "cross_outgoing": outgoing[m], "cross_incoming": incoming[m],
                 "within_domain": internal[m], "unresolved": unresolved[m],
                 "isolated": not neighbors[m],
                 "cross_isolated": not cross_neighbors[m]}
                for m, d in sorted(docs.items())]
    domain_coverage = [
        {"domain": domain, "chapters": len(group),
         "cross_linked": sum(not c["cross_isolated"] for c in group),
         "cross_isolated": sum(c["cross_isolated"] for c in group),
         "isolated_all_chapters": sum(c["isolated"] for c in group),
         "cross_isolated_ids": [c["id"] for c in group if c["cross_isolated"]]}
        for domain in domains
        for group in [[c for c in chapters if c["domain"] == domain]]
    ]
    domain_pairs = [{"left": a, "right": b, "references": sum(pairs[(a, b)].values()),
                     "reading": pairs[(a, b)]["atlasref"]}
                    for a, b in combinations(domains, 2)]
    remaining = set(docs)
    components = []
    while remaining:
        stack = [min(remaining)]
        component = set()
        while stack:
            m = stack.pop()
            if m in component:
                continue
            component.add(m)
            stack.extend(neighbors[m] - component)
        remaining.difference_update(component)
        components.append(sorted(component))
    components.sort(key=lambda c: (-len(c), c))
    catalog = None
    if catalog_path is not None:
        data = json.loads(Path(catalog_path).read_text(encoding="utf-8"))
        expected = [(module_id(Path(p)), p) for b in data["books"] for p in b["chapters"]]
        missing = [{"id": m, "path": p} for m, p in expected if m not in docs]
        mismatched = [{"id": m, "expected": p, "indexed": docs[m]["path"]}
                      for m, p in expected if m in docs
                      and not (p == docs[m]["path"] or p.endswith("/" + docs[m]["path"]))]
        expected_ids = {m for m, _ in expected}
        catalog = {"expected": len(expected), "missing": missing,
                   "indexed_outside_catalog": [docs[m] for m in sorted(set(docs) - expected_ids)],
                   "path_mismatches": mismatched,
                   "duplicate_ids": sorted(m for m, n in Counter(m for m, _ in expected).items() if n > 1)}
    reading_inventory = reading_reference_inventory(con)
    return {"evidence": "explicit_tex_references", "catalog": catalog,
            "reading_audit": reading_audit,
            "reading_inventory": reading_inventory,
            "chapters": chapters, "domain_pairs": domain_pairs,
            "domain_coverage": domain_coverage,
            "edges": [{"source": s, "target": t, "weight": sum(c.values()),
                       "reading": c["atlasref"]} for (s, t), c in sorted(module_pairs.items())],
            "components": components,
            "summary": {"indexed_chapters": len(docs), "domains": len(domains),
                        "cross_linked_chapters": sum(bool(c["cross_incoming"] or c["cross_outgoing"]) for c in chapters),
                        "isolated_chapters": sum(c["isolated"] for c in chapters),
                        "cross_isolated_chapters": sum(c["cross_isolated"] for c in chapters),
                        "all_reading_references": reading_inventory["total"],
                        "qualified_reading_references": reading_inventory["qualified"],
                        "legacy_reading_references": reading_inventory["legacy"],
                        "connected_domain_pairs": sum(p["references"] > 0 for p in domain_pairs),
                        "domain_pairs": len(domain_pairs),
                        "reading_references": sum(c["atlasref"] for c in module_pairs.values()),
                        "invalid_reading_references": reading_audit["invalid"]}}
