# LST-01 / thm:equiv-test — niezależna kontrola semantyczna (trzy zmienne)

- Etap: stabilizacja istniejącego twierdzenia `LST-01:thm:equiv-test`; bez przejścia do kolejnego twierdzenia.
- Gałąź: `biblioteka-matematyczna-iteracja-6`; HEAD przed zapisem: `60fe4c9cc198a086b9c7920aa9c2e2f1a2477f66`.
- Odczytano aktualne `AGENTS.md`, `application/docs/LEAN_FORMALIZATION_PLAN.md`, `application/ROADMAP_I_DZIENNIK.md`, `application/lean/manifest.json`, kanoniczny `chapters/pl/logic_and_set_theory/01-zdania-i-spojniki-logiczne.tex` i `application/lean/src/LST01_SyntaxValuations.lean`.
- Git blob źródła TeX: `03f0971888288934e47c3453fd8f0de0a2c71469`; Git blob źródła Lean: `71f5206b8642f53c45d28004ced57d02e0ebe984`; Git blob manifestu: nieodnotowany w tej iteracji. Są to SHA-1 obiektów Git, **nie** niezależne SHA256 zawartości.
- Manifest deklaruje `source_document_sha256=9b5cbe26dee8ed5bc437cb3a0d19638eafc5d9ae178a3caa545b8bcf5842b8d0`; w tej iteracji nie przeliczono go z bajtów źródła, więc integralność SHA256 nie jest potwierdzona.

## Kontrola znaczenia

Oryginalne twierdzenie: dla dowolnych formuł zdaniowych `φ, ψ`, `φ ≡ ψ` wtedy i tylko wtedy, gdy formuła `φ ⇔ ψ` jest tautologią. Poprzedzająca definicja wymaga jednego wspólnego wartościowania obejmującego litery obu formuł. Lean definiuje `Formula` indukcyjnie, `Valuation := Nat → Bool`, `equivalent p q := ∀ ν, eval ν p = eval ν q` i `tautology p := ∀ ν, eval ν p = true`. Twierdzenie `lst01_syntax_equivalence_test` jest dokładnie `equivalent p q ↔ tautology (.iff p q)`. Zmienne atomowe są indeksowane przez `Nat`, a kwantyfikacja obejmuje wszystkie wartościowania, więc nie ma niezależnego przypisywania wartości powtarzającym się wystąpieniom tej samej litery. Różnica `Prop` (relacja semantyczna) versus `Formula` (składnia) została zachowana. Nie wykryto rozbieżności w kontrolowanym twierdzeniu.

## Rzeczywisty test regresyjny

Uruchomiono lokalnie Python 3, niezależnie od Lean: wszystkie 256 funkcji boolowskich trzech zmiennych sparowano w 65 536 uporządkowanych parach; dla każdej sprawdzono wszystkie 8 wartościowań. **65 536/65 536 par oraz 524 288/524 288 ocen wartościowań zgodnych** z równoważnością: równość funkcji przy każdym wartościowaniu iff tautologiczność ich dwukierunkowej implikacji. Jest to wyczerpujący test funkcji trójargumentowych, a nie test dowodu Lean ani wszystkich formuł o dowolnej liczbie zmiennych.

## Kernel, zależności i ograniczenia

- `command -v lake` i `command -v lean`: oba bez wyniku; **`lake env lean`: not_run / toolchain_unavailable**. Lokalny `git ls-remote` również nie zadziałał (brak DNS), więc odczyt repozytorium wykonano przez połączone API GitHub.
- Konfiguracja deklaruje Lean `v4.26.0` i Mathlib `2df2f0150c275ad53cb3c90f7c98ec15a56a1a67`. Nie odnotowano nowej kompilacji, nowego `#print axioms` ani nowego wyniku kernela. Historyczny wynik CI 45023719378 pozostaje historyczny.
- Nie wprowadzono `sorry`, `admit` ani nowych aksjomatów; kod Lean i manifest pozostają bez zmian.
- Korpus: **5 mapowań z docelowych 20–30** według odczytanego manifestu; **0 nowych formalizacji** i **0 nowych potwierdzeń przez kernel** w tej iteracji. Nie wyciąga się z testu Python wniosku `proof_status=verified`.
- Licznik pełnych czystych audytów od ostatniej poprawki: **0 zaliczonych w tej iteracji** (brak świeżej kompilacji i niezależnego SHA256). Oddzielny pełny audyt końcowy: **nieprzeprowadzony**. Stabilność: **niepotwierdzona**.

## Następny krok w tym samym etapie

Przeliczyć SHA256 oryginalnych bajtów TeX, odtworzyć `lake env lean` na przypiętej wersji, zachować surowy log i wynik kontroli aksjomatów; następnie wykonać pełny czysty audyt i oddzielny sceptyczny audyt końcowy. Nie przechodzić do nowego twierdzenia przed spełnieniem tych warunków.
