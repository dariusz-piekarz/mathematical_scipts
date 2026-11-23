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


## Aktualizacja stanu — 23 listopada 2026 r. (AA-44)

**AA-43: STABILNY** — raport audits/abstract_algebra/ch43_iteration_03.md.

**AA-44: STABILNY** — raport audits/abstract_algebra/ch44_iteration_03.md. Rozdział zawiera pełne dowody konieczności i dostateczności twierdzenia Liouville'a; dwa niezależne zestawy testów (9 + 5) zakończyły się sukcesem. Pełny CI na ostatecznym commicie źródła 9edced10d90537b7466f9bf2d94f4b9a439b63eb: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45151940204 — completed / success. Sprawdzono końcowy 281-stronicowy PDF i wszystkie 6 stron AA-44.

**Następny odblokowany etap: AA-45** (całki nieelementarne i kryteria hiperwykładnicze), zgodnie z zasadą jednego rozdziału i wielokrotnych audytów do stabilizacji. **AA-46** (Picard–Vessiot) dopiero później. Historycznych statusów AA-01–AA-42 nie zmieniono.


## Aktualizacja stanu — 23 listopada 2026 r. (AA-45)

**AA-43: STABILNY** — raport audits/abstract_algebra/ch43_iteration_03.md.
**AA-44: STABILNY** — raport audits/abstract_algebra/ch44_iteration_03.md.
**AA-45: STABILNY** — raport audits/abstract_algebra/ch45_iteration_03.md.

AA-45 obejmuje kryteria hiperwykładnicze i dla skończonych sum Laurenta, cztery pełne analizy całek nieelementarnych (Gaussa, sinusowej, logarytmicznej, eliptycznej), 12 dowodów i 5 przykładów. Ukończono audyty I–III, wykonano dwie niezależne serie regresji (10 + 8 testów PASS) i zweryfikowano zielony CI: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45154562082, commit 9a375ac376c90e04d6ec8b3172a224afd7551572. Końcowy PDF ma 289 stron, osiem stron AA-45 obejrzano, końcowy log bez błędów i ostrzeżeń; 45 rozdziałów w katalogu, bez brakujących odsyłaczy. Historii audytów AA-01–AA-42 nie zmieniono.

**Następny odblokowany etap: AA-46 — automorfizmy różniczkowe, rozszerzenia Picarda–Vessiota i grupy Galois równań liniowych.** Obowiązuje zasada: opracowanie AA-46, następnie niezależne audyty do stabilizacji, dopiero AA-47 (o ile zostanie zatwierdzony).


## Aktualizacja stanu — 23 listopada 2026 r. (AA-46)

**AA-43: STABILNY** — audits/abstract_algebra/ch43_iteration_03.md.
**AA-44: STABILNY** — audits/abstract_algebra/ch44_iteration_03.md.
**AA-45: STABILNY** — audits/abstract_algebra/ch45_iteration_03.md.
**AA-46: STABILNY** — audits/abstract_algebra/ch46_iteration_03.md.

Rozdział AA-46 włączono do kanonicznej książki i katalogu. Przeprowadzono trzy audyty, w tym rzeczywiste poprawki: poprawny dowód Eisensteina dla T^m−x przy dowolnym m≥2 (w tym złożonym), doprecyzowanie normalizacji Laurentów, zamiana tytułu sekcji powodującego ostrzeżenia hyperref oraz wzmocnienie niezależnych testów.

**Ostateczny GitHub Actions:** https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45157760575 — completed / success, 83/83 kroków. Testy AA-46: 10/10 SymPy + 8/8 Fraction PASS. Integralność: 46 rozdziałów, 939 etykiet unikatowych, 0 duplikatów, 451 odsyłaczy, 0 brakujących celów. Ostateczny PDF: 297 stron; AA-46 zajmuje 7 stron PDF 291–297, wszystkie obejrzano, końcowy log bez błędów i ostrzeżeń.

**AA-47 jest warunkowy**, zgodnie z tabelą tego planu: algorytmy Rischa i Kovacica należy najpierw objąć odrębną decyzją o zakresie (wymagane dowody poprawności, własne przykłady i audyty). Nie uruchamiać AA-47 automatycznie wyłącznie dlatego, że AA-46 osiągnął stabilność.


## Otwarcie AA-47 — 23 listopada 2026 r.

Na podstawie prośby o kontynuację po stabilnym AA-46 przyjęto **ograniczony, audytowalny zakres** AA-47 w `docs/pl/zakres_aa47_risch_kovacic.md`: pełne dowody algorytmów wymiernych i dla wielomianowych parametrów, plus wyraźnie cytowane klasyczne wyniki pełnego Rischa i Kovacica. Rozdział i audyty dopiero powstają. **AA-47 NIE STABILNY** do zielonego CI, niezależnych audytów i pełnej kontroli PDF; nie otwierać AA-48.
