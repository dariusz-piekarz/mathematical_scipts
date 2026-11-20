"""Regression cases for audit aggregation and exact provenance (in-memory only)."""
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from audit_reference_provenance import audit, markdown, main


class ReferenceProvenanceAuditTests(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(":memory:")
        self.db.row_factory = sqlite3.Row
        self.db.executescript("""
        CREATE TABLE documents(id TEXT,path TEXT,domain TEXT,title TEXT,sha256 TEXT);
        CREATE TABLE labels(name TEXT,document_id TEXT,entity_id TEXT,offset INTEGER,line INTEGER,excerpt TEXT);
        CREATE TABLE label_conflicts(name TEXT,document_id TEXT,entity_id TEXT,offset INTEGER,line INTEGER,excerpt TEXT);
        CREATE TABLE references_tex(id INTEGER PRIMARY KEY,source_document TEXT,source_entity TEXT,
            command TEXT,target_label TEXT,line INTEGER,offset INTEGER,
            target_document TEXT,target_entity TEXT,status TEXT);
        INSERT INTO documents VALUES
          ('A','chapters/pl/algebra/01.tex','algebra','Algebra','hash-a'),
          ('B','chapters/pl/topology/01.tex','topologia','Topologia','hash-b'),
          ('C','chapters/pl/topology/02.tex','topologia','Topologia 2','hash-c');
        INSERT INTO labels VALUES ('tw:x','A','t1',7,3,'twierdzenie A'),('tw:y','A','t2',9,4,'twierdzenie Y');
        INSERT INTO label_conflicts VALUES
          ('tw:x','A','t1',7,3,'twierdzenie A'),
          ('tw:x','B','t3',12,5,'twierdzenie B');
        INSERT INTO references_tex VALUES
          (1,'C',NULL,'ref','tw:x',9,40,NULL,NULL,'ambiguous'),
          (2,'C',NULL,'ref','tw:missing',10,62,NULL,NULL,'missing'),
          (3,'A',NULL,'ref','tw:x',11,80,'A','t1','resolved'),
          (4,'B',NULL,'ref','tw:y',12,90,'A','t2','resolved');
        """)

    def tearDown(self):
        self.db.close()

    def test_provenance_and_counts(self):
        result = audit(self.db)
        self.assertEqual(result["counts"]["documents"],3)
        self.assertEqual(result["counts"]["reference_statuses"],{"ambiguous":1,"missing":1,"resolved":2})
        self.assertEqual(result["counts"]["unresolved_occurrences"],2)
        self.assertEqual(result["counts"]["conflicting_label_names"],1)
        ref = result["unresolved_references"][0]
        self.assertEqual(ref["target_label"],"tw:x")
        self.assertEqual({o["document_id"] for o in ref["candidates"]},{"A","B"})
        self.assertEqual({o["sha256"] for o in ref["candidates"]},{"hash-a","hash-b"})
        self.assertEqual(result["label_conflicts"][0]["ambiguous_reference_count"],1)
        self.assertEqual(result["unresolved_references"][1]["candidates"],[])
        self.assertIn("C:9",markdown(result))
        self.assertIn("topology/01.tex",markdown(result))

    def test_read_only_and_no_fake_owner(self):
        before = self.db.execute("SELECT count(*) FROM references_tex").fetchone()[0]
        result = audit(self.db)
        self.assertEqual(before,self.db.execute("SELECT count(*) FROM references_tex").fetchone()[0])
        self.assertEqual(result["unresolved_references"][1]["diagnosis"],"no_indexed_label_owner")
        self.assertNotIn("suggested_owner",str(result))

if __name__ == '__main__':
    unittest.main()