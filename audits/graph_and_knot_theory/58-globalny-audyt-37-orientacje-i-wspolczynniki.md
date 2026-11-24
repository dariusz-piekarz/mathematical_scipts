# Globalny audyt 37 — orientacje i współczynniki

2026-11-24. Baza 10cdc2b2bad594f69f6b1f6543373c9ca8889a8d. Przegląd rozdziałów 06, 07, 11, 13–16 (w 14 sprawdzono definicję przestrzeni Reeba, pas regularny i krytyczny; w 15 dowód eliminacji i wcześniejszy test GF(2)).

- 06: zmiana orientacji nie zachowuje dosłownie jądra w stałych współrzędnych. Dla diagonalnej macierzy znaków D nowa macierz BD ma jądro D ker B; rząd i abstrakcyjna grupa cykli są zachowane.
- 07: doprecyzowano otwarte pokrycie bukietu w dowodzie van Kampena, kontrakcję lokalnie skończonego nieskończonego drzewa oraz odwołanie do wcześniejszego twierdzenia.
- 11: pętle mają kolumnę zerową; krawędzie równoległe osobne kolumny; ściany orientujemy zgodnie z powierzchnią. Jawna zmiana współczynników na R przed obliczaniem wymiarów.
- 13: wymiar pustego kompleksu, właściwy warunek czystości dwuwymiarowej, spójność w twierdzeniu o grafie dualnym. Dowód kryterium ogniwa odróżnia ogniwo krawędzi od pełnego lokalnego ogniwa punktu; lokalna H2 ma rangę k-1 dla k półdysków. Definicja łańcuchów nad pierścieniem i Euler–Poincaré nad dowolnym ciałem (potrzebne w 15).
- 15: w dowodzie charakteryzacji Hassego należy odwrócić kierunek cyklu, aby uzyskać V-ścieżkę. Dodano całkowitoliczbową redukcję: pivoty ±1 są jednostkami i zachowują się w eliminacji trójkątnej. Przykład RP2 pokazuje torsję i różnice między współczynnikami.
- 16: różniczka na kołańcuchach jako złożenie funkcjonału z brzegiem, transpozycja tylko w odpowiednich bazach. Terminologia drugiego aksjomatu przeliczalności.

Dodano test niezależnej eliminacji na podpisanych macierzach całkowitych, kontrolę d²=0 po każdej eliminacji i porównanie liczb Bettiego modulo 2,3,5. Sfera, torus i 6-wierzchołkowa triangulacja RP2 z redukcją do pojedynczych generatorów i współczynnikiem ±2 w ostatnim przypadku. Test dołączono do workflow globalnego. CI, kompilacja i oględziny jeszcze niepotwierdzone. Audyt 37 otwarty.

## Stabilizacja — kontrola matematyczna

Dla SHA bf731f6d2c7fa043be0fe9c06bd6d28719d0ffc5 przebieg globalny 45302954204: structural-audit 138139744133 zakończony success. Rzeczywisty log: PASS: 56 signed small matchings; integral sphere, torus, RP2 pivot 2; GF(2), GF(3), GF(5). Wcześniejsze testy także success, unresolved_references=0, manual_chapter_numbers=0. Workflow algorytmiczny 45302954148, aplikacja 45302954119 i terminologia 45302954449 zakończone success. Porównanie bieżącej gałęzi z tym SHA nie wykazało innych zmian grafowych.

### Niezależna kontrola argumentów

- Orientacja: dla trójkąta z orientacją cykliczną ker B jest rozpięte przez (1,1,1). Po odwróceniu pierwszej krawędzi ker(BD) jest rozpięte przez (-1,1,1). To jawny przykład, że niezmienność dotyczy grupy cykli po identyfikacji baz, a nie podzbioru ustalonej przestrzeni współrzędnych.
- Lokalna homologia: dla k półdysków pełne ogniwo punktu we wnętrzu krawędzi ma dwa wierzchołki i k krawędzi, stąd H_1 ogniwa ma rangę k-1, a H_2 pary lokalnej tę samą rangę. Dla k=1,2,3 otrzymujemy odpowiednio 0, Z, Z². Warunek czystości zapewnia k≥1.
- Torsja: dla zredukowanego kompleksu płaszczyzny rzutowej z jedną komórką w każdym z wymiarów 0,1,2 brzeg dwuwymiarowy ±2 daje H_1=Z/2Z. Redukcja modulo 2 zeruje ten brzeg, a modulo 3 i 5 czyni go izomorfizmem. W obu przypadkach suma naprzemienna liczb Bettiego wynosi 1. Testy nad ciałami nie zastępują samego całkowitoliczbowego argumentu o odwracalnych pivotach.

Job full-book-pdf 138139743698 podczas ostatniej kontroli nadal instalował TeX. Nie potwierdzono pełnej kompilacji ani wyglądu zmienionych stron. Audyt 37 otwarty do zakończenia tej bramki.
