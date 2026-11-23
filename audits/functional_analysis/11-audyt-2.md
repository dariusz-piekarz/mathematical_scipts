# Analiza funkcjonalna — rozdział 11 — audyt 02 (pełny przegląd, poprawki i pierwsza bramka CI)

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6` — bez tworzenia nowych gałęzi.  
**Źródło:** `chapters/pl/functional_analysis/11-przestrzenie-frecheta-twierdzenia-o-odwzorowaniu-otwartym-i-wykresie-domknietym.tex`.  
**SHA przed audytem:** `ac11608f7af7af32c893cb5e77a3400d1fb7f993`.  
**SHA po poprawkach:** `73505ec4ff0f51ae76f0cfdf67cccd5eccbbd2b2`.  
**Werdykt:** **AUDYT Z POPRAWKAMI, NIE CZYSTY — 0/2**. Po zakończeniu tej iteracji rozdział 11 wymaga dwóch niezależnych czystych audytów identycznego źródła oraz zielonej bramki CI.

## Stan wejściowy i punkt kontynuacji

Po sprawdzeniu bieżącej gałęzi okazało się, że automatyzacja zapisała już `11-audyt-1.md`; nie powielano tego pliku. Raport 11/01 obejmował przegląd 10 dowodów i 6 przykładów, ale nie obejmował ani rzeczywistej kompilacji LaTeX, ani testów regresyjnych, ani inspekcji schematu TikZ. Zgodnie z zasadą stabilizacji jego stan wynosił 0/2, nie zaś 1/2. W rozdziale 10 potwierdzono już końcowe **2/2 + zielony GitHub Actions #45225001868**. Otwarto zatem kolejną jednostkę 11/02.

## Niezależny przegląd matematyczny 10 dowodów

1. **Metryka z przeliczalnej rodziny seminorm.** Każdy składnik `2^{-n}\min(1,p_n(x-y))` jest symetryczny i nieujemny; nierówność trójkąta wynika z subaddytywności `\min(1,\cdot)`. Oddzielanie punktów przez seminormy zapewnia dodatnią określoność. Kontrola pierwszych `N` składników i reszty szeregu daje zgodność topologii także dla sieci, a argument Cauchy'ego daje zgodność kanonicznej struktury jednostajnej.
2. **Stabilność podprzestrzeni, ilorazów i produktów przestrzeni Frécheta.** Domknięta podprzestrzeń dziedziczy zupełność. Dla domkniętego `M` ilorazowa metryka `\bar d(qx,qy)=\inf_{m\in M}d(x-y+m,0)` jest poprawna i Hausdorffa; rzutowanie `q` wysyła kule na kule. Dla ciągu Cauchy'ego w ilorazie można wybrać podciąg z odległościami kolejnych wyrazów `<2^{-k-1}`, a następnie reprezentantów różniących się w metryce o `<2^{-k}`; pełność `E` daje granicę. Przeliczalny produkt jest zupełny w metryce `\sum 2^{-j}\min(1,d_j)`.
3. **Krok Baire'a dla obrazu absolutnie wypukłego otoczenia.** Z surjektywności i pochłaniania `U` wynika `F=\bigcup_n nT(U)`. Domknięcia tych zbiorów są domknięte, Baire zapewnia niepuste wnętrze jednego z nich, a absolutna wypukłość pozwala przenieść wnętrze do otoczenia zera w `\overline{T(U)}`.
4. **Twierdzenie o odwzorowaniu otwartym.** Istnieje otwarte absolutnie wypukłe `U_0` z `\overline{U_0}\subset U`. Konstruowane `U_n` spełniają `U_n+U_n\subset U_{n-1}` oraz `U_n\subset A_n`. Z lematu Baire'a wybiera się `V_n\subset\overline{T(U_n)}\cap B_n`. Indukcja wyznacza `x_n\in U_n` z resztami `y-T\sum_{k\le n}x_k\in V_{n+1}`, a więc dążącymi do zera. Oszacowanie ogonów szeregu przez `U_{m-1}` zapewnia warunek Cauchy'ego sum częściowych; zupełność `E` daje `x\in\overline{U_0}\subset U` i `Tx=y`. Domknięcie argumentu przez translacje dowodzi otwartości dowolnego obrazu otwartego.
5. **Ciągłość operatora odwrotnego.** Dla liniowej bijekcji `T` obraz każdego otwartego `U\subset E` jest otwarty w `F`, czyli przeciwobraz `U` przez `T^{-1}` jest otwarty; wymagana ciągłość jest prawidłowo wyprowadzona.
6. **Oszacowanie normy operatora odwrotnego.** Ciągły liniowy `T^{-1}` pomiędzy Banachami jest ograniczony. Wybór `C=\max(1,\|T^{-1}\|)` zapewnia właściwy stały oszacowania także przy zerowej przestrzeni.
7. **Izomorfizm ilorazu przez jądro surjekcji.** `\ker T` jest domknięte, `E/\ker T` pozostaje Frécheta, a kanoniczny operator `\widetilde T` jest ciągłą liniową bijekcją; twierdzenie o ciągłości odwrotności stosuje się przy pełnych hipotezach.
8. **Kryterium ciągowe domknięcia wykresu.** Produkt dwóch metryzowalnych TVS jest metryzowalny, więc zbiór wykresu jest domknięty dokładnie wtedy, gdy zawiera granice wszystkich swoich zbieżnych ciągów. Sprawdzono konieczność hipotezy określenia operatora na całej `E`.
9. **Twierdzenie o wykresie domkniętym.** Jeśli `T` jest ciągły, wykres jest przeciwobrazem singletonu `\{0\}` przez ciągłe `(x,y)\mapsto y-Tx`. W drugą stronę zamknięty `G(T)` jest przestrzenią Frécheta jako domknięta podprzestrzeń produktu, a rzutowanie `P:G(T)\to E` jest liniową ciągłą bijekcją. Ciągłość `P^{-1}` implikuje `T=\pi_F\circ P^{-1}` ciągły.
10. **Równoważność zupełnych porównywalnych norm.** Identyczność `(V,\|\cdot\|_a)\to(V,\|\cdot\|_b)` jest liniową ciągłą bijekcją pomiędzy Banachami, więc jej odwrotność jest ciągła na mocy wcześniejszego wniosku i daje oszacowanie w drugą stronę.

**Kontrola dowodów:** 10/10 jednostek bez nowego kontrprzykładu wymagającego zmiany tezy. Stosowano niezależny przegląd argumentacji, nie formalną weryfikację Lean.

## Sześć przykładów i przypadki graniczne

1. **Przykłady Frécheta:** `\K^{\N}` jest zupełny współrzędnie; w `C^\infty([0,1])` jednostajna zbieżność każdej pochodnej prowadzi do funkcji `g_j`, a całkowa tożsamość i twierdzenie podstawowe rachunku całkowego zapewniają `g'_j=g_{j+1}`. Wcześniejsza wersja zbyt szybko przeskakiwała ten istotny krok. **Dowód w przykładzie rozpisano.**
2. **Bijekcja do niezupełnej przeciwdziedziny:** odwzorowanie identycznościowe `(\ell^1,\|\cdot\|_1)\to(\ell^1,\|\cdot\|_2)` jest ciągłą bijekcją, lecz nieotwartą; wektory z pierwszymi `n` współrzędnymi `1/n` mają normy `1` i `n^{-1/2}`.
3. **Domknięty wykres bez zupełnej dziedziny:** odwrotna identyczność z `(\ell^1,\|\cdot\|_2)` do `(\ell^1,\|\cdot\|_1)` jest nieciągła, lecz jej wykres jest domknięty dzięki jednoznaczności granic w `\ell^2`.
4. **Pochodna jako operator domknięty nieograniczony:** `D(T)=C^1([0,1])\subset C([0,1])`; `f_n=n^{-1}\sin(nt)` ujawnia nieograniczoność. Jeśli `f_n\to f` i `f'_n\to g` jednostajnie, to całkowa tożsamość zapewnia `f\in C^1` i `f'=g`. Pełna dziedzina hipotez twierdzenia nie zachodzi.
5. **Pochodna na `C^\infty([0,1])`:** `p_n(Df)\le p_{n+1}(f)` dowodzi ciągłości; całkowanie daje prawą odwrotność i surjektywność, a przestrzeń stałych jest jądrem. Z ilorazowego wniosku wynika odpowiedni izomorfizm topologiczny.
6. **Gęsty, niecały obraz `\ell^1\hookrightarrow\ell^2`:** obraz zawiera `c_{00}`, ale nie zawiera ciągu `(n^{-3/4})`, który należy do `\ell^2\setminus\ell^1`. Odwrotność na obrazie z topologią indukowaną jest nieciągła, bo przeciwdziedzina nie jest zupełna.

**Kontrola przykładów:** 6/6 logicznie poprawnych po dodaniu uzasadnienia zupełności `C^\infty`.

## Konkretne korekty wykonane w 11/02

- Usunięto niedopuszczony termin „zupełność sekwencyjna”. W jego miejsce wyraźnie odróżniono zupełność względem kanonicznej struktury jednostajnej od zbieżności samych ciągów Cauchy'ego przy braku założenia metryzowalności.
- Rozpisano brakującą całkową argumentację zupełności `C^\infty([0,1])`: jednostajna granica funkcji `f_n^{(j)}`, zbieżność pod całką, identyfikacja `g'_j=g_{j+1}` i zbieżność wszystkich seminorm. Commit `df6a4988fd8d93da38bd6ff9ff1796640d1a9881`.
- Po uruchomieniu nowych testów wykryto jeszcze dwa wystąpienia „sekwencyjne” w tytule i powołaniu kryterium domknięcia wykresu. Zamieniono na **„kryterium ciągowe”**. Commit `e031a92243475d69c78437b6f94efab333e7fa54`.
- Dodano **15 testów** regresyjnych `tools/tests/test_functional_analysis_ch11.py` obejmujących matematykę skończonych modeli, formuły kontrprzykładów, strukturę TeX, 16 odsyłaczy, terminologię i rysunek. Commit `d1cca14add09cf1bef6e82bce51f77f10c1d39cd`.
- Dodano dedykowany `.github/workflows/functional-analysis-ch11.yml` — prawdziwe uruchomienie testów, przygotowanie dokumentu z plików 01–11, kompilacja LaTeX, kontrola tekstowego wyniku i diagnostyki PDF oraz publikacja artefaktu. Commit `5116b7f609ca629ec1400a546da8a80d42c88377`.

## Rzeczywiste kontrole struktury i odsyłaczy

Pobrano ponownie pliki wszystkich rozdziałów **01–11** z bieżącej gałęzi. Łącznie znaleziono **202 etykiety bez duplikatów**. Rozdział 11 ma **20 etykiet** i **16 odsyłaczy**, wszystkie rozwiązane w źródłach 01–11. Wszystkie środowiska są poprawnie sparowane: 10 `proof`, 2 `definicja`, 2 `stwierdzenie`, 3 `twierdzenie`, 1 `lemat`, 4 `wniosek`, 6 `przyklad`, 4 `uwaga`, 1 `tikzpicture` i 1 `center`. Nie pozostały niedozwolone użycia „sekwencyjne”; obecny jest precyzyjny termin „ciągowe”. W źródle jest jeden schemat TikZ twierdzenia o wykresie domkniętym — do sprawdzenia wizualnie po uzyskaniu PDF.

## Bramki CI i dalsza stabilizacja

Pierwszy rzeczywisty przebieg dedykowanego CI [#45229321602](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45229321602) zakończył się **FAILURE** na teście terminologii, a więc nie uruchomił kompilacji LaTeX. Poprawiono źródło, nie rozluźniając kontraktu. Następny przebieg [#45229640597](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45229640597), na commicie `e031a92243475d69c78437b6f94efab333e7fa54`, przeszedł **15/15 testów** i przygotowanie kompletnego kontekstu 01–11; jego późniejsze etapy kompilacji i PDF należy zweryfikować wprost po ukończeniu. Nie przypisujemy statusu PASS krokom jeszcze nierozstrzygniętym.

**Werdykt 11/02: AUDYT Z POPRAWKAMI — 0/2.** Po zielonym CI i inspekcji PDF następna iteracja 11/03 powinna niezależnie skontrolować niezmienioną wersję źródła SHA `73505ec4ff0f51ae76f0cfdf67cccd5eccbbd2b2`; dopiero wtedy może uzyskać pierwszy czysty wynik 1/2. Rozdział 12 jest zablokowany.

## Zakończenie audytu 11/02 — CI i PDF

Po poprawkach rozdziału 11 dedykowany przebieg [GitHub Actions #45229640597](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45229640597) zakończył się **COMPLETED/SUCCESS**: **15/15 testów regresyjnych PASS**, kompletowanie 11 rzeczywistych `\input` PASS, kompilacja LaTeX PASS, automatyczna kontrola logów oraz PDF i odsyłaczy PASS, publikacja artefaktu `functional-analysis-ch11-pdf` PASS. Dokument pobrano z artefaktu **#14845897294**: `functional_analysis_ch11_context_ci.pdf`, **66 stron**. Rozdział 11 zajmuje strony **61–66**.

Przeprowadzono dodatkową **rzeczywistą inspekcję wizualną** wszystkich stron 61–66 na arkuszu podglądowym oraz osobno powiększono stronę **65** z diagramem TikZ. **Nie stwierdzono kolizji etykiet, obcięć wzorów, nachodzenia podpisu na rysunek ani bloków tekstu poza marginesami strony.** Programowa kontrola współrzędnych bloków tekstowych w PyMuPDF również nie wykazała przekroczeń prostokątów stron. Samo CI potwierdza budowę dokumentu i testy kontraktów, a nie stanowi formalnego dowodu twierdzeń.

Dodatkowy workflow wyzwolony zapisem pierwszej wersji niniejszego raportu ma identyczne SHA źródła i testów; jego końcowy rezultat należy sprawdzić osobno przed zamknięciem raportu. W tej iteracji **nie** zalicza się czystego przeglądu: źródło uległo zmianom terminologicznym i zostało rozszerzone matematyczne uzasadnienie przykładu.

**Ostateczny werdykt merytoryczny 11/02: AUDYT Z POPRAWKAMI, STABILIZACJA 0/2.** Następna niezależna kontrola 11/03 może rozpocząć pierwsze czyste zaliczenie wyłącznie na niezmienionym blobie `73505ec4ff0f51ae76f0cfdf67cccd5eccbbd2b2`, po potwierdzeniu zielonego CI.

## Ostateczne potwierdzenie CI dla audytu 11/02

Po zakończeniu inspekcji PDF i zapisaniu uzupełnionego raportu zakończył się najnowszy przebieg dedykowanego [GitHub Actions #45230359395](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45230359395), commit `220751fae228be67949156de8173457a89f05f6f`: **COMPLETED/SUCCESS**. Potwierdzono wszystkie kroki: **15/15 testów regresyjnych PASS**, przygotowanie kontekstu 01–11 PASS, kompilację LaTeX PASS, automatyczną kontrolę PDF i odsyłaczy PASS oraz przesłanie artefaktu PASS. Poprzedni przebieg raportu [#45230008006](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45230008006) również był zielony. Źródło rozdziału 11 pozostaje w blobie SHA `73505ec4ff0f51ae76f0cfdf67cccd5eccbbd2b2`.

**Bramka techniczna 11/02 jest ukończona; audyt pozostaje audytem z poprawkami (0/2).** Od następnej iteracji 11/03 wolno rozpocząć pierwszą niezależną kontrolę stabilizacyjną tego niezmienionego źródła. Rozdział 12 nadal czeka na 2/2 czystych audytów rozdziału 11.
