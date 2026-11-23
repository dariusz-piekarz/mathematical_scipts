# Topologia ogólna — globalny audyt 60: pełna indywidualna kontrola 21 dowodów rozdziału 24

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Źródło:** `chapters/pl/general_topology/24-grupy-topologiczne-i-przestrzenie-jednorodne.tex`.
**Niezmieniony, odczytany blob:** `4b72d373d98eab0c1cc4563b72a6bb8fa62170b6`.
**Zakres:** 21/21 dowodów `proof`; hipotezy, lematy pomocnicze, przykłady i kontrprzykłady, rysunek, spójność odsyłaczy, skład i CI.

Niniejszy raport uzupełnia wcześniejszą [macierz 35](00-globalny-audyt-35-macierz-dowodow-19-26.md), [kontrolę prób kontrprzykładów 42](00-globalny-audyt-42-proby-kontrprzykladow-24-26.md) i [lokalne stabilizacyjne 2+1](24-grupy-topologiczne-iteracja-04.md). **Nie** traktuje samej obecności starego 2+1 jako indywidualnego audytu matematycznego; każdy dowód oceniono poniżej oddzielnie na bieżącym blobie.

## Rejestr 21/21 dowodów: rozumowanie i przypadki krytyczne

| ID | Etykieta; wiersz `proof` | Wynik i zweryfikowany argument |
|---|---|---|
| 24-01 | `thm:topog24-difference`; 64 | **PASS.** Ciągłość `(x,y)↦xy⁻¹` wynika ze złożenia działań. W przeciwną stronę `y⁻¹=D(e,y)` i `xy=D(x,y⁻¹)`; nie trzeba zakładać `T₂`. |
| 24-02 | `prop:topog24-translations`; 84 | **PASS.** Translacje i sprzężenia są ciągłe oraz mają ciągłe odwrotności wyznaczone przez `g⁻¹`; odwracanie jest ciągłą inwolucją. |
| 24-03 | `cor:topog24-homogeneous`; 106 | **PASS.** Translacja `L_{yx⁻¹}` przenosi `x` w `y`; niezmienniczość lokalnych własności topologicznych wynika z homeomorfizmu. |
| 24-04 | `lem:topog24-small-neighborhoods`; 129 | **PASS.** `V=W₁∩W₂∩W₁⁻¹∩W₂⁻¹` jest otwarte i symetryczne, `V²⊂U`. Indukcyjna iteracja `V_{j+1}²⊂V_j` i `e∈V_j` daje `V_r^k⊂U` dla `2^r≥k`. |
| 24-05 | `lem:topog24-closure`; 158 | **PASS.** Dla `x∈cl V` otwarte `xV` przecina `V`; równość `xv=w` daje `x=wv⁻¹∈V²`. Symetria jest tu niezbędna. |
| 24-06 | `thm:topog24-regular`; 182 | **PASS.** Wybór otwartego otoczenia `V` elementu neutralnego z `cl V⊂x⁻¹O` i jego przesunięcie zapewniają `x∈xV⊂cl(xV)⊂O`; `T₁` wynika z Hausdorffowości. |
| 24-07 | `prop:topog24-hom-continuity`; 204 | **PASS.** Dzięki homomorficzności `f(xV)=f(x)f(V)`; ciągłość w `e_G` wystarcza do ciągłości w dowolnym `x`. |
| 24-08 | `thm:topog24-subgroup-closure`; 245 | **PASS.** Ciągłość mapy różnicowej `(x,y)↦xy⁻¹` zapewnia, że dowolne otoczenie `ab⁻¹` spotyka podgrupę `H`; domknięcie jest podgrupą. Sprzężenie jako homeomorfizm zachowuje domknięcie i normalność. |
| 24-09 | `prop:topog24-open-closed`; 287 | **PASS.** Dopełnienie otwartej podgrupy jest sumą innych otwartych lewych warstw; prawa wersja wynika analogicznie. |
| 24-10 | `prop:topog24-centralizers`; 316 | **PASS.** Warunek `xa=ax` jest przeciwobrazem przekątnej w `G²` przez ciągłą mapę; `T₂` zapewnia jej domkniętość. Dowolne przecięcie tych zbiorów jest domknięte. |
| 24-11 | `thm:topog24-open-quotient`; 377 | **PASS.** `q⁻¹q(U)=UH=⋃_{h∈H}Uh` jest otwarte. Ciągłość i surjektywność `q` wynikają z definicji. Normalność `H` nie jest potrzebna. |
| 24-12 | `thm:topog24-coset-action`; 410 | **PASS.** Działanie jest dobrze określone dzięki `y=xh`. Mapa `id_G×q` jest otwartą ciągłą surjekcją i dlatego odwzorowaniem ilorazowym; `α∘(id×q)=q∘m_G` daje ciągłość. Stabilizator `H` i przechodniość policzone prawidłowo. |
| 24-13 | `thm:topog24-coset-hausdorff`; 452 | **PASS.** Konieczność z `q⁻¹({H})=H`. Przy `xH≠yH`, `g=x⁻¹y∉H`; ciągłość `(u,v)↦u⁻¹gv` daje `V⁻¹gV∩H=∅`. Wspólna warstwa w `q(xV)∩q(yV)` wymusiłaby `v⁻¹gw∈H`, sprzeczność. |
| 24-14 | `thm:topog24-normal-quotient`; 505 | **PASS.** Normalność daje poprawność ilorazowych działań. Otwartość `q×q` na prostokątach zapewnia ilorazowość i ciągłość mnożenia. `T₁` w ilorazie sprowadza się do domkniętości `N`, a `T₁` wraz z `V²⊂U` daje `T₂` w grupie topologicznej. |
| 24-15 | `thm:topog24-isomorphism`; 597 | **PASS.** `ker f` jest domknięte przez `T₂` w celu. `\widetilde f` jest dobrze określoną bijekcją, ciągłą dzięki ilorazowości `q`, a otwartą **wyłącznie dzięki jawnej hipotezie otwartości `f`**. |
| 24-16 | `thm:topog24-coset-compact`; 655 | **PASS.** Zwartość przechodzi przez ciągły obraz. W przypadku lokalnym zwarty `K` zawiera otwarte otoczenie `e`; `q(K)` jest zwarte i zawiera otwarte `q(int K)`. Translacje na `G/H` przenoszą to otoczenie na każdą warstwę. |
| 24-17 | `thm:topog24-identity-component`; 765 | **PASS.** Ciągły obraz spójnego `G⁰×G⁰` przez mapę różnicową mieści się w `G⁰`; sprzężenia dowodzą normalności. W dowodzie całkowitej niespójności ilorazu **otwartość `q` i nasycenie rozkładu przez spójne włókna** przenoszą rozdzielenie z `q⁻¹(C)` na `C`. Nie zastąpiono spójności spójnością drogową. |
| 24-18 | `thm:topog24-uniformities`; 894 | **PASS.** Dla lewych relacji `x⁻¹z=(x⁻¹y)(y⁻¹z)`, dla prawych analogicznie `xz⁻¹=(xy⁻¹)(yz⁻¹)`. Sekcje `E_U^L[x]=xU`, `E_U^R[x]=U⁻¹x` dają topologię. Translacje, odwracanie i homomorfizmy zachowują wskazane kierunki struktur. |
| 24-19 | `cor:topog24-abelian-uniform`; 959 | **PASS.** Dla grup przemiennych `xy⁻¹=(x⁻¹y)⁻¹`, a `U↦U⁻¹` permutuje bazę otoczeń `e`; struktury lewe i prawe są równe. |
| 24-20 | `thm:topog24-birkhoff-kakutani`; 987 | **PASS.** Malejące symetryczne `U_n` spełniają `U_{n+1}³⊂U_n∩B_{n+1}` i `⋂U_n={e}`. Funkcja dyadyczna `ρ` jest dodatnia poza `e`. W indukcji oszacowania `(*)` dla `S<2^{-(n+1)}` stosuje się dwa krótsze iloczyny, a dla `2^{-(n+1)}≤S<2^{-n}` rozcina się iloczyn przed i po pierwszym przekroczeniu połowy progu; środkowy czynnik ma wagę najwyżej `2^{-(n+1)}`. Dopuszczono puste fragmenty. Metryka jako infimum kosztów łańcuchów jest dodatnio określona dzięki `(*)`, lewostronnie niezmiennicza, ograniczona przez 1 i zgodna z topologią na mocy `U_{n+1}⊂B_d(e,2^{-n})⊂U_n`. |
| 24-21 | `cor:topog24-right-metric`; 1168 | **PASS.** `d_R(x,y)=d_L(x⁻¹,y⁻¹)` wyznacza właściwą topologię, a `(xg)⁻¹=g⁻¹x⁻¹` przenosi prawą niezmienniczość na lewą niezmienniczość `d_L`. |

## Próby kontrprzykładów i granice twierdzeń

1. **Bez `T₂`:** antydyskretna topologia wieloelementowej grupy zapewnia ciągłość działań, lecz nie oddzielanie; rozdział prawidłowo zastrzega Hausdorffowość w definicji i późniejszych kryteriach.
2. **Bez normalności podgrupy:** w `S₃` podgrupa `H={e,(12)}` jest domknięta, a `G/H` jest dyskretna i Hausdorffa, ale mnożenie warstw przez reprezentantów jest niepoprawne; tekst pokazuje sprzężenie wychodzące poza `H`.
3. **Bez otwartości homomorfizmu:** identyczność `(ℝ, topologia dyskretna)→(ℝ, topologia euklidesowa)` jest ciągłą bijekcją grupową bez ciągłej odwrotności.
4. **Bez domkniętości podgrupy:** `ℚ≤ℝ` jest gęsta i niedomknięta, więc `ℝ/ℚ` nie jest Hausdorffa; kontrast z `ℝ/ℤ≅S¹` jest prawidłowy.
5. **Zamiast pierwszego aksjomatu przeliczalności nie wystarczy dowolne ograniczenie kardynalności:** nieprzeliczalna grupa dyskretna spełnia pierwszy aksjomat; produkt `{0,1}^I` przy nieprzeliczalnym `I` nie spełnia go, bo przeliczalne cylindry kontrolują najwyżej przeliczalnie wiele współrzędnych.
6. **Lewy/prawy wariant struktur jednostajnych:** wyraźnie zachowano różne wzory na relacje; twierdzenie o zgodności w grupach przemiennych nie jest bezpodstawnie uogólnione na dowolną grupę.

## Technika, rysunek i publikacja

Ponownie odczytano aktualny plik. Ma **21 otwarć / 21 zamknięć `proof`**, **41 unikatowych etykiet**, **14 wystąpień odwołań** do **10 istniejących celów**. Wszystkie pary środowisk `twierdzenie`, `stwierdzenie`, `lemat`, `wniosek`, `definicja`, `przyklad`, `uwaga`, `figure` i `tikzpicture` są zrównoważone. Rozdział jest dołączony w katalogu, samodzielnym i głównym pliku książki. Test `tools/tests/test_general_topology_ch24.py` utrwala m.in. model `S₃`, ilorazy grup cyklicznych, okrąg oraz skończone modele konstrukcji Birkhoffa–Kakutaniego.

Źródłowy rysunek `fig:topog24-circle-quotient` (w. 719–749) zawiera opisane punkty całkowite na prostej, strzałkę mapy wykładniczej i punkt `1` na okręgu; te znaczenia są zgodne z przykładem. **W tej iteracji nie renderowano ponownie PDF**. Starszy [lokalny audyt 04](24-grupy-topologiczne-iteracja-04.md) dokumentuje rzeczywisty przegląd wszystkich 10 stron i figur na tym samym blobie oraz zielony [workflow 45053429106](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45053429106); jego status `completed/success` potwierdzono ponownie. Nie należy utożsamiać tego ze świeżym renderem na najnowszym HEAD.

## Decyzja i bilans

**Werdykt matematyczny: 21/21 PASS.** Rozdział 24 ma teraz pełny indywidualny raport dowód po dowodzie na niezmienionym źródle, obok wcześniejszych czystych audytów stabilizacyjnych. Nie znaleziono potrzeby zmian w LaTeX ani nowych błędów merytorycznych.

Po zamknięciu 13 w raporcie 59 bilans indywidualnej dokumentacji całego skryptu rośnie z **281/325** do **302/325**. Pozostają **23 dowody**: 14 w rozdziale 25 oraz 9 w rozdziale 26. Kolejny audyt powinien objąć wszystkie 14 dowodów rozdziału 25 na aktualnym blobie, następnie 26; ostateczny status całego tomu nadal wymaga przekrojowego audytu i CI, a nie tylko zsumowania pozytywnych wierszy.
