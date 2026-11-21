# Topologia algebraiczna — TOP-28: audyty I–V

**Data:** 21 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6` (bez modyfikowania `main`).  
**Rozdział:** `chapters/pl/algebraic_topology/28-topologia-gladkich-zespolonych-odmian-projektowych-twierdzenia.tex`.  
**Końcowy blob źródła:** `b0dbd26f8414a39d021bebfb2dfc98b8bdbb60fb`.  
**Moduły współdzielone, sprawdzone i zachowane bez kopiowania:** `shared/pl/slabe_twierdzenie_lefschetza.tex`, `shared/pl/rozdmuchanie_punktu_normalna.tex`, `shared/pl/rozdmuchanie_punktu_kohomologia.tex`.

Zakres zgodny ze standardem DG-01: weryfikacja istniejącej treści, samodzielność sformułowań, kompletność istotnych uzasadnień, poprawność rachunków i przykładów, terminologia, odsyłacze, LaTeX, rysunki i CI. Nie dodawano żadnych nowych twierdzeń, lematów ani przykładów.

## Audyt I — operator Lefschetza i lemat liniowoalgebraiczny

- W definicji klasy hiperpłaszczyzny dopisano jawnie `X⊂P^N_C`, założenia gładkości, spójności i wymiar.
- W Lemacie `lem:xvii-sl2` ustalono stopniowanie `V=⊕_{k=0}^{2n}V^k`, ortogonalność stopni, formy adjunktów `Λ=L*` i konwencję `V^j=0` poza zakresami. Bez tego równość adjunkcji i stopniowania nie była jawna.
- Rozpisano indukcję komutatorową `ΛL^rv=r(n-k-r+1)L^{r-1}v` od przypadku `r=1` do `r+1`, wskazując dokładnie udział równości `[Λ,L]L^rv=(n-k-2r)L^rv`.
- Uściślono wyprowadzenie izomorfizmu `L^{n-k}:V^k→V^{2n-k}` na każdym łańcuchu pierwotnym, zamiast skrótowego „obracania” łańcuchów.
- Rozróżniono ujemną określoność na prymitywnej rzeczywistej części typu `(1,1)` od dodatnich kierunków `(2,0)+(0,2)`.

Commit `18c5380f6a94626f78471e4e605a54e2044741cd`.

## Audyt II — samodzielność sformułowań

- W silnym twierdzeniu Lefschetza określono zanurzenie projektowe, klasę `h=c1(O_X(1))` i wszystkie stopnie.
- Wniosek o liczbach Bettiego otrzymał kwantyfikatory `0≤k≤2n`, `j≥0` oraz definicję `b_{2j+1}`.
- Definicja kohomologii prymitywnej, twierdzenie o rozkładzie Lefschetza oraz relacje Hodge'a–Riemanna otrzymały samodzielnie określone `X,n,L,ω,k,p,q`.
- W twierdzeniu Hodge'a o indeksie zdefiniowano dodatnią/ujemną sygnaturę `b_2^±` oraz liczby Hodge'a `h^{p,q}`.
- W ogólnym wzorze na całkowitą kohomologię rozdmuchania dopisano kwantyfikator `k∈Z`; zachowano istniejący pełny argument przez kohomologię par, homomorfizm Gysina i klasę tautologiczną.

Commit `d043cf6d8d61bcb73b8299cd76376bf25a4d37d9`.

## Audyt III — relacje Hodge'a–Riemanna i klasa kanoniczna

- W samodzielnej tezie Hodge'a–Riemanna określono `P^k(X;C)=ker L^{n-k+1}`, także dla ogólnej zwartej rozmaitości Kählerowskiej.
- Jawnie wskazano orientację zespoloną przy formie przecięcia.
- W twierdzeniu o klasie kanonicznej rozdmuchania zapisano `p∈S`, `E=π^{-1}(p)`, holomorficzną wiązkę kanoniczną i sens `K_S^2`.
- W dowodzie `K_{Bl_pS}^2=K_S^2-1` dopisano precyzyjny odsyłacz do **wcześniej istniejącego, wspólnego** Twierdzenia `thm:xvii-blowup`; wyjaśniono osobno `π^*c1(K_S)·e=0`, `e^2=-1` i zachowanie samoprzecięcia przez morfizm stopnia 1.
- Uporządkowano terminologię map współrzędnych.

Commit `2aa81b7dc265a7c85142fa30f908d53000f72d89`.

## Audyt IV — regresje i niezależne rachunki

Dopisano regresje obecności hipotez i uzasadnień oraz testy rzeczywistych operatorów `sl2` na łańcuchach Lefschetza. Dla `0≤n<20`, `0≤m≤n`, `0≤r≤n-m` sprawdzono **1540** trójek przy użyciu postaci ortonormalnej
`L e_r=√((r+1)(n-m-r)) e_{r+1}`, `Λ=L^*` i różnicy kwadratów współczynników. Każdorazowo odzyskano `[Λ,L]e_r=(n-m-2r)e_r` i zgodny indeks stopnia symetrycznego.

Zachowano wcześniejsze regresje całkowitej formuły rozdmuchania i przykładu krzywej eliptycznej w `P^3`. Dołożono rzeczywiste testy form przecięcia `diag(1,-1)` dla `Bl_pP^2` i `[[0,1],[1,0]]` dla `P^1×P^1`; wykazano dodatni, ujemny i ortogonalny kierunek (zamiast testować tautologiczną równość). Dla krzywej rodzaju `g` zweryfikowano wzór liczbowy `χ=6-2g`; w przypadku eliptycznym wynik to `4`.

Commity testów `7819c7dbc338794564b8b3a45a862dedb61d059f`, `1c52fe552a1ccd5051cbd1b77f5892af3d536104`.

## Audyt V — końcowe doprecyzowania i zgodność tekstu

- Wiązkę kanoniczną powierzchni zapisano jednoznacznie jako holomorficzną `K_S=∧²Ω_S¹=Ω_S²`, a nie nieokreśloną gładką wiązkę kowektorów.
- Doprecyzowano współczynniki `b_2`, `χ_top`, `σ` w przykładzie rozdmuchania `P²` i jawnie podano, skąd `χ=4`.
- Kontrola rysunku i tekstu ujawniła `Mapy π i p` użyte w znaczeniu odwzorowań: poprawiono na `Odwzorowania π i p`, zachowując `mapa` dla chart.
- Zauważono merytoryczną nieścisłość: **względne silne twierdzenie Lefschetza w używanej wersji wymaga morfizmu projektowego**, nie dowolnego właściwego. Poprawiono tezę przeglądową i dopisano regresję chroniącą to założenie.
- Po ostatnim przebiegu nie zgłoszono nowych zmian matematycznych; istniejące głębokie wyniki (Bertini, geometryczne Lefschetz, tożsamości Kählerowskie, Hodge–Riemann, Gysin i Leray–Hirsch) pozostają jawnie wskazanymi zależnościami, zgodnie ze standardem.

Commity źródła `4c58d2c431d6999840a0a49d4eb02be98d462d46`, `a90304a84f0e63f97617aad20271bc096cd03026`, `7c5a21ea3564e63949dc7aa64c8e48e1dc7b2b13`; końcowa regresja `7c0f12b91bce21753e085a71ad68f5061ee75998`.

## Kontrola strukturalna i PDF

- Rozdział TOP-28 oraz trzy moduły współdzielone: **16 unikatowych etykiet**, 11 odwołań `\ref`; wszystkie cele są lokalne lub rozwiązywane przez poprzednie rozdziały. W tych czterech plikach 8 twierdzeń, 2 lematy, 1 wniosek, 4 definicje, 9 przykładów, 11 dowodów; liczniki `begin/end` zgodne.
- Dwa diagramy TikZ: geometria dzielnika wyjątkowego i przesunięcia Gysina. Wszystkie strony (w tym rysunki i podpisy) obejrzano wizualnie; bez nakładających się napisów.
- Cała książka (28 rozdziałów) w zweryfikowanym przebiegu pdfLaTeX — **309 stron A4**; TOP-28 to strony 300–309, wyodrębnione do **10-stronicowego PDF**. Po ostatnich poprawkach terminologicznych i projektywności należy pobrać ponownie artefakt z właściwego przebiegu, aby zachować zgodność PDF z końcowym blobem.

## GitHub Actions — status wymagający potwierdzenia

- [TOP-27/28: sukces kompilacji](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44946746180) dla źródła przed wyłącznie końcowymi poprawkami.
- [TOP-27/28: końcowy przebieg po poprawkach źródła i testów](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44947025662) — wynik do odczytania.
- [Ogólne kontrole aplikacji po końcowych testach](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44947025671) — wynik do odczytania.
- [Międzytomowy audyt po zmianie wzmianki o względnym Lefschetzu](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44947010738) — wynik do odczytania.

**Status redakcyjno-matematyczny:** TOP-28 po audytach I–V stabilny; formalne zamknięcie wymaga potwierdzenia końcowego CI, a PDF powinien pochodzić z tego samego końcowego bloba źródła. Następny w kolejności TOP-29.
