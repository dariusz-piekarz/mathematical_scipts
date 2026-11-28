# Grafy i węzły — niezależny audyt BFS/DFS, iteracja 02

Stan: **w toku — audyt kontrolny i regresje**, jeszcze nie oznaczamy jako stabilny przed potwierdzeniem PDF CI.

## Stwierdzona wada w integracji
W poprzedniej iteracji rozdział 37 został podłączony do \`books/pl/graph_and_knot_theory.tex\`, ale wpisu zabrakło w \`catalog/books.json\`.
Poprawiono: dodano ten sam plik dokładnie po historycznym rozdziale 05 w katalogu, zgodnie z kolejnością \`\\input\` w książce.

## Przegląd matematyczny i redakcyjny
1. **BFS:** niezmiennik kolejki, wniosek o odległościach i odtwarzaniu najkrótszej drogi sprawdzone na modelach skończonych. Obsłużono niespójność, izolowane wierzchołki i wielokrotne najkrótsze drogi.
2. **DFS:** sprawdzono zagnieżdżenie czasów, rodziców i wykrywanie cyklu. Dookreślono znaczenie terminu „przodek”: zawiera sam wierzchołek.
3. **Mosty:** weryfikacja niezależna przez usuwanie pojedynczej krawędzi i przeliczanie liczby składowych; w rozdziale kryterium \`low\` jawnie ograniczone do grafów prostych.
4. **DAG:** uproszczono i wzmocniono dowód: brak łuków do wierzchołków szarych implikuje ścisłą nierówność \`tout\` na każdym łuku, która wyklucza cykl.
5. **Rysunek:** dodano podpis, etykietę i odstęp między podpisami warstw a wierzchołkami (TikZ).
6. **Koszt:** oszacowania \`O(n+m)\` odnoszą się do list sąsiedztwa i jawnie uwzględniają obie orientacje wpisów w grafie nieskierowanym.

## Niezależne testy
Niezależne modele przetestowano lokalnie na 1099 grafach prostych nieskierowanych o 1–5 wierzchołkach i 4165 grafach skierowanych bez pętli o 1–4 wierzchołkach. Oczekiwane odpowiedzi pochodziły z innego algorytmu: relaksacji dróg, usuwania krawędzi i przeliczania składowych, pełnej enumeracji kolorowań oraz algorytmu Kahna.

W repozytorium dodano samodzielny test regresyjny \`tools/tests/test_graph_and_knot_bfs_dfs.py\` i workflow \`.github/workflows/graph-and-knot-algorithms.yml\`; workflow uruchamia testy enumeracyjne, a także rzeczywistą kompilację PDF podzbioru 00–05+37 przy użyciu preambuły książki oraz zapisuje PDF i logi jako artefakty.

## Warunek stabilizacji
Rozdział będzie można uznać za stabilny, gdy oba zadania nowego CI zakończą się sukcesem, a PDF nie wykaże krytycznych problemów składu, etykiet i rysunku. Bieżący raport nie zastępuje jeszcze weryfikacji wyniku na GitHub Actions.
