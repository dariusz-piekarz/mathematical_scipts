# Teoria grafów i węzłów — audyt globalny 23: rozdziały 28–30, drugie przejście

Data: 2026-11-23. Gałąź: `biblioteka-matematyczna-iteracja-6`.  
Pierwsze przejście: [audyt 22](43-globalny-audyt-22-rozdzialy-28-30-pierwsze-przejscie.md).  
Przedmiot: trzy rozdziały teorii Seiberga–Wittena. **Drugie niezależne przejście**, a nie powtórzenie testów z audytu 22.

## Dokładnie kontrolowany zakres

1. **28 — Wprowadzenie do teorii Seiberga–Wittena.**
   Formalna parzystość indeksu, zgodność struktur `Spin^c`
   po wymiernej kontrakcji, wymiar oczekiwany, konieczne
   warunki podniesienia klas, przykład `E(4)`,
   oddzielenie rachunku od wyników Fintushela–Sterna.
2. **29 — Przestrzenie moduli i komory.**
   Konwencje połączeń, prawo działania grupy cechowania,
   przekrój Coulomba, Hodge'owskie równanie ściany,
   poprzeczność rodzin perturbacji, zwartość i
   formuła zmiany komory.
3. **30 — Analityczne przejście do niezmiennika.**
   Zgodność normalizacji Clifforda, dokładność symbolu
   `d^* ⊕ d^+`, jawne oszacowanie jego odwracalności,
   wyznacznik, argument transwersalności
   i granica rachunku bez globalnej teorii Fredholma.

Wewnętrzne rachunki zostały oddzielone od wyników
analitycznych przyjmowanych z literatury.
**Testy skończone nie stanowią dowodu**
twierdzenia Atiyaha–Singera, Fintushela–Sterna,
Taubesa, Sarda–Smale'a, kompaktowości moduli
ani formuły zmiany komory.

## 28 — usunięcie luki w dopuszczalnych podniesieniach `Spin^c`

Dodano lemat
`lem:tg-sw-c2-admissible-pairing`
z bezpośrednim dowodem przez rozkład
racjonalnej formy przecięcia przy sferze
`S²=−4`.

Niech `C_2` będzie dyskowym otoczeniem sfery,
`X_(2)` wymierną kontrakcją i niech
struktury `Spin^c` `s` na `X`
oraz `s'` na `X_(2)` mają **zgodne
ograniczenia do dopełnienia `W`**.
Po oznaczeniu `m=<c1(s),[S]>` mamy dokładną
tożsamość:
`c1(s)²−c1(s')²=−m²/4`.

Dowód: składnik Poincarégo dualny do `c1(s)`
na prostej wymiernej generowanej przez `[S]`
to `−(m/4)[S]`, gdyż `[S]²=−4`.
Kwadrat tego składnika to `−m²/4`.
Na części `W` składniki są identyczne,
ponieważ struktury `Spin^c` mają zgodne ograniczenia.

Ponieważ `κ(X_(2))=κ(X)+1` dla
`κ=2e+3σ`, otrzymujemy
`d_X(s)−d_X_(2)(s')=(4−m²)/16`.
Stąd zgodność wymiarów oczekiwanych
jest **równoważna** `|m|=2`.
Jest to jednak warunek konieczny,
nie automatyczny dowód istnienia
zgodnego podniesienia.

**Dodatkowa przeszkoda całkowitości:**
dla rzeczywiście istniejących zgodnych
struktur oba indeksy `d` są
całkowite. Przy `m` parzystym
wynika stąd `m≡2 (mod 4)`.
Zatem `m=0` już wyklucza
takie przedłużenie — nawet przed
pytaniem o równość wymiarów.

W przykładzie `E(4)`
wskazano jawnie rolę tego lematu.
Dla sekcji `S` mamy `F·S=1`.
Trzy podstawowe klasy wyjściowe
to `−2F,0,2F`;
ich wartości na `S` wynoszą
odpowiednio `−2,0,2`.
Tylko klasy `±2F`
spełniają konieczny
warunek wymiarowy.
Dalsza konkluzja
o ocalałych niezerowych
niezmiennikach wymaga
rzeczywistej formuły sklejenia
Fintushela–Sterna.
Zgodność przykładów potwierdzają
m.in. klasyczne
[wykłady Fintushela i Sterna](https://bpb-us-e2.wpmucdn.com/faculty.sites.uci.edu/dist/3/246/files/2011/03/57_Six_Lectures.pdf).

## 29 — dokładna poprzeczność ściany bez twierdzenia o zmianie komory

Dodano lemat `lem:tg-sw-affine-wall`
dla każdej metryki na zamkniętej zorientowanej
czterorozmaitości o `b2^+=1`,
ustalonej struktury `Spin^c`
i dowolnej gładkiej rodziny
samodualnych perturbacji
`η_t=η_0+tθ`.

Po normalizacji dodatniej harmonicznej formy
`ω_g` do `∫ω_g∧ω_g=1` i
ustaleniu `a=∫θ∧ω_g`
funkcja definiująca ścianę jest
dokładnie afiniczna:
`w_s(g,η_t)=w_s(g,η_0)−ta`.

- Gdy `a≠0`, rodzina ma jedno
  przecięcie ze ścianą:
  `t_*=w_s(g,η_0)/a`.
  Jest ono poprzeczne,
  gdyż pochodna wynosi `−a≠0`.
- Gdy `a=0`, rodzina
  leży w ścianie w całości
  albo jej nie przecina.

Dowód opiera się tylko na
liniowości rzutu harmonicznego i całki.
Warunek taki pozwala **zlokalizować
redukuwalne rozwiązania**, ale
sam nie zapewnia niezerowego skoku
`SW^+−SW^−`: ten pozostaje
twierdzeniem analitycznym
wymagającym lokalnej teorii Kuranishiego.

## 30 — pełna macierz symbolu i mocniejsza tożsamość

Dodano `lem:tg-sw12-symbol-matrix`
z wyprowadzoną w bazach
`(e12+e34,e13−e24,e14+e23)`
macierzą `M(ξ)` operatora symbolu
`a↦(−<ξ,a>,(ξ∧a)^+)`.
Wykazano wprost, że
`M(ξ)M(ξ)^T=|ξ|² diag(1,1/4,1/4,1/4)`.

W dowodzie obliczono wszystkie normy
i iloczyny skalarne wierszy.
Daje to ilościową wersję
wcześniejszej eliptyczności:
`|det M(ξ)|=|ξ|⁴/8`
dla każdego niezerowego `ξ`.
Bez odwołań do teorii Fredholma
otrzymano więc **dokładną algebraiczną
odwracalność symbolu**;
pełna teoria indeksu pozostaje
zewnętrznym wynikiem.

## Nowe niezależne regresje

Utworzono moduł
`tools/tests/test_graph_and_knot_sw_second_pass.py`,
włączony do
`.github/workflows/graph-and-knot-global-audit.yml`.
Wszystkie wartości wyznaczników,
kongruencji i parametrów obliczane
są **dokładnie**, nad `Z` lub `Q`,
bez arytmetyki zmiennoprzecinkowej.

Nowe rodziny niezależne od
89 906 regresji audytu 22:

1. **104** testy `C_2`:
   wyprowadzenie wzoru `(4−m²)/16`
   dla `m=−100,−98,…,100`,
   koniecznego warunku `m≡2 (mod4)`,
   wartości `m=±2` i
   trzech klas `E(4)`.
2. **17 326** testów
   dokładnych jednoparametrowych
   rodzin ściany przy
   `c,η_0∈{−7,…,7}`,
   `a=num/den`,
   `num∈{−5,…,5}`,
   `1≤den≤7`;
   obejmują unikalne przecięcie,
   przypadek styczny
   `a=0` i znak zmian po obu
   stronach ściany.
3. **12 000** testów
   jawnego symbolu:
   2400 niezerowych kowektorów
   `ξ∈{−3,…,3}⁴`;
   dla każdego: iloczyn `MM^T`,
   wyznacznik macierzy `2M`
   przez niezależne rozwinięcie
   permutacyjne, oraz pięć
   przykładów wektorów dziedziny
   z zachowaniem ważonej normy.

Łącznie **29 430 nowych przypadków**
w audycie 23.
Razem z modułem audytu 22:
**119 336 dokładnych przypadków SW**
w obu niezależnych przejściach.

W CI należy zawsze sprawdzać
**ostatni commit źródeł oraz testów**
(aktualnie `15bade78d69f5a4ca0f61450900d45b0d34a1e43`),
a nie wynik wcześniejszej wersji źródeł.

## Bramka końcowa audytu 23

[GitHub Actions 45229804811](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45229804811)
ma już wynik `structural-audit=success`.
Log potwierdza:
**44/44** rozdziały, **0** duplikatów etykiet,
**0** niezwiązanych odsyłaczy,
**0** błędów środowiska i
**0** terminów zakazanych;
wszystkie **29 430** przypadków nowego
modułu są `PASS`.

Zamknięcie audytu wymaga jeszcze
końcowego `full-book-pdf=success`,
trzech przebiegów `pdflatex`,
pustego pliku ostrzeżeń
i wizualnego przeglądu
nowych stron rozdziałów 28–30.

**Dopóki te warunki nie są spełnione,
rozdziały 28–30 pozostają w stabilizacji.**
W razie powodzenia: lokalna stabilizacja
rozdziałów 01–30; następnie audyt 24
(pierwsze przejście 31–33).
Całościowy audyt 44-rozdziałowego
tomu pozostaje otwarty.
