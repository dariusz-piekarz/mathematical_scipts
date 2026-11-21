# Algebra liniowa — rozdział 06, audyt 2 (stabilizacyjny)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/linear_algebra/06-wyznaczniki-macierzy.tex`  
**SHA skontrolowanej treści:** `ca2041609035de1bbe8ce390ccc23c0369d726fb`

## Założenia i definicje

Ponownie skontrolowano bez dodawania nowego materiału całą treść rozdziału: permutacje i parzystość inwersji, definicję wyznacznika przez permutacje, normalizację dla rozmiaru `0×0`, wieloliniowość i naprzemienność, operacje elementarne, wyznaczniki macierzy trójkątnych, transpozycję, multiplikatywność, odwracalność, podobieństwo, rozwinięcie Laplace'a, macierz dołączoną i wzory Cramera. Wszystkie definicje i tezy określają ciało, rozmiar i zakres parametrów; wymaganie `n≥1` występuje przy minorach, rozwinięciu Laplace'a, macierzy dołączonej i wzorach Cramera.

## Niezależna ocena dowodów

1. Znak zamiany dwóch wierszy wynika z naprzemienności i wieloliniowości; samo `det B=-det A` nie jest użyte do wykazywania zerowania przy identycznych wierszach. W charakterystyce `2` dowód przez parowanie przeciwnych składników nadal daje dokładnie zero.
2. Dowód jednoznaczności znormalizowanej naprzemiennej funkcji wieloliniowej jest kompletny: rozwinięcie po wektorach standardowych, wyzerowanie składników z powtórzeniami i znak permutacji pozostałych.
3. Dowód multiplikatywności opiera się na tej jednoznaczności zastosowanej do `A → det(AB)`, bez zakładania odwracalności `A` lub `B`.
4. W kryterium `det A≠0 ⇔ A` odwracalna zastosowano jedynie operacje mnożące wyznacznik przez niezerowe elementy, a postać zredukowana pełnego rzędu jest dokładnie `I_n`. Przypadek `n=0` jest objęty dowodem.
5. W rozwinięciu Laplace'a czynnik `(-1)^(i+j)` ma prawidłową orientację. Dla `n=1` minor ma determinant `1_K`. W tożsamości `A adj A=(det A)I=adj A A` wszystkie elementy pozadiagonalne otrzymano przez wiersz/kolumnę z powtórzonymi wektorami.
6. Wzory Cramera oparto na liniowości w kolumnach oraz istnieniu i jednoznaczności rozwiązania; nie rozciągnięto ich niepoprawnie na przypadek osobliwy lub prostokątny. Zachowano różnicę między interpretacją pola nad `R` a twierdzeniami algebraicznymi nad dowolnym ciałem.

**Wynik:** nie znaleziono nowej istotnej luki ani błędu w rozdziale 06; jego treść pozostaje niezmieniona.

## Testy niezależne i integralność

- Znak permutacji: wszystkie pary `S_n×S_n`, `0≤n≤5`, bez rozbieżności.
- Multiplikatywność wyznacznika: **262144** par macierzy `3×3` nad `F_2` oraz **6561** par `2×2` nad `F_3`, bez rozbieżności.
- Rozwinięcie Laplace'a, wierszowe zamiany i tożsamość macierzy dołączonej: wszystkie **19683** macierze `3×3` nad `F_3`, bez rozbieżności.
- Niezależnie sprawdzono transpozycję, rozwinięcia według kolumn i kryterium pełnego rzędu także na tych **19683** macierzach — zero rozbieżności.
- Dla wszystkich sześciu rozdziałów algebry liniowej kontrola statyczna wykazała **258 unikalnych etykiet** i **113 poprawnie rozwiązanych odsyłaczy**, bez błędów środowisk LaTeX, zakazanych terminów ani brakujących importów.
- CI po pierwszej iteracji rozdziału: [44910119376](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44910119376) — **success**; końcowy PDF ma **65 stron**, brak `Overfull`, `Underfull`, `LaTeX Warning`, `Missing character`, `Undefined control sequence` i błędów odsyłaczy w końcowym logu. Powiązane przebiegi `validate-cli` i `index-and-test` również zakończyły się sukcesem.

## Decyzja

**Rozdział 06 jest stabilny i zamknięty po czystym audycie II.** Nie zmieniano pliku matematycznego w tej iteracji. Niniejszy raport i korekta komentarza w pliku głównym uruchomią nowy przebieg walidacji; jego wynik należy sprawdzić oddzielnie. Następny etap merytoryczny: kolejny rozdział algebry liniowej, bez ponownego rozszerzania zamkniętych rozdziałów 01–06.
