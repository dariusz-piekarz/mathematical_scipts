# Algebra liniowa — rozdział 25, audyt I

**Data:** 21 listopada 2026  
**Źródło:** chapters/pl/linear_algebra/25-sterowalnosc-obserwowalnosc-i-stabilizowalnosc.tex  
**Blob:** `27572fc264e838d7c81e11a5d5f32dfa261ca643`

## Zakres wstępnej kontroli

1. Kalman: przestrzeń osiągalna jest minimalną podprzestrzenią A-niezmienniczą zawierającą obraz B; argument z Cayleya–Hamiltona objaśnia, dlaczego wystarcza n potęg A. Dokładnie wyprowadzono wzór na x_N oraz kryterium osiągalności w dokładnie n krokach.
2. Czas ciągły: metoda wariacji stałych, gramian W_T, dowód ker W_T=ker K* i jawne sterowanie prowadzące do celu w każdym T>0. Uwzględniono każdy stan początkowy.
3. Obserwowalność: przestrzeń N=ker O jest największą niezmienniczą podprzestrzenią zawartą w ker C, równość rang pod sprzężeniem i warunek iniektywności obserwacji ciągłej.
4. PBH: ranga [λI-A, B] jest pełna dla wszystkich λ dokładnie przy sterowalności. Oba kierunki uzasadniono przez anihilator przestrzeni osiągalnej i jego wektor własny. Osobno udowodniono kryterium obserwowalności.
5. Rozkład Kalmana: kolejność U=R∩N, R/U, N/U i V/(R+N) oraz bloki A, B, C wynikają z niezmienniczości obu podprzestrzeni. Nie założono nieuzasadnionej A-niezmienniczości wybranych dopełnień.
6. Stabilizowalność i wykrywalność: wykazano pełne kryteria PBH dla niestabilnych wartości własnych. Kluczowy lemat o istnieniu sprzężenia sterowalnej pary udowodniono konstrukcyjnie z funkcji wymiernych (bez powoływania się na pełne twierdzenie o rozmieszczaniu dowolnie zadanych biegunów).
7. Energia: W_N^d=K_N K_N*, a najniższa energia ma postać d*(W_N^d)^(-1)d; uzasadniono przez ortogonalny rozkład wszystkich rozwiązań.
8. Przypadek rzeczywisty: skomentowano konieczność uwzględniania wszystkich zespolonych wartości własnych w PBH i realność stabilizujących macierzy sprzężenia.
9. Skład źródłowy: 47 różnych etykiet, 30 odsyłaczy, 17 poprawnie domkniętych środowisk proof; brak terminów zabronionych. Skorygowano wcześniej nieistniejącą etykietę `ch:lin16-invariant` na rzeczywiste `ch:lin16-niezmiennicze` jeszcze przed integracją.

## Kryteria dalsze

- Zielone CI (w tym dokładne testy F2/F3 kryterium PBH, dualności i arytmetyki wymiernej), pełne kompilowanie książki bez ostrzeżeń i samodzielny PDF 25.
- Co najmniej dwa kolejne czyste audyty po ostatniej korekcie.

**Decyzja:** audyt I wykonał kontrolę struktury i korektę etykiety, lecz rozdział 25 pozostaje **w audycie** aż do dowodów, testów i kontroli końcowego PDF.
