# Teoria grafów i węzłów — audyt globalny 22: rozdziały 28–30, pierwsze przejście

Data: 2026-11-23. Gałąź: `biblioteka-matematyczna-iteracja-6`.  
Rozdziały 01–27 pozostają **lokalnie stabilne** po audycie 21.
Rozdziały 28–30: **pierwsze szczegółowe przejście**;
bez przedwczesnej stabilizacji.

## Zakres audytu

1. **28 — Wprowadzenie do teorii Seiberga–Wittena i zastosowań w wymiarze cztery.**
   Sprawdzono dekompozycję Hodge'a, klasy charakterystyczne,
   wiązki `Spin^c`, konwencje cechowania, wymiar oczekiwany,
   wpływ krzywizny skalarnej, klas podstawowych i wymiernej kontrakcji.
2. **29 — Analityczne podstawy teorii Seiberga–Wittena.**
   Sprawdzono grupy i przekroje cechowania, kompleks eliptyczny,
   oszacowania Weitzenböcka, zwartość, regularność generyczną,
   równanie ściany oraz formułę zmiany komory.
3. **30 — Analiza Seiberga–Wittena: od lokalnego przekroju do niezmiennika.**
   Sprawdzono normalizację kwadratowego odwzorowania spinorowego,
   lokalną strukturę ilorazu, kratę dużych przekształceń,
   symbol operatora deformacji, kontrolę krzywizny,
   przejście od L∞ do C∞ oraz argument transwersalności.

Podczas audytu celowo **odróżniono rachunki możliwe do
uzasadnienia elementarnie od głębokich założeń analitycznych**.
W szczególności testy nie dowodzą twierdzenia indeksowego
Atiyaha–Singera, własności Fredholma, twierdzenia
Sarda–Smale'a, zwartości przestrzeni moduli ani
modelu Kuranishiego. Te wyniki pozostają oznaczone
w rozdziałach jako zewnętrzne.

## Rozdział 28 — nowa parzystość wymiaru oczekiwanego

Dodano wniosek `cor:tg-sw-index-parity`
z pełnym dowodem na podstawie
rachunku indeksowego:
`d(s)=2 ind_C D_A+b1−1−b2^+`,
a więc
`d(s)≡b1−1−b2^+ (mod 2)`.
W szczególności, gdy `b1=0` i
`b2^+` jest parzyste, dla żadnej
struktury `Spin^c` nie zachodzi `d(s)=0`.

Dodano dokładny przykład
`ex:tg-sw-index-parity`:
dla `CP²#CP²` mamy
`b1=0,b2^+=2,e=4,σ=2`.
Klasa charakterystyczna `c=H1+H2`
ma `c²=2`, więc
`d(s)=(2−8−6)/4=−3`.
Niezależnie od konkretnej klasy
każdy wymiar oczekiwany pozostaje
nieparzysty.

Wynik nie orzeka sam przez się,
że przestrzenie moduli są puste;
zerowy wymiar oczekiwany jest
jedynie określonym przypadkiem
definicji liczbowego niezmiennika.

## Rozdział 29 — jawne przejście przez ścianę

Dodano przykład
`ex:tg-sw-wall-cp2`
z ustaloną metryką Fubiniego–Study'ego
na `CP²`, dodatnim generatorem `H`,
`c1(L)=3H`, harmoniczną samodualną
formą `ω` reprezentującą `H`
i `∫ω∧ω=1`.
Dla perturbacji `η_t=tω`
równanie ściany sprowadza się
do **jawnej funkcji**
`w_s(g,η_t)=6π−t`.

W konsekwencji:
- przy `t=6π` występują
  redukowalne rozwiązania równania krzywizny;
- przy `t≠6π` redukowalne
  rozwiązania są wykluczone;
- ścieżka przecina ścianę
  poprzecznie, gdyż pochodna
  `d w_s/dt=−1`;
- `d(s)=(9−2·3−3·1)/4=0`;
- przy `t=0` dodatnia
  krzywizna skalarna i
  Weitzenböck wykluczają
  rozwiązania nieredukowalne,
  zatem `SW` w tej komorze
  jest zero;
- wartość `±1` po drugiej
  stronie wynika dopiero
  z analitycznego twierdzenia
  o zmianie komory, nie
  z liniowej arytmetyki ściany.

Poprawiono również użycie polskich słów
`ciąg`, `podciąg` zamiast
niepoprawnego anglicyzmu
`sekwencja` w kontekście
zbieżności rozwiązań.
Poprawiono odmianę gramatyczną.

## Rozdział 30 — domknięcie luki w transwersalności

Dodano lemat
`lem:tg-sw12-clifford-real-iso`
z samodzielnym dowodem:
dla niezerowego `ψ∈S_x^+`
rzeczywisto-liniowe odwzorowanie
`T_x^*X→S_x^-`,
`v↦ρ(iv)ψ`,
jest izomorfizmem rzeczywistych
przestrzeni wymiaru cztery.

Z relacji Clifforda mamy
`ρ(v)^*ρ(v)=|v|² id` i stąd
`|ρ(iv)ψ|²=|v|²|ψ|²`.
Przy `ψ≠0` jądro jest zerowe.
Równość wymiarów rzeczywistych
`dim_R(T_x^*X)=dim_R(S_x^-)=4`
daje surjektywność.
W ten sposób kluczowy krok
dowodu `lem:tg-sw12-surj`
nie jest już przyjęty
bez uzasadnienia — odnosi się
do nowego, jawnego lematu.
Dalsze wykorzystanie zasady
jednoznacznego przedłużenia
dla operatora Diraca pozostaje
prawidłowo wskazanym zewnętrznym
twierdzeniem analitycznym.

Poprawiono również terminologię
ciągów i podciągów, nie naruszając
znaczenia słowa `konsekwencja`.

## Dokładne regresje matematyczne

Dodano
`tools/tests/test_graph_and_knot_sw_index_wall_clifford.py`
i włączono go do
`.github/workflows/graph-and-knot-global-audit.yml`.

Trzy **niezależne rodziny rachunków**:
- **86 700** testów charakterystycznych klas
  na macierzach `diag(+1^p,−1^q)`,
  dla `1≤p≤4`, `0≤q≤3`,
  `0≤b1≤2`, ze współczynnikami
  z `{−3,−1,1,3}`.
  Sprawdzane są kongruencje
  `c²≡σ (mod 8)`,
  podzielność wzoru wymiaru
  przez 4, równość z indeksem
  zespolonym i parzystość.
- **81** przypadków parametru
  `η_t` na `CP²`,
  w jednostkach `π`
  dla `−40≤t/π≤40`,
  z dokładnym równaniem
  `w/π=6−t/π`, i kontrolą
  przejścia przez zero.
- **3125** sprawdzeń mnożenia Clifforda
  za pomocą reprezentacji
  zespolonych macierzy Pauliego:
  `|M(v)ψ|²=|v|²|ψ|²`,
  dla 625 wektorów
  `v∈{−2,…,2}⁴`
  i pięciu niezerowych spinorów.

Łącznie **89 906 dokładnych przypadków**.
Ta kontrola algebry lokalnej nie
poświadcza twierdzeń globalnych
o zwartości lub orientacji moduli.

**Ważna uwaga o jakości audytu:**
pierwszy test terminologiczny
fałszywie wykrywał `sekwencja`
wewnątrz słowa `konsekwencja`.
Zamieniono wyszukiwanie
podciągu znaków na dopasowanie
całego słowa. Nie traktuje się
początkowego nieudanego
przebiegu CI jako sukcesu.

## Status CI i stabilizacji

Po ostatnich poprawkach oczekujemy
na końcowe wyniki pełnego
workflow uruchomionego
dla commitu
`732ff686e63a13d0e7ba8688b3470a5681179c14`:
[GitHub Actions 45225257390](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45225257390).

Do zamknięcia **pierwszego przejścia**
wymagane są:
(1) `structural-audit=success`,
(2) **89 906** regresji `PASS`,
(3) trzykrotny pełny skład 44-rozdziałowego
PDF bez ostrzeżeń,
(4) oględziny stron z rozdziałami 28–30
z uwzględnieniem nowych twierdzeń
i rysunków.

**Nie oznaczać rozdziałów 28–30
jako lokalnie stabilnych przed
drugim niezależnym przejściem
(audyt 23).**

Globalny audyt całego
44-rozdziałowego tomu pozostaje otwarty.
