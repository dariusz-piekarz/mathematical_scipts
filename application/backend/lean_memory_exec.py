"""POSIX launch shim: set an address-space limit before exec'ing the toolchain.

Invoked only by the trusted local Lean runner, with a fixed executable command.
Running the limit setup in this separate process avoids unsafe preexec_fn hooks
in the multi-threaded API server. RLIMIT_AS is per-process, not a cgroup cap.
"""
from __future__ import annotations

import os
import sys


def main() -> int:
    if len(sys.argv) < 4 or sys.argv[2] != "--" or not sys.argv[1].isdigit():
        print("Lean memory guard: invalid invocation", file=sys.stderr)
        return 125
    try:
        import resource
        limit_bytes = int(sys.argv[1])
        if limit_bytes < 512 * 1024 * 1024 or limit_bytes > 65536 * 1024 * 1024:
            raise ValueError("out-of-range address-space cap")
        resource.setrlimit(resource.RLIMIT_AS, (limit_bytes, limit_bytes))
    except (ImportError, AttributeError, OSError, ValueError) as exc:
        print(f"Lean memory guard failed before exec: {exc}", file=sys.stderr)
        return 125
    try:
        os.execvp(sys.argv[3], sys.argv[3:])
    except OSError as exc:
        print(f"Lean memory guard could not start toolchain: {exc}", file=sys.stderr)
        return 125
    return 125


if __name__ == "__main__":
    sys.exit(main())
