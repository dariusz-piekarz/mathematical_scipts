# Algebra liniowa — rozdział 23, audyt IV (stabilizacyjny)

**Data:** 21 listopada 2026  
**Źródło:** `chapters/pl/linear_algebra/23-dyskretne-rownanie-lapunowa-i-stabilnosc-schura.tex`  
**Kontrolowany blob:** `8939984648cdd1c38ee57702b3b11ff38d9a4238`  
**Audyty:** I i II wykryły dwie konieczne poprawki dotyczące konwencji potęgowania przy zerze; III czysty, niniejszy IV również czysty.

## Powtórna kontrola matematyczna

1. **Twierdzenie o potęgach:** w przypadku pojedynczego bloku Jordana rozwinięcie dwumianowe ma poprawny zakres indeksów `0≤j≤min(k,d−1)`. Osobno omówiono `λ=0`, `k=0`, `d=1`; nie pozostaje nieoznaczone `0^0`. Wzór oszacowania z `(1+k)^(d−1)(δ/r)^k` jest prawidłowy, a przejście przez podobieństwo daje oszacowanie normy całej macierzy.
2. **Twierdzenie Lapunowa:** `ρ(A)<1` wymusza zbieżność bezwzględną szeregu `P=Σ(A*)^kQA^k`; pierwszy składnik `Q` uzasadnia ścisłą dodatnią określoność, także dla osobliwej macierzy `A`. Jednoznaczność rozwiązania jest wykazana w pełnej przestrzeni, nie tylko wśród macierzy hermitowskich. Warunek konieczny wynika ze ścisłej ujemności \((|λ|^2-1)v^*Pv\).
3. **Energia:** przy `x_k≠0` jest ścisły spadek, a dla `x_k=0` energia pozostaje zerowa. Stałe `q_min,p_min,p_max` istnieją z twierdzenia spektralnego. Połączenie `P-Q=A*PA≥0` i oszacowania od dołu `Q` względem `P` daje `0≤γ<1`, niezależne od stanu początkowego.
4. **Widmo operatora Steina:** unitarne podobieństwo do górnotrójkątnej macierzy `T` i obliczenie `T*E_ijT` dają `χ_(T_A)=∏_(i,j)(t-conj(λ_i)λ_j)`, z krotnościami. Kryterium `conj(λ_i)λ_j≠1` jest konieczne i wystarczające do jednoznaczności rozwiązania dla wszystkich `Q`, bez dodatniej określoności.
5. **Niestabilne kontrprzykłady:** dla `diag(2,1/3)` istnieje dokładnie jedno rozwiązanie przy każdym `Q`, lecz `P` dla `Q=I` ma ujemną wartość diagonalną. Dla `diag(2,1/2)` otrzymujemy rodzinę rozwiązań z wolnymi wpisami pozadiagonalnymi i brak dodatnio określonego rozwiązania.
6. **Przykład nie-normalny:** dla `A=[[1/2,1/2],[0,1/4]]`, `Q=I`, obliczona macierz `P=[[4/3,8/21],[8/21,32/21]]` spełnia równanie; rozwinięcie `4/3|x+2y/7|²+208|y|²/147` potwierdza dodatnią określoność nad \(\mathbb C\). Kontrola ułamków daje `det P=832/441`.
7. **Połączenie z czasem ciągłym:** dla dowolnego \(h>0\) wartości własne \(e^{hH}\) są równe \(e^{hλ}\) i leżą w kole jednostkowym dokładnie przy \(\operatorname{Re}λ<0\). Dla jawnego Eulera warunek \(|1+hλ|<1\) jest równoważny \(2\operatorname{Re}λ+h|λ|²<0\). Przykład skalarnej macierzy \(H=-2\) poprawnie rozróżnia graniczny krok \(h=1\) i niestabilny \(h=3/2\).

## Kontrola techniczna i PDF

- **25 unikatowych etykiet**, **12 odsyłaczy**, **7 par środowiska `proof`**, zachowana globalna terminologia.
- Regresja `tools/test_linear_algebra_discrete_lyapunov.py` przeszła jako krok [GitHub Actions 44946101921](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44946101921) — **SUCCESS**. Sprawdzono rangi operatorów Steina nad \(\mathbb F_2\), \(\mathbb F_3\), arytmetykę dokładną przykładów i tożsamość energii.
- Ten sam przebieg CI potwierdził dwukrotną kompilację LaTeX, brak ostrzeżeń `Overfull`, `Underfull`, niezdefiniowanych odsyłaczy i błędów, a także poprawny eksport PDF aktualnego rozdziału.
- Samodzielny PDF rozdziału 23 ma **8 stron**, wszystkie **8 niepustych**. PyMuPDF nie znalazł żadnego bloku tekstowego poza stroną. Wyrenderowano i obejrzano układ wszystkich ośmiu stron; nie widać uciętych wzorów, kolizji ani błędnej paginacji.
- W niniejszym audycie nie zmieniono źródła rozdziału 23.

## Decyzja

**Audyt IV czysty**: druga kolejna pełna iteracja bez nowych poprawek po audycie II. **Rozdział 23 STABILNY po czterech audytach**, sprawdzonych testach, zielonym CI i odrębnym PDF. Rozdziały 01–23 algebry liniowej pozostają stabilne; następny etap: osobna decyzja o zakresie rozdziału 24, bez modyfikowania zatwierdzonej treści.

**Propozycja do osobnej decyzji:** równanie macierzowe Riccatiego, dyskretna i ciągła wersja, może stanowić naturalne rozszerzenie teorii Lapunowa w zastosowaniach do sterowania. Nie włączono jej do rozdziału 23.
