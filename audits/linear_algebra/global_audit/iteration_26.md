# Algebra liniowa — audyt globalny, iteracja 26: LA27–28, 20 indywidualnych dowodów

**Data:** 22 listopada 2026. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Kontynuacja:** [iteracja 25](iteration_25.md).

**Wynik audytu dowodów: CZYSTY W BADANYM ZAKRESIE.** Przeczytano pełne sformułowania i dowody wszystkich **20 twierdzeń, lematów, stwierdzeń i wniosków** w LA27 i LA28. Sprawdzono 6 przykładów. Nie stwierdzono błędów wymagających ingerencji w dowody. Wprowadzone poprawki dotyczą **dwóch niesamodzielnych tez** i **pięciu sformułowań terminologicznych**, nie zmieniając rachunków. Ani testy liczbowe, ani lektura dowodu nie stanowią formalnej certyfikacji Lean.

## 1. Wersje źródeł i integralność

| Rozdział | Ostateczny blob SHA | Wiersze | Dowody | Etykiety | Odsyłacze | Przykłady | Rysunki |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| LA27 — gramiany i realizacje minimalne | `becc4603ed2b4c6518f76f76ff96500688d869d6` | **1670** | **10/10** | 32 | 32 | 3 | 0 |
| LA28 — wymuszenie i funkcje przejścia | `e4b593387748da071a2d415277ec46b6703d11d4` | **669** | **10/10** | 36 | 31 | 3 | 0 |
| **Razem** | | **2339** | **20/20** | **68** | **63** | **6** | **0** |

**[Rejestr 20 indywidualnych kontroli](iteration_26_proof_review_27_28.csv)** zawiera dla każdej pozycji dokładny SHA, wiersze tezy i dowodu, osobną adnotację o krytycznym argumencie i status `Lean_formalization_assessed=NIE`. Wszystkie środowiska dowodu są poprawnie domknięte, nie ma lokalnych duplikatów etykiet ani wskazanych naruszeń zakazanej terminologii. W kontrolowanych rozdziałach nie występują rysunki, więc nie było wizualnych wykresów do inspekcji; nie oglądano osobno gotowych stron PDF.

## 2. LA27 — 10 dowodów, 3 przykłady

- **Obserwacje i gramiany:** dla `N≥n` jądro `W_o,N=O_N* O_N` jest dokładnie `N(C,A)` z Cayleya–Hamiltona, a `O_N* Y=W_o,N x0` pozwala odtworzyć stan. W czasie ciągłym tożsamość `∫₀ᵀ ||Ce^{tA}x||² dt=0` prowadzi do tej samej przestrzeni nieobserwowalnej dla każdego `T>0`, ponieważ funkcja analityczna ma wszystkie pochodne w 0 równe zeru.
- **Gramiany nieskończone:** rozkład Jordana i stabilność Schura/Hurwitza zapewniają bezwzględną zbieżność sum i całek, a telescoping/różniczkowanie prowadzą do właściwych równań Steina/Lapunowa. Dodatnia określoność odpowiada odpowiednio sterowalności i obserwowalności; w dowodach nie wymuszono, by Q w tych równaniach był dodatnio określony, jeżeli B lub C są osobliwe.
- **Parametry Markowa i redukcja:** `H_k=CA^kB` koduje splot wyjściowy zarówno w czasie dyskretnym, jak i ciągłym. Iloraz `V_min=R/(R∩N)` jest poprawnie zdefiniowany dzięki A-niezmienniczości obu przestrzeni; jego operator A_min, wejście B_min i wyjście C_min są dobrze określone i dają identyczne H_k. Przypadek zerowego wymiaru odpowiada zerowej funkcji wejście–wyjście.
- **Rząd macierzy Hankela:** `H_n,n=O_n K_n`, stąd `rank H_n,n=dim R−dim(R∩N)`. Jeśli inna realizacja ma wymiar q, faktoryzacja tej samej H przez jej O_n i K_n daje `q≥rank H`. Realizacja minimalna jest więc dokładnie sterowalna i obserwowalna. Sprawdzono również realizację `n=0`, gdzie H musi być zerowa.
- **Jednoznaczność minimalna:** podobieństwo między dwiema realizacjami z tymi samymi H_k definiuje się na wszystkich wektorach osiągalnych; jego dobre określenie wymaga obserwowalności drugiej realizacji. Wykazano relacje `TA₁=A₂T`, `TB₁=B₂`, `C₂T=C₁` i odwracalność T, również z osobną obsługą wymiaru zerowego.
- **Współrzędne zrównoważone:** `L=W_c^{1/2}`, `L W_o L=U Σ² U*`, `T=L U Σ^{−1/2}` prowadzą do `W'_c=W'_o=Σ`. Inwariantność σ_j² wynika z podobieństwa produktów W_cW_o, nie z bezpodstawnej unitarnej podobności gramianów. Rozwiązanie LS `x̂=(O*O)^{-1}O*Y` i oszacowanie błędu przez `1/sqrt(λ_min(O*O))` uzasadniono rzutem ortogonalnym.
- **Przykłady:** obliczenie `T⁴/12` dla ciągłego gramianu obserwacyjnego 2×2, realizacja minimalna o jednym stanie dla modelu trójwymiarowego z niewidocznymi składnikami, a także dokładne skalowanie gramianów diagonalnych przy zmianie bazy T.

## 3. LA28 — 10 dowodów, 3 przykłady

- **Wariacja stałych:** przy ciągłym wejściu dowód z `v=e^{−tA}x` i reguły Leibniza daje istnienie, jednoznaczność i wyjście `Cx+Du`. W wersji dyskretnej poprawne przesunięcie indeksu prowadzi do `x_k=A^kx0+Σ A^{k−1−j}Bu_j`, z pustą sumą dla k=0.
- **Impuls i splot:** bezpośredni współczynnik `h_0=D` w czasie dyskretnym i `h_k=CA^{k−1}B` dla k≥1, a w czasie ciągłym `h(t)=Ce^{tA}B`. Zbadano, czy definicje transmitancji są zgodne z tymi przesunięciami.
- **Laplace i Z:** zwarty nośnik wejścia oraz oszacowanie `||e^{tA}||≤e^{t||A||}` pozwalają całkować przez części przy dostatecznie dużej Re s. W transformacie Z przy x0=0 prawidłowo mamy `Σ_{k≥0} x_{k+1}z^{−k}=zX(z)`. Rozwinięcie `(zI−A)^{-1}=Σ A^j z^{−j−1}` daje współczynniki Laurenta równe H_j.
- **Wymierność i realizacja towarzysząca:** stopień elementów `adj(zI−A)` jest najwyżej n−1, więc G jest właściwa, a bieguny mogą pojawiać się tylko wśród wartości własnych A. Macierz companion z jedynkami na nadprzekątnej ma wektor własny `(1,z,…,z^{n−1})` dla p(z)=0, jest sterowalna dla B=e_n i obserwowalna dokładnie przy `gcd(p,q)=1`. Ujęto przypadki n=1 i q=0.
- **Ograniczone wejście:** dla Hurwitza norma `e^{tA}` zanika jak `Me^{−αt}`, więc odpowiedź jest ograniczona przez początkowy składnik zanikający i stałą `||D||+M||C||||B||/α` razy normę wejścia L∞. Dla Schura analogicznie działa suma geometryczna `1/(1−r)`. Nie mylono stabilności wejście–wyjście ze stabilnością ukrytych nieobserwowalnych stanów.
- **Przykłady:** wymuszenie stałe w jednowymiarowym `A=−2`, nieobserwowalny niestabilny stan A=diag(1,−1) z transmitancją `1/(z+1)` i prawidłowa realizacja funkcji `(2s+3)/(s²+3s+2)` wraz z odpowiedzią impulsową i skokową.

## 4. Poprawki źródeł

- **LA27:** w tezie `thm:lin27-hankel-rank` zapisano pełne `n,m,p≥1` i wymiary A,B,C oraz użyto tytułu **„Rząd macierzy Hankela i minimalność”** zamiast „Ranga”. Commit `4bdb58d544fc6ac4d80e8212eeeeea9be94675b7`. W czterech dodatkowych miejscach prozy zamieniono „ranga/rangi” na „rząd/rzędu”, commit `29aaa8c950023163490a5d8dafe4441a2698f683`.
- **LA28:** w `thm:lin28-variation` wprowadzono pełne `n,m,p≥1` oraz wymiary A,B,C,D, commit `8609badd5e1e7673181fc6f46f041270650452cc`. Jedno wystąpienie „rangi” zastąpiono „rzędu”, commit `817e90c82388160253cbc4f8b99a81cc6e570986`. Numery etykiet oraz wszystkie dowody pozostawiono.

## 5. Niezależny test i pełny CI

Nowy [test LA27–28](../../../tools/test_linear_algebra_la27_la28_realizations.py) w `.github/workflows/linear-algebra-chapter.yml` i filtrze ścieżek sprawdza wyczerpująco wszystkie pary A,B,C nad F₂/F₃ dla `n=2` i pojedynczego wejścia/wyjścia. Weryfikuje niezależnie rangę Hankela przez faktoryzację oraz liczbę różnych obserwacji na zbiorze osiągalnym (wymiar ilorazu). Deterministyczne testy zespolone liczą oba gramiany Steina, zmianę współrzędnych i ich jednoczesne równoważenie, estymację najmniejszych kwadratów z zakłóceniem, funkcję przejścia przez Laurent/resolwentę, realizację towarzyszącą, skokowy splot i znikanie niewidocznego bieguna.

**Zweryfikowany [CI 45070553933](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45070553933): `completed/success` całego workflow** na commicie `4a17676a790536c3df9dfcf8ab4c77fba70fe225`. Z oryginalnego logu: **27 259 / 27 259 PASS**, 0 FAIL, SHA256 skryptu **`5b9f989505e6eba19de1d17ab90a09488a8b31a5c1c906e917db0c5fbd660563`**. Potwierdzono sukces dwukrotnej kompilacji książki PDF, sprawdzenia nierozwiązanych odsyłaczy i eksportu osobnego rozdziału. Następne przebiegi obejmujące **dwie poprawki źródeł i terminologię** należy zweryfikować osobno przed stwierdzeniem, że właśnie te wersje źródła przeszły cały workflow.

## 6. Postęp globalny

Po iteracjach 17–26 indywidualnie przejrzano **357/382** dowodów. Pozostało **25**: LA29 Grassmanniany (**6**), LA30 algebry Clifforda (**3**), LA31 Pin/Spin i spinory (**6**), LA32 twistory (**10**). Po domknięciu całego rejestru wymagany jest dodatkowy sceptyczny audyt globalny, obejmujący także realną inspekcję wyrenderowanego PDF.
