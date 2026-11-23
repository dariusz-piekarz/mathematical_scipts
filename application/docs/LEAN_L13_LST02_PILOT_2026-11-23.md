# L1.3 — iteracja pilotażowa LST-02 (kandydaci do recenzji)

**Zakres:** jeden pakiet czterech mapowań dla kanonicznego
`LST-02`, bez ingerencji w plik LaTeX, starych formalizacji LST-01,
weryfikowany kandydat L1.4.1 ani status tamtego 2+1.

## Odwzorowania

| Oryginalna etykieta LaTeX | Deklaracje Lean | Co należy sprawdzić |
| --- | --- | --- |
| `thm:negation-quantifiers` | `lst02_not_forall`, `lst02_not_exists` | Obie równoważności, klasyczna logika, domena także pusta |
| `thm:same-quantifier-order` | `lst02_swap_forall`, `lst02_swap_exists` | Wymiana obu kwantyfikatorów tego samego typu bez założenia niepustości |
| `thm:swap-mixed` | `lst02_mixed_quantifier_forward`, `lst02_mixed_empty_counterexample` | Tylko poprawny kierunek implikacji; drugi pomocniczy kontrprzykład dla pustych dziedzin |
| `thm:unique-expansion-xli` | `lst02_unique_exists_expansion` | Definicyjne rozwinięcie `∃!` do istnienia i jednoznaczności |

Przepisanie nie wzmacnia hipotez o niepustości, nie wprowadza
nieudowodnionych aksjomatów i nie zmienia kanonicznego tekstu.
Twierdzenie o przeciwprzykładzie jest deklaracją **pomocniczą**,
nie dodatkowym mapowaniem źródłowym.

**Etap oceniania:** `statement_status=needs_review`,
brak `source_document_sha256` i brak `approved`. To celowe:
`formalization_status=draft` nawet przy prawidłowym bieżącym
dokumencie, dopóki nie zostanie wykonana osobna recenzja semantyczna
i przypięty digest oryginału. Sama kompilacja Lean, testy
statyczne i `axiom_check` nie mogą nadać `approved` ani
`certificate=true`.

## Kryteria dalszego odbioru

1. Potwierdzić, że wszystkie cztery etykiety należą do rzeczywistych
   środowisk `twierdzenie` w LST-02 i obejmują całe tezy,
   a status katalogu odróżnia `draft` od `approved`.
2. Uruchomić rzeczywisty Lean 4.26.0 i przypięty Mathlib na nowym
   `LST02_Quantifiers.lean`; skontrolować wszystkie siedem
   `#print axioms`, w szczególności `Classical.choice`
   dla pierwszej negacji. Nie traktować offline mocków jak kompilacji.
3. Sprawdzić negatywne przypadki pustych domen i brak odwrotnej
   implikacji przy mieszanych kwantyfikatorach.
4. Oddzielny recenzent ocenia dokładny zakres matematyczny
   i kwalifikuje mapowania do `approved`. Następnie przypiąć
   SHA256 kanonicznego źródła (bez żadnej edycji TeX) i
   przeprowadzić techniczne 2+1 na niezmiennym SHA.
5. Raportować odrębnie wpisy manifestu, deklaracje rzeczywiście
   kompilowane oraz recenzowane powiązania. Ukończenie całego
   pilotażu 20–30 i LA-01 pozostaje otwarte w issue #11.

**Brak certyfikatu semantycznego:** `certificate=false`.


## Audyt semantyczny mapowań LST-02 — kontrola wewnętrzna (23.11.2026)

**Audytowany commit kodu:** `163c8f6415d9d390fc1a737f6954b2865eff6c6e`.  
**Źródło kanoniczne:** `chapters/pl/logic_and_set_theory/02-kwantyfikatory-i-podstawowe-metody-dowodzenia.tex`;
Git blob `000ad4c0185eb2296ad7af3523ad30b08dfeebaf`.
**Plik Lean:** `application/lean/src/LST02_Quantifiers.lean`.

Ten przegląd obejmuje wszystkie **cztery** etykiety należące do
środowisk `twierdzenie` w rozdziale LST-02; zachowano kwantyfikatory,
kierunki implikacji, puste dziedziny i ograniczenia logiki klasycznej.
Jest to **samodzielny audyt pomocniczy**, a nie niezależny,
uwierzytelniony odbiór i nie automatyczne zatwierdzenie manifestu.
Wszystkie cztery wpisy nadal `statement_status=needs_review`.

### 1. `thm:negation-quantifiers`

Źródło: dla dowolnej dziedziny `D` (również pustej) i predykatu
`P`, w logice klasycznej zachodzą oba prawa:

`¬(∀ x∈D, P(x)) ↔ ∃ x∈D, ¬P(x)` oraz
`¬(∃ x∈D, P(x)) ↔ ∀ x∈D, ¬P(x)`.

`lst02_not_forall` i `lst02_not_exists` mają te same formuły,
bez dodania `Nonempty D` lub `Inhabited D`. W Lean
`{D : Type u}` dopuszcza też `Empty`; kwantyfikacja po
ogólnej klasie obiektów `D` jest reprezentowana przez kwantyfikację
po dowolnym typie. Klasyczna zasada użyta w pierwszej równoważności
jest jawna przez `classical`. Dla `D = Empty` oba prawa
są poprawne: kwantyfikator ogólny jest prawdziwy, a egzystencjalny
fałszywy.

**Rzeczywiste aksjomaty z logu Lean 4.26.0**:
`lst02_not_forall` — `[propext, Classical.choice, Quot.sound]`;
`lst02_not_exists` — brak zależności od aksjomatów. Ich dozwolenie
przez CI jest kontrolą jądra, a nie dowodem semantycznego odwzorowania
oryginału.

### 2. `thm:same-quantifier-order`

Źródło zakłada dowolne dziedziny `D,E` i predykat `P(x,y)`.
`lst02_swap_forall` sprawdza równoważność
`∀ x:D, ∀ y:E, P x y ↔ ∀ y:E, ∀ x:D, P x y`.
`lst02_swap_exists` sprawdza analogiczne
`∃ x:D, ∃ y:E, P x y ↔ ∃ y:E, ∃ x:D, P x y`.

W obu kierunkach Lean zachowuje kolejność argumentów predykatu
`P x y`: przestawia wyłącznie kwantyfikatory, nie myli
`P(x,y)` z `P(y,x)`. Brak założeń niepustości, także w
przypadku `D = Empty` lub `E = Empty`. Obie deklaracje
nie zależą od dodatkowych aksjomatów w logu `#print axioms`.

### 3. `thm:swap-mixed`

Źródło zawiera jednostronne twierdzenie:
`(∃ y:E, ∀ x:D, P x y) → (∀ x:D, ∃ y:E, P x y)`,
z informacją, że odwrotność jest ogólnie fałszywa.

`lst02_mixed_quantifier_forward` używa **jednego i tego samego**
świadka `y` dla dowolnego `x`; nie wnosi niejawnej
hipotezy `Nonempty E`. Obowiązuje także przy pustym `D`.
`lst02_mixed_empty_counterexample` to **pomocniczy** dowód
fałszywości odwrotności: przy `D = Empty`, `E = Empty`
właściwość `∀ x:D, ∃ y:E, False` jest prawdziwa pusto,
lecz `∃ y:E, ∀ x:D, False` jest fałszywa. Źródło zawiera
również kontrprzykład z liczbami naturalnymi; pomocniczy przykład
Lean świadczy o tym samym braku ogólnej odwrotności, ale **nie
formalizuje przykładu arytmetycznego z tekstu**. Nie liczymy
go jako piątego mapowania. Obie deklaracje mają brak
zależności od dodatkowych aksjomatów w logu Lean.

### 4. `thm:unique-expansion-xli`

`lst02_unique_exists_expansion` zestawia
`(∃! x:D, P x)` z
`∃ x:D, P x ∧ ∀ y:D, P y → y = x`. Zachowano kierunek
równości `y=x`, zakres wszystkich kwantyfikatorów
i brak założenia o niepustości. Definicyjny dowód `rfl`
odwzorowuje rozwinięcie Lean `ExistsUnique`; również dla
`D = Empty` obie strony są fałszywe. Log `#print axioms`
nie wykazał dodatkowych aksjomatów.

### 5. Niezależne liczniki i granice dowodu

Na kodzie `163c8f64` [pełny CI aplikacji
#45206502457](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45206502457)
uzyskał **736** testów, w tym 10 sklasyfikowanych pominięć,
0 nierozliczonych, Chromium **509** rozdziałów i zero błędów
JavaScript. [Rzeczywisty CI Lean
#45206502490](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45206502490)
zakończył się `success`: **5 plików, 25 deklaracji** skompilowanych
i zbadanych pod kątem aksjomatów. Spośród tych 25 **siedem**
jest nowych w LST-02. W rejestrze istnieją **4 nowe mapowania
LST-02**, a nie 7; łączna liczba wpisów manifestu to 9.

[Techniczny 2+1 #45208224201](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45208224201)
**zakończony sukcesem, 3/3 rund PASS** na niezmiennym kodzie `163c8f64`.
W każdej rundzie 736 testów aplikacji (10 sklasyfikowanych pominięć,
0 nierozliczonych), Chromium 509 rozdziałów bez błędów JavaScript,
5 plików i 25 rzeczywiście skompilowanych twierdzeń Lean 4.26.0
z `axiom_check=passed`; natywny Windows i regresje Lean PASS.
[Końcowy raport](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45208224201/artifacts/14837066604)
ma `problems=[]`, `status=stabilizing`, `skeptical_review=pending`,
`certificate=false`. Sceptyczna bramka kontraktowa i zadanie agregacji
zakończyły się sukcesem, ale nie zastępują recenzji semantycznej. Jeśli
nowe testy lub kod ulegną zmianie, konieczny będzie nowy SHA i
reset licznika. Aktualnego przeglądu nie zaliczać jako
niezależnej aprobującej recenzji.

**Następny warunek:** niezależny recenzent powinien sprawdzić
odpowiedniość stwierdzeń, w szczególności reprezentację dziedzin
przez typy Lean, brak założenia niepustości, użycie klasycznej
logiki i fakt, że arytmetyczny kontrprzykład źródłowy nie jest
dosłownie odwzorowany. Dopiero po osobnym odbiorze można
rozważyć `approved` i przypięcie SHA256 TeX. `certificate=false`
pozostaje obowiązujące.
