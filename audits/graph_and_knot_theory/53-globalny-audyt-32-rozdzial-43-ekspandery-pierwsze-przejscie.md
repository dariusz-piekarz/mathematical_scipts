# Teoria grafów i węzłów — audyt globalny 32: rozdział 43, pierwsze przejście

Data: 2026-11-24. Repozytorium: \`dariusz-piekarz/mathematical_scipts\`.
Gałąź: \`biblioteka-matematyczna-iteracja-6\`, bez tworzenia nowej.
Poprzednia bramka: audyt 31 rozdziałów źródłowych 40–42 **ZAMKNIĘTY**, pełny zdalny CI i PDF potwierdzone w przebiegu 45284927021; rozdziały 01–42 lokalnie stabilne.
Źródło: \`chapters/pl/graph_and_knot_theory/43-ekspandery-widmo-laplasjanu-i-spacery-losowe.tex\`.
To ostatni istniejący plik numerowany; tom zawiera dokładnie 44 pliki numerowane 00–43.

## Kontrola dowodów i założeń

1. **Ekspansje krawędziowa i wierzchołkowa.** Definicje \`h_E\`, \`h_V\` i \`Φ=h_E/d\` minimalizują po niepustych zbiorach o liczności co najwyżej \`n/2\`. Dla grafu o maksymalnym stopniu \`Δ\` porównanie \`h_V≤h_E≤Δh_V\` jest poprawne: każdemu wierzchołkowi granicznemu przypada od 1 do \`Δ\` krawędzi przekroju. Stąd dla regularnego \`Φ≤h_V≤dΦ\`.
2. **Laplasjan.** Tożsamość \`d<f,Lf>=Σ_{uv∈E}(f(u)-f(v))²\` poprawnie wykorzystuje symetrię i \`d\`-regularność; zakres widma \`[0,2]\`, liczba zerowych wartości własnych i wariacyjny opis \`λ₂\` odpowiadają jądru oraz dopełnieniu ortogonalnemu stałych.
3. **Lemat współpowierzchniowy i Cheeger.** Warunek nośnika \`|supp g|≤n/2\` umożliwia zastosowanie \`Φ\` do wszystkich niepustych poziomic \`{g²>t}\`. Zliczenie po krawędziach i nierówność Cauchy'ego–Schwarza dają \`Σ(g(u)-g(v))²≥dΦ² Σg²/2\`. Dowód \`Φ²/2≤λ₂≤2Φ\` jawnie używa funkcji charakterystycznej małego zbioru oraz dodatniej części wektora własnego po wyborze znaku; zerowe \`λ₂\` nie prowadzi do dzielenia przez zero.
4. **Leniwy spacer losowy.** Wymagana jest spójność oraz \`Q=(I+A/d)/2\`, a nie zwykłe \`P=A/d\` (zwykły spacer na \`K₂\` nie miesza się). Widmo \`Q\` na podprzestrzeni o sumie współrzędnych zero leży w \`[0,1-λ₂/2]\`. Nierówność \`||·||₁≤√n||·||₂\` i \`||μ-π||₂²≤1-1/n\` dają podaną granicę wariacji całkowitej. Ograniczenie czasu \`(2/λ₂)log(√n/(2ε))\` wymaga \`λ₂>0\`, zapewnionego spójnością.
5. **Średnica.** Przy \`h_V>0\` kolejne kule dopóki są mniejsze niż połowa \`V\` rosną co najmniej \`1+h_V\` razy. Dwie kule o rozmiarach większych niż połowa wierzchołków przecinają się, dając podane ograniczenie \`2R\`.
6. **Przykłady.** Dla \`K_n\`: \`Φ=ceil(n/2)/(n-1)\`, \`λ₂=n/(n-1)\`. Dla \`C_n\`: \`Φ=1/floor(n/2)\`, \`λ₂=1-cos(2π/n)\`; w obu przypadkach kontrolowano brzegowe \`n\` i zgodność z twierdzeniem Cheegera.

W pierwszej ręcznej kontroli nie wykryto koniecznej poprawki źródłowego twierdzenia. Nie zmieniano zatwierdzonej zawartości rozdziału tylko w celu dodania materiału.

## Niezależne testy regresyjne

Dodano \`tools/tests/test_graph_and_knot_expanders_first_pass.py\`. Bez zależności zewnętrznych:
- enumeruje wszystkie proste grafy na \`n=2,…,6\` wierzchołkach i filtruje **193** grafy regularne o dodatnim stopniu;
- dla każdego z nich osobno wyznacza dokładne \`h_E,h_V\` z enumeracji przekrojów oraz widmo z algorytmu Jacobiego, niezależnego od twierdzenia Cheegera;
- bada oba oszacowania spektralne i ich zachowanie w grafach niespójnych;
- dla każdego spójnego przypadku porównuje dokładną średnicę BFS z boundem ekspansyjnym i przez 11 kroków dokładnych ułamków kontroluje nierówność mieszania leniwego spaceru ze wszystkich wierzchołków początkowych;
- sprawdza osobno wszystkie cykle \`C₃,…,C₁₂\`, grafy pełne \`K₂,…,K₈\` oraz widoczne w źródłowym TeX hipotezy spójności, leniwości i oznaczenia twierdzeń.

Commit testu: \`d15113dafda6dd8aa5ac14e4c84081dc45cc7d64\`. Korekta rygorystycznego oczekiwania liczności rodzin regularnych na dokładne 193: \`5e01d7156e1d2ed2bec1ee1325e652df0cfa7d25\`.
Włączenie do workflow \`graph-and-knot-global-audit.yml\` wraz z \`push.paths\`: \`30c7c5a99e5fb047e7744b3d0cdbe31a93c8fb9a\`.

**W chwili utworzenia tego raportu** przebieg \`https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45289361352\`, przy SHA \`30c7c5a...\`, ma stan **in_progress**. Nie deklarować sukcesu testu ani PDF przed końcowym odczytem stanu zdalnego i artefaktów.

## Kontrola wizualna

Z potwierdzonego artefaktu 298-stronicowego PDF z poprzedniego stabilnego SHA 556587924... wyrenderowano i bezpośrednio obejrzano wszystkie **6 stron PDF 84–89** obejmujących źródłowy rozdział 43 (w druku rozdział 12). Nie stwierdzono uciętych wzorów ani kolizji oznaczeń czy rysunków; rysunek granicy przekroju cyklu \`C₈\` jest poprawnie rozmieszczony. Od SHA starego artefaktu do dodania nowego testu nie wprowadzono zmian w źródle 43. Kontrola składu nowego SHA wymaga jeszcze końcowej bramki CI.

## Osobno oznaczona propozycja, bez zmian w zatwierdzonym źródle

**Opcjonalnie**, po zakończeniu globalnego audytu, można zdefiniować rodziny ekspanderów o zmiennym stopniu \`1≤d_j≤D\`, zamiast wymagać jednego wspólnego \`d\`. Aktualna definicja jest matematycznie spójna i celowo restrykcyjna; szersze ujęcie daje bardziej standardową klasę rodzin o stopniach jednostajnie ograniczonych. Rozszerzenie zakresu wymaga zgody użytkownika zgodnie z AGENTS.md.

## Werdykt tymczasowy

**Audyt 32: pierwsze przejście merytoryczne i wizualne wykonane; regresje i pełny PDF na nowym SHA w stabilizacji.** Nie uznawać rozdziału 43 za zamknięty bez potwierdzonego wyniku CI, źródeł testu i PDF, a następnie niezależnego drugiego przejścia.


## Potwierdzony wynik zdalnego testu strukturalnego

Przebieg https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45289361352 dla dokładnego SHA \`30c7c5a99e5fb047e7744b3d0cdbe31a93c8fb9a\`:

- job \`structural-audit\`, ID \`138093867113\`: **completed / success**; lista kroków potwierdza sukces \`First independent Cheeger, diameter and lazy mixing audit (43)\`;
- przejrzano rzeczywisty log tego jobu: \`PASS chapter 43: 193 exhaustive positive-regular graphs; 165 connected mixing/diameter checks\`; \`PASS chapter 43: complete graphs, cycles, bipartite laziness and TeX hypotheses\`; \`PASS chapter 43 first independent audit (...)\`;
- job \`full-book-pdf\`, ID \`138093867521\`: na chwilę tego odczytu wciąż **in_progress**, z aktywną instalacją TeX. Nie można jeszcze poświadczyć nowej kompilacji.

Źródło rozdziału 43 nie było zmieniane podczas tworzenia testów; sześć stron 84–89 obejrzano w rzeczywistym PDF z poprzedniego pomyślnego przebiegu, który zawiera tę samą wersję źródła. **Pierwsze przejście 43 nadal otwarte do końcowego potwierdzenia PDF/CI**.
