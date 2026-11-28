# Teoria grafów i węzłów — ekspandery, audyt niezależny 02

Data: 2026-11-23.
Źródło: \`chapters/pl/graph_and_knot_theory/43-ekspandery-widmo-laplasjanu-i-spacery-losowe.tex\`.
Kontrolowana wersja merytoryczna: [commit 95e3cbdee2243903b7c13d9f03b69d69d59e42fa](https://github.com/dariusz-piekarz/mathematical_scipts/commit/95e3cbdee2243903b7c13d9f03b69d69d59e42fa).

## Weryfikacja matematyczna

1. Definicje \`h_E\`, \`h_V\`, \`Phi=h_E/d\` mają niepusty zakres minimalizacji dla \`n>=2\`; przegląd wszystkich zbiorów pokazuje \`h_V<=h_E<=Delta h_V\`. Dla grafów \`d\`-regularnych daje to \`Phi<=h_V<=d Phi\`.
2. Wzór energetyczny \`d <f,Lf>=sum_{uv in E}(f(u)-f(v))^2\` zlicza każdą krawędź dokładnie raz. Jądro \`L\` stanowią funkcje stałe na składowych; konsekwencje dla \`lambda_2=0\` i spójności są poprawne.
3. Charakterystyka Rayleigha wymaga ortogonalności do stałego wektora własnego; w tekście została jawnie zapewniona, również gdy graf jest niespójny.
4. Dowód \`lambda_2<=2 Phi\` wykorzystuje testową funkcję \`chi_S-|S|/n\`, jej normę \`|S|(n-|S|)/n\` oraz energię \`|boundary_E(S)|\`.
5. Dowód \`Phi^2/2<=lambda_2\` dobiera znak wektora własnego \`f\` tak, aby dodatni nośnik \`g=f_+\` miał najwyżej \`n/2\` elementów. Nierówność \`(a-b)(a_+-b_+)>=(a_+-b_+)^2\` oraz całkowanie po zbiorach poziomicowych uzasadniają ostatni krok. Nie pominięto przypadku grafu niespójnego.
6. Macierz leniwego spaceru \`Q=(I+A/d)/2\` jest stochastyczna, symetryczna i ma wartości własne \`eta_i=1-lambda_i/2\` w \`[0,1]\`. Dla grafu spójnego \`eta_2<1\`; nierówność norm \`L1\`-\`L2\` oraz górne ograniczenie normy rozkładu początkowego prowadzą do podanego oszacowania w wariacji całkowitej.
7. Średnica: wzrost kul przez ekspansję wierzchołkową aż do ponad połowy grafu wymusza przecięcie dwóch kul i daje jawne ograniczenie \`2R\`; nie zastosowano wzrostu do zbiorów przekraczających \`n/2\`.
8. Przykłady: \`Phi(K_n)=ceil(n/2)/(n-1)\`, \`lambda_2(K_n)=n/(n-1)\`, \`Phi(C_n)=1/floor(n/2)\`, \`lambda_2(C_n)=1-cos(2pi/n)\`. Rozróżniono grafy o rosnącym stopniu od rodziny o stałym stopniu.

Nie wykryto błędu matematycznego w powyższych rozumowaniach. Aproksymacyjna kontrola widma nie zastępuje matematycznego dowodu twierdzenia ani weryfikacji w Lean.

## Niezależna enumeracja i testowanie

[Github Actions — graph-and-knot 45152247639](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45152247639):
- \`finite-models\`: **success**;
- \`chapter-pdf\`: **success**.
- **33 866** wszystkich prostych grafów na 2–6 wierzchołkach; **193** grafy regularne przeanalizowano dodatkowo względem widma i granic wszystkich zbiorów.
- Dodatkowe **21** przypadków dokładnych rodzin grafów pełnych, cykli i grafu niespójnego \`C_3 ⊔ C_3\`.
- Sprawdzono obie nierówności Cheegera, równość energetyczną, związek luki ze spójnością, porównanie ekspansji, ograniczenie średnicy oraz dokładną ewolucję leniwego spaceru poprzez \`fractions.Fraction\`.
- Jacobi jest niezależną implementacją numeryczną wartości własnych bez \`numpy\`; nierówności sprawdzono z tolerancją numeryczną, a wartości ekspansji liczono dokładnie jako ułamki.
- W tym samym przebiegu ponownie zaliczono historyczne testy BFS/DFS, dróg ważonych, A*/CH, MST/DSU, przepływów, Turána/Ramseya i grafów losowych.

## Rzeczywista kontrola PDF

Pobrano artefakt \`graph-and-knot-expanders-pdf\` z GitHub Actions i skontrolowano jego zawartość:
- **75 stron A4**, nowy rozdział na stronach PDF 70–75 (druk 66–71);
- trzy udane przebiegi \`pdflatex\`; końcowy log bez \`Overfull\`, bez ostrzeżeń o niestabilnych lub niezdefiniowanych odsyłaczach;
- obejrzano renderowane strony rozdziału, w szczególności dowód Cheegera, szacowanie mieszania, wyprowadzenie wzorów dla \`K_n\` i \`C_n\` i rysunek cyklu \`C_8\`;
- rysunek ma czytelne cyfry, poprawnie wyróżnione dwie krawędzie granicy \`S={0,1,2}\` i nie nachodzi na podpis;
- ostatnia strona zawiera rysunek i końcową sekcję, nie jest przypadkowo niemal pusta.

## Integracja z aplikacją i terminologia

Katalog \`catalog/books.json\` i główny plik \`books/pl/graph_and_knot_theory.tex\` mają tę samą kolejność **44** plików źródłowych. Rozdział o ekspanderach jest bezpośrednio po rozdziale o grafach losowych.

[Mathematical library application checks — 45152247716](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45152247716): **success**.
[Polish mathematical terminology — 45152247581](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45152247581): **success**.

## Wniosek audytu

**PASS — rozdział spełnia lokalne warunki stabilizacji**.
Zalecane dalsze rozwinięcia (osobne moduły, dopiero po utrwaleniu tego): jawne konstrukcje ekspanderów o stałym stopniu, związki z kodowaniem, randomizowane algorytmy lub powrót do globalnego audytu całej książki. Nie oznacza to globalnej stabilności wszystkich historycznych rozdziałów.
