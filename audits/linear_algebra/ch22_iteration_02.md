# Algebra liniowa — rozdział 22, audyt II (matematyczno-redakcyjny)

**Data:** 21 listopada 2026  
**Źródło:** `chapters/pl/linear_algebra/22-rownania-sylvestera-i-lapunowa.tex`  
**Blob po korekcie:** `a4751c9d59eac700c9994de01facace6fb6f9a27`  
**Test regresyjny:** `tools/test_linear_algebra_sylvester.py` — rozszerzony o test zamkniętego wzoru.

## Niezależny przegląd dowodów

1. **Równanie jednorodne.** Zweryfikowano izomorfizm `ker S_(A,B)=Hom_{K[t]}(W_B,V_A)`, uwzględniający kierunek morfizmu `B -> A`, oraz afiniczną postać zbioru rozwiązań.
2. **Dzielniki niezmiennicze i jądro.** Twierdzenie o wymiarze jądra wykorzystuje `Hom(K[t]/(g_j),K[t]/(f_i))` ze znanego rozdziału 21; suma stopni NWD wszystkich par jest poprawna. Jej zerowanie jest równoważne względnej pierwszości `chi_A,chi_B`.
3. **Sylvester.** Endomorfizm macierzy `n x m` ma skończony wymiar `nm`; injectywność jest więc równoważna surjektywności. Nad `C` wspólna wartość własna odpowiada wspólnemu czynnikowi liniowemu.
4. **Tożsamość teleskopowa.** Po wymnożeniu sumy dla `A^kX-XB^k` wyrazy pośrednie skracają się parami. Test skalarów i przykładu trójkątnego potwierdza znak oraz mnożenie przez `h(B)^{-1}` **z prawej strony**.
5. **Wzór wykonawczy.** `h=chi_A`, `h(A)=0` oraz Bézout dla `h,chi_B` dają odwracalność `h(B)`. Z równania Sylvestera i wzoru teleskopowego wynika jednoznaczny `X`. Poszerzono test o bezpośrednie podstawienie tego wzoru nad `F2,F3` przy losowych parach o względnie pierwszych charakterystycznych.
6. **Dwa bloki Jordana.** Lewo- i prawostronne mnożenie `L_N`, `R_M` przemieniają się. Binom `(L_N-R_M)^{a+b-1}` znika przez ograniczenia `L_N^a=R_M^b=0`; skończony szereg geometryczny jest poprawny także w dodatniej charakterystyce.
7. **Lapunow.** Wykładnicze oszacowanie `||exp(tA)|| <= M(1+t^{n-1}) exp(-beta t)` wynika z bloków Jordana przy `Re λ<0`, z czego wynika całkowalność i zanik przy nieskończoności. Różniczkowanie `F(t)=exp(tA*)Qexp(tA)` daje `F'=A*F+FA`, a granice dają `A*P+PA=-Q`. Dodatnią określoność uzasadnia dodatniość integrandu przy `t=0` i ciągłość, jednoznaczność — stałość `exp(tA*)Hexp(tA)`. Implikuje to poprawne twierdzenie nad `C` bez wymogu diagonalizowalności.
8. **Odwrotny kierunek Lapunowa.** Po podstawieniu wektora własnego `v` równanie daje `2Reλ(v*Pv)=-v*Qv`; ścisła dodatnia określoność wymusza `Reλ<0` dla każdego λ.
9. **Przykłady.** Nad `Q`: `A=[[1,1],[0,1]]`, `B=[3]`, `C=(2,4)^T`, rozwiązanie `(-2,-2)^T`. Nad `R`: dla `A=[[-1,1],[0,-2]]`, `Q=I`, rozwiązanie `P=[[1/2,1/6],[1/6,1/3]]`, z `A^TP+PA=-I` i `det P=5/36`. Zweryfikowano rachunek niezależnie w SymPy.

## Zmiany w audycie II

- **Błąd odsyłacza**: w trzech miejscach rozdział błędnie przywoływał `ch:lin18-chevalley`; zastąpiono istniejącą etykietą `ch:lin18-jordan-chevalley`. Pierwszy przebieg CI wykrył tę usterkę.
- **Dodatnia określoność przykładu nad C**: zamiast polegać na nieopisanej adaptacji rzeczywistej formuły kwadratowej zapisano i uzasadniono bezpośrednio `z*Pz=1/2 |x+y/3|²+5/18 |y|²>0`. Usunięto w tym miejscu niepotrzebne powołanie na kryterium Sylvestera dla form.
- **Regresja wzoru wykonawczego**: dodano test bezpośredniego podstawienia rozwiązania do `AX-XB=C` po obliczeniu `chi_A(B)^{-1}` nad małymi ciałami.

## Stan

**Audyt II — poprawki konieczne, zatem jeszcze nie jest czysty.** Kolejny audyt powinien sprawdzić ostateczne źródło, testy i pełny PDF z GitHub Actions.
