"""Gate between Job Object attachment and starting the approved Lean command.

The parent starts this trusted Python helper with stdin PIPE. Until it receives
the exact START token after successful AssignProcessToJobObject, no toolchain
child is launched. The helper and its subprocesses inherit the job limits.
"""
from __future__ import annotations

import subprocess
import sys


def main() -> int:
    if len(sys.argv) < 3 or sys.argv[1] != "--":
        print("Windows Lean job guard: invalid invocation", file=sys.stderr)
        return 125
    token = sys.stdin.buffer.readline(16)
    if token != b"START\n":
        print("Windows Lean job guard: not authorized to start", file=sys.stderr)
        return 125
    try:
        result = subprocess.run(
            sys.argv[2:], stdin=subprocess.DEVNULL, check=False
        )
    except OSError as exc:
        print(f"Windows Lean job guard: toolchain start failed: {exc}", file=sys.stderr)
        return 125
    return result.returncode if result.returncode >= 0 else 125


if __name__ == "__main__":
    sys.exit(main())
