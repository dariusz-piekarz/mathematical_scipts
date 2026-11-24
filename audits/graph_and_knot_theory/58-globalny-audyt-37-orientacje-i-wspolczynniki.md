# Globalny audyt 37 — orientacje i współczynniki

2026-11-24. Baza 10cdc2b2bad594f69f6b1f6543373c9ca8889a8d. Przegląd rozdziałów 06, 07, 11, 13–16 (w 14 sprawdzono definicję przestrzeni Reeba, pas regularny i krytyczny; w 15 dowód eliminacji i wcześniejszy test GF(2)).

- 06: zmiana orientacji nie zachowuje dosłownie jądra w stałych współrzędnych. Dla diagonalnej macierzy znaków D nowa macierz BD ma jądro D ker B; rząd i abstrakcyjna grupa cykli są zachowane.
- 07: doprecyzowano otwarte pokrycie bukietu w dowodzie van Kampena, kontrakcję lokalnie skończonego nieskończonego drzewa oraz odwołanie do wcześniejszego twierdzenia.
- 11: pętle mają kolumnę zerową; krawędzie równoległe osobne kolumny; ściany orientujemy zgodnie z powierzchnią. Jawna zmiana współczynników na R przed obliczaniem wymiarów.
- 13: wymiar pustego kompleksu, właściwy warunek czystości dwuwymiarowej, spójność w twierdzeniu o grafie dualnym. Dowód kryterium ogniwa odróżnia ogniwo krawędzi od pełnego lokalnego ogniwa punktu; lokalna H2 ma rangę k-1 dla k półdysków. Definicja łańcuchów nad pierścieniem i Euler–Poincaré nad dowolnym ciałem (potrzebne w 15).
- 15: w dowodzie charakteryzacji Hassego należy odwrócić kierunek cyklu, aby uzyskać V-ścieżkę. Dodano całkowitoliczbową redukcję: pivoty ±1 są jednostkami i zachowują się w eliminacji trójkątnej. Przykład RP2 pokazuje torsję i różnice między współczynnikami.
- 16: różniczka na kołańcuchach jako złożenie funkcjonału z brzegiem, transpozycja tylko w odpowiednich bazach. Terminologia drugiego aksjomatu przeliczalności.

Dodano test niezależnej eliminacji na podpisanych macierzach całkowitych, kontrolę d²=0 po każdej eliminacji i porównanie liczb Bettiego modulo 2,3,5. Sfera, torus i 6-wierzchołkowa triangulacja RP2 z redukcją do pojedynczych generatorów i współczynnikiem ±2 w ostatnim przypadku. Test dołączono do workflow globalnego. CI, kompilacja i oględziny jeszcze niepotwierdzone. Audyt 37 otwarty.
