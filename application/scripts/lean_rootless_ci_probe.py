"""Real Docker rootless preflight on a dedicated CI host, using a fixed fixture.

No Lean, untrusted payload, registry access or user-provided code. The fixture
image is constructed from a system static BusyBox with a harmless entrypoint.
The preflight remains configuration-only. A separate CI-only runtime probe
starts the fixed harmless fixture to observe cgroup limits and security flags.
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
    value=$(/bin/busybox cat "/sys/fs/cgroup/$key") || exit 20
    printf '%s=%s\\n' "$key" "$value"
done
# Observe the actual credentials and kernel flags of the fixture shell.
/bin/busybox awk '
    /^(Uid|Gid):/ {key=$1; sub(/:$/, "", key); printf "%s=%s %s %s %s\\n",key,$2,$3,$4,$5}
    /^(CapEff|NoNewPrivs|Seccomp):/ {key=$1; sub(/:$/, "", key); printf "%s=%s\\n",key,$2}
' "/proc/$$/status" || exit 21
/bin/busybox awk '
    $5 == "/" {print "root.mountopts=" $6}
    $5 == "/tmp" {print "tmp.mountopts=" $6}
' "/proc/$$/mountinfo" || exit 22
# The image file is world-writable by mode, so a permissions-only refusal
# is not enough. Require the actual read-only filesystem error.
mode=$(/bin/busybox stat -c %a /opt/atlas/write-check) || exit 23
test "$mode" = 666 || exit 24
if err=$(LC_ALL=C /bin/busybox touch /opt/atlas/write-check 2>&1); then
    exit 11
fi
case "$err" in
    *"Read-only file system"*) printf 'root.write=EROFS\\n' ;;
    *) exit 12 ;;
esac
# Require the actual mount ownership and private mode, independently of write success.
tmp_owner=$(/bin/busybox stat -c '%u:%g:%a' /tmp) || exit 28
printf 'tmp.owner_mode=%s\\n' "$tmp_owner"
test "$tmp_owner" = 65534:65534:700 || exit 29
printf 'atlas-runtime-fixture' > /tmp/atlas-write-check || exit 25
test "$(/bin/busybox cat /tmp/atlas-write-check)" = atlas-runtime-fixture || exit 26
/bin/busybox rm /tmp/atlas-write-check || exit 27
printf 'tmp.write=ok\\n'
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



def validate_runtime_security(output: bytes) -> dict:
    """Check observed credentials, kernel restrictions and filesystem probes."""
    values = {}
    for line in output.decode("ascii").splitlines():
        key, sep, value = line.partition("=")
        if not sep or key in values:
            raise ValueError("Malformed or duplicate security observation")
        values[key] = value
    exact = {"Uid": "65534 65534 65534 65534", "Gid": "65534 65534 65534 65534",
             "CapEff": "0000000000000000", "NoNewPrivs": "1", "Seccomp": "2",
             "root.write": "EROFS", "tmp.write": "ok",
             "tmp.owner_mode": "65534:65534:700"}
    if set(values) != set(exact) | {"root.mountopts", "tmp.mountopts"}:
        raise ValueError("Missing or unexpected security observation")
    if any(values[k] != v for k, v in exact.items()):
        raise ValueError("Runtime credentials, restrictions or write probes differ")
    root_opts = set(values["root.mountopts"].split(","))
    tmp_opts = set(values["tmp.mountopts"].split(","))
    if "ro" not in root_opts or "rw" in root_opts:
        raise ValueError("Root mount must be read-only")
    if not {"rw", "noexec", "nosuid", "nodev"} <= tmp_opts or tmp_opts & {"ro", "exec", "suid", "dev"}:
        raise ValueError("Unexpected runtime temporary mount options")
    return values


def validate_runtime_observations(output: bytes) -> dict:
    cgroup = []
    security = []
    for line in output.splitlines():
        if line.partition(b"=")[0] in {b"memory.max", b"memory.swap.max", b"pids.max", b"cpu.max"}:
            cgroup.append(line)
        else:
            security.append(line)
    return {**validate_runtime_limits(b"\n".join(cgroup)),
            **validate_runtime_security(b"\n".join(security))}



_FIXTURE_EXIT_STAGES = {
    11: "root_write_unexpected_success", 12: "root_write_not_readonly_error",
    20: "cgroup_read", 21: "process_status_read", 22: "mountinfo_read",
    23: "root_fixture_stat", 24: "root_fixture_mode", 25: "tmp_write",
    26: "tmp_readback", 27: "tmp_remove", 28: "tmp_stat", 29: "tmp_owner_mode",
}


def runtime_failure_report(records: object, *, container_id: str, image_id: str) -> dict:
    """Report only bounded, typed state of the fixed CI fixture; never declare success."""
    report = {"status": "blocked", "execution_allowed": False,
              "proof_status": "not_run", "certificate": False}
    if (type(records) is not list or len(records) != 1 or type(records[0]) is not dict
            or records[0].get("Id") != container_id or records[0].get("Image") != image_id):
        return {**report, "stage": "state_identity_unconfirmed"}
    state = records[0].get("State")
    if type(state) is not dict or type(state.get("ExitCode")) is not int:
        return {**report, "stage": "state_unconfirmed"}
    code = state["ExitCode"]
    status = state.get("Status")
    if type(status) is not str or status not in ("created", "running", "exited", "dead", "paused", "restarting", "removing"):
        status = "unknown"
    return {**report, "container_state": status, "exit_code": code,
            "stage": (_FIXTURE_EXIT_STAGES.get(code, "unclassified_fixture_failure")
                      if status == "exited" else "container_not_exited")}


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
        try:
            output = call("container", "start", "--attach", cid)
        except (OSError, ValueError, subprocess.SubprocessError):
            # The production CLI helper intentionally suppresses failed output.
            # Inspect the same fixed CI container before removing it, so a
            # failure is diagnosable without exposing arbitrary process output.
            try:
                failed = transport._decode_metadata(call("container", "inspect", cid))
                report = runtime_failure_report(failed, container_id=cid, image_id=image_id)
            except (OSError, ValueError, RecursionError, subprocess.SubprocessError):
                report = {"status": "blocked", "stage": "inspection_failed",
                          "execution_allowed": False, "proof_status": "not_run", "certificate": False}
            print("ATLAS_ROOTLESS_RUNTIME_FAILURE " + json.dumps(report, sort_keys=True), flush=True)
            raise
        try:
            values = validate_runtime_observations(output)
        except ValueError:
            # Fixed local fixture only; JSON-escaped and bounded by _command.
            print("ATLAS_ROOTLESS_RUNTIME_INVALID " + json.dumps({
                "status": "blocked", "observations_raw": output.decode("ascii", errors="replace")[:4096],
                "execution_allowed": False, "proof_status": "not_run", "certificate": False,
            }, sort_keys=True), flush=True)
            raise
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
    return {"status": "runtime_limits_and_security_checked", "observations": values,
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
        writable = context / "write-check"
        writable.write_bytes(b"fixed harmless fixture")
        writable.chmod(0o666)
        (context / "Dockerfile").write_text(
            "FROM scratch\n"
            "COPY busybox /bin/busybox\n"
            "COPY run-draft /opt/atlas/run-draft\n"
            "COPY write-check /opt/atlas/write-check\n"
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
