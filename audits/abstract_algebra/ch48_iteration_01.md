# AA-48 — audyt I: konstrukcja i weryfikacja założeń

**Data:** 23 listopada 2026 r. **Werdykt: W AUDYCIE — NIE STABILNY.**
**Źródło:** chapters/pl/abstract_algebra/48-wymierna-galaz-kovacica-dla-potencjalow-wymiernych.tex.
**Plan:** docs/pl/zakres_aa48_kovacic_wymierny.md.

## Matematyka — sprawdzenie I

1. Wszystkie skończone bieguny r o rzędzie m>=2 wymuszają biegun q dokładnie rzędu 2m z niezerowym współczynnikiem wiodącym równym kwadratowi. Biegun prosty r daje w q wyraz z^-2 o współczynniku c(c-1). W zwykłym punkcie q biegun r jest prosty i ma residuum 1.
2. Dla q o biegunie prostym w a jedyną możliwą częścią główną r jest 1/(x-a); dla rzędu 2 residua są dwoma pierwiastkami c(c-1)=beta, a dla rzędu 2m>=4 m współczynników części głównej jest wyznaczonych przez dwa możliwe znaki pierwiastka wiodącego i rekurencję trójkątną. Dla q o nieparzystym biegunie rzędu >=3 nie może istnieć r wymierne.
3. Po odjęciu tych części głównych pozostałe bieguny są proste z residuum 1, a więc mogą być zapisane jako P'/P z P unormowanym i bez pierwiastków powtórzonych, względnie pierwszym z mianownikiem q.
4. Dokładna tożsamość Riccatiego jest równoważna liniowemu ODE P''+2uP'+(u'+u^2-q)P=0. Dowód braku wielokrotnych zer P wymaga regularności **obu funkcji u i q** w rozpatrywanym punkcie; hipotezę uzupełniono w źródle.
5. Rozwinięcia przy nieskończoności dzielą przypadki na (a) część wielomianowa dodatniego stopnia 2d i 2 znaki wielomianu omega, (b) niezerowa granica q i 2 znaki stałego omega, (c) q→0, wówczas q=O(x^-2) oraz kwadratowy test dla n=deg P. Każda gałąź daje co najwyżej 2 wartości n.
6. Dla każdej pary (omega,n) trzeba wybrać P w afinicznym zbiorze rozwiązań układu liniowego i wykluczyć wspólne zera z mianownikiem q. Warunek P(a) !=0 dla skończenie wielu a nie może zostać pominięty. Poprawność testu uzasadnia fakt, że skończona suma właściwych hiperpłaszczyzn nie pokrywa przestrzeni afinicznej nad C.
7. Skończoność wynika z kombinacji dwóch opcji na każdym biegunie, co najwyżej dwóch opcji w nieskończoności, i skończonych układów liniowych. Konieczność wynika z rozkładu każdego wymiernego r, dostateczność z bezpośredniego rachunku r'+r²=q.
8. Nie utożsamiać odmowy pierwszej gałęzi algorytmu Kovacica z nieistnieniem wszystkich rozwiązań liouvillowskich. Kontrprzykład q=x+5/(16x²), r=sqrt(x)-1/(4x) pokazuje ograniczenie.

## Testy i dokumentacja

Utworzono 11 symbolicznych testów SymPy i 9 niezależnych testów lokalnej arytmetyki Laurenta na fractions.Fraction. Testy obejmują wysokie bieguny, równanie stopnia n, P dzielące mianownik q jako niedopuszczalny przypadek gałęzi oraz szczególny potencjał q=0.

Zamknięcie wymaga rzeczywistego pełnego CI, kontroli etykiet i odsyłaczy, logu latexmk oraz oględzin każdej nowej strony PDF. Do tego czasu stan NIE STABILNY. AA-49 nieotwarty.
