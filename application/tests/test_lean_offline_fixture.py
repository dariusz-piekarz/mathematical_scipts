"""RT-09c contracts use synthetic bytes; only Linux CI may establish real execution."""
import copy
import hashlib
import json
import os
from pathlib import Path, PurePosixPath as P
import subprocess
import tempfile
import unittest
from unittest.mock import Mock, patch

from scripts import lean_offline_fixture as offline
from scripts import lean_artifact_manifest as artifacts
from tests import test_lean_mathlib_source_probe as source_fixture

VERSION = 'Lean (version 4.26.0, x86_64-unknown-linux-gnu, commit ' + offline.core.LEAN_COMMIT + ', Release)'
MISSING_OUTPUT = (VERSION + "\n/opt/atlas/Fixture.lean:1:0: error: object file '/"
                  + offline.MISSING_IMPORT + "' of module Mathlib.Logic.Basic does not exist\n").encode()


class DependencyTraceTests(unittest.TestCase):
    def test_persisted_json_rejects_duplicates_nonfinite_and_oversized_data(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'report.json'
            path.write_bytes(b'{"value":1}')
            self.assertEqual(offline.read_evidence(path), {'value': 1})
            for raw in (b'{"x":1,"x":2}', b'{"x":NaN}'):
                path.write_bytes(raw)
                with self.assertRaises(ValueError):
                    offline.read_evidence(path)
            with patch.object(artifacts, 'MAX_MANIFEST_BYTES', 2), self.assertRaises(ValueError):
                offline.read_evidence(path)

    def test_absolute_relative_and_directory_descriptor(self):
        raw = (b'openat(AT_FDCWD, "/lib/libc.so.6", O_RDONLY|O_CLOEXEC) = 3</usr/lib/libc.so.6>\n'
               b'openat(AT_FDCWD, "Fixture.lean", O_RDONLY) = 4</work/Fixture.lean>\n'
               b'12 openat(5</tools/lib>, "../bin/lean", O_RDONLY) = 6</tools/bin/lean>\n'
               b'openat(AT_FDCWD, "/absent", O_RDONLY) = -1 ENOENT (No such file)\n'
               b'+++ exited with 0 +++\n')
        self.assertEqual(offline.parse_trace(raw, cwd=P('/work')),
                         {P('/lib/libc.so.6'), P('/work/Fixture.lean'), P('/tools/bin/lean')})

    def test_annotated_working_directory_and_empty_thread_trace(self):
        raw = b'openat(AT_FDCWD</tools/lib>, "../bin/lean", O_RDONLY|O_CLOEXEC) = 3</tools/bin/lean>\n'
        self.assertEqual(offline.parse_trace(raw, cwd=P('/work')), {P('/tools/bin/lean')})
        self.assertEqual(offline.parse_trace(b'', cwd=P('/work'), allow_empty=True), set())
        with self.assertRaises(ValueError):
            offline.parse_trace(b'openat(AT_FDCWD, "truncated', cwd=P('/work'), allow_empty=True)

    def test_device_descriptors_from_real_mathlib_trace(self):
        # Exact descriptor format from rootless CI job 139518900286.
        raw = (b'openat(AT_FDCWD</tmp/atlas-offline-ma5puqyz>, "/dev/urandom", '
               b'O_RDONLY|O_CLOEXEC) = 11</dev/urandom<char 1:9>>\n'
               b'openat(AT_FDCWD, "/dev/sda", O_RDONLY) = 4</dev/sda<block 8:0>>\n')
        self.assertEqual(offline.parse_trace(raw, cwd=P('/work')),
                         {P('/dev/urandom'), P('/dev/sda')})

    def test_device_annotations_remain_strict_and_read_only(self):
        for descriptor, requested, flags in (
                ('/dev/urandom<char 1:9>', '/dev/urandom', 'O_RDWR'),
                ('/dev/urandom<char 1:9>', '/dev/urandom', 'O_RDONLY|O_CREAT'),
                ('/tools/lean<char 1:9>', '/tools/lean', 'O_RDONLY'),
                ('/dev/urandom<char 1:9>', '/tools/lean', 'O_RDONLY'),
                ('/dev/urandom<char 1:>', '/dev/urandom', 'O_RDONLY'),
                ('/dev/urandom<socket 1:9>', '/dev/urandom', 'O_RDONLY'),
                ('/dev/urandom<char 1:9> (deleted)', '/dev/urandom', 'O_RDONLY'),
                ('/dev/urandom<char 1:9', '/dev/urandom', 'O_RDONLY')):
            raw = f'openat(AT_FDCWD, "{requested}", {flags}) = 3<{descriptor}>\n'.encode()
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                offline.parse_trace(raw, cwd=P('/work'))

    def test_malformed_truncated_write_and_deleted_descriptors_are_rejected(self):
        for raw in (b'', b'openat(AT_FDCWD, "/x", O_RDONLY <unfinished ...>',
                    b'openat(AT_FDCWD, "/x", O_RDWR|O_CREAT) = 3</x>',
                    b'openat(AT_FDCWD, "/x", O_RDONLY) = 3</x (deleted)>', b'\xff'):
            with self.subTest(raw=raw), self.assertRaises((ValueError, UnicodeDecodeError)):
                offline.parse_trace(raw, cwd=P('/work'))
        with patch.object(offline, 'MAX_TRACE_BYTES', 2), self.assertRaises(ValueError):
            offline.parse_trace(b'123', cwd=P('/work'))

    def test_nonportable_names_and_relative_roots_are_rejected(self):
        for path in ('relative', '//lib/x', '/x\x00y', '/lib\\x', '/lib/CON', '/lib/a b'):
            with self.subTest(path=path), self.assertRaises(ValueError):
                offline.normalized(path)

    def test_only_approved_roots_may_be_relocated(self):
        tool = P('/tools/lean')
        packages = {'mathlib': P('/work/mathlib')}
        self.assertEqual(offline.destination(P('/tools/lean/bin/lean'), tool, packages), P('opt/lean/bin/lean'))
        self.assertEqual(offline.destination(P('/work/mathlib/A.olean'), tool, packages), P('opt/packages/mathlib/A.olean'))
        self.assertEqual(offline.destination(P('/lib/libc.so.6'), tool, packages), P('lib/libc.so.6'))
        for path in ('/home/user/token', '/tools/lean-other/bin/lean', '/work/mathlib/../../secret'):
            with self.subTest(path=path), self.assertRaises(ValueError):
                offline.destination(P(path), tool, packages)

    def test_unresolved_elf_dependencies_are_not_a_complete_closure(self):
        raw = b'linux-vdso.so.1 (0x123)\nlibc.so.6 => /lib/libc.so.6 (0xabcdef)\n/lib64/ld-linux.so (0x123)\n'
        self.assertEqual(offline.elf_dependencies(raw), {P('/lib/libc.so.6'), P('/lib64/ld-linux.so')})
        for raw in (b'', b'libc.so.6 => not found\n', b'statically linked'):
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                offline.elf_dependencies(raw)

    def test_observation_output_is_file_backed_and_capped(self):
        def spawn(*args, **kwargs):
            self.assertNotEqual(kwargs['stdout'], subprocess.PIPE)
            self.assertEqual(kwargs['stdin'], subprocess.DEVNULL)
            self.assertTrue(kwargs['start_new_session'])
            kwargs['stdout'].write(b'x' * 17)
            return Mock(wait=Mock(return_value=0))
        with patch.object(offline.subprocess, 'Popen', side_effect=spawn), patch.object(offline.policy, 'MAX_OUTPUT_BYTES', 16):
            with self.assertRaises(ValueError):
                offline.trace_command(['trusted-lean'], Path('trace'), cwd=Path('.'), env={})

    def test_timeout_kills_and_reaps_the_observed_process_group(self):
        process = Mock(pid=123, wait=Mock(side_effect=[subprocess.TimeoutExpired('trusted-lean', 120), 0]))
        with patch.object(offline.subprocess, 'Popen', return_value=process), patch.object(offline.os, 'killpg', create=True) as kill, patch.object(offline.signal, 'SIGKILL', 9, create=True):
            with self.assertRaises(subprocess.TimeoutExpired):
                offline.trace_command(['trusted-lean'], Path('trace'), cwd=Path('.'), env={})
            kill.assert_called_once_with(123, offline.signal.SIGKILL)
            self.assertEqual(process.wait.call_count, 2)

    @unittest.skipUnless(os.name == 'posix', 'Linux offline dependency staging')
    def test_staging_copies_regular_bytes_and_retains_provenance(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            tool = root / 'tool'
            tool.mkdir()
            source = tool / 'lean'
            source.write_bytes(b'observed-trusted-fixture')
            bundle = root / 'bundle'
            bundle.mkdir()
            result = offline.stage({source}, bundle, tool, {}, root / 'Fixture.lean')
            self.assertEqual((bundle / 'opt/lean/lean').read_bytes(), source.read_bytes())
            self.assertEqual(result['opt/lean/lean']['sha256'], hashlib.sha256(source.read_bytes()).hexdigest())
            self.assertEqual(result['opt/lean/lean']['resolved_source'], str(source.resolve()))

    @unittest.skipUnless(os.name == 'posix', 'Linux offline dependency staging')
    def test_staging_refuses_symlink_escape(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            tool = root / 'tool'
            tool.mkdir()
            private = root / 'private'
            private.write_bytes(b'outside-approved-root')
            source = tool / 'lean'
            source.symlink_to(private)
            bundle = root / 'bundle'
            bundle.mkdir()
            with self.assertRaises(ValueError):
                offline.stage({source}, bundle, tool, {}, root / 'Fixture.lean')


class OfflineReportTests(unittest.TestCase):
    def setUp(self):
        source = source_fixture.MathlibSourceClosureTests()
        source.setUp()
        self.addCleanup(source.doCleanups)
        source_report = source.inspect()
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        self.root = root
        data = {'opt/lean/bin/lean': b'synthetic-binary', offline.MISSING_IMPORT: b'synthetic-import',
                'opt/atlas/Fixture.lean': offline.SOURCE.encode(),
                'opt/atlas/run-draft': offline.entry_script(p['name'] for p in source_report['packages']).encode()}
        for name, content in data.items():
            target = root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
        self.manifest = artifacts.create_manifest(root, source_report)
        self.sha = source_report['checkout_sha']
        self.digest = hashlib.sha256(artifacts.encoded(self.manifest)).hexdigest()
        self.origins = {'opt/lean/bin/lean': {'source': '/tools/bin/lean', 'resolved_source': '/tools/bin/lean',
                        'sha256': hashlib.sha256(data['opt/lean/bin/lean']).hexdigest(), 'size': len(data['opt/lean/bin/lean'])}}
        self.origins[offline.MISSING_IMPORT] = {
            'source': '/packages/mathlib/Basic.olean', 'resolved_source': '/packages/mathlib/Basic.olean',
            'sha256': hashlib.sha256(data[offline.MISSING_IMPORT]).hexdigest(), 'size': len(data[offline.MISSING_IMPORT])}
        version = 'Lean (version 4.26.0, x86_64-unknown-linux-gnu, commit ' + offline.core.LEAN_COMMIT + ', Release)'
        self.report = {'schema': 1, 'status': 'trusted_mathlib_fixture_offline_compiled', 'checkout_sha': self.sha,
                       'source_sha256': hashlib.sha256(offline.SOURCE.encode()).hexdigest(),
                       'archive_sha256': offline.core.ARCHIVE_SHA256, 'manifest_sha256': self.digest,
                       'file_count': self.manifest['file_count'], 'total_bytes': self.manifest['total_bytes'],
                       'observed_origin_count': len(self.origins), 'execution_allowed': False, 'offline_ready': False,
                       'certificate': False, 'proof_status': 'not_run', 'container_state': 'exited', 'exit_code': 0,
                       'cleanup_status': 'removed_verified', 'image_id': 'sha256:' + 'a' * 64,
                       'container_id': 'b' * 64, 'lean_version': version, 'lake_version': 'Lake version 5.0.0',
                       'compiler_output': 'Lake version 5.0.0\n' + version + "\n'atlas_isolated_fixture' does not depend on any axioms\n"}

    def validate(self, report=None, manifest=None, origins=None):
        offline.validate_report(self.report if report is None else report,
                                self.manifest if manifest is None else manifest,
                                self.origins if origins is None else origins,
                                expected_sha=self.sha, expected_manifest_sha=self.digest)

    def test_scoped_report_roundtrip_does_not_allow_drafts(self):
        self.validate()
        self.assertFalse(self.report['offline_ready'])
        self.assertFalse(self.report['execution_allowed'])
        self.assertFalse(self.report['certificate'])

    def test_flags_identity_cleanup_and_compiler_output_cannot_be_promoted(self):
        changes = {'execution_allowed': True, 'offline_ready': True, 'certificate': True, 'exit_code': 1,
                   'checkout_sha': '0' * 40, 'image_id': 'latest', 'container_id': 'short',
                   'cleanup_status': 'pending', 'compiler_output': 'success', 'schema': True,
                   'proof_status': 'compiled', 'file_count': True}
        for key, value in changes.items():
            report = copy.deepcopy(self.report)
            report[key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                self.validate(report=report)

    def test_missing_provenance_and_tampered_manifest_fail(self):
        with self.assertRaises(ValueError):
            self.validate(origins={})
        origins = copy.deepcopy(self.origins)
        origins['opt/lean/bin/lean']['sha256'] = '0' * 64
        with self.assertRaises(ValueError):
            self.validate(origins=origins)
        manifest = copy.deepcopy(self.manifest)
        manifest['entries'][0]['path'] = 'elsewhere'
        with self.assertRaises(ValueError):
            self.validate(manifest=manifest)

    def rejected_evidence(self):
        (self.root / offline.MISSING_IMPORT).unlink()
        manifest = artifacts.create_manifest(self.root, self.manifest['source_closure'])
        origins = {p: o for p, o in self.origins.items() if p != offline.MISSING_IMPORT}
        report = {**self.report, 'status': 'trusted_mathlib_fixture_missing_import_rejected',
                  'missing_import': offline.MISSING_IMPORT, 'exit_code': 1,
                  'image_id': 'sha256:' + 'c' * 64, 'container_id': 'd' * 64,
                  'manifest_sha256': hashlib.sha256(artifacts.encoded(manifest)).hexdigest(),
                  'file_count': manifest['file_count'], 'total_bytes': manifest['total_bytes'],
                  'observed_origin_count': len(origins),
                  'compiler_output': self.report['lake_version'] + '\n' + MISSING_OUTPUT.decode()}
        return report, manifest, origins

    def test_missing_import_reports_are_distinct_and_only_one_file_may_differ(self):
        positive = self.report, self.manifest, self.origins
        negative = self.rejected_evidence()
        def validate(evidence):
            offline.validate_report_pair(positive, evidence, expected_sha=self.sha,
                                         expected_manifest_sha=self.digest,
                                         expected_rejected_manifest_sha=evidence[0]['manifest_sha256'])
        validate(negative)
        with self.assertRaises(ValueError):
            offline.validate_report(
                *negative, expected_sha=self.sha, expected_manifest_sha=negative[0]['manifest_sha256'])
        with self.assertRaises(ValueError):
            offline.validate_report(*positive, expected_sha=self.sha,
                                    expected_manifest_sha=self.digest, rejected=True)
        for key, value in (('image_id', self.report['image_id']), ('container_id', self.report['container_id']),
                           ('exit_code', 0), ('certificate', True), ('missing_import', 'Other.olean')):
            changed = copy.deepcopy(negative)
            changed[0][key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                validate(changed)
        # Even an internally consistent negative manifest must preserve all
        # other bytes of the successful bundle.
        (self.root / 'opt/lean/bin/lean').write_bytes(b'changed-binary')
        changed_manifest = artifacts.create_manifest(self.root, self.manifest['source_closure'])
        changed_origins = copy.deepcopy(negative[2])
        changed_origins['opt/lean/bin/lean'].update(sha256=hashlib.sha256(b'changed-binary').hexdigest(),
                                                 size=len(b'changed-binary'))
        changed_report = {**negative[0], 'total_bytes': changed_manifest['total_bytes'],
                          'manifest_sha256': hashlib.sha256(artifacts.encoded(changed_manifest)).hexdigest()}
        with self.assertRaisesRegex(ValueError, 'differ only'):
            validate((changed_report, changed_manifest, changed_origins))


class MissingImportRuntimeTests(unittest.TestCase):
    def test_diagnostic_rejects_success_other_errors_and_wrong_versions(self):
        self.assertEqual(offline.validate_missing_import_output(MISSING_OUTPUT), VERSION)
        for output in (MISSING_OUTPUT.replace(b'Basic.olean', b'Other.olean'),
                       MISSING_OUTPUT.replace(b':1:0:', b':2:0:'),
                       MISSING_OUTPUT.replace(offline.core.LEAN_COMMIT.encode(), b'0' * 40),
                       MISSING_OUTPUT + b'warning\n', b'daemon failure',
                       (VERSION + "\n'atlas_isolated_fixture' does not depend on any axioms\n").encode()):
            with self.subTest(output=output), self.assertRaises(ValueError):
                offline.validate_missing_import_output(output)

    def test_expected_rejection_requires_exit_diagnostic_identity_and_cleanup(self):
        cid, image = 'a' * 64, 'sha256:' + 'b' * 64
        lake = 'Lake version 5.0.0'
        for case in ('valid', 'compiled', 'exit', 'diagnostic', 'container_exit', 'identity', 'oom',
                     'timeout', 'output_limit', 'unreaped', 'cleanup'):
            calls = []
            def command(prefix, args, env, *, deadline=None, capture_failure=False):
                if args[0] == 'create':
                    return cid.encode()
                if args[:2] == ('container', 'start'):
                    self.assertTrue(capture_failure)
                    if case == 'compiled':
                        return b'unexpected success'
                    if case in ('timeout', 'output_limit', 'unreaped'):
                        error = {'timeout': offline.transport.DockerCommandTimeout,
                                 'output_limit': offline.transport.DockerOutputLimit,
                                 'unreaped': offline.transport.DockerCLIReapUnconfirmed}[case]
                        raise error('interrupted')
                    output = lake.encode() + b'\n' + MISSING_OUTPUT
                    raise offline.transport.DockerCommandFailed('failed', returncode=2 if case == 'exit' else 1,
                                                               output=b'other error' if case == 'diagnostic' else output)
                if deadline is not None:
                    calls.append((args, deadline))
                    if args[:2] == ('container', 'inspect'):
                        return json.dumps([{'Id': 'e' * 64 if case == 'identity' else cid, 'Image': image,
                            'State': {'Status': 'exited', 'Running': False, 'OOMKilled': case == 'oom',
                                      'ExitCode': 0 if case == 'container_exit' else 1}}]).encode()
                    if args[:2] == ('container', 'ls'):
                        return cid.encode() if case == 'cleanup' else b''
                return b'{}'
            with self.subTest(case=case), patch.object(offline.transport, '_command', side_effect=command), \
                    patch.object(offline.transport, 'validate_engine'), \
                    patch.object(offline.policy, 'validate_image_inspection'), \
                    patch.object(offline.transport, 'validate_container'):
                if case == 'valid':
                    result = offline.check_image([], {}, image, lake, rejected=True)
                    self.assertEqual(result['exit_code'], 1)
                    self.assertEqual(result['cleanup_status'], 'removed_verified')
                else:
                    with self.assertRaises((ValueError, TimeoutError)):
                        offline.check_image([], {}, image, lake, rejected=True)
            self.assertIn(('container', 'rm', '--force', cid), [args for args, _ in calls])
            self.assertEqual(len({deadline for _, deadline in calls}), 1)


if __name__ == '__main__':
    unittest.main()
