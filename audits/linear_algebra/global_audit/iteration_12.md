# Algebra liniowa — audyt globalny, iteracja 12 (dowody LA07 i LA09–11)

**Data:** 2026-11-22. **Repozytorium:** `dariusz-piekarz/mathematical_scipts`; gałąź `biblioteka-matematyczna-iteracja-6`.
**Stan wejściowy:** globalna iteracja 11 wykryła i poprawiła rzeczywistą usterkę parowania permutacji w LA08 oraz zamknęła powtórną stabilizację tego rozdziału. **Ta iteracja nie wznawia stabilnej sekwencji LA12–32.**
**Wynik bieżący:** **CZYSTY w zbadanym zakresie; nie wprowadzono zmian matematycznych ani redakcyjnych do źródeł.** Pozostaje globalna kontrola dowodów w dalszych rozdziałach.

## Kontrolowane źródła i SHA

| Rozdział | Blob na aktualnej gałęzi | Wiersze | Środowiska `proof` | Etykiety | Odsyłacze `ref/eqref` |
|---|---|---:|---:|---:|---:|
| 07 — Przestrzeń dualna i odwzorowania dualne | `5e320759f55012f807be790214d6ad76119ab544` | 1264 | 20 | 45 | 15 |
| 09 — Formy dwuliniowe i kwadratowe | `979ce687c677125aeb8304e9d13cb8e7af842602` | 1349 | 14 | 36 | 15 |
| 10 — Iloczyny tensorowe | `9c397a15f5f668e84cb68681e00bf0305cf73adf` | 1434 | 20 | 41 | 14 |
| 11 — Algebry tensorowa, symetryczna i zewnętrzna | `17f1bae2db46ac6790f1fc562660393f2f616076` | 1630 | 19 | 42 | 27 |

**Łącznie:** 5677 wierszy, **73 środowiska `proof`**, 164 etykiety i 71 odsyłaczy. Przeanalizowano treści rozdziałów, w szczególności wszystkie poniżej wymienione kluczowe dowody i ich zależności; liczenie wszystkich 73 środowisk nie jest deklaracją niezależnego, formalnego sprawdzenia każdego kroku każdego dowodu. Wszystkie cztery bloby pozostały niezmienione między odczytem źródeł, regresją i odczytem na przetestowanym commicie.

## Rozdział 07 — kontrola matematyczna

1. **Definicje, bazy i konwencje:** dla `V^*=Hom_K(V,K)` funkcjonały bazowe określają bazę `V^*` także dla `dim V=0`. Wzór `[v]_B=P[v]_C` daje `[φ]_{C^*}=P^T[φ]_{B^*}` i `w^j=Σ_i(P^{-1})_{ji}v^i`. Rozróżniono macierz zmiany bazy od jej odwrotności oraz współrzędne wektorów od funkcjonałów.
2. **Anihilatory:** `dim U^∘=n−dim U` wynika z bazy uzupełnionej; `(U^∘)_∘=U` i `(S_∘)^∘=S` wymagają wymiaru skończonego. W drugim dowodzie funkcja `L:V→K^s` jest surjektywna z niezależności bazowych funkcjonałów. Formuła `(U_1∩U_2)^∘=U_1^∘+U_2^∘` wynika z prawidłowej inkluzji i wzoru na wymiar przecięcia.
3. **Dualne odwzorowanie i iloraz:** `q^*:(V/U)^*→V^*` ma obraz `U^∘` i jest iniektywne. Dla `T:V→W`, `ker T^*=(im T)^∘` oraz `im T^*=(ker T)^∘`; odwrotną inkluzję uzasadnia funkcjonał `λ(Tv)=φ(v)`, dobrze określony przez wyzerowanie `ker T`, i jego przedłużenie. Rząd macierzy i transpozycji jest taki sam nad dowolnym ciałem.
4. **Bidualność i ślad:** `J_V:V→V^{**}` jest naturalne przez ewaluację, a `T^{**}J_V=J_WT` sprawdza się na wszystkich elementach `W^*`. `tr(AB)=tr(BA)` zachodzi dzięki przemienności skalarów, a dla `R_{v,φ}(x)=φ(x)v` mamy `tr R_{v,φ}=φ(v)` także w wymiarze zero. Nie utożsamiono arbitralnie `V` z `V^*`.

## Rozdział 09 — kontrola matematyczna

1. **Ortogonalność i radykał:** dla symetrycznej (także zdegenerowanej) formy `b` wzór `dim U^{⊥_b}=n−dim U+dim(U∩Rad(b))` pochodzi z rzędu pary sprzężonych odwzorowań `V→U^*`, `U→V^*`. Warunek `b|_{U×U}` niezdegenerowany wystarcza do `V=U⊕U^{⊥_b}`, bez nieuzasadnionego wymagania, aby całe `b` było niezdegenerowane.
2. **Polaryzacja i charakterystyka:** `q(v)=b_q(v,v)/2` jest używane tylko przy `char K≠2`. W `char K=2` polaryzacja formy `x_1x_2+x_1²` ignoruje składnik kwadratowy `x_1²`, co nie uprawnia do utożsamiania form z tym samym `b_q`.
3. **Diagonalizacja i Sylvester:** dla symetrycznej `b≠0` nad `char K≠2` istnienie `w` o `b(w,w)≠0` wynika z polaryzacji `2b(u,v)`; indukcja rozkłada przestrzeń na nieosobliwą prostą i jej dopełnienie. W prawie bezwładności `p` i `m` są maksymalnymi wymiarami podprzestrzeni odpowiednio dodatnich i ujemnych, zaś `z=n−p−m`; dowód nie używa nieudowodnionej klasyfikacji spektralnej.
4. **Wiodące minory:** indukcyjny dowód kryterium dodatniej określoności wykorzystuje dodatni pierwszy pivot oraz dopełnienie Schura `S=C−rr^T/a`. Wiodące minory `S` są dodatnie z tożsamości `Δ_{j+1}=a det S_j`. Przypadek `n=0` jest jawny.
5. **Formy naprzemienne w `char K=2`:** wybór `u,v` z `a(u,v)=1` daje niedegenerowany blok `J=[[0,1],[-1,0]]`. Wzory `x_U=a(x,v)u−a(x,u)v` i `x_⊥=x−x_U` poprawnie dają rozkład bez dzielenia przez `2`; rząd formy pozostaje parzysty.

## Rozdział 10 — kontrola matematyczna

1. **Konstrukcja i własność uniwersalna:** `V⊗W=K^{(V×W)}/N`, gdzie `N` narzuca cztery relacje dwuliniowości. Dobre określenie faktoryzacji przez `N` jest jawnie uzasadnione; jednoznaczność realizacji wynika z dwóch wzajemnie odwrotnych odwzorowań indukowanych przez własność uniwersalną.
2. **Baza i rząd tensora:** rodzina `v_i⊗w_j` jest liniowo niezależna dzięki funkcjonałom `v^p⊗w^q`; minimalna liczba tensorów prostych równa się rzędowi macierzy współczynników. Wymiar `0` jest objęty twierdzeniami.
3. **Odzworowania i Kronecker:** macierz `S⊗T` w leksykograficznych bazach jest `A⊗B`. Rząd wynosi `rk A × rk B`, również dla macierzy prostokątnych i zerowych wymiarów.
4. **Naturalne izomorfizmy:** zamiana i łączność czynników oraz rozdzielanie sumy prostej są przeprowadzone przez universal property, a nie przez nieuprawnione utożsamianie różnych przestrzeni. Równości weryfikuje się najpierw na tensorach prostych.
5. **`W⊗V^*→Hom(V,W)`:** tensor skończony daje skończony rząd; każdy operator o skończonym rzędzie ma rozkład na proste składniki; iniektywność wynika z niezależności wybranych `w_i`. Surjektywność do wszystkich operatorów jest poprawnie ograniczona do skończenie wymiarowego `V`.
6. **Dokładność i ślad:** dla `U⊂V` rozkład algebraiczny `V=U⊕H` daje dokładny ciąg `0→U⊗W→V⊗W→(V/U)⊗W→0`, bez założenia na wymiary. Kanoniczna kontrakcja `V⊗V^*→K` przechodzi na `tr T` przez `Θ^{-1}(T)` tylko przy skończonym wymiarze `V`.

## Rozdział 11 — kontrola matematyczna

1. **Ilorazy i charakterystyka:** algebra tensorowa `T(V)` jest nieujemnie stopniowana. Ideały relacji przemienności (`u⊗v−v⊗u`) oraz naprzemienności (`v⊗v`) są jednorodne; dzięki temu `S(V)` i `Λ(V)` są dobrze określone nad każdym ciałem, także w `char K=2`. Kwadrat generatora, a nie samo `u⊗v+v⊗u`, musi być zerowany w definicji algebry zewnętrznej.
2. **Bazy:** baza jednomianów `S^k(V)` jest wykazana przez homomorfizm do algebry wielomianów. Baza `Λ^k(V)` jest wykazana przez formy determinantowe `D_I`, które rozdzielają proponowane generatory, także dla `k>n`, `n=0`.
3. **Minory i Cauchy–Binet:** współczynnik `e_I` przy `v_1∧⋯∧v_k` jest wyznacznikiem minora; z `Λ^k(AB)=Λ^k AΛ^k B` wynika Cauchy–Binet bez założenia na charakterystykę. Przy `k=0` strony są `1_K`; przy `k>dim` przestrzeń zewnętrzna jest zerowa.
4. **Formy naprzemienne i przetasowania:** `(Λ^k V)^*≅Alt^k(V^*)` wynika z właściwej uniwersalności; w skończonym wymiarze wyznaczniki wartości funkcjonałów bazowych realizują `Λ^k V^*≅Alt^k(V^*)`. Wzór z przetasowaniami pochodzi z Laplace'a bez czynnika `p!q!`.
5. **Symetryzatory i antysymetryzatory:** z prawidłowego działania `P_σ P_τ=P_{στ}` wynika `S_k²=k! S_k` i `A_k²=k! A_k`. Znormalizowane operatory są rzutowaniami tylko gdy `k!1_K≠0_K`; konstrukcje ilorazowe pozostają bezwarunkowe. Zwrócono uwagę na znaki i parowanie przy równych czynnikach po historycznej korekcie LA08.

## Rzeczywiście wykonana nowa regresja obliczeniowa

W bieżącej iteracji utworzono i wykonano **`/mnt/data/la_global12_tests.py`** (Python, własna implementacja redukcji macierzy nad ciałami skończonymi; SymPy użyty dla dokładnych symetrycznych dodatnich macierzy). Losowania mają ustalony seed `202611221752`; nie importowano implementacji testów z repozytorium.

| Blok testów | Liczba PASS |
|---|---:|
| Rząd odwzorowania dualnego i anihilator | 1125 |
| Aihilator przecięcia — tożsamości wymiarów | 900 |
| Kongruencja form i jednorodność formy kwadratowej | 6000 |
| Kryterium Sylvestera, dokładne dodatnie macierze | 500 |
| Rząd macierzy Kroneckera | 3840 |
| Granice rzędu tensora prostego | 3000 |
| Cauchy–Binet (w tym `k=0`, puste sumy i char. 2) | 5700 |
| Łączność iloczynu zewnętrznego | 5250 |
| Kwadrat wektora w algebrze zewnętrznej | 5250 |
| Superprzemienność iloczynu zewnętrznego | 5250 |
| Wzór z przetasowaniami i minory | 2160 |
| Relacje `S_k²=k!S_k`, `A_k²=k!A_k` | 720 |
| **Łącznie** | **39 695/39 695 PASS, 0 FAIL** |

**Ograniczenia testów:** przykłady obliczeniowe nie dowodzą twierdzeń w pełnej ogólności i nie obejmują wszystkich przestrzeni nieskończenie wymiarowych. Niezależna analiza dowodów stanowi osobną podstawę oceny.

## Spójność techniczna, CI i stan aktualności

- Wszystkie cztery pliki mają prawidłowo zagnieżdżone i zamknięte środowiska LaTeX. Ich SHA zweryfikowano zarówno w aktualnym drzewie GitHub, jak i odczytując je z dokładnego commitu `d6e8db9bf7eecfe8ba9fff8a2783cb34968d8a78`, sprawdzonego w [GitHub Actions 45047361654](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45047361654): **completed/success**. Wszystkie cztery bloby są identyczne w przetestowanym commicie i bieżącej gałęzi.
- W tej iteracji **nie zmieniono źródłowych rozdziałów**. Pełny PDF po korekcie LA08 miał 319 stron i został wygenerowany w iteracji 11. **Nie wykonywano nowej osobnej wizualnej kontroli stron 07, 09–11** w bieżącej iteracji, dlatego nie przypisuje się jej jako nowego wyniku.

## Wnioski i następny etap

**ITERACJA 12 CZYSTA w podanym zakresie.** Potwierdzono poprawność najistotniejszych argumentów dla odwzorowań dualnych, form kwadratowych, iloczynów tensorowych i algebry zewnętrznej; nie wykryto koniecznych poprawek. Historyczne audyty rozdziałowe i iteracja 11 pozostają odrębne. Nie należy fałszywie przenosić ich liczników czystych kontroli do nowej globalnej sekwencji.

**Audyt globalny matematyczny nadal OTWARTY**, ponieważ nie poddano nowej niezależnej, wyczerpującej formalnej kontroli każdego z 382 dowodów całej książki. Następna iteracja powinna przejść do krytycznych zależności LA14–20: twierdzenia spektralnego, Cayleya–Hamiltona, postaci Jordana, rozkładu Jordana–Chevalleya, postaci Frobeniusa i rozkładu pierwotnego. Ukończona stabilizacja LA12–32 pozostaje zamknięta, dopóki nie pojawi się konkretna nowa usterka.
