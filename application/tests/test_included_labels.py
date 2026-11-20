"""Regressions for \input labels without canonical-source rewrites."""
import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from backend.latex_parser import build_database,connect


class IncludedLabelTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.repo=Path(self.temp.name)
        self.src=self.repo/"chapters"/"pl"/"algebraic_geometry"
        self.src.mkdir(parents=True)
        (self.repo/"books"/"pl").mkdir(parents=True)
        (self.repo/"shared"/"pl").mkdir(parents=True)
        self.db=self.repo/"application"/"data"/"test.db"

    def tearDown(self):
        self.temp.cleanup()

    def test_literal_shared_input_preserves_provenance_and_resolves(self):
        shared=self.repo/"shared"/"pl"/"theorem.tex"
        shared.write_text(r"\begin{twierdzenie}\label{thm:shared}\label{thm:alias}Wynik.\end{twierdzenie}",
                          encoding="utf-8")
        original=r"\chapter{Test}\input{../../shared/pl/theorem.tex}"+"\n"+r"\ref{thm:shared} oraz \ref{thm:alias}"
        file=self.src/"10-example.tex"
        file.write_text(original,encoding="utf-8")
        stats=build_database(self.repo/"chapters"/"pl",self.db,recursive=True)
        self.assertEqual(stats["included_resolved_references"],2)
        self.assertEqual(stats["missing_references"],0)
        self.assertEqual(stats["included_labels"],2)
        self.assertEqual(file.read_text(encoding="utf-8"),original)
        with connect(self.db) as con:
            r=con.execute("SELECT target_document,target_entity,status FROM references_tex").fetchall()
            self.assertEqual([(x[0],x[1],x[2]) for x in r],
                             [("ALG-10",None,"included_resolved")]*2)
            origins=con.execute("SELECT name,origin_path,origin_line FROM included_label_origins ORDER BY name").fetchall()
            self.assertEqual({x[0] for x in origins},{"thm:alias","thm:shared"})
            self.assertTrue(all(x[1]=="shared/pl/theorem.tex" and x[2]==1 for x in origins))
            self.assertEqual(con.execute("SELECT count(*) FROM labels").fetchone()[0],0)
            self.assertEqual(con.execute("SELECT count(*) FROM label_occurrences").fetchone()[0],0)

    def test_comments_escaped_and_missing_input_are_not_indexed(self):
        (self.repo/"shared"/"pl"/"available.tex").write_text(r"\label{thm:unused}",encoding="utf-8")
        text="% \\input{../../shared/pl/available.tex}\n"+r"\input{../../shared/pl/not-there.tex}"+"\n"+r"\ref{thm:unused}"
        (self.src/"10-example.tex").write_text(text,encoding="utf-8")
        stats=build_database(self.repo/"chapters"/"pl",self.db,recursive=True)
        self.assertEqual(stats["missing_references"],1)
        self.assertEqual(stats["included_labels"],0)

    def test_nested_include_cycle_is_not_infinite(self):
        shared=self.repo/"shared"/"pl"
        (shared/"a.tex").write_text(r"\label{a}\input{../../shared/pl/b.tex}",encoding="utf-8")
        (shared/"b.tex").write_text(r"\label{b}\input{../../shared/pl/a.tex}",encoding="utf-8")
        (self.src/"10-example.tex").write_text(r"\input{../../shared/pl/a.tex}\ref{b}",encoding="utf-8")
        stats=build_database(self.repo/"chapters"/"pl",self.db,recursive=True)
        self.assertEqual(stats["included_resolved_references"],1)
        self.assertEqual(stats["included_labels"],2)


if __name__=="__main__":
    unittest.main()
