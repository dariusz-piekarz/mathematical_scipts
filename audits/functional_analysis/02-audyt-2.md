# Analiza funkcjonalna — rozdział 02 — audyt 02 (niezależny)

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Rozdział:** `chapters/pl/functional_analysis/02-podprzestrzenie-produkty-ilorazy-i-topologie-uniwersalne.tex`.  
**SHA obiektu Git źródła audytowanego rozdziału:** `0b2772a13459c13d9720e3726966981b289e2bed`.  
**Wynik matematyczno-redakcyjny:** bez nowych poprawek do LaTeX. **Pierwszy czysty audyt rozdziału 02 (1/2), pod warunkiem końcowego PASS rozszerzonego CI**. Nie przechodzić do rozdziału 03 przed potwierdzeniem stabilizacji 02.

## Metoda

Ponowna, niezależna kontrola pełnej treści rozdziału, nieprzyjmująca automatycznie ocen poprzedniego raportu. Kontrola wszystkich 14 dowodów i 7 przykładów, przypadków pustych rodzin indeksów i zerowej przestrzeni liniowej, otoczeń nieotwartych, ilorazów przez podprzestrzenie niedomknięte, normy ilorazowej i zupełności, argumentu o najsilniejszej dopuszczalnej topologii oraz nieciągłości działań w zwykłej topologii końcowej. Dodatkowo kontrola konwencji językowych, etykiet, składu i rysunku 2.1.

## Macierz matematyczna — 14/14 sprawdzonych dowodów

| Nr | Dowód | Niezależnie zweryfikowany krok | Wynik |
| --- | --- | --- | --- |
| 1 | Podprzestrzeń TVS | Produkty podprzestrzeni i przeciwobrazy zbiorów otwartych; dziedziczenie Hausdorffa | PASS |
| 2 | Domknięcie podprzestrzeni | Obie inkluzje `cl(M)=∩_{U∈N(0)}(M+U)`; symetryzacja otoczeń; działania liniowe i przypadek λ=0 | PASS |
| 3 | Własność uniwersalna podprzestrzeni | `f:Z→M` jest ciągłe wtedy i tylko wtedy, gdy `i∘f:Z→X` jest ciągłe | PASS |
| 4 | Produkt TVS | Rzuty otwarte i ciągłe; własność uniwersalna dla dowolnego Z; rozdzielanie punktów w iloczynie | PASS |
| 5 | Ograniczoność produktu | Każde otoczenie ogranicza tylko skończenie wiele współrzędnych; maksimum `t_i` i zrównoważenie `V_i`; przypadek `I=∅` | PASS |
| 6 | Funkcjonały na produkcie `K^I` | Ciągły funkcjonał znika na wektorach o zerowych współrzędnych indeksowanych przez skończone F; pozostała suma jest skończona | PASS |
| 7 | Iloraz TVS | Otwartość rzutowania, otwartość `q×q` i `id×q` jako surjekcji; ciągłość łączna działań; Hausdorff `⇔` domkniętość M | PASS |
| 8 | Własność uniwersalna ilorazu | Ciągłość według preobrazów; dobrze określone, jednoznaczne faktoryzowanie `T` z `M⊆ker T` | PASS |
| 9 | Pierwsze twierdzenie o izomorfizmie | Homeomorfizm `X/ker T→T(X)` `⇔` odwzorowanie `T:X→T(X)` otwarte | PASS |
| 10 | Norma ilorazowa i zupełność | Niezależność od reprezentanta, ścisła dodatniość przy M domkniętej, równość kul, izomorfizm topologii i dobór reprezentantów podciągu Cauchy’ego z sumowalnymi przyrostami | PASS |
| 11 | Topologia początkowa TVS | Preobrazy podbazy i uniwersalna własność; wspólna ciągłość działań; rozdzielanie punktów przez rodzinę `T_i` | PASS |
| 12 | Istnienie topologii końcowej TVS | Niepustość rodziny dopuszczalnych topologii, złączenie wszystkich tych topologii zachowuje ciągłość działań, a ciągłość `T_i` i własność uniwersalna są utrzymane | PASS |
| 13 | Skończone sumy proste | Ciągłość `S(x_1,…,x_n)=∑_i(S∘j_i)(x_i)`; wykorzystanie własności uniwersalnej topologii końcowej | PASS |
| 14 | Hausdorffyzacja | `N=cl{0}` podprzestrzenią domkniętą; `N⊆ker T` dla ciągłych liniowych T do przestrzeni Hausdorffa; jednoznaczność rozkładu | PASS |

### Dodatkowe próby obalenia twierdzeń

- **Pusty produkt:** dla `I=∅` produkt jest przestrzenią zerową, a warunek ograniczoności wszystkich rzutów jest pusty; w dowodzie `F=∅` wybór `t=1` jest prawidłowy.
- **Niedomknięta podprzestrzeń:** dla `M=c_{00}⊂ℓ²` iloraz `ℓ²/M` nie jest Hausdorffa, a seminorma ilorazowa zeruje się również na klasach niezerowych; nie przeczy to tezie wymagającej domkniętości M.
- **Iloraz `R²/ span(1,1)`:** odległość do podprzestrzeni wynosi `|a-b|/√2`; użyto jako niezależnej kontroli mechanizmu normy ilorazowej.
- **Końcowa topologia dwóch osi:** `{(1,1)}` jest otwarte jako zbiór o pustych przeciwobrazach przez oba włożenia, a `{(0,0)}` nie; przesunięcia nie są więc homeomorfizmami — zasadniczy kontrprzykład pozostaje poprawny.
- **Przestrzeń `φ=⊕_n K e_n`:** `e_n→0` współrzędnie, ale `p_{(1,1,…)}(e_n)=1`; sprawdzono osobno dowód ciągłości operatora do przestrzeni zadanej rodziną seminorm.
- **Pusta rodzina początkowa:** otrzymana topologia jest trywialna; warunek `∩_i ker T_i={0}` jest wtedy równoważny `X={0}`, co odpowiada kryterium Hausdorffa.

Nie stwierdzono nowej błędnej tezy ani luki wymagającej korekty źródła.

## Przykłady — 7/7 PASS

1. Wielomiany jako gęsta, niezupełna podprzestrzeń funkcji ciągłych w normie supremum.
2. Ciąg funkcji o przesuwającym się zwężającym nośniku: zbieżność punktowa bez zbieżności jednostajnej.
3. Ciągła bijekcja liniowa między dwiema różnymi topologiami normowymi bez ciągłej odwrotności.
4. Iloraz przez jądro wartościowania w zerze i jawny ciągły prawy odwrotny.
5. Produkty i podprzestrzenie jako przestrzenie z topologiami początkowymi.
6. Topologia końcowa dwóch osi w `R²` jako kontrprzykład ciągłości przesunięć.
7. Algebraiczna suma prosta `φ` z dwiema różnymi topologiami i kontrolą seminorm.

## Terminy, odsyłacze, ilustracja i PDF

- Zachowano **15 unikatowych etykiet**, **14 dowodów** i **7 przykładów**. Brak samodzielnego użycia angielskiego rzeczownika „dual” oraz sformułowania „rodziny map”; odwołania do rozdziałów 01 i 05 zachowano.
- Konwencje TVS Hausdorffa oraz jawne wyjątki nie-Hausdorffa nie prowadzą do sprzeczności.
- Ponowna analiza pliku PDF z prawidłowego przebiegu [45152793250](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45152793250): dokument ma **33 strony A4**, rozdział 02 występuje na stronach **7–15**.
- Obejrzano wszystkie strony 7–15 w układzie 3×3, w tym rysunek **2.1**. Kontrola położenia bloków tekstowych w PDF: wszystkie w obrębie strony; bez widocznego nakładania lub obcięcia napisów. Końcowy log LaTeX bez nierozwiązanych odsyłaczy i przepełnionych wierszy.
- Wzmocniono **wyłącznie testy**, bez zmiany rozdziału: `tools/tests/test_functional_analysis_ch02.py` z 9 do **12 testów**. Nowe testy sprawdzają iloraz przez prostą diagonalną w `R²`, przykład `c_{00}⊂ℓ²` i ograniczenie liczby współrzędnych ciągłego funkcjonału na produkcie. To kontrole pomocnicze; nie zastępują dowodów.

## CI i decyzja

- Poprzedni przebieg [45152793250](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45152793250): **9/9 PASS**, kompilacja z rzeczywistym kontekstem rozdziałów 01–05, kontrola PDF i odsyłaczy PASS.
- Rozszerzone CI (12 testów): **stan w chwili pisania wymaga potwierdzenia**. Wynik czystego audytu liczony jako 1/2 dopiero po potwierdzeniu PASS nowego przebiegu.
- **Rozdział 02: bez zmian merytorycznych po audycie 01, oczekuje drugiego czystego audytu potwierdzającego**. Do rozdziału 03 nie przechodzimy przed stabilizacją rozdziału 02.
