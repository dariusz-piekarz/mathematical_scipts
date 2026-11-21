#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python tools/tests/test_general_topology_ch01.py
python tools/tests/test_general_topology_ch02.py
python tools/tests/test_general_topology_ch03.py
(
  cd books/pl
  latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error general_topology_ch03.tex > ../../compile_ch03.log 2>&1
  latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error general_topology.tex > ../../compile_book.log 2>&1
  for name in general_topology_ch03 general_topology; do
    test -s "${name}.pdf"
    if grep -qE 'Overfull|Underfull|Missing character|LaTeX Warning|Undefined control sequence|Fatal error' "${name}.log"; then
      echo "LaTeX warning: $name"
      grep -nE 'Overfull|Underfull|Missing character|LaTeX Warning|Undefined control sequence|Fatal error' "${name}.log"
      exit 1
    fi
  done
)
echo 'PASS: Chapters 01–03 local validation, standalone Chapter 03 PDF and book PDF.'
