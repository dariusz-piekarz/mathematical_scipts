# Algebra liniowa — rozdział 22, audyt III (niezależny po poprawkach)

**Data:** 21 listopada 2026  
**Tekst:** `chapters/pl/linear_algebra/22-rownania-sylvestera-i-lapunowa.tex`  
**Blob rozdziału:** `a4751c9d59eac700c9994de01facace6fb6f9a27`  
**Poprzednie audyty:** I — pierwszy tekst, II — naprawy odsyłaczy i uzasadnienia dodatniej określoności.

## Audyt matematyczny od podstaw

1. **Definicje i wymiary.** Operator `S_(A,B)` działa na pełnej `nm`-wymiarowej przestrzeni `Mat_(n×m)(K)`, a nie na macierzach kwadratowych. Ustalono `n,m≥1` i właściwe rozmiary wszystkich wyrazów `AX`, `XB`, `C`.
2. **Warunek jednorodny.** Równość `AX=XB` implikuje `A^kX=XB^k` dla wszystkich `k≥0`, a następnie `p(A)X=Xp(B)`. W drugą stronę działanie `t` wystarcza do przeplatania. Tym samym kierunek Hom `W_B→V_A` jest poprawny.
3. **Formuła wymiaru.** Podstawienie rozkładów na moduły cykliczne i uwzględnienie wszystkich par `(i,j)` daje `dim ker S=∑ deg gcd(f_i,g_j)`. Równość z zerem jest równoważna względnej pierwszości wielomianów charakterystycznych przez rozkład na czynniki nierozkładalne.
4. **Jednoznaczna rozwiązywalność.** Dla skończenie wymiarowej przestrzeni liniowość `S` i `ker S=0` są wystarczające, by `S` było surjekcją. Nie mylimy kryterium istnienia dla jednego `C` z kryterium istnienia dla każdego `C`.
5. **Algorytm wykonawczy.** Tożsamość teleskopowa została zweryfikowana dla `k=1,2` i ogólnie przez przesunięcie indeksu. Po zsumowaniu współczynników `h=chi_A` otrzymujemy `-Xh(B)=∑h_k∑A^(k-1-j)CB^j`. Bézout dla `h,chi_B` i Cayley–Hamilton dają odwracalność `h(B)`. Wzór jawny ma prawidłowy minus i prawostronne `h(B)^(-1)`.
6. **Bloki Jordana.** Operatory `L_N(X)=NX` i `R_M(X)=XM` przemieniają się; w `(L_N-R_M)^(a+b-1)` każdy składnik zawiera `L_N^a` albo `R_M^b` i znika. Odwrotność `(λ-μ)I+N` z szeregu geometrycznego ma dokładnie podaną liczbę składników; nie wymaga charakterystyki zero. Dla `λ=μ` wymiary Hom wynoszą `min(a,b)`.
7. **Lapunow — istnienie.** Nad `C` Jordan i skończony wzór na wykładniczą dają oszacowanie `||e^{tA}|| ≤ M(1+t^{n-1})e^{-βt}`; to wystarcza do bezwzględnej całkowalności `e^{tA*}Qe^{tA}`. Różniczkowanie podcałkowej funkcji oraz granica przy nieskończoności prowadzą do `A*P+PA=-Q`.
8. **Lapunow — dodatnia określoność i jednoznaczność.** Dla każdego `x≠0` funkcja podcałkowa ma dodatnią wartość przy `t=0` i jest ciągła, dlatego `x*Px>0`. Różnica dwóch rozwiązań jest rozwiązaniem jednorodnym, zaś `e^{tA*}He^{tA}` ma pochodną zerową i granicę zero, co daje `H=0`.
9. **Lapunow — konieczność.** Dla wartości własnej `λ` i wektora własnego `v≠0`: `2Reλ·(v*Pv)=-(v*Qv)`; dodatnia określoność obu macierzy wymusza `Reλ<0`. Wniosek o funkcji energii wynika z pochodnej iloczynu i odwracalności wykładniczej.

## Sprawdzenie przykładów

- Nad `Q` rozwiązanie `X=(-2,-2)^T` spełnia `AX-XB=(2,4)^T` dla `A=[[1,1],[0,1]]`, `B=(3)`; również formuła przez `h(B)=4` zwraca to samo.
- Dla `A=[[-1,1],[0,-2]]` i `Q=I` dokładny rachunek daje `P=[[1/2,1/6],[1/6,1/3]]`, `A^TP+PA=-I`, `det P=5/36` oraz `z*Pz=1/2|x+y/3|²+5/18|y|²>0` dla `z≠0`. Obliczenia niezależnie zweryfikowane w SymPy.
- Dla `A=diag(-1,1)`, `Q=I` brak dodatnio określonego rozwiązania wynika bezpośrednio po podstawieniu wektora własnego `e_2`.
- Przykład `A=B=(2)` ma zerowy operator Sylvestera, dlatego dla `C=(1)` brak rozwiązań, dla `C=(0)` wiele rozwiązań.

## LaTeX, język, referencje i regresje

- Wersja po audycie II ma **25 etykiet (wszystkie różne), 25 odsyłaczy, 10 otwarć i 10 zamknięć środowiska `proof`**.
- Wykryta poprzednio nieistniejąca etykieta `ch:lin18-chevalley` już nie występuje; używana jest istniejąca `ch:lin18-jordan-chevalley`.
- Nie występują zakazane formy: samodzielny angielski „dual”, „unia” dla sumy mnogościowej, „tensorowanie” czy „rozszczepianie się wielomianu”.
- Nowy test regresyjny obejmuje rangę operatora `AX-XB` i stopnie NWD czynników Smitha na kilkuset / kilku tysiącach par macierzy nad `F2,F3`, wzór wykonawczy i arytmetykę wymierną w przykładzie Lapunowa. Kroki matematycznych testów zostały ukończone w workflow; końcową kompilację PDF należy potwierdzić oddzielnie.

**Decyzja:** Audyt III matematycznie czysty po poprawkach II, bez nowej zmiany źródła. Przed zamknięciem potrzebny następny audyt i pełne zielone CI z kontrolą samodzielnego PDF.
