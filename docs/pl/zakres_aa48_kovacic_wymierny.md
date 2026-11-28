# AA-48 — zakres i bramka stabilizacji

**Data:** 23 listopada 2026 r.
**Po stabilizacji:** AA-47 — Algorytmy Rischa i Kovacica.
**Zakres przyjęty na podstawie polecenia „kontynuuj”:** pierwsza gałąź algorytmu Kovacica dla q wymiernego, czyli kompletny test rozwiązań wymiernych równania Riccatiego. Status: STABILNY w opisanym zakresie; końcowy raport: audits/abstract_algebra/ch48_iteration_03.md, CI #45172784971.

## Główne rezultaty wymagane

1. Analiza skończonych biegunów q: proste bieguny, bieguny rzędu 2 z równaniem indycjalnym, parzyste bieguny rzędu co najmniej 4 z dwiema rekurencjami, wykluczenie nieparzystych rzędów większych lub równych 3.
2. Oddzielenie części głównych w ustalonych biegunach q od biegunów ruchomych o residuum 1; postać r=omega+R+P'/P z P bez pierwiastków wielokrotnych i bez zer w biegunach q.
3. Nieskończoność: osobne przypadki dodatniego parzystego stopnia części wielomianowej q, niezerowej stałej wartości granicznej, q=O(1/x); wyznaczenie dopuszczalnych stopni P.
4. Równanie P''+2uP'+(u'+u^2-q)P=0 jest liniowe we współczynnikach P; skończona kontrola warunku P(a) !=0 przy wszystkich ustalonych biegunach. Należy uzasadnić możliwość wyboru rozwiązania spoza skończonej sumy właściwych hiperpłaszczyzn.
5. Pełny dowód konieczności i dostateczności testu wymiernego. Nie twierdzić, że to cały algorytm Kovacica; przypadki algebraiczne stopni 2,4,6,12 są odrębne.
6. Przykłady: q=2/x^2, q=x^-4-2x^-3, q=x^2+3+2/(x-1), q=1/x^3, q=x+5/(16x^2), oraz dodatnie i negatywne kontrole przy nieskończoności.
7. Dwie niezależne serie testów, globalna integralność, audyt I, audyt II, rzeczywisty CI, przegląd każdej strony nowego PDF, audyt III zamykający stabilizację.

## Granice i następny rozdział

To pełna procedura dla r w C(x) przy q w C(x), a nie pełny algorytm Kovacica. AA-49 pozostaje nieotwarty do decyzji o zakresie.


## Zamknięcie

Audyty I–III zakończone, 12/12 testów SymPy oraz 9/9 niezależnych Fraction PASS, pełny CI 88/88 SUCCESS, ostateczny 310-stronicowy PDF bez błędów, sześć stron AA-48 obejrzanych. AA-49 nieotwarty.
