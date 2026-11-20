"""Deterministic provenance and alias tests; no canonical LaTeX edits."""
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from backend.label_registry import Owner, resolve
from backend.latex_parser import build_database, connect


class LabelRegistryTests(unittest.TestCase):
    def test_scoped_owner_before_global_duplicate(self):
        pool=[Owner("TOP-03","thm:chain","label:thm:chain"),
              Owner("DG-06","thm:chain","DG-06::label:thm:chain")]
        result=resolve("TOP-05","thm:chain",pool)
        self.assertEqual(result.status,"resolved")
        self.assertEqual(result.owner.occurrence_id,"TOP-03::thm:chain")
        self.assertEqual(resolve("DG-08","thm:chain",pool).owner.document_id,"DG-06")
        self.assertEqual(resolve("FA-01","thm:chain",pool).status,"ambiguous")

    def test_explicit_prefix_does_not_rewrite_source_label(self):
        pool=[Owner("P1-02","ch:probability"),Owner("P2-02","ch:probability")]
        result=resolve("P4-01","I-ch:probability",pool)
        self.assertEqual(result.status,"external_resolved")
        self.assertEqual(result.owner.occurrence_id,"P1-02::ch:probability")
        self.assertEqual(resolve("TOP-01","I-ch:probability",pool).status,"missing")
        self.assertEqual(resolve("P4-01","I-ch:absent",pool).status,"missing")

    def test_curated_alias_requires_real_owner_and_scope(self):
        owners=[Owner("TOP-03","thm:homotopia-homologia")]
        alias={("TOP-05","old-theorem"):("TOP-03","thm:homotopia-homologia")}
        result=resolve("TOP-05","old-theorem",owners,aliases=alias)
        self.assertEqual(result.status,"alias_resolved")
        self.assertEqual(result.owner.document_id,"TOP-03")
        self.assertEqual(resolve("DG-08","old-theorem",owners,aliases=alias).status,"missing")
        bad={("TOP-05","old-theorem"):("DG-06","thm:homotopia-homologia")}
        self.assertEqual(resolve("TOP-05","old-theorem",owners,aliases=bad).reason,"stale_alias")


class IntegratedIndexTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.root=Path(self.tmp.name)
        self.src=self.root/"chapters"/"pl"
        self.src.mkdir(parents=True)
        self.db=self.root/"data"/"app.db"

    def tearDown(self):
        self.tmp.cleanup()

    def add(self,subdir,name,body):
        folder=self.src/subdir
        folder.mkdir(exist_ok=True)
        (folder/name).write_text(body,encoding="utf-8")

    def test_index_resolves_two_domains_and_external_volume(self):
        self.add("algebraic_topology","03-chain.tex",r"\\chapter{T}\\label{ch:shared}")
        self.add("algebraic_topology","05-homology.tex",r"\\chapter{T}\\ref{ch:shared}")
        self.add("differential_geometry_and_topology","06-chain.tex",r"\\chapter{D}\\label{ch:shared}")
        self.add("differential_geometry_and_topology","08-homology.tex",r"\\chapter{D}\\ref{ch:shared}")
        self.add("probability_volume_i","02-probability.tex",r"\\chapter{I}\\label{ch:probability}")
        self.add("probability_volume_iv","01-statistics.tex",r"\\chapter{IV}\\ref{I-ch:probability}")
        results=build_database(self.src,self.db,recursive=True)
        self.assertEqual(results["ambiguous_references"],0)
        self.assertEqual(results["missing_references"],0)
        self.assertEqual(results["external_resolved_references"],1)
        with connect(self.db) as con:
            r=con.execute("SELECT source_document,target_label,target_document,status FROM references_tex ORDER BY source_document").fetchall()
            self.assertEqual([(x["source_document"],x["target_document"],x["status"]) for x in r],
                             [("DG-08","DG-06","resolved"),("P4-01","P1-02","external_resolved"),("TOP-05","TOP-03","resolved")])
            labels=con.execute("SELECT occurrence_id FROM label_occurrences WHERE name='ch:shared' ORDER BY occurrence_id").fetchall()
            self.assertEqual([x[0] for x in labels],["DG-06::ch:shared","TOP-03::ch:shared"])

    def test_cross_script_ambiguity_remains_visible(self):
        self.add("algebraic_topology","03-chain.tex",r"\\label{ch:shared}")
        self.add("differential_geometry_and_topology","06-chain.tex",r"\\label{ch:shared}")
        self.add("functional_analysis","01-uses.tex",r"\\ref{ch:shared}")
        results=build_database(self.src,self.db,recursive=True)
        self.assertEqual(results["ambiguous_references"],1)
        with connect(self.db) as con:
            ref=con.execute("SELECT status,target_document FROM references_tex").fetchone()
            self.assertEqual(ref["status"],"ambiguous")
            self.assertIsNone(ref["target_document"])


if __name__ == "__main__":
    unittest.main()
