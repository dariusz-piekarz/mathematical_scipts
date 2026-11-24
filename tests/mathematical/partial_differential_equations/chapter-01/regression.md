# PDE-01 — trwałe kryteria regresyjne

Źródło: [rozdział 01](../../../../chapters/pl/partial_differential_equations/01-wprowadzenie-do-pde.tex).
Kryteria semantyczne wymagają ponownej oceny po zmianie źródła; nie są automatycznymi testami ani formalizacją Lean.

| ID | Etykieta / sekcja | Kryterium | Metoda |
|---|---|---|---|
| PDE-01-001 | sec:pde-unknown | Równanie Burgersa w podanej postaci ma jedną zmienną przestrzenną. | semantyczna |
| PDE-01-002 | sec:pde-unknown | Odróżnienie równania, zagadnienia i rozwiązania. | semantyczna |
| PDE-01-003 | sec:pde-unknown | C^{1,2} obejmuje ciągłość funkcji i wszystkich wymaganych pochodnych przestrzennych do rzędu 2 i czasowej do rzędu 1, bez wymogu pochodnych mieszanych. | semantyczna |
| PDE-01-004 | sec:pde-types | Superpozycja; obie inkluzje opisu zbioru rozwiązań jako przesunięcia jądra. | semantyczna |
| PDE-01-005 | eq:principal-symbol | Dla D=-i∂ symbol tego samego operatora to i^m p_m; znak dla -Δ zmienia się z -abs(ξ)^2 na +abs(ξ)^2. | semantyczna |
| PDE-01-006 | sec:pde-symbol | Test wysokich częstości jawnie dopuszcza funkcje zespolone i określa operator oraz konwencję. | semantyczna |
| PDE-01-007 | sec:pde-symbol | Funkcja definiująca hiperpowierzchnię jest lokalna i ma niezerową różniczkę. | semantyczna |
| PDE-01-008 | sec:pde-symbol | Wspólne jądro różniczek jest przestrzenią styczną; proporcjonalność z niezerowym czynnikiem i jednorodność symbolu. | semantyczna |
| PDE-01-009 | sec:pde-symbol | Charakterystyczność dotyczy kowektorów; symbol paraboliczny iτ+κabs(ξ)^2 odróżniony od zwykłego symbolu rzędu 2. | semantyczna |
| PDE-01-010 | sec:pde-classification | Macierz zerowa jest poza klasyfikacją; rząd 1, określoność i znaki wartości własnych rozróżnione. | semantyczna |
| PDE-01-011 | sec:pde-classification | Współczynniki A,B,C jawnie określone w stwierdzeniu. | semantyczna |
| PDE-01-012 | sec:pde-classification | J_{ki}=∂_i Φ_k, część główna J A J^T, pochodne drugie Φ tylko w części niższego rzędu; prawo bezwładności. | semantyczna |
| PDE-01-013 | thm:laplace-max | Jawne jednostajne ograniczenie eps*max abs(x)^2 i przejście do granicy. | semantyczna |
| PDE-01-014 | cor:dirichlet-stability | Funkcje rzeczywiste w dowodzie przez zasadę maksimum. | semantyczna |
| PDE-01-015 | cor:dirichlet-stability | Oba oszacowania w i -w oraz jednoznaczność przy zerowych danych różnicowych. | semantyczna |
| PDE-01-016 | eq:neumann-compatibility | Znak warunku zgodności dla -Δu=f i normalnej zewnętrznej. | semantyczna |
| PDE-01-017 | eq:neumann-compatibility | Tożsamość Greena z pola w∇w oraz warunków brzegowych. | semantyczna |
| PDE-01-018 | eq:neumann-compatibility | Zerowa całka gradientu, lokalna stałość i spójność obszaru. | semantyczna |
| PDE-01-019 | ex:burgers-blowup | Równanie charakterystyki z reguły łańcuchowej. | semantyczna |
| PDE-01-020 | ex:burgers-blowup | Ścisła monotoniczność, surjektywność, gładka odwrotność zależna od t,x i weryfikacja PDE oraz danych. | semantyczna |
| PDE-01-021 | prop:heat-kernel | Obliczenie pochodnych jądra i całkowalna majoranta dla różniczkowania. | semantyczna |
| PDE-01-022 | prop:heat-kernel | Ogon gaussowski po skalowaniu i jednostajna zbieżność na całej przestrzeni. | semantyczna |
| PDE-01-023 | thm:dalembert | Obraz t≥0 to ξ≥η, rozkład F+G uzasadniony na półpłaszczyźnie. | semantyczna |
| PDE-01-024 | thm:dalembert | Konstrukcja C², weryfikacja PDE i obu danych początkowych. | semantyczna |
| PDE-01-025 | prop:pde-v31-wave-cone | Zerowe dane implikują zerowy gradient początkowy i energię. | semantyczna |
| PDE-01-026 | prop:pde-v31-wave-cone | Odcinek pionowy zawarty w zwężającym się przedziale; ciągłość na brzegu. | semantyczna |
| PDE-01-027 | prop:heat-uniqueness | Jawne założenie d≥1 i rzeczywistości funkcji w energii kwadratowej. | semantyczna |
| PDE-01-028 | prop:heat-uniqueness | Ograniczona majoranta, zastosowanie Gaussa, zanik wyrazu brzegowego, zerowa energia i wniosek punktowy także na brzegu. | semantyczna |
| PDE-01-029 | prop:pde-v31-wave-cone | Rzeczywistość u i a,b oraz niepusty przedział na całym zakresie czasu. | semantyczna |
| PDE-01-030 | prop:pde-v31-wave-cone | Lokalna tożsamość energii wynika z równania i równości pochodnych mieszanych. | semantyczna |
| PDE-01-031 | eq:pde-v31-wave-cone | Znaki strumienia na obu końcach i poprawne dopełnienie kwadratów. | semantyczna + test skończony |
| PDE-01-032 | ex:laplace-illposed | Harmoniczność i obie dane Cauchy'ego sprawdzone przez różniczkowanie. | semantyczna |
| PDE-01-033 | ex:laplace-illposed | Zbieżność wszystkich ustalonych półnorm C^r. | semantyczna |
| PDE-01-034 | ex:laplace-illposed | Jawna klasa danych i rozwiązań, ciągłość przekroju, jednoznaczność jako założenie argumentu nie wniosek; poprawna asymptotyka normy i normalny kowektor. | semantyczna + test skończony |
| PDE-01-035 | ex:backward-heat | Periodyczność, równanie, półnormy, miara o masie 2π oraz warunki argumentu Hadamarda. | semantyczna + test skończony |
| PDE-01-036 | sec:pde-scaling | Jawne dodatnie parametry i wspólna otwarta dziedzina Q. | semantyczna |
| PDE-01-037 | sec:pde-scaling | Przeciwobrazy otwarte, zachowanie regularności, jawne czynniki λ² w obu równaniach. | semantyczna |
| PDE-01-038 | sec:pde-scaling | Skale czasu wynikają z bezwymiarowych współczynników κτ/ℓ² i c²τ²/ℓ². | semantyczna |

## Pierwsze wykonanie — 2026-11-24
Przejrzano kryteria 001–012 w poprawionym tekście (commit 6c55830d79679c70a164546a1f0ff953198e29f6). Kontrola strukturalna wykonana na treści przed zapisem: zachowano 35 etykiet, wszystkie 14 odsyłaczy wewnętrznych rozwiązywalne, środowiska begin/end poprawnie zagnieżdżone. Nie wykonano kompilacji LaTeX, renderowania rysunków ani Lean. Rozdział pozostaje otwarty; dalsze sekcje od sec:pde-models wymagają osobnego audytu.

## Druga iteracja — 2026-11-24
Przegląd semantyczny kryteriów 013–026 w ramach poprawek (commit 9eb95ea38bff8f46eab3e0ceaccc3e2a2606ff55). Kontrola strukturalna wykonana: 35 etykiet zachowanych, 15 odsyłaczy wewnętrznych rozwiązywalnych, środowiska poprawnie zagnieżdżone. Nie wykonano kompilacji ani renderowania; Lean nie uruchomiono. Otwarte: kontrola energetyczna równania ciepła, przykłady Hadamarda, skalowanie, niezależna kontrola całości oraz rysunki i kompilacja.

## Trzecia iteracja — 2026-11-24
Poprawki 027–038: commit 47eb7d7fd982665bb242cf58fd4a4319e342882d. Przegląd semantyczny zmienionych fragmentów wykonany; kontrola strukturalna: 35 niezmienionych unikalnych etykiet, 15 rozwiązywalnych odsyłaczy, zgodne zagnieżdżenie środowisk. Wykonano skończoną kontrolę rachunkową: 45 kombinacji całkowitych (c,p,q) dla obu tożsamości strumienia, 5 trybów k dla stosunku normy do asymptotyki i dyskretnej kontroli całki sin² na torusie. Wyniki pozytywne; nie zastępują dowodów. Pierwszy przebieg treści ukończony, niezależny audyt całości, kompilacja i renderowanie pozostają otwarte. Lean nie uruchomiono.

Testy wykonywalne: [test_energy_hadamard.py](test_energy_hadamard.py), commit 3dc7d65094e81c280c3b3aa3d81c7963dbde3377. Uruchomiono lokalnie kopię o identycznym SHA blob 1d8609e78e4887cde7164a5a65d65d9d7db6cdd2: 3/3 testy unittest zaliczone. Polecenie: `python tests/mathematical/partial_differential_equations/chapter-01/test_energy_hadamard.py -v`.
