# Algebra liniowa — rozdział 25, audyt III (pierwszy czysty po korekcie regresji)

**Data:** 21 listopada 2026  
**Źródło:** `chapters/pl/linear_algebra/25-sterowalnosc-obserwowalnosc-i-stabilizowalnosc.tex`, blob `27572fc264e838d7c81e11a5d5f32dfa261ca643`.  
**Test:** `tools/test_linear_algebra_control.py`, blob `8458d769829c52f35b03af0e94f802067cfd2d0c`.

## Powtórny niezależny przegląd

**1. Sterowalność dyskretna i ciągła.** Wyprowadzono dokładną sumę `x_N=A^Nx_0+sum_{j=0}^{N-1}A^{N-1-j}Bu_j`. Zależność `R(A,B)=im[B,AB,...,A^{n-1}B]` wynika z Cayleya–Hamiltona; zamknięcie pod działaniem A zostało udowodnione osobno. Dla każdej długości N zbiorem osiągalnym ze zera jest obraz odpowiedniej macierzy blokowej. W czasie ciągłym reguła iloczynu i wzór wariacji stałych są kompletne, łącznie z niejednorodnym stanem początkowym.

**2. Gramian.** `v*W_Tv=integral ||B*e^{tA*}v||²dt` jest nieujemne i zeruje się dla wszystkich t dokładnie wtedy, gdy v należy do `ker K(A,B)*`. Uzasadniono obydwa kierunki przez różniczkowanie w zerze i twierdzenie Cayleya–Hamiltona. Jawne sterowanie `u(t)=B*e^{(T-t)A*}W_T^-1(z-e^{TA}x_0)` rzeczywiście przenosi x_0 do z; zmiana zmiennej w całce jest poprawna. W przykładzie nilpotentnym obliczenia `W_T=[[T³/3,T²/2],[T²/2,T]]` i `det W_T=T⁴/12` są dokładne.

**3. Obserwowalność.** Matryca O jest pionowym złożeniem C,CA,...,CA^{n-1}; iniektywność pierwszych n obserwacji to dokładnie `ker O=0`. Z A-niezmienniczości `N=ker O` i warunku C(N)=0 wynika jej maksymalność. Dualność `K(A*,C*)=O(C,A)*` jest dokładna. Obserwowalność w czasie ciągłym odróżnia się od sterowalności: funkcja `Ce^{tA}x_0` identycznie zerowa daje wszystkie wyrazy CA^k x_0=0 i na odwrót.

**4. PBH i rozkład Kalmana.** Zawodność pełnej rangi `[λI-A,B]` jest równoważna istnieniu niezerowego lewego wektora własnego anulującego B. A-niezmienniczość R daje odwrotny kierunek przez niezerowy anihilator. W przypadku obserwowalności użyto A-niezmienniczości N. W czteroblokowym rozkładzie Kalmana zweryfikowano zerowe pozycje macierzy: `A(U)⊂U`, `A(R)⊂R`, `A(N)⊂N`; obraz B należy do R, a C znika na N. Poprawnie wyjaśniono, że dopełnienia R0,N0,W nie są kanonicznie ani koniecznie niezmiennicze.

**5. Stabilizacja.** W lemacie konstrukcyjnym przy dowolnym właściwym W i otwartym Ω znikanie wszystkich obrazów `(H-μI)^-1D` w W prowadziłoby do znikania wymiernej funkcji `φ(H-μI)^-1D` na otwartym zbiorze, a więc wszystkich `φH^kD`, sprzecznych z pełną rangą K. Wybór bazowych wektorów v_i i liniowego F z Fv_i=u_i daje wartości własne μ_i w Ω. Wykazano tylko istnienie odpowiednich biegunów stabilnych, bez fałszywego twierdzenia o dowolnym zadanym układzie biegunów.

**6. Kryteria konieczne i wystarczające.** Widmo nieosiągalnego bloku A_u nie zależy od sprzężenia, ponieważ BK ma obraz w R. Ranga PBH spada dokładnie dla wartości własnych A_u. Stabilność A_u daje stabilność całości po dobraniu sprzężenia dla sterowalnego A_r. Przypadki graniczne Re λ=0 i |λ|=1 są poprawnie zaliczone do niestabilnych. Wykrywalność przez sprzężenie A*,C* jest poprawna, również dla wartości własnych nierzeczywistych.

**7. Minimum energii.** `W_N^d=K_N K_N*`; minimalizator sterowań jest `w_0=K_N*(W_N^d)^-1(z-A^Nx_0)`. Każde inne rozwiązanie różni się o wektor z ker K_N, ortogonalny do w_0, co zapewnia jedyność i podany koszt. Przypadek rzeczywisty ma osobne uzasadnienie realności F.

## Terminologia i skład strukturalny

- 47 unikatowych etykiet, 30 odsyłaczy, 17 kompletnych dowodów; wszystkie lokalne odsyłacze istnieją, a międzyrozdziałowe odpowiadają ustalonym etykietom LA-16, LA-18, LA-22, LA-23 i LA-24.
- Brak niepożądanych terminów; zdania rozróżniają „mapę współrzędnych” od „odwzorowania”, a nierówności spektralne są jawne.
- Ostatnia korekta dotyczyła tylko nazwy zmiennej w regresji Python; matematyczny blob rozdziału nie uległ zmianie.

**Decyzja:** audyt III **czysty matematycznie i redakcyjnie**, bez zmian źródła. To pierwsza czysta iteracja po błędzie testu. Zielone testy Python potwierdzono; końcowy PDF i ostrzeżenia TeX podlegają dalszej walidacji.
