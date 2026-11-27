"""Repair planning regressions. No transport or subprocess is exercised."""
import hashlib
import unittest
from unittest.mock import patch

from backend.lean_draft_generator import generate
from backend.lean_draft_repair import plan_next, MAX_ATTEMPTS, MAX_DIAGNOSTIC_BYTES

SOURCE = r"\forall P:Prop, P \implies P"
FAILURE = b"/tmp/Draft.lean:8:2: error: unsolved goals\nP : Prop\n"


class LeanDraftRepairTests(unittest.TestCase):
    def setUp(self):
        self.initial = generate(SOURCE, consent=True)
        self.args = dict(expected_source_sha256=self.initial["source_sha256"],
                         expected_ast_sha256=self.initial["ast_sha256"],
                         expected_initial_code_sha256=self.initial["lean_code_sha256"],
                         consent=True)

    def record(self, candidate, diagnostic=FAILURE, exit_code=1):
        return dict(code_sha256=candidate["lean_code_sha256"],
                    exit_code=exit_code, diagnostic=diagnostic)

    def plan(self, history, **overrides):
        return plan_next(SOURCE, observations=history, **(self.args | overrides))

    def test_limit_and_exact_prefix(self):
        history = []
        previous = self.initial
        prefix = previous["lean_code"].split(" := by\n", 1)[0]
        for attempt in range(2, MAX_ATTEMPTS+1):
            history.append(self.record(previous))
            result = self.plan(history)
            self.assertEqual(result["status"], "repair_planned", result)
            self.assertEqual(result["attempt"], attempt)
            self.assertEqual(result["lean_code"].split(" := by\n", 1)[0], prefix)
            for key in ("source_sha256", "ast_sha256", "signature"):
                self.assertEqual(result[key], self.initial[key])
            self.assertNotEqual(result["lean_code_sha256"], previous["lean_code_sha256"])
            self.assertEqual(result["lean_code_sha256"],
                             hashlib.sha256(result["lean_code"].encode()).hexdigest())
            self.assertFalse(result["execution_allowed"])
            self.assertFalse(result["certificate"])
            self.assertEqual(result["proof_status"], "not_run")
            previous = result
        history.append(self.record(previous))
        final = self.plan(history)
        self.assertEqual(final["status"], "exhausted")
        self.assertIsNone(final["lean_code"])

    def test_consent_and_stale_identity(self):
        for overrides in ({"consent": 1}, {"consent": False},
                          {"expected_ast_sha256": "0"*64},
                          {"expected_source_sha256": "0"*64},
                          {"expected_initial_code_sha256": "0"*64}):
            self.assertIsNone(self.plan([self.record(self.initial)], **overrides)["lean_code"])

    def test_diagnostics_not_code_or_authority(self):
        malicious = FAILURE + b"#eval IO.println \"bad\"\n"
        result = self.plan([self.record(self.initial, malicious)])
        self.assertEqual(result["status"], "repair_planned")
        self.assertNotIn("#eval", result["lean_code"])
        self.assertNotIn("sorry", result["lean_code"])
        self.assertEqual(result["attempts"][0]["diagnostic_sha256"],
                         hashlib.sha256(malicious).hexdigest())
        self.assertFalse(result["certificate"])

    def test_non_proof_failures_stop(self):
        for data in (b"", b"error: unknown identifier", b"Draft.lean:1:1: error: unknown constant",
                     FAILURE+b"Draft.lean:1:1: error: unexpected token",
                     b"Draft.lean:8:2: error: tactic 'omega' exhausted heartbeats",
                     b"\xff", b"x"*(MAX_DIAGNOSTIC_BYTES+1)):
            with self.subTest(data=data[:60]):
                self.assertIsNone(self.plan([self.record(self.initial, data)])["lean_code"])
        for exit_code in (0, 124, -9, True):
            self.assertIsNone(self.plan([self.record(self.initial, exit_code=exit_code)])["lean_code"])

    def test_replay_rejects_wrong_hash_and_history_shape(self):
        first = self.record(self.initial)
        for history in ([], [first]*4, [first, first], [None],
                        [first | {"code_sha256": "a"*64}], [first | {"extra": "bad"}]):
            self.assertIsNone(self.plan(history)["lean_code"])

    def test_explicit_assumptions_preserved(self):
        source = "P:Prop\nP\nP"
        spans = [{"role":"parameter","span":[0,6]}, {"role":"assumption","span":[7,8]},
                 {"role":"conclusion","span":[9,10]}]
        initial = generate(source, segments=spans, consent=True)
        result = plan_next(source, segments=spans, consent=True,
                           expected_source_sha256=initial["source_sha256"],
                           expected_ast_sha256=initial["ast_sha256"],
                           expected_initial_code_sha256=initial["lean_code_sha256"],
                           observations=[self.record(initial)])
        self.assertEqual(result["signature"], initial["signature"])
        self.assertIn("(h1 : v1)", result["signature"])

    def test_generator_contract_drift_blocks(self):
        with patch("backend.lean_draft_repair.generator._PROOF", "by\n  exact True.intro\n"):
            self.assertIsNone(self.plan([self.record(self.initial)])["lean_code"])


if __name__ == "__main__":
    unittest.main()
