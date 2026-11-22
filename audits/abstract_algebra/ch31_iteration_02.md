# Algebra abstrakcyjna — AA-31, audyt II (stabilizacyjny)

**Data:** 22 listopada 2026  
**Rozdział:** „Wielomiany symetryczne i wzory Viète’a”  
**Status:** stabilny po dwóch audytach; zero zmian źródła w audycie II.  
**Gałąź docelowa:** `biblioteka-matematyczna-iteracja-6`.

## Stan wejściowy i integralność

Źródłem jest pełna poprawiona wersja z audytu I (`AA-31-audyt-I-zrodlo.tex`), o skrócie SHA-256 `7462fce639b125f4a1bb890356c4f987055deb7bdc192f514262a4e9c68e8596`. Skrót źródła po audycie II pozostaje identyczny. Rozdział ma 294 wiersze, 9 unikatowych etykiet i 2 odsyłacze wewnętrzne, oba rozstrzygnięte.

## Niezależna weryfikacja dowodów

1. **Pierścień współczynników:** podstawowe twierdzenie zachodzi dla każdego przemiennego pierścienia z jedynką, w tym pierścienia zerowego i pierścieni z dzielnikami zera. Uzasadniono, dlaczego potrzebna jest jedynie moniczność elementarnych wielomianów symetrycznych, a nie dzielenie przez współczynniki.
2. **Algorytm eliminacji:** wykładniki wiodące wielomianu symetrycznego tworzą słabą partycję; obraz odpowiedniego jednomianu w `e_k` ma ten sam jednomian wiodący o współczynniku `1_A`. Ściśle malejąca sekwencja wiodących jednomianów pozostaje w skończonym zbiorze stopnia nie większego niż początkowy.
3. **Iniektywność:** różne jednomiany w zmiennych `T_k` mają różne wiodące jednomiany po podstawieniu. Maksymalny współczynnik nie może się skasować, także jeśli pierścień ma dzielniki zera.
4. **Wzory Viète’a:** sprawdzono występowanie pierwiastków z krotnościami, poprawność znaków we wzorach i tożsamości sum kwadratów oraz sześcianów w dodatnich charakterystykach.
5. **Przykłady:** sprawdzono przypadek `Z/4Z`, przykład trzech zmiennych i kontrprzykład do błędnego założenia liniowości przedstawienia.

## Testy

- Regresja z audytu I: **31/31 PASS**.
- Dodatkowy niezależny zestaw: **28/28 PASS**.
- Wspólny przebieg w układzie katalogów repozytorium: **59/59 PASS**, plik `AA-31-audyt-II-testy.log`.
- Dodatkowy zestaw sprawdza **dokładne odtworzenie wielomianu w generatorach** dla 18 kombinacji `(n,m)`, gdzie `n=1,2,3`, `m=2,3,4,5,6,8`, po 8 deterministycznych przykładów na kombinację. Obejmuje też permutacje 4 zmiennych i krotności pierwiastków w charakterystykach 2 i 3.
- Testy są kontrolą wielu przypadków, nie zastępują matematycznych dowodów.

## Kompilacja i skład

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error`: **PASS**, 4 strony A4.
- Brak ostrzeżeń LaTeX, nierozwiązanych odsyłaczy i przepełnień w logu.
- Wszystkie strony wyrenderowano i obejrzano; nie stwierdzono kolizji składu. Rozdział nie zawiera rysunków.
- Budowano rozdział w pomocniczym dokumencie używającym zgodnej preambuły. **Nie wykonano pełnej kompilacji całej książki ani nie potwierdzono zdalnego GitHub Actions.**

## Decyzja i integracja

**AA-31 STABILNY po audycie II.** Rozdział nadaje się do publikacji na istniejącej gałęzi GitHub. Plik źródłowy nie wymaga zmian; testy zostały przystosowane do ścieżek repozytorium, bez przywiązywania ich do skrótu źródła.

## Potwierdzenie publikacji na GitHub

Repozytorium `dariusz-piekarz/mathematical_scipts`, gałąź `biblioteka-matematyczna-iteracja-6`:

- Rozdział: `chapters/pl/abstract_algebra/31-wielomiany-symetryczne-i-wzory-viete.tex`, commit `624ba0a843ad4754f7aac41a6f74f43855b19b94`.
- Testy regresyjne: `tools/tests/test_abstract_algebra_ch31.py`, commit `11223f74cbb05887efa9c28d967ecc2d41877374`.
- Testy niezależne: `tools/tests/test_abstract_algebra_ch31_independent.py`, commit `7801424654cc5e17b4bb6fa792c1d8d40255fb45`.
- Plik główny książki: aktualizacja `books/pl/abstract_algebra.tex`, commit `7661117501fbe8c318cbf7d8454f268cebebd538`.
- Katalog: 31 rozdziałów, commit `67d2b3ae04b02ce67006dd7f157354e7baf172be`.
- Workflow: `AA-01–AA-31`, 59 testów rozdziału, commit `6a08f2124d9cee0dd73250967969d7ea0ed317b0`.

Zdalny odczyt plików po publikacji potwierdził zgodność bajtową źródła i testów oraz obecność `\input` i rejestracji w katalogu. Nie uzyskano potwierdzenia statusu zdalnego GitHub Actions ani pełnego PDF książki.
