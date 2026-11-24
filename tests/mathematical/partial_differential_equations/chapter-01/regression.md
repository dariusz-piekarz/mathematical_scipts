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

## Pierwsze wykonanie — 2026-11-24
Przejrzano kryteria 001–012 w poprawionym tekście (commit 6c55830d79679c70a164546a1f0ff953198e29f6). Kontrola strukturalna wykonana na treści przed zapisem: zachowano 35 etykiet, wszystkie 14 odsyłaczy wewnętrznych rozwiązywalne, środowiska begin/end poprawnie zagnieżdżone. Nie wykonano kompilacji LaTeX, renderowania rysunków ani Lean. Rozdział pozostaje otwarty; dalsze sekcje od sec:pde-models wymagają osobnego audytu.

## Druga iteracja — 2026-11-24
Przegląd semantyczny kryteriów 013–026 w ramach poprawek (commit 9eb95ea38bff8f46eab3e0ceaccc3e2a2606ff55). Kontrola strukturalna wykonana: 35 etykiet zachowanych, 15 odsyłaczy wewnętrznych rozwiązywalnych, środowiska poprawnie zagnieżdżone. Nie wykonano kompilacji ani renderowania; Lean nie uruchomiono. Otwarte: kontrola energetyczna równania ciepła, przykłady Hadamarda, skalowanie, niezależna kontrola całości oraz rysunki i kompilacja.
