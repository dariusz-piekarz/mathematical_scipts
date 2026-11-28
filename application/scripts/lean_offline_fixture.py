"""RT-09c: CI-only observed dependency closure for one trusted Mathlib fixture.

Trace trusted tools on the host, materialize regular files into a scratch image,
hash the complete rootfs, and compile the fixed fixture through the existing
rootless policy. No user input, application endpoint or draft execution.
"""
from __future__ import annotations

import ast
import argparse
import hashlib
import json
import os
import posixpath
import signal
from pathlib import Path, PurePosixPath
import re
import shlex
import stat
import subprocess
import tempfile
import time
import uuid

from backend import lean_draft_runner as policy, lean_draft_transport as transport
from scripts import lean_artifact_manifest as artifacts
from scripts import lean_mathlib_source_probe as sources
from scripts import lean_rootless_compiler_probe as core
from scripts.lean_rootless_ci_probe import cleanup_fixture, validate_exited_fixture

SOURCE = """import Mathlib.Logic.Basic
theorem atlas_isolated_fixture (p q : Prop) : (p ∧ q) ↔ (q ∧ p) := and_comm
#print axioms atlas_isolated_fixture
"""
MISSING_IMPORT = 'opt/packages/mathlib/.lake/build/lib/lean/Mathlib/Logic/Basic.olean'
MAX_TRACE_BYTES = 16 * 1024 * 1024
MAX_TRACE_FILES = 128
# Explicit opt-in for trusted host measurement only; never used by stage/main.
MEASUREMENT_TRACE_BYTES = 64 * 1024 * 1024
MEASUREMENT_TRACE_ENTRIES = 200000
SYSTEM_ROOTS = tuple(map(PurePosixPath, ("/lib", "/lib64", "/usr/lib")))
SYSTEM_FILES = set(map(PurePosixPath, ("/etc/ld.so.cache", "/etc/locale.alias", "/etc/localtime", "/bin/busybox", "/usr/bin/busybox", "/usr/share/zoneinfo/Etc/UTC")))
KERNEL_ROOTS = tuple(map(PurePosixPath, ("/proc", "/sys", "/dev")))
OPEN = re.compile(r'^(?:\d+\s+)?openat\((?P<directory>AT_FDCWD(?:<(?P<cwd>/[^>]*)>)?|\d+<(?P<base>/[^>]*)>), '
                  r'(?P<quoted>"(?:[^"\\]|\\.)*"), (?P<flags>[^\n]*)\)\s+=\s+(?P<fd>\d+)'
                  r'<(?P<resolved>/[^<>]+)(?:<(?P<device>char|block) \d+:\d+>)?>$')


def normalized(path: str, *, nonportable_components: set[str] | None = None) -> PurePosixPath:
    if not path.startswith("/") or path.startswith("//") or "\x00" in path or "\\" in path:
        raise ValueError("Expected absolute Linux dependency path")
    value = PurePosixPath(posixpath.normpath(path))
    for name in PurePosixPath(value.as_posix()).parts[1:]:
        try:
            artifacts.component(name)
        except ValueError:
            # A CI-only measurement collector may count Linux filenames that
            # cannot enter a portable artifact. Never relax the default path.
            if (nonportable_components is None or name.endswith(' (deleted)')
                    or any(ord(ch) < 32 or ord(ch) == 127 for ch in name)
                    or len(name.encode('utf-8')) > 255):
                raise
            nonportable_components.add(name)
            if len(nonportable_components) > MEASUREMENT_TRACE_ENTRIES:
                raise ValueError('Nonportable component measurement budget exceeded')
    return value


def parse_trace(raw: bytes, *, cwd: Path, allow_empty=False,
                measurement_only=False, nonportable_components: set[str] | None = None) -> set[Path]:
    """Accept only complete, decoded, read-only successful openat records."""
    if nonportable_components is not None and not measurement_only:
        raise ValueError('Nonportable collector requires measurement-only mode')
    byte_limit = MEASUREMENT_TRACE_BYTES if measurement_only else MAX_TRACE_BYTES
    entry_limit = MEASUREMENT_TRACE_ENTRIES if measurement_only else artifacts.MAX_ENTRIES
    if len(raw) > byte_limit:
        raise ValueError("Dependency trace byte budget exceeded")
    paths = set()
    for line in raw.decode("utf-8", errors="strict").splitlines():
        if not line or line.startswith(("--- ", "+++ ")):
            continue
        # Failed lookups supply no bytes; the isolated compilation must still
        # succeed without their host fallback paths.
        if re.search(r'\)\s+= -1 [A-Z]+(?: |$)', line):
            continue
        match = OPEN.fullmatch(line)
        if not match:
            raise ValueError("Incomplete or unexpected dependency trace: " + repr(line[:240]))
        directory, base = match['directory'], match['base'] or match['cwd']
        quoted, flags, resolved = match['quoted'], match['flags'], match['resolved']
        if any(token in flags for token in ("O_WRONLY", "O_RDWR", "O_CREAT", "O_TRUNC")):
            raise ValueError("Unexpected write in dependency trace")
        requested = ast.literal_eval(quoted)
        if type(requested) is not str:
            raise ValueError("Invalid dependency path literal")
        if not requested.startswith("/"):
            requested = str((PurePosixPath(base) if base else PurePosixPath(cwd)) / requested)
        requested_path = normalized(requested, nonportable_components=nonportable_components)
        resolved_path = normalized(resolved, nonportable_components=nonportable_components)
        # strace -yy annotates device descriptors, e.g. /dev/urandom<char 1:9>.
        # These are provided by the container runtime, never copied into rootfs.
        # Keep annotations restricted to /dev; other nested descriptor metadata
        # must still fail rather than be silently stripped from a file path.
        if match['device'] and not (requested_path.is_relative_to(PurePosixPath('/dev'))
                                    and resolved_path.is_relative_to(PurePosixPath('/dev'))):
            raise ValueError("Device descriptor outside /dev")
        paths.add(requested_path)
        if len(paths) > entry_limit:
            raise ValueError("Dependency trace entry budget exceeded")
    if not paths and not allow_empty:
        raise ValueError("Empty dependency trace")
    return paths


def elf_dependencies(raw: bytes) -> set[Path]:
    result = set()
    for line in raw.decode("ascii").splitlines():
        line = line.strip()
        if line.startswith("linux-vdso.so.1 "):
            continue
        match = re.fullmatch(r"(?:\S+ => )?(/\S+) \(0x[0-9a-f]+\)", line)
        if not match:
            raise ValueError("Unresolved ELF dependency")
        result.add(normalized(match.group(1)))
    if not result:
        raise ValueError("Empty ELF dependency set")
    return result


def destination(path: Path, toolchain: Path, packages: dict[str, Path], *,
                nonportable_components: set[str] | None = None) -> Path:
    path = normalized(str(path), nonportable_components=nonportable_components)
    toolchain = normalized(str(toolchain))
    packages = {name: normalized(str(root)) for name, root in packages.items()}
    if path.is_relative_to(toolchain):
        return PurePosixPath("opt/lean") / path.relative_to(toolchain)
    for name, root in packages.items():
        if path.is_relative_to(root):
            return PurePosixPath("opt/packages") / name / path.relative_to(root)
    if path in SYSTEM_FILES or any(path.is_relative_to(root) for root in SYSTEM_ROOTS):
        return path.relative_to("/")
    raise ValueError("Dependency outside approved roots: " + str(path))


def stage(paths: set[Path], rootfs: Path, toolchain: Path,
          packages: dict[str, Path], fixture: Path) -> dict:
    """Trusted CI files only; aliases become independent regular destination files."""
    origins = {}
    total = 0
    deadline = time.monotonic() + artifacts.SCAN_SECONDS
    for source in sorted(paths):
        if source == fixture or any(source.is_relative_to(root) for root in KERNEL_ROOTS):
            continue
        target = destination(source, toolchain, packages)
        source = Path(source)
        resolved = source.resolve(strict=True)
        # Also validate the symlink target, so an allowed alias cannot import
        # arbitrary host files. System /lib -> /usr/lib aliases are materialized.
        destination(resolved, toolchain, packages)
        info = artifacts.checked_stat(resolved)
        if stat.S_ISDIR(info.st_mode):
            continue
        if target.as_posix() in origins:
            raise ValueError("Colliding staged dependency")
        total += info.st_size
        if total > artifacts.MAX_TOTAL_BYTES or len(origins) >= artifacts.MAX_ENTRIES:
            raise ValueError("Offline bundle budget exceeded")
        before = artifacts.identity(info)
        sha = artifacts.hash_file(resolved, before, deadline)
        dest = rootfs / target
        dest.parent.mkdir(parents=True, exist_ok=True)
        # Source is trusted and quiescent; check copy bytes again below.
        with resolved.open("rb") as reader, dest.open("xb") as writer:
            remaining = info.st_size
            while remaining:
                if time.monotonic() >= deadline:
                    raise ValueError("Offline copy deadline exceeded")
                block = reader.read(min(artifacts.CHUNK, remaining))
                if not block:
                    raise ValueError("Offline dependency truncated")
                writer.write(block)
                remaining -= len(block)
            if reader.read(1):
                raise ValueError("Offline dependency grew")
        dest.chmod(0o755 if info.st_mode & 0o111 else 0o644)
        copied = artifacts.hash_file(dest, artifacts.identity(artifacts.checked_stat(dest)), deadline)
        if copied != sha or artifacts.identity(artifacts.checked_stat(resolved)) != before:
            raise ValueError("Offline dependency changed while staging")
        origins[target.as_posix()] = {"source": str(source), "resolved_source": str(resolved),
                                      "sha256": sha, "size": info.st_size}
    if not origins:
        raise ValueError("Empty offline dependency bundle")
    return origins


def validate_lake(output: bytes) -> str:
    value = output.decode("ascii").strip()
    if not re.fullmatch(r"Lake version [A-Za-z0-9 .+()_-]{1,180}", value):
        raise ValueError("Unexpected Lake version evidence")
    return value


def entry_script(package_names) -> str:
    relocated = ":".join("/opt/packages/" + name + "/.lake/build/lib/lean" for name in sorted(package_names))
    return ("#!/bin/busybox sh\nset -eu\nexport LEAN_PATH=" + shlex.quote(relocated) + "\n"
            "/opt/lean/bin/lake --version\n/opt/lean/bin/lean --version\n"
            "exec /opt/lean/bin/lean /opt/atlas/Fixture.lean\n")


def validate_missing_import_output(output: bytes) -> str:
    lines = output.decode('ascii').splitlines()
    diagnostic = ("/opt/atlas/Fixture.lean:1:0: error: object file '/" + MISSING_IMPORT
                  + "' of module Mathlib.Logic.Basic does not exist")
    if len(lines) != 2 or lines[1] != diagnostic:
        raise ValueError('Unexpected missing-import compiler evidence')
    return core.validate_version(lines[0])


def validate_report(report, manifest, origins, *, expected_sha, expected_manifest_sha, rejected=False):
    """Check persisted consistency, not authenticity or general offline readiness."""
    fixed = {"schema": 1, "status": "trusted_mathlib_fixture_offline_compiled", "checkout_sha": expected_sha,
             "source_sha256": hashlib.sha256(SOURCE.encode()).hexdigest(), "archive_sha256": core.ARCHIVE_SHA256,
             "manifest_sha256": expected_manifest_sha, "execution_allowed": False, "offline_ready": False,
             "certificate": False, "proof_status": "not_run", "container_state": "exited", "exit_code": 0,
             "cleanup_status": "removed_verified"}
    if rejected:
        fixed.update(status='trusted_mathlib_fixture_missing_import_rejected', exit_code=1,
                     missing_import=MISSING_IMPORT)
    variable = {"file_count", "total_bytes", "observed_origin_count", "image_id", "container_id",
                "lean_version", "lake_version", "compiler_output"}
    if (not isinstance(expected_sha, str) or not sources.REV.fullmatch(expected_sha)
            or not isinstance(expected_manifest_sha, str) or not artifacts.HEX.fullmatch(expected_manifest_sha)
            or type(report) is not dict or set(report) != set(fixed) | variable
            or any(type(report[k]) is not type(v) or report[k] != v for k, v in fixed.items())):
        raise ValueError("Invalid scoped offline fixture report")
    for name in ("file_count", "total_bytes", "observed_origin_count"):
        if type(report[name]) is not int or report[name] <= 0:
            raise ValueError("Invalid offline evidence counts")
    # Validate the raw list before path-keyed maps can hide duplicate entries.
    artifacts.validate_manifest_structure(manifest)
    if (type(manifest) is not dict or type(origins) is not dict
            or hashlib.sha256(artifacts.encoded(manifest)).hexdigest() != expected_manifest_sha
            or manifest.get('file_count') != report['file_count'] or manifest.get('total_bytes') != report['total_bytes']
            or len(origins) != report['observed_origin_count']):
        raise ValueError("Offline manifest counts differ")
    source = artifacts.provenance(manifest.get('source_closure'))
    if source['checkout_sha'] != expected_sha:
        raise ValueError("Offline source evidence is stale")
    files = {entry['path']: entry for entry in manifest.get('entries', []) if entry.get('kind') == 'file'}
    if (len(files) != report['file_count'] or len(files) != len(origins) + 2
            or sum(entry['size'] for entry in files.values()) != report['total_bytes']
            or set(files) != set(origins) | {'opt/atlas/Fixture.lean', 'opt/atlas/run-draft'}):
        raise ValueError("Incomplete observed dependency provenance")
    for path, origin in origins.items():
        if (type(origin) is not dict or set(origin) != {'source', 'resolved_source', 'sha256', 'size'}
                or origin['sha256'] != files[path]['sha256'] or origin['size'] != files[path]['size']):
            raise ValueError("Observed file differs from manifest")
        normalized(origin['source'])
        normalized(origin['resolved_source'])
    generated = {'opt/atlas/Fixture.lean': SOURCE,
                 'opt/atlas/run-draft': entry_script(p['name'] for p in source['packages'])}
    for path, text in generated.items():
        if files[path]['sha256'] != hashlib.sha256(text.encode()).hexdigest() or files[path]['size'] != len(text.encode()):
            raise ValueError("Fixed fixture bytes differ")
    if rejected and MISSING_IMPORT in files:
        raise ValueError('Rejected fixture still contains the required import')
    if (not isinstance(report['image_id'], str) or not policy._IMAGE.fullmatch(report['image_id'])
            or not isinstance(report['container_id'], str) or not transport._CONTAINER_ID.fullmatch(report['container_id'])):
        raise ValueError("Invalid isolated execution identity")
    output = report['compiler_output']
    if type(output) is not str or len(output) > transport.MAX_METADATA_BYTES:
        raise ValueError("Invalid compiler evidence")
    lake, separator, rest = output.partition('\n')
    validate_output = validate_missing_import_output if rejected else core.validate_output
    if (not separator or validate_lake(lake.encode()) != report['lake_version']
            or validate_output(rest.encode()) != report['lean_version']):
        raise ValueError("Inconsistent compiler evidence")


def validate_report_pair(positive, negative, *, expected_sha, expected_manifest_sha,
                         expected_rejected_manifest_sha):
    for evidence, digest, rejected in ((positive, expected_manifest_sha, False),
                                       (negative, expected_rejected_manifest_sha, True)):
        validate_report(*evidence, expected_sha=expected_sha,
                        expected_manifest_sha=digest, rejected=rejected)
    success, manifest, origins = positive
    failure, rejected_manifest, rejected_origins = negative
    if (success['image_id'] == failure['image_id']
            or success['container_id'] == failure['container_id']
            or any(success[k] != failure[k] for k in ('lean_version', 'lake_version'))):
        raise ValueError('Missing-import controls require distinct identities and identical tools')
    files = {e['path']: e for e in manifest['entries'] if e['kind'] == 'file'}
    rejected_files = {e['path']: e for e in rejected_manifest['entries'] if e['kind'] == 'file'}
    entries = {e['path']: e for e in manifest['entries']}
    rejected_entries = {e['path']: e for e in rejected_manifest['entries']}
    if (MISSING_IMPORT not in files or set(rejected_files) != set(files) - {MISSING_IMPORT}
            or any(files[path] != entry for path, entry in rejected_files.items())
            or rejected_entries != {p: e for p, e in entries.items() if p != MISSING_IMPORT}
            or rejected_origins != {p: o for p, o in origins.items() if p != MISSING_IMPORT}
            or manifest['source_closure'] != rejected_manifest['source_closure']):
        raise ValueError('Negative bundle must differ only by the required import')


def read_evidence(path: Path):
    artifacts.root_path(path.parent)
    info = artifacts.checked_stat(path)
    if not stat.S_ISREG(info.st_mode) or info.st_size > artifacts.MAX_MANIFEST_BYTES:
        raise ValueError('Offline evidence exceeds its regular-file budget')
    before = artifacts.identity(info)
    fd = os.open(path, os.O_RDONLY | getattr(os, 'O_BINARY', 0) | getattr(os, 'O_NOFOLLOW', 0))
    with os.fdopen(fd, 'rb') as handle:
        opened = os.fstat(handle.fileno())
        if artifacts.identity(opened) != before:
            raise ValueError('Offline evidence changed while opening')
        raw = handle.read(artifacts.MAX_MANIFEST_BYTES + 1)
        finished = os.fstat(handle.fileno())
    if (len(raw) != info.st_size or len(raw) > artifacts.MAX_MANIFEST_BYTES
            or artifacts.identity(finished) != before or finished.st_ctime_ns != opened.st_ctime_ns
            or artifacts.identity(artifacts.checked_stat(path)) != before):
        raise ValueError('Offline evidence changed or exceeded the byte budget')
    def reject_constant(value):
        raise ValueError('Non-finite JSON in offline evidence')
    return json.loads(raw, object_pairs_hook=sources.unique_object, parse_constant=reject_constant)


def check_image(prefix: list[str], env: dict[str, str], image: str, lake_version: str,
                *, rejected=False) -> dict:
    def call(*args):
        return transport._command(prefix, args, env)
    transport.validate_engine(transport._decode_metadata(call("info", "--format", "{{json .}}")))
    policy.validate_image_inspection(transport._decode_metadata(call("image", "inspect", image)),
                                     approved_image_id=image)
    name = "atlas-draft-" + uuid.uuid4().hex
    cid = call(*policy.isolation_arguments(image_id=image, container_name=name)).decode("ascii").strip()
    if not transport._CONTAINER_ID.fullmatch(cid):
        raise ValueError("Ambiguous offline fixture container ID")
    cleanup = transport.deferred_cleanup_command(prefix, env)
    try:
        transport.validate_container(transport._decode_metadata(call("container", "inspect", cid)),
                                     container_id=cid, image_id=image, name=name)
        if rejected:
            try:
                transport._command(prefix, ("container", "start", "--attach", cid), env,
                                   capture_failure=True)
            except transport.DockerCommandFailed as exc:
                if exc.returncode != 1 or type(exc.output) is not bytes:
                    raise ValueError('Missing-import control requires CLI exit 1 and diagnostics') from exc
                output = exc.output
            else:
                raise ValueError('Missing-import fixture unexpectedly compiled')
        else:
            output = call("container", "start", "--attach", cid)
        first, sep, rest = output.partition(b"\n")
        if not sep or first.decode("ascii") != lake_version:
            raise ValueError("Isolated Lake version differs from prepared tool")
        version = (validate_missing_import_output if rejected else core.validate_output)(rest)
        state = validate_exited_fixture(
            transport._decode_metadata(cleanup("container", "inspect", cid)),
            container_id=cid, image_id=image, expected_exit=1 if rejected else 0)
    finally:
        cleanup_fixture(cleanup, cid)
    return {"image_id": image, "container_id": cid, "lean_version": version,
            "lake_version": lake_version, "compiler_output": output.decode("ascii"),
            "cleanup_status": "removed_verified", **state}


def trace_command(command: list[str], trace: Path, *, cwd: Path, env: dict,
                  measurement_only=False) -> bytes:
    # Fixed trusted executables/sources only, never a draft or client argument.
    byte_limit = MEASUREMENT_TRACE_BYTES if measurement_only else MAX_TRACE_BYTES
    args = ["/usr/bin/prlimit", "--fsize=" + str(byte_limit), "--",
            "/usr/bin/strace", "-ff", "-qq", "-yy", "-s", "4096", "-e", "trace=openat",
            "-o", str(trace), *command]
    # File-backed output is bounded by prlimit and never accumulated unboundedly in RAM.
    with tempfile.TemporaryFile() as output, tempfile.TemporaryFile() as diagnostic:
        process = subprocess.Popen(args, cwd=cwd, env=env, stdin=subprocess.DEVNULL,
                                   stdout=output, stderr=diagnostic, start_new_session=True)
        try:
            code = process.wait(timeout=120)
        except BaseException:
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            process.wait(timeout=5)
            raise
        output.seek(0)
        diagnostic.seek(0)
        raw = output.read(policy.MAX_OUTPUT_BYTES + 1)
        error = diagnostic.read(16001)
    if code or len(raw) > policy.MAX_OUTPUT_BYTES or len(error) > 16000:
        raise ValueError(f"Trusted dependency observation failed (exit={code}, "
                         f"stdout_bytes={len(raw)}, stderr_bytes={len(error)}): "
                         + error[:1800].decode(errors="replace"))
    return raw


def main() -> int:
    if os.name != "posix" or not Path("/proc/sys/kernel").is_dir():
        raise ValueError("The trusted offline fixture requires Linux CI, not a client runtime")
    lean_root = Path(__file__).resolve().parents[1] / "lean"
    sha = os.environ.get("GITHUB_SHA", "")
    source_report = sources.inspect_sources(lean_root, expected_sha=sha)
    archive = Path(os.environ["RUNNER_TEMP"]) / "atlas-lean-4.26.0-linux.tar.zst"
    core.verify_archive(archive)
    lock = sources.validate_lock(sources.read_json(lean_root / "mathlib-source-lock.json"))
    packages = {name: (lean_root / ".lake/packages" / name).resolve(strict=True) for name in lock}
    with tempfile.TemporaryDirectory(prefix="atlas-offline-") as directory:
        work = Path(directory)
        subprocess.run(["tar", "--zstd", "-xf", str(archive), "-C", directory], check=True, timeout=180)
        toolchain = work / "lean-4.26.0-linux"
        fixture = work / "Fixture.lean"
        fixture.write_text(SOURCE, encoding="utf-8")
        path = ":".join(str(root / ".lake/build/lib/lean") for root in packages.values())
        observe_env = {"PATH": str(toolchain / "bin") + ":/usr/bin:/bin", "HOME": "/tmp",
                       "LANG": "C", "LEAN_NUM_THREADS": "1", "LEAN_PATH": path}
        lean, lake = toolchain / "bin/lean", toolchain / "bin/lake"
        version = trace_command([str(lean), "--version"], work / "lean-trace", cwd=work, env=observe_env)
        core.validate_version(version.decode("ascii").strip())
        lake_version = validate_lake(trace_command([str(lake), "--version"], work / "lake-trace", cwd=work, env=observe_env))
        output = trace_command([str(lean), str(fixture)], work / "fixture-trace", cwd=work, env=observe_env)
        core.validate_output(version + output)
        traces = list(work.glob("*-trace.*"))
        if not 1 <= len(traces) <= MAX_TRACE_FILES or sum(p.stat().st_size for p in traces) > MAX_TRACE_BYTES:
            raise ValueError("Aggregate dependency trace budget exceeded")
        paths = {lean, lake, Path("/bin/busybox")}
        observed = set()
        for trace in traces:
            with trace.open("rb") as handle:
                observed.update(parse_trace(handle.read(MAX_TRACE_BYTES + 1), cwd=work, allow_empty=True))
        if not observed:
            raise ValueError('No successful dependency reads were observed')
        paths.update(observed)
        for binary in (lean, lake):
            paths.update(elf_dependencies(subprocess.check_output(
                ["/usr/bin/ldd", str(binary)], env=observe_env, timeout=15)))
        context = work / "context"
        rootfs = context / "rootfs"
        rootfs.mkdir(parents=True)
        origins = stage(paths, rootfs, toolchain, packages, fixture)
        atlas = rootfs / "opt/atlas"
        atlas.mkdir(parents=True)
        (atlas / "Fixture.lean").write_text(SOURCE, encoding="utf-8")
        (atlas / "run-draft").write_text(entry_script(packages), encoding="ascii")
        (atlas / "run-draft").chmod(0o755)
        (rootfs / "tmp").mkdir(mode=0o1777)
        (context / "Dockerfile").write_text(core.DOCKERFILE, encoding="ascii")
        config = work / "docker-config"
        config.mkdir(mode=0o700)
        prefix = [str(transport._DOCKER), "--host", "unix://" + str(transport._local_socket()), "--config", str(config)]
        env = {"PATH": "/usr/bin:/bin", "HOME": directory, "LANG": "C"}
        def run_case(case_origins, *, rejected):
            manifest = artifacts.create_manifest(rootfs, source_report)
            raw = artifacts.encoded(manifest)
            digest = hashlib.sha256(raw).hexdigest()
            verification = artifacts.verify_manifest(rootfs, raw, expected_sha256=digest,
                                                      expected_source_report=source_report)
            iid = work / ('rejected-image-id' if rejected else 'image-id')
            subprocess.run(prefix + ['build', '--network=none', '--pull=false', '--iidfile', str(iid), str(context)],
                           check=True, timeout=360, stdin=subprocess.DEVNULL, env={**env, 'DOCKER_BUILDKIT': '0'})
            image = iid.read_text(encoding='ascii').strip()
            if not policy._IMAGE.fullmatch(image):
                raise ValueError('Invalid offline fixture image ID')
            try:
                # Compare actual bytes immediately before container admission.
                artifacts.verify_manifest(rootfs, raw, expected_sha256=digest, expected_source_report=source_report)
                result = check_image(prefix, env, image, lake_version, rejected=rejected)
            finally:
                transport._command(prefix, ('image', 'rm', image), env)
            report = {'schema': 1, 'status': 'trusted_mathlib_fixture_offline_compiled', 'checkout_sha': sha,
                      'source_sha256': hashlib.sha256(SOURCE.encode()).hexdigest(),
                      'archive_sha256': core.ARCHIVE_SHA256, 'manifest_sha256': digest,
                      'file_count': verification['file_count'], 'total_bytes': verification['total_bytes'],
                      'observed_origin_count': len(case_origins), 'execution_allowed': False,
                      'offline_ready': False, 'proof_status': 'not_run', 'certificate': False, **result}
            if rejected:
                report.update(status='trusted_mathlib_fixture_missing_import_rejected', missing_import=MISSING_IMPORT)
            validate_report(report, manifest, case_origins, expected_sha=sha,
                            expected_manifest_sha=digest, rejected=rejected)
            return report, manifest, case_origins

        positive = run_case(origins, rejected=False)
        if MISSING_IMPORT not in origins:
            raise ValueError('Required import was not present in the successful observed bundle')
        (rootfs / MISSING_IMPORT).unlink()
        negative = run_case({p: o for p, o in origins.items() if p != MISSING_IMPORT}, rejected=True)
        validate_report_pair(positive, negative, expected_sha=sha,
                             expected_manifest_sha=positive[0]['manifest_sha256'],
                             expected_rejected_manifest_sha=negative[0]['manifest_sha256'])
        for evidence, prefix_name, marker in (
                (positive, 'atlas-mathlib-offline-', 'ATLAS_MATHLIB_OFFLINE_FIXTURE'),
                (negative, 'atlas-mathlib-offline-rejected-', 'ATLAS_MATHLIB_OFFLINE_REJECTED')):
            for name, payload in zip(('report', 'manifest', 'origins'), evidence):
                target = Path(os.environ['RUNNER_TEMP']) / (prefix_name + name + '.json')
                with target.open('xb') as handle:
                    handle.write(artifacts.encoded(payload))
            print(marker + ' ' + json.dumps(evidence[0], sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--validate-report', type=Path)
    parser.add_argument('--manifest', type=Path)
    parser.add_argument('--origins', type=Path)
    parser.add_argument('--expected-manifest-sha256')
    parser.add_argument('--validate-report-pair', action='store_true')
    parser.add_argument('--evidence-directory', type=Path)
    parser.add_argument('--expected-rejected-manifest-sha256')
    args = parser.parse_args()
    if args.validate_report_pair:
        if not all((args.evidence_directory, args.expected_manifest_sha256, args.expected_rejected_manifest_sha256)):
            parser.error('Pair validation requires evidence directory and both independently captured digests')
        def evidence(prefix):
            return tuple(read_evidence(args.evidence_directory / (prefix + name + '.json'))
                         for name in ('report', 'manifest', 'origins'))
        validate_report_pair(evidence('atlas-mathlib-offline-'), evidence('atlas-mathlib-offline-rejected-'),
                             expected_sha=os.environ.get('GITHUB_SHA', ''),
                             expected_manifest_sha=args.expected_manifest_sha256,
                             expected_rejected_manifest_sha=args.expected_rejected_manifest_sha256)
        print('ATLAS_MATHLIB_OFFLINE_REPORT_PAIR_VALIDATED')
    elif args.validate_report:
        if not all((args.manifest, args.origins, args.expected_manifest_sha256)):
            parser.error('Validation requires manifest, origins and independently captured manifest digest')
        raw = read_evidence(args.manifest)
        # Canonical persisted bytes: the expected digest is a separate CI input.
        if hashlib.sha256(artifacts.encoded(raw)).hexdigest() != args.expected_manifest_sha256:
            raise ValueError('Persisted manifest digest mismatch')
        validate_report(read_evidence(args.validate_report), raw, read_evidence(args.origins),
                        expected_sha=os.environ.get('GITHUB_SHA', ''), expected_manifest_sha=args.expected_manifest_sha256)
        print('ATLAS_MATHLIB_OFFLINE_REPORT_VALIDATED')
    else:
        raise SystemExit(main())
