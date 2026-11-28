"""Real Lean 4 compiler smoke for generated MetaM without Mathlib.

The separate full Mathlib build remains mandatory.
"""
from __future__ import annotations

import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

from backend import lean_introspection as inspection

SOURCE = """import Lean

def atlas_probe_inc (n : Nat) : Nat := Nat.succ n

theorem atlas_probe_or (p q : Prop) : p → p ∨ q := by
  intro hp
  exact Or.inl hp
"""
NAMES = ["atlas_probe_inc", "atlas_probe_or"]


class LeanCoreCompilerSmokeTests(unittest.TestCase):
    def test_real_lean_core_classifies_type_and_value(self):
        executable = shutil.which("lean")
        if executable is None:
            if os.environ.get("MATLIB_REQUIRE_CORE_LEAN_TEST") == "1":
                self.fail("Mandatory Lean core compiler test: executable missing")
            self.skipTest("Lean unavailable; no compiler execution")

        token = "4" * 32
        program = SOURCE + inspection.make_instrumentation(
            NAMES, token, classified=True)
        with tempfile.TemporaryDirectory(prefix="atlas-meta-core-") as directory:
            path = Path(directory) / "Probe.lean"
            path.write_text(program, encoding="utf-8")
            result = subprocess.run(
                [executable, str(path)], cwd=directory,
                capture_output=True, text=True, encoding="utf-8",
                errors="replace", check=False, timeout=120)

        self.assertEqual(
            result.returncode, 0,
            result.stdout[-3000:] + "\n" + result.stderr[-3000:])
        parsed = inspection.parse_classified_inspection(
            result.stdout + "\n" + result.stderr, token, NAMES)
        self.assertEqual(set(parsed["constants"]), set(NAMES))
        for name in NAMES:
            self.assertTrue(parsed["type_constants"][name], name)
            self.assertTrue(parsed["value_constants"][name], name)
            self.assertEqual(
                set(parsed["constants"][name]),
                set(parsed["type_constants"][name]) |
                set(parsed["value_constants"][name]))
        self.assertTrue(parsed["reference_edges"])


if __name__ == "__main__":
    unittest.main()
