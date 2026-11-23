# Plan dalszego rozwoju „Algebry abstrakcyjnej” — od AA-43

**Ustalenie:** globalny audyt kanonicznych AA-01–AA-42 został zakończony i pozostaje zamkniętym punktem odniesienia. Dalsze prace nie polegają na „audytowaniu istniejącego AA-43”: na starcie 23 listopada 2026 r. rozdziały 43+ **nie istniały**. Należy więc najpierw przygotować nowy rozdział na podstawie materiału źródłowego, potem wielokrotnie go audytować i dopiero po stabilizacji otworzyć następny.

## Dostępny materiał do wykorzystania

W repozytorium jest rozbudowany starszy skrypt `sources/pl/galois(2).tex`, który poza już opisanymi tematami klasycznej teorii Galois zawiera:
- rozdział „Ciała różniczkowe i twierdzenie Liouville'a” (początek około wiersza 802);
- rozdział „Cztery ważne całki nieelementarne” (początek około wiersza 1037);
- rozdział „Przykłady z równań różniczkowych” (początek około wiersza 1254), obejmujący przykłady automorfizmów różniczkowych oraz równanie Airy'ego.

To nie jest osobny zbiór gotowych do importu „AA-43–AA-74”. Stare numery rozdziałów należą do **innego monolitycznego skryptu**. Nowe numery w kanonicznej książce wynikają z redakcyjnego podziału tematycznego.

## Kolejność jednoznacznych iteracji

| Nowy numer | Materiał przewodni | Główna zależność | Warunek przejścia |
| --- | --- | --- | --- |
| **AA-43** | Ciała różniczkowe, pochodne elementów algebraicznych, stałe, ślad i norma, przestępne kroki | AA-20/21/23 | dwa niezależne audyty, brak usterek w LaTeX, oba testy, pełne CI i przegląd stron |
| **AA-44** | Twierdzenie Liouville'a o całkowaniu elementarnym, pełny dowód w obie strony; formalne części wielomianowe pochodnych | AA-43 | niezależny sprawdzian przejścia po wieży, kontrola kroków algebraicznych, logarytmicznych i wykładniczych |
| **AA-45** | Kryteria dla funkcji hiperwykładniczych i szczegółowe przykłady całek nieelementarnych | AA-44 | dla każdego przykładu redukcja do testu równań wymiernych, pełne dowody i kontrprzykłady |
| **AA-46** | Automorfizmy różniczkowe, podstawy rozszerzeń Picarda–Vessiota, grupy Galois równań liniowych | AA-43–AA-45 | oddzielenie twierdzeń udowodnionych od głębszych cytowanych wyników; kompletna kontrola przykładów |
| **AA-47 (warunkowo)** | Algorytmy Rischa i Kovacica, efektywna procedura i podstawy poprawności | AA-44–AA-46 | osobna decyzja o pełnym zakresie, zanim rozpocznie się wymagające opracowanie |

## Globalny rygor audytu

Dla każdego nowego rozdziału należy:
1. opracować definicje i twierdzenia z wszystkimi hipotezami, oznaczeniami i zakresami;
2. dołączyć motywacje, szczegółowe dowody, przykłady i kontrprzykłady, używając polskiej terminologii matematycznej;
3. wykonać audyt I treści i struktury, rzeczywiście usunąć błędy;
4. wykonać audyt II niezależny od pierwszego, obejmujący przypadki brzegowe i tożsamości w niezależnych modelach;
5. utrzymać dwa niezależne zestawy testów regresyjnych, integralność odsyłaczy oraz zgodność `books/pl/abstract_algebra.tex` z `catalog/books.json`;
6. potwierdzić zielony CI na źródłach danego rozdziału, obejrzeć **każdą nową stronę** wygenerowanego PDF i sprawdzić log LaTeX;
7. udokumentować źródła, poprawki, commity, faktyczny CI i ostateczny werdykt `STABILNY` — dopiero potem zacząć następny numer.

Zmiana zakresu książki na 43+ nie unieważnia zamkniętego raportu AA-01–AA-42. Test integralności należy rozszerzać o nowy rozdział **bez fałszowania historycznego pokrycia**. Nie wolno przedstawiać obliczeń skończonych przypadków jako dowodu wszystkich twierdzeń ani oznaczać nieodbytej kompilacji jako zatwierdzonej.
