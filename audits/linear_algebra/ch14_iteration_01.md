# Algebra liniowa — rozdział 14, audyt I

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/linear_algebra/14-wartosci-wlasne-diagonalizacja-i-twierdzenie-spektralne.tex`  
**Wersja oceniana (blob):** `09fda2f083ad5fbd752699606d42862eb7022987`

## Zakres, motywacja i zależności

Rozdział 14 „Wartości własne, diagonalizacja i twierdzenie spektralne” jest kontynuacją rozdziałów 12–13 (iloczyny skalarne, bazy ortonormalne, adjoint, rzuty), ale wprowadza wartości własne od podstaw, bez zakładania wcześniejszej teorii spektralnej. Wykorzystuje już zaudytowane twierdzenia `thm:lin12-gram-schmidt`, `thm:lin12-zmiana-ortonormalna` (w tekście poprawne rzeczywiste oznaczenie `prop:lin12-zmiana-ortonormalna`), `thm:lin13-adjoint`, `prop:lin13-adjoint-kalkul`, `thm:lin13-rzut-wlasnosci`. Przedstawienie rzeczywistych form symetrycznych jest zgodne z rozdziałem 09, ale nie powtarza tamtego dowodu prawa bezwładności.

Rozdział zawiera: wartości i przestrzenie własne, wielomian charakterystyczny, krotności algebraiczne i geometryczne, niezależność przestrzeni własnych, diagonalizację algebraiczną, twierdzenie Schura, operator normalny, twierdzenie spektralne nad `C`, rzeczywisty wariant dla operatorów symetrycznych, rzuty spektralne i wielomiany operatorów, iloraz Rayleigha, określoność form, normę operatora normalnego i jednoczesną diagonalizację przemiennych operatorów samosprzężonych.

## Kontrola matematyczna — punkty krytyczne

1. **Definicje i przypadki zerowe:** wartości własne wymagają wektora niezerowego; w wymiarze 0 wielomian charakterystyczny ma wartość 1, a spektrum jest puste. Te konwencje są stosowane konsekwentnie, także w pustych sumach rzutów.
2. **Niezależność bazy wielomianu charakterystycznego:** podobieństwo `P^{-1}AP` daje niezmienniczość wyznacznika `det(tI-A)`. Moniczność i stopień `n` wynikają bezpośrednio z rozwinięcia wyznacznika.
3. **Krotności:** wybór bazy przestrzeni własnej oraz uzupełnienie jej do bazy `V` daje górnoblokowo-trójkątną postać operatora i czynnik `(t-λ)^g` wielomianu charakterystycznego, stąd `1≤g≤a`.
4. **Niezależność przestrzeni własnych:** operator `∏_{j≠k}(T-λ_j I)` zeruje wszystkie składowe poza jedną; różnice różnych wartości własnych są niezerowymi skalarami w ciele, więc suma przestrzeni własnych jest bezpośrednia.
5. **Diagonalizowalność:** kryteria `V=⊕ E_λ`, `Σ g_λ=n` i pełne rozszczepienie wielomianu z równością krotności algebraicznych i geometrycznych są równoważne. Kontrprzykład bloku Jordana `[[1,1],[0,1]]` jest poprawny nad dowolnym ciałem.
6. **Schur:** istnienie zespolonego pierwiastka wielomianu charakterystycznego zapewnia zasadnicze twierdzenie algebry; normalizacja wektora własnego i indukcja stosowana do kompresji `P_{e_1^⊥}T|_{e_1^⊥}` dają macierz górnotrójkątną bez fałszywego założenia, że `e_1^⊥` jest niezmiennicza dla ogólnego `T`.
7. **Normalność i wektor własny sprzężenia:** dla normalnego `N` zachodzi `||Nv||=||N^*v||`. Operator `N=T-λI` pozostaje normalny, zatem `Tv=λv` implikuje `T^*v=conj(λ)v` bez wykorzystywania twierdzenia spektralnego.
8. **Twierdzenie spektralne nad `C`:** z wektora własnego operatora normalnego powstaje wspólna niezmiennicza redukcja `V=Ce_1⊕e_1^⊥` dla `T` i `T^*`; ograniczenie jest normalne i indukcja działa. Odwrotność `U^*AU=D ⇒ T` normalny wynika z przemienności diagonalnych `D`, `D^*`.
9. **Samosprzężoność i unitarność:** z `h(v,Tv)=h(Tv,v)` przy `T=T^*` wynika rzeczywistość wartości własnych; izometria normy daje `|λ|=1` dla operatora unitarnego. Nie pomylono wymagań dla operatora normalnego i samosprzężonego.
10. **Przypadek rzeczywisty:** kompleksyfikacja macierzy rzeczywistej symetrycznej jest hermitowska; jej wartości własne są rzeczywiste. Część rzeczywista albo urojona niezerowego wektora zespolonego dostarcza niezerowego rzeczywistego wektora własnego, a rzeczywiste dopełnienie ortogonalne jest niezmiennicze; indukcja nie wymaga rzeczywistej wersji zasadniczego twierdzenia algebry. Kontrprzykład rzeczywistej rotacji ma `t²+1` i nie jest diagonalizowalny nad `R`.
11. **Rzuty spektralne:** przy parami różnych `λ_j` wyrażenie `∏_{k≠j}(T-λ_k I)/(λ_j-λ_k)` działa jak identyczność na `E_{λ_j}` i zero na pozostałych; dzięki ortogonalnemu rozkładowi jest dokładnie `P_j`. Suma rzutów jest `I`, ich wzajemne iloczyny są zerowe i `T=Σ λ_jP_j`.
12. **Rachunek wielomianowy:** dla normalnego `T`, `p(T)=Σ p(λ)P_λ`. Ślad i wyznacznik są sumą oraz iloczynem wartości własnych z wymiarami przestrzeni własnych. Puste sumy/iloczyny odpowiadają wymiarowi zero.
13. **Rayleigh i określoność:** liczba `h(v,Tv)/h(v,v)` jest ważoną średnią rzeczywistych wartości własnych, stąd znajduje się między ich minimum i maksimum; warunki równości udowodniono przez nieujemne składniki. Forma hermitowska `h(u,Tv)` jest dodatnio określona dokładnie przy dodatnich wszystkich wartościach własnych.
14. **Jednoczesna diagonalizacja:** dla `ST=TS`, drugi operator zachowuje każdą przestrzeń własną pierwszego; jego ograniczenie pozostaje samosprzężone. W każdej przestrzeni własnej wybieramy własną bazę ortonormalną i łączymy bazy ortogonalnych składników. Uwzględniono wielokrotne wartości własne pierwszego operatora.

## Testy i struktura

- Nowy rozdział: **1455 wierszy**, **39 etykiet**, **22 odsyłacze**.
- Kontrola statyczna całej książki 01–14: **574 różne etykiety**, **245 odsyłaczy do istniejących etykiet**, zrównoważone środowiska, brak niedozwolonej terminologii.
- `tools/test_linear_algebra_spectral.py`: niezależne obliczenia dla macierzy normalnych będących unitarnymi podobieństwami diagonalnych, rzutów spektralnych, wielomianów operatora, ilorazu Rayleigha, macierzy hermitowskich i przemiennych oraz kontrprzykładu nie-normalnego.
- Rozdział jest dopisany w `books/pl/linear_algebra.tex` i `catalog/books.json`; dedykowany CI sprawdza 14 rozdziałów.
- Końcowy status CI dokumentujemy dopiero po ukończeniu kompilacji; testy matematyczne regresji już zaliczyły przebieg.

## Wynik

**Audyt I — brak znalezionych problemów matematycznych w przeanalizowanych punktach.** Rozdział pozostaje otwarty do audytu II i weryfikacji PDF; nie ogłaszamy stabilizacji przed niezależnym drugim sprawdzeniem.
