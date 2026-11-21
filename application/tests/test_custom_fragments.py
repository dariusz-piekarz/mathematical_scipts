"""Regression tests for user-authored scripts assembled from exact source lines."""
import io
import sqlite3
import unittest
import zipfile

from fastapi.testclient import TestClient
from backend.api import ROOT, app
from backend.generator import GenerationError, project_files


class CustomScriptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.con = sqlite3.connect(ROOT / "data" / "biblioteka.db")
        cls.con.row_factory = sqlite3.Row

    @classmethod
    def tearDownClass(cls):
        cls.con.close()

    def build(self, items, **kwargs):
        return project_files(self.con, [], [], "Mój skrypt", items=items, **kwargs)

    def test_exact_lines_and_source_provenance(self):
        original = self.con.execute(
            "SELECT content,sha256 FROM documents WHERE id='ALG-09'").fetchone()
        lines = original["content"].splitlines(keepends=True)
        # Choose lines with no reference commands: external refs are intentionally
        # rewritten by the generator and therefore are not byte-identical.
        import re
        start = next(i for i in range(len(lines) - 2)
                     if all(not re.search(
                         r"\\(?:ref|eqref|pageref|autoref|nameref|cref|Cref|vref|Vref)\s*\{",
                         lines[j]) for j in range(i, i + 3)))
        first, last = start + 1, start + 3
        files, manifest = self.build([
            {"kind": "lines", "module": "ALG-09", "start_line": first, "end_line": last},
        ])
        excerpt = "".join(lines[start:start+3])
        generated = files["rozdzialy/ALG-09-001.tex"].decode("utf-8")
        self.assertTrue(generated.endswith(excerpt))
        self.assertEqual(manifest["source_sha256"]["ALG-09"], original["sha256"])
        self.assertEqual(manifest["ordered_items"][0]["start_line"], first)
        self.assertEqual(manifest["ordered_items"][0]["end_line"], last)
        self.assertIn(r"\input{rozdzialy/ALG-09-001.tex}", files["main.tex"].decode())

    def test_interleaved_excerpts_keep_exact_user_order(self):
        files, manifest = self.build([
            {"kind": "lines", "module": "ALG-09", "start_line": 1, "end_line": 2},
            {"kind": "lines", "module": "BT-00", "start_line": 1, "end_line": 2},
            {"kind": "lines", "module": "ALG-09", "start_line": 4, "end_line": 5},
        ])
        expected = ["rozdzialy/ALG-09-001.tex", "rozdzialy/BT-00-001.tex",
                    "rozdzialy/ALG-09-002.tex"]
        self.assertEqual([x["output_file"] for x in manifest["ordered_items"]], expected)
        main = files["main.tex"].decode()
        self.assertLess(main.index(expected[0]), main.index(expected[1]))
        self.assertLess(main.index(expected[1]), main.index(expected[2]))
        for name in expected:
            self.assertIn(name, files)
        self.assertEqual(len(manifest["fragments"]["ALG-09"]), 2)

    def test_contained_duplicates_removed_and_partly_overlapping_rejected(self):
        files, report = self.build([
            {"kind": "lines", "module": "ALG-09", "start_line": 1, "end_line": 12},
            {"kind": "lines", "module": "ALG-09", "start_line": 3, "end_line": 5},
            {"kind": "lines", "module": "ALG-09", "start_line": 1, "end_line": 12},
        ])
        self.assertEqual(len(report["ordered_items"]), 1)
        self.assertEqual(len([x for x in files if x.startswith("rozdzialy/")]), 1)
        with self.assertRaisesRegex(GenerationError, "Częściowo zachodzące"):
            self.build([
                {"kind": "lines", "module": "ALG-09", "start_line": 2, "end_line": 7},
                {"kind": "lines", "module": "ALG-09", "start_line": 5, "end_line": 9},
            ])

    def test_whole_module_wins_over_excerpts(self):
        files, report = self.build([
            {"kind": "lines", "module": "BT-00", "start_line": 1, "end_line": 2},
            {"kind": "module", "id": "BT-00"},
            {"kind": "lines", "module": "BT-00", "start_line": 3, "end_line": 4},
        ])
        self.assertEqual(report["whole_modules"], ["BT-00"])
        self.assertEqual([x["kind"] for x in report["ordered_items"]], ["module"])
        raw = self.con.execute("SELECT content FROM documents WHERE id='BT-00'").fetchone()[0]
        self.assertIn(raw.splitlines()[0], files["rozdzialy/BT-00.tex"].decode())

    def test_entity_and_lines_can_be_combined(self):
        files, manifest = self.build([
            {"kind": "entity", "id": "ALG-09/proof/0004"},
            {"kind": "lines", "module": "BT-00", "start_line": 1, "end_line": 2},
        ])
        self.assertEqual([x["kind"] for x in manifest["ordered_items"]], ["entity", "lines"])
        self.assertIn("ALG-09/proof/0004", manifest["fragments"]["ALG-09"])
        self.assertIn("rozdzialy/ALG-09-001.tex", files)

    def test_reject_invalid_or_mixed_selection(self):
        bad = [
            {"kind": "lines", "module": "ALG-09", "start_line": 0, "end_line": 3},
            {"kind": "lines", "module": "ALG-09", "start_line": 5, "end_line": 4},
            {"kind": "lines", "module": "ALG-09", "start_line": 1, "end_line": 100000000},
            {"kind": "lines", "module": "../secret", "start_line": 1, "end_line": 2},
            {"kind": "lines", "module": "ALG-09", "start_line": True, "end_line": 2},
            {"kind": "entity", "id": "not-here"},
            {"kind": "invalid", "id": "ALG-09"},
        ]
        for item in bad:
            with self.subTest(item=item), self.assertRaises(GenerationError):
                self.build([item])
        with self.assertRaises(GenerationError):
            project_files(self.con, ["BT-00"], [], "Bad", items=[{"kind": "module", "id": "BT-00"}])


    def test_every_indexed_subject_has_generator_preamble(self):
        from backend.generator import PROJECT_TEMPLATE_KEYS
        prefixes = {r[0].split("-", 1)[0] for r in self.con.execute("SELECT id FROM documents")}
        self.assertTrue({"LA", "LST", "FA", "DG", "PDE", "ME"} <= prefixes)
        for prefix in prefixes:
            with self.subTest(prefix=prefix):
                self.assertIn(prefix, PROJECT_TEMPLATE_KEYS)
                name = PROJECT_TEMPLATE_KEYS[prefix]
                self.assertTrue((ROOT / "config" / "preambles" / f"{name}.tex").is_file())

    def test_new_subject_excerpts_and_lettered_chapter(self):
        for prefix in ("LA", "LST", "FA", "DG", "PDE", "ME"):
            row = self.con.execute(
                "SELECT id FROM documents WHERE id LIKE ? ORDER BY id LIMIT 1",
                (prefix + "-%",)
            ).fetchone()
            self.assertIsNotNone(row, prefix)
            with self.subTest(module=row[0]):
                files, manifest = self.build([
                    {"kind": "lines", "module": row[0], "start_line": 1, "end_line": 1}
                ])
                self.assertEqual(manifest["modules"], [row[0]])
                self.assertIn(f"rozdzialy/{row[0]}-001.tex", files)
        files, manifest = self.build([
            {"kind": "lines", "module": "FA-15A", "start_line": 1, "end_line": 1}
        ])
        self.assertEqual(manifest["modules"], ["FA-15A"])
        self.assertIn("rozdzialy/FA-15A-001.tex", files)

    def test_explicit_empty_items_and_legacy_selection(self):
        with self.assertRaisesRegex(GenerationError, "Wybierz od 1"):
            self.build([])
        with self.assertRaisesRegex(GenerationError, "Nie łącz"):
            project_files(self.con, ["BT-00"], [], "Zestaw", items=[])
        files, manifest = project_files(self.con, ["BT-00"], [], "Dawny klient")
        self.assertEqual(manifest["modules"], ["BT-00"])
        self.assertIn("rozdzialy/BT-00.tex", files)

    def test_http_manifest_zip_and_draft_accept_custom_items(self):
        request = {"title": "Wybór fragmentu", "items": [
            {"kind": "lines", "module": "BT-00", "start_line": 1, "end_line": 2},
        ]}
        with TestClient(app) as client:
            response = client.post("/api/generate/manifest", json=request)
            self.assertEqual(response.status_code, 200, response.text)
            self.assertEqual(response.json()["ordered_items"][0]["kind"], "lines")
            archive = client.post("/api/generate", json=request)
            self.assertEqual(archive.status_code, 200, archive.text)
            with zipfile.ZipFile(io.BytesIO(archive.content)) as z:
                self.assertIsNone(z.testzip())
                self.assertIn("rozdzialy/BT-00-001.tex", z.namelist())
                self.assertIn("manifest.json", z.namelist())
            invalid = client.post("/api/generate", json={
                **request, "modules": ["BT-00"]})
            self.assertEqual(invalid.status_code, 422)
            legacy = client.post("/api/generate/manifest", json={"modules": ["BT-00"]})
            self.assertEqual(legacy.status_code, 200, legacy.text)
            empty = client.post("/api/generate/manifest", json={"items": [], "modules": ["BT-00"]})
            self.assertEqual(empty.status_code, 422)


if __name__ == "__main__":
    unittest.main()
