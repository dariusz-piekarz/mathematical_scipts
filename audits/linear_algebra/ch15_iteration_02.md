# Algebra liniowa — rozdział 15, audyt II (niezależna kontrola stabilizacyjna)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Plik:** `chapters/pl/linear_algebra/15-rozklady-macierzy.tex`  
**Zbadany blob:** `119b00abd09ef761960560e5ee4c653a65c873a3`  
**Poprzedni raport:** `audits/linear_algebra/ch15_iteration_01.md`.

## Kontrola poprawności matematycznej i kompletności założeń

1. **LU, LDU i PLU.** Sprawdzono indukcję na dopełnieniu Schura, relację wiodących minorów `Δ_{j+1}=a det S_j`, wzór na pivots i jednoznaczność LU z jednostkową przekątną `L`. PLU jest dowiedzione także dla singularnych macierzy i zerowej pierwszej kolumny; permutacje niższego bloku są poprawnie wprowadzane do `P`. Nie przypisano PLU nieuzasadnionej jednoznaczności.
2. **Cholesky.** Dla hermitowskiej dodatnio określonej `H` skalar `a>0` i `S=C-bb*/a` jest dodatnio określony, bo `(-b*z/a,z)* H (-b*z/a,z)=z*Sz`. Czynniki `LL*=H` mają unikalną dodatnią przekątną. Przykład zespolony sprawdzono przez wymnożenie; nie przenosi się dodatniego diagonalu na macierze tylko półokreślone.
3. **QR i Householder.** Dla `m≥n` ortonormalną rodzinę `q_1,...,q_n` można skonstruować także dla zależnych kolumn, przez dobranie wektora prostopadłego, gdy reszta ortogonalizacji znika. `R=Q*A` jest górnotrójkątna z nieujemnym rzeczywistym diagonalem. Jednoznaczność wymaga pełnego rzędu kolumn i dodatniego diagonalu. Dla Householdera `H=I-2vv*/(v*v)` jest samosprzężoną inwolucją, a dobór `α` uwzględnia fazę zespoloną i przypadki `x_1=0` oraz `x` równoległego do `e_1`.
4. **SVD.** Dowód jest oparty na twierdzeniu spektralnym dla `A*A`; tylko dodatnie wartości `σ_i` służą do definiowania `u_i=Av_i/σ_i`. Uzupełnienie baz obejmuje macierze prostokątne, osobliwe, zerowe i o pustym wymiarze. Liczba dodatnich `σ_i` jest rzędem `A`; normy i podprzestrzenie jądra/obrazu są podane poprawnie.
5. **Twierdzenie Eckarta–Younga.** W normie operatorowej dolna granica `σ_{k+1}` wynika z niezerowego przecięcia `span(v_1,...,v_{k+1})∩ker B`. W normie Frobeniusa nierówność Bessela daje `Σ||P_{im B}u_i||²≤k`, a nierówność dla uporządkowanych wag `σ_i²` zapewnia optymalny błąd `sqrt(Σ_{i>k}σ_i²)`. Sprawdzono przypadki `k=0` i `k≥rank A`.
6. **Pseudoodwrotność Moore’a–Penrose’a.** Cztery tożsamości wyznaczają samosprzężone projekcje `AX=P_im A` oraz `XA=P_(ker A)^perp`. Dla każdego `y`, `Xy` jest jedynym minimizerem normy wśród rozwiązań najmniejszych kwadratów. To dowodzi jednoznaczności `A+` i niezależności od baz SVD. Przykład rzędu jeden daje prawidłową macierz `A+=1/10[[1,2],[1,2]]`.
7. **Rozkład biegunowy.** Dodatni pierwiastek `(A*A)^(1/2)` jest jednoznaczny przez jednoczesną diagonalizację przemiennych macierzy samosprzężonych. Kanoniczna częściowa izometria `W` spełnia `A=W|A|`, `W*W=P_(ker A)^perp`, `WW*=P_im A`, `ker W=ker A`. Unikalność kanonicznego `W` odróżniono od niejednoznaczności unitarnych rozszerzeń przy singularnym kwadratowym `A`.
8. **Kwantyfikatory i terminologia.** Oddzielono wyniki nad dowolnym ciałem od twierdzeń wymagających `R` lub `C`, a przypadki macierzy zerowych/pustych od norm wymagających `σ_1`. Nie znaleziono braku założeń ani błędnego rozumowania kołowego.

## Testy, struktura i wygląd PDF

W rozdziale 15 znajduje się **1782 wierszy, 40 etykiet, 22 odsyłacze**. W całej książce 01–15 jest **614 różnych etykiet i 267 odsyłaczy do istniejących celów**, bez otwartych środowisk.

Pierwszy przebieg regresji: **761** przypadków PLU, **481** Choleskiego, **522** QR z kolumnami niezależnymi i **17** konfiguracji SVD/pseudoodwrotności/rozkładu biegunowego. W audycie II wykryto lukę w **testach**, a nie w matematycznym twierdzeniu QR: brak sprawdzenia zależnych kolumn. Dodano przypadki zależne, w tym zespolony przykład `a_2=i a_1`, do `tools/test_linear_algebra_decompositions.py`; nowy test regresyjny przeszedł w CI.

Zweryfikowano w obrazach wszystkie **14 stron** osobnego PDF rozdziału 15 z GitHub Actions; nie stwierdzono uciętych wzorów ani kolizji tekstu. W [Actions 44929624956](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44929624956) pełna książka została skompilowana poprawnie i wygenerowano artefakt `linear-algebra-current-chapter`. Zaktualizowane testy QR przeszły w [Actions 44929984597](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44929984597); status końcowy tego i następnego przebiegu CI należy sprawdzić osobno.

## Decyzja

**Audyt II — czysty matematycznie i typograficznie.** Poprawiono wyłącznie pokrycie testów przypadkiem niepełnego rzędu. Tekst rozdziału 15 oraz rozdziałów 01–14 pozostał niezmieniony. Na podstawie dwóch audytów i udanej kompilacji **rozdział 15 uznano za stabilny**. Kolejnym przedmiotem prac jest rozdział 16 zgodnie z planem.

**Zasada prezentacji:** użytkownik otrzymuje tylko PDF aktualnie audytowanego rozdziału; GitHub Actions nadal kompiluje pełny tom w celu sprawdzenia odsyłaczy i spójności.
