"""Regression tests for Atlas immutable-revision CI evidence.

Every forged or incomplete report must fail closed; no test run grants a
Lean/LaTeX semantic certificate.
"""
import json
from pathlib import Path
import tempfile
import unittest

from scripts.atlas_ci_report import classify_skip
from scripts.atlas_validation_gate import (
    evaluate, require_sha, validate_unit_report,
)

SHA = "a" * 40
OTHER = "b" * 40
TEST = ("tests.test_lean_environment.LeanEnvironmentTests."
        "test_real_olean_growth_during_read_fails_closed")


def evidence(pass_id, *, sha=SHA):
    outcome = {"id": TEST, "status": "passed"}
    return {
        "schema": 1, "candidate_sha": sha,
        "validation_pass": pass_id,
        "runner": "linux",
        "executed": 1, "outcome_count": 1,
        "failures": 0, "errors": 0, "unexpected_successes": 0,
        "skipped": 0, "unreviewed_skips": 0,
        "outcomes": [outcome], "success": True, "certificate": False,
    }


class NamedSkipTests(unittest.TestCase):
    def test_expected_platform_specific_skip_is_classified(self):
        self.assertEqual(
            classify_skip("tests.test_lean_windows_job.Foo.test_native",
                          "Native Windows Job Objects test"), "windows_native")

    def test_fake_reason_or_module_cannot_be_allowlisted(self):
        self.assertEqual(
            classify_skip("tests.test_other.Foo.test_native",
                          "Native Windows Job Objects test"), "unreviewed")
        self.assertEqual(
            classify_skip("tests.test_lean_windows_job.Foo.test_native",
                          "unrelated reason"), "unreviewed")

    def test_real_lean_skip_still_requires_separate_pinned_workflow(self):
        self.assertEqual(
            classify_skip("tests.test_lean_introspection_real.Foo.real",
                          "Lake/Mathlib unavailable; no real Lean execution"),
            "pinned_lean")


class GateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for pass_id in ("1", "2", "3"):
            d = self.root / ("atlas-unittest-" + pass_id)
            d.mkdir()
            (d / "report.json").write_text(json.dumps(evidence(pass_id)),
                                           encoding="utf-8")

    def run_gate(self, **overrides):
        args = {
            "application": "success", "native": "success",
            "lean": "success", "skeptic": "success",
        }
        args.update(overrides)
        return evaluate(SHA, "L1.1", self.root, **args)

    def test_reject_short_sha(self):
        with self.assertRaises(ValueError):
            require_sha(SHA[:8])

    def test_three_clean_passes_without_independent_review_are_not_stable(self):
        result = self.run_gate()
        self.assertEqual(result["status"], "stabilizing")
        self.assertEqual(len(result["passes"]), 3)
        self.assertIs(result["certificate"], False)

    def test_matching_documented_review_is_required_to_be_stable(self):
        reviewer = {
            "candidate_sha": SHA, "fragment": "L1.1",
            "decision": "approved", "independent": True,
            "reviewer": "Independent Reviewer",
            "critical_findings": [],
            "checks": ["TOCTOU regression independently reviewed",
                       "SHA / skip evidence and negative cases checked"],
        }
        self.assertEqual(self.run_gate(review=reviewer)["status"], "stable")
        reviewer["candidate_sha"] = OTHER
        self.assertEqual(self.run_gate(review=reviewer)["status"], "blocked")

    def test_missing_or_swapped_pass_is_blocked(self):
        (self.root / "atlas-unittest-2" / "report.json").unlink()
        self.assertEqual(self.run_gate()["status"], "blocked")
        (self.root / "atlas-unittest-2" / "report.json").write_text(
            json.dumps(evidence("2", sha=OTHER)), encoding="utf-8")
        self.assertEqual(self.run_gate()["status"], "blocked")

    def test_unknown_skips_block_gate(self):
        doc = evidence("1")
        doc["outcomes"].append({
            "id": "tests.other.Test.unknown", "status": "skipped",
            "classification": "unreviewed", "reason": "unexpected",
        })
        doc["skipped"] = 1
        doc["outcome_count"] = 2
        doc["unreviewed_skips"] = 1
        (self.root / "atlas-unittest-1" / "report.json").write_text(
            json.dumps(doc), encoding="utf-8")
        self.assertEqual(self.run_gate()["status"], "blocked")

    def test_missing_mandatory_real_file_regression_is_blocked(self):
        doc = evidence("3")
        doc["outcomes"][0]["id"] = "tests.other.Test.incomplete"
        (self.root / "atlas-unittest-3" / "report.json").write_text(
            json.dumps(doc), encoding="utf-8")
        self.assertEqual(self.run_gate()["status"], "blocked")

    def test_unverified_lean_and_skeptic_are_blocked(self):
        self.assertEqual(self.run_gate(lean="skipped")["status"], "blocked")
        self.assertEqual(self.run_gate(skeptic="failure")["status"], "blocked")
        self.assertEqual(self.run_gate(native="cancelled")["status"], "blocked")

    def test_per_test_duplicate_identity_is_rejected(self):
        doc = evidence("1")
        doc["outcomes"].append(dict(doc["outcomes"][0]))
        doc["outcome_count"] = 2
        self.assertIn("duplicate test identity",
                      validate_unit_report(doc, SHA, "1"))


if __name__ == "__main__":
    unittest.main()
