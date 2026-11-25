# Audyt 219 — drukowany rozdział 24, kontrola stabilizacyjna A

Data: 2026-11-25. Kontynuacja 218 bez rozszerzania zakresu.
Źródło: chapters/pl/graph_and_knot_theory/17-grafy-cayleya-dzialania-na-drzewach-i-teoria-bassa-serre-a.tex.
Commit źródłowy 7dd1dbfaf127259219f733a2c53bb6626599cbf2, blob a6830b28deff06af43d16bb8bec3de449fc6b3a7 potwierdzony dwukrotnie. Bez zmian źródła.

## Kontrola
Ponownie przeczytano pełne źródło. Sprawdzono definicję grafu Cayleya, wolną bazę, brak cykli, swobodne działanie bez inwersji i iloraz zorientowanych krawędzi, nakrywanie gwiazd w topologii CW także przy nieskończonym stopniu, argument skończonych podkompleksów, homomorfizm przez końce podniesionych pętli, prezentację grafu grup, pokrycie podwójnego cylindra i konwencję HNN, konstrukcję reprezentantów drzewa rozpinającego i stabilizatorów, zgodność sprzężenia h_e z relacją t_e i końcem klasy g t_e^{-1}G_t, odwrócenie półkrawędzi, wzór indeksowy i przykłady C2*C3, torusa, BS(1,2). Nie znaleziono nowej istotnej usterki w przyjętym zakresie. Fundamentalne twierdzenie Bassa–Serre'a, w tym izomorficzność homomorfizmu z prezentacji oraz fakt, że graf klas bocznych jest drzewem, pozostaje wynikiem przyjętym z literatury, nie dowodem własnym. Zachowano 5 etykiet i 30 poprawnie zagnieżdżonych par środowisk. Wszystkie 5 wystąpień ref (4 różne etykiety) sprawdzono ponownie w źródle 07: ch:tg-topology, thm:tg-wedge, thm:tg-free-pi1, lem:tg-collapse-CW.

## Regresje
Ponownie pobrano i wykonano wszystkie trzy skrypty:
- GKT-24-CAYLEY-01 PASS: 380 modeli cyklicznych, 4486 wierzchołków, 12724 krawędzi, 41 niespójnych, 4308 słów zredukowanych i 31892 przejścia.
- GKT-24-COSET-01 PASS: 585 prób reprezentantów, 1755 incydencji i odwróceń, 15795 kontroli zmiany reprezentanta, 5265 translacji, 2047 wierzchołków ograniczonego modelu reszt i 4094 kontroli dziecko–rodzic. Nie dowód wierności reprezentacji afinicznej.
- GKT-24-FREE-PRODUCT-01 PASS: 218 słów, 219 wierzchołków i 218 krawędzi skończonego poddrzewa, 1090 kontroli incydencji, 654 translacje.
Wykonano w izolacie JS, nie potwierdzono integracji z CI ani wykonania w procesie Node; nie formalizacja Lean.

## Bramka CI i PDF
Dla 7dd1dbfa: terminologia 45588642803 SUCCESS; pełny audyt 45588642579, aplikacja 45588642607 i algorytmy 45588642566 pozostają in_progress przy ostatnim odczycie. Dostępny tylko artefakt strukturalny 15009927179, brak artefaktu kompletnego tomu dla właściwego SHA. Nie przeprowadzono oględzin PDF i nie przeniesiono wyników z wcześniejszej wersji.
Etap A pozostaje otwarty mimo braku nowych usterek w kontroli źródła. Następny audyt 220: weryfikacja końcowych wyników CI i rzeczywiste oględziny PDF, w tym dwóch rysunków, a przy spełnieniu bramki zamknięcie A. Postęp 23/44.
