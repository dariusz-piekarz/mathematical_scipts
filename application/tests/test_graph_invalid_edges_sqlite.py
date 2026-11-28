"""Direct SQLite regression tests for the exclusion of invalid graph edges."""
import sqlite3
import unittest

from backend.graph_coverage import graph_coverage


class TestCoverageInvalidEdges(unittest.TestCase):
    def setUp(self):
        self.con = sqlite3.connect(':memory:')
        self.addCleanup(self.con.close)
        self.con.executescript('''
        CREATE TABLE documents(id TEXT, domain TEXT, title TEXT, path TEXT);
        CREATE TABLE entities(id TEXT, document_id TEXT);
        CREATE TABLE label_occurrences(document_id TEXT, name TEXT, entity_id TEXT);
        CREATE TABLE references_tex(id INTEGER PRIMARY KEY, source_document TEXT, target_label TEXT, line INTEGER, status TEXT, target_document TEXT, target_entity TEXT, command TEXT);
        INSERT INTO documents VALUES ('AA-01','AA','A','a.tex'),('LA-01','LA','B','b.tex');
        INSERT INTO entities VALUES ('a','AA-01'),('b','LA-01');
        INSERT INTO label_occurrences VALUES ('AA-01','shared','a'),('LA-01','other','b');
        INSERT INTO references_tex VALUES (1,'LA-01','AA-01::shared',1,'external_resolved','AA-01','a','atlasref');
        ''')

    def test_valid(self):
        r = graph_coverage(self.con)
        self.assertEqual(r['edges'], [dict(source='LA-01', target='AA-01', weight=1, reading=1)])
        self.assertEqual(r['components'], [['AA-01', 'LA-01']])

    def assert_invalid(self, reason):
        r = graph_coverage(self.con)
        self.assertEqual(r['reading_audit']['issues'][0]['reason'], reason)
        self.assertEqual(r['reading_audit']['issues'][0]['reference_id'], 1)
        self.assertEqual(r['edges'], [])
        self.assertEqual(r['summary']['cross_linked_chapters'], 0)
        self.assertEqual(r['summary']['isolated_chapters'], 2)
        self.assertEqual(r['summary']['reading_references'], 0)
        self.assertEqual(r['summary']['all_reading_references'], 1)
        self.assertEqual(r['summary']['invalid_reading_references'], 1)
        self.assertEqual(r['components'], [['AA-01'], ['LA-01']])
        self.assertEqual({c['id']: c['unresolved'] for c in r['chapters']},
                         {'AA-01': 0, 'LA-01': 1})

    def test_ambiguous(self):
        self.con.execute("INSERT INTO label_occurrences VALUES ('AA-01','shared','a')")
        self.assert_invalid('qualified_occurrence_ambiguous')

    def test_wrong_entity_owner(self):
        self.con.execute("UPDATE references_tex SET target_entity='b'")
        self.assert_invalid('target_entity_owner_mismatch')

    def test_wrong_qualified_occurrence(self):
        self.con.execute("UPDATE references_tex SET target_label='LA-01::other'")
        self.assert_invalid('qualified_occurrence_mismatch')

    def test_unresolved(self):
        self.con.execute("UPDATE references_tex SET status='unresolved'")
        self.assert_invalid('unresolved')

    def test_valid_ordinary_ref_preserved(self):
        self.con.execute("INSERT INTO label_occurrences VALUES ('AA-01','shared','a')")
        self.con.execute("INSERT INTO references_tex VALUES (2,'LA-01','shared',2,'external_resolved','AA-01','a','ref')")
        r = graph_coverage(self.con)
        self.assertEqual(r['edges'], [dict(source='LA-01', target='AA-01', weight=1, reading=0)])
        self.assertEqual(r['summary']['cross_linked_chapters'], 2)
        self.assertEqual(r['reading_audit']['invalid'], 1)
