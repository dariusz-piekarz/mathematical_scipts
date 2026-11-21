# Algebra liniowa — rozdział 25, audyt VI (pierwszy czysty po korektach)

**Data:** 21 listopada 2026  
**Kontrolowany plik:** `chapters/pl/linear_algebra/25-sterowalnosc-obserwowalnosc-i-stabilizowalnosc.tex`.  
**Blob niezmieniony w tej iteracji:** `6b57fc1b64ef560b98e17f89322c688160376ccf`.

## Matematyka — kompletna kontrola zależności

1. **Przestrzeń osiągalna.** R(A,B)=im[B,AB,...,A^(n-1)B] zawiera im B, jest A-niezmiennicza i jest najmniejszą taką podprzestrzenią. Dowód stabilizacji przestrzeni po n potęgach korzysta z udowodnionego w LA-16 Cayleya–Hamiltona, nie z niejawnego ograniczenia.
2. **Równanie stanu.** Formuła x_N=A^Nx_0+sum A^(N-1-j)Bu_j jest udowodniona przez indukcję; wynika z niej osiągalność w N krokach i przeniesienie pomiędzy dowolnymi dwoma stanami w n krokach. W czasie ciągłym zastosowano wariację stałych z właściwymi znakami i warunkiem początkowym.
3. **Gramian ciągły.** W_T=integral e^{tA}BB*e^{tA*} dt ma jądro ker K(A,B)*, co dowiedziono przez ciągłość funkcji podcałkowej, różniczkowanie w zerze i wzór wykładniczy. Konstrukcja u(s)=B*e^{(T-s)A*}W_T^{-1}(z-e^{TA}x_0) dokładnie osiąga z. Przykład A nilpotentnej daje det(W_T)=T^4/12>0.
4. **Obserwowalność.** O(C,A) jest pionową macierzą [C;CA;...]; jej jądro to największa A-niezmiennicza część ker C. Wykazano zarówno obserwowalność po n próbkach, jak i ciągłą iniektywność obserwacji na dowolnym dodatnim przedziale. Związek K(A*,C*)=O(C,A)* jest dokładny.
5. **Kryterium PBH.** Dla kontrolowalności wykazano równoważność pełnej rangi [λI-A,B] z brakiem lewego wektora własnego zerującego B. W kierunku przeciwnym pracuje się w anihilatorze R, który jest niezerowy i A^T-niezmienniczy, gdy R nie jest pełna. PBH obserwowalności dowiedziono niezależnie z A-niezmienniczości ker O.
6. **Rozkład Kalmana.** W czterech składnikach U=R∩N, R0, N0 i W wszystkie zero-bloki wynikają z niezmienniczości R,N. Wskazano interpretację przez podilorazy; tekst nie twierdzi, że arbitralne dopełnienia same są A-niezmiennicze.
7. **Konstrukcja sprzężenia.** Lemat z rezolwentą daje bazę v_j=(H-μ_j I)^-1Du_j dla różnych μ_j z zadanego niepustego obszaru otwartego; dowód sprzeczności używa tożsamości funkcji wymiernej i pełnej sterowalności. Fv_j=u_j zapewnia dokładne wartości własne μ_j. Pozwala to stabilizować każdą sterowalną część bloku.
8. **Stabilizowalność.** W rozkładzie osiągalnym awaria PBH dla λ jest równoważna λ∈σ(A_u). Feedback A-BK nie zmienia operatora indukowanego na V/R. Zatem spektralna stabilność A_u jest konieczna i wystarczająca; warunki Re λ≥0 i |λ|≥1 poprawnie obejmują granice.
9. **Wykrywalność.** Po sprzężeniu A*,C* stabilizacja A*−C*L* jest równoważna stabilizacji A−LC; sprzężone wartości własne zachowują część rzeczywistą i moduł. Obserwator ma błąd e'= (A−LC)e lub e_{k+1}=(A−LC)e_k. W dowodzie wypisano jawnie kwantyfikator „każda wartość własna”, eliminując nieprecyzyjną notację z audytu V.
10. **Minimum energii.** W_N^d=K_NK_N*; rozwiązanie najmniejszej normy w_0=K_N*(W_N^d)^−1d jest ortogonalne do ker K_N, a więc jednoznaczne. Podane wzory są poprawne również w wymiarach m>1. Przypadek macierzy rzeczywistych zawiera osobne uzasadnienie istnienia rzeczywistej macierzy sprzężenia.

## CI i struktura

- 47 unikatowych etykiet, 30 odsyłaczy; 17 środowisk proof domkniętych; żadnych lokalnych odsyłaczy do nieistniejących etykiet.
- Wszystkie zmiany wynikające z audytów II, IV i V dotyczą tylko testu Python, nagłówka twierdzenia i doprecyzowania kwantyfikatora w dowodzie obserwatora; w bieżącej iteracji nie stwierdzono dodatkowej poprawki.
- Nowy test PBH nad F2 i F3 sprawdza wszystkie macierze 2×2 i wektory B, również wartości własne z rozszerzeń algebraicznych przez NWD minorów wielomianowych. Test przy tym sprawdza zgodność rang, dualność, Gramians i dokładne sprzężenia nad Q. Krok testowy CI był zaliczony w przebiegu 44949122637; pełny CI po aktualnym blobie w trakcie.
- Obejrzano render poprzedniej wersji rozdziału: 15 stron, wszystkie niepuste, 0 bloków tekstu poza marginesami i bez widocznych kolizji. Obecny końcowy PDF należy ponownie pobrać po zielonym CI i sprawdzić.

**Wynik:** **audyt VI czysty matematycznie i redakcyjnie** po korektach z I–V. Jest to pierwsza kolejna pełna czysta kontrola dla nowego bloba; stan techniczny i samodzielny PDF wymagają jeszcze potwierdzenia.
