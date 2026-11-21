# Algebra liniowa — rozdział 18, audyt II

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Plik:** `chapters/pl/linear_algebra/18-rozklad-jordana-chevalleya-i-funkcje-macierzy.tex`  
**Zweryfikowany blob po poprawkach:** `7b1d306bec1d43944c3275bc950ade9b17c1ee2f`  
**Wcześniej:** `audits/linear_algebra/ch18_iteration_01.md`.

## Ponowny niezależny audyt matematyczny

1. **Założenia:** pierwsza część jest ważna nad dowolnym ciałem `K`, o ile `m_T` rozszczepia się nad `K`. W rachunku holomorficznym oraz w twierdzeniu o wykładniczej jawnie pracujemy nad `C`. Zbadano przypadki `V=0`, `p=0`, `k=0`, `λ=0` i niezerowych operatorów nilpotentnych w dodatniej charakterystyce.
2. **Rzuty na uogólnione przestrzenie własne:** wielomiany Bézouta `u_λ g_λ+v_λ f_λ=1` spełniają wymagane kongruencje; `q_λ(T)` działa identycznościowo na `W_λ`, a zerowo na pozostałych składnikach sumy prostej. Z tego wynikają idempotentność, `P_λP_μ=0` dla `λ≠μ`, `ΣP_λ=I`, `imP_λ=W_λ` i niezależność od wyboru reprezentanta `q_λ`.
3. **Jednoznaczność rozkładu Jordana–Chevalleya:** `S=ΣλP_λ` jest diagonalizowalny nad `K`, `N=T-S` nilpotentny i oba są wielomianami w `T`. Dla konkurencyjnego `S'+N'` podprzestrzenie własne `S'` są niezmiennicze względem `N'` i zawarte w odpowiadających im `W_λ`; bezpośredniość obu rozkładów wymusza `S'=S`. Sprawdzono argument także dla `V=0`.
4. **Współczynniki wielomianowe w dowolnej charakterystyce:** definicja `p^[j](λ)` jako współczynnika `u^j` w `p(λ+u)` nie wymaga dzielenia przez `j!`. **Wykryto błąd definicyjny:** poprzednia wersja pisała górną granicę sumowania `deg p` także dla `p=0`, bez konwencji dla `deg 0`. Naprawiono przez rozdzielenie `p≠0` oraz `p=0`, gdzie jawnie `p^[j](λ)=0`.
5. **Rachunek wielomianów, potęg i odwrotności:** formuła `p(T)=Σ_λΣ_{j<a_λ}p^[j](λ)N^jP_λ` wynika z podstawienia do wielomianu po ograniczeniu do `W_λ`. Współczynniki dwumianowe i `0^0=1` przy `k=0` są właściwie interpretowane nad dowolnym ciałem. Skończony szereg geometryczny daje `T^{-1}` dla `0∉σ_K(T)`.
6. **Funkcje analityczne nad `C`:** z lokalnych rozwinięć Taylora na nilpotentnych składnikach wynika liniowość i multiplikatywność `f\mapsto f(T)`, zgodność z wielomianami oraz wzór `(f(T))^{-1}=(1/f)(T)`, jeśli `f` nie znika w widmie. Otwarty zbiór definicji nie musi być spójny ani obejmować całej `C`.
7. **Wykładnicza:** poprawny jest argument z normy operatorowej i szeregów bezwzględnie zbieżnych. **Wykryto duży skrót** w uzasadnieniu wzoru na `e^{zT}`: poprzednia wersja przeskakiwała od dwumianu Newtona do iloczynu bez rozpisania zmiany kolejności sum. Dodano szczegółowy rachunek dla `k=h+j`, ze współczynnikiem `binom(h+j,j)/(h+j)!=1/(h!j!)` oraz z ograniczeniem `0≤j<a_λ`. Następnie własność grupowa wynika z multiplicatywności rachunku analitycznego.
8. **Przykłady:** `q_3(t)=(t-1)^2/4` przy `T=J_2(1)⊕(3)` daje rzuty `P_3=`diag`(0,0,1)`, `P_1=I-P_3`; `N^2=0`. Wzór na `J_3(1)^k` jest poprawny także w charakterystyce 2; przykład ODE dla `J_3(2)` spełnia równanie i warunek początkowy.
9. **Terminologia i LaTeX:** poprawiono również podsumowanie, aby jednoznacznie wskazywało lokalne czynniki `e^{zλ}`. Skontrolowano **21 różnych etykiet, 13 odsyłaczy i 6 zamkniętych dowodów**, bez kolizji etykiet i bez niedozwolonej terminologii.

## Testy i kontrola CI

- Wzmocniono `tools/test_linear_algebra_chevalley.py` o przypadki `n=0`, `n=1`, wielomian zerowy w dwóch reprezentacjach, wyższe stopnie i charakterystykę dodatnią. Zachowano testy `2×2` i `3×3` nad `F_2,F_3` oraz test wykładniczej.
- Dwa oddzielne przebiegi CI: [po korekcie rozdziału](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44938050412) oraz [po rozszerzeniu regresji](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44938099131). Ich status i eksport PDF trzeba potwierdzić po zakończeniu; nie deklarujemy sukcesu przed wynikiem.
- PDF z poprzedniej wersji audytu I: 7 stron, 0 bloków poza stroną. Aktualny PDF musi zostać pobrany z najnowszego pomyślnego przebiegu i obejrzany oddzielnie.

## Decyzja

**Audyt II wykrył i usunął dwie nieścisłości (przypadek `p=0` i szczegółowość dowodu wykładniczej).** Rozdział 18 pozostaje **w audycie**; audyt III ma ponownie niezależnie sprawdzić matematykę i aktualny PDF bez rozszerzania zawartości.
