"""Regression tests for Atlas immutable-revision CI evidence.

Every forged or incomplete report must fail closed; no test run grants a
Lean/LaTeX semantic certificate.
"""
import json
from pathlib import Path
import tempfile
import unittest

from scripts.atlas_ci_report import classify_skip
from scripts.atlas_validation_select import select

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

    def test_self_declared_independent_review_never_grants_stable(self):
        reviewer = {
            "candidate_sha": SHA, "fragment": "L1.1",
            "decision": "approved", "independent": True,
            "reviewer": "Independent Reviewer",
            "critical_findings": [],
            "checks": ["TOCTOU regression independently reviewed",
                       "SHA / skip evidence and negative cases checked"],
        }
        forged = self.run_gate(review=reviewer)
        self.assertEqual(forged["status"], "stabilizing")
        self.assertEqual(forged["skeptical_review"], "documented_unverified")
        self.assertEqual(forged["problems"], [])
        self.assertIs(forged["certificate"], False)
        # Any person who can write JSON can also fill in an "independent"
        # claim; adding further fields may not authenticate that claim.
        reviewer["reviewer"] = "Fake Independent Reviewer"
        reviewer["independent"] = True
        reviewer["verification"] = "approved"
        self.assertEqual(self.run_gate(review=reviewer)["status"], "stabilizing")
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

    def test_forged_skip_category_cannot_bypass_allowlist(self):
        doc = evidence("1")
        doc["outcomes"].append({
            "id": "tests.unrelated.Fake.test_disabled", "status": "skipped",
            "reason": "Native Windows Job Objects test",
            "classification": "windows_native",
        })
        doc["executed"] = 2
        doc["outcome_count"] = 2
        doc["skipped"] = 1
        doc["unreviewed_skips"] = 0
        issues = validate_unit_report(doc, SHA, "1")
        self.assertIn("skip classification does not match reviewed allowlist", issues)
        (self.root / "atlas-unittest-1" / "report.json").write_text(
            json.dumps(doc), encoding="utf-8")
        self.assertEqual(self.run_gate()["status"], "blocked")

    def test_valid_platform_skip_and_spoofed_category_are_distinguished(self):
        doc = evidence("1")
        doc["outcomes"].append({
            "id": "tests.test_lean_windows_job.Foo.test_native",
            "status": "skipped",
            "reason": "Native Windows Job Objects test",
            "classification": "windows_native",
        })
        doc["executed"] = 2
        doc["outcome_count"] = 2
        doc["skipped"] = 1
        self.assertEqual(validate_unit_report(doc, SHA, "1"), [])
        doc["outcomes"][1]["classification"] = "pinned_lean"
        self.assertIn("skip classification does not match reviewed allowlist",
                      validate_unit_report(doc, SHA, "1"))

    def test_report_cannot_hide_missing_test_outcomes(self):
        doc = evidence("1")
        doc["executed"] = 687
        self.assertIn("executed test count does not match per-test outcomes",
                      validate_unit_report(doc, SHA, "1"))
        doc["executed"] = True
        self.assertIn("empty or malformed test suite",
                      validate_unit_report(doc, SHA, "1"))

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


class CandidateSelectionTests(unittest.TestCase):
    def test_push_reads_valid_candidate_without_moving_its_sha(self):
        with tempfile.TemporaryDirectory() as tmp:
            request = Path(tmp) / "request.json"
            request.write_text(json.dumps({
                "candidate_sha": SHA, "fragment": "L1.1",
                "request_note": "frozen candidate",
            }), encoding="utf-8")
            self.assertEqual(
                select("push", dispatch_sha="", dispatch_fragment="",
                       request_path=request), (SHA, "L1.1"))

    def test_manual_dispatch_overrides_stale_request(self):
        path = Path("does-not-exist.json")
        self.assertEqual(
            select("workflow_dispatch", dispatch_sha=OTHER,
                   dispatch_fragment="L1.2", request_path=path),
            (OTHER, "L1.2"))

    def test_unknown_fragment_and_request_fields_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            request = Path(tmp) / "request.json"
            for data in (
                {"candidate_sha": SHA, "fragment": "L1.1\\nINJECTED=1"},
                {"candidate_sha": SHA, "fragment": "L1.1", "extra": "x"},
            ):
                request.write_text(json.dumps(data), encoding="utf-8")
                with self.assertRaises(ValueError):
                    select("push", dispatch_sha="", dispatch_fragment="",
                           request_path=request)


if __name__ == "__main__":
    unittest.main()
