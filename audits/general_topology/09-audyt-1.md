# Topologia ogólna — rozdział 09: audyt 1

**Data:** 2026-11-21  
**Rozdział:** `chapters/pl/general_topology/09-aksjomaty-przeliczalnosci.tex`  
**Tytuł:** Aksjomaty przeliczalności i własności pokrewne  
**Wersja:** 0.1 (pierwszy audyt)  
**Licznik kolejnych czystych audytów:** 0/2

## Zakres

- Pierwsza przeliczalność (zgodna z rozdziałem 06) i druga przeliczalność;
- dziedziczenie obu własności przez podprzestrzenie i stabilność drugiej przeliczalności przy iloczynach przeliczalnych;
- ośrodkowość oraz własność Lindelöfa, konsekwencje drugiej przeliczalności;
- zachowanie tych własności przez obrazy ciągłe i wybrane podprzestrzenie;
- równoważność drugiej przeliczalności, ośrodkowości i własności Lindelöfa w przestrzeniach metrycznych;
- prosta i płaszczyzna Sorgenfreya, topologia koskończona, nieprzeliczalna przestrzeń dyskretna, uzwarcenie jednopunktowe;
- schemat implikacji oraz rysunek półotwartych przedziałów.

## Przegląd matematyczny

Dowody wszystkich sformułowanych twierdzeń i przykładów sprawdzono co do kwantyfikatorów, założeń, przypadków pustych i wybranych podprzestrzeni. Zidentyfikowano następujące uzupełnienia wymagane przez standard:

1. **Dowód własności Lindelöfa prostej Sorgenfreya.** Jawnie przytoczono twierdzenie o dziedziczeniu drugiej przeliczalności przez podprzestrzenie przy przejściu z przestrzeni euklidesowej do zbioru otwartego `G`. Dzięki temu zastosowanie własności Lindelöfa do pokrycia `G` ma wyraźne uzasadnienie.
2. **Dowód zestawienia implikacji.** Uzupełniono przykład przeciwny dla kierunku „Lindelöf ⇒ ośrodkowość” poprzez szczegółowe wyjaśnienie braku przeliczalnego zbioru gęstego w nieprzeliczalnym uzwarceniu jednopunktowym przestrzeni dyskretnej. Dopisano też, że płaszczyzna Sorgenfreya pozostaje pierwszo przeliczalna, choć nie jest Lindelöfa.

Ponieważ audyt wprowadził dwie rzeczywiste korekty uzasadnień, **nie jest czysty**.

## Testy

- Regresja rozdziałów 01–08: PASS.
- Rozdział 09: 390 topologii skończonych; 1516 minimalnych otoczeń; 2483 rekonstrukcji zbiorów otwartych; 5931 testów gęstości; 5931 testów podprzestrzeni; 864 weryfikacje otoczeń w iloczynach; 96 przypadków racjonalnych siatek ilustrujących argument dla prostej Sorgenfreya — PASS.
- Unikatowość etykiet i rozwiązywanie odsyłaczy w rozdziałach 01–09: 364 etykiety, 93 odsyłacze — PASS.
- `latexmk` pełna książka oraz samodzielny rozdział 09 — PASS, brak ostrzeżeń `Overfull`, `Underfull`, `Missing character`, `LaTeX Warning`, `Undefined control sequence`, `Fatal error`.
- PDF rozdziału 09: **7 stron**; PDF całej książki 01–09: **80 stron**.
- Render i kontrola wszystkich siedmiu stron: PASS. Dwa rysunki i podpisy bez kolizji.

## Status i dalszy krok

Rozdziały 01–08 pozostają stabilne w GitHub i CI. Rozdział 09 ma status **roboczy 0.1, 1 audyt, 0/2 czystych**. Nie wypychać go na GitHub przed stabilizacją. Następna iteracja: **audyt 2 bez rozszerzania zakresu**.

Potencjalny temat na dalszy rozdział (wyłącznie propozycja dla użytkownika): twierdzenie Urysohna o metryzowalności, z dokładnym rozróżnieniem założeń regularności i drugiej przeliczalności. Nie włączać go do rozdziału 09 bez decyzji użytkownika.
