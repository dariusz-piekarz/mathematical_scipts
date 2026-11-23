# Teoria grafów i węzłów — audyt globalny 31: rozdziały 40–42, drugie niezależne przejście

Data: 2026-11-23. Repozytorium: `dariusz-piekarz/mathematical_scipts`.
Gałąź: istniejąca `biblioteka-matematyczna-iteracja-6`; nie tworzono nowej.
Poprzedni etap: audyt 30, pierwsze przejście 40–42 — PASS, raport `51-globalny-audyt-30-rozdzialy-40-42-pierwsze-przejscie.md`. Rozdziały źródłowe 01–39 pozostają lokalnie stabilne.

## Niezależna kontrola matematyczna

### Rozdział 40 — wymagana poprawka twierdzenia o drogach rozłącznych

W `thm:tg-flow-integral-paths` pierwsze przejście dopuszczało przepustowości `c(a)∈{0,1}`, ale utożsamiało maksymalną liczbę dróg rozłącznych krawędziowo z najmniejszą liczbą łuków, których usunięcie niszczy **wszystkie** skierowane drogi w pierwotnym grafie. Jest to fałszywe, jeśli drogi mogą używać łuków o przepustowości 0.

**Minimalny kontrprzykład:** `V={s,t}`, jeden łuk `s→t`, `c(s,t)=0`. Wartość maksymalnego dopuszczalnego przepływu jest równa 0, podczas gdy w pierwotnym grafie istnieje droga skierowana, do której usunięcia trzeba skasować jeden łuk.

**Wprowadzona korekta:** zdefiniowano `D_+=(V,{a∈A:c(a)=1})`; zarówno rodzina dróg rozłącznych krawędziowo, jak i minimalna liczba łuków rozdzielających `s,t` odnoszą się teraz **wyłącznie do D_+**. W dowodzie uzasadniono, że rozkład dodatniego przepływu nie korzysta z łuków pojemności 0, a pojemność przekroju równa się liczbie jego łuków w `D_+`.

**Druga wymagana korekta założenia:** jawnie dodano `k=|f|≥0` dla rozkładu na skierowane drogi `s→t`. Sam warunek `0≤f(a)≤c(a)` i zachowanie przepływu poza `s,t` nie zabraniają przepływu o ujemnej wartości: dla pojedynczego łuku `t→s` z przepływem 1 wartość bilansu wypływu ze źródła wynosi −1. Taka wartość nie może być sumą dodatnich krotności dróg `s→t`.

Zachowano istniejący label `thm:tg-flow-integral-paths`, historię odsyłaczy, wszystkie pozostałe twierdzenia i zatwierdzony zakres rozdziału.

### Rozdział 41 — drugie sprawdzenie oszacowań ekstremalnych

Ponownie skontrolowano argument symetryzacji Zykowa, warunki twierdzenia Turána, dowód nierówności Caro–Weiego przez losową permutację, liniowość wartości oczekiwanej, Cauchy'ego–Schwarza oraz przypadki równości. Dodatkowy, niezależny orakl enumeruje wszystkie proste grafy na 1–5 wierzchołkach, dokładnie oblicza liczbę niezależności i wyznacza funkcję ekstremalną `ex(n,K_{r+1})` dla wszystkich badanych `r`. Równość Caro–Weiego sprawdzono także dla `K_2 ⊔ K_3`.

W sprawdzonym zakresie nie wykryto nowego kontrprzykładu wymagającego zmiany rozdziału.

### Rozdział 42 — niezależna enumeracja całych przestrzeni probabilistycznych

Ponownie wyprowadzono wzory na pierwsze dwa momenty liczby trójkątów i wierzchołków izolowanych, rozróżniając pary konfiguracji bez wspólnej krawędzi od par z krawędzią wspólną. Niezależny orakl enumeruje każdy oznaczony graf na `n=3,4,5` w modelach `G(n,p)` dla `p=1/3,1/2,2/3`, z dokładnymi wagami wymiernymi. Sprawdza dokładną średnią, wariancję i przypadek `P(G(3,p)\text{ spójny})=3p²−2p³`. Sprawdzono też skalowanie drugiego momentu w dowodzie progu dla `K_r`, przy stałym `r`.

W sprawdzonym zakresie nie wykryto nowego kontrprzykładu wymagającego zmiany rozdziału.

## Nowy niezależny pakiet regresyjny

Dodano `tools/tests/test_graph_and_knot_flow_extremal_random_second_pass.py` i osobny krok `Second independent exact path-packing, extremal and random moments audit (40-42)` w `.github/workflows/graph-and-knot-global-audit.yml`; nowa ścieżka testu została również dodana do filtrów `push.paths`.

**Lokalny wynik uruchomienia nowego skryptu: PASS.**

- Rozdział 40: **4564** tożsamości maksymalnego pakowania prostych skierowanych dróg i minimalnego przekroju na grafach o 2–4 wierzchołkach (wszystkie konfiguracje) oraz 5 wierzchołkach (400 deterministycznie generowanych konfiguracji); osobno jawny kontrprzykład z łukiem pojemności 0. Pakowanie oblicza się przez przeszukanie rodzin dróg, a przekrój niezależnie przez enumerację podzbiorów wierzchołków — bez odwoływania się do implementacji max-flow.
- Rozdział 41: **1099** wszystkich prostych grafów o 1–5 wierzchołkach, dokładne oszacowania Caro–Weiego i wszystkie analizowane przypadki twierdzenia Turána; przykład `K_2 ⊔ K_3`.
- Rozdział 42: **3288** dokładnych ważonych przypadków `G(n,p)` i kontrola trójkątów, izolowanych wierzchołków oraz spójności małego modelu.

Te liczby nie są sumą różnych losowych instancji testu pierwszego przejścia. Nie należy też utożsamiać regresji skończonych z dowodem ogólnych twierdzeń.

## Commity źródeł i CI

- Korekta zera w pojemnościach i podgrafu `D_+`: `0a83056b95482ac0e3dce8fcdab7518df623b615`.
- Nowy zestaw testów: `204800dcad6c74a8d13eb22be5c5ace560d1fc58`.
- Włączenie testu do workflow: `4abb6f85fb04d9c8e12d37225c810bc25d4e4c49`.
- Jawne założenie nieujemnej wartości przepływu: `08d5d6303972297250fa2acb2e96e013dfacea1e`.

W trakcie tej iteracji odczyt statusów po commicie `08d5d630...` zwrócił puste listy statusów i przebiegów; interfejs pobierania przebiegów po SHA nie pokazuje przebiegów typu `push`. **Nie jest to dowód sukcesu CI ani jego awarii.** Pełne zadania `structural-audit` i `full-book-pdf`, wygenerowany PDF, ostrzeżenia LaTeX oraz oględziny stron 40–42 wymagają potwierdzenia dla wersji ze wszystkimi powyższymi zmianami.

## Werdykt i bramka stabilizacji

**Audyt 31: korekty matematyczne wdrożone, lokalne niezależne regresje PASS; CI i PDF niepotwierdzone — W STABILIZACJI.**

Aby zamknąć 40–42 i uznać rozdziały źródłowe 01–42 za lokalnie stabilne, trzeba uzyskać na końcowym SHA sukces `structural-audit` z nowym krokiem, sukces `full-book-pdf`, brak błędów odsyłaczy i ostrzeżeń kompilacji oraz rzeczywistą kontrolę stron poprawionego rozdziału 40. Nie zamykać audytu 31 na podstawie samego uruchomienia lokalnego.

Dopiero po stabilizacji przejść do pierwszego szczegółowego audytu pozostałych rozdziałów źródłowych 43–44. Globalny audyt wszystkich 44 rozdziałów jest nadal otwarty.


## Kontynuacja audytu 31 — regresja hipotez w źródle (2026-11-23)

W kolejnym przebiegu wykryto ryzyko w samym mechanizmie testów: poprzednia enumeracja potwierdzała poprawne twierdzenie o drógach w podgrafie dodatnich przepustowości, lecz nie wykrywałaby przypadkowego usunięcia tego ograniczenia z pliku LaTeX. Jest to regresja jakości kontroli, a nie kolejny błąd dowodu.

**Zastosowane zabezpieczenie:** w istniejącym teście drugiego przejścia dodano funkcję \`verify_source_hypotheses()\`. W czasie wykonywania CI otwiera ona rzeczywisty plik źródłowy rozdziału 40, izoluje twierdzenie \`thm:tg-flow-integral-paths\` i wymaga:
- jawnego założenia \`k=|f|≥0\`;
- definicji \`D_+\` i ograniczenia do łuków o przepustowości 1;
- obu wystąpień ograniczenia w tezie o drogach i rozcinających łukach;
- uzasadnienia w dowodzie, że nie wolno liczyć ścieżek korzystających z łuków o przepustowości 0.

**Commit zabezpieczenia:** \`556587924ede7975e2339cd2190f82770c2f1fdc\`.

**Rzeczywista weryfikacja wykonana w tej iteracji:** uruchomiono niezależny pakiet dokładnych testów z lokalnej kopii pliku — 4564 kontroli dróg/przekrojów, 1099 kontroli ekstremalnych i 3288 przypadków modelu \`G(n,p)\`, wszystkie PASS. Następnie przeprowadzono lokalne uruchomienie rozszerzonego pakietu w *syntetycznej strukturze repozytorium*, na reprezentatywnym fragmencie TeX zawierającym wymagane hipotezy; nowa kontrola źródła również PASS. Niezależnie przez konektor GitHub odczytano **prawdziwy źródłowy rozdział 40** na istniejącej gałęzi i sprawdzono obecność wszystkich wymaganych fragmentów — komplet PASS. Test na fragmencie syntetycznym **nie jest** równoznaczny z przebiegiem CI na całej książce.

**Pozostaje otwarte:** sprawdzenie rzeczywistych przebiegów GitHub Actions typu push i wyników obu jobów dla commitu z nowymi testami, pełny 44-rozdziałowy PDF, kontrola ostrzeżeń, odsyłaczy i oględziny zmienionych stron. Narzędzie do odczytu przebiegów po SHA udostępnia wyłącznie przebiegi PR, dlatego pusta lista nie daje żadnego wniosku o statusie przepływu uruchamianego przez push.

**Werdykt bez zmian: audyt 31 W STABILIZACJI.** Nie rozpoczynać audytu rozdziałów 43–44 przed zamknięciem bramki jakości dla 40–42.
