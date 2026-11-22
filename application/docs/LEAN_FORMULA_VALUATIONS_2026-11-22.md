# Lean 4 — składnia i semantyka rachunku zdań (LST-01)

**Data:** 22 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło kanoniczne:** `chapters/pl/logic_and_set_theory/01-zdania-i-spojniki-logiczne.tex`. Bez zmian w LaTeX-u.

## Zaimplementowana definicja

`application/lean/src/LST01_SyntaxValuations.lean` wprowadza `LST01.Formula` jako typ indukcyjny z konstruktorami `atom`, `neg`, `conj`, `disj`, `imp` i `iff`. Reprezentuje dokładnie sześć reguł budowania z definicji `def:propositional-grammar-xli` (atom i pięć spójników). Każde drzewo jest skończone.

`LST01.Valuation := Nat → Bool` przypisuje wartość każdej literze. Funkcja `LST01.eval` wylicza wartość formuły indukcyjnie, a dla implikacji stosuje `¬p ∨ q` na wartościach Bool; `iff` jest prawdziwe, gdy wartości są identyczne. `LST01.equivalent p q` znaczy `∀ ν, eval ν p = eval ν q`. `LST01.tautology p` znaczy `∀ ν, eval ν p = true`.

`Nat` indeksuje symbole od 0, podczas gdy skrypt nazywa je `p_1,p_2,…`; reindeksacja `atom (n-1)` nie zmienia sensu praw. Powtórzone wystąpienia tego samego symbolu czytają dokładnie `ν n`, a zatem **nie** są traktowane jak niezależne wartości.

## Korespondencja twierdzeń

| Etykieta źródła | Twierdzenie Lean | Status |
| --- | --- | --- |
| `thm:de-morgan-logic` | `lst01_syntax_de_morgan_and`, `lst01_syntax_de_morgan_or` | kandydująca równoważność wartościowań |
| `thm:implication-laws` | `lst01_syntax_implication_as_disjunction`, `lst01_syntax_implication_contrapositive`, `lst01_syntax_modus_ponens` | kandydująca równoważność i tautologia |
| `thm:negated-implication-xli` | `lst01_syntax_negated_implication` | kandydująca równoważność wartościowań |

Dodatkowe twierdzenia `lst01_syntax_iff_as_two_implications` oraz `lst01_syntax_repeated_atom` dokumentują definicję równoważności i spójność wielokrotnych wystąpień atomu. Łącznie **8 deklaracji na poziomie składni**. Istniejące **6 twierdzeń na poziomie `Prop`** zachowano w trzech odrębnych plikach. CI zostało rozszerzone, aby kompilować i audytować wszystkie pliki `.lean` w `src/`, a nie tylko aktywne powiązania w `manifest.json`.

Rejestr zawiera nadal **3 etykiety**, obecnie wskazujące na `LST01_SyntaxValuations.lean`, a każda etykieta ma wskazane jedno główne twierdzenie do podglądu. Panel wyświetla kod obejmujący wszystkie 8 formalnych twierdzeń tego pliku.

## Ocena matematyczna

Ujęcie `Formula → Valuation → Bool` usuwa podstawowe niedopasowanie pierwotnej wersji `Prop`: jawnie występują formuły jako drzewa składniowe oraz wszystkie wartościowania ich liter. Prawa są dowodzone przez wyczerpanie dwóch możliwych wartości podformuł po ustaleniu dowolnego wartościowania. Zawiera to również przypadek wspólnych liter w `p` i `q`: nie zakładamy istnienia wartościowań realizujących wszystkie cztery pary wartości, lecz pokazujemy prawo dla każdej możliwej pary.

**Pozostała ostrożność:** zapis `statement_status=needs_review` w rejestrze utrzymano celowo. Sukces `lake env lean` potwierdza deklarację w formalnym systemie z danymi definicjami, lecz przyznanie pełnej wierności oryginalnej definicji i semantyki jest osobnym krokiem recenzyjnym. Nie ma certyfikatu; `certificate=false`. Nie formalizowano jeszcze rachunku predykatów ani składni z kwantyfikatorami.

## Wyniki weryfikacji

Poprzedni etap: rzeczywisty CI [45011246156](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45011246156) potwierdził wszystkie 6 wcześniejszych twierdzeń z 3 plików `Prop`. Nowy przebieg dla składni i wartościowań: [45011738363](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45011738363); w chwili utworzenia tej dokumentacji trwa inicjalizacja Lean/Mathlib — nie oznaczać 8 nowych deklaracji jako skompilowanych bez rzeczywistego sukcesu tego kroku.

Testy API czytnika: `application/tests/test_lean_http.py` obejmują teraz wszystkie trzy etykiety `LST-01` i wymagają obecności modelu `Formula` oraz `equivalent`.

## Dalsza praca

Po potwierdzeniu zielonego CI: niezależny audyt znaczenia `equivalent` i wszystkich sześciu praw, ewentualne zatwierdzenie mapowania, przypięcie SHA aktualnego dokumentu i przejście do składni oraz semantyki logiki pierwszego rzędu.
