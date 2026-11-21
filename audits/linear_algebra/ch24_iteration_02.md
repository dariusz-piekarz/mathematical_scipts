# Algebra liniowa — rozdział 24, audyt II (matematyczny po korekcie I)

**Data:** 21 listopada 2026  
**Źródło:** `chapters/pl/linear_algebra/24-rownania-riccatiego-i-sterowanie-liniowo-kwadratowe.tex`  
**Ostatni kontrolowany blob:** `ae1d94e8a95838225b254096e284f98f571cc829`.

## Dowody od podstaw

1. **Uzupełnianie kwadratu.** Dla hermitowskiego `M>0` tożsamość `u*Mu+2Re(u*c)+d=(u+M^-1c)*M(u+M^-1c)+d-c*M^-1c` jest algebraicznie poprawna. Ścisła dodatnia określoność daje jedyność minimalizatora.
2. **Dyskretny horyzont N.** Bellmanowski krok minimalizacji jest uzasadniony przez indukcję i podzielenie horyzontu na pierwszy etap i pozostałe N etapów. Macierz `M_N=R+B*P_NB` jest dodatnio określona; rekurencja `P_{N+1}` jest poprawna z uwzględnieniem kolejności czynników. Nie zakłada się odwracalności `B`.
3. **Monotoniczność P_N.** Dodatkowy nieujemny koszt etapu nie może obniżyć minimalnej wartości; ograniczenie przez sterowanie zerowe daje `P_N≤W` dla stabilnego A, gdzie W rozwiązuje dyskretne równanie Lapunowa.
4. **Istnienie DARE.** Dla każdej pary wektorów zespolonych monotoniczność i ograniczenie form kwadratowych dają zbieżność współczynników przez polaryzację. M≥R zapewnia ciągłość odwrotności w rekurencji. Granica `P≥P_1=Q>0` spełnia DARE.
5. **Dyskretna stabilność zamkniętej pętli.** Po podstawieniu `K=(R+B*PB)^-1 B*PA` równanie DARE jest równoważne `P=Q+K*RK+(A-BK)*P(A-BK)`; dyskretne twierdzenie Lapunowa gwarantuje `rho(A-BK)<1`.
6. **Dyskretna jednoznaczność.** Nie wolno wymagać `R+B*P_2B>0` od dowolnego stabilizującego rozwiązania P_2. Dowód po audycie I używa jedynie odwracalności obu M_i i tożsamości różnicy `D=(A-BK_1)*D(A-BK_2)`. Po iteracji k i zaniku obu potęg D=0. Kontrola niezależna w wymiarze jeden: dla `A=1/2,B=1,Q=7/8,R=1`, rozwiązania `P_1=1,P_2=-7/8` dają `A_1=1/4,A_2=4,D=15/8` i rzeczywiście `D=A_1DA_2`.
7. **Dyskretne sterowanie nieskończone.** Dla dowolnego sterowania o skończonym koszcie dodatnio określone Q gwarantuje `sum ||x_k||²<∞`, więc `x_k→0`. Sumowanie tożsamości dopełnienia kwadratu daje dolne ograniczenie kosztu; sterowanie `u=-Kx` osiąga je, a dodatnio określona macierz M wymusza jego jedyność.
8. **Ciągłe równanie różniczkowe.** Równanie `S'=A*S+SA-SBR^-1B*S+Q`, `S(0)=0` ma lokalne rozwiązanie dzięki lokalnej lipschitzowskości prawej strony. Hermitowskość wynika z jednoznaczności i sprzężenia. Podstawienie `S(T-t)` w pochodnej `x*Sx` daje prawidłowy znak minus i identyczność kosztu. Konstrukcja optymalnego liniowego sprzężenia zwrotnego zapewnia osiągnięcie minimum. Porównanie z zerowym sterowaniem ogranicza S na dowolnym skończonym horyzoncie i wyklucza wybuch rozwiązania ODE.
9. **Nieoznaczoność wartości w punktach.** Doprecyzowano: optymalne sterowanie przy klasie funkcji przedziałami ciągłych jest jednoznaczne **prawie wszędzie**, nie dosłownie jako funkcja punktowa. Wyjaśnienie znajduje się także w osobnej uwadze.
10. **Ciągłe CARE i stabilność.** Przy stabilnym A monotoniczna rodzina S(t) jest ograniczona przez całkę z zerowego sterowania. Zbieżność elementów daje macierz P; dodatnia określoność S(1) uzasadnia `P>0`. Jeżeli S(t)→P i S'(t)=F(S(t)), to z ciągłości F i zbieżności S wynika F(P)=0. Tożsamość `A_cl*P+PA_cl=-(Q+K*RK)` i ciągłe twierdzenie Lapunowa zapewniają stabilność zamkniętej pętli.
11. **Ciągła jednoznaczność.** Tożsamość kosztu dopełnienia kwadratu pozostaje prawdziwa dla hermitowskiego rozwiązania P_2 dowolnego znaku. Porównanie dwóch stabilizujących sprzężeń daje kolejno `P_1≥P_2` i `P_2≥P_1`, więc równość. Każde nieujemne rozwiązanie jest dodatnie: wektor w jądrze P przeczyłby ujemnej określoności prawej strony równania Lapunowa.
12. **Ciągły nieskończony horyzont.** Dla skończonego kosztu x,u są L²; równanie stanu daje x'∈L². Całkowanie pochodnej normy i Cauchy–Schwarz uzasadniają x(t)→0. Dopiero wtedy poprawne jest pominięcie warunku brzegowego przy T→∞.

## Rachunki przykładów

- DARE scalar: `8p²-p-7=0` daje p=1 i -7/8; sprzężenia odpowiednio K=1/4 i -7/2, z zamkniętymi mnożnikami 1/4 i 4. P_1=7/8, P_2=119/120.
- CARE scalar: `-2p-p²+3=0` daje p=1 i -3; zamknięte współczynniki odpowiednio -2 i 2. Jawne rozwiązanie `s(t)=3(1-e^{-4t})/(3+e^{-4t})` spełnia ODE i granicę 1.
- Przykład dwustanowy: dla CARE `A=diag(-1,-2),B=I,R=I,Q=diag(3,5)` rozwiązanie P=I; dla DARE `A=diag(1/2,1/3),B=I,R=I,Q=diag(7/8,17/18)` również P=I. Oba sprzężenia stabilizują układ.

## Język, odsyłacze i LaTeX

- 26 unikatowych etykiet i 31 odsyłaczy, w tym właściwe nazwy etykiet rozdziałów 22–23.
- 8 par środowisk proof; 4 twierdzenia, 4 definicje, 2 wnioski, 3 przykłady; brak terminów zabronionych w `AGENTS.md`.
- Dodano regresje bez zewnętrznych bibliotek `tools/test_linear_algebra_riccati.py`; w pierwszym przebiegu CI ukończyły się poprawnie. Ocena składu PDF zostanie odnotowana po zakończeniu budowania.

**Decyzja:** **Audyt II czysty matematycznie i redakcyjnie** po poprawkach z audytu I. Brak nowych zmian źródła; stabilność wymaga niezależnej iteracji i końcowej kontroli CI/PDF.
