# Grafy losowe — niezależny audyt 02: matematyka, testy i skład

Data: 2026-11-23. Rozdział: \`chapters/pl/graph_and_knot_theory/42-grafy-losowe-i-metoda-probabilistyczna.tex\`.

## Wyniki pierwszego CI
[GitHub Actions 45150118695](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45150118695):
- \`finite-models\`: **success**;
- \`chapter-pdf\`: **success**;
- dokładne (na ułamkach \`Fraction\`) sprawdzenie **38 268** grafów z różnymi rozkładami Bernoulliego, od 0 do 6 wierzchołków;
- **36** niezależnych przypadków weryfikacji oczekiwanej liczby monochromatycznych klik i oszacowań Ramseya;
- historyczne testy BFS/DFS, Dijkstry/A*, CH, MST/DSU, przepływów oraz Turána/Ramseya również zakończone sukcesem;
- 70-stronicowy PDF A4, trzy przebiegi \`pdflatex\`, bez ostrzeżeń o odsyłaczach i przepełnień.

## Niezależna kontrola dowodów

- Model \`G(n,p)\` jest oparty na niezależnych wskaźnikach krawędzi; wariancje liczby krawędzi i stopni wynikają z sum niezależnych zmiennych Bernoulliego.
- Wariancja liczby trójkątów została sprawdzona przez dokładne zliczenie nieuporządkowanych par różnych trójkątów mających wspólną krawędź: \`C(n,2)*C(n-2,2)\`. Trójkąty mające wspólny tylko wierzchołek są niezależne jako funkcje rozłącznych zestawów wskaźników krawędzi.
- Pierwszy moment przy \`np→0\` i drugi moment przy \`np→∞\` prowadzą do progu trójkątów \`p~1/n\`. Zbadano wyrażenie \`Var(X)/(EX)^2\`.
- Dla wierzchołków izolowanych wspólna krawędź \`uv\` jest liczona raz, co daje dokładnie \`2n-3\` niezależnych braków krawędzi; wykorzystano ten fakt w wariancji i dowodzie dolnej strony progu spójności.
- Górna strona progu spójności nie polega na utożsamieniu braku izolowanych wierzchołków ze spójnością; oddzielnie oszacowano sumę prawdopodobieństw istnienia składowej rozmiaru \`1≤k≤n/2\`, dzieląc zakres przy \`k=n/log n\`. Założenie \`a_n=o(log n)\` zapewnia, że \`p_n^-\` i \`p_n^+\` są prawdopodobieństwami.
- Losowe kolorowanie \`K_n\`: prawdopodobieństwo monochromatyczności ustalonej \`K_k\` to \`2^(1-C(k,2))\`; argument Markowa pokazuje istnienie kolorowania, gdy oczekiwana liczba takich klik jest mniejsza niż 1.

## Korekta wynikająca z kontroli wizualnej

PDF z pierwszego CI miał **70 stron**. Strona 70 zawierała jedynie końcowy akapit zapowiadający ekspandery; nie ma tam nowego twierdzenia ani dowodu. Ten akapit powtarza zapowiedź z wprowadzenia rozdziału i planu projektu, więc usunięto go, zachowując pełną treść matematyczną. Po korekcie konieczna jest ponowna kompilacja i kontrola czy końcowy rozdział mieści się bez pustej strony.

Ilustracja przykładowej realizacji \`G(6,p)\` oraz wzory na stronach 64–69 pierwszej wersji były czytelne; nie stwierdzono kolizji elementów.

## Status

**Jeszcze nie stabilny w tej iteracji** — należy zaczekać na świeże CI po zmianie źródła, sprawdzić końcową liczbę stron i poprawne odsyłacze, dopiero potem nadać status stabilizacji.
