"""Selection and fail-closed regression coverage."""
import hashlib
import unittest
from unittest.mock import patch
from backend import lean_generator_adapter as adapter
from backend import lean_draft_generator as rules


def digest(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


class LeanGeneratorAdapterTests(unittest.TestCase):
    def assert_blocked(self, r, error):
        self.assertEqual(r["status"], "blocked")
        self.assertEqual(r["error"], error)
        self.assertIsNone(r["lean_code"])
        self.assertEqual(r["proof_status"], "not_run")
        for key in ("execution_allowed", "certificate", "model_called",
                    "automatic_fallback", "external_transfer_allowed"):
            self.assertIs(r[key], False)
        self.assertEqual(r["external_cost_minor_units"], 0)

    def test_rules_preserve_existing_output(self):
        for s in (r"\top", r"\bot", r"\forall P:Prop, P \implies P",
                  r"\forall n:Nat, n + (0:Nat) = n"):
            r = adapter.generate(s, generator="rules", consent=True,
                                 expected_source_sha256=digest(s))
            original = rules.generate(s, consent=True)
            self.assertEqual(r["status"], "generated")
            for key, value in original.items():
                self.assertEqual(r[key], value, key)
            self.assertIs(r["model_called"], False)

    def test_modes_never_fall_back(self):
        with patch.object(rules, "generate", side_effect=AssertionError("fallback")):
            for name, error in (("local_model", "local_model_not_integrated"),
                                ("external_provider", "external_provider_disabled"),
                                ("unknown", "unknown_generator"), ([], "unknown_generator")):
                self.assert_blocked(adapter.generate(
                    r"\top", generator=name, consent=True,
                    expected_source_sha256=digest(r"\top")), error)

    def test_consent_and_stale_hash_rejected(self):
        with patch.object(rules, "generate", side_effect=AssertionError("dispatch")):
            for consent in (False, 1, "true", None):
                self.assert_blocked(adapter.generate(
                    r"\top", generator="rules", consent=consent,
                    expected_source_sha256=digest(r"\top")), "explicit_consent_required")
            for name in ("rules", "local_model", "external_provider"):
                self.assert_blocked(adapter.generate(
                    r"\top", generator=name, consent=True,
                    expected_source_sha256=digest(r"\bot")), "stale_source")

    def test_bad_source_rejected(self):
        for source in (None, "", "\ud800", "ą" * 17000, " " * 32769):
            self.assert_blocked(adapter.generate(source, generator="rules", consent=True,
                                expected_source_sha256=""), "invalid_source")

    def test_unsupported_is_not_generated(self):
        s = r"\top \text{extra}"
        r = adapter.generate(s, generator="rules", consent=True,
                             expected_source_sha256=digest(s))
        self.assertNotEqual(r["status"], "generated")
        self.assertIsNone(r["lean_code"])

    def test_tampered_identity_is_blocked(self):
        s = r"\top"
        original = rules.generate(s, consent=True)
        for key in ("source_sha256", "lean_code_sha256"):
            with patch.object(rules, "generate", return_value={**original, key: "0" * 64}):
                self.assert_blocked(adapter.generate(
                    s, generator="rules", consent=True,
                    expected_source_sha256=digest(s)), "candidate_identity_mismatch")

    def test_capabilities_fresh_and_closed(self):
        a = adapter.capabilities()
        a["generators"]["local_model"]["available"] = True
        b = adapter.capabilities()
        self.assertIs(b["generators"]["rules"]["available"], True)
        self.assertIs(b["generators"]["local_model"]["available"], False)
        self.assertIs(b["generators"]["external_provider"]["available"], False)
        self.assertIs(b["automatic_fallback"], False)

    def test_malformed_and_contradictory_results_fail_closed(self):
        s = r"\top"
        original = rules.generate(s, consent=True)
        for result in (None, [], {}, {**original, "lean_code": None},
                       {**original, "lean_code": "\ud800"},
                       {**original, "lean_code": "a" * 65537},
                       {**original, "certificate": True},
                       {**original, "execution_allowed": True},
                       {**original, "offline_ready": True},
                       {**original, "status": "unsupported"},
                       {**original, "external_cost_minor_units": False}):
            with self.subTest(result_type=type(result)):
                with patch.object(rules, "generate", return_value=result):
                    self.assert_blocked(adapter.generate(
                        s, generator="rules", consent=True,
                        expected_source_sha256=digest(s)), "invalid_generator_result")

    def test_rehashed_wrong_statement_and_ast_rejected(self):
        s = r"\top"
        original = rules.generate(s, consent=True)
        wrong = original["lean_code"].replace(": True :=", ": False :=")
        self.assertNotEqual(wrong, original["lean_code"])
        for result in ({**original, "ast_sha256": "0" * 64},
                       {**original, "lean_code": wrong, "lean_code_sha256": digest(wrong)},
                       {**original, "trace": {}},
                       {**original, "signature": "theorem atlas_draft : False"}):
            with patch.object(rules, "generate", return_value=result):
                self.assert_blocked(adapter.generate(
                    s, generator="rules", consent=True,
                    expected_source_sha256=digest(s)), "candidate_identity_mismatch")

    def test_rehashed_altered_proof_and_trailing_command_rejected(self):
        s = r"\top"
        original = rules.generate(s, consent=True)
        for changed in (
            original["lean_code"].replace(rules._PROOF, "by\n  exact True.intro\n"),
            original["lean_code"] + "\n#check True\n",
            original["lean_code"] + "\n",
        ):
            self.assertNotEqual(changed, original["lean_code"])
            with patch.object(rules, "generate", return_value={
                    **original, "lean_code": changed,
                    "lean_code_sha256": digest(changed)}):
                self.assert_blocked(adapter.generate(
                    s, generator="rules", consent=True,
                    expected_source_sha256=digest(s)), "candidate_identity_mismatch")

    def test_failure_diagnostics_bound_to_parser(self):
        s = r"\top \text{extra}"
        original = rules.generate(s, consent=True)
        self.assertIn("diagnostic", original)
        actual = adapter.generate(s, generator="rules", consent=True,
                                  expected_source_sha256=digest(s))
        self.assertEqual(actual["diagnostic"], original["diagnostic"])
        self.assertEqual(actual["error"], original["error"])
        for changed in (
            {**original, "diagnostic": []},
            {**original, "diagnostic": {"span": [0, 99999]}},
            {**original, "diagnostic": {**original["diagnostic"], "extra": "untrusted"}},
            {**original, "error": "invented_error"},
            {k: v for k, v in original.items() if k != "diagnostic"},
        ):
            with patch.object(rules, "generate", return_value=changed):
                self.assert_blocked(adapter.generate(
                    s, generator="rules", consent=True,
                    expected_source_sha256=digest(s)), "candidate_identity_mismatch")
        with patch.object(rules, "generate", return_value=original):
            self.assert_blocked(adapter.generate(
                r"\top", generator="rules", consent=True,
                expected_source_sha256=digest(r"\top")), "candidate_identity_mismatch")

    def test_code_limit_failure_is_preserved(self):
        s = r"\top"
        with patch.object(rules, "MAX_CODE_BYTES", 1):
            result = adapter.generate(s, generator="rules", consent=True,
                                      expected_source_sha256=digest(s))
        self.assertEqual(result["status"], "invalid_input")
        self.assertEqual(result["error"], "code_byte_limit")
        self.assertIsNone(result["lean_code"])

    def test_segment_roles_and_uncovered_assumptions(self):
        s = "P:Prop\nP\nP"
        spans = [{"role": "parameter", "span": [0, 6]},
                 {"role": "assumption", "span": [7, 8]},
                 {"role": "conclusion", "span": [9, 10]}]
        result = adapter.generate(s, generator="rules", consent=True, segments=spans,
                                  expected_source_sha256=digest(s))
        self.assertEqual(result["status"], "generated", result)
        self.assertEqual(result["signature"],
                         "theorem atlas_draft (v1 : Prop) (h1 : v1) : v1")
        omitted = [spans[0], spans[2]]
        actual = adapter.generate(s, generator="rules", consent=True, segments=omitted,
                                  expected_source_sha256=digest(s))
        self.assertEqual(actual["error"], "uncovered_source")
        self.assertIsNone(actual["lean_code"])
        original = rules.generate(s, segments=spans, consent=True)
        with patch.object(rules, "generate", return_value=original):
            self.assert_blocked(adapter.generate(
                s, generator="rules", consent=True, segments=omitted,
                expected_source_sha256=digest(s)), "candidate_identity_mismatch")

    def test_numeric_trace_types_are_exact(self):
        import copy
        s = r"\top"
        original = rules.generate(s, consent=True)
        for replacement in (False, 0.0):
            changed = copy.deepcopy(original)
            changed["trace"]["segments"][0]["span"][0] = replacement
            self.assertEqual(changed["trace"], original["trace"])
            with patch.object(rules, "generate", return_value=changed):
                self.assert_blocked(adapter.generate(
                    s, generator="rules", consent=True,
                    expected_source_sha256=digest(s)), "candidate_identity_mismatch")

    def test_numeric_diagnostic_types_are_exact(self):
        import copy
        s = r"\text{extra}"
        original = rules.generate(s, consent=True)
        changed = copy.deepcopy(original)
        self.assertEqual(changed["diagnostic"]["span"][0], 0)
        changed["diagnostic"]["span"][0] = False
        self.assertEqual(changed["diagnostic"], original["diagnostic"])
        with patch.object(rules, "generate", return_value=changed):
            self.assert_blocked(adapter.generate(
                s, generator="rules", consent=True,
                expected_source_sha256=digest(s)), "candidate_identity_mismatch")
