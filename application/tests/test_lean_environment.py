"""Regression checks for materialized Lake dependency and executable identity."""
from __future__ import annotations

from pathlib import Path
import hashlib
import os
import shutil
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

    @unittest.skipUnless(shutil.which("git"), "Git not installed")
    def test_real_git_checkout_dirty_state_and_new_commit(self):
        # Exercise real installed checkout metadata, not only mocked Git output.
        package = self.root / ".lake" / "packages" / "mathlib"
        package.mkdir(parents=True)
        git = shutil.which("git")

        def command(*args):
            result = subprocess.run(
                [git, "-C", str(package), *args],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                text=True, check=False, timeout=10)
            self.assertEqual(result.returncode, 0, result.stderr)

        command("init", "--quiet")
        command("config", "core.autocrlf", "false")
        source = package / "Mathlib.lean"
        source.write_text("def auxiliary : Nat := 1\n", encoding="utf-8")
        command("add", "Mathlib.lean")
        command("-c", "user.name=Test", "-c", "user.email=test@example.invalid",
                "commit", "-qm", "initial")
        baseline = lean_environment.external_packages_sha256(self.root)
        source.write_text("def auxiliary : Nat := 2\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Modified"):
            lean_environment.external_packages_sha256(self.root)
        command("add", "Mathlib.lean")
        command("-c", "user.name=Test", "-c", "user.email=test@example.invalid",
                "commit", "-qm", "revised")
        self.assertNotEqual(baseline,
                            lean_environment.external_packages_sha256(self.root))

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

    def test_unverifiable_fake_path_matches_absent_toolchain_snapshot(self):
        with patch("backend.lean_environment.shutil.which",
                   return_value=None):
            absent = lean_environment.executable_toolchain_sha256(self.root)
        with patch("backend.lean_environment.shutil.which",
                   return_value=str(self.root / "fake-lake-executable")):
            advertised_only = lean_environment.executable_toolchain_sha256(self.root)
        self.assertEqual(absent, advertised_only)

    def test_real_olean_content_change_invalidates_artifact_hash(self):
        build = self.root / ".lake" / "build" / "lib" / "lean" / "Local"
        build.mkdir(parents=True)
        file = build / "Example.olean"
        file.write_bytes(b"compiled version 1")
        original = lean_environment.compiled_artifacts_sha256(self.root)
        file.write_bytes(b"compiled version 2")
        self.assertNotEqual(original,
                            lean_environment.compiled_artifacts_sha256(self.root))

    def test_package_artifacts_and_build_tree_creation_change_snapshot(self):
        empty = lean_environment.compiled_artifacts_sha256(self.root)
        root = self.root / ".lake" / "packages" / "mathlib" / ".lake" / "build" / "lib" / "lean"
        root.mkdir(parents=True)
        built = lean_environment.compiled_artifacts_sha256(self.root)
        self.assertNotEqual(empty, built)
        package = root / "Mathlib" / "Data"
        package.mkdir(parents=True)
        artifact = package / "Nat.olean"
        artifact.write_bytes(b"compiled mathlib")
        self.assertNotEqual(built, lean_environment.compiled_artifacts_sha256(self.root))
        artifact.unlink()
        self.assertEqual(built, lean_environment.compiled_artifacts_sha256(self.root))

    def test_olean_budget_is_explicit_and_metadata_changes_are_detected(self):
        root = self.root / ".lake" / "build" / "lib" / "lean"
        root.mkdir(parents=True)
        artifact = root / "Large.olean"
        artifact.write_bytes(b"a" * 1024)
        with patch("backend.lean_environment.MAX_OLEAN_HASH_BYTES", 1):
            budget = [1]
            before = lean_environment._olean_tree(root, label="project", budget=budget)
            self.assertEqual(before["coverage"], "metadata_only")
            self.assertEqual(before["artifacts"][0]["content"], "metadata_only")
            first = lean_environment.compiled_artifacts_sha256(self.root)
            artifact.write_bytes(b"b" * 2048)
            second = lean_environment.compiled_artifacts_sha256(self.root)
            self.assertNotEqual(first, second)

    def test_olean_tree_rejects_symlink_and_too_many_files(self):
        root = self.root / ".lake" / "build" / "lib" / "lean"
        root.mkdir(parents=True)
        target = self.root / "external"
        target.write_bytes(b"compiled")
        link = root / "External.olean"
        try:
            link.symlink_to(target)
        except (OSError, NotImplementedError):
            self.skipTest("Symbolic links are unavailable")
        with self.assertRaisesRegex(ValueError, "Symlinked"):
            lean_environment.compiled_artifacts_sha256(self.root)
        link.unlink()
        (root / "One.olean").write_bytes(b"1")
        (root / "Two.olean").write_bytes(b"2")
        with patch("backend.lean_environment.MAX_OLEAN_FILES", 1):
            with self.assertRaisesRegex(ValueError, "Too many"):
                lean_environment.compiled_artifacts_sha256(self.root)

    def test_olean_file_limit_applies_across_all_package_roots(self):
        project = self.root / ".lake" / "build" / "lib" / "lean"
        project.mkdir(parents=True)
        (project / "First.olean").write_bytes(b"first")
        external = (self.root / ".lake" / "packages" / "mathlib" /
                    ".lake" / "build" / "lib" / "lean")
        external.mkdir(parents=True)
        (external / "Second.olean").write_bytes(b"second")
        with patch("backend.lean_environment.MAX_OLEAN_FILES", 1):
            with self.assertRaisesRegex(ValueError, "Too many"):
                lean_environment.compiled_artifacts_sha256(self.root)

    def test_olean_content_fingerprint_detects_same_length_edit(self):
        root = self.root / ".lake" / "build" / "lib" / "lean"
        root.mkdir(parents=True)
        artifact = root / "Exact.olean"
        artifact.write_bytes(b"AAAA")
        first = lean_environment._olean_tree(
            root, label="project", budget=[100])
        artifact.write_bytes(b"BBBB")
        second = lean_environment._olean_tree(
            root, label="project", budget=[100])
        self.assertNotEqual(first["artifacts"][0]["sha256"],
                            second["artifacts"][0]["sha256"])
        self.assertEqual(first["artifacts"][0]["size"],
                         second["artifacts"][0]["size"])

    def test_olean_lexical_name_optimization_preserves_original_tree_schema(self):
        """Compare with the pre-optimization algorithm, including exact key order."""
        root = self.root / ".lake" / "build" / "lib" / "lean"
        for name, contents in (
            ("Zeta.olean", b"foo"),
            ("sub/Alpha.olean", b"something longer"),
            ("sub/Nazwa_ż.olean", b"polish"),
            ("_nested/Ord.olean", b""),
        ):
            artifact = root / name
            artifact.parent.mkdir(parents=True, exist_ok=True)
            artifact.write_bytes(contents)
        (root / "sub" / "ignored.txt").write_bytes(b"not an artifact")

        def previous_implementation(budget):
            # This reproduces the earlier name/sort/read path, NOT a
            # replacement production fingerprint or weaker digest.
            paths = []
            for directory, dirs, names in os.walk(root, followlinks=False):
                base = Path(directory)
                if any((base / name).is_symlink() for name in dirs):
                    raise ValueError("Symlinked Lake artifact directory")
                for name in names:
                    artifact = base / name
                    if artifact.suffix == ".olean":
                        if artifact.is_symlink():
                            raise ValueError("Symlinked Lake .olean artifact")
                        paths.append(artifact)
            entries = []
            metadata_only = 0
            for artifact in sorted(paths, key=lambda x: x.relative_to(root).as_posix()):
                info = artifact.stat()
                if not artifact.is_file():
                    raise ValueError("Lake .olean artifact is not a regular file")
                entry = {
                    "name": artifact.relative_to(root).as_posix(),
                    "size": info.st_size,
                    "mtime_ns": info.st_mtime_ns,
                    "ctime_ns": info.st_ctime_ns,
                    "inode": info.st_ino,
                }
                if info.st_size <= budget:
                    digest = hashlib.sha256()
                    with artifact.open("rb") as stream:
                        for chunk in iter(lambda: stream.read(128 * 1024), b""):
                            digest.update(chunk)
                        open_size = os.fstat(stream.fileno()).st_size
                    after = artifact.stat()
                    if (info.st_size != open_size or info.st_size != after.st_size
                            or info.st_mtime_ns != after.st_mtime_ns
                            or info.st_ctime_ns != after.st_ctime_ns
                            or info.st_ino != after.st_ino):
                        raise ValueError("Lake .olean artifact changed while fingerprinting")
                    entry["sha256"] = digest.hexdigest()
                    budget -= info.st_size
                else:
                    entry["content"] = "metadata_only"
                    metadata_only += 1
                entries.append(entry)
            return {
                "label": "project", "state": "built",
                "coverage": "metadata_only" if metadata_only else "content_sha256",
                "artifacts": entries,
            }

        for budget in (0, 3, 128 * 1024):
            with self.subTest(budget=budget):
                expected = previous_implementation(budget)
                actual = lean_environment._olean_tree(
                    root, label="project", budget=[budget])
                self.assertEqual(expected, actual)
                self.assertEqual(
                    [x["name"] for x in actual["artifacts"]],
                    sorted(x["name"] for x in actual["artifacts"]))

    def test_unresolved_path_is_recorded_not_verified(self):
        fake = self.root / "missing"
        value = lean_environment._binary_identity(str(fake))
        self.assertEqual(value["state"], "unresolved")
        self.assertNotIn("sha256", value)


if __name__ == "__main__":
    unittest.main()
