# Algebra liniowa — rozdział 24, audyt I

**Data:** 21 listopada 2026  
**Źródło:** `chapters/pl/linear_algebra/24-rownania-riccatiego-i-sterowanie-liniowo-kwadratowe.tex`.  
**Stan wcześniejszy:** rozdziały 01–23 stabilne, ostatni CI LA-23 **SUCCESS**.

## Zakres i pierwszy przegląd

1. Uzupełnianie kwadratu dla hermitowskiej macierzy dodatnio określonej `R`.
2. Zasada optymalności na skończonym horyzoncie w czasie dyskretnym: rekurencja `P_{N+1}=Q+A*P_NA-A*P_NB(R+B*P_NB)^{-1}B*P_NA` i jednoznaczność pierwszego kroku optymalnego sterowania.
3. Monotoniczność rekurencji `P_N` przez porównanie minimalnych kosztów, ograniczenie z góry przez koszt zerowego sterowania, gdy `A` jest macierzą Schura.
4. Istnienie stabilizującego DARE przez monotoniczną zbieżność macierzy, dodatnią określoność `P>=Q`, tożsamość zamkniętej pętli i dyskretne twierdzenie Lapunowa. W pierwszym przeglądzie wykryto, że kryterium stabilizującego rozwiązania nie powinno nakładać dodatniej określoności na `M=R+B*PB` dla dowolnego drugiego rozwiązania. Dowód jednoznaczności **poprawiono**, stosując dokładną tożsamość `D=A_1*D A_2` i zanik potęg obu zamkniętych macierzy.
5. Optymalność nieskończonego horyzontu w dyskretnym problemie LQR: suma teleskopowa i ścisła dodatnia określoność `M`.
6. Czas ciągły: całkowa tożsamość dopełnienia kwadratu, równanie `S'=A*S+SA-SBR^{-1}B*S+Q` z `S(0)=0`, globalne istnienie przez ograniczenie kosztu zerowego sterowania.
7. Przejście `S(t)->P` przy stabilnym `A`: monotoniczność kosztów, górne ograniczenie z ciągłego twierdzenia Lapunowa, przejście do granicy w ODE. Dowód dodatniej określoności korzysta z osiągnięcia minimum i dodatniego kosztu na dodatnim horyzoncie.
8. Stabilność rozwiązania CARE: zamknięte równanie Lapunowa `A_cl*P+PA_cl=-(Q+K*RK)`. Wykazano jednoznaczność stabilizującego rozwiązania bez wstępnego założenia dodatniej określoności drugiego rozwiązania.
9. Ciągły problem nieskończonego horyzontu: dla każdego sterowania o skończonym koszcie `x,u,x' in L2`, skąd `x(t)->0`; wynik umożliwia przejście do granicy w tożsamości kosztu.
10. Przykłady: dokładne rozwiązania skalarne CARE/DARE z niestabilizującymi drugimi pierwiastkami i dwuwymiarowe przykłady ciągłe i dyskretne.

## Kryteria zamknięcia

- Uruchomić `tools/test_linear_algebra_riccati.py` oraz wcześniejsze regresje, sprawdzić równania na macierzach wymiernych.
- Kontrola etykiet, odsyłaczy, terminologii, wszystkich pełnych dowodów i przypadków krańcowych.
- Zbudować książkę bez ostrzeżeń i wyeksportować samodzielny PDF rozdziału 24.
- Po ostatniej korekcie przeprowadzić co najmniej dwa kolejne czyste audyty.

**Status: audyt I wykrył jedną istotną lukę dotyczącą warunku `M>0` w porównaniu stabilizujących rozwiązań. Naprawiona; rozdział nadal w audycie.**
