# Teoria grafów i węzłów — audyt 29, drugie niezależne przejście rozdziałów 37–39

Data: 2026-11-23. Repozytorium: dariusz-piekarz/mathematical_scipts, istniejąca gałąź biblioteka-matematyczna-iteracja-6.
Poprzednie przejście: [audyt 28](49-globalny-audyt-28-rozdzialy-37-39-pierwsze-przejscie.md).
Obowiązuje zasada: dwa rzeczywiste audyty trzech rozdziałów, zielone niezależne regresje i pełny skład PDF z kontrolą wizualną przed lokalną stabilizacją.

## 37 — multigrafy, identyfikatory krawędzi, low i punkty artykulacji

Dodano stwierdzenie `prop:tg-dfs-multigraph-edges` z dowodem, a także przykład `ex:tg-dfs-parallel-edges`.

Poprzednie rozdziały precyzyjnie zakładały grafy proste. W wielu zastosowaniach realny graf ma jednak równoległe krawędzie, a klasyczny skrót „pomiń sąsiada równego rodzicowi” jest wtedy **błędny**.

W grafie nieskierowanym, bez pętli, z odrębnymi identyfikatorami każdej krawędzi, DFS powinien pomijać tylko **identyfikator tej krawędzi drzewowej, którą przyszedł do aktualnego wierzchołka**. Pozostałe krawędzie do rodzica są rzeczywistymi krawędziami niedrzewowymi, które aktualizują `low`.

Dowód obejmuje zachowanie własności zagnieżdżenia poddrzew, kryterium mostu `low[w]>tin[v]` i kryterium artykulacji `low[w]≥tin[v]` dla wierzchołka niebędącego korzeniem. Korzeń nadal jest punktem artykulacji dokładnie wtedy, gdy ma co najmniej dwoje dzieci. Czas pozostaje `O(|V|+|E|)`.

Kontrprzykład: graf z dwoma wierzchołkami i **dwiema równoległymi krawędziami**. Po usunięciu jednej z nich graf pozostaje spójny, więc żadna nie jest mostem. Błędne pominięcie obu wystąpień sąsiada-rodzica generowałoby fałszywy most.

## 38 — twierdzenie Johnsona o zmianie wag przez potencjały

Dodano sekcję `sec:tg-weighted-johnson`, twierdzenie `thm:tg-weighted-johnson` z dowodem i przykład `ex:tg-weighted-johnson`.

Dla grafu skierowanego o rzeczywistych wagach, **bez cykli ujemnych**, dodajemy nowe źródło `q` i łuki `q→v` o wadze zero. Bellman–Ford oblicza potencjał `p(v)=δ(q,v)`. Z nierówności trójkąta wynika

`p(v)≤p(u)+w(u,v)`, stąd nowe wagi
`w_p(u,v)=w(u,v)+p(u)−p(v)≥0`.

Dla każdego spaceru od `s` do `t` sumowanie potencjałów teleskopuje:
`w_p(P)=w(P)+p(s)−p(t)`.
Wobec tego

`δ_w(s,t)=δ_wp(s,t)−p(s)+p(t)`.

Jedno uruchomienie Bellmana–Forda i po jednym uruchomieniu Dijkstry dla każdego źródła dają wszystkie pary najkrótszych dróg. Przy kopcu z `decrease-key` złożoność to `O(n(n+m)log(n+1))`, pamięć pomocnicza `O(n+m)` poza macierzą wyników `O(n²)`. Ujemny cykl jest wykrywany przy obliczaniu potencjałów i uniemożliwia zastosowanie standardowego algorytmu Johnsona.

Jawny przykład zawiera łuk o wadze `−2`. Potencjały `(0,−2,−1)` dają wagi zredukowane `(0,6,0,5)` i poprawną odległość pierwotną `δ(s,b)=−1`.

## 39 — ilościowa odporność MST i granica zachowania jednoznaczności

Dodano wniosek `cor:tg-mst-stability-gap`, dowód i przykład `ex:tg-mst-stability-gap`.

Dla minimalnego lasu rozpinającego `T` i krawędzi niedrzewowej `e=uv` definiujemy

`γ_e(T)=w(e)−max_{f∈P_T(u,v)}w(f)`,
`γ(T)=min_{e∉T}γ_e(T)`,
z wartością `+∞` przy braku krawędzi spoza `T`.

Ze sprawdzonego w audycie 28 kryterium wynika `γ(T)≥0`, a `T` jest **jedynym MSF** dokładnie wtedy, gdy `γ(T)>0`. Jeżeli zmiany wszystkich wag nie przekraczają `ε` i `2ε<γ(T)`, każda luka między krawędzią niedrzewową a maksymalną wagą na drodze drzewa pozostaje dodatnia:

`w̃(e)−max_{f∈P_T(e)}w̃(f)≥γ(T)−2ε>0`.

Zatem `T` pozostaje **jedynym** minimalnym lasem dla zmienionych wag. Gdy `G` sam jest lasem, jest jedynym MSF niezależnie od wag.

Przykład trójkąta o wagach `1,2,5` daje `γ=3`. Przy zmianach mniejszych niż `3/2` jedyne MST nie zmienia się. Na granicy `ε=3/2` dwie krawędzie można doprowadzić do remisu, tracąc jednoznaczność.

## Nowe, niezależne regresje i CI

Utworzono `tools/tests/test_graph_and_knot_search_paths_mst_second_pass.py` i dopisano oddzielne wywołanie do `.github/workflows/graph-and-knot-global-audit.yml`.
Ten test nie zastępuje modułu audytu 28; bada inne niezmienniki i przypadki brzegowe.

W przebiegu
[GitHub Actions 45277041073](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45277041073)
commit źródłowo-testowy `181b45395836c20f01e0040a2b3c9e5ffc1dc733`:

1. **Multigrafy — PASS:** 3780 grafów, **24 805** usunięć pojedynczych krawędzi i **18 900** usunięć pojedynczych wierzchołków. Wyniki Tarjana, uwzględniającego identyfikatory krawędzi, porównano z niezależnymi oraklami opartymi na rzeczywistym przeliczeniu spójności po usunięciu.
2. **Johnson — PASS:** 2241 grafów bez cyklu ujemnego i **1119** grafów z ujemnymi cyklami. Dla pierwszych sprawdzono **67 389** odległości par wierzchołków względem niezależnego algorytmu Floyda–Warshalla; dla drugich odrzucenie z uwagi na cykl ujemny.
3. **Odporność MST — PASS:** 1225 grafów, **18 585** wyliczonych dopuszczalnych lasów, **435** przypadków dodatniej luki. Dla każdego z tych przypadków sprawdzono zachowanie jednoznaczności pod perturbacją mniejszą niż połowa luki i powstanie remisu na dokładnej granicy `γ/2`.

**structural-audit = success**, 44/44 źródła,
0 powtórzonych etykiet, 0 niezwiązanych odsyłaczy,
0 błędów środowiskowych, 0 zabronionych terminów.
Wykonano także wszystkie starsze moduły testowe,
w tym niezależny audyt 28.

## Końcowe bramki: dwa rzeczywiste zielone przebiegi — PASS

### A. Matematyka, struktura i nowe regresje — PASS

[GitHub Actions 45277041073](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45277041073), commit
`181b45395836c20f01e0040a2b3c9e5ffc1dc733`:

- **structural-audit = success**;
- 44/44 rozdziały, 0 duplikatów etykiet,
  0 niezwiązanych odsyłaczy,
  0 błędów środowiskowych,
  0 zabronionych terminów;
- nowe testy dotyczące 37–39:
  3780 multigrafów, 24 805 przypadków
  usunięcia pojedynczej krawędzi,
  18 900 przypadków usunięcia wierzchołka,
  2241 grafów z prawidłowymi
  odległościami Johnsona,
  1119 grafów z wykrytym cyklem ujemnym,
  67 389 porównań odległości
  z niezależnym algorytmem Floyda–Warshalla,
  18 585 wyliczonych lasów,
  435 testów odporności
  i 435 dokładnych remisów
  na granicy `γ/2` — wszystkie PASS;
- pierwsze niezależne regresje audytu 28
  oraz starsze moduły również PASS.

### B. Źródłowo identyczny pełny skład tomu — PASS

[GitHub Actions 45276540727](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45276540727)
uruchomiono dla **ostatniego commitu
zmieniającego źródła LaTeX rozdziałów 37–39**:
`21c0eecd6a7bf629a4689e4b7b3824285b161b4a`.
Późniejsze zmiany dotyczyły **wyłącznie modułu
testowego, workflow i raportu**.
W tym przebiegu oba zadania,
**structural-audit** i **full-book-pdf**,
zakończyły się **success**.

Pobrano i rozpakowano oficjalny
artefakt GitHub Actions
`graph-and-knot-complete-book-audit`
**ID 14868796721**.
W rzeczywistym artefakcie potwierdzono:

- pliki wynikowe trzech kolejnych
  kompilacji `pdflatex`;
- końcowy PDF **295 stron A4**;
- plik
  `graph_and_knot_full_warnings.txt`
  o długości **0 bajtów**;
- plik diagnostyki układu i końcowy log.

Odrębne zadanie **full-book-pdf**
w przebiegu 45277041073 było jeszcze
w toku podczas ostatniej kontroli,
więc **nie przypisujemy mu
przedwcześnie wyniku success**.
Jest to dodatkowy przebieg dla
niezmienionych plików źródłowych
LaTeX, służący potwierdzeniu
tych samych wyników.

### C. Kontrola wizualna wszystkich stron 37–39 — PASS

Na podstawie PDF z przebiegu B
sprawdzono pozycję nowych rozdziałów
w drukowanym tomie. Rozdziały
**źródłowe 37–39** tworzą
**rozdziały drukowane 6–8**,
na stronach **PDF 42–63**.

Rzeczywiście wyrenderowano
i osobno obejrzano kontaktowe arkusze
każdej ze stron **42–63**:

- 42–49: źródłowy 37 —
  BFS, DFS, kryteria mostów,
  punkty artykulacji, nowa
  poprawka dla krawędzi
  równoległych (strony 47–48),
  diagram warstw i algorytm DAG;
- 50–57: źródłowy 38 —
  Bellman–Ford, Dijkstra, A*,
  nowy algorytm Johnsona
  i przykład liczbowy
  (strony 54–55),
  dwukierunkowa Dijkstra
  i hierarchie kontrakcji;
- 58–63: źródłowy 39 —
  własności przekroju i cyklu,
  certyfikat MST, nowa
  ilościowa luka optymalności
  i przykład granicznej
  perturbacji wag (strona 60),
  Prim, Kruskal, DSU,
  rysunek ważonego grafu.

**Werdykt wizualny: PASS**.
Nie zauważono uciętych
wzorów, wychodzących poza
margines elementów, nałożonych
podpisów, naruszenia
odstępów diagramów
ani błędnej numeracji.
Po przejściu do PDF strona 64
rozpoczyna kolejny rozdział
o przepływach, co potwierdza
właściwy zakres stron kontroli.

## Końcowy werdykt audytu 29

**DRUGIE NIEZALEŻNE PRZEJŚCIE: PASS.**

Rozdziały **37–39 uznaje się za
LOKALNIE STABILNE** na podstawie
obu audytów 28 i 29, realnych zmian
matematycznych w trzech plikach,
dwóch niezależnych zestawów
regresyjnych, potrójnego składu
źródłowo identycznego PDF
i oględzin pełnych 22 stron bloku.

Kontrola kodu Python, CI
oraz wizualizacja PDF nie są
formalistycznym poświadczeniem
dowodów; ich rola to niezależne
regresje algorytmiczne,
kontrola spójności i
jakości technicznej.

**Stan całej książki: rozdziały
01–39 lokalnie stabilne.**
Do pierwszego i drugiego przejścia
pozostały źródłowe rozdziały
**40–44**. Następna iteracja:
**audyt 30 — pierwsze szczegółowe
przejście rozdziałów 40–42**.
Globalny audyt 44 rozdziałów
pozostaje otwarty.
