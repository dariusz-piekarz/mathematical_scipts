# Audyt LXXXIX (89) — rozdział 25: drugi przegląd różniczkowania miar

Data: 2026-11-24. Gałąź: biblioteka-matematyczna-iteracja-6.

## Stan wejściowy
Przebieg https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45297157253 dla bb04a807dccbdac5030a2f85f2b2583b835ac7ea: success. Logi 138120348566 i 138120348950 potwierdzają 4 testy rozdziału i 4 testy integralności, pełny PDF 265 stron, samodzielny rozdział 7 stron, 20 lokalnych i 7 zewnętrznych etykiet. Wynik dotyczy poprzedniego bloba a1608ca2fc3bcdbe13b8a4b67ffa60202416bc4e.

## Poprawki i niezależny przegląd
Commit 350e8825374cbfda58d5b9e92dbeb191e6b6ccb1, blob d74356d24685f8e5d6f3395e83c72a96b65da921.
- W dowodzie względnego twierdzenia o różniczkowaniu wybrano skończony borelowski reprezentant i wykazano mierzalność oscylacji: dla ustalonego c licznik jest półciągły z dołu względem środka (Fatou), zależność od c jest lipschitzowska ze stałą równą masie kuli, a podstawienie f(x) można uzasadnić przez borelowskie funkcje proste. Względem promienia wystarcza ciągłość od dołu dla kul otwartych; nie zakładamy zerowej masy sfer. To pozwala użyć przeliczalnych supremów po promieniach wymiernych.
- Uzasadniono również mierzalność granicy górnej w lemacie o zaniku gęstości miary osobliwej względem Lebesgue'a.
- Sprecyzowano konwencję skończonej miary ze znakiem i zespolonej zgodnie z rozdziałem 16; wariant lokalny dotyczy wartości na ograniczonych zbiorach, bez odejmowania nieskończonych mas.
- Dodano wniosek o różniczkowaniu skończonych miar ze znakiem i zespolonych względem dowolnej dodatniej miary Radona: część osobliwa jest kontrolowana przez jej wariację całkowitą.
- Dodano przykład skończonej miary atomowej, dla której ilorazy mu(5B_n)/mu(B_n) wynoszą 1+2^n, pokazując, dlaczego zwykły lemat 5r nie zapewnia uniwersalnego oszacowania względem dowolnej miary Radona.
- Dodano kontrprzykład f=sgn na prostej: średnie w zerze wynoszą zero, ale oscylacja wynosi jeden. Granica średnich nie wystarcza do własności punktu Lebesgue'a.
- Ponownie sprawdzono dodatniość mianownika na nośniku, pokrywanie ograniczonych zbiorów poziomicowych Besicovitchem, lokalizację oraz aproksymację części osobliwej przez ograniczenie do zwartego zbioru zerowej miary odniesienia. Nie znaleziono dalszych luk w tych krokach.

## Regresje
Commit f8b77ef7dabadce80a84f81923e2138589605cc9: trzy dodatkowe metody testowe (atomy na brzegu kuli, miary ze znakiem, przykład bez jednostajnego ograniczenia ilorazu mas). Łącznie 7 metod.
Niezależnie rzeczywiście wykonano w JavaScript 648 kontroli mas kul przy promieniach rosnących do promienia granicznego, 6750 kontroli atomowego rozkładu miar ze znakiem i 24 dokładne obliczenia ilorazu mas w przykładzie z atomami (wspólny mianownik 2^50, całkowite obliczenia BigInt). Wszystkie przeszły. Nie zastępują ogólnych dowodów ani uruchomienia testów Python.
Aktualny plik: 21 unikalnych etykiet, poprawne zagnieżdżenie środowisk, 8 różnych odsyłaczy zewnętrznych. Status nowego commitu w chwili odczytu pusty. Nie oglądano PDF najnowszego bloba.

## Werdykt
24/31 rozdziałów ustabilizowanych. Rozdział 25 pozostaje w stabilizacji. Następny audyt XC (90): końcowy przegląd matematyczny, potwierdzenie 7+4 testów oraz rzeczywista kontrola wszystkich stron najnowszego PDF. Nie przechodzić do rozdziału 26 przed zamknięciem bramki.
