# Algebra liniowa — rozdział 25, audyt II

**Data:** 21 listopada 2026  
**Rozdział:** `chapters/pl/linear_algebra/25-sterowalnosc-obserwowalnosc-i-stabilizowalnosc.tex`.  
**Blob matematyczny:** `27572fc264e838d7c81e11a5d5f32dfa261ca643`.  
**Test po poprawce:** `tools/test_linear_algebra_control.py`, commit `b8a0a2de07f88e4aaee2e3bf1ffd735db56ecfe7`.

## Wyniki audytu

- Pierwszy pełny przebieg CI: [44949063148](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44949063148) — **FAILURE** na nowym teście. Dokładna przyczyna: w wyrażeniu składanym `sum(a[i][k]*k[k][j] for k in range(2))` nazwa `k` została przypadkowo użyta równocześnie dla macierzy Kalmana i indeksu sumowania. Python zwrócił `TypeError: 'int' object is not subscriptable`; problem nie dotyczył dowodów matematycznych.
- Poprawa techniczna: zastąpiono indeks zmienną `h` w wyrażeniu `sum(a[i][h]*k[h][j] for h in range(2))`. Nowy przebieg CI potwierdził zaliczenie kroku **Verify Kalman reachability, PBH, Gramians and stabilizing feedback**. Kompilacja LaTeX pozostaje do osobnego sprawdzenia.
- **Powtórna analiza dowodów:** wzory x_N=A^Nx_0+sum A^(N-1-j)Bu_j; ker W_T=ker K*; obserwowalność jako iniektywność O; oba kierunki PBH przez anihilator R i własne wektory z N; pełna, czteroblokowa macierz rozkładu Kalmana — zgodne z definicjami.
- **Szczególnie ważny krok:** lemat konstrukcji sprzężenia dla pary sterowalnej dowodzi istnienia r liniowo niezależnych wektorów z obrazów (H-μI)^(-1)D na dowolnym otwartym obszarze Ω. Gdyby wszystkie obrazy były w właściwej przestrzeni W, to niezerowy funkcjonał zerowałby wymierną funkcję (H-μI)^(-1)D, a więc wszystkie H^kD. To przeczy kryterium Kalmana. Wybranie Fv_j=u_j daje (H-DF)v_j=μ_jv_j. Jest to pełne uzasadnienie istnienia stabilizującego sprzężenia, nie twierdzenie o dowolnie zadanym zestawie biegunów.
- PBH dla stabilizowalności zawiera przypadki graniczne Re λ=0 i |λ|=1 po stronie niestabilnej. Przy r=0/r=n puste bloki są jawnie uwzględnione. Związek dualny z wykrywalnością zachowuje sprzężenie wartości własnych i kryteria obu czasów.
- Dla macierzy rzeczywistych stabilizujące sprzężenie może być rzeczywiste: konstrukcja wybiera rzeczywiste μ spośród ujemnych liczb lub z (-1,1); argument o wielomianie z nieskończenie wieloma zerami nadal działa.
- Gramian dyskretny W_N=K_N K_N* i minimalny koszt energii są wyprowadzone przez rozwiązanie najmniejszej normy i rozkład ortogonalny, w zgodzie z przykładami.

## Stan

**Audyt II wykrył i usunął błąd regresji w Pythonie. Nie jest liczony jako czysty audyt** w kryterium stabilizacji. Po pełnym sukcesie CI i kontroli PDF należy przeprowadzić co najmniej dwa kolejne czyste audyty na niezmienionej treści matematycznej.
