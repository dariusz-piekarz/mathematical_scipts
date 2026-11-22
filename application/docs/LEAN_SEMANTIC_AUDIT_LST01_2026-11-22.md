# Audyt semantyczny Lean ↔ LaTeX: LST-01 (iteracja 22 listopada 2026)

## Źródła i wynik

Kanoniczny plik: `chapters/pl/logic_and_set_theory/01-zdania-i-spojniki-logiczne.tex`, `LST-01`. Zweryfikowany SHA256 jego **pełnych bajtów UTF-8**:

```
9b5cbe26dee8ed5bc437cb3a0d19638eafc5d9ae178a3caa545b8bcf5842b8d0
```

Ścisły zakres zatwierdzenia: `thm:de-morgan-logic`, `thm:implication-laws` i `thm:negated-implication-xli`, łącznie **sześć tez**. Główny kod `application/lean/src/LST01_SyntaxValuations.lean`; `manifest.json` wskazuje teraz **wszystkie** deklaracje odpowiadające każdemu twierdzeniu przez `lean_theorems`, dodatkowo jego `lean_theorem`, `source_document_path` i `source_document_sha256`.

### Zgodność definicji

| Element oryginalnego rozdziału | Definicja Lean | Sprawdzenie |
| --- | --- | --- |
| `def:propositional-grammar-xli`: litery i pięć spójników, tylko skończona budowa | `LST01.Formula`: `atom : Nat → Formula` oraz `neg`, `conj`, `disj`, `imp`, `iff` | Typ indukcyjny generuje wyłącznie skończone drzewa z dokładnie tymi sześcioma rodzajami konstruktorów |
| `def:valuation`: przypisanie każdej występującej literze jednej wartości 0/1 | `Valuation := Nat → Bool` | Każde przypisanie do skończonego zbioru liter rozszerza się do funkcji całkowitej; pozostałe wartości nie wpływają na `eval` |
| Tablice spójników | `eval`: `!`, `&&`, `||`, `(!p)||q`, `decide(p=q)` | Negacja, koniunkcja, alternatywa, implikacja materialna i równoważność mają identyczne cztery/tworzące dwie wartości tablice |
| `def:tautology`: `p ≡ q` przy każdym wspólnym wartościowaniu | `equivalent p q := ∀ ν, eval ν p = eval ν q` | Równość wartości obejmuje także litery występujące tylko po jednej stronie; `≡` pozostaje relacją, nie spójnikiem |
| `def:tautology`: prawda przy wszystkich wartościowaniach | `tautology p := ∀ ν, eval ν p = true` | Zgodne bez dodatkowych założeń |

Indeksowanie przez `Nat` zaczyna się od zera, podczas gdy tekst używa `p₁,p₂,…`. To czysta zmiana indeksu `pᵢ ↔ atom (i-1)`, bez zmiany przestrzeni wartościowań. Konstruktor `iff` jest wewnątrz formuły, a `equivalent` jest relacją na całych formułach; nie są utożsamione. Powtórzone wystąpienia tej samej litery są oceniane przez `ν n`, co wyklucza nieuprawnione niezależne wartościowanie poszczególnych wystąpień.

### Sprawdzenie wszystkich sześciu tez

| Etykieta LaTeX | Deklaracje Lean | Kontrola tezy |
| --- | --- | --- |
| `thm:de-morgan-logic` | `lst01_syntax_de_morgan_and`, `lst01_syntax_de_morgan_or` | Oba prawa `¬(p∧q)≡(¬p∨¬q)`, `¬(p∨q)≡(¬p∧¬q)` |
| `thm:implication-laws` | `lst01_syntax_implication_as_disjunction`, `lst01_syntax_implication_contrapositive`, `lst01_syntax_modus_ponens` | Dokładnie dwie równoważności oraz tautologia `((p⇒q)∧p)⇒q`, nie sama reguła metateoretyczna |
| `thm:negated-implication-xli` | `lst01_syntax_negated_implication` | `¬(p⇒q)≡(p∧¬q)` |

Każde z tych twierdzeń ma kwantyfikację po dowolnych `p,q : Formula` oraz — za sprawą `equivalent` albo `tautology` — po wszystkich `ν : Nat → Bool`. Nie zakładamy, że cztery kombinacje wartości dwóch formuł są niezależnie realizowalne, jeśli formuły mają wspólne litery.

Dodatkowo sprawdzono tablicowo **osiem** tożsamości z kodu dla każdej z czterech par wartości argumentów — **32** poprawne przypadki. Dwie pomocnicze tezy, `lst01_syntax_iff_as_two_implications` oraz `lst01_syntax_repeated_atom`, wspierają semantykę definicji; nie zwiększają liczby trzech zatwierdzonych etykiet źródłowych.

### Rzeczywista kompilacja i aksjomaty

W [GitHub Actions #45011738363](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45011738363), zakończonym sukcesem 22 listopada 2026 o 10:22 UTC, skompilowano wszystkie **cztery pliki / czternaście deklaracji** w Lean 4.26.0 i Mathlib z commitu `2df2f0150c275ad53cb3c90f7c98ec15a56a1a67`. Polecenia `#print axioms` dla ośmiu deklaracji na poziomie `Formula` wykazały wyłącznie `propext` albo brak aksjomatów. Nie wystąpił `sorryAx`.

Kontrola zgodności treści została wykonana **oddzielnie od uruchomienia Lean**: porównano indukcyjną składnię, semantykę pięciu spójników, znaczenie relacji `≡`, zakres kwantyfikatorów oraz wszystkie człony trzech źródłowych twierdzeń. Na tej podstawie wpisy `manifest.json` mają `statement_status=approved` **tylko dla podanego SHA**. Jest to recenzja semantyczna w tej iteracji, nie podpis niezależnego recenzenta ani dowód w Lean odnoszący się bezpośrednio do tekstu LaTeX.

## Zabezpieczenia przed nieaktualną zgodnością

- Backend kontroluje, czy indeks SQLite ma SHA256 zgodne z zapisaną treścią; naruszenie integralności daje HTTP 409.
- Dla zmienionego, ale spójnego indeksu: `formalization_status=stale`; zatwierdzenie z manifestu jest w efektywnym API cofane do `statement_status=needs_review`. Kompilacja jest blokowana.
- CI `lean_ci_audit.py` wymaga pełnej listy `lean_theorems`, poprawnego SHA dla `approved` i porównuje bajty kanonicznego `.tex` ze źródłem przypiętym w rejestrze; brak pliku, różnica SHA albo wyjście poza `chapters/pl` stanowi błąd.
- Testy API wymagają `ready`, `approved`, właściwego SHA i wszystkich sześciu nazw. Testy regresji odróżniają zmianę źródła od uszkodzenia indeksu.

## Ograniczenia i dalszy kierunek

`statement_status=approved` nie jest tożsame z `certificate=true`. W aplikacji `certificate=false` pozostaje obowiązkowe, ponieważ certyfikacja całości wymaga jeszcze zdefiniowania polityki wydawania certyfikatów i dowodowego związku recenzowanego tłumaczenia z pinem kompilacji. Recenzja dotyczy **trzech wskazanych twierdzeń**, a nie całego `LST-01` ani dalszej logiki pierwszego rzędu.

Dalsze twierdzenia do formalizacji: `thm:valuation-well-defined-xli` i `thm:equiv-test` w `LST-01`, następnie zakres kwantyfikatorów w `LST-02`.
