"""Real LST theorem context and negative provenance checks."""
import hashlib
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

from backend import latex_parser, lean_formalization, lean_theorem_context as context


class LeanTheoremContextTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.tmp.cleanup)
        base = Path(cls.tmp.name)
        source = base / "chapters/pl/logic_and_set_theory"
        source.mkdir(parents=True)
        name = "01-zdania-i-spojniki-logiczne.tex"
        shutil.copyfile(Path(__file__).resolve().parents[2] / "chapters/pl/logic_and_set_theory" / name, source / name)
        cls.db = base / "index.db"
        latex_parser.build_database(source.parent, cls.db, recursive=True)

    def setUp(self):
        self.con = latex_parser.connect(self.db)
        self.addCleanup(self.con.close)

    def call(self, label="thm:equiv-test", digest=None, consent=True):
        eid = "label:" + label
        row = self.con.execute(
            "SELECT d.content,e.start_offset,e.end_offset FROM documents d "
            "JOIN entities e ON d.id=e.document_id WHERE e.id=?", (eid,)).fetchone()
        if digest is None:
            digest = hashlib.sha256(row[0][row[1]:row[2]].encode("utf-8")).hexdigest()
        return context.resolve_theorem(self.con, entity_id=eid,
                                       expected_source_sha256=digest, consent=consent)

    def test_real_registered_theorem_context(self):
        for (_, label), (mapping_id, _, concepts) in context._RULES.items():
            with self.subTest(label=label):
                r = self.call(label)
                self.assertEqual(r["status"], "context_candidates", r)
                self.assertEqual(r["registered_mapping"]["id"], mapping_id)
                self.assertEqual([c["id"] for c in r["candidates"]], list(concepts))
                self.assertTrue(all(c["mapping_status"] == "needs_review" for c in r["candidates"]))
                self.assertEqual(r["statement_status"], "unreviewed")
                self.assertEqual(r["proof_status"], "not_run")
                self.assertFalse(r["certificate"])
                self.assertIsNone(r["lean_code"])

    def test_missing_consent_stale_digest_and_unsupported_theorem(self):
        self.assertEqual(self.call(consent=False)["status"], "source_or_registry_rejected")
        self.assertEqual(self.call(digest="0"*64)["status"], "source_or_registry_rejected")
        self.assertEqual(self.call("thm:implication-laws")["status"], "unsupported")

    def test_registry_approval_cannot_bypass_source_pin(self):
        items = lean_formalization._registry()
        altered = [dict(x) for x in items]
        next(x for x in altered if x["id"] == "lst01-equivalence-test")["source_document_sha256"] = "0"*64
        with patch.object(lean_formalization, "_registry", return_value=altered):
            r = self.call()
            self.assertEqual(r["status"], "stale_mapping")
            self.assertIsNone(r["registered_mapping"])
            self.assertEqual(r["candidates"], [])

    def test_unreviewed_and_duplicate_mappings_are_refused(self):
        items = lean_formalization._registry()
        altered = [dict(x) for x in items]
        next(x for x in altered if x["id"] == "lst01-equivalence-test")["statement_status"] = "needs_review"
        with patch.object(lean_formalization, "_registry", return_value=altered):
            self.assertEqual(self.call()["status"], "mapping_needs_review")
        duplicate = next(x for x in items if x["id"] == "lst01-equivalence-test")
        with patch.object(lean_formalization, "_registry", return_value=items+[duplicate]):
            self.assertEqual(self.call()["status"], "invalid_registry")

    def test_definition_collision_blocks_entire_context(self):
        self.con.execute(
            "INSERT INTO label_occurrences(occurrence_id,name,document_id,entity_id,line,offset) "
            "SELECT 'duplicate-context',name,document_id,entity_id,line+1,offset+1 "
            "FROM label_occurrences WHERE name='def:tautology'")
        r = self.call()
        self.assertEqual(r["status"], "invalid_context")
        self.assertEqual(r["context_status"], "ambiguous_label")
        self.assertEqual(r["candidates"], [])
        self.assertIsNone(r["registered_mapping"])
        self.con.rollback()
