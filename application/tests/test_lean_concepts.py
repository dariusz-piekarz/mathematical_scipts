"""L1.5.5a: conservative dictionary resolution and non-certification."""
import hashlib
import json
import unittest
from pathlib import Path

from backend import lean_concepts as concepts


class LeanConceptTests(unittest.TestCase):
    def test_scope_disambiguates_syntax_and_propositions(self):
        r = concepts.lookup("równoważność")
        self.assertEqual(r["status"], "ambiguous")
        self.assertIsNone(r["selected"])
        self.assertEqual({c["declaration"] for c in r["candidates"]},
                         {"Iff", "LST01.equivalent"})
        for scope, name in (("logic.prop", "Iff"), ("logic.syntax", "LST01.equivalent")):
            self.assertEqual(concepts.lookup("równoważność", scope)["selected"]["declaration"], name)

    def test_context_required_even_for_unique_match(self):
        r = concepts.lookup("odwzorowanie liniowe")
        self.assertEqual(r["status"], "needs_context")
        self.assertIsNone(r["selected"])
        self.assertEqual(r["candidates"][0]["declaration"], "LinearMap")

    def test_no_scope_fallback_or_fuzzy_resolution(self):
        for alias, scope in ((r"\equiv", "logic.prop"), (r"\iff", "logic.syntax"),
                             ("Koniunkcja", "logic.prop"), (" koniunkcja", "logic.prop"),
                             ("koniunkcje", "logic.prop"), ("⊂", "set")):
            self.assertEqual(concepts.lookup(alias, scope)["status"], "unsupported")

    def test_input_limits(self):
        for alias in (None, [], "", " ", "a"*129, "a\nb", "\ud800"):
            self.assertEqual(concepts.lookup(alias)["status"], "invalid_input")
        for scope in ([], {}, "", "unknown"):
            self.assertEqual(concepts.lookup("zbiór", scope)["status"], "invalid_input")

    def test_pins_and_deterministic_fingerprint(self):
        root = Path(__file__).resolve().parents[1] / "lean"
        self.assertEqual((root / "lean-toolchain").read_text().strip(), concepts.LEAN_TOOLCHAIN)
        self.assertIn('rev = "' + concepts.MATHLIB_REV + '"', (root / "lakefile.toml").read_text())
        raw = json.dumps(concepts._payload(), ensure_ascii=False, sort_keys=True,
                         separators=(",", ":")).encode("utf-8")
        self.assertEqual(concepts.dictionary_sha256(), hashlib.sha256(raw).hexdigest())
        self.assertEqual(concepts.lookup("zbiór", "set"), concepts.lookup("zbiór", "set"))

    def test_registry_integrity(self):
        rows = concepts._CONCEPTS
        self.assertEqual(len({c.id for c in rows}), len(rows))
        aliases = [(c.scope, a) for c in rows for a in c.aliases]
        self.assertEqual(len(set(aliases)), len(aliases))
        for c in rows:
            self.assertIn(c.scope, concepts.SCOPES)
            for a in c.aliases:
                r = concepts.lookup(a, c.scope)
                self.assertEqual(r["selected"]["id"], c.id)

    def test_results_not_certificates_or_executable_code(self):
        for alias, scope in (("zbiór", "set"), ("równoważność", None), ("?", None), (None, None)):
            r = concepts.lookup(alias, scope)
            self.assertFalse(r["certificate"])
            self.assertFalse(r["external_transfer_allowed"])
            self.assertIsNone(r["lean_code"])
            self.assertEqual(r["proof_status"], "not_run")
            self.assertEqual(r["candidate_status"], "not_generated")
            for candidate in r["candidates"]:
                self.assertEqual(candidate["mapping_status"], "needs_review")
                self.assertEqual(candidate["declaration_check"], "not_run")

    def test_returned_metadata_cannot_mutate_registry(self):
        r = concepts.lookup("zbiór", "set")
        r["selected"]["aliases"].clear()
        r["candidates"][0]["declaration"] = "forged"
        self.assertEqual(concepts.lookup("zbiór", "set")["selected"]["declaration"], "Set")
        self.assertEqual(concepts.lookup("zbiór", "set")["selected"]["aliases"], ["zbiór"])

    def test_existing_local_syntax_declarations(self):
        source = (Path(__file__).resolve().parents[1] / "lean/src/LST01_SyntaxValuations.lean").read_text(encoding="utf-8")
        self.assertIn("namespace LST01", source)
        self.assertIn("inductive Formula", source)
        self.assertIn("def equivalent (p q : Formula)", source)
        self.assertIn("def tautology (p : Formula)", source)
        self.assertEqual(concepts.lookup("formuła", "logic.syntax")["selected"]["declaration"], "LST01.Formula")
        self.assertEqual(concepts.lookup("tautologia", "logic.syntax")["selected"]["declaration"], "LST01.tautology")


if __name__ == "__main__":
    unittest.main()
