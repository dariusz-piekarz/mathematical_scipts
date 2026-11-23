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

## Bramka końcowego PDF — wymagane dalsze sprawdzenie

Do pełnego zamknięcia drugiego przejścia należy potwierdzić:
- `full-book-pdf = success` dla końcowego stanu plików źródłowych TeX, najlepiej dla run 45277041073;
- rzeczywiste trzy przebiegi `pdflatex` i plik ostrzeżeń długości zero;
- odczyt i oględziny wizualne wszystkich stron zawierających źródłowe rozdziały 37–39, w tym nowy przykład multigrafu, Johnsona i granicy perturbacji MST.

**Do czasu przejścia tej bramki nie przypisujemy blokowi 37–39 lokalnej stabilności.** W przypadku PASS stabilne będą lokalnie rozdziały 01–39; do audytowania pozostaną źródłowe rozdziały 40–44. Następna iteracja — audyt 30: pierwsze przejście rozdziałów 40–42.
