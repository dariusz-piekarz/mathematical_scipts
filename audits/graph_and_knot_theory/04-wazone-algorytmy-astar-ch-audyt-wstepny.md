# Teoria grafów i węzłów — rozdział 38: algorytmy ważone, A* i CH (iteracja 01)

## Zakres utworzonego rozdziału

Zachowano wcześniejszy stabilny rozdział 37 BFS/DFS. Nowy rozdział 38 dodano bezpośrednio po nim w \`books/pl/graph_and_knot_theory.tex\` i \`catalog/books.json\`.
Numer 38 oznacza numer pliku, a nie numer rozdziału w złożonej książce.

- Wagi i odległości, cykle ujemne, relaksacja.
- Dijkstra: poprawność dla wag nieujemnych, warianty kopca i koszty.
- Bellman--Ford: wagi ujemne, wykrywanie osiągalnych cykli ujemnych.
- Floyd--Warshall: rekurencja programowania dynamicznego i wszystkie pary.
- A*: heurystyki dopuszczalne i spójne, dowód przez redukcję do Dijkstry; ostrzeżenie o konieczności ponownego otwierania przy niespójności.
- Dwukierunkowy Dijkstra: graf odwrócony, minima kolejek i poprawne zatrzymanie.
- Contraction Hierarchies: dokładny wariant dla nieskierowanych grafów o dodatnich wagach, skróty, rangi i dowód poprawności zapytań; koszt przygotowania, charakterystyka zastosowań.

## Audyt wymagań i zakresu

Zwrócono uwagę, że nie istnieje uniwersalnie najszybszy algorytm.
A* nie musi przyspieszać bez silnej heurystyki. Dla CH opisano konkretny model z przygotowaniem danych i bez pomijania koniecznych skrótów.
Łuki odwrócone są obowiązkowe dla przeszukiwania dwukierunkowego w grafie skierowanym.
Wartości minus nieskończoność ograniczono do wierzchołków osiągalnych z osiągalnych cykli ujemnych.
Dodano figurę TikZ i odsyłacze. Istniejący test integracyjny BFS/DFS przestawiono na 39 plików.

## Niezależna walidacja

Dodano \`tools/tests/test_graph_and_knot_weighted.py\`.
Zawiera wyczerpujące małe grafy skierowane o nieujemnych wagach z porównaniem Dijkstry, Bellmana--Forda, Floyda--Warshalla, A* i Dijkstry dwukierunkowej;
losowe grafy z wagami ujemnymi, również z cyklami ujemnymi;
heurystyki A* dopuszczalne, ale potencjalnie niespójne;
oraz wszystkie nieskierowane grafy na 1–4 wierzchołkach z wybranymi dodatnimi wagami, z kontrolą CH przy każdej kolejności rang.
Workflow istniejącego modułu grafów rozszerzono o testy oraz kompilację izolowanego fragmentu 00–05+37+38.

## Status

**WSTĘPNY — rozdział nie jest jeszcze stabilny.**
Warunki stabilizacji: sukces enumeracji i PDF CI, kontrola niezależna dowodów oraz inspekcja PDF pod kątem przepełnień i rysunków.
W kolejnej iteracji należy również skontrolować przykłady grafów z rozbieżnymi wagami i skrajne przypadki przy heurystykach A*.
