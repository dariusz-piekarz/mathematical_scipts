#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
for n in 01 02 03 04 05; do
  python "tools/tests/test_general_topology_ch${n}.py"
done
(
 cd books/pl
 latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error general_topology_ch05.tex > ../../compile_ch05.log 2>&1
 latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error general_topology.tex > ../../compile_book.log 2>&1
 for name in general_topology_ch05 general_topology; do
   test -s "${name}.pdf"
   if grep -qE 'Overfull|Underfull|Missing character|LaTeX Warning|Undefined control sequence|Fatal error' "${name}.log"; then
     echo "LaTeX warnings in ${name}"
     grep -nE 'Overfull|Underfull|Missing character|LaTeX Warning|Undefined control sequence|Fatal error' "${name}.log"
     exit 1
   fi
 done
)
echo 'PASS: Chapters 01–05 regression tests, standalone Chapter 05 and complete book PDFs.'
