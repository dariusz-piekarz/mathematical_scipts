# Audyt 208 — drukowany rozdział 22, zamknięcie etapu A

Data: 2026-11-25. Kontynuacja 207 bez rozszerzania zakresu.
Źródło chapters/pl/graph_and_knot_theory/15-dyskretna-teoria-morse-a-formana.tex.
Commit źródłowy 0a436d68f580b252c1e68ec33501f37d301b7867, blob 2ad61fc865659e0e80951f78b53e415e82ecee9d potwierdzony dwukrotnie. Bez zmian źródła.

## Stabilizacja
Sprawdzono definicje niepustych sympleksów, kierunki nierówności Morse'a, argument rombu, sortowanie topologiczne, opis krytyczności, warunek wolnej ściany, barycentryczną retrakcję także dla p=0 i sklejanie homotopii. Dotychczasowe dowody eliminacji i torsji z 205–206 zachowane; nie znaleziono nowej istotnej usterki. Twierdzenie Formana o modelu CW jest jawnie przyjmowane z literatury, nie utożsamiane z dowodem algebraicznej eliminacji. Zachowano 13 etykiet i 36 poprawnie zagnieżdżonych par środowisk.
Sprawdzono wszystkie 10 wystąpień ref w rozdziale: etykiety lokalne i zewnętrzne z rozdziałów 18 i 20 istnieją; skontrolowano także wybrane zależności źródeł 02,06,07,11–16, m.in. konwencje grafu dualnego, sympleksów i orientacji. Nie wykryto konfliktu. Kontrola celowana, nie pełny audyt dalszych rozdziałów.

## PDF i CI
Dla 0a436d68: terminologia 45577187370, algorytmy 45577187736, pełny audyt 45577187416, aplikacja 45577187356 — wszystkie SUCCESS.
Pobrano i rozpakowano artefakt 15004049148 dla właściwego SHA. PDF ma 348 stron, rozdział 22 fizyczne strony 186–193 (druk 176–183), rozdział 23 zaczyna się na 194. 10 adnotacji odsyłaczy w rozdziale. Plik ostrzeżeń ma 0 bajtów. Wyrenderowano wszystkie osiem stron w skali 1.5 i obejrzano dwa arkusze kontaktowe. Oba schematy czytelne, bez zauważalnych kolizji i obcięć, wzory mieszczą się w obszarze składu. Dowód twierdzenia o parowaniu zaczyna się na stronie następującej po wypowiedzi; niektóre dłuższe dowody przechodzą przez granice stron, lecz pozostają czytelne. Nie wprowadzano kosmetycznych zmian.

## Regresje
Ponownie pobrano i wykonano:
- GKT-22-CANCEL-01 PASS: 240 kompleksów, 152 z parami sąsiednich wymiarów, 3652 eliminacje, 6433 aktualizacje Schura, 1920 porównań nad ciałami.
- GKT-22-TREE-COTREE-01 PASS: 120 prób, 3936 eliminacji, 24 wyniki RP2 z d2=±2, 96 z zerową różniczką, 60 kontroli ogniw.
- GKT-22-FUNCTION-COLLAPSE-01 PASS: 16384 przypisania, 232 funkcje Morse'a, 201 z równością w parze, 42 parowania (40 acyklicznych i 2 cykliczne), 1715 punktów barycentrycznych, 12005 kontroli homotopii.
Skrypty wykonano w izolacie JS, nie potwierdzono wykonania w procesie Node ani integracji z CI; nie formalizacja Lean.

## Decyzja
Etap A zamknięty dla wskazanego blobu. Rozdział 22 pozostaje otwarty do niezależnego etapu B. Następny audyt 209: niezależna kontrola całego rozdziału, szczególnie rozkładu kompleksu i zgodności eliminacji nad Z. Bez niezatwierdzonych rozszerzeń. Postęp 21/44.
