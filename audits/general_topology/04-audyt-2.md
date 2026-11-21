# Topologia ogólna — rozdział 04 — audyt 2

**Data:** 21 listopada 2026 r.
**Wersja:** 0.1, bez zmian.
**SHA-256 źródła:** `1782069b7efa42a773542ed4b417676c8e54b6abe2ac34255fab2835e890fc2a`.
**Zakres:** 666 wierszy LaTeX; 8 stron samodzielnego PDF; 36 stron książki obejmującej rozdziały 01–04.

## Kontrola matematyczna

Sprawdzono wszystkie definicje, sformułowania, dowody i przykłady dotyczące topologii podprzestrzeni, iloczynu, sumy rozłącznej, topologii początkowej i końcowej oraz topologii ilorazowej. Weryfikowano szczególnie: przechodniość topologii podprzestrzeni, domknięcie i brzeg względny, skończone ograniczenia współrzędnych w iloczynie dowolnej rodziny, rzutowania jako odwzorowania otwarte, własności uniwersalne, przypadki pustych rodzin, nasycenie zbiorów i kontrprzykłady dla odwzorowań ilorazowych. Sprawdzono, czy wzory używane w dowodach mają dostateczne uzasadnienie lub odniesienie do wcześniejszych własności.

**Wynik:** brak wykrytych błędów i luk wymagających modyfikacji rozdziału.

## Weryfikacja techniczna i niezależna

- `bash tools/validate_general_topology_ch04.sh` — PASS; regresja wszystkich czterech rozdziałów.
- Kontrola 823 przypadków podprzestrzeni, 361 iloczynów dwuczynnikowych, 1481 sum rozłącznych, 83 topologii początkowych/końcowych, 391 ilorazów, 406 rodzin początkowych i 398 końcowych — PASS.
- Nowy test niezależny: **16 384** odwzorowania do iloczynów trzech przestrzeni dwupunktowych, wszystkie kombinacje ich czterech topologii i wszystkich topologii źródła dwupunktowego: kryterium ciągłości przez rzutowania oraz otwartość rzutowań — PASS.
- Nowy test niezależny: wszystkie **15** partycji zbioru czteropunktowego, wszystkie **355** jego topologie i wszystkie 16 podzbiorów: **85 200** kontroli otwartości/domkniętości obrazów przez nasycenie — PASS.
- 40 etykiet rozdziału 04, 3 odsyłacze i zrównoważone środowiska — PASS.
- `latexmk -pdf` samodzielnego rozdziału i całej książki — PASS, bez ostrzeżeń.
- Wizualnie sprawdzono kompozycję wszystkich ośmiu stron, w szczególności dwa rysunki i zamknięte/otwarte końce przedziałów — PASS.

**Decyzja:** audyt 2 **czysty**; licznik kolejnych czystych audytów: **1/2**. Wersja 0.1 źródła nie została zmieniona; rozdział 04 nie został jeszcze wypchnięty do GitHuba. Następna iteracja to audyt 3.
