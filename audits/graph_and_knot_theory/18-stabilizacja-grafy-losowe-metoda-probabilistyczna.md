# Teoria grafów i węzłów — stabilizacja grafów losowych i metody probabilistycznej

Data: 2026-11-23.

**WYNIK: STABILNY W ZAKRESIE NOWEGO ROZDZIAŁU 42 I JEGO LOKALNEJ INTEGRACJI.**
Status nie oznacza ukończenia globalnego audytu wszystkich historycznych rozdziałów skryptu ani formalizacji dowodów w Lean.

## Źródła i zakres

Rozdział: \`chapters/pl/graph_and_knot_theory/42-grafy-losowe-i-metoda-probabilistyczna.tex\` (końcowa wersja po korekcie składu w commicie [23c649c5122aeb15420ca55e51e0f0deea9e2ef9](https://github.com/dariusz-piekarz/mathematical_scipts/commit/23c649c5122aeb15420ca55e51e0f0deea9e2ef9)).

Raporty poprzednich etapów:
- \`audits/graph_and_knot_theory/16-grafy-losowe-gnp-metoda-probabilistyczna-audyt-01.md\`;
- \`audits/graph_and_knot_theory/17-grafy-losowe-audyt-02-sklad-i-dowody.md\`.

Treść rozdziału:
- model Erdősa–Rényiego \`G(n,p)\` z niezależnymi wskaźnikami krawędzi;
- wartości oczekiwane i wariancje liczby krawędzi, stopni i trójkątów;
- metoda pierwszego i drugiego momentu z dowodami;
- próg pojawiania się trójkąta \`p~1/n\`;
- wariancja liczby wierzchołków izolowanych i dwustronny próg spójności \`p~(log n)/n\` wraz z jawnymi założeniami na ciąg \`a_n\`;
- pierwsze momenty liczby większych klik;
- metoda losowego dwukolorowania \`K_n\` i wykładnicze dolne oszacowanie \`R(k,k)\`;
- przykład prawdopodobieństwa spójności \`G(3,p)\` i rysunek przykładowej realizacji \`G(6,p)\`.

## Niezależna weryfikacja matematyczna

W audycie szczegółowym sprawdzono:
1. Sumy zmiennych Bernoulliego, warunki niezależności i poprawność wzorów dla liczby krawędzi i stopnia.
2. Warianty wspólnego przekroju trójkątów: rozłączne zbiory krawędzi dają kowariancję zero, wspólna krawędź prowadzi do \`p^5(1-p)\`; liczba nieuporządkowanych par o wspólnej krawędzi wynosi \`C(n,2)C(n-2,2)\`.
3. Iloraz wariancji i kwadratu średniej w dowodzie progu trójkąta, z odróżnieniem \`np→0\` i \`np→∞\`.
4. Kowariancję izolowanych wierzchołków wymagającą braku \`2n-3\` różnych krawędzi, dokładną wariancję i argument drugiego momentu.
5. Oszacowanie spójności od góry przez sumę zdarzeń istnienia rozdzielonej składowej wielkości \`k\`, z podziałem na \`k≤n/log n\` oraz \`n/log n<k≤n/2\`. Brak izolowanych wierzchołków nie został błędnie utożsamiony ze spójnością.
6. Rozmiar kliki \`r\` i warunek \`p=o(n^{-2/(r-1)})\` otrzymany z pierwszego momentu.
7. Prawdopodobieństwo monochromatycznej kliki w losowym dwukolorowaniu: \`2^{1-C(k,2)}\`, a także wniosek z \`E X<1\` o istnieniu kolorowania bez takiej kliki.

## Rzeczywiście wykonane testy

[GitHub Actions — końcowy przebieg 45150566514](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45150566514):
- \`finite-models\`: **success**;
- \`chapter-pdf\`: **success**.

Test \`tools/tests/test_graph_and_knot_random.py\` sprawdził:
- **38 268 dokładnych enumeracji grafów** z parametrami \`p\` reprezentowanymi przez \`fractions.Fraction\`, w tym wszystkie grafy na sześciu wierzchołkach przy \`p=1/2\`, a na mniejszych zbiorach również \`p=0,1/3,2/3,1\`;
- bezpośrednie rozkłady i momenty liczby krawędzi, trójkątów i izolowanych wierzchołków, niezależną rekurencję prawdopodobieństwa spójności;
- **36** zestawów sprawdzających oczekiwane liczby jednobarwnych klik oraz dolne oszacowanie Ramseya;
- graniczne przypadki grafów pustych, wartość \`p=0\` i \`p=1\`, kontrolę etykiet i spójności rozdziału z katalogiem książki.

Przeszły również wszystkie obowiązujące testy wcześniejszych modułów BFS/DFS, Dijkstry/A*, CH, MST/DSU, przepływów i teorii ekstremalnej.

## Końcowy skład PDF i kontrola wzrokowa

- W pierwszej wersji po audycie powstał 70-stronicowy PDF; strona 70 zawierała tylko powtórzoną zapowiedź przyszłego rozdziału o ekspanderach.
- Usunięto wyłącznie ten redakcyjnie redundantny akapit, bez zmian w definicjach, twierdzeniach, wzorach i dowodach.
- Po ponownym uruchomieniu CI uzyskano **69-stronicowy PDF A4**; nowy rozdział zajmuje strony PDF 64–69 i kończy się na pełnej, czytelnie złożonej stronie 69.
- Trzy udane przebiegi \`pdflatex\`; końcowy log nie ma ostrzeżeń \`LaTeX Warning\` o odsyłaczach ani \`Overfull\`.
- Sprawdzono wizualnie strony 64–69, w tym rysunek grafu \`G(6,p)\`, wzory i podpisy: bez kolizji i nieczytelnych elementów.

Pozostałe potwierdzone kontrole dla końcowego commita:
- [Mathematical library application checks — 45150566512](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45150566512): **success**;
- [Polish mathematical terminology — 45150566511](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45150566511): **success**.

\`catalog/books.json\` i \`books/pl/graph_and_knot_theory.tex\` mają identyczną kolejność **43** plików źródłowych.

## Dalsza kolejność

Można przejść do **oddzielnego modułu o ekspanderach** (ekspansja krawędziowa i wierzchołkowa, Laplasjan i wartości własne, mieszanie spacerów losowych, przykłady), stosując ten sam rytm: stworzenie jednego rozdziału, niezależne audyty matematyczne, testy, faktyczna kompilacja i wizualna kontrola PDF, dopiero potem stabilizacja i kolejny moduł.
