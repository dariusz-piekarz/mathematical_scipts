# Global editorial rules for mathematical manuscripts

These instructions apply to **all Polish-language mathematical manuscripts** in this repository, including new chapter creation, revisions, audits, figure captions and cross-chapter merges.

Refer to [the Polish terminology standard](docs/pl/standardy_terminologiczne.md) for detailed rules.

## Mandatory terminology

1. For set-theoretic union \(A\cup B\), write **„suma zbiorów”** or, when distinguishing it from an algebraic sum, **„suma mnogościowa”**. Do **not** write „unia” in Polish mathematical prose. Distinguish \(A\cup B\) from the algebraic sum \(U+W=\{u+w:u\in U,w\in W\}\).
2. For the equality \(\sum_{i=1}^{m} a_i v_i=0\) used to test linear independence, write **„warunek niezależności liniowej wektorów”**, **„równość z warunku niezależności liniowej”** or **„równość świadcząca o zależności”**. Do **not** call this a „relacja liniowa”. The ordinary mathematical word „relacja” remains valid for set-theoretic relations, equivalence relations and orders.

3. In Polish mathematical text, avoid the standalone English noun **„dual”**, including in section and theorem titles. Use **„przestrzeń dualna”**, **„przestrzeń sprzężona”** or **„przestrzeń funkcjonałów liniowych”**, as appropriate. Polish adjectives **„dualny/dualna/dualne”** are allowed, e.g. **„odwzorowanie dualne”**. Preserve stable LaTeX labels and references.


4. For polynomials, write **„wielomian rozkłada się nad \(K\) na czynniki liniowe”** or **„rozkłada się na czynniki nierozkładalne”**. Do not write **„wielomian rozszczepia się”**, **„rozszczepiony wielomian”** or **„rozszczepienie wielomianu”**. Reserve „rozszczepienie” for mathematically distinct contexts (e.g. split exact sequences), and do not rename historical LaTeX labels.

5. In Polish-language mathematical manuscripts, translate **chart** (a local coordinate chart on a manifold) as **„mapa”**, not **„karta”**. Write **„mapa współrzędnych”**, **„mapa lokalna”**, **„mapy atlasu”**, **„dziedzina mapy”**, **„zmiana map”**, with grammatically correct Polish inflections. Translate **mapping/map** (a function between spaces) as **„odwzorowanie”**, not „mapa”, unless the object truly is a coordinate chart. This rule applies to all Polish scripts, proofs, examples, headings, captions and audits. Preserve stable LaTeX labels and references; never perform blind substitutions that corrupt inflections or mathematical meaning.

6. For topological countability properties, use **„spełnia pierwszy aksjomat przeliczalności”** and **„spełnia drugi aksjomat przeliczalności”** (with appropriate inflections), not adjectival formulations **„pierwszoprzeliczalna / pierwszo przeliczalna”** or **„drugoprzeliczalna / drugo przeliczalna”**. Prefer the noun phrases **„pierwszy aksjomat przeliczalności”** and **„drugi aksjomat przeliczalności”** in headings, propositions, explanations and figures. Applies globally to all Polish math scripts. Preserve existing stable LaTeX labels and references.


7. For Polish set-theory manuscripts, **always spell out „liczba kardynalna”** with the correct grammatical case, number and feminine agreement: e.g. „liczba kardynalna Mahla”, „mierzalna liczba kardynalna”, „silnie nieosiągalna liczba kardynalna”, „słabo zwarta liczba kardynalna”. **Never shorten** this noun to „kardynał”, „kardynały” or their inflected forms in prose, headings or audits. Keep historical stable filenames and LaTeX labels unchanged.

## Preserve references and rigor

- Preserve existing stable `\label` names and corresponding `\ref` targets even if they contain an older word. Text, theorem titles, captions and prose should follow the current terminology.
- State all assumptions and quantify all objects explicitly. Justify every substantive proof step and special case.

### Mandatory proof-detail standard (all manuscripts and audits)

- Write complete, detailed proofs, at the level of chapter 01 of the differential geometry manuscript. Every mathematically substantive implication, intermediate estimate, construction, change of variables, limit, case distinction and application of a theorem must be written out and justified. Do not leave essential intermediate steps as exercises or omit them on the grounds that they are standard, analogous, obvious, or straightforward.
- When applying a previously established theorem, identify it, verify all hypotheses in the current setting, and explain exactly how its conclusion gives the desired step. Provide a stable cross-reference when available. Reuse proved results rather than unnecessarily repeating their entire proofs.
- For nontrivial calculations, display intermediate equalities or inequalities, identify the objects and domains involved, and explain why the transitions are valid. For existence constructions, justify existence, well-definedness, and every property used subsequently.
- Apply the same standard to examples and counterexamples. Explicitly handle exceptional, boundary, degenerate and zero-dimensional cases when relevant.
- During every audit, treat missing or unjustified substantive steps as actual defects requiring correction, not optional enrichment. Do not mark a chapter as stabilized merely because its final conclusions are correct or its LaTeX compiles. A clean audit must also verify the completeness of the proofs. If a full detailed audit is too large, divide it into consecutive bounded portions and keep the chapter open until all portions have been checked.
- Do not broaden an approved chapter's topical coverage merely to add material: focus audits on mathematical correctness, missing justifications, precise examples, language, reference integrity and build quality.
- For LaTeX chapters under `chapters/pl/`, keep chapter files independent of external graphics or code when self-contained TikZ can be used.

## Suggested additions during audits

- When auditing any mathematical manuscript, if a potentially valuable missing theorem, lemma, example, counterexample, explanation, drawing or connection is identified, **flag it separately as a proposal for the user to decide**. State why it would help and where it would fit; distinguish an essential omission from an optional enrichment.
- **Do not insert suggested new content into an audited, previously approved chapter without the user's explicit approval.** Suggestions alone do not reset the count of clean audits. A genuine mathematical mistake, unsupported argument, missing required hypothesis, or necessary correction does count as an audit finding and must be fixed.
- This rule applies to every manuscript in the repository and to subsequent writing and review work. Continue the planned audit after presenting such suggestions.

## Global code listings

- All manuscript and Atlas export preambles must use the generated global listings block in `latex/pl/code-listings.tex`. Use `language=Python` or `language=Julia` explicitly for source code. Preserve the aliases for existing listings. Run `python tools/sync_code_listings.py --check` in audits; regenerate with `--write` after changing the canonical style. See [code style standard](docs/pl/standard_kodu.tex.md). Check rendered code for line wrapping, highlighting and readability.
