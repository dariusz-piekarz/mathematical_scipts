# Mathematical library — repository structure (iteration IV)

The source language is currently **Polish**. Directory identifiers, code comments,
function names and descriptions are in **English** to support future locales.

```text
chapters/pl/<subject>/<chapter>.tex   # Modular chapter content (Polish)
books/pl/<book>.tex                # Book entry point with \input dependencies
shared/pl/<topic>/*.tex            # Canonical subject modules (after audited merges)
sources/pl/                        # Original user-supplied source copies
tools/                             # English-language maintenance scripts
audits/previous/                   # Previous audit reports (historical)
audits/legacy_tools/               # Historical scripts from earlier iterations
catalog/new_chapters.json          # 20 additional chapters, SHA-256 provenance
catalog/topic_registry.json        # Planned canonical subject ownership
```

The 236 existing chapters were relocated to English-language subject directories.
Twelve book entry points retain all of their existing chapter imports after the move.
The 20 newly supplied chapters are located in
`chapters/pl/differential_geometry_and_topology/`, and are assembled by
`books/pl/differential_geometry_and_topology.tex`.

**Compiling:** from `books/pl` run
`latexmk -pdf -interaction=nonstopmode -halt-on-error differential_geometry_and_topology.tex`.

**Validating:** from the repository root run `python tools/validate_repository.py`.

## Content-merging policy

One mathematical topic should eventually have one canonical source module, regardless
of how many books require it. When merging rings, fields, homology or Morse theory,
inspect both sources, preserve all distinct theorems, hypotheses, proof variants,
examples, code and figures, and maintain existing label aliases. Update all consuming
books to `\input` the canonical module. Never silently delete the only copy of a
source argument. The registry marks candidates as **pending** until mathematically
audited; language-aware relocation alone is not a merge.

## Migration notes

- The prior `main` branch remains unchanged; iteration IV builds on iteration III.
- Old integration manifests and validators are historical. The new validator verifies
  the current paths and uploaded source copies.
- The original monolithic `geometria_i_topologia_rozniczkowa.tex` in the repository
  root is preserved as a legacy source and is not part of the modular book.
- Source snapshots in this iteration are stored with LF line endings on GitHub;
  the archive generated from the newly uploaded files retains their original bytes.
- A complete second LaTeX pass was not finished for the large differential geometry
  and topology book; do not assume its references have all been resolved yet.

## Measure theory and jets (Polish)

- [Measure theory](books/pl/measure_theory.tex): 31 chapters in [chapters/pl/measure_theory](chapters/pl/measure_theory).
- [Jets](chapters/pl/measure_theory/31-dzety-geometria-i-teoria-miary.tex): geometric and measure-theoretic jets; the Rademacher theorem is covered in chapter 28.
- [Integration theory](books/pl/integration_theory.tex) remains a separate, unchanged book.
- [Manifest](catalog/measure_theory_manifest.json) and [module documentation](docs/pl/measure_theory.md).
- Build: `latexmk -cd -pdf books/pl/measure_theory.tex`.

The source language is Polish; directory names are English. Any later merge with integration theory requires proof-by-proof review.

## Functional analysis (Polish)

- [Book entry point](books/pl/functional_analysis.tex): 35 modular chapters in [chapters/pl/functional_analysis](chapters/pl/functional_analysis).
- [Chapter documentation](docs/pl/functional_analysis.md).
- The Polish term is **zbieżność zmajoryzowana**, including theorem headings.
- Build from `books/pl`: `latexmk -pdf functional_analysis.tex`.
