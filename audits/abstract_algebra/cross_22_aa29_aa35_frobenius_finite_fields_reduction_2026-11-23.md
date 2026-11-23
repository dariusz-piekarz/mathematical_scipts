# Algebra abstrakcyjna — AA-X22: Frobenius nad ciałami skończonymi a typy cykli po redukcji (AA-29 × AA-35)

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **HEAD przed zapisem:** `722e853f3edf96557ac9cdf4a83c81414d892b0b`.

## Zakres i odrębność
Nowy audyt przekrojowy porównuje AA-29 (pierwiastki Frobeniusa, stopnie wielomianów nierozkładalnych i odwrócenie Möbiusa) z AA-35 (dobra redukcja i cykle Frobeniusa). Nie powtarza AA-X11 (AA-29 × AA-30) ani AA-X21 (prezentacje grup i algebry grupowe). Odczytano `AGENTS.md`, `docs/pl/standardy_terminologiczne.md`, `docs/pl/plan_algebry_abstrakcyjnej_aa43_plus.md`, `catalog/books.json`, listę 50 źródeł oraz istniejące raporty audytów. AA-51 nie występuje w katalogu źródeł.

## Kontrola matematyczna
1. AA-29, twierdzenie `aa:tw:finite-frobenius-roots`: dla monicznego nierozkładalnego `f` stopnia `d` nad `F_q` pierwiastki tworzą jedną orbitę `x -> x^q` długości `d`. Dowód wykorzystuje liczność `q^d`, minimalny okres oraz dzielenie z resztą. Zgadza się z AA-35, `aa:tw:frob-cycles`, gdzie różne czynniki dają rozłączne orbity.
2. AA-35 wymaga rozdzielczości redukcji (równoważnie `p` nie dzieli wyróżnika). To istotna hipoteza: dla `X^2-5` przy `p=2` otrzymujemy `(X+1)^2`, z czego nie wolno odczytać transpozycji. Przykład jest poprawny.
3. AA-35 nie zakłada nierozkładalności nad `Q`: przykład `(X^2-2)(X-3)` ma wyróżnik `392`; przy `p=5` występują stopnie `(2,1)`. Odpowiada to działaniu automorfizmu na dwóch pierwiastkach kwadratowych i jednym wymiernym.
4. Przykład `X^3-X-1` z AA-35: wyróżnik `-23`; przy `p=2` brak pierwiastków i typ `(3)`, przy `p=5` pierwiastek `2` i nierozkładalny czynnik kwadratowy, typ `(1,2)`; przy `p=23` pierwiastki `3,10` (drugi podwójny), redukcja zła; przy `p=59` trzy różne pierwiastki `4,13,42`, typ `(1,1,1)`. Niezależne sprawdzenie reszt potwierdziło te wartości.
5. Wzór AA-29 `N_q(n)=(1/n) sum_{d|n} mu(d) q^(n/d)` niezależnie sprawdzono przez wyliczenie **wszystkich monicznych wielomianów** nad `F_p` i test dzielników monicznych stopnia najwyżej `floor(n/2)`. Dla `p=2,3,5` oraz `n=1,2,3,4` otrzymano **12/12 zgodności**: `p=2: [2,1,2,3]`, `p=3: [3,3,8,18]`, `p=5: [5,10,40,150]`. Ten test nie stanowi dowodu ogólnego wzoru.
6. Sprawdzono wewnętrzne deklaracje etykiet i użycia `ref` w obu plikach: AA-29 ma 11 etykiet i 5 odsyłaczy, AA-35 ma 12 etykiet i 14 odsyłaczy; bez duplikatów etykiet w badanej parze. Odsyłacz `aa:tw:finite-frobenius-roots` z AA-35 prowadzi do AA-29. Pozostałych zewnętrznych celów nie certyfikowano w tym przebiegu globalnym skanem.

## Wynik i ograniczenia
**Matematyka w badanym interfejsie: bez wykrytej sprzeczności.** Niezależne obliczenia: **12/12** liczności wielomianów oraz kontrola czterech redukcji przykładu sześciennego. Nie jest to pełny audyt wszystkich dowodów 50 rozdziałów. Nie wprowadzono zmian do zatwierdzonych źródeł, etykiet ani odsyłaczy; licznik czystych audytów nie jest resetowany.

**LaTeX:** nowej kompilacji nie wykonano. **PDF:** nowej wizualnej inspekcji nie wykonano. **CI:** nowego przebiegu nie uruchomiono i nie deklaruje się PASS. Wynik matematyczny nie jest wynikiem kompilacji/CI.

**Status AA-X22:** opublikowany raport kontroli przekrojowej, bez ogłoszenia nowej stabilizacji całego tomu. **Następny krok:** ponowny odczyt HEAD i obecności AA-51; jeśli go brak, nowy, niepowtórzony audyt przekrojowy, z osobnym sprawdzeniem CI/PDF gdy możliwe.
