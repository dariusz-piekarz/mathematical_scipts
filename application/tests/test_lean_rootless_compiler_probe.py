"""Contract tests for the CI-only trusted Lean fixture, not real compiler evidence."""
import json
import unittest
from unittest.mock import patch

from backend import lean_draft_transport as transport
from scripts import lean_rootless_compiler_probe as probe

VERSION = b"Lean (version 4.26.0, x86_64-unknown-linux-gnu, commit abcdef123456, Release)\n"
AXIOMS = b"'atlas_isolated_fixture' does not depend on any axioms\n"


class TrustedCoreFixtureTests(unittest.TestCase):
    def test_strict_compiler_output(self):
        self.assertEqual(probe.validate_output(VERSION + AXIOMS), VERSION.decode().strip())
        for output in (AXIOMS, VERSION, VERSION.replace(b"4.26.0", b"4.27.0") + AXIOMS,
                       VERSION + AXIOMS + b"warning\n", VERSION + b"'atlas_isolated_fixture' depends on axioms: [sorryAx]\n"):
            with self.subTest(output=output), self.assertRaises(ValueError):
                probe.validate_output(output)

    def exercise(self, *, output=VERSION + AXIOMS, exit_code=0, remaining=b""):
        cid, image = "a" * 64, "sha256:" + "b" * 64
        calls = []
        def command(prefix, args, env, *, deadline=None):
            calls.append((args, deadline))
            if args[0] == "create":
                return cid.encode()
            if args[:2] == ("container", "start"):
                self.assertIsNone(deadline)
                return output
            if args[:2] == ("container", "inspect") and deadline is not None:
                return json.dumps([{"Id": cid, "Image": image, "State": {
                    "Status": "exited", "Running": False, "OOMKilled": False,
                    "ExitCode": exit_code}}]).encode()
            if args[:2] == ("container", "ls"):
                return remaining
            return b"{}"
        with patch.object(transport, "_command", side_effect=command), \
                patch.object(transport, "validate_engine"), \
                patch.object(probe.policy, "validate_image_inspection"), \
                patch.object(transport, "validate_container"):
            if output != VERSION + AXIOMS or exit_code or remaining:
                with self.assertRaises(ValueError):
                    probe.check_compiler([], {}, image)
            else:
                result = probe.check_compiler([], {}, image)
                self.assertEqual(result["status"], "trusted_core_fixture_compiled")
                self.assertEqual(result["cleanup_status"], "removed_verified")
                self.assertFalse(result["execution_allowed"])
                self.assertFalse(result["certificate"])
                self.assertEqual(result["proof_status"], "not_run")
        cleanup = [(args[1], deadline) for args, deadline in calls if deadline is not None]
        self.assertEqual([name for name, _ in cleanup],
                         ["inspect", "rm", "ls"] if output == VERSION + AXIOMS else ["rm", "ls"])
        self.assertEqual(len({deadline for _, deadline in cleanup}), 1)

    def test_compilation_and_removal_share_evidence_contract(self):
        self.exercise()

    def test_reject_nonzero_exit_wrong_output_and_unconfirmed_removal(self):
        for kwargs in ({"exit_code": 1}, {"output": b"fake success"}, {"remaining": b"a" * 64}):
            with self.subTest(kwargs=kwargs):
                self.exercise(**kwargs)


    def test_release_archive_checks_size_and_digest_before_extraction(self):
        import hashlib
        import tempfile
        from pathlib import Path
        data = b"small controlled archive fixture"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "release.tar.zst"
            path.write_bytes(data)
            with patch.object(probe, "ARCHIVE_SIZE", len(data)), \
                    patch.object(probe, "ARCHIVE_SHA256", hashlib.sha256(data).hexdigest()):
                probe.verify_archive(path)
                path.write_bytes(b"x" * len(data))
                with self.assertRaisesRegex(ValueError, "digest"):
                    probe.verify_archive(path)
                path.write_bytes(b"x")
                with self.assertRaisesRegex(ValueError, "size"):
                    probe.verify_archive(path)

    def test_missing_or_unexpected_dynamic_dependency_blocks_image(self):
        import tempfile
        from pathlib import Path
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for raw in (b"libX.so => not found\n",
                        b"libX.so => /tmp/unexpected.so (0x1234)\n"):
                with self.subTest(raw=raw), \
                        patch.object(probe.subprocess, "check_output", return_value=raw), \
                        patch.object(probe.shutil, "copy2") as copy:
                    with self.assertRaises(ValueError):
                        probe.stage_host_libraries(root / "toolchain", root / "rootfs")
                    copy.assert_not_called()
