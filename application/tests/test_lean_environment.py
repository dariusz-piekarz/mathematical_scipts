"""Regression checks for materialized Lake dependency and executable identity."""
from __future__ import annotations

from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from backend import lean_environment


class LeanEnvironmentTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def test_missing_packages_are_distinguishable_from_installed(self):
        empty = lean_environment.external_packages_sha256(self.root)
        packages = self.root / ".lake" / "packages"
        packages.mkdir(parents=True)
        self.assertNotEqual(empty, lean_environment.external_packages_sha256(self.root))

    def test_materialized_git_commit_change_invalidates(self):
        package = self.root / ".lake" / "packages" / "mathlib"
        (package / ".git").mkdir(parents=True)
        commit = ["a" * 40]

        def git(path, *args):
            self.assertEqual(path, package)
            if args == ("rev-parse", "--show-toplevel"):
                return str(package)
            if args == ("rev-parse", "HEAD"):
                return commit[0]
            if args == ("status", "--porcelain", "--untracked-files=normal"):
                return ""
            self.fail(str(args))

        with patch("backend.lean_environment._git", side_effect=git):
            original = lean_environment.external_packages_sha256(self.root)
            commit[0] = "b" * 40
            modified = lean_environment.external_packages_sha256(self.root)
            self.assertNotEqual(original, modified)
            self.assertEqual(modified, lean_environment.external_packages_sha256(self.root))

    def test_dirty_or_unverifiable_package_refuses_cached_proof_status(self):
        package = self.root / ".lake" / "packages" / "mathlib"
        package.mkdir(parents=True)
        with self.assertRaises(ValueError):
            lean_environment.external_packages_sha256(self.root)
        (package / ".git").mkdir()
        with patch("backend.lean_environment._git",
                   side_effect=["/other/package", "a" * 40, ""]):
            with self.assertRaises(ValueError):
                lean_environment.external_packages_sha256(self.root)

        def git(path, *args):
            if args == ("rev-parse", "--show-toplevel"):
                return str(package)
            if args == ("rev-parse", "HEAD"):
                return "a" * 40
            return " M Mathlib/Change.lean"

        with patch("backend.lean_environment._git", side_effect=git):
            with self.assertRaisesRegex(ValueError, "Modified or untracked"):
                lean_environment.external_packages_sha256(self.root)

    def test_git_timeout_fails_closed(self):
        with patch("backend.lean_environment.shutil.which", return_value="git"), \
             patch("backend.lean_environment.subprocess.run",
                   side_effect=subprocess.TimeoutExpired(cmd="git", timeout=15)):
            with self.assertRaises(ValueError):
                lean_environment._git(self.root, "status", "--porcelain")

    def test_actual_executable_bytes_change_fingerprint(self):
        program = self.root / "lean"
        program.write_bytes(b"first executable")
        other = self.root / "lake"
        other.write_bytes(b"lake executable")

        def which(name):
            return {"lean": str(program), "lake": str(other)}.get(name)

        with patch("backend.lean_environment.shutil.which", side_effect=which):
            first = lean_environment.executable_toolchain_sha256(self.root)
            program.write_bytes(b"second executable")
            second = lean_environment.executable_toolchain_sha256(self.root)
            self.assertNotEqual(first, second)

    def test_elan_resolution_takes_precedence_over_path_shims(self):
        executable = self.root / "resolved"
        executable.write_bytes(b"real lean binary")
        shim = self.root / "shim"
        shim.write_bytes(b"elan shim")

        with patch("backend.lean_environment._elan_which",
                   return_value=str(executable)), \
             patch("backend.lean_environment.shutil.which",
                   return_value=str(shim)):
            original = lean_environment.executable_toolchain_sha256(self.root)
            shim.write_bytes(b"shim modified")
            self.assertEqual(original, lean_environment.executable_toolchain_sha256(self.root))
            executable.write_bytes(b"real lean binary updated")
            self.assertNotEqual(original, lean_environment.executable_toolchain_sha256(self.root))

    def test_unresolved_path_is_recorded_not_verified(self):
        fake = self.root / "missing"
        value = lean_environment._binary_identity(str(fake))
        self.assertEqual(value["state"], "unresolved")
        self.assertNotIn("sha256", value)


if __name__ == "__main__":
    unittest.main()
