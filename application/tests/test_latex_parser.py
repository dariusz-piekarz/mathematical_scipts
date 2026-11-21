"""Testy funkcjonalne parsera i bazy. Uruchom: python -m unittest discover -s tests -v"""
from pathlib import Path
from contextlib import closing
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from backend.latex_parser import (
    analyze_selection, build_database, connect, graph_edges, grouped, masked_source, parse_document,
    search, show_label,
)


class ParserTests(unittest.TestCase):
    def test_nested_arguments(self):
        x = r"{Tytuł z {zagnieżdżeniem} oraz \textbf{tekstem}}"
        self.assertEqual(grouped(x, 0), (x[1:-1], len(x)))

    def test_comment_and_escaped_percent(self):
        txt = "tekst \\% nie komentarz \\ref{widoczny}\n% \\ref{ukryty}\n\\ref{tak}"
        masked = masked_source(txt)
        self.assertNotIn("\\ref{ukryty}", masked)
        self.assertIn("\\ref{widoczny}", masked)
        self.assertIn("\\ref{tak}", masked)
        self.assertEqual(len(masked), len(txt))
        self.assertEqual([i for i,x in enumerate(masked) if x=='\n'], [i for i,x in enumerate(txt) if x=='\n'])

    def test_verbatim_and_inline_verb(self):
        txt = "\\begin{lstlisting}\n\\ref{zly}\n\\end{lstlisting}\n\\verb|\\ref{zly2}| \\ref{dobry}"
        doc = parse_document(txt, "rozdzialy/ALG-00--test.tex")
        self.assertEqual([x.target for x in doc.references], ["dobry"])

    def test_heading_nested_reference(self):
        doc = parse_document(r"\chapter{Wstęp \ref{pojecie}}\label{ch:wstep}", "rozdzialy/TOP-01--x.tex")
        self.assertEqual([r.target for r in doc.references], ["pojecie"])
        self.assertEqual(doc.labels[0].entity_id, "label:ch:wstep")

    def test_theorem_label_is_owned(self):
        txt = ("\\chapter{X}\\label{ch:x}\n\\begin{twierdzenie}[Własność]"
               "\\label{tw:w}Niech X ...\\end{twierdzenie}\n"
               "\\begin{proof}Dowód.\\end{proof}\n")
        d = parse_document(txt, "rozdzialy/ALG-00--x.tex")
        self.assertEqual(next(l for l in d.labels if l.name=="tw:w").entity_id,
                         "label:tw:w")
        self.assertEqual(next(e for e in d.entities if e.kind=="theorem").title, "Własność")
        self.assertTrue(any(e.kind=="proof" for e in d.entities))

    def test_multi_ref_and_hyperref(self):
        d = parse_document(r"\cref{tw:x,lem:y} \eqref{eq:z} \hyperref[sec:abc]{tekst}", "rozdzialy/TOP-00--test.tex")
        self.assertEqual([r.target for r in d.references], ["tw:x", "lem:y", "eq:z", "sec:abc"])

    def test_parent_section_and_line(self):
        txt = "\\chapter{A}\n\\section{B}\n\\begin{definicja}\\label{def:b}Treść\\end{definicja}"
        d = parse_document(txt, "rozdzialy/GA-00--x.tex")
        section = next(e for e in d.entities if e.kind == "section")
        child = next(e for e in d.entities if e.kind == "definition")
        self.assertEqual(child.parent_id, section.id)
        self.assertEqual(d.labels[0].line, 3)

    def test_label_id_persists_after_new_preceding_theorem(self):
        fixed = r"\chapter{A}\begin{twierdzenie}\label{tw:stable}Zdanie\end{twierdzenie}"
        added = r"\chapter{A}\begin{twierdzenie}Nowe\end{twierdzenie}\begin{twierdzenie}\label{tw:stable}Zdanie\end{twierdzenie}"
        before = parse_document(fixed, "rozdzialy/TOP-00--test.tex")
        after = parse_document(added, "rozdzialy/TOP-00--test.tex")
        self.assertEqual(before.labels[0].entity_id, after.labels[0].entity_id)
        self.assertEqual(after.labels[0].entity_id, "label:tw:stable")

    def test_starred_heading(self):
        d = parse_document(r"\section*{Podsumowanie}", "rozdzialy/TOP-00--test.tex")
        self.assertTrue(d.entities[0].starred)


class DatabaseTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        folder = self.root / "rozdzialy"
        folder.mkdir()
        (folder / "ALG-00--start.tex").write_text(
            "\\chapter{Algebra}\\label{ch:alg}\n\\begin{twierdzenie}"
            "\\label{tw:alg}Własność\\end{twierdzenie}", encoding="utf8")
        (folder / "TOP-00--top.tex").write_text(
            "\\chapter{Topologia}\\label{ch:top}"
            "Wykorzystujemy \\ref{tw:alg}.", encoding="utf8")
        self.path = self.root / "data" / "biblioteka.db"
        self.folder = folder

    def tearDown(self): self.tmp.cleanup()

    def test_index_and_graph(self):
        report=build_database(self.folder,self.path)
        self.assertEqual(report["documents"], 2)
        self.assertEqual(report["labels"],3)
        self.assertEqual(report["references"],1)
        self.assertEqual(report["missing_references"],0)
        self.assertEqual(report["cross_document_edges"],1)
        with closing(connect(self.path)) as c:
            self.assertEqual(graph_edges(c)[0]["source_document"], "TOP-00")
            self.assertIn("Własność", show_label(c,"tw:alg")["latex"])
            self.assertTrue(search(c,"Algebra"))

    def test_plan_external_reference(self):
        build_database(self.folder, self.path)
        with closing(connect(self.path)) as c:
            plan = analyze_selection(c,["TOP-00"])
            self.assertEqual(plan["external_references"],1)
            self.assertEqual(plan["internal_references"],0)
            self.assertEqual(plan["external_targets"][0]["module"],"ALG-00")
            self.assertEqual(plan["external_targets"][0]["labels"],["tw:alg"])

    def test_missing_ref_is_reported(self):
        (self.folder / "TOP-00--top.tex").write_text("\\ref{nieistnieje}",encoding="utf8")
        report=build_database(self.folder,self.path)
        self.assertEqual(report["missing_references"],1)
        self.assertEqual(report["missing_targets"][0]["target_label"],"nieistnieje")

    def test_duplicate_label_is_reported(self):
        (self.folder / "TOP-00--top.tex").write_text("\\label{ch:alg}",encoding="utf8")
        report=build_database(self.folder,self.path)
        self.assertEqual(report["duplicate_labels"],1)
        self.assertEqual(report["duplicate_labels_detail"][0]["label"],"ch:alg")

    def test_reproducibility(self):
        r1=build_database(self.folder,self.path)
        r2=build_database(self.folder,self.path)
        for k in ("documents","entities","labels","references","missing_references"):
            self.assertEqual(r1[k],r2[k])


if __name__ == "__main__":
    unittest.main()