# Algebra liniowa — rozdział 27, audyt I

**Data:** 21 listopada 2026  
**Plik:** `chapters/pl/linear_algebra/27-gramiany-obserwowalnosci-i-realizacje-minimalne.tex`  
**Zachowane stabilne źródła:** rozdziały 01–26.  
**Zakres:** gramiany obserwowalności, minimalne realizacje, Hankel, podobieństwo realizacji, równoważenie i estymacja stanu.

## Kontrola założeń, zależności i dowodów

1. Gramian dyskretny W_o,N=O_N*O_N daje dokładnie sumę kwadratów norm obserwacji. Dla N≥n jego jądro równa się N(C,A), dzięki Cayleyowi–Hamiltonowi; dla O_N o pełnej randze odtwarzanie stanu jest dane przez W_o,N^{-1} O_N*Y.
2. W czasie ciągłym gramian W_o,T=integral e^{tA*}C*Ce^{tA}dt ma jądro N(C,A) dla każdego T>0. Wniosek wynika z różniczkowania analitycznej funkcji Ce^{tA}x w 0 oraz odwrotności przez szereg wykładniczy. Sprawdzono wzór odtwarzający x_0 z całki wyjścia.
3. Dla A Schura (czas dyskretny) i A Hurwitz (czas ciągły) odpowiednie graminany W_c i W_o istnieją i są jedynymi rozwiązaniami równań Steina/Lapunowa. Dodatnia określoność jest równoważna odpowiedniej pełnej randze; nie mylić Q≥0 z Q>0 w twierdzeniach o stabilności.
4. Parametry Markowa H_k=CA^kB dają dyskretny splot wyjścia i ciągłe jądro Ce^{tA}B przez szereg wykładniczy. Równość wszystkich H_k gwarantuje równość odpowiedzi wejście–wyjście dla zerowych stanów początkowych w obu rodzajach czasu; ta ograniczająca hipoteza została wypisana jawnie.
5. Minimalna przestrzeń stanu R/(R∩N): dobre określenie A_min, B_min, C_min wynika z niezmienniczości R,N i U=R∩N. Wykazano sterowalność i obserwowalność ilorazu oraz równość wszystkich parametrów Markowa. Przypadek zerowego wymiaru został sformułowany osobno.
6. Hankel H_{n,n}=O_n K_n ma rangę dim R−dim(R∩N). Każda inna realizacja o wymiarze q ma faktoryzację tej samej macierzy przez przestrzeń wymiaru q, stąd q≥rank H. Daje to minimalność ilorazu i kryterium: pełna sterowalność i obserwowalność.
7. Minimalne realizacje o tych samych H_k są podobne. Przesłanie sumy A_1^kB_1u_k na sumę A_2^kB_2u_k jest dobrze określone przez obserwowalność drugiej realizacji, a surjektywne przez jej sterowalność. Weryfikacja TA_1=A_2T, TB_1=B_2, C_2T=C_1 jest jawna.
8. Dla stabilnej realizacji minimalnej W_c,W_o>0. Z faktoryzacji L=W_c^{1/2}, S=L W_o L=U Σ² U* konstruujemy T=L U Σ^{-1/2}. Wtedy W_c'=W_o'=Σ. Iloczyn W_c W_o przechodzi przez podobieństwo, toteż wartości Hankela są niezmiennikami. Nie stwierdzamy nieudowodnionego twierdzenia o błędzie redukcji zrównoważonej.
9. Przy błędzie pomiarowym Y=O_N x_0+ε rozwiązanie najmniejszych kwadratów W^{-1}O_N*Y jest jedyne; oszacowanie ||xhat−x_0||≤||ε||/sqrt(λ_min(W)) wynika z rzutu ortogonalnego na obraz O_N oraz W>0.

## Regresje i warunki zamknięcia

- Nowy test `tools/test_linear_algebra_minimal_realizations.py` obejmuje wyczerpująco wszystkie jednowejściowe, jednowyjściowe trójki 2×2 nad F2/F3 (256 oraz 6561 układów), weryfikując rangi Kalmana, iloczyn O K oraz dwie wielkości macierzy Hankela, niezależnie od możliwych rozszerzeń ciał dla widma.
- Testy wymierne obejmują minimalną redukcję 3→1, podobieństwo realizacji 2×2, gramiany Steina i Lapunowa, transformację współrzędnych zrównoważonych oraz normalne równania najmniejszych kwadratów.
- Do stabilizacji: przynajmniej dwa kolejne czyste audyty po ostatniej korekcie, pełne zielone CI i samodzielny PDF rozdziału 27 ze sprawdzonymi stronami, marginesami, ilustracjami i ostrzeżeniami LaTeX.

**Status po audycie I: w audycie, bez deklaracji stabilizacji.** Plan LA-29/30/31/32 zachowany: grassmanniany i algebry Clifforda, następnie zatwierdzone Pin/Spin i spinory z DG-04 oraz nowy rozdział o twistorach.
