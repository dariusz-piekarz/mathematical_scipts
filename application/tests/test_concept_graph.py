"""Regressions for a source-grounded graph of mathematical concepts."""
from __future__ import annotations

import sqlite3
import unittest

from backend.concept_graph import build_concept_graph, resolve_concept


class ConceptGraphTests(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(":memory:")
        self.db.row_factory = sqlite3.Row
        self.db.executescript("""
            CREATE TABLE documents (id TEXT, title TEXT, domain TEXT, content TEXT);
            CREATE TABLE entities (
                id TEXT, document_id TEXT, kind TEXT, title TEXT,
                start_offset INTEGER, end_offset INTEGER, start_line INTEGER
            );
        """)
        sample = [
            ("LA-01", "Przestrzenie wektorowe", "algebra liniowa",
             "Przyjmijmy aksjomat wyboru (równoważnie lemat Zorna).\n"
             "Wynika stąd istnienie bazy Hamela każdej przestrzeni wektorowej."),
            ("FA-06", "Hahn–Banach", "analiza funkcjonalna",
             "Dowód Hahna--Banacha wykorzystuje lemat Kuratowskiego--Zorna."),
            ("DG-01", "Przestrzenie Hausdorffa", "topologia",
             "Przestrzeń jest Hausdorffa. To nie jest zasada maksymalności."),
            ("BT-01", "Etykiety i komentarze", "teoria mnogości",
             r"\label{lemat-zorna} % lemat Zorna"),
        ]
        for module, title, domain, content in sample:
            self.db.execute("INSERT INTO documents VALUES (?,?,?,?)",
                            (module, title, domain, content))
            self.db.execute("INSERT INTO entities VALUES (?,?,?,?,?,?,?)",
                            ("thm:"+module, module, "theorem", title,
                             0, len(content), 1))
        self.db.commit()

    def tearDown(self):
        self.db.close()

    def test_zorn_graph_distinguishes_relations_from_occurrences(self):
        result = build_concept_graph(self.db, "Zorn", max_occurrences=36)
        self.assertEqual(result["root"], "zorn")
        nodes = {n["id"]:n for n in result["nodes"]}
        for concept in ("choice", "hausdorff_max", "hamel", "well_order", "hahn_banach"):
            self.assertIn(concept, nodes)
        relation_edges = [e for e in result["edges"] if e["type"] != "occurrence"]
        self.assertTrue(any(e["target"] == "choice" and e["type"] == "equivalent"
                            for e in relation_edges))
        self.assertTrue(any(e["target"] == "hamel" and e["type"] == "implies"
                            for e in relation_edges))
        self.assertTrue(all(e["evidence"] == "curated_mathematical_relation"
                            for e in relation_edges))
        locations = [n for n in result["nodes"] if n["type"] == "occurrence"]
        self.assertTrue(any(n["module"] == "LA-01" and n["entity_id"] == "thm:LA-01"
                            for n in locations))
        self.assertTrue(any(n["module"] == "FA-06" for n in locations))
        self.assertTrue(all(n["line"] > 0 and n["snippet"] for n in locations))
        self.assertEqual(nodes["hausdorff_max"]["matches_total"], 0)
        self.assertFalse(any(n["module"] == "BT-01" for n in locations))
        self.assertTrue(all(e["source"] in nodes or e["source"] in {n["id"] for n in locations}
                            for e in result["edges"]))

    def test_reverse_relationship_preserves_actual_direction(self):
        result = build_concept_graph(self.db, "baza Hamela")
        self.assertEqual(result["root"], "hamel")
        self.assertTrue(any(e["source"] == "zorn" and e["target"] == "hamel"
                            for e in result["edges"]))
        self.assertFalse(any(e["source"] == "hamel" and e["target"] == "zorn"
                             for e in result["edges"]))

    def test_unknown_query_uses_only_literal_occurrences(self):
        result = build_concept_graph(self.db, "przestrzeni")
        self.assertEqual(result["root"], "query")
        self.assertEqual(result["relationships"], 0)
        self.assertTrue(result["occurrences_shown"] > 0)
        self.assertTrue(all(e["type"] == "occurrence" for e in result["edges"]))
        malicious = build_concept_graph(self.db, r"(?P<token>.*)")
        self.assertEqual(malicious["matches_total"], 0)

    def test_caps_and_no_result(self):
        self.assertEqual(build_concept_graph(self.db, "Zorn", max_occurrences=1)["occurrences_shown"], 1)
        self.assertEqual(build_concept_graph(self.db, "niewystępujący")["occurrences_shown"], 0)
        for query, limit in [("",36), ("Zorn",0), ("Zorn",81)]:
            with self.subTest(query=query, limit=limit), self.assertRaises(ValueError):
                build_concept_graph(self.db,query,max_occurrences=limit)
        self.assertEqual(resolve_concept("Lemat Zorna").key,"zorn")


if __name__ == "__main__":
    unittest.main()
