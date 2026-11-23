# AA-50 — trzeci przypadek Kovacica i skończone grupy Galois

**Data:** 23 listopada 2026 r.
**Poprzedni etap:** AA-49 STABILNY.
**Status:** STABILNY w opisanym zakresie — raport III: audits/abstract_algebra/ch50_iteration_03.md, końcowy CI #45184219678.
**Źródło:** chapters/pl/abstract_algebra/50-trzeci-przypadek-kovacica-i-skonczone-grupy-galois.tex.

## Zatwierdzony zakres bieżącej iteracji

1. Przypadek trzeci klasycznego algorytmu Kovacica dla z''=qz nad K=C(x): skończone prymitywne grupy Galois i projektywne grupy A4, S4, A5, z parametrami n=4,6,12. Klasyfikacja grup jest **wynikiem klasycznym, jawnie cytowanym**.
2. Konieczne warunki lokalne dla q: skończone bieguny rzędu 1 i 2 oraz ord∞ q≥2. Dokładne skończone zbiory E_c(n), E_∞(n), stopień d=(n/12)(e∞−Σe_c) i θ=(n/12)Σ e_c/(x−c) są **cytowanymi wynikami algorytmu Kovacica**; pełny dowód ich wyczerpującego charakteru nie jest częścią AA-50.
3. Samodzielny dowód rekurencji: S=∏_{c∈Γ}(x−c), P_{n+1}=0, P_n=−P, P_{i−1}=−S P_i'+((n−i)S'−Sθ)P_i−(n−i)(i+1)S²qP_{i+1}, warunek P_{−1}=0. Dla F=Σ S^iP_i T^i/(n−i)! zachodzi (∂_x+(q−T²)∂_T)F=(-nT+nS'/S−θ)F.
4. Samodzielny dowód, że każdy pierwiastek nierozkładalnego czynnika F jest algebraicznym rozwiązaniem Riccatiego, nawet gdy F ma czynniki z krotnością. Wykorzystać separowalność w charakterystyce 0, nie zakładać bez dowodu że F jest bezkwadratowy.
5. Enumeracja końcowa na każdy n∈{4,6,12}: całkowity stopień d≥0, liniowe równania w współczynnikach monicznego P, rozwiązanie algebraicznego F i całkowanie z' = wz. Kompletność **warunkowo od cytowanego wyniku klasycznego**, poprawność każdego wyniku dodatniego samodzielnie udowodniona.
6. Konkretny dodatni przykład typu czworościennego: q=−3/(16x²)−2/(9(x−1)²)+3/(16x(x−1)); n=4, e0=3, e1=4, e∞=7, d=0, P=1, θ=1/x+4/(3(x−1)), P_{−1}=0 z jawnymi wszystkimi P_i. Dodatkowo negatywne testy przy nieskończoności, dokładna kontrola całkowitości i zdegenerowany wcześniejszy przypadek wymierny q=2/x².
7. Dwa niezależne zestawy regresji (SymPy i Fraction), audyty I–III, pełny GitHub Actions oraz oględziny każdej nowej strony PDF przed werdyktem STABILNY.

## Granice

Samodzielne dowody rekurencji i odzyskiwania pierwiastków nie są niezależnym dowodem wyczerpującej klasyfikacji lokalnej, algebry niezmienników A4/S4/A5 ani pełnego twierdzenia Picarda–Vessiota. Nie przypisujemy typu grupy Galois wyłącznie faktowi, że rekurencja n=4 znalazła rozwiązanie: może on wystąpić również w wcześniejszych gałęziach. Model efektywny musi obsługiwać rozkład wielomianów i testy równości; nie twierdzimy, że ogólna implementacja CAS jest w tym zakresie kompletna.

**AA-51 nieotwarty.**


## Zamknięcie

Audyty I–III, 13/13 symbolicznych i 12/12 niezależnych testów wymiernych PASS; CI 92/92 SUCCESS na commicie 4103a830163f9abcebca492d26e58f33e9784f82. PDF 322 strony, AA-50 strony 317–322 obejrzane; log bez błędów i ostrzeżeń. Klasyczna kompletność lokalna i grupy A4, S4, A5 pozostają jawnie cytowanymi twierdzeniami. AA-51 nieotwarty.
