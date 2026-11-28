# Algebra liniowa — rozdział 15 „Rozkłady macierzy”, audyt I

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Plik:** `chapters/pl/linear_algebra/15-rozklady-macierzy.tex`  
**Wersja badana (blob):** `119b00abd09ef761960560e5ee4c653a65c873a3`

## Cel i zależności

Rozdział 15 rozwija zatwierdzoną teorię z rozdziałów 05 (eliminacja Gaussa), 09 (formy kwadratowe), 12 (iloczyny skalarne), 13 (rzuty i najmniejsze kwadraty) i 14 (twierdzenie spektralne). Materiał podzielono na sześć grup:
- rozkłady PLU, LU, LDU, eliminacja i zamiany wierszy;
- rozkład Choleskiego dla macierzy hermitowskich dodatnio określonych;
- rozkłady QR oraz odbicie Householdera;
- wartości osobliwe, SVD i norma macierzy;
- twierdzenie Eckarta–Younga i pseudoodwrotność Moore’a–Penrose’a;
- kanoniczny rozkład biegunowy oraz zastosowania.

Przy audycie sprawdzano istniejący tekst, nie dodawano nowych twierdzeń nieuzasadnionych wcześniejszym materiałem.

## Weryfikacja matematyczna

1. **LU i LDU:** niezerowość wszystkich wiodących minorów uzasadnia eliminację bez zamian wierszy. W dowodzie blokowym `S=C-ca^{-1}b` ma niezerowe wiodące wyznaczniki `Δ_{j+1}/a`, a konstrukcja `L,U` rzeczywiście daje `A=LU`. Rozkład z jedynkami na przekątnej `L` jest jednoznaczny; pivots `U_{kk}=Δ_k/Δ_{k-1}` są niezerowe i prowadzą do unikalnego `LDR`.
2. **PLU:** sprawdzono osobno przypadek zerowej pierwszej kolumny i przypadek z niezerowym pivotem, gdzie zamiana wierszy jest włączana do permutacji `P`. Równanie blokowe `P'C=P'S+(P'c)a^{-1}b` zgadza się z `LU`. Twierdzenie obejmuje także macierze osobliwe i nie obiecuje jednoznaczności.
3. **Cholesky:** dla hermitowskiej dodatnio określonej macierzy `H=[[a,b*],[b,C]]` liczba `a>0`, a dopełnienie Schura `S=C-bb*/a` jest dodatnio określone: `x=(-b*z/a,z)` daje `x*Hx=z*Sz`. Indukcja daje `H=LL*` i jedyność przy dodatniej rzeczywistej przekątnej. Kontrprzykład półokreślony jest poprawny.
4. **QR:** w procesie Grama–Schmidta przy zależnej kolumnie można dołączyć dowolny wektor ortonormalny, ponieważ `j≤m`; warunek `a_j∈span(q_1,...,q_j)` jest zachowany. Macierz `R=Q*A` jest górnotrójkątna, ma nieujemną rzeczywistą przekątną, a `QR=A`. Dla pełnego rzędu kolumn i dodatniej przekątnej dwie bazy QR odpowiadają tej samej przestrzeni obrazu, więc ich przejście jest unitarną górnotrójkątną macierzą z dodatnią przekątną, a zatem identycznością.
5. **Householder:** `P=vv*/(v*v)` jest rzutem ortogonalnym, `H=I-2P` spełnia `H*=H=H^{-1}`. Dla `v=x-αe_1` z dobranym znakiem `α` zachodzą `v*v=2v*x` i `Hx=αe_1`. Rozpatrzono `x_1=0` i `x` równoległy do `e_1`.
6. **SVD:** macierz `A*A` jest hermitowska dodatnio półokreślona, co daje ortonormalne wektory `v_i` i nieujemne `σ_i`. Dla dodatnich `σ_i` wektory `u_i=Av_i/σ_i` są ortonormalne, a pozostałe `Av_i` znikają. Uzupełnienie do baz daje `A=UΣV*`; różnica między jednostkowymi bazami i samymi wartościami osobliwymi została jawnie wskazana. Macierze prostokątne i zerowe pozostają objęte sformułowaniem.
7. **Rząd i normy:** `im A=span(u_1,...,u_r)`, `ker A=span(v_{r+1},...,v_n)`, `||A||op=σ_1` dla niezerowej macierzy, `||A||F²=Σσ_i²`. Podano osobno zerowy operator, aby nie używać nieistniejącej `σ_1` przy wymiarze zero.
8. **Eckart–Young, norma operatorowa:** dla `rank B≤k<rank A` przestrzenie `span(v_1,...,v_{k+1})` i `ker B` mają niezerowe przecięcie. Dla jednostkowego `x` w przecięciu `||Ax||≥σ_{k+1}`; SVD obcięte do `k` wartości osiąga dolną granicę.
9. **Eckart–Young, norma Frobeniusa:** podział reszty względem `im B` jest ortogonalny. Dla `a_i=||P_{im B}u_i||²` mamy `0≤a_i≤1`, `Σa_i≤rank B≤k` z nierówności Bessela. Ważona nierówność dla malejących `σ_i²` daje `||A-B||F²≥Σ_{i>k}σ_i²`; konstrukcja `A_k` daje równość. Dla `k=0` i `k≥r` wprowadzono jawne argumenty.
10. **Moore–Penrose:** formuła `A+=VΣ+U*` daje `AA+=P_im A`, `A+A=P_ker A perp`. Cztery tożsamości są zweryfikowane, a ich odwrotna implikacja wyznacza obie projekcje i jedyny wektor najmniejszych kwadratów o najmniejszej normie dla każdego `y`; to dowodzi niezależności od SVD i jedyności. Przykład `[[1,1],[2,2]]` daje `A+=1/10[[1,2],[1,2]]`.
11. **Dodatni pierwiastek:** definicja `H^{1/2}` przez twierdzenie spektralne daje dodatnią macierz hermitowską. Każdy drugi dodatni pierwiastek komutuje z `H=S²`, więc przez jednoczesną diagonalizację jego wartości własne muszą być odpowiednimi nieujemnymi pierwiastkami. Dowód jednoznaczności jest prawidłowy.
12. **Rozkład biegunowy:** z SVD `A=UΣV*` buduje się `W=UEV*`, a `|A|=V(Σ*Σ)^{1/2}V*`. Sprawdzono `A=W|A|`, `W*W=P_ker A perp`, `WW*=P_im A` i `ker W=ker A`. Jednoznaczność wynika z działania na `im |A|=(ker A)^⊥` i zerowania jądra. Dla kwadratowej macierzy odwracalnej `W` jest unitarna.

## Kontrola techniczna

- Rozdział 15: **1782 wierszy**, **40 etykiet**, **22 odsyłacze**.
- Cała książka 01–15: **614 różnych etykiet**, **267 rozwiązanych odsyłaczy**; brak niedomkniętych środowisk LaTeX i niezgodnych importów.
- `tools/test_linear_algebra_decompositions.py` zawiera dokładną eliminację na ułamkach, losowane przypadki hermitowskie i zespolone, QR, SVD, pseudoodwrotności oraz sprawdzenia błędów aproksymacji. Testy zakończyły się sukcesem w CI rozdziału 15.
- `catalog/books.json`, `books/pl/linear_algebra.tex` i workflow kompilacyjny zawierają rozdział 15 w właściwym miejscu.
- Zgodnie z zasadą dostarczania wyników automatyczny workflow eksportuje **osobny PDF rozdziału 15**. Cały tom pozostaje kompilowany i weryfikowany, ale w rozmowie pokazujemy tylko bieżący rozdział.

## Decyzja

**Audyt I:** nie wykryto błędów w przedstawionych powyżej przesłankach i wyprowadzeniach; rozdział pozostaje **otwarty**, dopóki nie przejdzie kolejnego niezależnego audytu matematycznego i wizualnej kontroli PDF. Należy kontynuować iterację na niezmienionym materiale, nie dodając nowych twierdzeń.
