from contextlib import closing
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest

from backend.graph_coverage import graph_coverage, reading_reference_issues
from backend.latex_parser import build_database


class GraphCoverageTest(unittest.TestCase):
    def test_isolated_chapters_missing_catalog_entries_and_direction(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            root = base / "pl"
            sources = {
                "abstract_algebra/01-a.tex": r"\chapter{A}\label{aa:a}",
                "linear_algebra/01-b.tex": r"\chapter{B}\atlasref{AA-01::aa:a}{A}",
                "linear_algebra/02-c.tex": r"\chapter{C}\ref{missing}",
                "general_topology/01-d.tex": r"\chapter{D}",
            }
            for p, body in sources.items():
                dest = root / p
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(body, encoding="utf-8")
            catalog = base / "books.json"
            catalog.write_text(json.dumps({"books": [{"chapters": [
                "chapters/pl/" + p for p in sources
            ] + ["chapters/pl/abstract_algebra/02-missing.tex"]}]}), encoding="utf-8")
            db = base / "test.db"
            build_database(root, db, recursive=True)
            with closing(sqlite3.connect(db)) as con, con:
                report = graph_coverage(con, catalog)
            self.assertEqual(report["summary"]["indexed_chapters"], 4)
            self.assertEqual(report["summary"]["cross_linked_chapters"], 2)
            self.assertEqual(report["summary"]["isolated_chapters"], 2)
            self.assertEqual(report["summary"]["connected_domain_pairs"], 1)
            self.assertEqual(report["summary"]["domain_pairs"], 3)
            self.assertEqual(report["catalog"]["missing"][0]["id"], "AA-02")
            self.assertEqual(report["catalog"]["path_mismatches"], [])
            self.assertEqual(report["edges"], [
                {"source": "LA-01", "target": "AA-01", "weight": 1, "reading": 1}
            ])
            chapters = {c["id"]: c for c in report["chapters"]}
            self.assertEqual(chapters["LA-02"]["unresolved"], 1)
            self.assertTrue(chapters["GT-01"]["isolated"])
            self.assertEqual(chapters["AA-01"]["cross_incoming"], 1)
            self.assertEqual(chapters["LA-01"]["cross_outgoing"], 1)


    def test_reading_audit_rejects_missing_and_wrong_occurrence(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "pl"
            for relative, body in {
                "abstract_algebra/01-a.tex": r"\chapter{A}\label{shared}",
                "abstract_algebra/02-b.tex": r"\chapter{B}\label{shared}",
                "linear_algebra/01-c.tex": (
                    r"\chapter{C}\atlasref{AA-01::shared}{A}"
                    r"\atlasref{AA-02::shared}{B}"
                    r"\atlasref{AA-03::shared}{Missing}"
                ),
            }.items():
                dest = root / relative
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(body, encoding="utf-8")
            db = Path(tmp) / "index.db"
            build_database(root, db, recursive=True)
            with closing(sqlite3.connect(db)) as con, con:
                audit = reading_reference_issues(con)
                self.assertEqual(audit["checked"], 3)
                self.assertEqual(audit["invalid"], 1)
                self.assertEqual(audit["issues"][0]["reason"], "unresolved")
                wrong = con.execute(
                    "SELECT entity_id FROM label_occurrences "
                    "WHERE document_id='AA-02' AND name='shared'"
                ).fetchone()[0]
                con.execute(
                    "UPDATE references_tex SET target_document='AA-02', target_entity=? "
                    "WHERE target_label='AA-01::shared'", (wrong,))
                audit = reading_reference_issues(con)
                self.assertEqual(audit["invalid"], 2)
                self.assertEqual({i["reason"] for i in audit["issues"]},
                                 {"unresolved", "qualified_occurrence_mismatch"})
                self.assertEqual(graph_coverage(con)["summary"]["invalid_reading_references"], 2)
                # Wrong entity from a different chapter must be distinguished
                # from a self-consistent but incorrectly selected occurrence.
                con.execute(
                    "UPDATE references_tex SET target_document='AA-01' "
                    "WHERE target_label='AA-01::shared'")
                audit = reading_reference_issues(con)
                self.assertEqual({i["reason"] for i in audit["issues"]},
                                 {"unresolved", "target_entity_owner_mismatch"})
                self.assertEqual(audit["checked"], 3)

    def test_reading_audit_rejects_wrong_entity_in_same_chapter(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "pl"
            for relative, body in {
                "measure_theory/01-a.tex": (
                    "\\chapter{Miary}\n\\section{Pierwsza}\\label{first}\n"
                    "\\section{Druga}\\label{second}\n"),
                "functional_analysis/15B-b.tex": (
                    "\\section{Całki}\\atlasref{ME-01::first}{Pierwsza}\n"
                    "\\ref{ordinary-missing}\n"),
            }.items():
                dest = root / relative
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(body, encoding="utf-8")
            db = Path(tmp) / "index.db"
            build_database(root, db, recursive=True)
            with closing(sqlite3.connect(db)) as con, con:
                self.assertEqual(reading_reference_issues(con),
                                 {"checked": 1, "invalid": 0, "issues": []})
                wrong = con.execute(
                    "SELECT entity_id FROM label_occurrences "
                    "WHERE document_id='ME-01' AND name='second'"
                ).fetchone()[0]
                con.execute(
                    "UPDATE references_tex SET target_entity=? WHERE command='atlasref'",
                    (wrong,))
                audit = reading_reference_issues(con)
                self.assertEqual(audit["invalid"], 1)
                self.assertEqual(audit["issues"][0]["reason"],
                                 "qualified_occurrence_mismatch")

    def test_canonical_measure_topology_reading_edges(self):
        """Regression: Radon/Riesz proofs link to exact topology results."""
        canonical = Path(__file__).resolve().parents[2] / "chapters" / "pl"
        if not canonical.is_dir():
            self.skipTest("canonical repository chapters not available")
        paths = (
            "measure_theory/20-miary-borelowskie-regularnosc-i-miary-radona.tex",
            "measure_theory/21-twierdzenie-riesza-markowa-kakutaniego.tex",
            "general_topology/09-aksjomaty-przeliczalnosci.tex",
            "general_topology/10-metryzowalnosc.tex",
        )
        expected = (
            ("ME-20", "GT-09", "thm:topog-metryczne-trzy-warunki"),
            ("ME-21", "GT-09", "thm:topog-metryczne-trzy-warunki"),
            ("ME-21", "GT-10", "thm:topog-urysohn-metryzowalnosc"),
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "pl"
            for relative in paths:
                dest = root / relative
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes((canonical / relative).read_bytes())
            db = Path(tmp) / "index.db"
            build_database(root, db, recursive=True)
            with closing(sqlite3.connect(db)) as con, con:
                edges = {(e["source"], e["target"]): e
                         for e in graph_coverage(con)["edges"]}
                for source, target, label in expected:
                    with self.subTest(source=source, target=target, label=label):
                        rows = con.execute(
                            "SELECT status,target_document,target_entity "
                            "FROM references_tex WHERE source_document=? "
                            "AND command='atlasref' AND target_label=?",
                            (source, target + "::" + label),
                        ).fetchall()
                        self.assertEqual(len(rows), 1)
                        status, owner, entity = rows[0]
                        self.assertEqual(status, "external_resolved")
                        self.assertEqual(owner, target)
                        self.assertEqual(con.execute(
                            "SELECT entity_id FROM label_occurrences "
                            "WHERE document_id=? AND name=?", (target, label)
                        ).fetchall(), [(entity,)])
                        self.assertGreaterEqual(edges[(source, target)]["reading"], 1)

    def test_canonical_vector_integral_reading_edges(self):
        """Qualified links compare vector results and identify scalar foundations."""
        canonical = Path(__file__).resolve().parents[2] / "chapters" / "pl"
        if not canonical.is_dir():
            self.skipTest("canonical repository chapters not available")
        paths = (
            "measure_theory/30-miary-wektorowe-calka-bochnera-i-wlasnosc-radona-nikodyma.tex",
            "functional_analysis/15B-calki-bochnera-pettisa-dunforda-i-gelfanda-oraz-miary-wektorowe.tex",
            "measure_theory/25-rozniczkowanie-calek-i-miar.tex",
        )
        expected = (
            ("ME-30", "FA-15B", "thm:bochner-measure15b"),
            ("ME-30", "FA-15B", "thm:bochner-lebesgue-differentiation15b"),
            ("ME-30", "FA-15B", "thm:rnp-lipschitz15b"),
            ("FA-15B", "ME-30", "thm:variation-density-30"),
            ("FA-15B", "ME-30", "lem:bochner-differentiation-30"),
            ("FA-15B", "ME-30", "thm:rnp-lipschitz-equiv-30"),
            ("FA-15B", "ME-25", "thm:lebesgue-diff-25"),
            # Existing reverse link to the vector generalization.
            ("ME-25", "FA-15B", "thm:bochner-lebesgue-differentiation15b"),
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "pl"
            for relative in paths:
                dest = root / relative
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes((canonical / relative).read_bytes())
            db = Path(tmp) / "index.db"
            build_database(root, db, recursive=True)
            with closing(sqlite3.connect(db)) as con, con:
                report = graph_coverage(con)
                edges = {(e["source"], e["target"]): e for e in report["edges"]}
                for source, target, label in expected:
                    with self.subTest(source=source, target=target, label=label):
                        rows = con.execute(
                            "SELECT status,target_document,target_entity "
                            "FROM references_tex WHERE source_document=? "
                            "AND command='atlasref' AND target_label=?",
                            (source, target + "::" + label),
                        ).fetchall()
                        self.assertEqual(len(rows), 1)
                        status, owner, entity = rows[0]
                        self.assertEqual(status, "external_resolved")
                        self.assertEqual(owner, target)
                        self.assertIsNotNone(entity)
                        self.assertEqual(con.execute(
                            "SELECT entity_id FROM label_occurrences "
                            "WHERE document_id=? AND name=?", (target, label)
                        ).fetchall(), [(entity,)])
                for source, target, minimum in (
                    ("ME-30", "FA-15B", 5),
                    ("FA-15B", "ME-30", 5),
                    ("FA-15B", "ME-25", 1),
                    ("ME-25", "FA-15B", 1),
                ):
                    with self.subTest(source=source, target=target):
                        self.assertGreaterEqual(edges[(source, target)]["reading"], minimum)

    def test_canonical_measure_geometry_reading_edges(self):
        """Cross-domain links resolve to the exact geometric or measure result."""
        canonical = Path(__file__).resolve().parents[2] / "chapters" / "pl"
        if not canonical.is_dir():
            self.skipTest("canonical repository chapters not available")
        paths = (
            "differential_geometry_and_topology/01-rozmaitosci-rozniczkowe.tex",
            "differential_geometry_and_topology/10-formy-rozniczkowe-orientacja-i-kohomologia-de-rhama.tex",
            "differential_geometry_and_topology/11-tensor-metryczny-dlugosc-i-miara.tex",
            "differential_geometry_and_topology/15-twierdzenie-sarda-i-transwersalnosc.tex",
            "measure_theory/27-miary-na-rozmaitosciach-ujecie-miarowo-teoretyczne.tex",
            "measure_theory/28-wzor-na-pole-powierzchni-krotnosci-i-koobszar.tex",
            "measure_theory/31-dzety-od-geometrii-rozniczkowej-do-teorii-miary.tex",
        )
        expected = (
            ("ME-27", "DG-10", "thm:stokes-formy"),
            ("ME-27", "DG-01", "wn:immersja-lokalnie"),
            ("ME-28", "DG-11", "def:metryka-indukowana"),
            ("ME-31", "DG-01", "tw:rozniczka-odwzorowania-wspolrzedne"),
            ("DG-15", "ME-28", "thm:coarea-manifolds-28"),
            # Existing links that must survive the migration.
            ("ME-28", "DG-15", "thm:sard"),
            ("ME-31", "DG-01", "def:wiazka-wektorowa"),
            ("DG-11", "ME-27", "thm:riemann-radon-27"),
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "pl"
            for relative in paths:
                dest = root / relative
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes((canonical / relative).read_bytes())
            db = Path(tmp) / "index.db"
            build_database(root, db, recursive=True)
            with closing(sqlite3.connect(db)) as con, con:
                edges = {(e["source"], e["target"]): e
                         for e in graph_coverage(con)["edges"]}
                for source, target, label in expected:
                    with self.subTest(source=source, target=target, label=label):
                        rows = con.execute(
                            "SELECT status,target_document,target_entity "
                            "FROM references_tex WHERE source_document=? "
                            "AND command='atlasref' AND target_label=?",
                            (source, target + "::" + label),
                        ).fetchall()
                        self.assertEqual(len(rows), 1)
                        status, owner, entity = rows[0]
                        self.assertEqual(status, "external_resolved")
                        self.assertEqual(owner, target)
                        self.assertIsNotNone(entity)
                        self.assertEqual(con.execute(
                            "SELECT entity_id FROM label_occurrences "
                            "WHERE document_id=? AND name=?", (target, label)
                        ).fetchall(), [(entity,)])
                        self.assertGreaterEqual(edges[(source, target)]["reading"], 1)

    def test_canonical_qualified_algebra_reading_edges(self):
        """Keep algebra reading links independent of global label collisions."""
        repository = Path(__file__).resolve().parents[2]
        canonical = repository / "chapters" / "pl"
        if not canonical.is_dir():
            self.skipTest("canonical repository chapters not available")
        from backend.latex_parser import module_id

        expected = (
            ("ALG-02", "AA-11", "aa:ch:wielomiany"),
            ("ALG-04", "AA-12", "aa:tw:localization-universal"),
            ("ALG-04", "AA-16", "aa:ch:modules-introduction"),
            ("ALG-04", "AA-18", "aa:ch:module-tensor-product"),
            ("ALG-04", "AA-40", "aa:ch:integral-extensions"),
            ("ALG-04", "AA-38", "aa:tw:noether-normalization"),
            ("ALG-04", "AA-39", "aa:def:krull-dimension"),
            ("ALG-04", "AA-37", "aa:tw:transcendence-degree"),
            ("ALG-02", "LA-11", "cor:lin11-wielomiany"),
            ("AA-17", "LA-19", "thm:lin19-frobenius"),
            ("AA-18", "LA-10", "thm:lin10-baza"),
            ("AA-18", "ALG-04", "tw:lokalizacja-plaska"),
            ("LA-29", "ALG-02", "def:projective-space"),
        )
        needed = {item for source, target, _ in expected for item in (source, target)}
        catalog = json.loads((repository / "catalog" / "books.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "pl"
            found = set()
            for book in catalog["books"]:
                for relative in book["chapters"]:
                    source_path = repository / relative
                    chapter = module_id(source_path)
                    if chapter not in needed:
                        continue
                    self.assertNotIn(chapter, found)
                    found.add(chapter)
                    dest = root / source_path.relative_to(canonical)
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest.write_bytes(source_path.read_bytes())
            self.assertEqual(found, needed)
            db = Path(tmp) / "index.db"
            build_database(root, db, recursive=True)
            with closing(sqlite3.connect(db)) as con, con:
                edges = {(e["source"], e["target"]): e for e in graph_coverage(con)["edges"]}
                for source, target, label in expected:
                    with self.subTest(source=source, target=target, label=label):
                        rows = con.execute(
                            "SELECT status,target_document,target_entity "
                            "FROM references_tex WHERE source_document=? "
                            "AND command='atlasref' AND target_label=?",
                            (source, target + "::" + label),
                        ).fetchall()
                        self.assertEqual(len(rows), 1)
                        status, owner, entity = rows[0]
                        self.assertEqual(status, "external_resolved")
                        self.assertEqual(owner, target)
                        self.assertIsNotNone(entity)
                        self.assertEqual(con.execute(
                            "SELECT entity_id FROM label_occurrences "
                            "WHERE document_id=? AND name=?", (target, label)
                        ).fetchall(), [(entity,)])
                        self.assertGreaterEqual(edges[(source, target)]["reading"], 1)

    def test_canonical_category_topology_algebra_reading_edges(self):
        """Category examples must resolve to the concrete results they use."""
        repository = Path(__file__).resolve().parents[2]
        canonical = repository / "chapters" / "pl"
        if not canonical.is_dir():
            self.skipTest("canonical repository chapters not available")
        from backend.latex_parser import module_id

        expected = (
            ("KAT-04", "TOP-03", "uwaga:les-naturalnosc"),
            ("KAT-08", "TOP-10", "thm:solenoid-v4"),
            ("KAT-08", "TOP-10", "prz:cech-lim-niedokladnosc"),
            ("KAT-08", "TOP-29", "thm:xviii-ml"),
            ("KAT-09", "AA-16", "aa:tw:modules-free-universal"),
            ("KAT-09", "AA-18", "aa:tw:tensor-universal"),
            ("TOP-03", "KAT-04", "cat:ex:connecting-natural"),
            ("TOP-10", "KAT-08", "cat:ex:inverse-not-exact"),
        )
        needed = {doc for source, target, _ in expected for doc in (source, target)}
        catalog = json.loads((repository / "catalog" / "books.json").read_text(encoding="utf-8"))
        sources = {}
        for book in catalog["books"]:
            for relative in book["chapters"]:
                source_path = repository / relative
                chapter = module_id(source_path)
                if chapter in needed:
                    if chapter in sources:
                        self.assertEqual(sources[chapter], source_path)
                    sources[chapter] = source_path
        self.assertEqual(set(sources), needed)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "pl"
            for source_path in sources.values():
                dest = root / source_path.relative_to(canonical)
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(source_path.read_bytes())
            db = Path(tmp) / "index.db"
            build_database(root, db, recursive=True)
            with closing(sqlite3.connect(db)) as con, con:
                edges = {(e["source"], e["target"]): e for e in graph_coverage(con)["edges"]}
                for source, target, label in expected:
                    with self.subTest(source=source, target=target, label=label):
                        rows = con.execute(
                            "SELECT status,target_document,target_entity "
                            "FROM references_tex WHERE source_document=? "
                            "AND command='atlasref' AND target_label=?",
                            (source, target + "::" + label),
                        ).fetchall()
                        self.assertEqual(len(rows), 1)
                        status, owner, entity = rows[0]
                        self.assertEqual(status, "external_resolved")
                        self.assertEqual(owner, target)
                        self.assertIsNotNone(entity)
                        self.assertEqual(con.execute(
                            "SELECT entity_id FROM label_occurrences "
                            "WHERE document_id=? AND name=?", (target, label)
                        ).fetchall(), [(entity,)])
                        self.assertGreaterEqual(edges[(source, target)]["reading"], 1)
                self.assertGreaterEqual(edges[("KAT-08", "TOP-10")]["reading"], 2)
