# Audyt 184 — drukowany rozdział 19, etap A (regresja konstrukcyjna)

Data: 2026-11-25. Kontynuacja 183; bez rozszerzania zakresu.
Źródło: chapters/pl/graph_and_knot_theory/12-wielomian-tutte-a-kolorowania-i-dualnosc-algebraiczna.tex.
Źródło bez zmian: commit f8eb8d88cd4adce8327754455dde2594e1e78d4e, blob 2472339133f7c28a618e3fd47dbbc1ba46658755, potwierdzony na gałęzi roboczej.
32 poprawnie zagnieżdżone pary środowisk, 12 etykiet; zachowano trzy wskazania bibliograficzne w końcowej sekcji.

## Ponowna kontrola
- Rekurencja, specjalizacje, dualność Tutte'a i przepływów: bez zmian w źródle. Brak nowych zidentyfikowanych istotnych usterek matematycznych w kontroli stabilizacyjnej.
- GKT-19-REC-01 PASS: 3528 grafów, 89217 podzbiorów, 15855 rekurencji, 14112 porównań kolorowań.
- GKT-19-DUAL-01 PASS: 747 układów, 453 sferyczne, 3533 par podzbiorów, 1812 porównań przepływów i kolorowań, 906 dla złożonych q.
- GKT-19-KIRCH-01 PASS: 3527 grafów, 954 spójne, 3532 dokładne minory.
Wszystkie trzy zapisane skrypty wykonano ponownie w izolacie JS.

## Dodatkowa trwała regresja istniejącego dowodu
GKT-19-LIFT-01, test_gkt19_flow_lift.js, commit 6ed7309c597998a3035efa2605bd94d4a861d423.
Niezależnie od liczenia przepływów i kolorowań sprawdzono znaki różnic ścian, warunek brzegowy nad Z, konstrukcję drzewa dualnego dopełniającego oraz rekonstrukcję każdego przepływu (również z zerowymi współrzędnymi) przez potencjały ścian i niezmienniczość względem dodania stałej.
PASS: 453 spójne modele sferyczne do 3 krawędzi, 3533 warianty orientacji, 8791 całkowitych kontroli kolumn różnic ścian, 216466 rekonstrukcji dla q=2,3,4,6, w tym 178826 dla q=4,6. Skrypt uruchomiono dwukrotnie, drugi raz z odczytanego pliku repozytorium, w izolacie JS. Próby częściowo pokrywają się z wcześniejszymi modelami; nie jest to formalizacja Lean ani wykonanie w procesie Node. Skrypt zapisany trwale, nie dodano osobnego wywołania do workflow.

## Bramka CI i PDF
Dla właściwego commitu źródła: Mathematical library application checks 45569720006 in_progress; Graph and knot theory - full book global audit 45569719965 in_progress; Polish mathematical terminology 45569719896 success; Graph and knot theory - algorithms audit 45569720000 success.
W pełnym audycie 45569719965 zadanie structural-audit SUCCESS; zadanie full-book-pdf nadal w toku przy ostatnim odczycie z instalacją TeX. Dostępny był jedynie artefakt strukturalny 15001048849, brak nowego PDF. Nie potwierdzono efektu korekty łamania stron z 183; nie przenosimy wcześniejszego PASS PDF.
Etap A nadal otwarty z powodu bramki CI/PDF. Następnie sprawdzić rzeczywisty PDF dla f8eb8d88 i wyniki wszystkich właściwych przebiegów, zamknąć A, następnie wykonać niezależny etap B. Nie przechodzimy do rozdziału 20.
