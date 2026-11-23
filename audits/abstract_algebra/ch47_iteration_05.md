# AA-47 — audyt V: uruchomione testy arytmetyczne

**Data:** 23 listopada 2026 r.
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Status:** NIE STABILNY.

## Faktyczne wykonanie

W lokalnym środowisku wykonano `python /mnt/data/test_aa47_audit05.py` z SymPy 1.14.0 oraz standardowym modułem `fractions`. Wynik: **15/15 PASS**, bez błędów wykonania.

Kod testów został dodany do repozytorium jako `audits/abstract_algebra/test_aa47_audit05.py` (commit `d9619f703e6bddc5fb96d9b5bf13f3801f244fb1`). Obejmuje:
- rozkład Hermite'a i niezerowe residuum (2 testy);
- wypadkową Rothsteina–Tragera i rekonstrukcję części logarytmicznej (2);
- dwa równania `r'+hr=s`, w tym stałe `h` (2);
- trzy tożsamości Riccatiego, w tym rozwiązanie algebraiczne `sqrt(x)-1/(4*x)` (3);
- niezależne obliczenia `fractions.Fraction` w trzech punktach dla dwóch tożsamości (6).

**Ważne ograniczenie:** `fractions.Fraction` testuje skończenie wiele wartości, a nie stanowi niezależnego ogólnego dowodu; testy nie są jeszcze podłączone do CI i nie stanowią całego wymaganego zestawu regresyjnego. Nie przeprowadzono kompilacji LaTeX ani inspekcji PDF.

## Stan stabilizacji

Zamknięto tę lokalną serię 15 sprawdzeń. Pozostało: pełne dwa zestawy testów repozytorium, kontrola wszystkich odsyłaczy, kompilacja i kontrola PDF, zielony CI na końcowym źródle, niezależny audyt stabilizacyjny. AA-48 nieotwarty.
