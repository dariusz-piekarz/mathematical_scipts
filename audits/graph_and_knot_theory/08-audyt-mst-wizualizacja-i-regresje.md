# Audyt MST — iteracja 02: PDF, figury i jednoznaczność

Dnia 2026-11-23 po wprowadzeniu nowego rozdziału o algorytmach Prima, Kruskala i DSU przeprowadzono kontrolę kompilacji oraz niezależnych modeli grafowych.

## Wynik pierwszego przebiegu CI
[GitHub Actions — 45142058285](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45142058285):
- zadanie \`finite-models\`: **success**;
- zadanie \`chapter-pdf\`: **success**;
- 4166 wyczerpująco wygenerowanych małych grafów o wagach z \`{brak, -2, 0, 3}\`, ponadto 490 deterministycznych przypadków grafów o pięciu i sześciu wierzchołkach;
- porównano Prima i Kruskala z **niezależnym algorytmem enumeracyjnym**, który sprawdza wszystkie lasy rozpinające i ich koszty;
- osobno kontrolowano podział oraz rozmiary DSU, własność przekroju i eliminację ściśle najcięższej krawędzi cyklu;
- przeszły również wcześniejsze testy BFS/DFS, dróg ważonych, A* i CH.

Wydrukowano 51 stron fragmentu książki 00–05+37+38+39, bez ostrzeżeń LaTeX i bez \`Overfull\`. Źródłem kontroli wizualnej jest PDF z rzeczywistego artefaktu workflow.

## Wynik wizualnego audytu
Na stronie 51/48 numeracji książki dostrzeżono nakładanie się etykiety \`5\` na otoczenie wierzchołka \`c\` oraz zbyt bliskie sąsiedztwo etykiety \`4\` i górnych krawędzi. Technicznie PDF przechodził, ale rysunek nie spełniał standardu czytelności. Zmodyfikowano trasowanie krawędzi przerywanych: wagę \`4\` przeniesiono do wnętrza, a krawędź o wadze \`5\` wyprowadzono łukiem ponad wierzchołkiem \`c\`.

## Wzmocnienie testu
Dotychczasowy test sprawdzał tylko, że przy unikalnym optimum i różnych wagach wyjście Kruskala jest jedynym rozwiązaniem. W nowej wersji niezależnie sprawdza **faktyczną jednoznaczność optimum**, gdy wszystkie wagi grafu są parami różne, zgodnie z udowodnionym twierdzeniem.

## Status
**Do potwierdzenia w kolejnym przebiegu CI i do ponownej wizualnej inspekcji**. Sam wynik pierwszego CI nie wystarcza do zamknięcia audytu rysunku. Po pozytywnej kontroli można oznaczyć sam nowy rozdział jako stabilny; nie dotyczy to globalnego audytu całego skryptu.
