"""Conservative declared-import graph and source-integrity regressions."""
from __future__ import annotations

import hashlib
import json
import sqlite3
import tempfile
import unittest
from pathlib import Path

from fastapi import HTTPException

from backend import lean_dependencies


SOURCE = "\\begin{twierdzenie}\\label{t:x}\nLogic.\n\\end{twierdzenie}\n"


class LeanDependencyGraphTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "application" / "lean"
        (self.root / "src").mkdir(parents=True)
        (self.root / "src" / "T.lean").write_text(
            "import Mathlib\n"
            "import Mathlib.Logic.Basic -- comment\n"
            "/- import Fake -/\n"
            "theorem one (p : Prop) : p → p := by exact id\n",
            encoding="utf-8")
        self.sha = hashlib.sha256(SOURCE.encode("utf-8")).hexdigest()
        self.item = {"id": "example", "source_module": "LST-01",
                     "source_label": "t:x", "lean_file": "src/T.lean",
                     "lean_theorem": "one", "lean_theorems": ["one", "two"],
                     "source_document_sha256": self.sha,
                     "statement_status": "approved"}
        self.save_manifest()
        self.con = sqlite3.connect(":memory:")
        self.con.row_factory = sqlite3.Row
        self.addCleanup(self.con.close)
        self.con.executescript("""
            CREATE TABLE documents(id TEXT, title TEXT, sha256 TEXT, content TEXT);
            CREATE TABLE entities(id TEXT, document_id TEXT, kind TEXT, title TEXT,
                start_line INTEGER, end_line INTEGER, start_offset INTEGER, end_offset INTEGER);
            CREATE TABLE labels(name TEXT, entity_id TEXT, offset INTEGER);
        """)
        self.con.execute("INSERT INTO documents VALUES(?,?,?,?)",
                         ("LST-01", "Logic", self.sha, SOURCE))
        self.con.execute("INSERT INTO entities VALUES(?,?,?,?,?,?,?,?)",
                         ("e1", "LST-01", "theorem", "Test", 1, 3, 0, len(SOURCE)))
        self.con.execute("INSERT INTO labels VALUES(?,?,?)", ("t:x", "e1", SOURCE.index("\\label{")))
        self.con.commit()

    def save_manifest(self):
        (self.root / "manifest.json").write_text(
            json.dumps({"schema_version": 1, "items": [self.item]}),
            encoding="utf-8")

    def test_real_imports_and_manifest_correspondences(self):
        graph = lean_dependencies.graph(self.con, "example", lean_root=self.root)
        self.assertEqual(graph["formalization_status"], "ready")
        self.assertEqual(graph["statement_status"], "approved")
        self.assertEqual(graph["source_entity_id"], "e1")
        self.assertEqual(graph["declared_imports"],
                         ["Mathlib", "Mathlib.Logic.Basic"])
        self.assertEqual(len(graph["nodes"]), 6)
        self.assertEqual(len(graph["edges"]), 6)
        kinds = [e["kind"] for e in graph["edges"]]
        self.assertEqual(kinds.count("manifest_correspondence"), 2)
        self.assertEqual(kinds.count("manifest_file"), 2)
        self.assertEqual(kinds.count("declared_import"), 2)
        self.assertFalse(graph["certificate"])
        self.assertFalse(graph["proof_status_included"])
        self.assertNotIn("proof_status", graph)

    def test_lexical_import_scanner_ignores_nested_comments_and_strings(self):
        source = (
            '-- import False.One\n'
            '/- outer import False.Two /- inner import False.Three -/ -/\n'
            'def s := "import False.Four"\n'
            'import Mathlib Mathlib.Logic.Basic -- import False.Five\n'
            'import Mathlib\n'
            ' /- \nimport False.Six\n -/\n'
        )
        self.assertEqual(lean_dependencies.declared_imports(source),
                         ["Mathlib", "Mathlib.Logic.Basic"])

    def test_modified_index_revokes_current_mapping(self):
        revised = SOURCE + "% edited\n"
        self.con.execute("UPDATE documents SET content=?,sha256=?",
                         (revised, hashlib.sha256(revised.encode()).hexdigest()))
        self.con.commit()
        result = lean_dependencies.graph(self.con, "example", lean_root=self.root)
        self.assertEqual(result["formalization_status"], "stale")
        self.assertEqual(result["statement_status"], "needs_review")
        self.assertFalse(result["certificate"])

    def test_bad_id_and_missing_registration(self):
        with self.assertRaises(HTTPException) as err:
            lean_dependencies.graph(self.con, "../etc/passwd", lean_root=self.root)
        self.assertEqual(err.exception.status_code, 400)
        with self.assertRaises(HTTPException) as err:
            lean_dependencies.graph(self.con, "missing", lean_root=self.root)
        self.assertEqual(err.exception.status_code, 404)

    def test_large_module_and_bad_import_are_rejected(self):
        source_file = self.root / "src" / "T.lean"
        source_file.write_text("import Mathlib\n" + "x" * 60000, encoding="utf-8")
        with self.assertRaises(HTTPException) as err:
            lean_dependencies.graph(self.con, "example", lean_root=self.root)
        self.assertEqual(err.exception.status_code, 503)
        source_file.write_text("import Mathlib;danger\n", encoding="utf-8")
        with self.assertRaises(HTTPException) as err:
            lean_dependencies.graph(self.con, "example", lean_root=self.root)
        self.assertEqual(err.exception.status_code, 503)

    def test_excessive_import_count_is_rejected(self):
        many = "import " + " ".join("M" + str(i) for i in range(81))
        with self.assertRaises(ValueError):
            lean_dependencies.declared_imports(many)


if __name__ == "__main__":
    unittest.main()
