"""Contract tests for the CI-only trusted Lean fixture, not real compiler evidence."""
import json
import unittest
from unittest.mock import patch

from backend import lean_draft_transport as transport
from scripts import lean_rootless_compiler_probe as probe

VERSION = b"Lean (version 4.26.0, x86_64-unknown-linux-gnu, commit d8204c9fd894, Release)\n"
AXIOMS = b"'atlas_isolated_fixture' does not depend on any axioms\n"


class TrustedCoreFixtureTests(unittest.TestCase):
    def test_strict_compiler_output(self):
        self.assertEqual(probe.validate_output(VERSION + AXIOMS), VERSION.decode().strip())
        for output in (AXIOMS, VERSION, VERSION.replace(b"4.26.0", b"4.27.0") + AXIOMS,
                       VERSION.replace(b"d8204c9fd894", b"abcdef123456") + AXIOMS,
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


    def valid_report(self):
        import hashlib
        return {"status": "trusted_core_fixture_compiled", "checkout_sha": "c" * 40,
                "archive_sha256": probe.ARCHIVE_SHA256,
                "source_sha256": hashlib.sha256(probe.SOURCE.encode()).hexdigest(),
                "container_state": "exited", "exit_code": 0,
                "cleanup_status": "removed_verified", "execution_allowed": False,
                "proof_status": "not_run", "certificate": False,
                "lean_version": VERSION.decode().strip(),
                "compiler_output": (VERSION + AXIOMS).decode(),
                "image_id": "sha256:" + "b" * 64, "container_id": "a" * 64}

    def test_report_rejects_inconsistent_identity_and_false_success(self):
        report = self.valid_report()
        probe.validate_report(report, expected_sha="c" * 40)
        for key, value in (("checkout_sha", "d" * 40), ("archive_sha256", "0" * 64),
                           ("source_sha256", "0" * 64), ("exit_code", False),
                           ("execution_allowed", True), ("certificate", True),
                           ("cleanup_status", "unconfirmed"), ("proof_status", "compiled"),
                           ("image_id", "latest"), ("container_id", "a"),
                           ("compiler_output", VERSION.decode()),
                           ("lean_version", "Lean 4.26.0")):
            with self.subTest(key=key), self.assertRaises(ValueError):
                probe.validate_report({**report, key: value}, expected_sha="c" * 40)
        for altered in ({**report, "extra": True},
                        {k: v for k, v in report.items() if k != "compiler_output"}):
            with self.assertRaises(ValueError):
                probe.validate_report(altered, expected_sha="c" * 40)

    def test_persisted_report_rejects_stale_duplicate_and_symlink(self):
        import tempfile
        from pathlib import Path
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "report.json"
            report = self.valid_report()
            probe.write_report(path, report, expected_sha="c" * 40)
            self.assertEqual(probe.read_report(path, expected_sha="c" * 40), report)
            with self.assertRaises(FileExistsError):
                probe.write_report(path, report, expected_sha="c" * 40)
            path.write_text('{"certificate": false, "certificate": true}')
            with self.assertRaises(ValueError):
                probe.read_report(path, expected_sha="c" * 40)
            path.unlink()
            path.symlink_to(Path(directory) / "missing")
            with self.assertRaises(OSError):
                probe.read_report(path, expected_sha="c" * 40)


    def test_interrupted_compiler_never_promotes_success_and_still_cleans_up(self):
        cid, image = "a" * 64, "sha256:" + "b" * 64
        for kind in (transport.DockerCommandTimeout, transport.DockerCLIReapUnconfirmed,
                     transport.DockerOutputLimit, transport.DockerCommandFailed):
            for listing_failed in (False, True):
                failure = kind("controlled interruption")
                calls = []
                def command(prefix, args, env, *, deadline=None):
                    if args[0] == "create":
                        return cid.encode()
                    if args[:2] == ("container", "start"):
                        raise failure
                    if deadline is not None:
                        calls.append((args[1], deadline))
                    if args[:2] == ("container", "ls") and listing_failed:
                        return cid.encode()
                    return b"{}" if deadline is None else b""
                with self.subTest(kind=kind, listing_failed=listing_failed), \
                        patch.object(transport, "_command", side_effect=command), \
                        patch.object(transport, "validate_engine"), \
                        patch.object(probe.policy, "validate_image_inspection"), \
                        patch.object(transport, "validate_container"):
                    if listing_failed:
                        with self.assertRaisesRegex(ValueError, "removal not confirmed"):
                            probe.check_compiler([], {}, image)
                    else:
                        with self.assertRaises(kind) as caught:
                            probe.check_compiler([], {}, image)
                        self.assertIs(caught.exception, failure)
                self.assertEqual([name for name, _ in calls], ["rm", "ls"])
                self.assertEqual(len({deadline for _, deadline in calls}), 1)
