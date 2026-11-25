# Audyt 177 — drukowany rozdział 18, zamknięcie etapu A

Data: 2026-11-25. Kontynuacja 176; bez rozszerzania zakresu.
Źródło: chapters/pl/graph_and_knot_theory/11-grafy-na-powierzchniach-grafy-dualne-i-homologia-komorkowa.tex.
Commit źródłowy 133d9432b9ad8b28edfa4d5458ebe2b9a2dccbb3, blob b1a926c25e6eb8dea68f79eef1322ea76f10f580 (potwierdzony także na aktualnej gałęzi).

## CI oraz rzeczywisty PDF
- Pełny audyt tomu 45567090921 SUCCESS; algorytmy 45567091069 SUCCESS; terminologia 45567090919 SUCCESS; aplikacja 45567090879 SUCCESS. Wszystkie dotyczą wskazanego commitu.
- Pobrano artefakt 15001005055 (graph-and-knot-complete-book-audit) z przebiegu 45567090921; PDF 338 stron, plik ostrzeżeń 0 bajtów.
- Wyrenderowano wszystkie osiem stron PDF 156–163 (druk 146–153) przy skali 1.5 i porównano piksele z PDF z audytu 176. Siedem stron identycznych, na stronie PDF 160 różnica ograniczona do poprawianego fragmentu rysunku. Obejrzano powiększenie zmienionego fragmentu: cztery łuki przy F3 nie mają dodatkowych przecięć; oznaczenie zewnętrznej ściany F3 jest widoczne. Nie stwierdzono nowej usterki. Zachowano 7 adnotacji odsyłaczy na ośmiu stronach.
- Treść matematyczna pozostaje niezmieniona od audytu 175; 14 etykiet.

## Regresje wykonane ponownie
Pobrano pięć zapisanych skryptów JS i wykonano ich funkcje testowe w izolacie JavaScript z przechwyceniem logu i odpowiednikiem asercji Node (nie proces Node).
- BRIDGE-01 PASS: 1067 mostów.
- ROT-01 PASS: 7776 rotacji K5, 64 rotacje K3,3, minimalny rodzaj 1.
- TC-01 PASS: 2546 układów, 2221 spójnych, 4442 rozkłady, 8996 elementów bazy, 12354 relacje.
- ORIENT-01 PASS: 6177 kontroli znaków na 2221 spójnych układach.
- FIG-01 PASS: separacja kierunków 42.501011 stopnia, suma wygięć 24 stopnie, cztery łuki; dodatkowo oględziny rzeczywistego PDF jak wyżej.
Próby TC i ORIENT częściowo się pokrywają. Regresje nie stanowią formalizacji Lean.

## Decyzja
Etap A zamknięty dla wskazanego blobu: wszystkie zidentyfikowane usterki z audytów 171–176 mają poprawki, obowiązkowe kontrole wykonano, brak otwartych usterek w tym etapie. Nie jest to zakończenie niezależnego etapu B. Następna iteracja: odrębny audyt kontrolny rozdziału 18, bez nowych rozszerzeń. Nie przechodzimy jeszcze do rozdziału 19.
