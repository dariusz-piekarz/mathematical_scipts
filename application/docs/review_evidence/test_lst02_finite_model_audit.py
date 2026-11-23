"""Regression tests for the stand-alone finite-model auditor (including python -O)."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import unittest

from lst02_finite_model_audit import (
    FiniteModelAuditError, require, test_unary, test_binary,
    test_negative_controls,
)

SCRIPT = Path(__file__).with_name("lst02_finite_model_audit.py")


class FiniteModelAuditTests(unittest.TestCase):
    def test_unary(self):
        self.assertEqual(test_unary()["unary_predicates"], 31)

    def test_binary(self):
        out = test_binary()
        self.assertEqual(out["binary_predicates"], 689)
        self.assertEqual(out["reverse_mixed_counterexamples"], 201)
        self.assertTrue(out["has_empty_empty_counterexample"])
        self.assertTrue(out["has_nonempty_nonempty_counterexample"])

    def test_false_claim_rejected(self):
        with self.assertRaisesRegex(FiniteModelAuditError, "deliberately incorrect"):
            require(False, "deliberately incorrect")

    def test_adversarial_negative_controls(self):
        self.assertEqual(test_negative_controls()["deliberately_false_claims_rejected"], 3)

    def test_optimized_execution_does_not_bypass_checking(self):
        for args in ([], ["-O"], ["-OO"]):
            with self.subTest(flags=args):
                result = subprocess.run(
                    [sys.executable, *args, str(SCRIPT)],
                    check=True, capture_output=True, text=True, timeout=15,
                )
                data = json.loads(result.stdout)
                self.assertEqual(data["status"], "passed")
                self.assertFalse(data["certificate"])
                self.assertEqual(data["unary"]["unary_predicates"], 31)
                self.assertEqual(data["binary"]["binary_predicates"], 689)
                self.assertEqual(data["binary"]["reverse_mixed_counterexamples"], 201)
                self.assertEqual(data["negative_controls"]["deliberately_false_claims_rejected"], 3)


if __name__ == "__main__":
    unittest.main()
