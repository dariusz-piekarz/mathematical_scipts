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

## Kontrola PDF i korekta łamania stron

Workflow 45302954204 dla bf731f6d2c7fa043be0fe9c06bd6d28719d0ffc5: oba joby success, pełny PDF 300 stron, 0 ostrzeżeń. Pobrano artefakt 14879169442 oraz wersję poprzednią 14877802452. Porównanie tekstu wszystkich stron z wyrównaniem przesunięcia paginacji wykazało 20 zmienionych stron fizycznych (8, 90–94, 96–99, 124, 131–134, 141, 143–145, 147). Wyrenderowano i obejrzano wszystkie 20. Nie stwierdzono kolizji ani obcięć, lecz strony 94 i 99 zawierały jedynie krótkie zakończenia rozdziałów. Uporządkowano dowód rozkładu Hodge'a (06) i argument metryczny (07); zamiast skrótowego uzasadnienia ciągłości kontrakcji drzewa podano nierówności metryczne, a w dowodzie zgodności metryk zastąpiono niejasną aproksymację krzywych podziałem na fragmenty w małych gwiazdach. Nie zmieniono ustawień kompilacji. Wymagana ponowna kontrola CI i PDF; audyt 37 nadal otwarty.

## Dodatkowa kontrola kontrakcji metrycznej

Dla SHA 5dbaef46b36c70348b56cef6e28962909154ec00 osobny workflow algorytmiczny 45305107343 oraz terminologiczny 45305107329 zakończyły się success. Job structural-audit 138146911209 również success. Pełny PDF 138146911138 nadal w toku (workflow 45305107395); nie deklarujemy zamknięcia składu.

Niezależna kontrola nierówności użytej w rozdziale 07. Niech a=d(r,x), b=d(r,y), c=d(r,z), gdzie z jest końcem wspólnego początkowego odcinka dróg od korzenia do x i y. Dla l=1-t odległość obrazów wynosi dokładnie l(a+b)-2 min(c,la,lb). Ponieważ a,b≥c i 0≤l≤1, minimum jest co najmniej lc. Stąd d(H_t(x),H_t(y))≤l d(x,y). Z kolei d(H_t(x),H_s(x))=|t-s|d(r,x), gdyż oba obrazy leżą na tej samej drodze od korzenia. Te dwie nierówności dają łączną ciągłość homotopii.

W lokalnym Pythonie wykonano niezależny test dokładny Fraction: a,b od 0 do 8, c od 0 do min(a,b), l=j/8 dla j=0,...,8 (2565 konfiguracji), oraz 729 konfiguracji zmiany parametru na pojedynczej drodze. Wszystkie asercje PASS. Jest to kontrola pomocnicza, a nie zamiennik ogólnego dowodu. Nie modyfikowano ponownie źródeł matematycznych.
