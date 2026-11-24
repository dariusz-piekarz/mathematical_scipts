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

## Pierwsze wykonanie — 2026-11-24
Przejrzano kryteria 001–012 w poprawionym tekście (commit 6c55830d79679c70a164546a1f0ff953198e29f6). Kontrola strukturalna wykonana na treści przed zapisem: zachowano 35 etykiet, wszystkie 14 odsyłaczy wewnętrznych rozwiązywalne, środowiska begin/end poprawnie zagnieżdżone. Nie wykonano kompilacji LaTeX, renderowania rysunków ani Lean. Rozdział pozostaje otwarty; dalsze sekcje od sec:pde-models wymagają osobnego audytu.
