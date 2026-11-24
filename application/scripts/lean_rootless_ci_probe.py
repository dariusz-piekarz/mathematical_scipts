"""Real Docker rootless preflight on a dedicated CI host, using a fixed fixture.

No Lean, untrusted payload, registry access or user-provided code. The fixture
image is constructed from a system static BusyBox with a harmless entrypoint.
This script checks configuration only; it never starts a container.
"""
from __future__ import annotations

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

from backend import lean_draft_transport as transport


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
        # Entry point is deliberately a fixed no-op; probe must not execute it.
        entry = context / "run-draft"
        entry.write_text("#!/bin/busybox sh\nexit 0\n", encoding="utf-8")
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
            return 0
        finally:
            transport._command(prefix, ("image", "rm", image_id), env)


if __name__ == "__main__":
    sys.exit(main())
