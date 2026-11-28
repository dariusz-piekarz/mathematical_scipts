# Teoria grafów i węzłów — audyt wstępny 01: grafy losowe i metoda probabilistyczna

Data: 2026-11-23. Gałąź: \`biblioteka-matematyczna-iteracja-6\`.
**Status: NOWY MODUŁ, NIEUSTABILIZOWANY.** Konieczne dalsze audyty, niezależne testy, trzy przebiegi PDF i kontrola wizualna.

## Zakres

Dodano \`chapters/pl/graph_and_knot_theory/42-grafy-losowe-i-metoda-probabilistyczna.tex\` po stabilnym rozdziale 41 o twierdzeniach Mantela, Turána i Ramseya. Nie zmieniono dotychczasowych dowodów. Kolejny osobny temat: expandery.

1. Precyzyjna przestrzeń probabilistyczna modelu Erdősa–Rényiego \`G(n,p)\`, zmienne Bernoulliego i niezależność krawędzi.
2. Dokładny rozkład i momenty liczby krawędzi oraz stopni; koncentracja z nierówności Czebyszewa.
3. Nierówności pierwszego i drugiego momentu z dowodami; liczba trójkątów z kowariancjami trójkątów mających wspólną krawędź.
4. Próg pojawiania się trójkąta \`p ~ 1/n\`; dowód przez pierwszy i drugi moment.
5. Wierzchołki izolowane: dokładna wartość oczekiwana i wariancja; dwustronny próg spójności dla \`p=(log n ± a_n)/n\`, \`a_n→∞\`, \`a_n=o(log n)\`, z jawnym oszacowaniem sumy po składowych.
6. Pierwszy moment dla klik dowolnego ustalonego rozmiaru, wraz z właściwym wykładnikiem \`n^{-2/(r-1)}\`.
7. Losowe dwukolorowanie \`K_n\` i probabilistyczne dolne oszacowanie \`R(k,k)\`, w szczególności wykładnicze ograniczenie z użyciem \`k!\`.
8. Ilustracja przykładowej realizacji grafu i dokładnie omówiony przykład spójności \`G(3,p)\`.

## Kontrola założeń

Twierdzenia progowe dotyczą ciągów prawdopodobieństw i granic \`n→∞\`, nie deterministycznych własności pojedynczego grafu. Przy spójności narzucono \`a_n=o(log n)\`, aby oba rozważane parametry znajdowały się w \`[0,1]\` dla dużych \`n\`. Wzory na wierzchołki izolowane rozpatrują \`n≥2\`, a przypadek pustego grafu jest dopuszczony w modelu.

## Niezależne kontrole

Dodano \`tools/tests/test_graph_and_knot_random.py\`:
- dokładna enumeracja wszystkich oznaczonych grafów na 0–6 wierzchołkach z wagami probabilistycznymi jako \`Fraction\` (bez symulacji);
- porównanie wartości oczekiwanych i wariancji krawędzi, trójkątów i wierzchołków izolowanych, bezpośrednie sprawdzenie obu nierówności momentowych;
- niezależna rekurencja prawdopodobieństwa spójności przez rozkład według składowej wierzchołka 0;
- enumeracja dwukolorowań małych grafów pełnych, weryfikacja średniej liczby monochromatycznych klik oraz probabilistycznego dolnego oszacowania Ramseya;
- 43 wpisy \`catalog/books.json\` w identycznej kolejności jak \`\\input\` i kontrola etykiet/środowisk LaTeX.

Historyczne testy BFS/DFS, A*/CH, MST/DSU, przepływów i Turána/Ramseya nadal są obowiązkowe. Rozszerzono workflow o nowy test i skład fragmentu 00–05+37–42, z trzema przebiegami \`pdflatex\` i ostrym sprawdzaniem odsyłaczy/przepełnień.

## Dalszy plan audytu

Po utworzeniu rozdziału należy sprawdzić wyniki pierwszego CI i rzeczywisty PDF, następnie niezależnie zweryfikować dowody (zwłaszcza kowariancje, warunki w progach i konstrukcję Ramseya), poprawić wykryte błędy i ponowić wszystkie kontrole. Nie nadawać statusu stabilnego bez tego procesu.
