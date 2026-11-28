# Algebra liniowa — rozdział 27, audyt V (pierwszy czysty po korektach)

**Data:** 21 listopada 2026  
**Kontrolowany rozdział:** `chapters/pl/linear_algebra/27-gramiany-obserwowalnosci-i-realizacje-minimalne.tex`.  
**Blob:** `f4503d54238a2c67d96d7e0cc9441db0181d1eac`.  
**Poprzednie korekty:** II (ranga wspólnej macierzy Hankela dla różnych wymiarów), III (`\mathscr\to\mathcal`), IV (polskie „punkt minimum”).

## Ponowna niezależna kontrola matematyczna

1. **Założenia i wymiary.** Jawnie ustalono n,m,p≥1, A∈M_n(C), B∈M_(n×m)(C), C∈M_(p×n)(C), oraz obydwa układy z y=Cx bez bezpośredniego członu D u. Dla alternatywnych realizacji dopuszczono wymiar stanu zero, objaśniając znaczenie pustych macierzy.
2. **Dyskretna obserwowalność.** Dla N≥1 mamy `W_o,N=O_N*O_N` i `x*W_o,N x=sum ||CA^k x||²`. Dowód jądra `ker W_o,N=ker O_N` pochodzi z tożsamości normy. Dla N≥n Cayley–Hamilton daje `ker O_N=ker O_n=N(C,A)`; wymagana jest dodatnia określoność gramianu dokładnie przy pełnej randze O_n.
3. **Ciągła obserwowalność.** `x*W_o,T x=integral ||Ce^{tA}x||²dt`. Zerowanie na przedziale jest równoważne zerowaniu funkcji analitycznej Ce^{tA}x i wszystkich współczynników CA^k x, co implikuje x∈N(C,A) i odwrotnie. Stąd pełna ranga niezależna od T>0. Wzór na x_0 przez całkę z e^{tA*}C*y(t) jest poprawny.
4. **Nieskończone gramiany.** W przypadku dyskretnym oszacowanie ||A^k||≤Mr^k, r<1, zapewnia zbieżność obu szeregów, równania Steina i jedyność przez zanik potęg. W czasie ciągłym oszacowanie e^{tA} i całkowanie pochodnych dają równania Lapunowa. Każdy składnik/czynnik jest półokreślony, a ściśle dodatnią określoność graminów zapewnia odpowiednie kryterium sterowalności lub obserwowalności.
5. **Parametry Markowa.** `H_k=CA^kB` mają rozmiar p×m. Dla x_0=0 dyskretny sygnał wyjścia jest splotem z H_k, a ciągłe jądro Ce^{tA}B jest określone przez szereg `sum t^k H_k/k!`. Jednostajna zbieżność na przedziale zwartym jest uzasadniona przez oszacowanie normy, co weryfikuje równoważność wejście–wyjście w obu rodzajach czasu.
6. **Redukcja.** Podprzestrzenie R i N są A-niezmiennicze, więc U=R∩N też. Operatory A_min[r]=[Ar], B_min u=[Bu], C_min[r]=Cr są dobrze określone na R/U, bo U⊂ker C i A(U)⊂U. Obraz B_min generuje iloraz przez potęgi A_min; jeśli klasa jest nieobserwowalna, jej reprezentant leży w R∩N, a więc klasa jest zerowa. Zachowana jest każda macierz CA^kB.
7. **Hankel i wymiar minimalny.** Bloki iloczynu O_n K_n to dokładnie H_(i+j). Ranga iloczynu wynosi `dim R−dim(R∩N)` przez twierdzenie o wymiarze obrazu/jądra ograniczenia `O|_R`. Dla alternatywnej realizacji o q stanach ta sama macierz Hankela faktoryzuje się przez przestrzeń wymiaru q, więc d≤q; realizacja na R/U ma wymiar d. Minimalność jest więc równoważna jednoczesnej sterowalności i obserwowalności.
8. **Jednoznaczność do podobieństwa.** Po korekcie II ustalono wspólny horyzont N=max(d_1,d_2,1), tak że ranga identycznej macierzy H_(N,N) wynosi d_i dla każdej realizacji minimalnej; to dowodzi d_1=d_2, również rozpatrując przypadek wymiaru zero. Odwzorowanie T(sum A_1^k B_1u_k)=sum A_2^k B_2u_k jest niezależne od przedstawienia, gdyż obserwowalność drugiej realizacji unieważnia każdą zależność; sterowalność zapewnia surjekcję. Sprawdzono TA_1=A_2T, TB_1=B_2, C_2T=C_1.
9. **Równoważenie.** Dla stabilnej minimalnej realizacji W_c,W_o>0. Przy L=W_c^{1/2}, S=L W_o L>0, spektralne rozłożenie S=UΣ²U* i T=L U Σ^{−1/2} daje W_c'=W_o'=Σ. Transformacje W_c'=T^{−1}W_c T^{−*} oraz W_o'=T*W_o T prowadzą do podobieństwa iloczynów, zatem kwadraty σ_i są niezmiennikami. Nie wyprowadzono bez dowodu stabilności obciętej realizacji ani oszacowania błędu aproksymacji.
10. **Najmniejsze kwadraty.** O_N*O_N>0 gwarantuje jedyny punkt minimum `xhat=W^{−1}O_N*Y`. Reszta Y−O_N xhat jest ortogonalna do obrazu O_N; granica błędu ||xhat−x_0||≤||ε||/sqrt(λ_min(W)) wynika z własności rzutu i definicji λ_min(W). Nie wymagano fałszywie niezakłóconego sygnału.
11. **Przykłady.** Dla A nilpotentnej i C=e1* uzyskano W_o,2=I i ciągły gramian z wyznacznikiem T^4/12. Trójstanowy przykład redukuje się do A_min=(2),B_min=C_min=(1), a H_(3,3) ma rangę 1. Dwustanowy stabilny układ diagonalny ma W_c=W_o=diag(4/3,9/8); przy T=diag(2,3) oba gramiany zmieniają się zgodnie z kongruencją, a ich iloczyn zachowuje widmo.

## Struktura

- Wszystkie etykiety unikatowe, wszystkie lokalne odsyłacze zdefiniowane, środowiska proof poprawnie domknięte.
- Nie ma niezdefiniowanego `\mathscr` ani angielskiego słowa „minimizer”; nie stwierdzono nowych błędów terminologicznych.
- Regresja z pełnym wyliczeniem nad F2/F3 przeszła w CI, testy wymierne obejmują sumy/calki graminów oraz faktoryzację Hankela. Trwa końcowa walidacja LaTeX i PDF dla bloba po audycie IV.

**Wynik:** **audyt V czysty matematycznie i redakcyjnie**, bez zmian źródła; pierwszy z dwóch wymaganych kolejnych audytów. Nie deklarować stabilizacji przed zielonym CI i końcowym PDF.
