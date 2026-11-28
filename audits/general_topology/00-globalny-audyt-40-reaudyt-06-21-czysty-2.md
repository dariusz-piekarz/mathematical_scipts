# Topologia ogólna — audyt globalny 40: druga czysta kontrola rozdziałów 06 i 21 po korekcie rysunków

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Badane niezmienione bloby:** rozdział 06 `71d7b30abb97286b7c64ddd5e369ec9f69ea1ff5`; rozdział 21 `eae0bef9c2357189e1bdb7c9398b845fe7347c7b`.
**Pierwszy czysty audyt nowych blobów:** raport globalny 39. **Metoda drugiego audytu:** sprawdzono przypadki graniczne, obie implikacje, użycia zwartości, kierunki odsyłaczy i nazwy wszystkich **33** środowisk `proof`, a także cały przepływ argumentów między rozdziałami.

## 1. Rozdział 06 — wszystkie 18 pozycji proof

| Etykieta | Niezależny kierunek kontroli |
|---|---|
| `prop:topog-ciag-baza` | Każde otoczenie zawiera element bazy, a warunek ostatecznej przynależności do elementów bazy daje warunek dla wszystkich otoczeń |
| `prop:topog-ciag-metryka` | Kule metryczne stanowią bazę otoczeń; `∀ε>0` zachowuje właściwą kolejność kwantyfikatorów |
| `prop:topog-ciag-podciag-ciaglosc` | Nierówność `n_k≥k` gwarantuje wspólną kontrolę ogonów; obrazy ciągów wymagają ciągłości w granicy, nie globalnej |
| `thm:topog-ciag-hausdorff` | Rozłączne otoczenia różnych granic przeczyłyby istnieniu wspólnego wyrazu dostatecznie daleko |
| `prop:topog-ciagi-domkniecie` | Stałe ciągi pokazują `A⊆scl A`, a każdy otwarty zbiór zawierający granicę spotyka A |
| `thm:topog-pierwsza-przeliczalnosc-domkniecie` | Malejąca baza `W_n` i świadkowie `A∩W_n` dają ciąg bez użycia T1 |
| `thm:topog-ciagowe-kryterium-ciaglosci` | Negacja ciągłości w x dostarcza świadków poza przeciwobrazem jednego otoczenia f(x) |
| `prop:topog-siec-ciaglosc-jeden-kierunek` | Ciągłość w x wystarcza do zbieżności sieci obrazowej w f(x) |
| `thm:topog-siec-domkniecie` | Indeksy `(U,a)` tworzą zbiór skierowany, a malejące U zapewniają zbieżność niezależnie od wyboru reprezentantów |
| `thm:topog-siec-kryterium-ciaglosci` | Sieć w dopełnieniu `f⁻¹(V)` neguje ciągłość punktową, jeśli wszystkie sieci zbieżne mają obrazy zbieżne |
| `thm:topog-sieci-hausdorff` | Przy braku T2 trójki `(U,V,z)` produkują sieć z dwiema granicami bez pozornego założenia pierwszego aksjomatu przeliczalności |
| `prop:topog-podsiec-granica` | Ostateczna współkońcowość `φ`, a nie tylko obraz φ kofinalny jako zbiór, pozwala przenosić ogony |
| `thm:topog-punkt-skupienia-podsiec` | Z punktu skupienia powstaje skierowany zbiór `(d,U)` oraz ostatecznie współkońcowa mapa φ; konwersja działa także dla przedporządków |
| `thm:topog-siec-iloczyn` | Tylko skończenie wiele współrzędnych wymaga wspólnego ograniczenia górnego; dla pustego indeksu produkt to singleton |
| `def:topog-filtr` (nazwane `proof`) | Baza filtru jest niepusta, skierowana przez przecięcia i składa się z niepustych podzbiorów; uzasadnienie nie należy do twierdzenia o iloczynie |
| `thm:topog-filtr-domkniecie` | Filtr generowany przez `A∩U` jest właściwy; w drugą stronę niepustość `A∩U` wynika z właściwości filtra |
| `thm:topog-sieci-filtry` | Filtr ogonów i sieć `(F,a)` dają obie strony równoważności; kluczowy wybór wszystkich `(F,b)` wymusza `F⊆U` |
| `cor:topog-filtr-ciaglosc-hausdorff` | `V∈f_*𝔽 ⇔ f⁻¹(V)∈𝔽`; charakterystyka T2 wynika z niemożności jednoczesnej przynależności rozłącznych otoczeń do filtra |

**Przypadki graniczne:** przestrzeń pusta nie posiada właściwego filtra; zbiory skierowane w rozdziale są niepuste; przestrzenie niedające jednoznacznej granicy nie są błędnie traktowane jako T2; topologia koprzeliczalna nie wymaga przeliczalnej bazy otoczeń. **18/18 — brak nowej uwagi merytorycznej.**

## 2. Rozdział 21 — wszystkie 15 pozycji proof

| Etykieta | Niezależny kierunek kontroli |
|---|---|
| `prop:topog21-vietoris-basis` | Jedna konstrukcja `⟨V,V∩W₁,...,V∩W_s⟩` obejmuje dowolne skończone przecięcia warunków dolnych i górnych, w tym s=0 |
| `prop:topog21-singletons` | Oba przeciwobrazy podbazowe są równe U; dla T2 singletony tworzą zbiór domknięty w hiperprzestrzeni |
| `thm:topog21-vietoris-separation` | Z `x∈A\B` i zwartości B otrzymuje się otwarte rozłączne U i V, a stąd rozłączne `U⁻` oraz `V⁺` |
| `prop:topog21-induced` | Dwa przeciwobrazy podbazowych warunków trafienia i zawierania są dokładnie obrazami odwrotnymi otwartych w Y |
| `thm:topog21-hausdorff-metric` | Dodatnia określoność wymaga domkniętości B i A (zapewnia ją zwartość w metrycznym X); nierówność trójkąta wynika z inf/sup |
| `thm:topog21-vietoris-hausdorff` | Dla `K⊂U` dodatnie minimum odległości od `X\U` występuje na zwartym K; druga inkluzja topologii korzysta ze skończonej r/3-sieci |
| `cor:topog21-hausdorff-convergence` | Przesunięcie ε do ε/2 pozwala przejść od ścisłych r-nierówności do kryterium `d_H→0` |
| `thm:topog21-complete` | Zbieżność funkcji odległości jest jednostajna, K={f=0} niepusty; skończona sieć A_j dowodzi total boundedness K przed orzeczeniem jego zwartości |
| `thm:topog21-compact-metric` | `S_K` jest niepuste dla niepustego K, zaś skończenie wiele niepustych podzbiorów S daje skończoną ε-sieć hiperprzestrzeni |
| `thm:topog21-vietoris-compact` | Ultrafiltrowa konstrukcja niepustego domkniętego K wymaga zwartości X i nie zakłada metryki; warunki U⁻, U⁺ zapewniają obie strony zbieżności |
| `lem:topog21-alexander` | Przy ultrafiltrze niezbieżnym jeden element podbazy spośród skończonego przecięcia nie należy do filtra; pokrycie podbazowe i skończoność dają sprzeczność |
| `thm:topog21-fell-compact` | Dowolny X, nawet nie-Hausdorffa: `C_j∩(X\U_i)` są domknięte we względnie zwartej C_j, więc własność skończonych przecięć jest wystarczająca bez kompaktowości całego X |
| `thm:topog21-fell-hausdorff` | Lokalna zwartość + Hausdorff zapewniają otwarte W o zwartym domknięciu C⊂X\G; `W⁻` i `C⁰` rozdzielają F,G |
| `prop:topog21-fell-nets` | Jednoczesne spełnienie finitely many warunków podbazowych wynika ze skierowania indeksów sieci |
| `thm:topog21-fell-vietoris` | Przy zwartym T2 X zbiory domknięte są zwarte, a `U⁺` odpowiada ominięciu zwartego dopełnienia U; obie podbazy mają tę samą topologię po ograniczeniu do niepustych |

**Przypadki graniczne:** dla X=∅ zbiór `𝒦(X)` jest pusty, a `𝔽(X)={∅}` jest przestrzenią jednopunktową zwartą; przy niezwartym X ciąg singletonów uciekających do nieskończoności może dążyć do ∅ w topologii Fella, ale nie w Vietorisa. **15/15 — brak nowej uwagi merytorycznej.**

## 3. Zmiany źródeł, PDF, regresje

**Zmiany wyłącznie w rysunkach**: porównanie pełnych 18 + 15 bloków `proof` przed i po kommitach `9352c1be...` / `1e0b2003...` dało 33 identyczne teksty. Identyczne są także etykiety i referencje. W raporcie globalnym 38 są podane zmierzone współrzędne prostokątów PDF przed i po poprawce; w obu wypadkach uzyskano >5pt pionowej przerwy.

- Realny workflow **45133887910**, artefakt `14798298647`: `completed/success` i 188-stronicowy PDF bez ostrzeżeń, 27 podpisów.
- Workflow **45134198801**, commit `a0dd1d5f10c0d3b47b8ddab59ebc7c04d23e11ef`: `completed/success`, w tym oba nowe testy regresji `test_general_topology_ch06.py` oraz `test_general_topology_ch21.py`.
- Workflow po raporcie globalnym 38 **45134587477**: sprawdzony wynik `completed/success`.
- Przebieg po raporcie 39 wymaga osobnego odczytu; nie zakładamy jego sukcesu na podstawie wcześniejszych działań.

## 4. Decyzja

**CZYSTY 2/2 na identycznych nowych blobach `71d7b30...` i `eae0bef9...`**, po odrębnej kontroli 33/33 argumentów i przypadków szczególnych. Rysunki po korekcie zweryfikowane w rzeczywistym PDF. Źródeł matematycznych i geometrycznych nie zmieniono.

Do przywrócenia statusu stabilnego pozostaje **niezależny audyt potwierdzający +1**, ponowny odczyt CI tego raportu, a potem finalne skorelowanie macierzy dowodów z nowymi blobami. Inne rozdziały pozostają niezmienione.