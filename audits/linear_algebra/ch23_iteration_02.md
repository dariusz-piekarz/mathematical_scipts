# Algebra liniowa — rozdział 23, audyt II (matematyczny, po pierwszym CI)

**Data:** 21 listopada 2026  
**Źródło:** `chapters/pl/linear_algebra/23-dyskretne-rownanie-lapunowa-i-stabilnosc-schura.tex`  
**Blob po korekcie:** `8939984648cdd1c38ee57702b3b11ff38d9a4238`.

## Kontrola założeń i dowodów

1. **Stabilność.** Promień spektralny zdefiniowano wyłącznie nad \(\mathbb C\), gdzie każda macierz stopnia dodatniego ma co najmniej jedną wartość własną. Warunek \(\rho(A)<1\) jest równoważny \(A^k\to0\) przez wartości własne i oszacowanie postaci Jordana. Nie potrzeba diagonalizowalności.
2. **Jordan i wartość zero.** W pierwotnej wersji ocena używała \((1+k^{d-1})\), co przy \(k=0,d=1\) prowadzi do zapisu \(0^0\). W audycie I zastąpiono to przez \((1+k)^{d-1}\). Audyt II usunął drugą niejednoznaczność: przy \(\lambda=0\) i \(j=k\) zapisano jawnie, dlaczego czynnik \(\lambda^0\) przyjmujemy równy \(1\), oraz wskazano bezpośrednią tożsamość \(J_d(0)^k=N^k\).
3. **Istnienie rozwiązania Steina.** Dla \(Q=Q^*>0\) oszacowanie \(\|(A^*)^kQA^k\|\le M^2\|Q\|r^{2k}\) daje zbieżność bezwzględną w normie operatorowej. Szereg jest hermitowski i dodatnio określony przez pierwszy wyraz \(Q\), również dla osobliwego \(A\). Przesunięcie indeksu ma poprawny znak.
4. **Jednoznaczność w pełnej przestrzeni.** Jeżeli \(A^*DA=D\), to \(D=(A^*)^kDA^k\). Oszacowanie normowe prowadzi do \(D=0\) bez dodatkowego warunku \(D=D^*\). Odwrotnie, podstawienie wektora własnego daje \((|\lambda|^2-1)v^*Pv=-v^*Qv<0\), a więc stabilność Schura.
5. **Energia.** Równość \(E_{k+1}-E_k=-x_k^*Qx_k\) prowadzi do ścisłego spadku *tylko wtedy, gdy \(x_k\ne0\)*. Ten warunek jest istotny przy macierzach nilpotentnych. Uzasadnienie geometrycznego tempa używa odpowiednich ekstremalnych wartości własnych \(P,Q\) i faktu \(P-Q=A^*PA\ge0\).
6. **Widmo \(X\mapsto A^*XA\).** Po unitarnej triangularizacji \(A=UTU^*\) macierz \(T^*E_{ij}T\) jest kombinacją tylko \(E_{pq}\) z \(p\ge i\), \(q\ge j\), z diagonalnym współczynnikiem \(\overline\lambda_i\lambda_j\). Stąd charakterystyczny wielomian endomorfizmu macierzy to iloczyn po wszystkich uporządkowanych parach. Kryterium odwracalności \(I-\mathcal T_A\) nie zakłada dodatniej określoności.
7. **Rachunki porównawcze.** Dla dokładnego kroku \(e^{hH}\), \(h>0\), na każdym bloku Jordana wartości własne to \(e^{h\lambda}\); ich moduły są \(e^{h\operatorname{Re}\lambda}\). Dla jawnej metody Eulera \(I+hH\) wartości własne są \(1+h\lambda\), a ich moduł poniżej 1 oznacza \(2\operatorname{Re}\lambda+h|\lambda|^2<0\). Wszystkie warunki na \(h\) zostały sformułowane jawnie.

## Przykłady

- Nilpotentna macierz \(A=\left(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right)\) i \(Q=I_2\) dają \(P=\operatorname{diag}(1,2)\), ponieważ \(A^2=0\).
- Nienormalna macierz \(A=\left(\begin{smallmatrix}1/2&1/2\\0&1/4\end{smallmatrix}\right)\) daje \(P=\left(\begin{smallmatrix}4/3&8/21\\8/21&32/21\end{smallmatrix}\right)\). Rachunek na ułamkach wymiernych potwierdził \(A^{\mathsf T}PA-P=-I_2\) i \(\det P=832/441\).
- Dla \(A=\operatorname{diag}(2,1/3)\) równanie jest jednoznacznie rozwiązywalne mimo niestabilności, a rozwiązanie dla \(Q=I_2\) jest nieokreślone dodatnio: \(\operatorname{diag}(-1/3,9/8)\).
- Dla \(A=\operatorname{diag}(2,1/2)\) iloczyn wartości własnych równy \(1\) pozwala na dowolne parametry pozadiagonalne, zatem rozwiązania nie są jednoznaczne.
- Dla \(H=(-2)\) dokładne próbkowanie jest stabilne dla dowolnego \(h>0\), a jawny Euler dokładnie dla \(0<h<1\).

## Weryfikacje strukturalne

- Źródło ma 25 unikatowych etykiet, 12 odsyłaczy i 7 poprawnych par środowisk `proof`.
- Zidentyfikowano etykiety rozdziałów 14, 17, 18 i 22; nie wprowadzono nowych zależności od nieistniejących rozdziałów.
- Zintegrowano 23. rozdział z `books/pl/linear_algebra.tex`, `catalog/books.json`, `README.md` i regresem CI.
- \(\chi_{\mathcal T_A}\) oznacza wielomian charakterystyczny endomorfizmu przestrzeni macierzy, nie funkcję charakterystyczną zbioru; notacja nie koliduje z zasadą \(\chi_E\) dla funkcji charakterystycznych.

## Decyzja

**Audyt II zawierał konieczne doprecyzowanie dowodu dla \(\lambda=0\).** Następna iteracja powinna być niezależna od obecnej i sprawdzić wynik CI, skład PDF oraz wszystkie tezy bez dodawania nowego materiału. Rozdział pozostaje w audycie.
