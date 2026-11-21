# Topologia algebraiczna — TOP-30: audyty I–V

**Data:** 21 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Rozdział:** `chapters/pl/algebraic_topology/30-minimalne-przypomnienie-geometrii-rozniczkowej.tex`.  
**Końcowy blob źródła TOP-30:** `fd7c66d943ca8d518882cc0c918de2804822641f`.

Zgodnie ze standardem DG-01 przeprowadzono pięć iteracji audytu **istniejących** treści, bez dodawania nowych twierdzeń, lematów i przykładów: poprawność matematyczna, precyzja twierdzeń, istotne przejścia dowodowe, przykłady, terminologia, LaTeX, rysunki i testy. Poniżej zakres faktycznie wykonanych zmian i zależności, z odróżnieniem dowodów własnych od wyników przyjętych.

## I. Definicje rozmaitości i algebra zewnętrzna

- Zapis definicji rozmaitości określa przestrzeń Hausdorffa, drugi aksjomat przeliczalności, mapy na otwarte podzbiory `R^n`, zmiany klasy `C∞` na ich dziedzinach i równoważność atlasów.
- Przestrzeń styczna ma jawnie określony punkt `p∈M`, dziedzinę derywacji `C∞(M)` i regułę Leibniza; przestrzeń kostyczna jest przestrzenią sprzężoną.
- Stwierdzenie o bazie `∧^k V*` definiuje `V`, bazę `e_i`, bazę dualną `e^i`, indeksy i przypadek `k=0`.
- Dowód niezależności jest pełny: wartościowanie na uporządkowanych wektorach bazowych daje macierz jednostkową, bo `(e^{i_1}∧…∧e^{i_k})(e_{j_1},…,e_{j_k}) = det(e^{i_a}(e_{j_b})) = δ_{I,J}`.
- Nie zmieniono treści stwierdzenia.

Commit `17cb58d2daf6ed59202f15958b83ddd1f3003320`.

## II. Submersje, transwersalność, Sard, otoczenia tubularne i uramowania

- Samodzielne definicje submersji punktowej i globalnej, wartości regularnej (także dla pustego przeciwobrazu), transwersalności w punkcie oraz wiązki normalnej `ν(S,M)=TM|_S/TS`. Wyjaśniono zależność identyfikacji normalnej z ortogonalnym dopełnieniem od wyboru metryki.
- W jednym **istniejącym** twierdzeniu zestawiono precyzyjnie założenia i tezy dla: lokalnej postaci submersji, przecięcia transwersalnego, otoczenia tubularnego domkniętej podrozmaitości osadzonej oraz twierdzenia Sarda (miara zero wartości krytycznych w lokalnych mapach).
- Ogólne twierdzenia o perturbacyjnej transwersalności nie są dowodzone ani nie są używane bez określenia przestrzeni odwzorowań/topologii. W uwadze wyjaśniono, dlaczego sama transwersalność nie zapewnia skończonej liczby przecięć: potrzebne są dopełniające wymiary i zwartość przecięcia.
- Definicja globalnego uramowania mówi o wiązce `π:E→B`, przekrojach `s_i` i liniowej niezależności; dowód równoważności uramowania i gładkiej trywialności obejmuje jawne odwzorowanie `τ(x,a)=Σ a_i s_i(x)` i gładkość macierzy odwrotnej w lokalnych trywializacjach.

Commit `3648b737b4b092857b5ef7a6968f730e5bc19fa1`.

## III. Okrąg jako poziomica regularna i jawne otoczenie tubularne

- W przykładzie `F(x,y,z)=(x²+y²−1,z)` uzasadniono rangę różniczki `2` na `S=F^{-1}(0)`, powiązano regularność z lokalną postacią submersji i jawnie wskazano jądro `dF`.
- Wyjaśniono, dlaczego wektory `(x,y,0)` i `(0,0,1)` stanowią globalne ortonormalne uramowanie wiązki normalnej oraz jak wybór metryki identyfikuje ją z wiązką ilorazową.
- Podano identyfikację `ν(S,R³) ≅ S×R²` i przeprowadzono sprawdzenie obu kierunków funkcji `Φ((x,y,0),a,b)=((1+a)x,(1+a)y,b)`. Dla `0<ε<1/2` współrzędna `ρ=√(X²+Y²)>0` gwarantuje poprawność i gładkość `Φ^{-1}`.
- Wszystkie użyte wzory są teraz uzasadnione lub powiązane z wcześniej przyjętą konstrukcją.

Commit `4c85f4872720b8008deb412a40b125554fe787fc`.

## IV. Przecięcie okręgu z prostą i regresje

- Dla stycznego `y=1` uzasadniono jedyny punkt `(0,1)` i równość przestrzeni stycznych.
- Dla `y=1−ε`, `0<ε<1`, wyliczono `x²=ε(2−ε)>0`, oba punkty `p_±`, styczne `R(−y,x)` i `R(1,0)` i wyznacznik `−x`, zapewniający transwersalność.
- Wskazano orientacje i wynikające z nich znaki lokalne `−1,+1`; suma jest zerowa, mimo dwóch geometrycznych punktów przecięcia.
- Do `application/tests/test_topology_chapters_29_30.py` dodano trzy regresje: samodzielne hipotezy twierdzeń, kombinatoryczną bazę algebry zewnętrznej dla `0≤n≤8` i `0≤k≤n`, oraz numeryczne sprawdzenie `Φ`, uramowania normalnego i współrzędnych rysunku dla `ε=0,3`.

Commity `c69f9e9b6e2478a3d20baa33aec76741ff12ab61`, `c36f7f7971df3a76ca11369331307d2935df32ae`.

## V. Globalna spójność, język, kwantyfikatory, odsyłacze

- Zapisano `n∈Z_{≥0}` i `r∈Z_{≥0}`, dopisano w definicji przekroju warunek `π∘s_i=id_B`.
- Przywrócono zwykłą polską pisownię „wiązkę”, bez wymuszonego dzielenia wyrazu. Stosujemy **„mapa” tylko dla chart** i **„odwzorowanie” dla mapping**.
- Przegląd całego źródła: **5 unikatowych etykiet**, 0 aktywnych odsyłaczy lokalnych `\ref` (obce etykiety DG są celowo wymieniane jako tekst `\texttt`, bez tworzenia fałszywych referencji), 3 definicje, 1 twierdzenie, 1 stwierdzenie, 2 przykłady, 1 dowód, 1 uwaga, 1 rysunek TikZ. Wszystkie odpowiednie liczniki `\begin` / `\end` są zgodne.
- Pozostawiono dotychczasowe zależności od wcześniejszego tomu geometrii różniczkowej, zamiast tworzyć ich fikcyjne wewnętrzne kopie lub pozorne linki. Nie dodano żadnych nowych twierdzeń ani przykładów.
- Rozdział pełni rolę krótkiego dodatku — nie zastępuje wyczerpującego tomu geometrii różniczkowej.

Commit `a886f3b46dee91c13370e9d2ed947ad4471824c8`.

## Wynik CI i PDF — do potwierdzenia po zakończeniu trwających przebiegów

- [TOP-29/30, kompilacja całego tomu i regresje](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44948439855).
- [Ogólne CI aplikacji](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44948439753).
- [Międzytomowe AT–DG–AG](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44948439803).

**Stan audytu matematycznego:** Pięć iteracji wykonano, rozdział bez znanych otwartych luk w jego własnych obliczeniach. Wyniki głębokie wskazane jako przyjmowane. Formalne zamknięcie: po potwierdzeniu końcowych przebiegów CI i wizualnej kontroli PDF wydzielonego z tej samej wersji źródła. Następnym etapem jest **globalny audyt TOP-00–TOP-30**, a nie tworzenie TOP-31 bez zatwierdzonego planu.
