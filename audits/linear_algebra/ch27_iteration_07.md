# Algebra liniowa — rozdział 27, audyt VII (pierwszy czysty po korektach)

**Data:** 21 listopada 2026  
**Źródło:** `chapters/pl/linear_algebra/27-gramiany-obserwowalnosci-i-realizacje-minimalne.tex`  
**Kontrolowany blob:** `a91dfa108d4a6ef4221b9ba24a98c87772c75d4a`  
**Poprzednie poprawki:** II — domknięcie wymiarowego argumentu Hankela; III — niedostępny krój `\mathscr`; IV — angielskie określenie; VI — tytuł twierdzenia i ostrzeżenie Underfull.

## Ponowny przegląd dowodów

1. **Definicje, zakres i wymiary.** Ustalono jawnie n,m,p≥1 oraz wymiary A,B,C. Obie wersje układu mają wyjście y=Cx i nie zawierają członu bezpośredniego Du. Formalna równoważność wejście–wyjście dotyczy wszystkich sygnałów sterujących przy zerowym stanie początkowym, co jest napisane wprost. Dopuszczenie realizacji zerowymiarowej występuje tylko w konstrukcji minimalizującej i jest odpowiednio zinterpretowane.
2. **Obserwowalność dyskretna i ciągła.** `W_o,N=O_N*O_N`, forma jako suma ||CA^k x||², jej jądro przez normę, stabilizacja jądra dla N≥n przez Cayleya–Hamiltona. W czasie ciągłym z całki normy i ciągłości wynika zanik Ce^{tA}x dla wszystkich t, po różniczkowaniu w zerze — zanik CA^kx, co daje to samo jądro N(C,A). Wzory na stan z obserwacji są uzasadnione przez mnożenie O_N* lub całkowanie e^{tA*}C*y(t).
3. **Stein i Lapunow.** Potęgi A oraz macierz wykładnicza e^{tA} mają odpowiednie oszacowania wynikające ze stabilności. Sumy i całki definiujące oba gramiany są bezwzględnie zbieżne, a przesunięcie szeregu albo całkowanie pochodnej daje odpowiednie równania. Jednoznaczność wynika z zaniku potęg lub z rozwiązania homogenicznego równania Lapunowa. Dodatniość z jądra gramianu jest równoważna odpowiedniemu kryterium Kalmana.
4. **Parametry Markowa.** Dla x_0=0 dyskretne y_k=sum H_(k-1-j)u_j i ciągłe y(t)=integral Ce^{(t-s)A}Bu(s)ds wynikają z wcześniej udowodnionych wzorów na rozwiązanie stanu. Tożsamość wszystkich H_k oznacza tożsamość jądra Ce^{tA}B, ponieważ szereg macierzowy jest zbieżny jednostajnie na przedziałach zwartych. Zatem identyczne są odpowiedzi na wszystkie dopuszczalne sterowania.
5. **Minimalna przestrzeń R/U.** R=im K(A,B), N=ker O(C,A), U=R∩N są odpowiednio niezmiennicze względem A. Operatory A_min[r]=[Ar], B_min u=[Bu], C_min[r]=Cr są dobrze określone dzięki A(U)⊂U oraz U⊂ker C. Wykazano osiągalność wszystkich klas w ilorazie i brak niezerowych nieobserwowalnych klas. Parametry Markowa są identyczne, a dim V_min=dim R−dim U.
6. **Ranga Hankela i minimalność.** `H_(n,n)=O_n K_n`, więc jego obraz jest obrazem O_n|_R, a jego ranga to dim R−dim(R∩N). Dowolna inna realizacja wymiaru q faktoryzuje tę samą macierz Hankela przez przestrzeń wymiaru q, więc q jest ograniczony z dołu przez tę rangę. Konstrukcja ilorazu osiąga dolne ograniczenie; stąd realizacja minimalna ⇔ sterowalna i obserwowalna.
7. **Jednoznaczność podobieństwa.** Po poprawce II wybrano `N=max(d_1,d_2,1)`, sprawdzając dla obu minimalnych realizacji, że wspólna macierz H_(N,N) ma rangę d_i; osobno uwzględniono d_i=0. Dopiero po uzyskaniu d_1=d_2 tworzona jest liniowa T na sumach A_1^kB_1u_k. Niezależność od przedstawienia wynika z obserwowalności drugiej realizacji i równości H_k, surjekcja ze sterowalności drugiej, a odwracalność z równości wymiarów. Równości TA_1=A_2T, TB_1=B_2 i C_2T=C_1 wynikają bez dodatkowych przesłanek.
8. **Zrównoważenie.** Gramiany minimalnej stabilnej realizacji są dodatnio określone. Hermitowski pierwiastek L=W_c^(1/2) i S=L W_o L>0 dają rozkład S=UΣ²U*. Transformacja T=L U Σ^(−1/2) spełnia W_c'=W_o'=Σ. Podobieństwo iloczynów W_c'W_o' i W_c W_o zachowuje kwadraty wartości σ_j. Przykład diagonalny weryfikuje wzory dokładnie.
9. **Najmniejsze kwadraty.** W=O_N*O_N>0, xhat=W^{-1}O_N*Y, błąd pomiaru ε. Reszta Y−O_Nxhat jest ortogonalna do im O_N; stąd jedyne minimum i oszacowanie błędu przez λ_min(W)>0. Wszystkie macierze i wektory mają zadeklarowane wymiary, a polska terminologia jest poprawna.
10. **Przykłady i przypadki graniczne.** Minimalna realizacja 3→1 zachowuje wszystkie CA^kB=2^k, choć usunięty stan e_3 może być niestabilny i nieobserwowalny. W przypadku dim V_min=0 wszystkie parametry Markowa znikają. Stabilne przykłady wyraźnie rozróżniają własności rzeczywistych trajektorii, graminów i ich zmian współrzędnych.

## Struktura LaTeX i regresje

- Obecna wersja nie używa `\mathscr`, ma krótki nagłówek `Podobieństwo realizacji` oraz polski zwrot „punkt minimum”.
- 32 unikatowe etykiety i 10 domkniętych środowisk `proof`; wszystkie lokalne `lin27` są rozwiązywalne. Brak terminów zabronionych przez standard repozytorium.
- Testy dokładne Python przeszły: nad F2/F3 wyczerpujące 256 i 6561 trójek, rangi H_(2,2), H_(3,3), oraz wymierne przykłady równań Stein/Lapunowa, minimalnej redukcji i błędu najmniejszych kwadratów.
- Pełny CI i PDF dla ostatniego bloba są jeszcze w toku, dlatego status pozostaje otwarty do ich weryfikacji.

**Wynik:** **pierwszy czysty audyt matematyczny, redakcyjny i strukturalny po korektach**; żadna zmiana w źródle nie była potrzebna. Do stabilizacji wymagany kolejny czysty audyt i zielony CI/PDF.
