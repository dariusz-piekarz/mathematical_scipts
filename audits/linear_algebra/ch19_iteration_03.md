# Algebra liniowa — rozdział 19, audyt III

**Data:** 21 listopada 2026  
**Tekst:** `chapters/pl/linear_algebra/19-postac-frobeniusa-i-czynniki-niezmiennicze.tex`  
**Blob:** `230cea2d0c9e7bd616bd7f1ed9f24e0953609a7e`  
**Poprzednio:** audyt I i audyt II (w II dopisano wyjaśnienie zachowania ideałów minorów).

## Pełny odczyt krytyczny

1. W definicji `V_T` działanie jednostki, dodawania i mnożenia `K[t]` na `V` jest zgodne z działaniem liniowym wielomianu operatorowego; izomorfizm modułów zachowuje mnożenie przez `t`, a więc przeplata operatory, również gdy przestrzenie są różne.
2. W prezentacji `V_T` ewaluacja wielomianów wektorowych jest epimorfizmem modułów. Tożsamość teleskopowa działa także dla współczynników stałych; jądro jest dokładnie obrazem `tI-A`, co eliminuje ryzyko pomylenia cokernela z jądrem.
3. Przy algorytmie Smitha każdy restart po wykryciu niedzielącego się elementu bloku `B` zmniejsza stopień niezerowego pivota. Zerowanie wiersza/kolumny nie narusza `K[t]`-odwracalności operacji. Indukcja jest poprawna dla `n=1` i przechodzi do `n-1`.
4. Dzielniki wyznacznikowe są wyznaczone przez ideały minorów; uzupełnione w audycie II uzasadnienie ich niezmienniczości jest poprawne także przy dwóch wybranych wierszach. Dla macierzy diagonalnej z podzielnością iloczyn `d_1...d_k` rzeczywiście dzieli wszystkie minory i sam występuje.
5. Macierz towarzysząca ma jedynki pod przekątną; jej kolumny odpowiadają mnożeniu przez `t` na klasach `1,t,...,t^{d-1}`. Minimalny wielomian wyznacza anihilator elementu generującego, a charakterystyczny ma taki sam stopień.
6. W dowodzie Frobeniusa lewy i prawy czynnik unimodularny nie zmieniają izomorfizmu ilorazu; wycięcie bloków `d_j=1` jest konieczne, a ich dodatni stopień zachowuje łańcuch podzielności. `\chi_T` i `m_T` wynikają osobno, bez utożsamiania obu pojęć.
7. Wyprowadzono wszystkie trzy kierunki równoważności cykliczności; uwaga o `n=0` zapobiega niesłusznemu warunkowi jednego bloku w wymiarze zerowym.
8. Sprawdzono rachunek minorów w trzech przykładach oraz konwencję przy braku wartości własnych nad `\mathbb R`; nie znaleziono kontrprzykładu ani niedopowiedzianego założenia.

## Kontrole techniczne

- 20 etykiet unikatowych, 13 odsyłaczy `ref/eqref`, 7 poprawnych par środowisk `proof`.
- Nie wykryto zabronionych w tym kontekście sformułowań „unia”, „relacja liniowa”, „rozszczepiony wielomian” czy „tensorowanie”.
- [GitHub Actions 44941540440](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44941540440): **SUCCESS** dla blobu `230cea2d0c9e7bd616bd7f1ed9f24e0953609a7e`, obejmujący testy, pełny PDF i eksport rozdziału.

## Decyzja

**Audyt III czysty:** bez zmian matematycznych i redakcyjnych, pierwszy czysty przebieg po audycie II.
