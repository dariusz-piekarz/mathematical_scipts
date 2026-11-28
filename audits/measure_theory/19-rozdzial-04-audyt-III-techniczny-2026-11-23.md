# Miara i całka — R04, audyt III techniczno-matematyczny (iteracja XIX)

**Data:** 2026-11-23. **Wyłącznie istniejąca gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Jedyny audytowany rozdział:** `chapters/pl/measure_theory/04-miara-lebesguea-na-przestrzeni-euklidesowej.tex`.  
**Blob rozdziału:** `77e4ad8551f55a2ff579aa171761ccdd01aaa918` (niezmieniony od poprawki audytu XVII).

## Odczytany stan wejściowy

Przed pracą sprawdzono stan gałęzi względem commitu audytu XVIII `c543acf5ed2ee0f54087aab7a145f9194fd65918`, najnowszy raport XVIII, aktualny tekst R04, preambułę `books/pl/measure_theory.tex`, istniejący workflow R03, odpowiednie fragmenty sąsiednich rozdziałów R01–R03 i obowiązujące standardy redakcyjne z poprzedniego audytu. Brak osobnego workflow R04 i raportu XIX przed tą iteracją potwierdzono odczytami repozytorium.

## Nowa weryfikacja spójności R04

Zebrano automatycznie z aktualnego źródła:
- 979 linii, 11 sekcji, 28 etykiet `\label` i 30 wystąpień `\ref`/`\eqref` (23 różne cele);
- wszystkie cele są zdefiniowane w R01–R04; żadnych powielonych etykiet w tej czwórce;
- 106 znaczników początku/końca środowisk LaTeX, bez błędów kolejności i niedomkniętych środowisk;
- dokładnie jeden rysunek TikZ, przedstawiający pierwsze etapy konstrukcji zbioru Cantora;
- brak niedozwolonych notacji funkcji charakterystycznej `\mathbf{1}`, `\mathbb{1}`, `\mathds{1}`, wyrażenia „zbieżność zdominowana” i „unia zbiorów”.

To jest statyczna kontrola struktury, a nie wynik kompilacji PDF. Rozdziały R01–R03 były tylko kontekstem rozwiązania odsyłaczy, nie przedmiotem nowego audytu.

## Nowe niezależne kontrole geometryczne

Dodano `tools/test_measure_theory_ch04_geometry.py` w commicie **`b375511f954f6c6bffdbda2de569bcee50e5a1aa`**. Test używa wyłącznie arytmetyki całkowitej i wymiernej:
1. 512 rodzin komórek na siatce 3×3; sprawdzenie 262 144 uporządkowanych par względem monotoniczności, podaddytywności oraz addytywności zbiorów rozłącznych.
2. Pierwsze 11 etapów klasycznego zbioru Cantora, z dokładnym rachunkiem długości `(2/3)^n`.
3. Pierwsze 10 etapów zbioru Smitha–Volterry–Cantora, z dokładną długością poszczególnych przedziałów i sumą długości `1/2+2^{-n-1}`.
4. Czternaście skończonych świadectw braku absolutnej ciągłości funkcji Cantora (suma przyrostów 1 przy malejącej sumie długości).
5. Dziewięć dokładnych oszacowań powierzchni pokrycia wykresu funkcji Lipschitzowskiej.

Niezależne lokalne wykonanie analogicznych obliczeń w Pythonie dało **PASS** dla wszystkich podanych rodzin przypadków. Nie należy mylić tych kontroli skończonych z dowodami twierdzeń dla dowolnych przestrzeni.

## Workflow kompilacji i wizualnej diagnostyki

Dodano `.github/workflows/measure-theory-ch04.yml` w commicie **`3be535595d6e4faa3ea79c3683c3a970f6ce34c4`**, z dwoma zadaniami:
- uruchamianie dokładnego testu geometrycznego;
- kompilacja izolowanego R04 na oryginalnej preambule, PDF dwukrotnie, tekst i bounding boxes słów, rasteryzacja stron do PNG, a następnie trzykrotna kompilacja pełnej książki wyłącznie do sprawdzenia odsyłaczy i integracji R04.

Archiwum GitHub Actions zawierać ma izolowany PDF, podglądy PNG, rozpoznane teksty i logi. Kontrola ramek sprawdza geometryczne wyjście słów poza strony, ale **nie gwarantuje** braku nakładania tekstu na rysunek: nadal konieczny rzeczywisty przegląd obrazu.

**Stan w chwili raportowania:** pliki workflow i skrypt zostały ponownie odczytane z GitHub i ich zawartość zweryfikowana. Interfejs GitHub dostępny w tej sesji nie udostępnił identyfikatora ani wyniku nowego przebiegu push Actions (lista uruchomień dla commitu w dostępnym endpointzie była pusta; endpoint ten dotyczy uruchomień PR). **Nie deklarujemy, że workflow przeszedł**. Po uzyskaniu numeru run należy sprawdzić oba wyniki, logi oraz pobrać/renderować PDF.

## Stan matematyczny i rozstrzygnięcie

Utrzymane ustalenia audytów XVII–XVIII: jedyną poprawką matematyczną w R04 była korekta przypadku zdegenerowanego prostopadłościanu przy nierówności pokryciowej; w kolejnych kontrolach nie stwierdzono nowej wykazanej usterki. W tej iteracji nie rozszerzano treści R04 ani nie zmieniano jego źródła.

**STATUS R04: NIEZATWIERDZONY — techniczna stabilizacja w toku.** Zamknięto statyczną kontrolę odsyłaczy i struktur; przygotowano osobne testy i workflow, ale wymagana jest faktyczna weryfikacja zielonego CI, kontrola wynikowego PDF (zwłaszcza rysunku Cantora) i kolejny czysty audyt po ostatnich zmianach technicznych.

**Kolejna iteracja:** tylko R04; nie przechodzić do R05.
