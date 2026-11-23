# Teoria grafów i węzłów — moduł MST: audyt wstępny 01

Data: 2026-11-23.
Gałąź: \`biblioteka-matematyczna-iteracja-6\`.
Status początkowy: **NOWY, WYMAGA CI I DALSZEGO AUDYTU**.

## Poprzedni materiał i decyzja o integracji

Sprawdzono definicje drzew rozpinających, cykli fundamentalnych i przekrojów w dotychczasowym rozdziale 02 oraz ujęcie lasów BFS/DFS w rozdziale 37. Pozostawiono ten materiał bez powielania; nowy rozdział odwołuje się do niego. Prefiks 39 jest identyfikatorem źródłowym, nie numerem w gotowym składzie książki. Po historycznym rozdziale 05 występują teraz kolejno 37 (BFS/DFS), 38 (drogi ważone, A*, CH) i 39 (MST), a dopiero potem 06.

## Nowy rozdział

\`chapters/pl/graph_and_knot_theory/39-minimalne-drzewa-rozpinajace-prim-kruskal-dsu.tex\`:
1. Definicje MST, MSF, koszty, graf niespójny, wagi ujemne, zerowe i z remisami;
2. Twierdzenie o najlżejszej krawędzi przekroju i niezależnie udowodniona własność cyklu;
3. Jednoznaczność MSF przy wagach parami różnych, wraz z ostrzeżeniem, że warunek jest tylko wystarczający;
4. Kruskal z dowodem niezmiennika przedłużalności lasu do MSF;
5. DSU: \`find\`, \`union\`, łączenie według rozmiaru, kompresja ścieżek i samodzielny dowód ograniczenia logarytmicznego;
6. Prim jako kolejka krawędzi przekraczających aktualny przekrój i przypadek grafu niespójnego;
7. Koszty obliczeniowe obu algorytmów, przykłady liczone ręcznie i rysunek TikZ.

Granice dowodów: silniejsze amortyzowane oszacowanie DSU z odwrotnością funkcji Ackermanna przyjęto jako wynik klasyczny, wyraźnie oznaczony; dowód logarytmicznego oszacowania został podany.

## Niezależne testy i CI

Dodano \`tools/tests/test_graph_and_knot_mst.py\`. Zamiast porównywać tylko Prima i Kruskala, test enumeruje kandydatów na las rozpinający, sprawdza spójność niezależnie przez DFS i wyznacza optymalny koszt. Sprawdza dodatkowo warunki przekroju i cyklu, klasy oraz rozmiary DSU, brak cykli, graf pusty, wierzchołki izolowane, grafy niespójne, wagi ujemne i remisy. Obejmuje wszystkie małe grafy do czterech wierzchołków i deterministyczne losowe grafy pięcio- i sześciowierzchołkowe. Zmieniono historyczne asercje liczby plików z 39 na 40; \`catalog/books.json\` musi być dokładnie zgodny z kolejnością \`\\input\`.

Workflow \`.github/workflows/graph-and-knot-algorithms.yml\` uruchamia wszystkie historyczne regresje BFS/DFS i dróg ważonych oraz nowy test MST, a także składa PDF fragmentu 00–05+37+38+39 z kontrolą etykiet, rysunku i przepełnień LaTeX.

## Warunek przejścia dalej

Najpierw wynik testów oraz realnej kompilacji PDF; następnie osobna kontrola matematyczna dowodów, wizualna diagramu i składu, poprawki oraz końcowy raport stabilizacji. Dopiero potem moduł maksymalnego przepływu i minimalnego przekroju.
