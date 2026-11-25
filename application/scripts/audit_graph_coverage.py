"""Run after rebuilding the index: python -m scripts.audit_graph_coverage."""
import argparse
import json
from pathlib import Path
import sqlite3

from backend.graph_coverage import graph_coverage


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", type=Path, required=True)
    parser.add_argument("--catalog", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    with sqlite3.connect(args.db) as con:
        result = graph_coverage(con, args.catalog)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], ensure_ascii=False))
    catalog = result["catalog"]
    # Missing index entries and broken explicit reading links fail CI.
    # Missing thematic edges remain a review queue, never invented relationships.
    return int(bool(catalog["missing"] or catalog["path_mismatches"] or catalog["duplicate_ids"]
                    or result["reading_audit"]["invalid"]))


if __name__ == "__main__":
    raise SystemExit(main())
