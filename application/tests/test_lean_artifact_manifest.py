"""Selected-tree integrity tests; fixtures do not establish offline readiness."""
import copy
import contextlib
import hashlib
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from scripts import lean_artifact_manifest as artifacts
from tests import test_lean_mathlib_source_probe as source_fixture


class ArtifactManifestTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "bundle"
        self.root.mkdir()
        (self.root / "lib").mkdir()
        (self.root / "empty").mkdir()
        self.file = self.root / "lib/Basic.olean"
        self.file.write_bytes(b"test-artifact\x00\xff")
        # Reuse source-probe fixture only to obtain well-shaped source evidence.
        fixture = source_fixture.MathlibSourceClosureTests()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        self.report = fixture.inspect()
        self.manifest = artifacts.create_manifest(self.root, self.report)
        self.raw = artifacts.encoded(self.manifest)
        self.sha = hashlib.sha256(self.raw).hexdigest()

    def verify(self, raw=None, report=None):
        return artifacts.verify_manifest(
            self.root, self.raw if raw is None else raw, expected_sha256=self.sha,
            expected_source_report=self.report if report is None else report)

    def test_roundtrip_hashes_every_byte_and_retains_empty_directories(self):
        result = self.verify()
        self.assertEqual(result["status"], "selected_artifact_bytes_verified")
        self.assertEqual(result["file_count"], 1)
        self.assertEqual(result["total_bytes"], self.file.stat().st_size)
        entry = next(r for r in self.manifest["entries"] if r["kind"] == "file")
        self.assertEqual(entry["sha256"], hashlib.sha256(self.file.read_bytes()).hexdigest())
        self.assertIn({"path": "empty", "kind": "directory"}, self.manifest["entries"])
        for flag in ("offline_ready", "execution_allowed", "certificate"):
            self.assertIs(result[flag], False)
        self.assertEqual(self.raw, artifacts.encoded(artifacts.create_manifest(self.root, self.report)))

    def test_same_size_mutation_with_restored_mtime_is_rejected(self):
        old = self.file.stat()
        self.file.write_bytes(b"X" * old.st_size)
        os.utime(self.file, ns=(old.st_atime_ns, old.st_mtime_ns))
        with self.assertRaisesRegex(ValueError, "mismatch"):
            self.verify()

    def test_missing_extra_renamed_and_empty_directory_changes(self):
        for mode in ("missing", "extra", "renamed", "directory"):
            with self.subTest(mode=mode):
                if mode == "missing":
                    self.file.unlink()
                elif mode == "extra":
                    (self.root / "extra").write_bytes(b"")
                elif mode == "renamed":
                    self.file.rename(self.root / "lib/Other.olean")
                else:
                    (self.root / "empty").rmdir()
                with self.assertRaises(ValueError):
                    self.verify()
                if mode == "extra":
                    (self.root / "extra").unlink()
                elif mode == "renamed":
                    (self.root / "lib/Other.olean").rename(self.file)
                elif mode == "directory":
                    (self.root / "empty").mkdir()
                else:
                    self.file.write_bytes(b"test-artifact\x00\xff")

    def test_untrusted_manifest_digest_is_required(self):
        for sha in (None, "", "a" * 64, "A" * 64):
            with self.subTest(sha=sha), self.assertRaises(ValueError):
                artifacts.verify_manifest(self.root, self.raw, expected_sha256=sha,
                                          expected_source_report=self.report)
        with self.assertRaises(ValueError):
            self.verify(raw=self.raw + b" ")

    def test_cli_roundtrip_refuses_overwrite_and_output_inside_bundle(self):
        manifest_path = Path(self.temp.name) / "manifest.json"
        common = [str(self.root), str(manifest_path), "--lean-root", "unused",
                  "--checkout-sha", self.report["checkout_sha"]]
        with patch.object(artifacts.sources, "inspect_sources", return_value=self.report), \
                contextlib.redirect_stdout(io.StringIO()):
            with patch("sys.argv", ["manifest", "create", *common]):
                self.assertEqual(artifacts.main(), 0)
                with self.assertRaises(FileExistsError):
                    artifacts.main()
            actual_sha = hashlib.sha256(manifest_path.read_bytes()).hexdigest()
            with patch("sys.argv", ["manifest", "verify", *common,
                                    "--expected-sha256", actual_sha]):
                self.assertEqual(artifacts.main(), 0)
            common[1] = str(self.root / "manifest.json")
            with patch("sys.argv", ["manifest", "create", *common]), \
                    self.assertRaisesRegex(ValueError, "outside"):
                artifacts.main()
        self.assertFalse((self.root / "manifest.json").exists())

    def test_platform_skip_classification_is_narrow(self):
        from scripts.atlas_ci_report import classify_skip
        test_id = "tests.test_lean_artifact_manifest.ArtifactManifestTests.test_native_windows_junction_is_rejected"
        reason = "Native Windows junction regression"
        self.assertEqual(classify_skip(test_id, reason), "windows_native")
        self.assertEqual(classify_skip(test_id, reason + " other"), "unreviewed")
        self.assertEqual(classify_skip("tests.other_test.test_junction", reason), "unreviewed")

    def test_authenticated_but_invalid_schema_paths_and_claims_are_rejected(self):
        for field, value in (("schema", True), ("scope", "all_dependencies"),
                             ("offline_ready", True), ("execution_allowed", True),
                             ("certificate", True), ("file_count", 999),
                             ("unexpected", "field"),
                             ("entries", [{"path": "../../outside", "kind": "file"}])):
            data = {**self.manifest, field: value}
            raw = artifacts.encoded(data)
            with self.subTest(field=field), self.assertRaises(ValueError):
                artifacts.verify_manifest(self.root, raw,
                                          expected_sha256=hashlib.sha256(raw).hexdigest(),
                                          expected_source_report=self.report)

    def test_source_checkout_and_closure_are_bound_to_manifest(self):
        report = copy.deepcopy(self.report)
        report["checkout_sha"] = "b" * 40
        with self.assertRaisesRegex(ValueError, "mismatch"):
            self.verify(report=report)
        for field, value in (("lean_toolchain", "other"), ("package_count", True),
                             ("lock_sha256", "0" * 64), ("offline_ready", True)):
            with self.subTest(field=field), self.assertRaises(ValueError):
                artifacts.create_manifest(self.root, {**self.report, field: value})

    def test_duplicate_json_keys_and_excessive_nesting_fail(self):
        for raw in (b'{"schema":1,"schema":2}', b"[" * 2000 + b"]" * 2000):
            with self.subTest(raw=raw[:30]), self.assertRaises(ValueError):
                artifacts.verify_manifest(self.root, raw,
                                          expected_sha256=hashlib.sha256(raw).hexdigest(),
                                          expected_source_report=self.report)

    def test_file_total_entry_depth_and_manifest_limits_fail(self):
        limits = {"MAX_FILE_BYTES": 2, "MAX_TOTAL_BYTES": 2,
                  "MAX_ENTRIES": 2, "MAX_DEPTH": 0, "MAX_MANIFEST_BYTES": 10}
        for key, value in limits.items():
            with self.subTest(limit=key), patch.object(artifacts, key, value), \
                    self.assertRaises(ValueError):
                artifacts.create_manifest(self.root, self.report)
        with patch.object(artifacts, "MAX_MANIFEST_BYTES", 2), self.assertRaises(ValueError):
            self.verify()

    def test_nonportable_paths_are_rejected_before_opening(self):
        for name in ("..", ".", "CON", "nul.olean", "COM1.txt", "a:ads", "foo.",
                     "a\\b", "/absolute", "a/b", "name with spaces", "x" * 121):
            with self.subTest(name=name), self.assertRaises(ValueError):
                artifacts.component(name)

    @unittest.skipIf(os.name == "nt", "Case-sensitive filesystem test; portable paths tested separately")
    def test_case_collisions_are_rejected(self):
        (self.root / "lib/basic.olean").write_bytes(b"other")
        with self.assertRaisesRegex(ValueError, "Case-colliding"):
            artifacts.create_manifest(self.root, self.report)

    def test_hardlinks_are_rejected(self):
        os.link(self.file, self.root / "alias")
        with self.assertRaisesRegex(ValueError, "Hardlinked"):
            artifacts.create_manifest(self.root, self.report)

    @unittest.skipIf(os.name == "nt", "Native junction regression covers Windows reparse paths")
    def test_symlinked_file_root_and_ancestor_are_rejected(self):
        alias = Path(self.temp.name) / "alias"
        alias.symlink_to(self.root, target_is_directory=True)
        for root in (alias, alias / "lib"):
            with self.subTest(root=root), self.assertRaises(ValueError):
                artifacts.create_manifest(root, self.report)
        (self.root / "link").symlink_to(self.file)
        with self.assertRaises(ValueError):
            artifacts.create_manifest(self.root, self.report)

    @unittest.skipUnless(os.name == "nt", "Native Windows junction regression")
    def test_native_windows_junction_is_rejected(self):
        import subprocess
        junction = self.root / "junction"
        target = Path(self.temp.name) / "target"
        target.mkdir()
        result = subprocess.run(["cmd", "/c", "mklink", "/J", str(junction), str(target)],
                                capture_output=True, timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)
        try:
            for root in (self.root, junction):
                with self.subTest(root=root), self.assertRaises(ValueError):
                    artifacts.create_manifest(root, self.report)
        finally:
            junction.rmdir()

    def test_mutation_after_hash_and_added_file_during_scan_fail(self):
        original = artifacts.hash_file
        def mutate(path, info, deadline):
            result = original(path, info, deadline)
            (self.root / "new").write_bytes(b"new")
            return result
        with patch.object(artifacts, "hash_file", side_effect=mutate), \
                self.assertRaisesRegex(ValueError, "tree changed"):
            artifacts.create_manifest(self.root, self.report)

    def test_growing_real_file_read_is_bounded_and_rejected(self):
        fdopen = os.fdopen
        read_bytes = []
        target = self.file
        class GrowingReader:
            def __init__(self, handle):
                self.handle = handle
            def __enter__(self):
                return self
            def __exit__(self, *args):
                self.handle.close()
            def fileno(self):
                return self.handle.fileno()
            def read(self, size):
                data = self.handle.read(size)
                read_bytes.append(len(data))
                if len(read_bytes) == 1:
                    with target.open("ab") as writer:
                        writer.write(b"growth")
                return data
        before = self.file.stat().st_size
        with patch.object(artifacts.os, "fdopen", side_effect=lambda *a: GrowingReader(fdopen(*a))), \
                self.assertRaisesRegex(ValueError, "changed during read"):
            artifacts.create_manifest(self.root, self.report)
        self.assertLessEqual(sum(read_bytes), before + 1)

    def test_expired_deadline_and_empty_tree_fail(self):
        with patch.object(artifacts, "SCAN_SECONDS", -1), self.assertRaisesRegex(ValueError, "deadline"):
            artifacts.create_manifest(self.root, self.report)
        self.file.unlink()
        with self.assertRaisesRegex(ValueError, "Empty"):
            artifacts.create_manifest(self.root, self.report)


if __name__ == "__main__":
    unittest.main()
