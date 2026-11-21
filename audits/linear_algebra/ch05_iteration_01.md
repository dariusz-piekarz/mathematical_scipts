# Algebra liniowa — rozdział 05, audyt 1 (kontrola wprowadzanej treści)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Plik:** `chapters/pl/linear_algebra/05-eliminacja-gaussa-i-uklady-liniowe.tex`

## Zakres nowego rozdziału

Rozdział rozwija materiał rozdziału 04: odwracalne elementarne operacje na wierszach, konstrukcję postaci schodkowej i zredukowanej, liczbę pivotów, wymiar jądra, kryterium zgodności układów, bazy jądra i obrazu, jednoznaczność postaci zredukowanej i metodę Gaussa--Jordana znajdowania odwrotności. Dla każdego kroku algorytmu podano uzasadnienie i ograniczenie do niezerowych elementów wiodących; zachowano przypadki zerowych wymiarów. Obliczone przykłady wykorzystują tę samą macierz prostokątną oraz odwracalną macierz (2\\times2) z poprzedniego rozdziału.

## Weryfikacja wstępna

Sprawdzono zgodność rachunków w przykładzie `3\\times4`: postać zredukowana ma pivoty (1,3), bazę jądra `(-2,1,0,0)`, `(1,0,-1,1)`, a zgodny układ z prawą stroną `(3,7,4)` ma rozwiązanie `(2,0,1,0)+s(-2,1,0,0)+t(1,0,-1,1)`; zmiana ostatniej współrzędnej prawej strony z 4 na 5 daje sprzeczność. Rachunek odwrotności macierzy `[[2,1],[1,1]]` kończy się blokiem `[[1,-1],[-1,2]]`. Szczególnie sprawdzono, że bazę obrazu wybiera się z oryginalnej macierzy, nie z jej zredukowanej postaci.

## Status

Rozdział 05 pozostaje **otwarty** i wymaga kolejnego pełnego audytu, nawet przy poprawnym CI. Wyniki nowego przebiegu GitHub Actions należy zweryfikować osobno po publikacji. Nie należy deklarować zakończenia audytów 05, dopóki nie nastąpi czysta iteracja stabilizacyjna.
