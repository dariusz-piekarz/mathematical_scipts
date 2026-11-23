# L1.3 / LST-02 — pakiet do niezależnej recenzji semantycznej

**Audytowany, niezmienny commit:** `163c8f6415d9d390fc1a737f6954b2865eff6c6e`.  
**Cztery formalizacje zgłoszone do recenzji:** `needs_review`, nie `approved`.  
**Odbiór techniczny:** [2+1 #45208224201](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45208224201), **3/3 PASS**.  
**Odbiór semantyczny:** `pending`; autor niniejszego pakietu **nie** jest niezależnym recenzentem.  
**Rejestr sprawy:** [GitHub issue #11](https://github.com/dariusz-piekarz/mathematical_scipts/issues/11).

## 1. Dokładny zakres i kryterium akceptacji

Porównać oryginalne, całe stwierdzenia LaTeX (łącznie z
dziedzinami, kwantyfikatorami, logiką klasyczną, zastrzeżeniami
o pustych dziedzinach i przeciwnymi kierunkami implikacji) z
**konkretnymi deklaracjami** z
`application/lean/src/LST02_Quantifiers.lean`. Kod Lean ma
reprezentować sens sformułowania, nie jedynie dowodzić
słabszego stwierdzenia prawdziwego dla wybranej wartości.

Pliki do przejrzenia na **tym samym** commit SHA:
- `chapters/pl/logic_and_set_theory/02-kwantyfikatory-i-podstawowe-metody-dowodzenia.tex`
- `application/lean/src/LST02_Quantifiers.lean`
- `application/lean/manifest.json` (cztery wpisy `LST-02`)
- `application/tests/test_lean_ci_audit.py` i `application/scripts/lean_ci_audit.py`
- `application/docs/LEAN_L13_LST02_PILOT_2026-11-23.md` (raport autora, nie dowód niezależności)

**Identyfikacja źródeł:** Git blob kanonicznego pliku LaTeX na
kandydacie: `000ad4c0185eb2296ad7af3523ad30b08dfeebaf`.
Nie mylić SHA Git blob z `source_document_sha256`: pola SHA256
celowo **brakuje** w czterech nowych wpisach dopóki nie
nastąpi akceptacja semantyczna.

## 2. Macierz porównania każdej kompletnej tezy

| Etykieta LaTeX | Lean | Zasady oceny |
| --- | --- | --- |
| `thm:negation-quantifiers` | `lst02_not_forall`, `lst02_not_exists` | Obydwie równoważności, również gdy `D` jest puste. Pierwsza wymaga klasycznej eliminacji podwójnej negacji; nie zastępować jej konstruktywnym, słabszym twierdzeniem. |
| `thm:same-quantifier-order` | `lst02_swap_forall`, `lst02_swap_exists` | Zachować obydwa kierunki, obydwa rodzaje kwantyfikatorów, kolejność argumentów `P x y` mimo wymiany kwantyfikatorów; `D` i `E` niezależne, możliwie puste. |
| `thm:swap-mixed` | `lst02_mixed_quantifier_forward`, pomocniczo `lst02_mixed_empty_counterexample` | Zachować wyłącznie `(∃ y:E, ∀ x:D, P x y) → (∀ x:D, ∃ y:E, P x y)`. Nie formułować równoważności. Pomocniczy przykład `D = E = Empty` obala odwrotność; nie jest przekładem przykładu arytmetycznego z oryginału. |
| `thm:unique-expansion-xli` | `lst02_unique_exists_expansion` | Sprawdzić definicję `∃!`, istnienie świadka, jednoznaczność względem **wszystkich** `y:D`, równość `y=x`, także pustą dziedzinę. |

### Granice semantyczne wymagające jawnej decyzji

1. **Dziedziny:** oryginał kwantyfikuje po zbiorach/kolekcjach
   `D,E`; Lean używa typów `D : Type u`, `E : Type v`
   (również `Empty`). Recenzent powinien ocenić, czy to
   poprawne odwzorowanie semantyki **dla wskazanych czterech tez**.
2. **Logika klasyczna:** `lst02_not_forall` korzysta z `classical`.
   CI dla tego twierdzenia drukuje `[propext, Classical.choice,
   Quot.sound]`; dla pozostałych sześciu deklaracji LST-02
   nie wykazuje dodatkowych aksjomatów. Jest to wynik jądra,
   nie certyfikat przekładu.
3. **Odwrotność kwantyfikatorów mieszanych:** źródło zawiera
   kontrprzykład na liczbach naturalnych, a Lean formalizuje
   alternatywny kontrprzykład na pustych typach. Czy to wystarcza
   do zaakceptowania całej tezy „nie zachodzi ogólnie”, czy
   wymaga osobnego formalnego odwzorowania przykładu z tekstu?
   Recenzent powinien to rozstrzygnąć, a nie milcząco utożsamiać
   oba przykłady.
4. **Statusy:** `statement_status=needs_review` jest poprawny
   do czasu formalnej decyzji. `certificate=false` także po
   akceptacji: nie istnieje automatyczny certyfikat LaTeX–Lean.

## 3. Powtarzalna reprodukcja — na SHA kandydata

Poniższe polecenia są **instrukcją** dla recenzenta, a nie
dodatkowym uruchomieniem wykonanym w tej iteracji:

```bash
git fetch origin biblioteka-matematyczna-iteracja-6
git worktree add --detach ../atlas-lst02-review 163c8f6415d9d390fc1a737f6954b2865eff6c6e
cd ../atlas-lst02-review
git rev-parse HEAD
git show HEAD:application/lean/manifest.json
git show HEAD:application/lean/src/LST02_Quantifiers.lean
sha256sum chapters/pl/logic_and_set_theory/02-kwantyfikatory-i-podstawowe-metody-dowodzenia.tex
cd application
python -m unittest tests.test_lean_ci_audit -v
cd lean
lake update
lake exe cache get
lake env lean src/LST02_Quantifiers.lean
```

Jeśli `lake update` lub dostęp do Mathlib zawiedzie,
nie raportować rzeczywistej kompilacji lokalnej jako PASS.
Porównać plik `lean-toolchain` i przypiętą rewizję
`lakefile.toml`; ewentualne uruchomienie lokalne odnotować
z dokładną wersją Lean i Mathlib.

**Już zgromadzone dowody CI**:
- [Workflow 2+1 #45208224201](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45208224201) — wszystkie trzy pełne rundy, `skeptical_contract` i `evidence` PASS.
- [Archiwum statusu #14837066604](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45208224201/artifacts/14837066604), SHA256 ZIP `e16754acbe13634884b037b941f171c0dbf6d52b619166d1f7dbb9038ba8c119`: `candidate_sha` powyżej, `fragment=L1.3`, `passes=[true,true,true]`, `problems=[]`, `status=stabilizing`, `skeptical_review=pending`, `certificate=false`.
- Każda runda: **736** testów aplikacji, **10** sklasyfikowanych pominięć, **0** nierozliczonych, Chromium **509** rozdziałów bez błędów JavaScript, Windows PASS.
- Rzeczywisty Lean **4.26.0** / Mathlib `2df2f0150c275ad53cb3c90f7c98ec15a56a1a67`, w każdej rundzie **5 plików i 25 deklaracji**, `axiom_check=passed`, MetaM PASS. Liczba 25 to **nie** liczba odrębnych powiązań źródło–Lean.

## 4. Decyzja uprawnionego, niezależnego recenzenta

Recenzent powinien osobno zapisać w uwierzytelnionym kanale
GitHub/organizacji:

- swoją tożsamość, niezależność od autora ocenianych zmian
  i dokładny SHA `163c8f6415d9d390fc1a737f6954b2865eff6c6e`;
- ocenę **każdej** z czterech pozycji tabeli (`accept`,
  `request_changes` albo `unresolved`), w tym powyższych
  granic semantycznych;
- źródła, które przeczytał, oraz rzeczywiste dowody kompilacji
  i aksjomatów, na których polega;
- jednoznaczny wynik `approve` lub `request changes`
  z uzasadnieniem.

Komentarz autora, automatyczny CI, ten raport oraz niesygnowany
wpis `semantic_review` w JSON **nie stanowią** takiej
decyzji. Jeśli recenzent wskaże potrzebne korekty, poprawić
**tę samą partię**, następnie nadać jej nowe SHA i uruchomić
pełne 2+1 od zera. Jeżeli decyzja jest pozytywna, dopiero
w **nowym commicie** przypiąć rzeczywisty SHA256 kanonicznego
TeX-u, zmienić odpowiednie statusy na `approved` wraz z
udokumentowanym uzasadnieniem recenzenta i przeprowadzić
ponowne techniczne 2+1 dla zmienionego manifestu; wyniku
`163c8f64` nie przenosić automatycznie na nowy SHA.

Dalszy pakiet **LA-01** i przejście do **L1.4.2** pozostają
zablokowane do spełnienia sekwencyjnego planu. W szczególności
pełny pilotaż L1.3 to **20–30 odrębnych mapowań**, obejmujących
LST-01, LST-02 i LA-01; bieżący manifest ma ich **9**.
