# Algebra liniowa — rozdział 05, audyt 3 (stabilizacyjny)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/linear_algebra/05-eliminacja-gaussa-i-uklady-liniowe.tex`  
**SHA treści:** `f94bdf0b4a35730e858c50cb7fb7288b117facf6`

## Ponowna kontrola matematyczna

Skontrolowano wszystkie dziewięć części rozdziału, w szczególności: odwracalność trzech operacji na wierszach, istnienie i zakończenie algorytmów Gaussa i Gaussa–Jordana, brak dzielenia przez zero, interpretację zmiennych swobodnych, wyprowadzenie rzędu z twierdzenia o wymiarze jądra i obrazu, równoważność kryteriów zgodności `Ax=b`, konstrukcje baz jądra oraz obrazu i rozróżnienie oryginalnych kolumn od kolumn zredukowanych, jednoznaczność postaci schodkowej zredukowanej poprzez niezmienniczość przestrzeni wierszy, a także obliczanie macierzy odwrotnej. Sprawdzono także przypadki `m=0`, `n=0`, rząd zerowy i pełny. Żaden dowód nie wymaga aksjomatu wyboru dla danych przestrzeni skończenie wymiarowych.

**Nie znaleziono nowego błędu ani istotnej luki po korekcie składu z audytu 2. Plik rozdziału 05 pozostawiono bez zmian.**

## Niezależne testy skończonych ciał

- Nad `F_2`: wszystkie **689 macierzy** rozmiaru `m×n` dla `0≤m,n≤3`, w tym **5054 układy** `Ax=b`: 0 rozbieżności dotyczących rzędu, jądra, baz, zgodności i sprzecznych wierszy.
- Nad `F_3`: **21304 macierze** wszystkich rozmiarów `0≤m,n≤3`; osobna implementacja z dzieleniem przez niezerowe elementy pola sprawdziła pivoty, rząd, pełne jądro, bazę jądra i bazę oryginalnych kolumn obrazu: 0 rozbieżności.
- Rachunki dwóch przykładów nad `R` zweryfikowano przez bezpośrednie podstawienie do `Ax=b`, do jądra i do tożsamości `AA^{-1}=I`.

Testy są pomocnicze i nie zastępują dowodów.

## Kontrola spójności i CI

Dla pięciu rozdziałów z aktualnej gałęzi: **226 niepowtarzających się etykiet, 102 istniejące cele odsyłaczy, brak niedomkniętych środowisk**, brak naruszeń terminologii. Po poprawce wzoru w audycie 2 przeprowadzono pełny CI: [44908598158](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44908598158) — **success**, PDF ma **56 stron**, końcowy przebieg `pdflatex` bez `Overfull`, `Underfull`, `LaTeX Warning`, `Missing character`, `Undefined control sequence`, `Fatal error` i nierozwiązanych odsyłaczy. Równoległe [44908598130](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44908598130) — **success** (indeksowanie i testy aplikacji). Wcześniejszy `validate-cli` dla pierwszego commitu 05 także zakończył się sukcesem.

W tym commicie raportowym zaostrzono kontrolę końcowego logu: nowy warunek CI kończy się błędem przy ostrzeżeniach składu i kompilacji. Jest to zabezpieczenie przed powtórzeniem usterki, nie zmiana treści matematycznej.

## Status

**Rozdział 05 stabilny i zamknięty po audycie 3 bez nowych zmian treści.** Można przejść do następnego rozdziału zgodnie z planem książki. Kontrolę CI po aktualizacji raportów/statusu/workflow należy traktować jako osobny, nowy przebieg.
