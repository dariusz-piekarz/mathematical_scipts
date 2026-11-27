"""Testy funkcjonalne parsera i bazy. Uruchom: python -m unittest discover -s tests -v"""
from pathlib import Path
from contextlib import closing, redirect_stdout
import io
from concurrent.futures import ThreadPoolExecutor
from threading import Barrier, Event
import sqlite3
from unittest.mock import patch
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from backend.latex_parser import (
    analyze_selection, build_database, connect, graph_edges, grouped, masked_source, parse_document,
    main, search, show_label,
)


class ParserTests(unittest.TestCase):
    def test_mathematical_analysis_i_identity_and_template(self):
        from backend.generator import MODULE_ID, PROJECT_TEMPLATE_KEYS
        doc = parse_document(r"\chapter{Liczby}", "chapters/pl/mathematical_analysis_i/01-konstrukcja-systemow-liczbowych.tex")
        self.assertEqual(doc.id, "AM1-01")
        self.assertEqual(doc.domain, "analiza matematyczna I")
        self.assertIsNotNone(MODULE_ID.fullmatch(doc.id))
        self.assertEqual(PROJECT_TEMPLATE_KEYS["AM1"], "AM1")
        root = Path(__file__).resolve().parents[1]
        template = (root / "config/preambles/AM1.tex").read_text(encoding="utf-8")
        book = (root.parent / "books/pl/mathematical_analysis_i.tex").read_text(encoding="utf-8")
        self.assertEqual(template.strip(), book.split(r"\begin{document}", 1)[0].strip())

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

    def test_failed_rebuild_closes_connection_and_preserves_index(self):
        build_database(self.folder, self.path)
        before = self.path.read_bytes()
        (self.folder / "TOP-00--top.tex").write_bytes(b"\xff")
        opened = []
        real_connect = sqlite3.connect

        def track(*args, **kwargs):
            con = real_connect(*args, **kwargs)
            opened.append(con)
            return con

        with patch("backend.latex_parser.sqlite3.connect", side_effect=track):
            with self.assertRaises(UnicodeDecodeError):
                build_database(self.folder, self.path)
        self.assertEqual(len(opened), 1)
        with self.assertRaises(sqlite3.ProgrammingError):
            opened[0].execute("SELECT 1")
        self.assertEqual(list(self.path.parent.glob(f".{self.path.name}.build-*")), [])
        self.assertEqual(self.path.read_bytes(), before)
        with closing(connect(self.path)) as con:
            self.assertEqual(con.execute("SELECT count(*) FROM documents").fetchone()[0], 2)

    def test_replacement_failure_preserves_previous_index(self):
        build_database(self.folder, self.path)
        before = self.path.read_bytes()
        with patch.object(Path, "replace", side_effect=PermissionError("fixture")):
            with self.assertRaises(PermissionError):
                build_database(self.folder, self.path)
        self.assertEqual(self.path.read_bytes(), before)
        self.assertEqual(list(self.path.parent.glob(f".{self.path.name}.build-*")), [])

    def test_parallel_builds_publish_only_complete_private_databases(self):
        from backend import latex_parser
        other = self.root / "other"
        other.mkdir()
        (other / "TOP-01--other.tex").write_text(r"\chapter{Other}", encoding="utf-8")
        populate = latex_parser._populate_database
        barrier = Barrier(2, timeout=15)
        staged = []

        def overlap(con, *args):
            staged.append(Path(con.execute("PRAGMA database_list").fetchone()[2]))
            barrier.wait()
            return populate(con, *args)

        with patch.object(latex_parser, "_populate_database", side_effect=overlap):
            with ThreadPoolExecutor(max_workers=2) as pool:
                a = pool.submit(build_database, self.folder, self.path)
                b = pool.submit(build_database, other, self.path)
                self.assertEqual(a.result(timeout=30)["documents"], 2)
                self.assertEqual(b.result(timeout=30)["documents"], 1)
        self.assertEqual(len(set(staged)), 2)
        self.assertEqual(list(self.path.parent.glob(f".{self.path.name}.build-*")), [])
        with closing(connect(self.path)) as con:
            self.assertEqual(con.execute("PRAGMA integrity_check").fetchone()[0], "ok")
            ids = {row[0] for row in con.execute("SELECT id FROM documents")}
            self.assertIn(ids, ({"ALG-00", "TOP-00"}, {"TOP-01"}))

    def test_failed_parallel_build_does_not_remove_other_staging(self):
        from backend import latex_parser
        build_database(self.folder, self.path)
        broken = self.root / "broken"
        broken.mkdir()
        (broken / "TOP-02--broken.tex").write_bytes(b"\xff")
        populate = latex_parser._populate_database
        barrier = Barrier(2, timeout=15)
        failed = Event()

        def overlap(con, files, source_dir, *args):
            barrier.wait()
            if source_dir == self.folder:
                if not failed.wait(timeout=15):
                    raise AssertionError("failed build did not finish")
            return populate(con, files, source_dir, *args)

        def fail_build():
            try:
                build_database(broken, self.path)
            finally:
                failed.set()

        with patch.object(latex_parser, "_populate_database", side_effect=overlap):
            with ThreadPoolExecutor(max_workers=2) as pool:
                bad = pool.submit(fail_build)
                good = pool.submit(build_database, self.folder, self.path)
                with self.assertRaises(UnicodeDecodeError):
                    bad.result(timeout=30)
                self.assertEqual(good.result(timeout=30)["documents"], 2)
        self.assertEqual(list(self.path.parent.glob(f".{self.path.name}.build-*")), [])
        with closing(connect(self.path)) as con:
            self.assertEqual(con.execute("PRAGMA integrity_check").fetchone()[0], "ok")
            self.assertEqual(con.execute("SELECT count(*) FROM documents").fetchone()[0], 2)

    def test_cli_closes_connection_on_normal_and_early_return(self):
        build_database(self.folder, self.path)
        for args in (["stats"], ["graph", "--format", "tsv"],
                     ["show", "--label", "missing"]):
            with self.subTest(args=args):
                con = connect(self.path)
                with patch("backend.latex_parser.connect", return_value=con):
                    with redirect_stdout(io.StringIO()):
                        main([*args, "--db", str(self.path)])
                with self.assertRaises(sqlite3.ProgrammingError):
                    con.execute("SELECT 1")

    def test_cli_closes_connection_on_exception(self):
        build_database(self.folder, self.path)
        con = connect(self.path)
        with patch("backend.latex_parser.connect", return_value=con):
            with patch("backend.latex_parser.get_stats", side_effect=RuntimeError("fixture")):
                with self.assertRaises(RuntimeError):
                    main(["stats", "--db", str(self.path)])
        with self.assertRaises(sqlite3.ProgrammingError):
            con.execute("SELECT 1")

    def test_reproducibility(self):
        r1=build_database(self.folder,self.path)
        r2=build_database(self.folder,self.path)
        for k in ("documents","entities","labels","references","missing_references"):
            self.assertEqual(r1[k],r2[k])


if __name__ == "__main__":
    unittest.main()