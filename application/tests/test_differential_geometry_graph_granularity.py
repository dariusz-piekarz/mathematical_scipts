"""Independent end-to-end graph projection of canonical DG reading references."""
from collections import Counter
import json
from pathlib import Path
import sqlite3
from contextlib import closing
import tempfile
import unittest

from backend.api import bipartite_graph
from backend.label_registry import qualified_occurrence
from backend.latex_parser import build_database, module_id, parse_document

ROOT = Path(__file__).resolve().parents[2]
CANONICAL = ROOT / "chapters/pl"
HEADINGS = {"chapter", "section", "subsection", "subsubsection", "paragraph", "part"}


class DifferentialGeometryGraphGranularityTest(unittest.TestCase):
    def test_exact_endpoints_in_every_graph_projection(self):
        catalog = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))
        paths = {module_id(Path(name)): ROOT / name
                 for book in catalog["books"] for name in book["chapters"]}
        dg_ids = {mid for mid in paths if mid.startswith("DG-")}
        self.assertTrue({f"DG-{i:02d}" for i in range(1, 21)} <= dg_ids)
        wanted = set(dg_ids)
        expected = set()
        for mid in sorted(dg_ids):
            path = paths[mid]
            doc = parse_document(path.read_text(encoding="utf-8-sig"),
                                 str(path.relative_to(ROOT)))
            for ref in doc.references:
                if ref.command != "atlasref":
                    continue
                owner = qualified_occurrence(ref.target)
                self.assertIsNotNone(owner, (mid, ref.target))
                target, _ = owner
                self.assertIn(target, paths)
                wanted.add(target)
                if target not in dg_ids:
                    expected.add((mid, ref.target, target))
        self.assertGreaterEqual(len(expected), 35)

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "pl"
            for mid in sorted(wanted):
                source = paths[mid]
                dest = root / source.relative_to(CANONICAL)
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(source.read_bytes())
            db = Path(tmp) / "graph.db"
            build_database(root, db, recursive=True)
            with closing(sqlite3.connect(db)) as con, con:
                con.row_factory = sqlite3.Row
                documents = {r["id"]: r["domain"] for r in con.execute(
                    "SELECT id,domain FROM documents")}
                entities = {r["id"]: dict(r) for r in con.execute(
                    "SELECT id,document_id,parent_id,kind FROM entities")}
                rows = con.execute(
                    "SELECT source_document,source_entity,target_document,target_entity,"
                    " target_label,status FROM references_tex WHERE command='atlasref'"
                    " AND target_document IS NOT NULL"
                ).fetchall()
                dg_domains = {documents[mid] for mid in dg_ids}
                self.assertEqual(len(dg_domains), 1)
                dg_domain = dg_domains.pop()
                cross = [r for r in rows
                         if (r["source_document"] in dg_ids) !=
                            (r["target_document"] in dg_ids)]
                outgoing = {(r["source_document"], r["target_label"], r["target_document"])
                            for r in cross if r["source_document"] in dg_ids}
                self.assertEqual(outgoing, expected)

                def endpoint(eid, mid, level):
                    if level == "module":
                        return mid
                    self.assertIn(eid, entities)
                    self.assertEqual(entities[eid]["document_id"], mid)
                    if level == "entity":
                        return eid
                    visited = set()
                    while eid is not None:
                        self.assertNotIn(eid, visited, "cycle in entity ancestry")
                        visited.add(eid)
                        self.assertIn(eid, entities)
                        entity = entities[eid]
                        self.assertEqual(entity["document_id"], mid)
                        if entity["kind"] in HEADINGS:
                            return eid
                        eid = entity["parent_id"]
                    return mid

                other_domains = set(documents.values()) - {dg_domain}
                for other in sorted(other_domains):
                    relevant = [r for r in cross if {
                        documents[r["source_document"]], documents[r["target_document"]]
                    } == {dg_domain, other}]
                    self.assertTrue(relevant, other)
                    for level in ("module", "section", "entity"):
                        for left, right in ((dg_domain, other), (other, dg_domain)):
                            with self.subTest(domain=other, level=level, left=left):
                                required = Counter()
                                for r in relevant:
                                    self.assertEqual(r["status"], "external_resolved")
                                    s, t = r["source_document"], r["target_document"]
                                    a = endpoint(r["source_entity"], s, level)
                                    b = endpoint(r["target_entity"], t, level)
                                    pair = (a, b) if documents[s] == left else (b, a)
                                    required[pair] += 1
                                # Internal API: use a high bound so the test audits all
                                # edges, not just the UI's intentionally truncated view.
                                graph = bipartite_graph(con, left, right, level, 1, 100000)
                                self.assertFalse(graph["truncated"])
                                nodes = {n["id"]: n for n in graph["nodes"]}
                                actual = {}
                                for edge in graph["edges"]:
                                    a, b = nodes[edge["source"]], nodes[edge["target"]]
                                    self.assertEqual((a["domain"], b["domain"]), (left, right))
                                    self.assertEqual((a["side"], b["side"]), ("left", "right"))
                                    actual[a["entity_id"], b["entity_id"]] = edge["weight"]
                                for pair, weight in required.items():
                                    self.assertGreaterEqual(actual.get(pair, 0), weight, pair)


if __name__ == "__main__":
    unittest.main()
