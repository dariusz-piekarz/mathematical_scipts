# Lean 4 — pilotaż LST-01: kolejne prawa logiczne

> **Aktualizacja po audycie semantycznym:** opis poniżej dokumentuje wcześniejszy stan pilotażu. Nowszy [audyt LST-01](LEAN_SEMANTIC_AUDIT_LST01_2026-11-22.md) potwierdził realną kompilację 14 deklaracji, zatwierdził zgodność sześciu tez z trzema etykietami (`statement_status=approved`) wyłącznie dla SHA256 `9b5cbe26dee8ed5bc437cb3a0d19638eafc5d9ae178a3caa545b8bcf5842b8d0` i wprowadził automatyczne unieważnianie zatwierdzenia przy zmianie kanonicznego źródła. `certificate=false` pozostaje obowiązujące.


Data: 22 listopada 2026 r. Gałąź: `biblioteka-matematyczna-iteracja-6`.

## Podstawa źródłowa

Kanoniczny dokument: `chapters/pl/logic_and_set_theory/01-zdania-i-spojniki-logiczne.tex`, identyfikator `LST-01`. Pozostaje bez zmian.

| Etykieta LaTeX | Treść źródłowa | Deklaracje Lean | Status korespondencji |
| --- | --- | --- | --- |
| `thm:de-morgan-logic` | Dwie równoważności dla dowolnych formuł | `lst01_de_morgan_and`, `lst01_de_morgan_or` | `needs_review` |
| `thm:implication-laws` | `(p→q) ≡ (¬p∨q)`; przeciwstawienie implikacji; modus ponens | `lst01_implication_as_disjunction`, `lst01_implication_contrapositive`, `lst01_modus_ponens` | `needs_review` |
| `thm:negated-implication-xli` | `¬(p→q) ≡ (p∧¬q)` | `lst01_negated_implication` | `needs_review` |

**Razem: 3 powiązania etykiet z 6 deklaracjami Lean.** Wszystkie trzy pliki `application/lean/src/LST01_*.lean` mają jawne `#print axioms` dla każdego twierdzenia. Rejestr `application/lean/manifest.json` wskazuje konkretną etykietę i główną deklarację w każdym pliku.

## Audyt matematyczny zakresu formalizacji

Każdy termin `p` i `q` po stronie Lean jest wartością typu `Prop`, a nie syntaktycznym drzewem składniowym formuł. Spójnik `→` jest odpowiednikiem prawdziwościowej implikacji, `↔` odpowiada równoważności wartości logicznych. W klasycznej semantyce formuł źródłowe `p ≡ q` oznacza prawdziwość `p ↔ q` przy wszystkich wartościowaniach.

Wszystkie trzy grupy odtwarzają **treść równości wartości po interpretacji**, przy czym:

- `lst01_implication_as_disjunction`: użycie prawa wyłączonego środka / logiki klasycznej jest istotne dla równoważności `p → q` z `¬p ∨ q`.

- `lst01_implication_contrapositive`: oba kierunki klasycznej równoważności są reprezentowane.

- `lst01_modus_ponens`: reprezentuje formułę `((p → q) ∧ p) → q`, czyli dokładnie tautologię z treści twierdzenia (nie samo metatwierdzenie o regule dedukcji).

- `lst01_negated_implication`: reprezentuje `¬(p → q) ↔ (p ∧ ¬q)`, z jawną klasycznością.


**Niezrealizowany element semantyczny:** nie wprowadzono jeszcze indukcyjnej składni `Formula`, funkcji `eval : Formula → Valuation → Bool` ani kwantyfikacji po wszystkich `Valuation`. Dlatego w żadnym wpisie nie podniesiono `statement_status` do `approved`. Konieczne jest osobne sprawdzenie przekładu kompozycyjnego na wartościowania oraz jawna kontrola wszystkich członów źródłowego twierdzenia.

## Weryfikacja przez Lean

- Rzeczywisty CI kompilujący `LST01_DeMorgan.lean` i sprawdzający jego 2 deklaracje przeszedł: [GitHub Actions 45010519869](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45010519869). Log nie zawiera niedopuszczonych aksjomatów.
- Dwa nowe pliki `LST01_ImplicationLaws.lean` i `LST01_NegatedImplication.lean` zostały dodane i zarejestrowane. Przebieg CI dla nich: [GitHub Actions 45011246156](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45011246156). **Nie oznaczać tych 4 nowych deklaracji jako skompilowanych, dopóki raport tego przebiegu nie zakończy się sukcesem.**
- Skuteczna kompilacja nie daje certyfikatu wierności matematycznej `LaTeX ↔ Lean`. `certificate` pozostaje `false`.

## Kolejne zadania

Kontynuować od składni formuł i semantyki wartościowań albo przygotować analogiczny jawnie niezatwierdzony pilotaż `LST-02` (kwantyfikatory) oraz `LA-01`. Przy zmianach źródła przypinać i aktualizować jego SHA dopiero po ponownym pełnym audycie powiązania.
