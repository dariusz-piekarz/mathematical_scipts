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
import tempfile
import uuid

from backend import lean_draft_runner as policy
from backend import lean_draft_transport as transport
from scripts.lean_rootless_ci_probe import cleanup_fixture, validate_exited_fixture

LEAN_VERSION = "4.26.0"
ARCHIVE_SHA256 = "873c252b1c6b1392e5720ad8d5a137aabbe72c9f96a930fdb5a1dd1ddc5da454"
ARCHIVE_SIZE = 502305727
SOURCE = """theorem atlas_isolated_fixture (p : Prop) : p → p := by
  intro h
  exact h
#print axioms atlas_isolated_fixture
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


def validate_output(output: bytes) -> str:
    lines = output.decode("ascii").splitlines()
    if (len(lines) != 2 or not re.fullmatch(
            r"Lean \(version 4\.26\.0, x86_64-unknown-linux-gnu, commit [0-9a-f]{7,40}, Release\)", lines[0])
            or lines[1] != "'atlas_isolated_fixture' does not depend on any axioms"):
        raise ValueError("Unexpected fixed Lean compiler evidence")
    return lines[0]


def check_compiler(prefix: list[str], env: dict[str, str], image_id: str) -> dict:
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
        output = call("container", "start", "--attach", cid)
        version = validate_output(output)
        state = validate_exited_fixture(
            transport._decode_metadata(cleanup_call("container", "inspect", cid)),
            container_id=cid, image_id=image_id, expected_exit=0)
    finally:
        cleanup_fixture(cleanup_call, cid)
    return {"status": "trusted_core_fixture_compiled", "lean_version": version,
            "archive_sha256": ARCHIVE_SHA256, "source_sha256": hashlib.sha256(SOURCE.encode()).hexdigest(),
            "image_id": image_id, "container_id": cid, **state,
            "cleanup_status": "removed_verified", "execution_allowed": False,
            "proof_status": "not_run", "certificate": False}


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
        (atlas / "Fixture.lean").write_text(SOURCE, encoding="utf-8")
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
        iid = root / "image-id"
        subprocess.run(prefix + ["build", "--network=none", "--pull=false", "--iidfile",
                                 str(iid), str(context)], check=True, timeout=360,
                       stdin=subprocess.DEVNULL, env={**env, "DOCKER_BUILDKIT": "0"})
        image_id = iid.read_text(encoding="ascii").strip()
        if not policy._IMAGE.fullmatch(image_id):
            raise ValueError("Invalid immutable fixture image ID")
        try:
            result = check_compiler(prefix, env, image_id)
        finally:
            transport._command(prefix, ("image", "rm", image_id), env)
    print("ATLAS_ROOTLESS_LEAN_CORE " + json.dumps({**result, "checkout_sha": sha}, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
