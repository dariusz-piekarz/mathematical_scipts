"""CI-only fixed Lean core fixture in the existing rootless isolation policy.

No input from users, no application endpoint, no permission to run drafts.
The official archive is fetched on the host and verified before extraction.
Host dynamic libraries are part of this CI image, not a portable locked base.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import uuid

from backend import lean_draft_runner as policy
from backend import lean_draft_transport as transport
from scripts.lean_rootless_ci_probe import (
    cleanup_fixture, validate_exited_fixture, _read_report_json, MAX_REPORT_BYTES,
)

LEAN_VERSION = "4.26.0"
LEAN_COMMIT = "d8204c9fd894f91bbb2cdfec5912ec8196fd8562"
ARCHIVE_SHA256 = "873c252b1c6b1392e5720ad8d5a137aabbe72c9f96a930fdb5a1dd1ddc5da454"
ARCHIVE_SIZE = 502305727
SOURCE = """theorem atlas_isolated_fixture (p : Prop) : p → p := by
  intro h
  exact h
#print axioms atlas_isolated_fixture
"""
REJECTED_SOURCE = """theorem atlas_isolated_rejected : False := by
  exact True.intro
"""
ENTRY = """#!/bin/busybox sh
set -eu
/opt/lean/bin/lean --version
/opt/lean/bin/lean /opt/atlas/Fixture.lean
"""
DOCKERFILE = """FROM scratch
COPY rootfs /
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV HOME=/tmp LEAN_NUM_THREADS=1
USER 65534:65534
WORKDIR /tmp
ENTRYPOINT ["/opt/atlas/run-draft"]
"""


def verify_archive(path: Path) -> None:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        if os.fstat(handle.fileno()).st_size != ARCHIVE_SIZE:
            raise ValueError("Unexpected Lean archive size")
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    if h.hexdigest() != ARCHIVE_SHA256:
        raise ValueError("Lean release digest mismatch")


def validate_version(line: str) -> str:
    match = re.fullmatch(
        r"Lean \(version 4\.26\.0, x86_64-unknown-linux-gnu, commit ([0-9a-f]{7,40}), Release\)",
        line)
    if not match or not LEAN_COMMIT.startswith(match.group(1)):
        raise ValueError("Unexpected fixed Lean compiler identity")
    return line


def validate_output(output: bytes) -> str:
    lines = output.decode("ascii").splitlines()
    if len(lines) != 2 or lines[1] != "'atlas_isolated_fixture' does not depend on any axioms":
        raise ValueError("Unexpected fixed Lean compiler evidence")
    return validate_version(lines[0])


def validate_rejected_output(output: bytes) -> str:
    version, sep, diagnostic = output.decode("ascii").partition("\n")
    # Fixed source, exactly one diagnostic: True.intro cannot prove False.
    # Allow whitespace and the precise diagnostic column to vary, not the
    # error location, error class or the two types.
    if not sep or not re.fullmatch(
            r"/opt/atlas/Fixture\.lean:2:[0-9]+: error: [Tt]ype mismatch"
            r"\s+True\.intro\s+has type\s+True\s+but is expected to have type\s+False",
            diagnostic.rstrip("\n")):
        raise ValueError("Unexpected fixed Lean rejection diagnostic")
    return validate_version(version)


def check_compiler(prefix: list[str], env: dict[str, str], image_id: str, *, rejected: bool = False) -> dict:
    def call(*args):
        return transport._command(prefix, args, env)

    transport.validate_engine(transport._decode_metadata(call("info", "--format", "{{json .}}")))
    policy.validate_image_inspection(transport._decode_metadata(call("image", "inspect", image_id)),
                                     approved_image_id=image_id)
    name = "atlas-draft-" + uuid.uuid4().hex
    cid = call(*policy.isolation_arguments(image_id=image_id, container_name=name)).decode("ascii").strip()
    if not transport._CONTAINER_ID.fullmatch(cid):
        raise ValueError("Ambiguous fixed Lean fixture creation: " + name)
    cleanup_call = transport.deferred_cleanup_command(prefix, env)
    try:
        transport.validate_container(transport._decode_metadata(call("container", "inspect", cid)),
                                     container_id=cid, image_id=image_id, name=name)
        if rejected:
            try:
                transport._command(prefix, ("container", "start", "--attach", cid), env,
                                   capture_failure=True)
            except transport.DockerCommandFailed as exc:
                if type(exc.returncode) is not int or exc.returncode != 1 or type(exc.output) is not bytes:
                    raise ValueError("Expected bounded Lean rejection with CLI exit 1") from exc
                output = exc.output
                version = validate_rejected_output(output)
            else:
                raise ValueError("Invalid fixed Lean proof unexpectedly accepted")
        else:
            output = call("container", "start", "--attach", cid)
            version = validate_output(output)
        state = validate_exited_fixture(
            transport._decode_metadata(cleanup_call("container", "inspect", cid)),
            container_id=cid, image_id=image_id, expected_exit=1 if rejected else 0)
    finally:
        cleanup_fixture(cleanup_call, cid)
    return {"status": "trusted_core_fixture_rejected" if rejected else "trusted_core_fixture_compiled",
            "lean_version": version,
            "compiler_output": output.decode("ascii"),
            "archive_sha256": ARCHIVE_SHA256, "source_sha256": hashlib.sha256((REJECTED_SOURCE if rejected else SOURCE).encode()).hexdigest(),
            "image_id": image_id, "container_id": cid, **state,
            "cleanup_status": "removed_verified", "execution_allowed": False,
            "proof_status": "not_run", "certificate": False}


def validate_report(report: object, *, expected_sha: str, rejected: bool = False) -> None:
    """Validate the exact scoped evidence; never treat it as a draft certificate."""
    fixed = {"status": "trusted_core_fixture_rejected" if rejected else "trusted_core_fixture_compiled",
             "checkout_sha": expected_sha, "archive_sha256": ARCHIVE_SHA256,
             "source_sha256": hashlib.sha256((REJECTED_SOURCE if rejected else SOURCE).encode()).hexdigest(),
             "container_state": "exited", "exit_code": 1 if rejected else 0,
             "cleanup_status": "removed_verified", "execution_allowed": False,
             "proof_status": "not_run", "certificate": False}
    variable = {"lean_version", "compiler_output", "image_id", "container_id"}
    if (type(expected_sha) is not str or not re.fullmatch(r"[0-9a-f]{40}", expected_sha)
            or type(report) is not dict or set(report) != set(fixed) | variable
            or any(type(report[k]) is not type(v) or report[k] != v for k, v in fixed.items())
            or any(type(report[k]) is not str for k in variable)
            or not policy._IMAGE.fullmatch(report["image_id"])
            or not transport._CONTAINER_ID.fullmatch(report["container_id"])):
        raise ValueError("Invalid fixed Lean fixture report")
    output = report["compiler_output"].encode("ascii")
    validator = validate_rejected_output if rejected else validate_output
    if len(output) > transport.MAX_METADATA_BYTES or validator(output) != report["lean_version"]:
        raise ValueError("Inconsistent fixed Lean compiler evidence")


def read_report(path: Path, *, expected_sha: str, rejected: bool = False) -> dict:
    report = _read_report_json(path)
    validate_report(report, expected_sha=expected_sha, rejected=rejected)
    return report


def validate_report_pair(positive: object, negative: object, *, expected_sha: str) -> None:
    """Both separately valid records must describe distinct executions."""
    validate_report(positive, expected_sha=expected_sha)
    validate_report(negative, expected_sha=expected_sha, rejected=True)
    if (positive["image_id"] == negative["image_id"]
            or positive["container_id"] == negative["container_id"]):
        raise ValueError("Positive and negative fixture identities must differ")
    if positive["lean_version"] != negative["lean_version"]:
        raise ValueError("Positive and negative compiler identities must agree")


def read_report_pair(positive_path: Path, negative_path: Path, *, expected_sha: str) -> tuple[dict, dict]:
    positive = read_report(positive_path, expected_sha=expected_sha)
    negative = read_report(negative_path, expected_sha=expected_sha, rejected=True)
    validate_report_pair(positive, negative, expected_sha=expected_sha)
    return positive, negative


def write_report(path: Path, report: dict, *, expected_sha: str, rejected: bool = False) -> None:
    validate_report(report, expected_sha=expected_sha, rejected=rejected)
    raw = (json.dumps(report, sort_keys=True, ensure_ascii=True, allow_nan=False) + "\n").encode("ascii")
    if len(raw) > MAX_REPORT_BYTES:
        raise ValueError("Fixed Lean report exceeds byte limit")
    with path.open("xb") as handle:
        handle.write(raw)
    if read_report(path, expected_sha=expected_sha, rejected=rejected) != report:
        raise ValueError("Fixed Lean report serialization mismatch")


def stage_host_libraries(toolchain: Path, rootfs: Path) -> None:
    """Copy actual transitive ELF dependencies from the dedicated CI host.

    ldd is used only on the verified official compiler, never a user binary.
    Reject unresolved dependencies and unexpected dependency paths.
    """
    raw = subprocess.check_output(
        ["/usr/bin/ldd", str(toolchain / "bin/lean")],
        env={"PATH": "/usr/bin:/bin", "LANG": "C"}, timeout=15).decode("ascii")
    for line in raw.splitlines():
        line = line.strip()
        if line.startswith("linux-vdso.so.1 "):
            continue
        m = re.fullmatch(r"(?:\S+ => )?(/\S+) \(0x[0-9a-f]+\)", line)
        if not m:
            raise ValueError("Unresolved or unexpected ELF dependency")
        source = Path(m.group(1))
        if source.is_relative_to(toolchain):
            continue  # complete official lib directory is already copied
        if not source.is_relative_to("/lib") and not source.is_relative_to("/lib64") \
                and not source.is_relative_to("/usr/lib"):
            raise ValueError("Unexpected host library location")
        dest = rootfs / source.relative_to("/")
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, dest)


def main() -> int:
    checkout = Path(__file__).resolve().parents[2]
    sha = os.environ.get("GITHUB_SHA", "")
    if not re.fullmatch(r"[0-9a-f]{40}", sha) or subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=checkout, timeout=5).decode().strip() != sha:
        raise ValueError("CI checkout identity mismatch")
    if (checkout / "application/lean/lean-toolchain").read_text().strip() != "leanprover/lean4:v" + LEAN_VERSION:
        raise ValueError("Fixed fixture toolchain differs from project pin")
    archive = Path(os.environ["RUNNER_TEMP"]) / "atlas-lean-4.26.0-linux.tar.zst"
    verify_archive(archive)
    socket = transport._local_socket()
    with tempfile.TemporaryDirectory(prefix="atlas-core-fixture-") as directory:
        root = Path(directory)
        subprocess.run(["tar", "--zstd", "-xf", str(archive), "-C", directory],
                       check=True, timeout=180)
        toolchain = root / "lean-4.26.0-linux"
        context = root / "context"
        rootfs = context / "rootfs"
        (rootfs / "opt/lean/bin").mkdir(parents=True)
        shutil.copy2(toolchain / "bin/lean", rootfs / "opt/lean/bin/lean")
        shutil.copytree(toolchain / "lib", rootfs / "opt/lean/lib", symlinks=True)
        stage_host_libraries(toolchain, rootfs)
        (rootfs / "bin").mkdir(exist_ok=True)
        shutil.copy2("/bin/busybox", rootfs / "bin/busybox")
        atlas = rootfs / "opt/atlas"
        atlas.mkdir()
        fixture = atlas / "Fixture.lean"
        fixture.write_text(SOURCE, encoding="utf-8")
        entry = atlas / "run-draft"
        entry.write_text(ENTRY, encoding="utf-8")
        entry.chmod(0o755)
        (context / "Dockerfile").write_text(DOCKERFILE, encoding="ascii")
        config = root / "config"
        config.mkdir(mode=0o700)
        prefix = [str(transport._DOCKER), "--host", "unix://" + str(socket),
                  "--config", str(config)]
        env = {"PATH": "/usr/bin:/bin", "HOME": directory, "LANG": "C"}
        transport.validate_engine(transport._decode_metadata(transport._command(
            prefix, ("info", "--format", "{{json .}}"), env)))
        def run_case(*, rejected: bool) -> dict:
            iid = root / ("rejected-image-id" if rejected else "image-id")
            fixture.write_text(REJECTED_SOURCE if rejected else SOURCE, encoding="utf-8")
            subprocess.run(prefix + ["build", "--network=none", "--pull=false", "--iidfile",
                                     str(iid), str(context)], check=True, timeout=360,
                           stdin=subprocess.DEVNULL, env={**env, "DOCKER_BUILDKIT": "0"})
            image_id = iid.read_text(encoding="ascii").strip()
            if not policy._IMAGE.fullmatch(image_id):
                raise ValueError("Invalid immutable fixture image ID")
            try:
                return check_compiler(prefix, env, image_id, rejected=rejected)
            finally:
                transport._command(prefix, ("image", "rm", image_id), env)
        result = run_case(rejected=False)
        rejection = run_case(rejected=True)
    report = {**result, "checkout_sha": sha}
    rejected_report = {**rejection, "checkout_sha": sha}
    validate_report_pair(report, rejected_report, expected_sha=sha)
    write_report(Path(os.environ["RUNNER_TEMP"]) / "atlas-rootless-lean-core.json",
                 report, expected_sha=sha)
    write_report(Path(os.environ["RUNNER_TEMP"]) / "atlas-rootless-lean-rejected.json",
                 rejected_report, expected_sha=sha, rejected=True)
    print("ATLAS_ROOTLESS_LEAN_CORE " + json.dumps(report, sort_keys=True), flush=True)
    print("ATLAS_ROOTLESS_LEAN_REJECTED " + json.dumps(rejected_report, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--validate-report":
        read_report(Path(sys.argv[2]), expected_sha=os.environ.get("GITHUB_SHA", ""))
        print("ATLAS_ROOTLESS_LEAN_CORE_REPORT_VALIDATED", flush=True)
    elif len(sys.argv) == 3 and sys.argv[1] == "--validate-rejected-report":
        read_report(Path(sys.argv[2]), expected_sha=os.environ.get("GITHUB_SHA", ""), rejected=True)
        print("ATLAS_ROOTLESS_LEAN_REJECTED_REPORT_VALIDATED", flush=True)
    elif len(sys.argv) == 4 and sys.argv[1] == "--validate-report-pair":
        read_report_pair(Path(sys.argv[2]), Path(sys.argv[3]),
                         expected_sha=os.environ.get("GITHUB_SHA", ""))
        print("ATLAS_ROOTLESS_LEAN_CORE_REPORT_VALIDATED", flush=True)
        print("ATLAS_ROOTLESS_LEAN_REJECTED_REPORT_VALIDATED", flush=True)
        print("ATLAS_ROOTLESS_LEAN_REPORT_PAIR_VALIDATED", flush=True)
    elif len(sys.argv) == 1:
        raise SystemExit(main())
    else:
        raise SystemExit("Unexpected CI fixture arguments")
