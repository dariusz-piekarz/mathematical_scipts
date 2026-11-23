# Teoria miary / Miara i całka — rozdział 03, samodzielny audyt I (iteracja globalna XV)

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Audytowany plik:** `chapters/pl/measure_theory/03-miary-zewnetrzne-i-konstrukcja-caratheodoryego.tex`. Zgodnie z regułą **dokładnie jednego rozdziału** w tej iteracji nie audytowano ani nie edytowano treści R01–R02 lub R04–R31; sąsiednie rozdziały posłużyły wyłącznie do potwierdzenia celów odsyłaczy.

## 1. Rzeczywisty stan wejściowy

Odczytano z GitHuba aktualny HEAD gałęzi `46aeb1dce37109fc04c2f57c8fd7600a9f902703`, najnowsze commity i katalog raportów `audits/measure_theory/`. Ostatni raport dotyczący rozdziału 02 (`14-rozdzial-02-audyt-III-2026-11-23.md`) certyfikował R02 jako stabilny; wcześniejszy R01 również posiada potwierdzoną stabilność. Nie istniał raport osobnego audytu R03 w bieżącej serii.

Pobrano aktualny R03 (blob **`842d9468bee76b11b0ea4805f1ae1363f166d9f5`**, 522 linii przed zmianą), `books/pl/measure_theory.tex`, `books/pl/integration_theory.tex`, `AGENTS.md` i `docs/pl/standardy_terminologiczne.md`. Nie scalano obu książek, nie dodano nowych twierdzeń, nie zmieniano zaakceptowanego zakresu.

## 2. Pierwszy samodzielny przegląd matematyczny całego R03

Przeczytano wszystkie **7 sekcji i 1 podsekcję**, w tym **6 twierdzeń, 2 lematy, 4 definicje, 4 przykłady, 4 uwagi i 8 dowodów**. Kontrolowano wszystkie jawne hipotezy, kwantyfikatory, wyjątkowe przypadki `∞`, granice szeregów, poprawność i zupełność argumentów oraz interpretację kontrprzykładów.

- **`thm:outer-from-cover`:** sprawdzono istnienie pokryć i wymóg `c(∅)=0`, monotoniczność infimum oraz przeliczalną podaddytywność z pokryciami o błędzie `ε2^{-j}`; przypadek nieskończonej sumy jest poprawnie rozdzielony.
- **`thm:caratheodory`:** niezależnie oceniono wszystkie sześć etapów konstrukcji σ-algebry, addytywność na mierzalnych zbiorach i zupełność; również sytuacje `μ^*(T)=∞` nie wymagają odejmowania nieskończoności.
- **`lem:premeasure-cover`:** rozłącznienie pokrycia po przecięciu z `A` pozostaje w algebrze; użycie przeliczalnej addytywności premiary jest dopuszczalne, ponieważ suma jest równa `A∈𝒜`.
- **`thm:premeasure-continuity`:** dla ciągu malejącego do zbioru pustego różnica kolejnych wyrazów ma rozłączną sumę `A_1`, a suma szeregu jest skończona dzięki `μ_0(X)<∞`; w odwrotnym kierunku reszty `R_N↓∅`.
- **`thm:extension-caratheodory`:** sprawdzono mierzalność elementów algebry przez rozdzielenie każdego pokrycia, zgodność `μ_c^*(A)=μ_0(A)` za pomocą lematu o pokryciach, oraz rozróżnienie pełnej σ-algebry Carathéodory'ego od `σ(𝒜)`.
- **`thm:extension-uniqueness`:** warunek σ-skończoności daje wspólne wyczerpanie w algebrze, dzięki czemu miary ograniczone są skończone i zgodne na generatorze π; następnie działa ciągłość z dołu.
- **`lem:outer-approx-algebra` i `thm:caratheodory-completion`:** kontrola aproksymacji mierzalnych zbiorów z góry przy skończonej masie, ograniczenie błędów przez `2^{-n}/k` oraz obustronne przybliżenie `C⊆E⊆D` ze zbiorem `D\C` miary zero.

## 3. Rzeczywista poprawka merytoryczna

**Uwaga „Rola założeń” po `thm:outer-from-cover`** sugerowała, że równość `μ_c^*(C)=c(C)` jest możliwa **dopiero** wtedy, kiedy `c` jest premiarą. Jest to zbyt silne i może być odczytane jako fałszywa konieczność.

Kontrprzykład diagnostyczny: `X={a,b}`, `𝒞=P(X)`, `c(∅)=0` i `c(C)=1` dla każdego niepustego `C`. Funkcja `c` nie jest premiarą (`c(X)=1`, zaś `c({a})+c({b})=2`), ale **`μ_c^*(C)=c(C)` dla każdego `C∈𝒞`**.

Poprawiono wyłącznie zdanie o konieczności na precyzyjne stwierdzenie, że gdy `𝒞` jest algebrą, a `c` premiarą, to równość jest gwarantowana; **hipoteza jest wystarczająca, lecz niekonieczna**. Nie dodano nowego przykładu do tekstu (kontrprzykład jest wyłącznie w raporcie i teście), zachowano wszystkie historyczne etykiety i dotychczasową treść rozdziału.

- Commit poprawki: **`a3fdeb4ea86fa07e845c05df07a988cc175f2870`**.
- Ponowny odczyt GitHuba: nowy blob R03 **`3c95138c4dc60b892835e8c9bc8421c70666ee72`**, 529 linii.

## 4. Testy niezależne od dowodów — wykonane w tej iteracji

Dodano `tools/test_measure_theory_ch03_outer.py`, commit **`fe892d46a8f08ff93eaa543fc51c0b9ce9bcd053`**, z wyczerpującym przeszukaniem modeli skończonych, a następnie workflow `.github/workflows/measure-theory-ch03.yml`, commit **`760d8a7723ef0da8d9d0adc18d884af6ac2ab350`**.

Test uruchomiono **rzeczywiście** w środowisku Python na 3-elementowej przestrzeni (wszystkie **81** miar zewnętrznych o wartościach z `{0,1,2,∞}`; liczby rodzin Carathéodory'ego: 16 o 2 zbiorach, 27 o 4, 38 o 8). Kontrola obejmuje kryterium Carathéodory'ego, zamknięcie na dopełnienia i sumy, addytywność, zupełność.

Na czteroelementowej przestrzeni wyliczono **15 algebr** wyznaczonych podziałami i **756** modeli premiar o wagach z `{0,1,2,∞}`. Sprawdzono w nich koszt pokryć, równość kosztu i miary zewnętrznej na algebrze, mierzalność Carathéodory'ego, addytywność, domknięcie uzupełnienia, a dla **309** modeli σ-skończonych równość rodziny Carathéodory'ego i uzupełnienia; łącznie **9812** instancji zbiorów mierzalnych.

Osobny test weryfikuje kontrprzykład diagnostyczny do błędnej konieczności premiary. Wszystkie trzy moduły zgłosiły `PASS` lokalnie. Wyniki **nie zastępują ogólnych dowodów**, lecz stanowią niezależną regresję.

**CI:** nowy workflow ma dwa joby: `chapter-03-finite-models` uruchamia test, a `chapter-03-pdf-and-book-context` kompiluje izolowany R03 dwukrotnie oraz pełną książkę trzykrotnie wyłącznie w celu sprawdzenia odsyłaczy i składu R03. Powstały PDF oraz logi są archiwizowane. Przebieg **[45134011603](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45134011603)** na commitcie `760d8a7723ef0da8d9d0adc18d884af6ac2ab350` — job modeli skończonych uzyskał `success`; kompilacja była w toku podczas pierwszego odczytu. Końcowy wynik należy potwierdzić osobno.

## 5. Kontrola LaTeX i terminologii

Po poprawce: **18 unikalnych etykiet**, **25 odsyłaczy**, **38 poprawnie sparowanych par środowisk**; brak niezrównoważonych środowisk i duplikatów etykiet. Sześć różnych celów zewnętrznych zostało rzeczywiście odnalezionych: pięć w R02 (`ch:miary-wlasnosci`, `ex:counting`, `thm:uniqueness-finite`, `thm:measure-continuity`, `thm:completion`) i jeden w R04 (`ch:lebesgue`). R02 i R04 odczytano wyłącznie w zakresie koniecznym do potwierdzenia odsyłaczy.

Brak `\\mathbf{1}`, `\\mathbb{1}`, `\\mathds{1}`, „zbieżność zdominowana” i „unia zbiorów”. Zgodność z `AGENTS.md` i globalnym standardem terminologicznym zachowana. **W R03 nie ma środowisk `figure` ani `tikzpicture`**; nie ma rysunków z napisami do skontrolowania.

## 6. Status i otwarte sprawy

**ROZDZIAŁ 03: AUDYT I WYKONANY, FORMALNIE JESZCZE NIESTABILNY.**

Powód: w tej iteracji nastąpiła **rzeczywista poprawka** tekstu. Zgodnie z protokołem wymaga to **kolejnego pełnego, niezależnego, czystego audytu tego samego rozdziału na nowym blobie**, w tym sceptycznej oceny poprawionego fragmentu i innych twierdzeń. Należy też zamknąć kontrolę CI i realny przegląd wyrenderowanego PDF R03. Sam fakt pozytywnych testów skończonych nie oznacza stabilności.

**Następna iteracja:** audyt II wyłącznie R03; potwierdzić bieżący CI, skontrolować strony i hiperłącza w PDF, ponownie przeanalizować wszystkie dowody. Nie przechodzić do R04 przed wyraźnym certyfikatem stabilności R03.
