# Teoria grafów i węzłów — audyt wstępny i iteracja 01 modułu algorytmicznego

Gałąź docelowa: \`biblioteka-matematyczna-iteracja-6\`.

## Audyt zależności przed dodaniem
Przejrzano definicje i odpowiednie miejsca rozdziałów 01, 02, 03, 04, 05 oraz 08.
- Rozdział 01 definiuje graf prosty, drogę i odległość \`d_G\`. Nowy tekst używa tych samych pojęć.
- Rozdział 02 wspomina BFS/DFS bez pełnego algorytmu i dowodu poprawności; nowy rozdział doprecyzowuje ich działanie i związki z drzewami.
- Rozdział 03 wykorzystuje własność krawędzi niedrzewowych DFS w grafie nieskierowanym. Nowy rozdział daje jej osobny dowód.
- Rozdział 04 zawiera już pojęcie sieci przepływowej, więc późniejszy moduł o maksymalnym przepływie powinien rozszerzyć ten model, a nie powielać definicje.
- Rozdział 05 operuje ścieżkami powiększającymi; przyszłe algorytmy skojarzeń powinny odwoływać się do tej konstrukcji.
- Rozdział 08 zawiera laplasjan i własności spektralne; nie jest potrzebna modyfikacja przed wprowadzeniem BFS/DFS.

## Dodany materiał
Nowy samodzielny plik \`chapters/pl/graph_and_knot_theory/37-algorytmiczne-przeszukiwanie-grafow-bfs-dfs.tex\`:
1. model list sąsiedztwa i złożoność;
2. BFS, niezmiennik kolejki, najkrótsze drogi, odtwarzanie rodziców;
3. składowe spójne i test dwudzielności;
4. DFS, czasy wejścia i wyjścia, las DFS i relacja przodka;
5. mosty przez \`low\`, cykle;
6. rozpoznawanie skierowanych cykli i sortowanie topologiczne;
7. przykłady, rysunek TikZ, odsyłacze i koszty.

## Kontrole tej iteracji
- Kontrakt pojęciowy: rozróżniono grafy nieskierowane od skierowanych, a wyniki o mostach ograniczono do grafów prostych.
- Podano osobne dowody poprawności BFS, własności DFS, kryterium mostu, dwudzielności i sortowania topologicznego.
- Każde oszacowanie \`O(n+m)\` uzależniono od reprezentacji listowej; policzono przeglądanie wpisów.
- Zaznaczono wymóg odróżniania krawędzi równoległych w multigrafach.
- Zachowano istniejące środowiska LaTeX i style TikZ bez dodawania zależności do preambuły.
- Nowy plik dodano logicznie po rozdziale 05 w \`books/pl/graph_and_knot_theory.tex\`. Prefiks \`37\` jest identyfikatorem nowego pliku, nie jego numerem w składzie; uporządkowanie prefiksów wymaga ostrożnej końcowej migracji nazw i odsyłaczy, nie wykonywać jej bez globalnej kontroli.
- Nie wykonano jeszcze faktycznej kompilacji PDF ani kontroli renderingu rysunku; rozdział ma status **wstępny, do ponownego audytu**, nie „stabilny”.

## Dalszy plan
1. Niezależny audyt szczegółowy nowego rozdziału: przypadki graniczne, dowody, skład TikZ, kompilacja i CI; poprawiać aż do stabilizacji.
2. Dopiero potem kolejny rozdział: najkrótsze drogi ważone (Dijkstra, Bellman–Ford, Floyd–Warshall).
3. Następnie minimalne drzewa rozpinające oraz algorytmiczna teoria przepływów.
4. Po ustabilizowaniu nowych rozdziałów: teoria ekstremalna i losowa, dodatkowe niezmienniki węzłów, obliczenia; na końcu pełne audyty całego skryptu.
