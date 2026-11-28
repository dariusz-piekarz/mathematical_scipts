# AA-52 — audyt VIII: stabilizacja matematyczna po korekcie VII

Data: 24 listopada 2026 r. Gałąź: biblioteka-matematyczna-iteracja-6.
Źródło: blob de35380cb5208b32ebb1bbac165dd554d44228d9, commit 7f69140bb0f7c97f4ab46da89718269d3bcf9d31.

## Niezależna kontrola dowodów
- Unitarność: A jest dodatnio określona, a g*Ag=A; P=A^(1/2) jest hermitowska i odwracalna, więc rachunek dodany w VII daje macierz unitarną. Normalizacja przez dodatni skalar nie zmienia sprzężenia i daje wyznacznik 1.
- Równoważność rzeczywista: wielomian det(X+tY) nie jest zerowy, bo dla t=i daje det Z; istnieje rzeczywiste t z odwracalnym L. D=L^T L komutuje z r1(k) dzięki ortogonalności obu reprezentacji. Dodatni pierwiastek odwrotny zachowuje tę przemienność przez rozkład na przestrzenie własne. Q0=LD^(-1/2) jest ortogonalna i przeplata reprezentacje; zastąpienie przez -Q0 w wymiarze 3 daje w razie potrzeby wyznacznik 1. Oba uzupełnienia VII są poprawne.
- Grupy dwucykliczne: w postaci normalnej (k,e) iloczyn ma współrzędne (k+(-1)^e l+n e f mod 2n, e+f mod 2). Po redukcji pierwszej współrzędnej modulo n otrzymujemy iloraz dwuścienny; jego jądro ma dwa elementy. Każdy element poza podgrupą diagonalną ma kwadrat (n,0), więc rząd 4. Jedyna inwolucja to (n,0), co potwierdza nierozszczepialność.
- Półniezmienniki: działanie na wielomianach jest przez podstawienie h^(-1), więc znaki dla xy są poprawne, a (xy)^2 jest niezmiennikiem. Rozkład jednorodnego wielomianu uwzględnia czynniki odpowiadające punktowi w nieskończoności. Nie znaleziono nowej luki wymagającej korekty.

## Niezależny test lokalny
Uruchomiono Python z dokładną arytmetyką całkowitą dla n=2,...,40: 39 grup. Sprawdzono wszystkie pary elementów w odniesieniu do prawa iloczynu w ilorazie, liczność grupy i ilorazu, tożsamość, jedyność inwolucji oraz rzędy elementów: 2n/gcd(2n,k) dla (k,0), 4 dla (k,1). Bez błędów.
Dodatkowo w stopniach d=0,...,16 (663 przypadki) wyliczono wymiary niezmienników metodą monomów: dla x^a y^(d-a) warunek niezmienniczości względem A to 2a-d=0 mod 2n; J zamienia a z d-a i daje znak (-1)^a. Każda dwuelementowa orbita dopuszczalnych wykładników wnosi wymiar 1 (d parzyste), jednoelementowa wnosi 1 wtedy i tylko wtedy, gdy a parzyste. Pierwszy dodatni stopień niezmiennika wynosi 4 dla wszystkich 39 grup. Test zakończył się kodem 0. Jest to dodatkowa kontrola przykładu, nie rozszerzenie zakresu źródła.

## Techniczna kontrola
629 wierszy, 18 różnych etykiet, 21 wystąpień odsyłaczy; wszystkie środowiska poprawnie zagnieżdżone. Sześć różnych odsyłaczy wychodzi poza rozdział; ich końcową rozwiązywalność potwierdzi kompilacja. Kontrole terminologii (45345253131) i aplikacji (45345253236) zakończone success dla właściwego commita. Walidacja AA (45345253078, job 138278146261) nadal in_progress: 50 success, 1 in_progress, 62 pending. PDF aktualnego bloba nie został jeszcze obejrzany.

## Werdykt
Pierwszy czysty przegląd matematyczno-redakcyjny po VII; źródło bez zmian. AA-52 pozostaje W AUDYCIE do końcowego CI i oględzin PDF, następnie dalsza kontrola stabilizacyjna. AA-53 nieotwarty. Nie zmieniano workflow ani innych rozdziałów.
