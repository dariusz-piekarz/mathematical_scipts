"""Optional actual Lean 4 smoke test for generated MetaM instrumentation.

Run inside application/ after Mathlib is installed:
  python -m unittest tests.test_lean_introspection_real -v

Skipping when the toolchain/cache is absent is NOT a successful Lean test.
"""
from __future__ import annotations

from pathlib import Path
import os
import secrets
import shutil
import subprocess
import tempfile
import unittest

from backend import lean_introspection as inspect

LEAN_ROOT = Path(__file__).resolve().parents[1] / "lean"


class LeanIntrospectionRealSmokeTests(unittest.TestCase):
    def test_real_lean_426_reports_constants(self):
        if not shutil.which("lake") or not (
                LEAN_ROOT / ".lake" / "packages" / "mathlib").is_dir():
            if os.environ.get("MATLIB_REQUIRE_REAL_LEAN_TEST") == "1":
                self.fail("Mandatory real Lean smoke test: Lake or Mathlib unavailable")
            self.skipTest("Lake/Mathlib unavailable; no real Lean execution")
        source = (LEAN_ROOT / "src" / "LST01_DeMorgan.lean").read_bytes()
        theorem = "lst01_de_morgan_and"
        token = secrets.token_hex(16)
        instrumented = (source + b"\n" +
                        inspect.make_instrumentation([theorem], token).encode("utf-8"))
        with tempfile.TemporaryDirectory(prefix="atlas-lean-inspection-") as directory:
            target = Path(directory) / "Inspect.lean"
            target.write_bytes(instrumented)
            result = subprocess.run(
                ["lake", "env", "lean", str(target)],
                cwd=LEAN_ROOT, capture_output=True, text=True,
                encoding="utf-8", errors="replace",
                check=False, timeout=180,
            )
        self.assertEqual(result.returncode, 0, result.stdout[-1800:] +
                         "\n" + result.stderr[-1800:])
        output = result.stdout + "\n" + result.stderr
        constants = inspect.parse_inspection(output, token, [theorem])
        self.assertIn(theorem, constants)
        self.assertGreater(len(constants[theorem]), 0)


if __name__ == "__main__":
    unittest.main()
