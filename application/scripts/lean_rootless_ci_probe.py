"""Real Docker rootless preflight on a dedicated CI host, using a fixed fixture.

No Lean, untrusted payload, registry access or user-provided code. The fixture
image is constructed from a system static BusyBox with a harmless entrypoint.
The preflight remains configuration-only. A separate CI-only runtime probe
starts the fixed harmless fixture to read actual cgroup limits.
"""
from __future__ import annotations

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import uuid

from backend import lean_draft_transport as transport
from backend import lean_draft_runner as policy



# Fixed fixture: no input, no user code, no network or resource stress.
_FIXTURE = """#!/bin/busybox sh
set -eu
for key in memory.max memory.swap.max pids.max cpu.max; do
    value=$(/bin/busybox cat "/sys/fs/cgroup/$key")
    printf '%s=%s\\n' "$key" "$value"
done
"""


def validate_runtime_limits(output: bytes) -> dict:
    """Require actual cgroup v2 observations, not Docker inspect metadata."""
    expected = {"memory.max": str(policy.MEMORY_BYTES),
                "memory.swap.max": "0", "pids.max": str(policy.PIDS_LIMIT)}
    values = {}
    for line in output.decode("ascii").splitlines():
        key, sep, value = line.partition("=")
        if not sep or key in values:
            raise ValueError("Malformed or duplicate cgroup observation")
        values[key] = value
    if set(values) != set(expected) | {"cpu.max"}:
        raise ValueError("Missing or unexpected cgroup observation")
    if any(values[k] != v for k, v in expected.items()):
        raise ValueError("Actual memory, swap or PID limit differs from policy")
    fields = values["cpu.max"].split()
    if (len(fields) != 2 or any(not field.isascii() or not field.isdecimal() for field in fields)
            or int(fields[0]) <= 0 or int(fields[0]) != int(fields[1])):
        raise ValueError("Actual CPU quota differs from one CPU")
    return values


def check_runtime_limits(prefix: list[str], env: dict[str, str], image_id: str) -> dict:
    """CI only; never pass source, accept commands or enable draft execution."""
    def call(*args):
        return transport._command(prefix, args, env)

    transport.validate_engine(transport._decode_metadata(call("info", "--format", "{{json .}}")))
    policy.validate_image_inspection(transport._decode_metadata(call("image", "inspect", image_id)),
                                     approved_image_id=image_id)
    name = "atlas-draft-" + uuid.uuid4().hex
    raw_id = call(*policy.isolation_arguments(image_id=image_id, container_name=name))
    cid = raw_id.decode("ascii").strip()
    if not transport._CONTAINER_ID.fullmatch(cid):
        raise ValueError("Ambiguous runtime fixture creation: " + name)
    try:
        transport.validate_container(transport._decode_metadata(call("container", "inspect", cid)),
                                     container_id=cid, image_id=image_id, name=name)
        values = validate_runtime_limits(call("container", "start", "--attach", cid))
        records = transport._decode_metadata(call("container", "inspect", cid))
        if (type(records) is not list or len(records) != 1 or type(records[0]) is not dict
                or records[0].get("Id") != cid or records[0].get("Image") != image_id):
            raise ValueError("Runtime fixture identity mismatch")
        state = records[0].get("State")
        if (type(state) is not dict or state.get("Status") != "exited"
                or state.get("Running") is not False or type(state.get("ExitCode")) is not int
                or state["ExitCode"] != 0 or state.get("OOMKilled") is not False):
            raise ValueError("Runtime fixture did not exit cleanly")
    finally:
        # Kill/remove by exact ID even if the local CLI timed out.
        # An unsuccessful removal is a failed test, never a success report.
        call("container", "rm", "--force", cid)
    return {"status": "runtime_limits_checked", "observations": values,
            "image_id": image_id, "cleanup_status": "removed",
            "execution_allowed": False, "proof_status": "not_run", "certificate": False}


def main() -> int:
    socket = transport._local_socket()
    with tempfile.TemporaryDirectory(prefix="atlas-rootless-fixture-") as directory:
        root = Path(directory)
        context = root / "context"
        context.mkdir()
        config = root / "config"
        config.mkdir(mode=0o700)
        busybox = Path("/bin/busybox")
        if not busybox.is_file():
            raise RuntimeError("Missing system busybox-static fixture")
        shutil.copyfile(busybox, context / "busybox")
        (context / "busybox").chmod(0o755)
        # Fixed read-only observations; the configuration preflight never starts it.
        entry = context / "run-draft"
        entry.write_text(_FIXTURE, encoding="utf-8")
        entry.chmod(0o755)
        (context / "Dockerfile").write_text(
            "FROM scratch\n"
            "COPY busybox /bin/busybox\n"
            "COPY run-draft /opt/atlas/run-draft\n"
            "ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\n"
            "ENV HOME=/tmp LEAN_NUM_THREADS=1\n"
            "USER 65534:65534\n"
            "WORKDIR /tmp\n"
            'ENTRYPOINT ["/opt/atlas/run-draft"]\n',
            encoding="utf-8",
        )
        prefix = [str(transport._DOCKER), "--host", "unix://" + str(socket),
                  "--config", str(config)]
        env = {"PATH": "/usr/bin:/bin", "HOME": directory, "LANG": "C"}
        info = transport._decode_metadata(transport._command(
            prefix, ("info", "--format", "{{json .}}"), env))
        transport.validate_engine(info)
        iid = root / "image-id"
        subprocess.run(prefix + ["build", "--network=none", "--pull=false",
                                 "--iidfile", str(iid), str(context)],
                       env={**env, "DOCKER_BUILDKIT": "0"}, stdin=subprocess.DEVNULL,
                       check=True, timeout=120)
        image_id = iid.read_text(encoding="ascii").strip()
        try:
            result = transport.probe(image_id)
            print("ATLAS_ROOTLESS_PREFLIGHT " + json.dumps(result, sort_keys=True), flush=True)
            if (result.get("status") != "configuration_checked"
                    or result.get("cleanup_status") != "removed"
                    or result.get("execution_allowed") is not False
                    or result.get("proof_status") != "not_run"
                    or result.get("certificate") is not False):
                return 1
            runtime = check_runtime_limits(prefix, env, image_id)
            print("ATLAS_ROOTLESS_RUNTIME " + json.dumps(runtime, sort_keys=True), flush=True)
            return 0
        finally:
            transport._command(prefix, ("image", "rm", image_id), env)


if __name__ == "__main__":
    sys.exit(main())
