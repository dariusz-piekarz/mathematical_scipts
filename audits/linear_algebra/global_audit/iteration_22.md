# Algebra liniowa — audyt globalny, iteracja 22: LA14–16, 42 indywidualne dowody

**Data:** 22 listopada 2026. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Kontynuacja:** [iteracja 21](iteration_21.md).

**Wynik przeglądu matematycznego: CZYSTY W BADANYM ZAKRESIE.** Przeczytano pełne sformułowania i wszystkie 42 dowody; nie znaleziono usterki wymagającej zmiany matematycznych źródeł LA14–16. Audyt rachunkowy i CI **nie są formalizacją Lean**.

## 1. Źródła, zakres i rejestr

| Rozdział | Blob SHA Git | Wiersze | Dowody | Etykiety | Odsyłacze | Przykłady | TikZ |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| LA14 — wartości własne i spektralne | `8216c60505324854e2339928bb9be562724e1db2` | 1691 | **17/17** | 43 | 22 | 10 | 0 |
| LA15 — rozkłady macierzy | `5a17f877bf3639cebc33ca95c202aca4498bd6c9` | 1787 | **13/13** | 40 | 22 | 7 | 0 |
| LA16 — podprzestrzenie niezmiennicze | `4f8da3c4b87b87ee8f8e6f7c7504637485c6e09a` | 887 | **12/12** | 30 | 17 | 5 | 0 |
| **Łącznie** | | **4365** | **42/42** | **113** | **61** | **22** | **0** |

[Per-dowodowy rejestr kontroli LA14–16](iteration_22_proof_review_14_16.csv) zawiera dla każdego twierdzenia etykietę, typ, zakres wierszy, identyfikator blob SHA źródła, informację o odczytaniu całej tezy i dowodu, osobną adnotację dotyczącą krytycznego kroku oraz `Lean_formalization_assessed_here=NIE`.

## 2. LA14: 17 dowodów

- **Wartości własne nad dowolnym ciałem:** niezmienniczość wielomianu charakterystycznego względem podobieństwa, niezerowy wymiar przestrzeni własnej dla wartości własnej, krotność geometryczna nieprzekraczająca algebraicznej, suma prosta przestrzeni własnych oraz kryterium diagonalizowalności wymagające **rozszczepienia wielomianu charakterystycznego nad K**. Szczególnie sprawdzono `n=0` i różnicę między diagonalizacją algebraiczną i unitarną.
- **Schur i normalność:** dowód indukcyjny Schura korzysta z kompresji `P_W T|_W`, **nie zakłada** niezmienniczości `W=e_1^⊥` dla dowolnego T. Normalność `T−λI` oraz relacja `Tv=λv => T*v=conj(λ)v` prowadzą do redukcji ortogonalnej i twierdzenia spektralnego. Skontrolowano sprzężenia zgodne z konwencją iloczynu skalarnego antyliniowego w pierwszym argumencie.
- **Rzeczywisty przypadek:** rzeczywista symetryczna A jest hermitowska po zespoleniu, ale uzyskanie rzeczywistego wektora własnego wymaga osobnego argumentu z `Re z`, `Im z`. Ograniczenie na `v^⊥` jest samosprzężone. Sprawdzono przykład macierzy hermitowskiej z pozornie kłopotliwymi współczynnikami zespolonymi.
- **Rzuty spektralne i funkcje operatora:** interpolacja Lagrange'a `P_j=∏_{k≠j}(T−λ_k I)/(λ_j−λ_k)`, zgodne wzory na `T,T*,p(T),tr T,det T,T⁻¹`, pusta suma dla `V={0}`. Iloraz Rayleigha ma ostre warunki równości; norma operatora normalnego to maksymalny moduł wartości własnej przy `V≠{0}`.
- **Jednoczesna diagonalizacja i triangularizacja:** przemienne samosprzężone redukują się na przestrzeniach własnych; przemienne algebraicznie diagonalizowalne macierze mają wspólną bazę własną bez normalności, co udowodniono przez wielomianowe rzuty. Dla dowolnej pary przemiennych zespolonych macierzy wyprowadzono wspólną flagę i ortonormalną bazę, dając unitarne postacie trójkątne. Kontrola kierunku `S=U* G_S U` jest zgodna z przyjętym `U=Q*`.

## 3. LA15: 13 dowodów

- **LU/LDU/PLU:** sprawdzono niezerowość wiodących minorów w jednoznacznym LU bez zamian wierszy oraz formułę `U_kk=Δ_k/Δ_{k−1}`; PLU obejmuje macierze osobliwe, w tym pierwszą zerową kolumnę, i poprawny czynnik `P' c a⁻¹`. Diagonalna macierz D w LDU jest odwracalna. Dopuszczono wymiary zerowe.
- **Cholesky/QR/Householder:** Schur `S=C−bb*/a` zachowuje dodatnią określoność; dodatnia rzeczywista przekątna L daje jedyność. QR obejmuje zależne kolumny przez dodatkowe ortogonalne wektory; jedyność znormalizowanego zredukowanego QR ograniczono do niezależnych kolumn. Odbicie `H_v=I−2vv*/(v*v)` jest samosprzężone i unitarne; przy zespolonym `x_1` zadano prawidłową fazę α unikającą zerowego v.
- **SVD i normy:** wyprowadzenie przez spektrum `A*A` obejmuje macierze prostokątne, osobliwe i puste, jednoznaczność wartości osobliwych, `im A`, `ker A`, normę operatorową i Frobeniusa.
- **Eckart–Young:** dolne oszacowanie operatorowe przez `span{v_1,...,v_{k+1}}∩ker B`, a dla normy Frobeniusa przez rzut na `im B`, Bessela i majorację sumy ważonej. Sprawdzono `k=0` i `k≥rank A`; nie zakłada się nieprawdziwej ogólnej jedyności najlepszego przybliżenia.
- **Pseudoodwrotność, pierwiastek i biegunowy:** cztery równania Penrose'a dają właściwe ortogonalne rzuty i jednoznaczną macierz `A+`; rozwiązanie o najmniejszej normie leży w `(ker A)^⊥`. Dodatni pierwiastek jest jedyny przez równoczesną diagonalizację; częściowa izometria `W` w `A=W|A|` ma `ker W=ker A` i rzutami są `W*W`, `WW*`.

## 4. LA16: 12 dowodów

- **Niezmienniczość:** jądra i obrazy `p(T)`, skończone sumy i przecięcia oraz iloraz przez podprzestrzeń niezmienniczą. Blok górnotrójkątny daje iloczyn wielomianów charakterystycznych ograniczenia i operatora ilorazowego. Przejrzano przykład nieistnienia niezmienniczego dopełnienia.
- **Przestrzenie cykliczne:** minimalny wielomian wektora ma stopień równy wymiarowi jego przestrzeni cyklicznej; kolejne potęgi tworzą bazę aż do pierwszej zależności. Wzór macierzy towarzyszącej poprawny dla `d=1,2` i ogólnie.
- **Wielomian minimalny i Cayley–Hamilton:** minimalność monicznego wielomianu zerującego, podzielność, najmniejsza wspólna wielokrotność na bazie i `n=0`. W dowodzie Cayleya–Hamiltona identyczność dla macierzy dołączonej stosowana jest nad **przemiennym pierścieniem K[t]**, a dalszy argument korzysta z porównania współczynników — nie z nieuprawnionego podstawienia macierzy do macierzowej tożsamości wielomianowej.
- **Rozkład pierwotny:** sprawdzono lemat Bézouta dla względnie pierwszych wielomianów, rozkład na jądra ich potęg i zachowanie składników przez T. Stabilizacja uogólnionych przestrzeni własnych wynika z odwracalności `T−λI` na komponencie towarzyszącym. Kryterium diagonalizacji `m_T` rozszczepiony na **różne czynniki liniowe** jest poprawne nad dowolnym ciałem, z pustym iloczynem dla `V=0`.

## 5. Niezależne testy i CI

Dodano [test LA14–16](../../../tools/test_linear_algebra_la14_la16_spectral_minpoly.py) do obowiązkowego workflow `.github/workflows/linear-algebra-chapter.yml` oraz do filtra ścieżek. Wykorzystuje dokładną arytmetykę małych ciał skończonych `F₂,F₃,F₅` oraz deterministyczne testy liczb zespolonych z NumPy (zależność instalowana przed krokiem). Nie używa wyników lub funkcji z matematycznych plików LaTeX.

**Zakres dokładny:** wyznaczniki wielomianowe, `χ_A(A)=0`, `m_A(A)=0`, `m_A|χ_A`, zgodność pierwiastków w K, kryterium diagonalizowalności, stabilizacja rozpiętości przestrzeni cyklicznej, również `n=0`. **Zakres numeryczny:** operator normalny i rzuty spektralne, interpolacja Lagrange'a, iloraz Rayleigha, jednoczesna diagonalizacja hermitowska i triangularizacja par przemiennych, SVD i liczba dodatnich wartości osobliwych, równania Penrose'a, ortogonalny rozkład biegunowy, równość błędów Eckarta–Younga, Cholesky, QR i równania normalne.

[GitHub Actions — kontrola LA14–16](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45067132900): nowy krok **„Verify LA14-LA16 finite minimal polynomials, normal operators and decompositions”** zakończył się `completed/success`. W chwili tej kontroli trwała jeszcze kompilacja PDF; pełny wynik przebiegu należy sprawdzić po zakończeniu. Zielony wynik testów nie stanowi certyfikatu Lean.

## 6. Redakcja, odsyłacze i dalszy plan

- 4365 wierszy, **113** etykiet (bez lokalnych duplikatów), **61** odsyłaczy, **42** sparowane środowiska `proof`, **22** przykłady. Nie wykryto lokalnych naruszeń zakazanych terminów. Rysunków w tych trzech rozdziałach nie ma, więc nie ma tutaj materiału TikZ do osobnej wizualnej kontroli.
- Źródeł matematycznych LA14–16 nie zmieniono; wcześniejszych stabilizacji rozdziałowych nie anulowano.
- **Po iteracji 22:** indywidualnie przeczytane w rejestrach 17–22 jest **250/382** dowodów, pozostało **132**: LA17–24 (**61**) i LA25–32 (**71**). Następnym etapem jest kontynuacja rejestru w LA17–24, a po domknięciu wszystkich 382 dowodów dodatkowa sceptyczna iteracja audytu końcowego, wraz z kontrolą PDF i odsyłaczy.
