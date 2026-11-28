# Algebra liniowa — rozdział 21, audyt II (matematyczny i redakcyjny)

**Data:** 21 listopada 2026.  
**Rozdział:** `chapters/pl/linear_algebra/21-komutant-operatora-i-centralizatory-macierzy.tex`.  
**Ostatnia korekta:** commit `e7938d594738f60c73e0b2ae41c2618f623409ea`, blob `6527ae1a6daca48717e6a5f5e83958271abb16f5`.

## Weryfikacja poszczególnych dowodów

1. Algebra komutanta jest domknięta na kombinacje liniowe i składanie, zawiera jedynkę, a element odwrotny do komutującego operatora również komutuje. Dla izomorfizmu `U` sprzężenie `S -> USU^{-1}` zachowuje sumy, iloczyny, jedynkę i odwracalność.
2. Równość `C(T)=End_{K[t]}(V_T)` jest równością algebr: kluczowe jest zarówno działanie stałych wielomianów (liniowość nad `K`), jak i działanie `t` (przeplatanie z `T`).
3. Dla homomorfizmu `K[t]/(f) -> K[t]/(g)` ustalony obraz `[1]` spełnia `fy=0 mod g`. Po zapisie `f=df0`, `g=dg0` zachodzi `g|fy <=> g0|f0y <=> g0|y` dzięki względnej pierwszości; sprawdzono dobrze określoność, surjektywność i injektywność `[h]_d -> [g0h]_g`. Przypadek `d=1` daje przestrzeń zerową.
4. Komutant operatora cyklicznego jest dokładnie `K[T]`. Izomorfizm `K[t]/(m_T) -> C(T)` jest izomorfizmem algebr (nie tylko przestrzeni); odwracalność `p(T)` jest równoważna `gcd(p,m_T)=1` w obu kierunkach.
5. Rozkład endomorfizmów sumy prostej na komponenty Hom jest pełny i nie zakłada, że każdy endomorfizm zachowuje pojedynczy składnik. Poprawnie uwzględniono **wszystkie uporządkowane pary indeksów**, dlatego `dim C(T) = sum_{i,j} deg gcd(f_i,f_j)`. Liczba par z `min(i,j)=k` to `2(r-k)+1`.
6. Dla `n≥1` nierówność `n≤dim C(T)` jest ostra przy więcej niż jednym czynniku niezmienniczym. Górna równość `dim C(T)=n²` wymusza komutowanie z wszystkimi `E_ij`, najpierw diagonalność `T`, potem równość wpisów na przekątnej. Przypadek `n=1` jest uwzględniony. Dla `n=0` wzory wymiaru sumy pustej dają 0.
7. Wzór na dzielniki elementarne poprawnie zeruje przestrzenie Hom dla różnych nierozkładalnych `p,q` i w obrębie jednego `p` używa `deg(p)min(a,b)`. W audycie II poprawiono wyjaśnienie przejścia do sumy `sum B_{p,k}²`: obecny tekst liczy trójki `(i,j,k)` zamiast wprowadzać nieobjaśnione oznaczenia funkcji charakterystycznych; wyjaśnienie nie opiera się na żadnej ukrytej definicji.
8. Dla `K=F_q` i cyklicznego `T` grupa `Z(T)` odpowiada elementom odwracalnym `K[t]/(m_T)`. CRT i wzór na liczbę klas podzielnych przez `p` dają dokładnie `q^n ∏(1-q^{-deg p})`. Tu `n=deg m_T`, co zostało wyraźnie wykorzystane.

## Kontrola rachunkowa

- `J_2(0)⊕J_1(0)`: komutant to macierze `[[a,b,c],[0,a,0],[0,d,e]]`, stąd 5 parametrów i `det=a²e`; nad `F_q` centralizator odwracalny ma `(q-1)²q³` elementów.
- `diag(1,1,2)` nad `Q`: komutant `M_2(Q)⊕Q` (jako algebra) ma wymiar 5; wzór z czynników `f_1=t-1`, `f_2=(t-1)(t-2)` daje `3·1+2=5`.
- Obrót `[[0,-1],[1,0]]` nad `R`: komutant `R[A]` to `{[[a,-b],[b,a]]}`, izomorficzny z `C`; wymiar 2 i wyznacznik `a²+b²`.
- `J_3⊕J_3` i `J_3⊕J_2⊕J_1`: odpowiednio `12` i `14) wymiarów komutanta, mimo wspólnych wielomianów minimalnego i charakterystycznego.
- `C((t²+t+1)²)` nad `F_2`: wymiar komutanta 4 i liczba jednostek 12.

## Redakcja i odsyłacze

Poprawiono jedno uzasadnienie (przejście od `min(a,b)` do kwadratów `B_{p,k}`). Pozostałe dowody są pełne na poziomie dotychczasowego standardu, a zakres nie wykracza poza zaakceptowaną tematykę. Rozdział zachowuje dotychczasową terminologię: „przestrzeń”, „odwzorowanie”, „wielomian rozkłada się na czynniki”, bez samodzielnego angielskiego „dual”.

## Decyzja

**Audyt II zawierał jedną uzasadnioną poprawkę redakcyjno-matematyczną.** Po niej konieczne są kolejne niezależne audyty i zielone CI wraz z PDF; rozdział nadal **w audycie**.
