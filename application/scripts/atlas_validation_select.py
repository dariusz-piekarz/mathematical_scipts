"""Select one immutable Atlas validation candidate from a branch-local request.

The request file allows repeatable SHA-pinned CI on a non-default branch:
updating its contents triggers push without editing the tested source tree.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re

from scripts.atlas_validation_gate import verify_ancestor

FRAGMENT = re.compile(r"[LGPA SMN]".replace(" ", "") + r"[1-7]\\.[1-9][0-9]*\\Z")


def select(event: str, *, dispatch_sha: str, dispatch_fragment: str,
           request_path: Path) -> tuple[str, str]:
    if event == "workflow_dispatch":
        sha, fragment = dispatch_sha, dispatch_fragment
    elif event == "push":
        doc = json.loads(request_path.read_text(encoding="utf-8"))
        if not isinstance(doc, dict) or set(doc) - {"candidate_sha", "fragment", "request_note"}:
            raise ValueError("Unexpected Atlas validation request schema")
        sha, fragment = doc.get("candidate_sha"), doc.get("fragment")
    else:
        raise ValueError("Unsupported validation event")
    if not isinstance(sha, str) or not isinstance(fragment, str):
        raise ValueError("Invalid SHA or fragment")
    if not FRAGMENT.fullmatch(fragment):
        raise ValueError("Invalid fragment ID")
    return sha, fragment


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--request", type=Path, required=True)
    p.add_argument("--event", required=True, choices=("push", "workflow_dispatch"))
    p.add_argument("--dispatch-sha", default="")
    p.add_argument("--dispatch-fragment", default="L1.1")
    p.add_argument("--branch", default="biblioteka-matematyczna-iteracja-6")
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args(argv)
    sha, fragment = select(args.event, dispatch_sha=args.dispatch_sha,
                           dispatch_fragment=args.dispatch_fragment,
                           request_path=args.request)
    verify_ancestor(sha, branch=args.branch)
    with args.output.open("a", encoding="utf-8") as stream:
        stream.write(f"sha={sha}\\nfragment={fragment}\\n")
    print(json.dumps({"candidate_sha": sha, "fragment": fragment,
                      "verified_branch_ancestry": True}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
