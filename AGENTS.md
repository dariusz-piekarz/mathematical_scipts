# Global editorial rules for mathematical manuscripts

These instructions apply to **all Polish-language mathematical manuscripts** in this repository, including new chapter creation, revisions, audits, figure captions and cross-chapter merges.

Refer to [the Polish terminology standard](docs/pl/standardy_terminologiczne.md) for detailed rules.

## Mandatory terminology

1. For set-theoretic union \(A\cup B\), write **„suma zbiorów”** or, when distinguishing it from an algebraic sum, **„suma mnogościowa”**. Do **not** write „unia” in Polish mathematical prose. Distinguish \(A\cup B\) from the algebraic sum \(U+W=\{u+w:u\in U,w\in W\}\).
2. For the equality \(\sum_{i=1}^{m} a_i v_i=0\) used to test linear independence, write **„warunek niezależności liniowej wektorów”**, **„równość z warunku niezależności liniowej”** or **„równość świadcząca o zależności”**. Do **not** call this a „relacja liniowa”. The ordinary mathematical word „relacja” remains valid for set-theoretic relations, equivalence relations and orders.

## Preserve references and rigor

- Preserve existing stable `\label` names and corresponding `\ref` targets even if they contain an older word. Text, theorem titles, captions and prose should follow the current terminology.
- State all assumptions and quantify all objects explicitly. Justify every substantive proof step and special case.
- Do not broaden an approved chapter's topical coverage merely to add material: focus audits on mathematical correctness, missing justifications, precise examples, language, reference integrity and build quality.
- For LaTeX chapters under `chapters/pl/`, keep chapter files independent of external graphics or code when self-contained TikZ can be used.
