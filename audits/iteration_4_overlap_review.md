# Iteration IV — thematic overlap audit (initial)

Source language: Polish. Folder names, script descriptions and machine-readable keys: English.

## Why the merge is staged
The 20 new files are chapters of a larger differential geometry and topology
book. Some overlap with previous standalone books; the presence of matching
terminology does not justify deleting distinct mathematical proofs or examples.
No content deletion has been performed in this iteration.

## Priority 1: rings and fields
- Algebraic geometry: `chapters/pl/algebraic_geometry/00-teoria-pierscieni-od-arytmetyki-do-geometrii-rownan.tex`
  is a full introductory chapter to rings, ideals and polynomial rings.
- Differential geometry and topology: `chapters/pl/differential_geometry_and_topology/05-abstract_algebra.tex`
  has a ring/ideal/quotient section (source lines 742–951), then modules, tensor
  products, localization and a fraction-field construction (source lines 1630–1721).
- Galois theory: `chapters/pl/galois_theory/00-ciala-i-rozszerzenia.tex`
  develops fields and field extensions with a different purpose.

Proposed canonical owners:
`shared/pl/ring_theory/foundations.tex` and
`shared/pl/field_theory/foundations.tex`.

Merge acceptance rules:
1. Form a union of **distinct content**: definitions, full hypotheses, theorems,
   proofs (including independent proof methods), diagrams, motivating examples,
   computational examples, and exercise references.
2. Preserve established labels by mapping them to the canonical statements
   without duplicate labels in a book.
3. Keep module-relative content independent of the identity of the consuming
   book; book-level introductions may remain thin wrappers.
4. Compile all consuming books twice, check duplicate/unresolved labels,
   and verify that the original content is still recoverable from sources.
5. Do not place the same foundational text in multiple source files.

Current status: candidates indexed; mathematical merging pending. The
original 12 source files and 20 newly attached chapters remain available.

## Other candidate overlaps
- Homology and chain complexes (new chapters 06–09 versus algebraic topology)
- de Rham cohomology (new chapter 10 versus algebraic topology)
- Morse theory and cobordisms (new chapters 18–20 versus graph/knot theory)
- Characteristic classes (new chapter 17 versus algebraic geometry/topology)

## Build/check notes
- 13 book entrypoints and 256 direct chapter imports were verified on GitHub.
- The 20 new chapters were uploaded and checksummed with original source names
  recorded in `catalog/new_chapters.json`.
- A small standalone test of chapter 05 compiled to 21 pages. References to
  chapters omitted from that test are expected to remain unresolved there.
- A full run of the large new book did not complete within the available
  compile window. No claim of full-book reference validation is made.
- The monolithic legacy geometry book remains untouched at repository root.
