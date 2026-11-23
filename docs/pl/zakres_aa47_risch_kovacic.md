# AA-47 — decyzja o zakresie i granice poprawności

**Data:** 23 listopada 2026 r.
**Działanie:** realizacja kolejnego rozdziału po stabilizacji AA-46, po poleceniu użytkownika „kontynuuj”.
**Status:** w przygotowaniu — nie zamykać bez wielokrotnych audytów.

## Jawnie przyjęty zakres

1. Pełny algorytm całkowania wymiernego nad C(x) wraz z dowodem: ułamki proste, redukcja Hermite'a, kryterium residuów, logarytmy, wypadkowa Rothsteina–Tragera i odtwarzanie części logarytmicznej przez NWD.
2. Pełny algorytm decyzyjny dla równania r'+hr=s, gdy h w C[x], s w C(x): lokalne rozwinięcia przy biegunach, jednoznaczne wyliczenie części głównych, przeszkoda residuum oraz skończony liniowy układ współczynników części wielomianowej. W połączeniu z AA-45 daje pełny test elementarności całek s exp(∫h).
3. Równanie z''=qz i Riccati; pełny algorytm wymiernej gałęzi Riccatiego dla q w C[x]: dwa możliwe wielomiany wiodące, stopień P wyliczony z współczynników, sprawdzenie liniowego ODE dla P.
4. Pozostałe gałęzie Kovacica dla q w C(x) i całościowy algorytm Rischa: jasno oznaczona **klasyczna klasyfikacja i twierdzenia cytowane** z literatury, bez nieprawdziwych deklaracji o pełnym samodzielnym dowodzie.
5. Własne przykłady pozytywne i negatywne oraz dwa testy regresyjne o niezależnych podstawach arytmetycznych (SymPy, fractions.Fraction).

## Granice

Nie prezentować implementacji podzbioru z pkt 1–3 jako pełnej implementacji algorytmu Rischa ani algorytmu Kovacica. Nie wolno wyciągać nieelementarności z porażki heurystycznego CAS; negatywne odpowiedzi mają wynikać z udowodnionej przeszkody. Brak wymiernego rozwiązania Riccatiego nie wyklucza algebraicznego rozwiązania stopnia 2; rozdział ma jawny kontrprzykład.

## Bramka stabilizacji

Najpierw rozdział AA-47, następnie audyt I i korekty, audyt II niezależny i korekty, dwie serie regresji, integralność 47 rozdziałów, rzeczywisty pełny CI i przegląd **każdej nowej strony PDF**. AA-48 pozostaje nieotwarty.
