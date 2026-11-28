"""Regression tests against real indexed LST/LA definitions and altered index."""
import hashlib
from pathlib import Path
import shutil
import tempfile
import unittest

from backend import latex_parser, lean_concept_context as context


class LeanConceptContextTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.tmp.cleanup)
        base = Path(cls.tmp.name)
        source = base / "chapters/pl"
        repo = Path(__file__).resolve().parents[2]
        for path in {a["path"] for a in context._ANCHORS}:
            target = base / "chapters" / path
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(repo / "chapters" / path, target)
        cls.db = base / "index.db"
        latex_parser.build_database(source, cls.db, recursive=True)

    def setUp(self):
        self.con = latex_parser.connect(self.db)
        self.addCleanup(self.con.close)
        self.addCleanup(self.con.rollback)

    def call(self, anchor, digest=None):
        return context.resolve_definition(
            self.con, anchor["module"], anchor["label"],
            digest if digest is not None else hashlib.sha256(
                anchor["source"].encode("utf-8")).hexdigest())

    def test_real_indexed_definitions_and_trace(self):
        for anchor in context._ANCHORS:
            with self.subTest(label=anchor["label"]):
                result = self.call(anchor)
                self.assertEqual(result["status"], "context_candidates", result)
                self.assertEqual([c["id"] for c in result["candidates"]],
                                 [pair[1] for pair in anchor["aliases"]])
                self.assertEqual(len(result["trace"]), len(anchor["aliases"]))
                self.assertFalse(result["certificate"])
                self.assertIsNone(result["lean_code"])
                self.assertTrue(all(c["mapping_status"] == "needs_review"
                                    for c in result["candidates"]))

    def test_stale_source_and_unknown_context(self):
        anchor = context._ANCHORS[0]
        self.assertEqual(self.call(anchor, "0"*64)["status"], "stale_source")
        self.assertEqual(context.resolve_definition(
            self.con, "LST-01", "def:unregistered", "0"*64)["status"], "unsupported")

    def test_wrong_index_owner_or_digest_is_refused(self):
        anchor = context._ANCHORS[0]
        self.con.execute("UPDATE documents SET sha256=? WHERE id=?",
                         ("0"*64, anchor["module"]))
        self.assertEqual(self.call(anchor)["status"], "invalid_binding")
        self.con.rollback()
        self.con.execute("UPDATE entities SET kind='theorem' WHERE id=?",
                         ("label:"+anchor["label"],))
        self.assertEqual(self.call(anchor)["status"], "invalid_binding")

    def test_duplicate_occurrence_is_refused(self):
        anchor = context._ANCHORS[0]
        self.con.execute(
            "INSERT INTO label_occurrences(occurrence_id,name,document_id,entity_id,line,offset) "
            "SELECT 'synthetic-duplicate',name,document_id,entity_id,line+1,offset+1 "
            "FROM label_occurrences WHERE name=?", (anchor["label"],))
        self.assertEqual(self.call(anchor)["status"], "ambiguous_label")

    def test_modified_definition_even_with_updated_digest_is_refused(self):
        anchor = context._ANCHORS[0]
        original = self.con.execute("SELECT content FROM documents WHERE id=?",
                                    (anchor["module"],)).fetchone()[0]
        modified = anchor["source"].replace("formuł", "FORMUŁ", 1)
        self.assertNotEqual(modified, anchor["source"])
        self.assertEqual(len(modified), len(anchor["source"]))
        changed = original.replace(anchor["source"], modified, 1)
        self.assertNotEqual(original, changed)
        self.con.execute("UPDATE documents SET content=?,sha256=? WHERE id=?",
                         (changed, hashlib.sha256(changed.encode()).hexdigest(), anchor["module"]))
        self.assertEqual(self.call(anchor, hashlib.sha256(modified.encode()).hexdigest())["status"],
                         "stale_source")
