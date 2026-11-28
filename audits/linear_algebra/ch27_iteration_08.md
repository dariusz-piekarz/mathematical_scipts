# Algebra liniowa — rozdział 27, audyt VIII (drugi czysty, stabilizacyjny)

**Data:** 21 listopada 2026  
**Rozdział:** `chapters/pl/linear_algebra/27-gramiany-obserwowalnosci-i-realizacje-minimalne.tex`  
**Zatwierdzony blob źródła:** `a91dfa108d4a6ef4221b9ba24a98c87772c75d4a`.  
**Historia:** I — integracja; II — domknięcie dowodu podobieństwa minimalnych realizacji; III — `\mathscr` niezdefiniowane w preambule; IV — polska terminologia; V — czysty matematycznie przed pełną kontrolą składu; VI — korekta długiego nagłówka; VII i VIII — dwie kolejne czyste, niezależne kontrole.

## Ponowny audyt matematyczny

1. **Założenia i liczba wymiarów.** Rozdział jawnie wprowadza n,m,p≥1 oraz A∈M_n(C), B∈M_(n×m)(C), C∈M_(p×n)(C). Definicja równoważności wejście–wyjście dotyczy odpowiedzi z zerowego stanu początkowego i zachowuje wszystkie parametry Markowa H_k=CA^kB. Pusty wymiar minimalnej przestrzeni stanu ma osobną interpretację.
2. **Dyskretny gramian obserwowalności.** Z O_N=[C;CA;...;CA^(N-1)] wynika W_o,N=O_N*O_N i dokładna suma energii obserwacji. Wyprowadzono ker W_o,N=ker O_N, a dla N≥n przez Cayleya–Hamiltona także ker O_N=ker O_n=N(C,A). Dla W_o,N>0 stan jest odtwarzany przez W_o,N^-1 O_N*Y; przy znanych sterowaniach od wyjść odejmuje się jawny wkład wymuszenia.
3. **Ciągły gramian.** Tożsamość x*W_o,T x=integral ||Ce^{tA}x||² i ciągłość funkcji podcałkowej dają zerowanie Ce^{tA}x na [0,T]; różniczkowanie w zerze i odwrotny argument przez szereg wykładniczy zapewniają ker W_o,T=N(C,A) dla każdego T>0. Prawidłowy jest wzór na x_0 przez całkę e^{tA*}C*y(t).
4. **Horyzont nieskończony.** Dla A Schur/Hurwitz zbieżność norm sum/całek wynika z geometrycznego/wykładniczego oszacowania potęg lub wykładnika A. Otrzymano obydwa równania Steina i obydwa Lapunowa, z jednoznacznością przez zanik części jednorodnej. Ich dodatnią określoność wyprowadzono z kryteriów Kalmana, a nie z samej nieujemności BB* i C*C.
5. **Parametry Markowa i jądro odpowiedzi.** Wartości H_k charakteryzują wyjście dyskretne przez splot. W czasie ciągłym Ce^{tA}B=sum t^kH_k/k!, szereg jednostajnie zbieżny dla t w przedziałach zwartych. Właśnie dlatego równość wszystkich H_k zachowuje dowolną odpowiedź przy zerowym stanie początkowym, nie tylko odpowiedź na pojedynczy impuls.
6. **Minimalizacja wymiaru.** U=R∩N jest A-niezmiennicza, A_min[r]=[Ar], B_min u=[Bu], C_min[r]=Cr są dobrze określone na R/U; brak nieobserwowalnych niezerowych klas i generowanie całego ilorazu przez A_min^k B_min są udowodnione. Blokowa macierz Hankela H_(n,n)=O_n K_n ma rangę dim R−dim U, zaś każda inna realizacja wymiaru q daje jej faktoryzację przez q-wymiarową przestrzeń. Stąd minimalny możliwy wymiar d to ta ranga.
7. **Jednoznaczność.** Wcześniejsza luka o różnych wymiarach została domknięta: wspólny horyzont N=max(d_1,d_2,1) zapewnia po Cayleyu–Hamiltonie rank H_(N,N)=d_i dla każdej minimalnej realizacji. Następnie odwzorowanie T na skończonych sumach osiągalnych jest dobrze określone dzięki obserwowalności drugiego układu. Wykazano TB_1=B_2, TA_1=A_2T, C_2T=C_1 i odwracalność przez surjekcję i równość wymiarów. Nagłówek ma teraz zwięzłą nazwę „Podobieństwo realizacji”, bez zmiany tezy.
8. **Gramiany zrównoważone.** Dla stabilnej minimalnej realizacji W_c,W_o>0; przez L=W_c^(1/2), S=L W_o L=UΣ²U* oraz T=L U Σ^-1/2 otrzymujemy W_c'=W_o'=Σ. Iloczyny W_cW_o i W_c'W_o' są podobne, więc kwadraty wartości σ_j są niezmiennikami. Nie deklaruje się bez dowodu oszacowania błędu po obcięciu stanów.
9. **Najmniejsze kwadraty.** Dla W=O_N*O_N>0 punkt minimum jest jedyny, a xhat=W^-1 O_N*Y. Ortogonalna reszta gwarantuje wyprowadzone wprost oszacowanie ||xhat−x_0||≤||ε||/sqrt(λ_min(W)). Sprawdzono także przypadek niezerowego szumu.
10. **Przykłady i język.** Obserwowalny układ nilpotentny ma gramian ciągły z wyznacznikiem T^4/12; przykład trójstanowy redukuje się do jednego stanu z identycznymi H_k=2^k; stabilny układ diagonalny ma W_c=W_o=diag(4/3,9/8), a zmiana współrzędnych zachowuje widmo ich iloczynu. Słownictwo polskie i ścisłe kwantyfikatory zgodne ze standardami.

## Potwierdzone CI, PDF i integralność

- [Run 44952142761](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44952142761) — **SUCCESS** dla dokładnego bloba `a91dfa108d4a6ef4221b9ba24a98c87772c75d4a`. Testy LA-01–27, walidacja katalogu, terminologii, etykiet i odsyłaczy, pełna kompilacja oraz krok „Verify compilation artifact and unresolved references” zakończone sukcesem. Pierwszy przejściowy log z pojedynczym Underfull został poprawiony przez kolejne przebiegi latexmk; końcowy log użyty przez walidator nie zawiera niedopuszczalnych ostrzeżeń.
- Test `tools/test_linear_algebra_minimal_realizations.py` przeszedł: **256** trójek nad F2 i **6561** trójek nad F3, z dokładną weryfikacją rang O,K,H_(2,2),H_(3,3), oraz wymierne przypadki podobieństwa, równań Stein/Lapunowa, minimalnej redukcji i oszacowania najmniejszych kwadratów.
- Kontrola struktury: **32 unikatowe etykiety**, **10 otwarć i 10 zamknięć `proof`**, wszystkie odsyłacze lokalne rozwiązane; brak niezdefiniowanego `\mathscr` i angielskiego „minimizer”.
- Pobrany z artefaktu `linear-algebra-current-chapter` samodzielny PDF zapisano jako `/mnt/data/algebra_liniowa_rozdzial_27.pdf`. Ma **11 stron**, każda niepusta; PyMuPDF: **0 bloków tekstu poza granicami stron**. Wszystkie 11 stron wyrenderowano do montażu `LA27_montage.jpg` i obejrzano: brak widocznych kolizji, uciętych wzorów i błędnych marginesów.
- Ostatnia czysta iteracja nie wymagała zmiany tekstu, etykiet, przykładu ani kodu regresyjnego.

## Decyzja

**Audyt VIII czysty**, drugi po audycie VII. **Rozdział 27 uznany za STABILNY po 8 audytach**, z pełnym zielonym CI i poprawnym samodzielnym PDF. Aktualny status algebry liniowej: **01–27 stabilne**. Rozdziały 28 (opcjonalna kontynuacja teorii układów liniowych), 29 (grassmanniany), 30 (algebry Clifforda), 31 (Pin, Spin, spinory i struktury spinowe) oraz 32 (nowe twistory) pozostają w zatwierdzonym planie. Dla LA-29–31 wykorzystać kanoniczny DG-04 i zachować dowody, przykłady i rysunki; LA-32 opracować od podstaw.
