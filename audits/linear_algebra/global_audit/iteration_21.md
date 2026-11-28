# Algebra liniowa — audyt globalny, iteracja 21: LA09–11, 53 indywidualne dowody

**Data:** 22 listopada 2026. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Poprzednio:** [iteracja 20](iteration_20.md).
**Decyzja:** **CZYSTY W BADANYM ZAKRESIE** — przeczytano pełne tezy i wszystkie 53 dowody, bez wykrycia koniecznych zmian w matematycznych źródłach. Indywidualny przegląd nie jest weryfikacją Lean.

## 1. Źródła i struktura

| Rozdział | Blob SHA Git | Wiersze | Pełne dowody | Etykiety | Odsyłacze | Przykłady | Rysunki TikZ |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| LA09 — formy dwuliniowe i kwadratowe | `979ce687c677125aeb8304e9d13cb8e7af842602` | 1349 | **14/14** | 36 | 15 | 7 | 1 |
| LA10 — iloczyny tensorowe | `9c397a15f5f668e84cb68681e00bf0305cf73adf` | 1434 | **20/20** | 41 | 14 | 5 | 1 |
| LA11 — algebry tensorowa, symetryczna i zewnętrzna | `17f1bae2db46ac6790f1fc562660393f2f616076` | 1630 | **19/19** | 42 | 27 | 6 | 2 |
| **Suma** | | **4413** | **53/53** | **119** | **56** | **18** | **4** |

[Rejestr 53 indywidualnych kontroli](iteration_21_proof_review_09_11.csv) dokumentuje dla każdego dowodu etykietę, pełną tezę przeczytaną razem z argumentem, przedział wierszy, identyfikator konkretnej wersji źródła, uwagę o matematycznie trudnym kroku i brak certyfikacji Lean. Wszystkie 53 środowiska `proof` są poprawnie domknięte, bez powtórzonych etykiet w tych trzech plikach.

## 2. LA09 — 14 dowodów, kontrola matematyczna

- **Ortogonalia dla form zdegenerowanych:** formuła `dim U^⊥ = dim V − dim U + dim(U∩Rad b)` została sprawdzona w rozumowaniu przez dwa odwzorowania liniowe i jednakowy rząd odwzorowania dualnego; nie zastępowano jej niepoprawnym wzorem obowiązującym tylko przy niezdegenerowanej formie. Rozkład `V=U⊕U^⊥` wymaga **niezdegenerowania ograniczenia b na U**, a nie całego V. Sprawdzono przykład z radykałem rozpiętym przez `e3`.
- **Formy kwadratowe:** definicja działa w każdej charakterystyce, lecz relacja `q(v)=1/2 b_q(v,v)` i diagonalizacja form symetrycznych wymagają `char K≠2`. Kontrolowano odzyskiwanie współczynników `a_i,c_ij`, także nad ciałem skończonym, a w `F₂` dwie różne formy o identycznej polaryzacji.
- **Prawo bezwładności Sylvestera:** wykazano, że `p,m` są maksymalnymi wymiarami dodatniej i ujemnej podprzestrzeni, a nie jedynie liczbą symboli w arbitralnej diagonalizacji. Również `z=n−p−m` oraz kryterium dodatniej określoności są poprawne.
- **Kryterium Sylvestera:** kontrola wiodących minorów, redukcji do dopełnienia Schura `S=C−rrᵀ/a`, indukcji i przypadku `n=0`. Zależności wyników z LA06/LA08 są prawidłowe.
- **Cauchy–Schwarz, Gram–Schmidt i rzut:** sprawdzono założenie dodatniej określoności, przypadki wektora zerowego i pustej rodziny, znikanie składników mieszanych oraz jedyne najlepsze przybliżenie.
- **Forma naprzemienna:** konstrukcja kolejnego bloku `J=[[0,1],[-1,0]]` prowadzi do rzędu parzystego **także w charakterystyce 2**; dowód nie dzieli przez 2 i nie zakłada symetrii w tej charakterystyce. Przejrzano odpowiadające przykłady.

## 3. LA10 — 20 dowodów, kontrola matematyczna

- **Istnienie i uniwersalność:** konstrukcja `K^(V×W)/N` poprawnie narzuca relacje dwuliniowości; odwzorowanie indukowane jest dobrze określone, a obrazy tensorów prostych rozpinają przestrzeń. Dla dowolnej innej realizacji rozpiętość wynika z jednoznaczności map do `T/S`.
- **Baza i rząd tensora:** dualne współrzędne bazowe rozdzielają `v_i⊗w_j`; rozmiary `0×m` są uwzględnione. Minimalna liczba tensorów prostych równa się rzędowi macierzy współczynników, a nie liczbie niezerowych wyrazów danego przedstawienia.
- **Mapy i operacje:** sprawdzono `S⊗T`, odwrotność tensorowego izomorfizmu, matrycę Kroneckera i kolejność jej indeksów, `rk(A⊗B)=rk(A)rk(B)`, zamianę czynników i kanoniczną łączność bez utożsamiania dosłownie różnych nawiasowań.
- **Linearyzacja:** dowód dla `k` czynników poprawnie przeprowadza uniwersalność indukcyjnie. Izomorfizm `(V⊗W)^*≅Hom(V,W^*)` nie wymaga wymiaru skończonego, podczas gdy `V^*⊗W^*≅(V⊗W)^*` ma go jako jawne założenie.
- **Iloczyn tensorowy, ilorazy i `Θ`:** opis skończenierzędowych odwzorowań przez `W⊗V^*` i identyfikacja kontrakcji ze śladem są poprawne. W dowodzie dokładności `U⊗W→V⊗W→(V/U)⊗W` użyto dopełnienia algebraicznego; w **nieskończonym wymiarze** wybór tego dopełnienia jest oparty na AC, a nie na niejawnej redukcji do wymiaru skończonego. Kanoniczny izomorfizm ilorazu nie zależy od wybranego dopełnienia.

## 4. LA11 — 19 dowodów, kontrola matematyczna

- **Algebra tensorowa i symetryczna:** sprawdzono poprawność ideałów dwustronnych, ich jednorodność, mnożenie klas, własności uniwersalne oraz bazę jednomianów symetrycznych przez odwzorowanie do `K[x_1,...,x_n]`. Liczenie `dim S^k(V)=binom(n+k−1,k)` nie wymaga dzielenia przez `k!` i obowiązuje w dodatniej charakterystyce.
- **Algebra zewnętrzna:** istotna relacja to `v∧v=0`, również gdy `char K=2`. Reguła znaków dla homogenicznych elementów jest zgodna z `(-1)^(pq)`. Własność uniwersalna `Λ^k(V)` dla form naprzemiennych wynika z zanikania na elementach ideału, a niezależność bazowych wielowektorów została uzasadniona funkcjonałami wyznacznikowymi.
- **Minory, Cauchy–Binet i wyznacznik:** macierz `Λ^kA` ma wyrazy równe minorom `A[I,J]`; przy `k=0` odpowiednie potęgi i wyznaczniki są równe jednostce, przy `k>dim` występują przestrzenie zerowe. Potwierdzono współczynniki z przykładów.
- **Formy i iloczyny:** izomorfizmy `(Λ^kV)^*≅Alt^k(V^*)` i `Λ^k(V^*)≅Alt^k(V^*)` (drugi przy wymiarze skończonym) są zgodne z konwencją wyznacznikową; w formule z **przetasowaniami** nie pojawia się dodatkowy czynnik `p!q!`. Sprawdzono przypadki `p=0` lub `q=0`.
- **Symetryzatory:** operator `P_σ` używa `σ⁻¹`, co daje właściwy kierunek kompozycji. `S_k²=k! S_k`, `A_k²=k! A_k` mają sens nad każdym ciałem, natomiast znormalizowane rzutowania oraz ich identyfikacje z ilorazami **wyłącznie gdy `k!1_K≠0_K`**. Udokumentowano to także przy sprawdzaniu charakterystyki 2.

## 5. Test regresyjny i CI

Nowy test: [tools/test_linear_algebra_la09_la11_exhaustive.py](../../../tools/test_linear_algebra_la09_la11_exhaustive.py), załączony do `.github/workflows/linear-algebra-chapter.yml` i filtra ścieżek. Używa jedynie standardowej biblioteki Pythona, bez NumPy i bez losowania.

**Wynik: 260 514 / 260 514 PASS, 0 FAIL.** Sprawdza wyczerpująco wybrane małe macierze i podprzestrzenie nad `F₂,F₃,F₅`: wzór na wymiar ortogonalnego dopełnienia **z radykałem** oraz `U^{⊥⊥}=U+Rad(b)` dla symetrycznych form w wymiarach do 3; polaryzację form kwadratowych również w charakterystyce 2; parzystość rzędu form naprzemiennych w wymiarze do 4; rangę, transpozycję i mieszany iloczyn Kroneckera; liczbę bazowych potęg symetrycznych i zewnętrznych oraz łączność i regułę znaków iloczynu zewnętrznego.

**[Przebieg CI 45066516139](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45066516139): `completed/success` dla CAŁEGO przebiegu** na commicie `ba000d4b26903a226d14143c049df34ea7cad18e`. Z osobnej kontroli logu wynika, że nowy krok **„Verify LA09-LA11 quadratic, tensor, exterior identities over finite fields”** otrzymał **`completed/success`, 260 514 / 260 514 PASS**, SHA256 skryptu **`5f0a41f1350c91a582e26042bec4f3981e52cd614c393676a6185a5603e88a28`**. Weryfikacja kroków tego samego przebiegu potwierdziła także **`completed/success` dwukrotnej kompilacji PDF i kontroli nierozwiązanych odsyłaczy**. Zielony test nie jest certyfikacją matematyczną w Lean.

## 6. LaTeX, terminologia, przykłady, rysunki

- **4413** wierszy, **119** różnych etykiet bez lokalnych duplikatów, **56** odsyłaczy, **53** dobrze domknięte środowiska `proof`, **18** przykładów. Analiza terminologiczna nie wykazała niechcianego angielskiego rzeczownika `dual`, słowa `unia` w prozie ani zakazanego terminu `tensorowanie`.
- Źródła **4** rysunków TikZ sprawdzono pod względem etykiet i opisanych tożsamości: elipsa dodatnio określona (LA09), diagram uniwersalny iloczynu tensorowego (LA10), diagram uniwersalny zewnętrznej potęgi i równoległobok o wyznaczniku `5` (LA11). **Nie wykonano nowej wizualnej inspekcji wyrenderowanych stron PDF.**
- Zbadano rachunki w przykładach szczególnie narażonych na pomyłki: charakterystyka 2, usuwanie mieszanego wyrazu, minory Cauchy’ego–Bineta, matryca Kroneckera, iloczyn zewnętrzny nieprostego dwuwektora i suma po przetasowaniach. Bez matematycznych poprawek w źródłach.

## 7. Status i dalsze działania

Po iteracjach 17–21 w nowym rejestrze skontrolowano indywidualnie **208/382** środowisk dowodowych (LA01–13, lecz LA12–13 wykonano wcześniej niż LA09–11). **Pozostały 174 dowody:** LA14–16 (**42**), LA17–24 (**61**), LA25–32 (**71**). Wcześniejszych audytów rozdziałowych nie anulowano, a źródła LA09–11 pozostały bez zmian.

**Następnie:** LA14–16 (wartości własne, diagonalizacja, rozkłady, podprzestrzenie niezmiennicze) i dopiero po domknięciu pełnej ewidencji dodatkowy sceptyczny audyt końcowy.
