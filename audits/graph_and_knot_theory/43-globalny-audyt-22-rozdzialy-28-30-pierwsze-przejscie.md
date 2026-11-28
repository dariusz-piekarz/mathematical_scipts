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

## Końcowy przebieg CI i kontrola wizualna

**Po ostatniej poprawce w nowym teście**, dla commitu
`a4d3e879b50914bc4858a348a8963308bd0296da`,
[GitHub Actions 45225602706](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45225602706)
zakończył się wynikiem **success** w obu zadaniach:
`structural-audit` oraz `full-book-pdf`.

Potwierdzenia z logu `structural-audit`:
- **44/44** źródła i rozdziały;
- **0** duplikatów etykiet, **0** nierozwiązanych odsyłaczy,
  **0** błędów środowisk, **0** terminów zakazanych;
- **86 700** testów klasy charakterystycznej, indeksu i parzystości: PASS;
- **81** modeli równania ściany na `CP²`: PASS;
- **3125** modeli rzeczywistego mnożenia Clifforda: PASS;
- łącznie **89 906 nowych przypadków: PASS**.

Zadanie `full-book-pdf` zakończyło się sukcesem:
- wszystkie **trzy** przebiegi rzeczywistego `pdflatex`;
- **284-stronicowy PDF A4** całego tomu;
- plik `graph_and_knot_full_warnings.txt` ma **0 bajtów**
  (brak ostrzeżeń, przepełnień i błędów zgłoszonych w logu).

Pobrano artefakt końcowy
`graph-and-knot-complete-book-audit` (ID **14843620294**).
Inspekcja wizualna wszystkich stron **228–249** obejmuje:
- **228–233**, rozdział 28, w tym nowy wniosek
  o parzystości i przykład `CP²#CP²`;
- **234–241**, rozdział 29, w tym nowy przykład ściany
  `6π−t`, diagram komór, kryterium Coulomba i
  model Kuranishiego;
- **242–249**, rozdział 30, w tym nowy lemat
  mnożenia Clifforda, rysunek kraty okresów,
  dowód transwersalności i diagram półprostej.

Na 22 stronach **nie wykryto** obciętych wzorów,
nakładających się napisów, kolizji podpisów z rysunkami
ani naruszeń marginesów. Sprawdzono dodatkowo
identyczność tekstu tych stron między artefaktem
ostatniego CI a wcześniejszą kompilacją
**tego samego stanu źródeł** (run 45224836628).

Dwa wcześniejsze przebiegi nowego testu miały wynik
failure z przyczyn technicznych **w samym teście**:
(1) fałszywe dopasowanie do słowa `konsekwencja`;
(2) zaokrąglenie przy `abs(z)**2`
zamiast dokładnej normy liczby całkowitej Gaussa.
Oba błędy testu usunięto; końcowy przebieg
potwierdza wszystkie przypadki metodą całkowitoliczbową.

## Werdykt audytu 22

**Pierwsze przejście rozdziałów 28–30: PASS.**

Dokonano rzeczywistych poprawek matematycznych
i językowych w trzech źródłach, włączono
niezależną regresję do CI, potwierdzono pełną
kompilację i wizualnie skontrolowano cały blok.

**Rozdziały 28–30 pozostają W STABILIZACJI.**
Ich lokalne ustabilizowanie wymaga drugiego
szczegółowego, niezależnego audytu:
**audyt 23**. Blok 01–27 jest lokalnie stabilny.
Globalny audyt wszystkich 44 rozdziałów
pozostaje otwarty.
