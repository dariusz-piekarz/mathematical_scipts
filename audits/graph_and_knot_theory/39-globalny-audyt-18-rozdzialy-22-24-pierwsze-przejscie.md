# Teoria grafów i węzłów — audyt globalny 18: rozdziały 22–24, pierwsze przejście

Data: 2026-11-23. Gałąź: `biblioteka-matematyczna-iteracja-6`.  
Poprzedni blok: 19–21, lokalnie stabilne po audycie 17.  
Kolejna jednostka: 22–24, **pierwsze przejście**, bez przedwczesnej stabilizacji.

## Kontrolowane rozdziały

- 22 — „Węzły i rozmaitości czterowymiarowe” (pierwotnie 621 linii),
- 23 — „Grafy plumbingowe, formy przecięcia i krata E8” (pierwotnie 934 linie),
- 24 — „Rozmaitości Seiferta i grafy gwiaździste” (pierwotnie 534 linie).

Zakres kontroli: pełne hipotezy i kwantyfikatory, zgodność orientacji,
rozdzielenie rachunku algebraicznego od geometrycznych lematów,
weryfikacja wzorów na formę przecięcia, homologii, wyznaczników,
twierdzeń głębokich, grafów, przykładów, odsyłaczy i kompilacji.

## Rozdział 22 — powierzchnie slice, formy Seiferta, Fox–Milnor

**Rzeczywista luka w dowodzie:** nierówność
`|σ(K)|≤2g4^sm(K)` przytaczała szacowanie
wymiaru podprzestrzeni izotropowej bez dowodu
i zawierała błędny fragment redakcyjny „dla S”.
Dodano Lemat `lem:kt-isotropic-signature` z pełnym
dowodem przez rzutowania na dodatnią i ujemną
podprzestrzeń spektralną. Dla niezdegenerowanej
formy symetrycznej o bezwładności
`(s+,s−)`, całkowicie izotropowa podprzestrzeń
`L` ma wymiar co najwyżej `min(s+,s−)`,
co daje dokładnie
`|sign S|≤dim(V)−2 dim(L)`.
Wniosek w dowodzie Murasugiego jest teraz
jawnie wyprowadzony z tego lematu.

**Granica samodzielności:** wcześniejszy
geometryczny lemat Murasugiego, który zapewnia
podprzestrzeń wymiaru przynajmniej `g−h`,
pozostaje jawnym klasycznym wynikiem topologicznym.
Lemat liniowo-algebraiczny **nie** dowodzi
samodzielnie tego istnienia.

Dodano Przykład `ex:kt-fox-milnor-matrix`
dla całkowitej macierzy Seiferta
`V=[[0,2],[1,0]]`.
Jej część antysymetryczna ma wyznacznik
`1`, a pierwszy wektor bazowy
rozpina metabolizer. Dokładne obliczenie
daje
`det(tV−V^T)=−2t²+5t−2=t(2t−1)(2t⁻¹−1)`.
Przykład rozróżnia formalną faktoryzację
od wniosku o istnieniu dysku slice
dla konkretnego węzła.

Sprawdzono relację między
`g4^top`, `g4^sm` a rodzajem Seiferta,
konstrukcję uchwytu indeksu dwa,
macierz splecenia i formę przecięcia,
ribbon, konkordancję, obstrukcje
Foxa–Milnora oraz dokładne twierdzenia
zewnętrzne Freedmana i Kronheimera–Mrowki.
Twierdzenia Freedmana i Donaldsona
nie są wyprowadzane z obliczeń
macierzowych. Dla wyniku Freedmana
o kontraktywnych wypełnieniach
homologicznych sfer brzegu wykorzystano
również kontrolę sformułowania
w przeglądach czterowymiarowej topologii.

## Rozdział 23 — rekurencja drzewa i kraty A, D, E

**Nowy lemat** `lem:tg-plumbing-leaf-determinant`:
dla liścia `v` o wadze `a` i
jego sąsiada `u` w ważonym drzewie
z dodatnimi wagami przecięć `+1`:
`det Q_Γ=a det Q_(Γ-v)−det Q_(Γ-{u,v})`.
Dowód wykonuje dwa rozwinięcia Laplace'a.
Obejmuje dowolne całkowite wagi,
również `a=0`, oraz rozłączny las
po usunięciu obu wierzchołków.

**Nowy test geometryczno-algebraiczny**
`ex:tg-plumbing-D4-leaf`:
dla ujemnej macierzy `D4`
`det Q=(-2)(-4)-4=4`,
niezależnie od wcześniejszego
obliczenia przez dopełnienie Schura.
To kontrola istotna w obliczaniu
homologii brzegu.

Ponownie skontrolowano:
- `Q_Γ` jako macierz przecięcia
  sekcji zerowych sfer z lokalną
  dodatnią orientacją krawędzi;
- dokładny ciąg
  `0→H2(Y)→Z^r→Q Z^r→H1(Y)→0`;
- formę splecenia torsyjnego
  `−x^TQ⁻¹y mod Z`;
- rekurencje `A_n`,
  klasyfikację grup brzegów `D_n`
  zależną od parzystości `n`,
  łańcuchy ułamków i blow-down;
- parzystość, unimodularność
  i ujemną określoność `E8`
  oraz `H1(∂P_E8)=0`;
- brak gładkiego kontraktywnego
  wypełnienia brzegu `E8` przez
  twierdzenie Donaldsona;
- istnienie wypełnienia
  topologicznego przez Freedmana,
  przy świadomym rozdzieleniu
  kategorii TOP i DIFF.

Pełne twierdzenia Freedmana i Donaldsona
pozostają przyjęte z literatury.
Kontrola wyznaczników nie jest
formalizacją tych twierdzeń.

## Rozdział 24 — homologia Seiferta i macierze gwiaździste

**Nowy przykład** `ex:tg-seifert-zero-e-torsion`:
dla danych `M(0;−1;(3,1),(3,1),(3,1))`
mamy `e_Q=0`, ale po
eliminacji generatorów `c_i,h`
uzyskujemy
`H1(M;Z)=Z⊕Z/3Z`.
Ranga pierwszej homologii
równa jeden **nie oznacza**
braku torsji. Uzupełniono
obliczenie o jawne relacje
`3d2=3d3=0`, `d2+d3=0`.

**Nowe stwierdzenie**
`st:tg-star-definiteness`.
Dla drzewa gwiaździstego
z centralną wagą `b`,
ramionami `(-a_ij)`,
`a_ij≥2`, i
`s=b+Σ_i β_i/α_i`
macierz ma `N−1` ujemnych kierunków
i jeden dodatkowy kierunek
o znaku `s`. Wynika to z jawnej
kongruencji blokowej przez
`P=[[I,−A⁻¹v],[0,1]]`,
dającej `P^TQP=diag(A,s)`.
Zatem `s<0` oznacza ujemną
określoność, `s=0` oznacza
jednowymiarowe jądro,
a `s>0` oznacza
dokładnie jedną dodatnią
wartość własną.
W konwencji rozdziału
`s=−e_Q(M)`.

Sprawdzono prezentację
`π1(M(g;b;(α_i,β_i)))`
z centralnym włóknem,
homologię przez dopełnienie
Schura, ułamki łańcuchowe
i zgodność orientacji
brzegu plumbingowania `E8`.
Weryfikacja ilorazu
`π1(Σ(2,3,5))→A5`
została objęta
skończonym modelem grup permutacji.
Sama identyfikacja brzegu
jako sfery homologicznej
Poincarégo i klasyfikacja
geometrii Thurstona pozostają
jawnymi wynikami zewnętrznymi.

## Nowa regresja niezależna od LaTeX

Dodano
`tools/tests/test_graph_and_knot_four_dim_plumbing_seifert.py`
i uruchamianie go z workflow
`.github/workflows/graph-and-knot-global-audit.yml`.

Model implementuje determinanty całkowite
metodą Bareissa, bez SymPy lub innej
biblioteki spoza standardowej:
- **58 425** sprawdzeń rekurencji
  wyznacznika ważonego drzewa
  przy zerowych, ujemnych
  i dodatnich wagach;
- **6687** przypadków grup
  `A_n`, `D_n`, `E8`,
  wyznaczników, rzędów modulo 2,
  kryterium Sylvestera i
  parzystości `E8`;
- **1160** konfiguracji ramion
  grafów gwiaździstych,
  z porównaniem wyznacznika
  z dopełnieniem Schura
  i prezentacją Seiferta;
- **5** specjalnych przypadków
  postaci Smitha, w tym
  `e_Q=0` i torsja `Z/3`;
- **341** dokładnych faktoryzacji
  Foxa–Milnora dla blokowych
  macierzy Seiferta, w tym
  jawny przykład z rozdziału;
- **100** konfiguracji izotropowych
  form symetrycznych;
- **60** elementów grupy
  `A5` generowanych przez
  permutacje z przykładu
  sfery Poincarégo.

Razem **66 778 sprawdzeń**.
Wszystkie sprawdzenia dotyczą
dokładnych modeli skończonych,
nie dowodzą ogólnych twierdzeń
o czterorozmaitościach.

## Struktura i niezakończone kontrole

Po wprowadzeniu testu (przebieg
[45204620682](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45204620682))
`structural-audit=success`:
`44/44` źródła,
`0` powtórzonych etykiet,
`0` nierozwiązanych odsyłaczy,
`0` błędów środowiskowych
oraz `0` zakazanych terminów.

Należy dodatkowo:
1. potwierdzić nowy test końcowy
   z przykładem Foxa–Milnora;
2. skompilować cały tom trzy razy
   po **ostatniej** zmianie;
3. pobrać i obejrzeć PDF,
   szczególnie nowe fragmenty
   rozdziałów 22–24, rysunki
   `A_n,D_n,E8` i gwiazdę Seiferta;
4. przeprowadzić drugi,
   niezależny audyt tego bloku,
   zanim otrzyma on status
   lokalnie stabilny.

**Werdykt pierwszego przejścia:
poprawki matematyczne wprowadzono,
blok 22–24 nadal W STABILIZACJI.
Nie przechodzić do 25–27
bez zamknięcia stabilizacji.**
