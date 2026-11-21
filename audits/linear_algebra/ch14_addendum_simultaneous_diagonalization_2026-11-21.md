# Algebra liniowa — uzupełnienie i audyt rozdziału 14: wspólna diagonalizacja

**Data:** 21 listopada 2026
**Gałąź:** `biblioteka-matematyczna-iteracja-6`
**Tekst:** `chapters/pl/linear_algebra/14-wartosci-wlasne-diagonalizacja-i-twierdzenie-spektralne.tex`
**Etykieta:** `thm:lin14-simultaneous-diagonalizable`

## Uzasadnienie uzupełnienia

W rozdziale istniały twierdzenia o wspólnej ortonormalnej bazie własnej dla operatorów samosprzężonych oraz o jednoczesnej unitarnej triangularizacji przemiennych macierzy zespolonych. Brakowało wyniku algebraicznego nad dowolnym ciałem: jeżeli `S,T` są diagonalizowalne nad `K` oraz `ST=TS`, istnieje **ta sama** odwracalna macierz `P`, dla której `P^{-1}SP` i `P^{-1}TP` są diagonalne.

## Audyt matematyczny

1. Założono wspólne ciało `K`, obie macierze kwadratowe tego samego rozmiaru `n>=0`, oraz diagonalizowalność nad **tym samym** `K`. Nie założono normalności ani iloczynu skalarnego. Dla `n=0` zastosowano bazę pustą.
2. Z `ST=TS` wynika niezmienniczość każdej przestrzeni `E_lambda(S)` względem `T`.
3. Ograniczenie diagonalizowalnego `T` do przestrzeni niezmienniczej pozostaje diagonalizowalne: wielomiany interpolacyjne Lagrange'a dla różnych wartości własnych `mu_j` dają projektory `p_j(T)`; niezmienniczość względem `T` daje niezmienniczość względem wszystkich `p_j(T)`. Otrzymujemy rozkład `E_lambda(S)=direct_sum_j (E_lambda(S) intersect E_mu_j(T))`. Wszystkie mianowniki `mu_j-mu_k` są niezerowe w ciele `K`.
4. Sumując podprzestrzenie wspólnych wektorów własnych po wszystkich `lambda` i `mu`, uzyskujemy bezpośredni rozkład całego `K^n`. Wybór baz jego niezerowych składników daje **jedną** bazę diagonalizującą obie macierze.
5. Przykład `S=[[1,1],[0,2]]`, `T=[[3,2],[0,5]]`, `P=[[1,1],[0,1]]` jest poprawny: obie macierze są przemienne, diagonalizowalne i nienormalne, a `P` nie jest ortogonalna. Pokazuje ograniczenie mocniejszej, unitarnej wersji.
6. Zachowano wszystkie dotychczasowe etykiety. Nowe sformułowanie nie powiela wyniku dla operatorów samosprzężonych ani twierdzenia o triangularizacji; uzupełnia logiczny łańcuch rezultatów.
7. W `tools/test_linear_algebra_spectral.py` dodano przykłady `2x2` i `3x3`, w tym wielokrotną wartość własną: sprawdzane są przemienność, wspólna diagonalizacja przez `P`, wspólne wektory własne i nienormalność.

## Weryfikacja CI i PDF

Zmiana tekstu: commit `6c388c880ea531f7a899bcbad0b8ec5b45bda5a3`.
Testy regresyjne: commit `d9b8f495842bc5b2cf0596e58c60d55ea278d636`.
Eksport bieżącego rozdziału 14: commit `71be2d4c342b136234a2dca32028271863e59157`.

Uruchomiony workflow: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44931996094 — wynik kompilacji i artefaktu należy potwierdzić po zakończeniu; nie deklaruje się tu przedwcześnie sukcesu.

**Po tym uzupełnieniu:** rozdział 14 wymaga końcowego zatwierdzenia na podstawie PDF, a rozdział 15 pozostaje wcześniej uznany za stabilny. Następnym rozdziałem przewidzianym do opracowania jest 16 (podprzestrzenie niezmiennicze).
