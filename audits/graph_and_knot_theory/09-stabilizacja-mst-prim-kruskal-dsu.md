# Teoria grafów i węzłów — stabilizacja MST, Prim, Kruskal i DSU

Data audytu: 2026-11-23.

**Wynik: STABILNY W ZAKRESIE ROZDZIAŁU 39 I JEGO LOKALNEJ INTEGRACJI.**
Nie oznacza to zakończenia globalnego audytu matematycznego wcześniejszych 36 rozdziałów skryptu.

## Kontrolowana wersja

Kod matematyczny, regresje i poprawiony rysunek:
[commit de9ff4cd472087feed3da2a47381047c788fd9b3](https://github.com/dariusz-piekarz/mathematical_scipts/commit/de9ff4cd472087feed3da2a47381047c788fd9b3).

[Potwierdzone testy grafów i PDF — GitHub Actions 45142662022](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45142662022):
- \`finite-models\`: success;
- \`chapter-pdf\`: success.
[Kontrole aplikacji Atlas — 45142662089](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45142662089): success.
[Kontrola terminologii — 45142662080](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45142662080): success.

## Kontrola matematyczna

Rozdział:
\`chapters/pl/graph_and_knot_theory/39-minimalne-drzewa-rozpinajace-prim-kruskal-dsu.tex\`.

Zostały osobno sprawdzone definicje MST i MSF dla grafów niespójnych,
twierdzenie o najlżejszej krawędzi przekroju, własność cyklu,
jednoznaczność przy wagach parami różnych, dowody poprawności
algorytmów Kruskala i Prima, poprawność i oszacowania DSU oraz
złożoność algorytmów.

Klasyczny wynik amortyzowany o odwrotności funkcji Ackermanna
został jawnie oznaczony jako zewnętrzny; logarytmiczne
oszacowanie DSU ma własny dowód.

Test \`tools/tests/test_graph_and_knot_mst.py\`:
- 4166 wyczerpujących przypadków grafów do czterech wierzchołków
  o wagach ze zbioru \`{-2, 0, 3}\` albo z brakiem krawędzi;
- 490 deterministycznych grafów pięcio- i sześciowierzchołkowych;
- niezależny enumeracyjny oracle bada wszystkie lasy rozpinające
  i porównuje optimum z wyjściami Prima i Kruskala;
- kontrola podziału klas DSU, kryterium przekroju, własności cyklu,
  jednoznaczności przy wszystkich wagach parami różnych;
- kontrola przykładów liczonych ręcznie, wag ujemnych i remisów,
  grafów niespójnych, pustych oraz wierzchołków izolowanych.

Przeszły również wcześniej istniejące testy BFS/DFS,
dróg ważonych, A* i hierarchii kontrakcji.

## Skład LaTeX i grafika

Po dwóch rundach:
- fragment książki 00–05 + 37 + 38 + 39 skompilowano
  dwukrotnie przez \`pdflatex\`;
- końcowy PDF ma **51 stron**, strony 47–51 zawierają
  nowy rozdział (strony drukowane 44–48);
- końcowy log bez ostrzeżeń \`LaTeX Warning\`,
  \`Overfull \\hbox\` i \`Overfull \\vbox\`;
- sprawdzono etykiety nowego rozdziału
  \`ch:tg-mst\`, \`thm:tg-mst-cut\`,
  \`thm:tg-mst-kruskal\`, \`thm:tg-mst-prim\`,
  \`fig:tg-mst-five\`;
- stwierdzony we wstępnym PDF problem z etykietami
  wag \`4\` i \`5\` na rysunku został poprawiony;
  w końcowym artefakcie (strona 51)
  wagi są czytelne i nie kolidują z wierzchołkami.
- książka i \`catalog/books.json\` zawierają
  tę samą kolejność **40** plików źródłowych.

## Dalszy plan

Po stabilizacji rozdziału MST dopuszczalne jest przejście do
algorytmów maksymalnego przepływu i minimalnego przekroju
(Edmonds--Karp, Dinic, konstrukcja sieci resztowej).
W następnym module najpierw sprawdzić istniejące definicje
sieci w rozdziale 04, aby nie dublować pojęć,
a po utworzeniu nowego tekstu przeprowadzić niezależne
testy enumeracyjne, matematyczny audyt i rzeczywistą kontrolę PDF.
