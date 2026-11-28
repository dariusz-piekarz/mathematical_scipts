"""Explorer and path API must agree with audited graph coverage."""
from contextlib import contextmanager
import sqlite3
import unittest
from unittest.mock import patch

from backend import api
from backend.graph_coverage import graph_coverage


class GraphAPIConsistencyTest(unittest.TestCase):
    def setUp(self):
        self.con = sqlite3.connect(":memory:")
        self.con.row_factory = sqlite3.Row
        self.addCleanup(self.con.close)
        self.con.executescript("""
            CREATE TABLE documents(id TEXT, domain TEXT, title TEXT, path TEXT,
                                   sha256 TEXT, content TEXT);
            CREATE TABLE entities(id TEXT, document_id TEXT, parent_id TEXT,
                                  kind TEXT, title TEXT);
            CREATE TABLE label_occurrences(document_id TEXT, name TEXT, entity_id TEXT);
            CREATE TABLE references_tex(id INTEGER PRIMARY KEY, source_document TEXT,
                target_label TEXT, line INTEGER, status TEXT, target_document TEXT,
                target_entity TEXT, command TEXT, source_entity TEXT);
            INSERT INTO documents VALUES
                ('AA-01','AA','A','a.tex','',''),
                ('LA-01','LA','B','b.tex','',''),
                ('GT-01','GT','C','c.tex','','');
            INSERT INTO entities VALUES
                ('a','AA-01',NULL,'section','A'),
                ('b','LA-01',NULL,'section','B'),
                ('c','GT-01',NULL,'section','C');
            INSERT INTO label_occurrences VALUES ('AA-01','shared','a'),('GT-01','other','c');
            INSERT INTO references_tex VALUES
                (1,'LA-01','AA-01::shared',1,'external_resolved','AA-01','a','atlasref','b'),
                (2,'GT-01','AA-01::shared',1,'external_resolved','AA-01','a','atlasref','c');
        """)

    def path(self, source, target):
        @contextmanager
        def connection():
            yield self.con
        with patch.object(api, "db_connection", connection):
            return api.graph_path(source, target)

    def test_valid_edges_and_paths(self):
        for granularity in ("module", "section", "entity"):
            with self.subTest(granularity=granularity):
                result = api.bipartite_graph(self.con, "AA", "LA", granularity, 1, 50)
                self.assertEqual(len(result["edges"]), 1)
                self.assertEqual(result["edges"][0]["weight"], 1)
        result = self.path("LA-01", "GT-01")
        self.assertTrue(result["found"])
        self.assertEqual([m["id"] for m in result["modules"]],
                         ["LA-01", "AA-01", "GT-01"])

    def test_wrong_qualified_target_does_not_form_edge_or_path(self):
        self.con.execute("UPDATE references_tex SET target_label='GT-01::other' WHERE id=2")
        self.assertEqual(graph_coverage(self.con)["summary"]["invalid_reading_references"], 1)
        for granularity in ("module", "section", "entity"):
            with self.subTest(granularity=granularity):
                result = api.bipartite_graph(self.con, "AA", "GT", granularity, 1, 50)
                self.assertEqual(result["edges"], [])
                self.assertEqual(result["nodes"], [])
        self.assertFalse(self.path("LA-01", "GT-01")["found"])
        self.assertTrue(self.path("LA-01", "AA-01")["found"])
        same = self.path("GT-01", "GT-01")
        self.assertTrue(same["found"])
        self.assertEqual(same["steps"], [])

    def test_duplicate_occurrence_does_not_inflate_weights(self):
        self.con.execute("INSERT INTO label_occurrences VALUES ('AA-01','shared','a')")
        self.con.execute("""INSERT INTO references_tex VALUES
            (3,'LA-01','shared',2,'external_resolved','AA-01','a','ref','b')""")
        coverage = graph_coverage(self.con)
        self.assertEqual(coverage["summary"]["invalid_reading_references"], 2)
        for granularity in ("module", "section", "entity"):
            result = api.bipartite_graph(self.con, "AA", "LA", granularity, 1, 50)
            self.assertEqual([e["weight"] for e in result["edges"]], [1])
        self.assertEqual(self.path("LA-01", "AA-01")["steps"][0]["weight"], 1)
        self.assertFalse(self.path("GT-01", "AA-01")["found"])
