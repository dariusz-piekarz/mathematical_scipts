# Teoria grafów i węzłów — ekspandery, audyt wstępny 01

Data: 2026-11-23. Gałąź: \`biblioteka-matematyczna-iteracja-6\`.

**Status: NOWY MODUŁ — DO WALIDACJI I STABILIZACJI.**

## Zakres

Dodano rozdział \`chapters/pl/graph_and_knot_theory/43-ekspandery-widmo-laplasjanu-i-spacery-losowe.tex\` po stabilnym rozdziale o grafach losowych. Historyczne definicje grafów prostych i macierzy sąsiedztwa z rozdziału 01 zostały zachowane, a nowy materiał nie dubluje wcześniejszych dowodów.

1. Dokładne definicje ekspansji krawędziowej \`h_E\`, wierzchołkowej \`h_V\` oraz normalizacji \`Phi=h_E/d\` dla grafów regularnych; porównanie \`Phi <= h_V <= d Phi\`.
2. Definicja rodziny ekspanderów o wspólnym ograniczonym stopniu i \`|V|→∞\`; rozróżnienie od grafów pełnych o stopniu rosnącym.
3. Znormalizowany Laplasjan \`L=I-A/d\`: postać energetyczna, widmo w \`[0,2]\`, jądro, spójność i iloraz Rayleigha.
4. **Pełny dowód nierówności Cheegera** \`lambda_2/2 <= Phi <= sqrt(2 lambda_2)\`, ze szczegółowym argumentem współpowierzchniowym, funkcją dodatnią i sumowaniem po poziomach.
5. Współmierne kryterium ekspandera przez dodatnią lukę spektralną w rodzinach \`d\`-regularnych.
6. Leniwy spacer losowy \`Q=(I+A/d)/2\`, rozkład jednostajny i jego stacjonarność, zbieżność w wariacji całkowitej oraz jawne ograniczenie tempa mieszania.
7. Rozwój kul i ograniczenie średnicy z ekspansji wierzchołkowej.
8. Dokładne przykłady \`K_n\` i \`C_n\` oraz rysunek TikZ granicy zbioru \`S={0,1,2}\` w \`C_8\`.

## Matematyka — kluczowe warunki

W każdej definicji i tezie określono graf, parametry \`n,d\`, warunek regularności, a tam gdzie potrzebna jest spójność, wskazano ją jawnie. Leniwy wariant spaceru usuwa przypadek okresowy dwudzielnego grafu. Grafy pełne nie są traktowane jako rodzina o ograniczonym stopniu.

## Niezależne testy

Dodano \`tools/tests/test_graph_and_knot_expanders.py\`:
- enumeracja wszystkich grafów prostych na 2–6 wierzchołkach;
- wyznaczanie stałych ekspansji poprzez niezależne przejrzenie wszystkich przekrojów i granic wierzchołkowych;
- własna implementacja algorytmu Jacobiego dla symetrycznych wartości własnych (bez NumPy) oraz kontrola obu nierówności Cheegera;
- dokładna postać energetyczna, kontrola liczby składowych i luki spektralnej;
- leniwy spacer z macierzą przejścia zbudowaną z \`fractions.Fraction\`, kontrola ograniczenia w wariacji całkowitej dla kolejnych czasów;
- wzory dla \`K_n\` i \`C_n\`, przypadek niespójnego grafu 2-regularnego, granice średnicy;
- integracja ze spisem treści i \`catalog/books.json\`: **44** pliki, nowy rozdział pod indeksem 12.

Wszystkie historyczne testy BFS/DFS, A*, CH, MST, przepływów, twierdzenia Turána/Ramseya i grafów losowych pozostały obowiązkowe. Rozszerzono workflow o trzykrotną kompilację rzeczywistego fragmentu książki \`00–05+37–43\`, etykiety i kontrolę ostrzeżeń LaTeX.

## Warunek dalszych prac

Pierwsza walidacja GitHub Actions, niezależna kontrola wzorów, dowodów i rysunku w PDF, korekty, powtórzenie wszystkich testów i dopiero wówczas raport stabilizacji. **Nie oznaczać modułu jako stabilnego przed uzyskaniem i skontrolowaniem wyników CI.**
