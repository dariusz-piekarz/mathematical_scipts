"""Move a trusted Lean launch into a delegated cgroup before exec'ing toolchain."""
from __future__ import annotations

import os
from pathlib import Path
import sys


def main() -> int:
    if len(sys.argv) < 4 or sys.argv[2] != "--":
        print("Lean cgroup guard: invalid invocation", file=sys.stderr)
        return 125
    try:
        (Path(sys.argv[1]) / "cgroup.procs").write_text(str(os.getpid()), encoding="ascii")
    except OSError as exc:
        print(f"Lean cgroup guard could not attach process: {exc}", file=sys.stderr)
        return 125
    try:
        os.execvp(sys.argv[3], sys.argv[3:])
    except OSError as exc:
        print(f"Lean cgroup guard could not start toolchain: {exc}", file=sys.stderr)
        return 125
    return 125


if __name__ == "__main__":
    sys.exit(main())
