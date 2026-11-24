# Audyt 163 — drukowany rozdział 17, etap A (kontynuacja)

2026-11-24. Plan 118, poprzedni raport 162.
Źródło: chapters/pl/graph_and_knot_theory/10-kryteria-planarnosci-podzialy-krawedzi-i-kolorowanie.tex.
Commit źródłowy: 78ba7850b80c7ea9c0dc0514bf747f524975ec67.
Commit regresji: 1f5fedfabdd8feef5e1ae445d435ae4b298c26a4.

## Zmiany
- Jednoznaczne wybieranie krawędzi modelu dla nieuporządkowanej pary i oznaczenie obu końców.
- Dowód prostoty ścieżek, dokładnej postaci ich przecięć, braku innych wierzchołków rozgałęzienia we wnętrzach oraz obsługa ścieżek zerowej długości w drzewach.
- Jawna konstrukcja podgrafu (niekoniecznie indukowanego), aby dodatkowe krawędzie nie zaburzały subdywizji.
- Uzasadnienie zmiany numeracji K5, wskazanie wszystkich dziewięciu świadków krawędzi modelu K3,3 i spójności rozciętych zbiorów; dodatkowe krawędzie w jednej części modelu są dozwolone.
- Uzupełnienie dowodu dziedziczenia braku zabronionych subdywizji przez minory: jawna sekwencja kontrakcji i przechodniość.
- Zachowano 22 etykiety, sprawdzono zagnieżdżenie 57 par środowisk LaTeX; odczyt aktualnego pliku potwierdza zapis.

## Regresje
GKT-17-MINOR-01: test_gkt17_minor_subdivision.js. Uruchomiono funkcję run w środowisku JS przed zapisem tej samej funkcji. PASS: 3372 modeli, 751 subdywizji K5, 2621 subdywizji K3,3 (w tym 1520 po rozcięciu modelu K5); 30994 ścieżek z co najmniej jednym zerowym odcinkiem drzewowym, 17036 wystąpień zbiorów rozgałęzienia z powtarzającymi się końcami. Zakres: zbiory rozgałęzienia będące ścieżkami do 4 wierzchołków, wyczerpująca zmienność etykiet pojedynczego zbioru i 500 deterministycznie generowanych konfiguracji mieszanych dla każdego grafu. Kontrolowano istnienie świadków, prostotę, przecięcia i stopnie w wybranym podgrafie. Nie jest to wyczerpujący test dowolnych modeli ani formalizacja Lean.
Ponownie uruchomiono lokalne kopie wcześniejszych regresji: OUTER PASS 3288 grafów, 22 triangulacje, 2650 spadków potencjału; KEMPE PASS 1016 grafów, 750 i 377 zamian; KUR PASS 79471 układów cyklicznych, 156 grafów trójspójnych, 2196 krawędzi. Ponowiono równoważny test TREE w JS: PASS 1442 drzewa, 249963 multizbiory etykiet.

## Stabilizacja
CI: dostępne zapytania o statusy i workflow commitu źródłowego zwracają puste listy. Lokalny pdflatex dostępny, ale rzeczywista próba git ls-remote zwróciła Could not resolve host: github.com. Pełny PDF nie został zbudowany ani obejrzany. Etap A OTWARTY.
Wznowienie: sprawdzić dowód istnienia kontrakcji zachowującej trójspójność, szczególnie przypadek separatorów nakładających się; następnie kontrola odsyłaczy, pełnej kompilacji i PDF przed zamknięciem A oraz niezależnym B tego samego rozdziału.
