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

    def test_collision_priority_is_source_aware_and_preserves_provenance(self):
        # The same text in two scripts is not evidence of a single theorem.
        self.db.execute(
            "INSERT INTO documents VALUES (?,?,?,?,?)",
            ("A-02", "chapters/pl/algebra/02.tex", "algebra",
             "Algebra 2", "hash-a2")
        )
        self.db.execute(
            "INSERT INTO label_conflicts VALUES (?,?,?,?,?,?)",
            ("tw:y", "A-02", "t4", 53, 15, "different statement")
        )
        self.db.execute(
            "INSERT INTO references_tex VALUES (?,?,?,?,?,?,?,?,?,?)",
            (5, "A-02", None, "ref", "tw:y", 20, 120, "A", "t2", "resolved")
        )
        result = audit(self.db)
        by_name = {r["label"]: r for r in result["label_conflicts"]}
        self.assertEqual(result["counts"]["conflicting_label_names"], 2)
        self.assertEqual(result["counts"]["same_script_collision_names"], 1)
        self.assertEqual(result["counts"]["cross_script_only_collision_names"], 1)
        self.assertEqual(result["counts"]["referenced_collision_names"], 2)
        self.assertEqual(result["counts"]["ambiguous_colliding_reference_occurrences"], 1)
        self.assertEqual(by_name["tw:y"]["risk_class"], "referenced_same_script_collision")
        self.assertEqual(by_name["tw:y"]["owner_scripts"], ["A"])
        self.assertEqual(by_name["tw:y"]["all_reference_count"], 2)
        self.assertEqual(by_name["tw:y"]["resolved_reference_count"], 2)
        self.assertEqual(by_name["tw:x"]["risk_class"], "ambiguous_reference")
        self.assertEqual(by_name["tw:x"]["owner_scripts"], ["A", "B"])
        self.assertEqual(result["collision_priority_queue"][0]["label"], "tw:x")
        self.assertEqual(result["collision_priority_queue"][1]["label"], "tw:y")
        self.assertIn("Kolejka audytu", markdown(result))
        self.assertEqual(
            {(o["document_id"], o["sha256"]) for o in by_name["tw:y"]["owners"]},
            {("A", "hash-a"), ("A-02", "hash-a2")}
        )

    def test_unused_cross_script_collision_is_lower_priority(self):
        self.db.execute(
            "INSERT INTO label_conflicts VALUES (?,?,?,?,?,?)",
            ("tw:y", "C", "t5", 90, 22, "a third chapter")
        )
        result = audit(self.db)
        label = next(x for x in result["label_conflicts"] if x["label"] == "tw:y")
        self.assertEqual(label["risk_class"], "referenced_cross_script_shared_name")
        self.assertFalse(label["same_script_collision"])
        self.assertEqual(label["all_reference_count"], 1)

    def test_read_only_and_no_fake_owner(self):
        before = self.db.execute("SELECT count(*) FROM references_tex").fetchone()[0]
        result = audit(self.db)
        self.assertEqual(before,self.db.execute("SELECT count(*) FROM references_tex").fetchone()[0])
        self.assertEqual(result["unresolved_references"][1]["diagnosis"],"no_indexed_label_owner")
        self.assertNotIn("suggested_owner",str(result))

if __name__ == '__main__':
    unittest.main()