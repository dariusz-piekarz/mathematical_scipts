# AA-54 — audyt II: gradacja, sprzężenie i dokładna relacja dwudziestościenna

Data: 24 listopada 2026 r. Gałąź biblioteka-matematyczna-iteracja-6.
Commit źródłowy 9ad6e1d2c2134bd985118fb8df5625ceeeec8201, blob a6942da66e2e9c7d6b60e38e54fac589022c0536.

## Korekty matematyczno-redakcyjne
Dopisano jawny izomorfizm algebr niezmienników dla sprzężonych podgrup i jego odwrotność. Uzupełniono rachunek licznika E w sumie Moliena oraz tożsamości dla złotej liczby. W kryterium prezentacji kwadratowej udowodniono jednorodność relacji względem wag p,q,r, korzystając z niezależności algebraicznej a,b. Rozpisano wartości pochodnych f,g w (1,0). W części dwudziestościennej jawnie określono phi i rozróżniono operator J od wielomianu K=J(F,H). Dodano wzory na współczynniki hesjanu: 264 a0 a2 i 1584 a0 a4 - 220 a2², oraz rachunek współczynnika K. Poprawiono końcową terminologię rezolucji osobliwości. Nie znaleziono fałszywych twierdzeń ani konieczności zmiany zakresu.

## Faktycznie wykonane obliczenia
W kontenerze uruchomiono Python/SymPy w dokładnych ciałach algebraicznych. Dla podstawienia generatora dwudziestościennego rozwinięto 13 współczynników wielomianu 2^12 F(X,Y) nad QQ(i,sqrt(5)); wszystkie 13 zgodne. Pierwsze wywołanie Poly.diff(x,2) w następnym teście było niepoprawne (PolynomialError), po czym wykonano poprawne różniczkowanie przez kolejne wywołania .diff(x).diff(x). Niezależny drugi proces zakończył się kodem 0: stopnie 12,20,30, relacja K²+129534197760 F⁵+(400/121)H³=0 jako dokładna tożsamość wielomianowa nad QQ(sqrt(5)). Odczytano współczynniki -5808 sqrt(5), -367840, -13939200 sqrt(5) i potwierdzono dodatkowo J(f,g)=-8t jako tożsamość wielomianową. Wszystkie poprawione obliczenia przeszły. Nie traktujemy testów jako zamiennika dowodów.

## CI i struktura
Ponownie odczytano aktualny blob: 455 wierszy, 10 etykiet, zrównoważone środowiska. Pierwotny CI 45350379719: w toku, 29 kroków success; nowy CI 45350623875 dla commita po korektach w toku. Nie wykonano oględzin aktualnego PDF. Żadnych zmian innych rozdziałów.

## Werdykt
AA-54 W AUDYCIE, licznik czystych niezależnych audytów po korekcie 0/2. Następnie niezależna kontrola śladów, relacji i wymiarów oraz CI. AA-55 nieotwarty.
