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
MAX_TRACE_BYTES = 16 * 1024 * 1024
MAX_TRACE_FILES = 128
SYSTEM_ROOTS = tuple(map(PurePosixPath, ("/lib", "/lib64", "/usr/lib")))
SYSTEM_FILES = set(map(PurePosixPath, ("/etc/ld.so.cache", "/etc/locale.alias", "/etc/localtime", "/bin/busybox", "/usr/bin/busybox", "/usr/share/zoneinfo/Etc/UTC")))
KERNEL_ROOTS = tuple(map(PurePosixPath, ("/proc", "/sys", "/dev")))
OPEN = re.compile(r'^(?:\d+\s+)?openat\((AT_FDCWD|\d+<(/[^>]*)>), '
                  r'("(?:[^"\\]|\\.)*"), ([^\n]*)\)\s+=\s+(\d+)<(/[^>]+)>$')


def normalized(path: str) -> PurePosixPath:
    if not path.startswith("/") or path.startswith("//") or "\x00" in path or "\\" in path:
        raise ValueError("Expected absolute Linux dependency path")
    value = PurePosixPath(posixpath.normpath(path))
    for name in PurePosixPath(value.as_posix()).parts[1:]:
        artifacts.component(name)
    return value


def parse_trace(raw: bytes, *, cwd: Path) -> set[Path]:
    """Accept only complete, decoded, read-only successful openat records."""
    if len(raw) > MAX_TRACE_BYTES:
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
            raise ValueError("Incomplete or unexpected dependency trace")
        directory, base, quoted, flags, _, resolved = match.groups()
        if any(token in flags for token in ("O_WRONLY", "O_RDWR", "O_CREAT", "O_TRUNC")):
            raise ValueError("Unexpected write in dependency trace")
        requested = ast.literal_eval(quoted)
        if type(requested) is not str:
            raise ValueError("Invalid dependency path literal")
        if not requested.startswith("/"):
            requested = str((PurePosixPath(cwd) if directory == "AT_FDCWD" else PurePosixPath(base)) / requested)
        requested_path = normalized(requested)
        normalized(resolved)  # Reject deleted descriptors and nonportable names.
        paths.add(requested_path)
        if len(paths) > artifacts.MAX_ENTRIES:
            raise ValueError("Dependency trace entry budget exceeded")
    if not paths:
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


def destination(path: Path, toolchain: Path, packages: dict[str, Path]) -> Path:
    path = normalized(str(path))
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


def validate_report(report, manifest, origins, *, expected_sha, expected_manifest_sha):
    """Check persisted consistency, not authenticity or general offline readiness."""
    fixed = {"schema": 1, "status": "trusted_mathlib_fixture_offline_compiled", "checkout_sha": expected_sha,
             "source_sha256": hashlib.sha256(SOURCE.encode()).hexdigest(), "archive_sha256": core.ARCHIVE_SHA256,
             "manifest_sha256": expected_manifest_sha, "execution_allowed": False, "offline_ready": False,
             "certificate": False, "proof_status": "not_run", "container_state": "exited", "exit_code": 0,
             "cleanup_status": "removed_verified"}
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
    if (not isinstance(report['image_id'], str) or not policy._IMAGE.fullmatch(report['image_id'])
            or not isinstance(report['container_id'], str) or not transport._CONTAINER_ID.fullmatch(report['container_id'])):
        raise ValueError("Invalid isolated execution identity")
    output = report['compiler_output']
    if type(output) is not str or len(output) > transport.MAX_METADATA_BYTES:
        raise ValueError("Invalid compiler evidence")
    lake, separator, rest = output.partition('\n')
    if (not separator or validate_lake(lake.encode()) != report['lake_version']
            or core.validate_output(rest.encode()) != report['lean_version']):
        raise ValueError("Inconsistent compiler evidence")


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


def check_image(prefix: list[str], env: dict[str, str], image: str, lake_version: str) -> dict:
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
        output = call("container", "start", "--attach", cid)
        first, sep, rest = output.partition(b"\n")
        if not sep or first.decode("ascii") != lake_version:
            raise ValueError("Isolated Lake version differs from prepared tool")
        version = core.validate_output(rest)
        state = validate_exited_fixture(
            transport._decode_metadata(cleanup("container", "inspect", cid)),
            container_id=cid, image_id=image, expected_exit=0)
    finally:
        cleanup_fixture(cleanup, cid)
    return {"image_id": image, "container_id": cid, "lean_version": version,
            "lake_version": lake_version, "compiler_output": output.decode("ascii"),
            "cleanup_status": "removed_verified", **state}


def trace_command(command: list[str], trace: Path, *, cwd: Path, env: dict) -> bytes:
    # Fixed trusted executables/sources only, never a draft or client argument.
    args = ["/usr/bin/prlimit", "--fsize=" + str(MAX_TRACE_BYTES), "--",
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
        raise ValueError("Trusted dependency observation failed: " + error[:2000].decode(errors="replace"))
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
        for trace in traces:
            with trace.open("rb") as handle:
                paths.update(parse_trace(handle.read(MAX_TRACE_BYTES + 1), cwd=work))
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
        manifest = artifacts.create_manifest(rootfs, source_report)
        raw = artifacts.encoded(manifest)
        manifest_sha = hashlib.sha256(raw).hexdigest()
        verification = artifacts.verify_manifest(rootfs, raw, expected_sha256=manifest_sha,
                                                  expected_source_report=source_report)
        (context / "Dockerfile").write_text(core.DOCKERFILE, encoding="ascii")
        config = work / "docker-config"
        config.mkdir(mode=0o700)
        prefix = [str(transport._DOCKER), "--host", "unix://" + str(transport._local_socket()), "--config", str(config)]
        env = {"PATH": "/usr/bin:/bin", "HOME": directory, "LANG": "C"}
        iid = work / "image-id"
        subprocess.run(prefix + ["build", "--network=none", "--pull=false", "--iidfile", str(iid), str(context)],
                       check=True, timeout=360, stdin=subprocess.DEVNULL, env={**env, "DOCKER_BUILDKIT": "0"})
        image = iid.read_text(encoding="ascii").strip()
        if not policy._IMAGE.fullmatch(image):
            raise ValueError("Invalid offline fixture image ID")
        try:
            # Compare actual bytes immediately before container admission.
            artifacts.verify_manifest(rootfs, raw, expected_sha256=manifest_sha, expected_source_report=source_report)
            result = check_image(prefix, env, image, lake_version)
        finally:
            transport._command(prefix, ("image", "rm", image), env)
        report = {"schema": 1, "status": "trusted_mathlib_fixture_offline_compiled", "checkout_sha": sha,
                  "source_sha256": hashlib.sha256(SOURCE.encode()).hexdigest(),
                  "archive_sha256": core.ARCHIVE_SHA256, "manifest_sha256": manifest_sha,
                  "file_count": verification["file_count"], "total_bytes": verification["total_bytes"],
                  "observed_origin_count": len(origins), "execution_allowed": False,
                  "offline_ready": False, "proof_status": "not_run", "certificate": False, **result}
        validate_report(report, manifest, origins, expected_sha=sha, expected_manifest_sha=manifest_sha)
        for name, payload in (("manifest", manifest), ("origins", origins), ("report", report)):
            target = Path(os.environ["RUNNER_TEMP"]) / ("atlas-mathlib-offline-" + name + ".json")
            with target.open("xb") as handle:
                handle.write(artifacts.encoded(payload))
        print("ATLAS_MATHLIB_OFFLINE_FIXTURE " + json.dumps(report, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--validate-report', type=Path)
    parser.add_argument('--manifest', type=Path)
    parser.add_argument('--origins', type=Path)
    parser.add_argument('--expected-manifest-sha256')
    args = parser.parse_args()
    if args.validate_report:
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
