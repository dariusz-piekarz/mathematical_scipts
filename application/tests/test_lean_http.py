"""HTTP-level regression for Lean panel against the indexed canonical source."""
from __future__ import annotations

import os
import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient
from backend.api import app


class LeanHttpTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.context = TestClient(app)
        cls.client = cls.context.__enter__()

    @classmethod
    def tearDownClass(cls):
        cls.context.__exit__(None, None, None)

    def test_inspection_endpoint_is_opt_in_and_never_certifies(self):
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "0"}):
            result = self.client.post("/api/lean/dependencies/inspect",
                                      json={"formalization_id": "lst01-de-morgan"})
        self.assertEqual(result.status_code, 200, result.text)
        self.assertEqual(result.json()["inspection_status"], "blocked")
        self.assertFalse(result.json()["certificate"])
        self.assertEqual(result.json()["constants"], {})
        invalid = self.client.post("/api/lean/dependencies/inspect",
                                   json={"formalization_id": "../../etc"})
        self.assertEqual(invalid.status_code, 400)
        malformed = self.client.post("/api/lean/dependencies/inspect",
                                     json={"formalization_id": "x" * 101})
        self.assertEqual(malformed.status_code, 422)

    def test_dependency_graph_real_lean_source(self):
        response = self.client.get("/api/lean/dependencies",
                                   params={"formalization_id": "lst01-de-morgan"})
        self.assertEqual(response.status_code, 200, response.text)
        data = response.json()
        self.assertEqual(data["source_module"], "LST-01")
        self.assertEqual(data["source_label"], "thm:de-morgan-logic")
        self.assertEqual(data["formalization_status"], "ready")
        self.assertEqual(data["declared_imports"], ["Mathlib"])
        self.assertEqual(len([
            n for n in data["nodes"] if n["kind"] == "registered_declaration"
        ]), 2)
        self.assertTrue(data["source_entity_id"])
        self.assertTrue(any(e["kind"] == "declared_import" for e in data["edges"]))
        self.assertNotIn("proof_status", data)
        self.assertFalse(data["certificate"])

    def test_dependency_graph_rejects_unknown_id(self):
        response = self.client.get("/api/lean/dependencies",
                                   params={"formalization_id": "unlisted"})
        self.assertEqual(response.status_code, 404)
        response = self.client.get("/api/lean/dependencies",
                                   params={"formalization_id": "../../file"})
        self.assertEqual(response.status_code, 400)

    def test_catalog_lists_navigable_real_formalizations(self):
        response = self.client.get("/api/lean/catalog")
        self.assertEqual(response.status_code, 200, response.text)
        data = response.json()
        self.assertGreaterEqual(data["total"], 5)
        self.assertFalse(data["proof_status_included"])
        entry = next(i for i in data["items"]
                     if i["formalization_id"] == "lst01-de-morgan")
        self.assertEqual(entry["source_label"], "thm:de-morgan-logic")
        self.assertEqual(entry["index_status"], "ok")
        self.assertEqual(entry["formalization_status"], "ready")
        self.assertEqual(entry["statement_status"], "approved")
        self.assertTrue(entry["source_entity_id"])
        self.assertNotIn("proof_status", entry)
        self.assertFalse(entry["certificate"])

    def test_status_and_missing_mapping(self):
        response = self.client.get("/api/lean/status")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(response.json()["registered_formalizations"], 1)
        response = self.client.get("/api/lean/fragment", params={
            "module_id": "LST-01", "start_line": 1, "end_line": 1
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["formalization_status"], "missing")

    def test_real_index_theorem_mapping(self):
        response = self.client.get("/api/modules/LST-01/outline")
        self.assertEqual(response.status_code, 200)
        theorem = next(
            e for e in response.json()["entities"]
            if "thm:de-morgan-logic" in e.get("labels", [])
        )
        result = self.client.get("/api/lean/fragment", params={"entity_id": theorem["id"]})
        self.assertEqual(result.status_code, 200, result.text)
        data = result.json()
        self.assertEqual(data["formalization_id"], "lst01-de-morgan")
        self.assertIn("lst01_syntax_de_morgan_and", data["lean_code"])
        self.assertIn("inductive Formula", data["lean_code"])
        self.assertIn("def equivalent", data["lean_code"])
        self.assertEqual(data["statement_status"], "approved")
        self.assertEqual(data["formalization_status"], "ready")
        self.assertEqual(data["source_document_sha256"],
                         "9b5cbe26dee8ed5bc437cb3a0d19638eafc5d9ae178a3caa545b8bcf5842b8d0")
        self.assertEqual(data["lean_theorems"],
                         ["lst01_syntax_de_morgan_and", "lst01_syntax_de_morgan_or"])
        self.assertFalse(data["certificate"])

    def test_all_lST01_source_labels_show_syntax_and_valuation_proofs(self):
        outline = self.client.get("/api/modules/LST-01/outline")
        self.assertEqual(outline.status_code, 200)
        expected = {
            "thm:de-morgan-logic": (
                "lst01-de-morgan", ["lst01_syntax_de_morgan_and", "lst01_syntax_de_morgan_or"]),
            "thm:implication-laws": (
                "lst01-implication-laws",
                ["lst01_syntax_implication_as_disjunction",
                 "lst01_syntax_implication_contrapositive", "lst01_syntax_modus_ponens"]),
            "thm:negated-implication-xli": (
                "lst01-negated-implication", ["lst01_syntax_negated_implication"]),
        }
        entities = outline.json()["entities"]
        for label, (formal_id, theorems) in expected.items():
            with self.subTest(label=label):
                entity = next(e for e in entities if label in e.get("labels", []))
                reply = self.client.get("/api/lean/fragment",
                                        params={"entity_id": entity["id"]})
                self.assertEqual(reply.status_code, 200, reply.text)
                data = reply.json()
                self.assertEqual(data["formalization_id"], formal_id)
                self.assertEqual(data["lean_theorem"], theorems[0])
                self.assertEqual(data["lean_theorems"], theorems)
                self.assertEqual(data["formalization_status"], "ready")
                self.assertIn("inductive Formula", data["lean_code"])
                self.assertIn("def equivalent", data["lean_code"])
                self.assertIn("∀ ν : Valuation", data["lean_code"])
                self.assertEqual(data["statement_status"], "approved")
                self.assertFalse(data["certificate"])

    def test_corrupt_index_blocks_fragment_preview(self):
        from backend import lean_formalization
        from fastapi import HTTPException
        from unittest.mock import patch as mock_patch

        original = lean_formalization._find_source

        def corrupt(*args, **kwargs):
            d, content, labels, first, last, eid, linkage = original(*args, **kwargs)
            d = dict(d)
            d["sha256"] = "0" * 64
            return d, content, labels, first, last, eid, linkage

        with mock_patch.object(lean_formalization, "_find_source", side_effect=corrupt):
            response = self.client.get("/api/lean/fragment", params={
                "module_id": "LST-01", "start_line": 1, "end_line": 1
            })
        self.assertEqual(response.status_code, 409)

    def test_execution_disabled_by_default(self):
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "0"}):
            result = self.client.post("/api/lean/run", json={
                "formalization_id": "lst01-de-morgan"
            })
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json()["proof_status"], "blocked")
        self.assertFalse(result.json()["certificate"])

    def test_unknown_formalization_rejected(self):
        result = self.client.post("/api/lean/run", json={
            "formalization_id": "not-registered"
        })
        self.assertEqual(result.status_code, 404)


if __name__ == "__main__":
    unittest.main()
