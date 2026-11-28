# Audyt 162 — drukowany rozdział 17, etap A (kontynuacja)
2026-11-24. Plan 118. Wznowienie po audycie 161.
Źródło: chapters/pl/graph_and_knot_theory/10-kryteria-planarnosci-podzialy-krawedzi-i-kolorowanie.tex.
Commit źródłowy: 9cfbfa49403e6d34eb9c67abb2c7631f22ef66f5.
Commit regresji: 1e359774de03d03ccc4ca6180a21160a7bc7d4da.

## Zmiany
Jawne zdefiniowanie spójności zbiorów rozgałęzienia przez podgrafy indukowane. Dowód model => minor: usunięcie zbędnych wierzchołków, kontrakcje rozłącznych drzew rozpinających, zachowanie po jednej wymaganej krawędzi. Dowód minor => model: dwa niezmienniki w pierwotnym G (spójność i świadkowie krawędzi). Lemat o etykietach: ścieżki długości zero, dowód rozłączności alternatyw środka i rozcięcia 2+2. Korekta językowa kroku 5. Zachowano 22 etykiety, sprawdzono 57 par środowisk. Odczyt zmian potwierdzony. Konflikt pierwszej próby zapisu rozwiązano ponownym odczytem aktualnego pliku, bez wymuszania zapisu.

## Regresje rzeczywiście wykonane
GKT-17-TREE-01: test_gkt17_tree_terminals.js; uruchomiono funkcję run w środowisku JS przed zapisaniem identycznej funkcji. PASS: 1442 drzewa etykietowane n=1..6, 249963 multizbiory etykiet, w tym 202645 z powtórzeniami. Środek 154887, rozcięcie 2+2 95076. Test niezależnie kontroluje przecięcia ścieżek i liczność etykiet po obu stronach krawędzi. Nie jest formalizacją Lean ani testem całego twierdzenia o modelach minorów.
Ponowne uruchomienie lokalnych kopii poprzednich regresji: OUTER: PASS 3288 grafów, 22 triangulacje, 2650 spadków potencjału; KEMPE: PASS 1016 grafów, 750 i 377 zamian; KUR: PASS 79471 układów cyklicznych, 156 grafów trójspójnych, 2196 krawędzi.

## Stabilizacja
CI: puste listy statusów i workflow; sukces niepotwierdzony. Lokalny pdflatex dostępny, ale git ls-remote nadal kończy się błędem DNS. Nie zbudowano pełnego PDF. Etap A OTWARTY.
Wznowienie: kontrola przejścia od modeli K5/K3,3 do subdywizji, zwłaszcza powtarzających się końców krawędzi; pełna kompilacja i kontrola CI/PDF przed zamknięciem A i niezależnym B.
