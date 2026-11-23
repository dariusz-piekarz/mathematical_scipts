# Algebra abstrakcyjna — AA-X22: Frobenius nad ciałami skończonymi a typy cykli po redukcji (AA-29 × AA-35)

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **HEAD przed zapisem:** `722e853f3edf96557ac9cdf4a83c81414d892b0b`.

## Zakres i odrębność
Nowy audyt przekrojowy porównuje AA-29 (pierwiastki Frobeniusa, stopnie wielomianów nierozkładalnych i odwrócenie Möbiusa) z AA-35 (dobra redukcja i cykle Frobeniusa). Nie powtarza AA-X11 (AA-29 × AA-30) ani AA-X21 (prezentacje grup i algebry grupowe). Odczytano `AGENTS.md`, `docs/pl/standardy_terminologiczne.md`, `docs/pl/plan_algebry_abstrakcyjnej_aa43_plus.md`, `catalog/books.json`, listę 50 źródeł oraz istniejące raporty audytów. AA-51 nie występuje w katalogu źródeł.

## Kontrola matematyczna
1. AA-29, twierdzenie `aa:tw:finite-frobenius-roots`: dla monicznego nierozkładalnego `f` stopnia `d` nad `F_q` pierwiastki tworzą jedną orbitę `x -> x^q` długości `d`. Dowód wykorzystuje liczność `q^d`, minimalny okres oraz dzielenie z resztą. Zgadza się z AA-35, `aa:tw:frob-cycles`, gdzie różne czynniki dają rozłączne orbity.
2. AA-35 wymaga rozdzielczości redukcji (równoważnie `p` nie dzieli wyróżnika). To istotna hipoteza: dla `X^2-5` przy `p=2` otrzymujemy `(X+1)^2`, z czego nie wolno odczytać transpozycji. Przykład jest poprawny.
3. AA-35 nie zakłada nierozkładalności nad `Q`: przykład `(X^2-2)(X-3)` ma wyróżnik `392`; przy `p=5` występują stopnie `(2,1)`. Odpowiada to działaniu automorfizmu na dwóch pierwiastkach kwadratowych i jednym wymiernym.
4. Przykład `X^3-X-1` z AA-35: wyróżnik `-23`; przy `p=2` brak pierwiastków i typ `(3)`, przy `p=5` pierwiastek `2` i nierozkładalny czynnik kwadratowy, typ `(1,2)`; przy `p=23` pierwiastki `3,10` (drugi podwójny), redukcja zła; przy `p=59` trzy różne pierwiastki `4,13,42`, typ `(1,1,1)`. Niezależne sprawdzenie reszt potwierdziło te wartości.
5. Wzór AA-29 `N_q(n)=(1/n) sum_{d|n} mu(d) q^(n/d)` niezależnie sprawdzono przez wyliczenie **wszystkich monicznych wielomianów** nad `F_p` i test dzielników monicznych stopnia najwyżej `floor(n/2)`. Dla `p=2,3,5` oraz `n=1,2,3,4` otrzymano **12/12 zgodności**: `p=2: [2,1,2,3]`, `p=3: [3,3,8,18]`, `p=5: [5,10,40,150]`. Ten test nie stanowi dowodu ogólnego wzoru.
6. Sprawdzono wewnętrzne deklaracje etykiet i użycia `ref` w obu plikach: AA-29 ma 11 etykiet i 5 odsyłaczy, AA-35 ma 12 etykiet i 14 odsyłaczy; bez duplikatów etykiet w badanej parze. Odsyłacz `aa:tw:finite-frobenius-roots` z AA-35 prowadzi do AA-29. Pozostałych zewnętrznych celów nie certyfikowano w tym przebiegu globalnym skanem.

## Wynik i ograniczenia
**Matematyka w badanym interfejsie: bez wykrytej sprzeczności.** Niezależne obliczenia: **12/12** liczności wielomianów oraz kontrola czterech redukcji przykładu sześciennego. Nie jest to pełny audyt wszystkich dowodów 50 rozdziałów. Nie wprowadzono zmian do zatwierdzonych źródeł, etykiet ani odsyłaczy; licznik czystych audytów nie jest resetowany.

**LaTeX:** nowej kompilacji nie wykonano. **PDF:** nowej wizualnej inspekcji nie wykonano. **CI:** nowego przebiegu nie uruchomiono i nie deklaruje się PASS. Wynik matematyczny nie jest wynikiem kompilacji/CI.

**Status AA-X22:** opublikowany raport kontroli przekrojowej, bez ogłoszenia nowej stabilizacji całego tomu. **Następny krok:** ponowny odczyt HEAD i obecności AA-51; jeśli go brak, nowy, niepowtórzony audyt przekrojowy, z osobnym sprawdzeniem CI/PDF gdy możliwe.

## Niezależna stabilizacja AA-X22 — kontrola AA-29 × AA-32 × AA-35

W osobnej iteracji rozszerzono pierwotny audyt o AA-32 (wyróżnik i znak permutacji) oraz o niezależne obliczenia arytmetyczne, bez zmiany zatwierdzonych rozdziałów.

### 1. Twierdzenie: odzyskiwanie typów cykli przez NWD

Niech \(p\) będzie liczbą pierwszą, \(h\in\mathbb F_p[X]\) monicznym i rozdzielczym wielomianem stopnia \(n\ge1\) o rozkładzie \(h=\prod_i h_i\) na różne nierozkładalne czynniki stopni \(d_i\). Dla każdego \(k\ge1\) połóżmy
\[
F_h(k)=\deg\gcd(h,X^{p^k}-X).
\]
Jeśli \(m_d\) jest liczbą czynników stopnia \(d\), to
\[
F_h(k)=\sum_{d_i\mid k}d_i=\sum_{d\mid k}d\,m_d,
\qquad
m_k=\frac1k\sum_{d\mid k}\mu(k/d)F_h(d).
\]
**Dowód.** Wielomian \(X^{p^k}-X\) ma pochodną \(-1\), więc wszystkie jego pierwiastki są proste. Jego pierwiastki to punkty stałe \(k\)-tej iteracji Frobeniusa \(x\mapsto x^p\). Każdy nierozkładalny czynnik \(h_i\) daje z AA-29 orbitę długości \(d_i\), w całości stałą dla \(k\)-tej iteracji dokładnie wtedy, gdy \(d_i\mid k\); wnosi wówczas \(d_i\) pierwiastków. Rozdzielczość \(h\) pozwala sumować bez krotności, otrzymując wzór na NWD. Odwrócenie Möbiusa daje wzór na \(m_k\). Koniec dowodu.

Praktyczny sens: stopnie czynników odzyskujemy bez bezpośredniego rozkładu \(h\), używając jedynie potęgowania modulo \(h\) i NWD. Dla wielomianu z powtórzonymi czynnikami wzory nie odzyskują ich krotności i **nie** stanowią typu cykli z twierdzenia o dobrej redukcji.

### 2. Twierdzenie: symbol Legendre’a i znak Frobeniusa

Niech \(f\in\mathbb Z[X]\) będzie moniczny stopnia \(n\ge2\), z \(\operatorname{disc}(f)\ne0\). Niech \(p\) będzie **nieparzystą** liczbą pierwszą z \(p\nmid\operatorname{disc}(f)\), a \(\bar f\) niech ma \(s\) różnych monicznych nierozkładalnych czynników. Wtedy
\[
\left(\frac{\operatorname{disc}(f)}p\right)=(-1)^{n-s}.
\]
**Dowód.** W ciele rozkładu \(\bar f\) numerujemy \(n\) różnych pierwiastków \(\alpha_i\) i kładziemy \(\Delta=\prod_{i<j}(\alpha_i-\alpha_j)\ne0\). Dla Frobeniusa \(\sigma:z\mapsto z^p\), korzystając z naprzemienności Vandermonde’a, mamy \(\Delta^p=\sigma(\Delta)=\operatorname{sgn}(\sigma)\Delta\). Zatem \(\operatorname{sgn}(\sigma)=\Delta^{p-1}=(\Delta^2)^{(p-1)/2}=\operatorname{disc}(\bar f)^{(p-1)/2}\). W AA-35 znak ten to \((-1)^{n-s}\); na mocy kryterium Eulera ostatnia potęga jest symbolem Legendre’a. Wyróżnik redukuje się ze współczynników całkowitych, więc \(\operatorname{disc}(\bar f)=\overline{\operatorname{disc}(f)}\). Koniec dowodu.

Symbol Legendre’a w tej postaci nie ma sensu dla \(p=2\); w charakterystyce dwa nie można utożsamiać znaku permutacji z wartością \(\pm1\) w ciele. Znak cykli jako liczba całkowita pozostaje natomiast prawidłowy.

### 3. Nowe, trwałe regresje i wymagania końcowe

Dodano moduł tools/tests/test_abstract_algebra_cross_aa29_32_35.py, obejmujący **6 nowych testów unittest**:
1. dobra redukcja i bezkwadratowość nad ciałami skończonymi dla sześciu wielomianów i siedmiu liczb pierwszych;
2. niezależny od faktoryzacji algorytm \(F_h(k)\) przez potęgowanie i NWD oraz odwrócenie Möbiusa;
3. **pełna enumeracja** wszystkich monicznych wielomianów nad \(\mathbb F_2,\mathbb F_3,\mathbb F_5\) stopni \(1\)–\(4\) i liczby \(N_p(n)\);
4. cztery dokładne redukcje \(X^3-X-1\), w tym zła redukcja \(p=23\);
5. znak Frobeniusa kontra symbol Legendre’a dla sześciu wielomianów i ośmiu nieparzystych liczb pierwszych;
6. unikatowość etykiet i poprawność odsyłaczy na pełnym drzewie 50 rozdziałów.

Istotna granica przy \(p=23\): wielomian redukuje się do \((X-3)(X-10)^2\), więc lista stopni czynników **z krotnościami** to \((1,1,1)\), a lista stopni **różnych czynników** to \((1,1)\). Nie wolno utożsamiać żadnej z nich z typem cykli Frobeniusa po dobrej redukcji. Test rozróżnia obie sytuacje.

Bezpośredni odczyt AA-29, AA-32 i AA-35 wskazał odpowiednio 11, 9 i 12 etykiet (łącznie 32) oraz 5, 5 i 14 odsyłaczy (łącznie 24). Test weryfikuje obecność ich celów w pełnej książce i unikatowość etykiet, nie tylko w tej trójce.

Workflow .github/workflows/abstract-algebra-chapter.yml rozszerzono o wyzwalacz nowego pliku i krok Run AA-X22 Frobenius finite-field cycles and discriminant checks. **Przebieg uruchomiony:** [GitHub Actions 45229284139](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45229284139), commit 5c8ca7caf35f228df3eb518d9ae2e3a5e632096e.

**Status tej iteracji: w stabilizacji.** Pełne zamknięcie wymaga sześciu pozytywnych testów w logu, zakończonego sukcesem całego workflow, kompilacji AA-01–AA-50 i kontroli PDF/odsyłaczy. Nie wykonano niezależnego przeglądu wizualnego stron. Żadnego dodatku nie wstawiono do wcześniej zatwierdzonych rozdziałów; oba twierdzenia powyżej stanowią opcjonalną propozycję redakcyjną, nie konieczną poprawkę.
