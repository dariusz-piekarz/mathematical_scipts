"""Permanent regressions and fixed trusted CI examples; no arbitrary execution."""
import hashlib
import unittest
from pathlib import Path
from backend.lean_draft_generator import generate

def segments(*parts):
    source = "\n".join(text for _, text in parts)
    start, result = 0, []
    for role, text in parts:
        result.append({"role": role, "span": [start, start + len(text)]})
        start += len(text) + 1
    return source, result


# These literal examples are repository-controlled test data, not UI requests.
FIXTURES = (
    (r"\forall P:Prop, P \implies P", None),
    (r"\forall P:Prop, \forall Q:Prop, (P \land Q) \iff (Q \land P)", None),
    (r"\forall n:Nat, n + (0:Nat) = n", None),
    (r"\forall x:Int, x \le x + (1:Int)", None),
    (r"\exists x:Real, x = (0:Real)", None),
    segments(("parameter", "P:Prop"), ("parameter", "Q:Prop"),
             ("assumption", "P"), ("assumption", r"P \implies Q"), ("conclusion", "Q")),
)


def write_trusted_fixtures(directory):
    root = Path(directory)
    for i, (source, spans) in enumerate(FIXTURES, 1):
        candidate = generate(source, segments=spans, consent=True)
        if candidate["status"] != "generated":
            raise ValueError(candidate)
        (root / f"Draft{i}.lean").write_text(
            candidate["lean_code"] + "\n#print axioms atlas_draft\n", encoding="utf-8")


class LeanDraftGeneratorTests(unittest.TestCase):
    def test_fixed_fixtures_and_hashes(self):
        for source, spans in FIXTURES:
            with self.subTest(source=source):
                r = generate(source, segments=spans, consent=True)
                self.assertEqual(r["status"], "generated", r)
                self.assertEqual(r, generate(source, segments=spans, consent=True))
                self.assertEqual(r["lean_code_sha256"], hashlib.sha256(r["lean_code"].encode()).hexdigest())
                self.assertEqual(r["source_sha256"], hashlib.sha256(source.encode()).hexdigest())
                self.assertEqual(r["candidate_status"], "draft")
                self.assertEqual(r["statement_status"], "needs_review")
                self.assertEqual(r["proof_status"], "not_run")
                self.assertFalse(r["certificate"])
                self.assertFalse(r["execution_allowed"])
                self.assertFalse(r["external_transfer_allowed"])
                self.assertNotIn("sorry", r["lean_code"])
                self.assertNotIn("admit", r["lean_code"])

    def test_consent_must_be_literal_true(self):
        for consent in (False, 1, "true", None):
            r = generate(r"\top", consent=consent)
            self.assertEqual(r["status"], "blocked")
            self.assertIsNone(r["lean_code"])

    def test_all_parameters_and_assumptions_preserved_in_order(self):
        s, spans = FIXTURES[-1]
        r = generate(s, segments=spans, consent=True)
        self.assertEqual(r["signature"], "theorem atlas_draft (v1 : Prop) (v2 : Prop) (h1 : v1) (h2 : (v1 → v2)) : v2")

    def test_shadowing_and_greek_display_names(self):
        r = generate(r"\forall \alpha:Nat, \exists \alpha:Int, \alpha = (0:Int)", consent=True)
        self.assertIn("∀ (v1 : Nat), (∃ (v2 : Int), (v2 = (0 : Int)))", r["signature"])
        self.assertNotIn("α", r["lean_code"])

    def test_all_operator_templates(self):
        s = r"\forall x:Int, \forall y:Int, \neg ((-x + y) \cdot (2:Int) - y > x) \lor ((x \le y) \iff (x = y))"
        r = generate(s, consent=True)
        self.assertEqual(r["status"], "generated", r)
        self.assertIn("¬", r["signature"])
        self.assertIn("∨", r["signature"])
        self.assertIn("↔", r["signature"])
        self.assertIn("≤", r["signature"])
        self.assertIn("(v1 < ", r["signature"])
        self.assertIn("(-v1)", r["signature"])

    def test_uncovered_or_unsupported_source_never_generates(self):
        for source in ("True; #eval IO.println", r"\forall P:Prop, P \implies P \text{extra}",
                       r"\forall n:Nat, n - n = n", r"\forall n:Nat, n = (0:Int)", "P"):
            with self.subTest(source=source):
                r = generate(source, consent=True)
                self.assertNotEqual(r["status"], "generated")
                self.assertIsNone(r["lean_code"])
        s, spans = FIXTURES[-1]
        self.assertIsNone(generate(s, segments=spans[:2]+spans[-1:], consent=True)["lean_code"])

    def test_false_proposition_never_claims_proof(self):
        r = generate(r"\bot", consent=True)
        self.assertEqual(r["status"], "generated")
        self.assertTrue(r["signature"].endswith(": False"))
        self.assertEqual(r["proof_status"], "not_run")
        self.assertFalse(r["certificate"])

    def test_resource_limit_and_malformed_input(self):
        for s in (" " * 32769, None, "\ud800", "(" * 100 + r"\top" + ")" * 100):
            self.assertIsNone(generate(s, consent=True)["lean_code"])
