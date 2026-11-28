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

    def test_diagnostic_location_must_be_inside_proof(self):
        for diagnostic in (
            b"Draft.lean:1:0: error: unsolved goals",
            b"Draft.lean:6:0: error: unsolved goals",
            b"Draft.lean:99:2: error: unsolved goals",
            b"Draft.lean:8:999: error: unsolved goals",
            b"Other.lean:8:2: error: unsolved goals",
            b"Draft.lean:8:2: error: tactic 'unknown' failed",
            b"Draft.lean:8:2: error: tactic 'omega' timeout failed",
            FAILURE + b"Draft.lean:1:0: error: unsolved goals",
        ):
            with self.subTest(diagnostic=diagnostic):
                self.assertIsNone(self.plan([self.record(self.initial, diagnostic)])["lean_code"])
        prefix = self.initial["lean_code"].split(" := by\n", 1)[0] + " := "
        row = prefix.count("\n")+1
        col = len(prefix.rsplit("\n", 1)[-1])
        for offset, expected in ((-1, "blocked"), (0, "repair_planned")):
            data = f"Draft.lean:{row}:{col+offset}: error: unsolved goals".encode()
            self.assertEqual(self.plan([self.record(self.initial, data)])["status"], expected)

    def test_known_tactic_diagnostic(self):
        for message in ("tactic 'omega' failed", "tactic \x60rfl\x60 failed"):
            data = f"Draft.lean:8:2: error: {message}".encode()
            self.assertEqual(self.plan([self.record(self.initial, data)])["status"], "repair_planned")

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


def write_trusted_repair_fixtures(directory):
    """Compile fixed proof variants only; deliberately simulated diagnostics."""
    from pathlib import Path
    from backend import lean_draft_runner as runner
    initial = generate(SOURCE, consent=True)
    identity = dict(expected_source_sha256=initial["source_sha256"],
                    expected_ast_sha256=initial["ast_sha256"],
                    expected_initial_code_sha256=initial["lean_code_sha256"],
                    consent=True)
    history, previous = [], initial
    for attempt in range(2, MAX_ATTEMPTS + 1):
        history.append(dict(code_sha256=previous["lean_code_sha256"],
                            exit_code=1, diagnostic=FAILURE))
        result = plan_next(SOURCE, observations=history, **identity)
        if result["status"] != "repair_planned":
            raise ValueError(result)
        status, prepared = runner.prepare_repair(
            SOURCE, observations=history, expected_repair_code_sha256=result["lean_code_sha256"],
            **identity)
        if prepared is None or status["execution_allowed"] or prepared.attempt != attempt:
            raise ValueError(status)
        (Path(directory) / f"DraftRepair{attempt}.lean").write_bytes(prepared.input_bytes)
        previous = result


class LeanRepairAdmissionTests(unittest.TestCase):
    setUp = LeanDraftRepairTests.setUp
    record = LeanDraftRepairTests.record
    plan = LeanDraftRepairTests.plan

    def prepare(self, history, **overrides):
        from backend import lean_draft_runner as runner
        result = self.plan(history)
        args = self.args | dict(expected_repair_code_sha256=result.get("lean_code_sha256"))
        return runner.prepare_repair(SOURCE, observations=history, **(args | overrides))

    def test_prepared_repair_is_distinct_and_blocked(self):
        from backend import lean_draft_runner as runner
        history = [self.record(self.initial)]
        result = self.plan(history)
        with patch("subprocess.Popen", side_effect=AssertionError("execution forbidden")):
            status, prepared = self.prepare(history)
        self.assertIsInstance(prepared, runner.PreparedRepair)
        self.assertNotIsInstance(prepared, runner.PreparedDraft)
        self.assertEqual(prepared.input_bytes, result["lean_code"].encode() + b"\n#print axioms atlas_draft\n")
        self.assertEqual(prepared.input_sha256, hashlib.sha256(prepared.input_bytes).hexdigest())
        self.assertEqual(prepared.diagnostic_sha256, (hashlib.sha256(FAILURE).hexdigest(),))
        self.assertEqual(status["diagnostic_authenticity"], "unverified")
        self.assertFalse(status["execution_allowed"])
        self.assertFalse(status["certificate"])
        self.assertEqual(status["proof_status"], "not_run")

    def test_admission_rejects_stale_hashes_and_consent(self):
        history = [self.record(self.initial)]
        for key in ("expected_source_sha256", "expected_ast_sha256",
                    "expected_initial_code_sha256", "expected_repair_code_sha256"):
            self.assertIsNone(self.prepare(history, **{key: "0"*64})[1])
        for consent in (False, 1, None):
            self.assertIsNone(self.prepare(history, consent=consent)[1])

    def test_second_attempt_and_exhaustion(self):
        history = [self.record(self.initial)]
        history.append(self.record(self.plan(history)))
        status, prepared = self.prepare(history)
        self.assertEqual(prepared.attempt, 3)
        self.assertEqual(len(prepared.diagnostic_sha256), 2)
        digest = prepared.lean_code_sha256
        history.append(self.record(self.plan(history)))
        self.assertIsNone(self.prepare(history, expected_repair_code_sha256=digest)[1])
        history[0] = self.record(self.initial, exit_code=0)
        self.assertIsNone(self.prepare(history, expected_repair_code_sha256=digest)[1])


if __name__ == "__main__":
    unittest.main()
