# Teoria grafów i węzłów — audyt 28: rozdziały 37–39, pierwsze przejście

Data: 2026-11-23. Gałąź: biblioteka-matematyczna-iteracja-6.
**Rozdziały 01–36** lokalnie stabilne po dwóch niezależnych przejściach.
Zakres obecnego audytu: **37 BFS/DFS, 38 najkrótsze drogi ważone,
39 minimalne drzewa rozpinające**.
Bieżący etap jest pierwszym niezależnym przejściem;
bez drugiego audytu 29 nie wolno uznać bloku 37–39 za stabilny.

## Kontrola matematyczna i zmiany rzeczywiste

### Rozdział 37 — punkty artykulacji na podstawie DFS

Dodano twierdzenie thm:tg-dfs-articulation z pełnym
dowodem dwóch kryteriów i liniową analizą złożoności.

Dla wierzchołka będącego korzeniem drzewa DFS
punkt artykulacji powstaje wtedy i tylko wtedy,
gdy korzeń ma co najmniej dwoje dzieci w drzewie DFS.
Dla wierzchołka niebędącego korzeniem
punkt artykulacji istnieje wtedy i tylko wtedy,
gdy jedno z jego dzieci w spełnia
**low[w] ≥ tin[v]**.
Nierówność jest nieostra — równość oznacza
istnienie krawędzi wstecznej do samego v,
która nie ratuje spójności po jego usunięciu.

Dowód korzysta z faktu, że w nieskierowanym DFS
każda krawędź niedrzewowa łączy potomka
z przodkiem; rozpatruje oddzielnie korzeń
oraz pozostałe wierzchołki.
Przy powrocie z rekurencji aktualizujemy low
i sprawdzamy warunek; wszystkie punkty artykulacji
znajdujemy w czasie O(n+m) i pamięci O(n).

Dodano przykład ex:tg-dfs-articulation:
**dwa trójkąty mające tylko wspólny wierzchołek**
posiadają punkt artykulacji, ale żadna ich
krawędź nie jest mostem. To bezpośrednio
rozgranicza dwa kryteria oparte na low.

Ponownie przejrzano niezmiennik kolejki BFS,
warstwy odległości, test dwudzielności,
własności przedziałów DFS, kryterium mostów,
rozpoznawanie cykli i sortowanie topologiczne,
w tym ograniczenie do grafów prostych
przy pomijaniu krawędzi do rodzica.

### Rozdział 38 — dokładny zasięg ujemnych cykli

Dodano twierdzenie thm:tg-weighted-bellman-negative-reach.
Po n−1 przebiegach relaksacji algorytmu
Bellmana–Forda definiujemy zbiór Z końców
osiągalnych łuków u→v, dla których nadal
jest możliwa ścisła poprawa:
d[u]<+∞ oraz d[u]+w(u,v)<d[v].

Wtedy zbiór **wszystkich** wierzchołków
o odległości δ(s,v)=−∞ jest dokładnie
**R(Z)** — zbiorem wierzchołków
osiągalnych z Z po łukach skierowanych.

Pełny dowód w obu kierunkach:

1. Wartość po n−1 przebiegach nie przekracza
   żadnej prostej ścieżki z s do v.
   Jeśli łuk jeszcze poprawia oszacowanie,
   pewien spacer lepszy niż wszystkie
   takie ścieżki musi zawierać cykl ujemny;
   jego końcowy wierzchołek należy więc
   do zasięgu osiągalnego cyklu ujemnego.
2. Jeśli z s osiągalny jest cykl ujemny,
   wszystkie jego wierzchołki mają
   skończone oszacowania. Gdyby żaden
   łuk cyklu nie mógł poprawić wartości,
   zsumowanie nierówności relaksacji
   dałoby 0≤w(C)<0. Sprzeczność.
   Co najmniej jeden wierzchołek cyklu
   należy do Z, stąd cały jego
   osiągalny zasięg jest zawarty w R(Z).
3. Po odrzuceniu R(Z), pozostałe osiągalne
   wierzchołki mają prawidłowe wartości
   skończone, a nieosiągalne +∞.

Zasięg R(Z) znajdujemy BFS/DFS w czasie O(n+m)
po standardowych O(nm+n) relaksacjach.
Dodano przykład ex:tg-weighted-negative-propagation:
cykl a→b→a o wadze −2 powoduje −∞
również w dalszym wierzchołku c,
ale nie w niezależnie osiągalnym t.

Kontrolowano także oddzielenie hipotez:
Dijkstra/A* — wagi nieujemne;
Bellman–Ford — wagi mogą być ujemne;
A* bez otwierania — heurystyka spójna;
A* z otwieraniem — dopuszczalność;
CH — określona wersja dla dodatnich wag.

### Rozdział 39 — certyfikat minimalnego lasu

Dodano twierdzenie thm:tg-mst-certificate
o warunku koniecznym i dostatecznym,
również przy wagach ujemnych i remisach.

Niech T rozpina każdą składową G i jest lasem.
Wtedy **T jest minimalnym lasem rozpinającym**
dokładnie wtedy, gdy dla każdej
krawędzi e=uv spoza T mamy

w(e) ≥ max{w(f): f∈P_T(u,v)},

gdzie P_T(u,v) jest jedyną drogą między
końcami e w lesie T.

Ponadto **T jest jedynym MSF**
dokładnie wtedy, gdy wszystkie
te nierówności są **ściśle** spełnione.

Dowód konieczności wymienia lżejszą
krawędź spoza T na cięższą
krawędź na jego fundamentalnym cyklu.
Dla dostateczności wzięto dowolny MSF S
maksymalizujący liczbę wspólnych krawędzi
z T. Gdyby S≠T, wymiana
krawędzi e∈S\T przez f∈T\S
przecinającą ten sam przekrój
dałaby nie droższy MSF o większym
przecięciu z T — sprzeczność.
Ścisłość daje jednoznaczność;
równość daje inne MSF przez
wymianę na fundamentalnym cyklu.

Dodano wskazówkę o niezależnej
certyfikacji wyników Prima i Kruskala
przez zapytania o maksymalną wagę
na drodze drzewowej. Po
przygotowaniu podnoszenia binarnego
otrzymujemy O((n+m)log(n+1)).

## Testy niezależne od algorytmów ocenianych w źródłach

Utworzono
tools/tests/test_graph_and_knot_search_paths_mst_first_pass.py
i włączono go do
.github/workflows/graph-and-knot-global-audit.yml.

**Prawdziwe orakle, nie tylko te same implementacje
z innymi nazwami:**

* DFS: wynik algorytmu low/tin porównano z
  niezależnym przeliczeniem liczby składowych
  grafu po fizycznym usunięciu każdego
  wierzchołka; **6661** instancji grafów.
* Bellman–Ford: odległości −∞ i wartości
  skończone porównano z niezależną
  macierzą wszystkich par Floyda–Warshalla
  oraz wykrywaniem osiągalnych cykli
  o ujemnej przekątnej; **4641** instancji.
* MST: wszystkie lasy rozpinające
  niewielkich grafów wyliczono
  **wyczerpująco** przez podzbiory krawędzi;
  wynikające minimum i liczbę minimów
  porównano z testowanym certyfikatem
  dla każdego kandydata: **3120** grafów,
  **23 639** sprawdzonych kandydatów.

Łącznie **34 941** niezależnych
przypadków porównania z oraklem;
3120 grafów MST jest zbiorem wejściowym
dla 23 639 sprawdzonych kandydatów,
więc nie dodajemy tych 3120
powtórnie do sumy.

## Walidacja CI i oględziny PDF — PASS

Zmiany matematyczne w 37–39 zakończono commitem
5186f5aedd007e45368adc0a2594d3dc6fd14374.
Po nim zmieniono jedynie nowy moduł
testowy, workflow i raport audytu;
treść trzech źródeł TeX nie była
dalej zmieniana.

### A. Wszystkie testy i kontrola struktury — PASS

[GitHub Actions 45271265050](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45271265050),
commit 50581a2eb7b2c349843957cea10a1073c572c114:

- **structural-audit = success**;
- **44/44** rozdziały;
- **0** zduplikowanych etykiet,
  **0** nierozwiązanych odsyłaczy,
  **0** błędów środowiskowych,
  **0** zakazanych terminów;
- **34 941** nowych przypadków
  z niezależnymi oraklami — PASS,
  w tym **23 639** zweryfikowanych
  kandydatów na minimalne lasy
  w **3120** instancjach grafów;
- wykonano także wszystkie wcześniejsze
  pakiety regresyjne całego tomu.

### B. Pełny skład ze zgodnego stanu źródeł — PASS

[GitHub Actions 45271072741](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45271072741)
to pomyślny przebieg dla **dokładnie końcowego
stanu plików źródłowych rozdziałów 37–39**
(commit 5186f5aedd007e45368adc0a2594d3dc6fd14374).
Oba zadania, `structural-audit` i `full-book-pdf`,
zakończyły się sukcesem.

Pobrano artefakt
*graph-and-knot-complete-book-audit*,
**ID 14864662169**.
Sprawdzono pliki
`graph_and_knot_full_pass1.txt`,
`graph_and_knot_full_pass2.txt`,
`graph_and_knot_full_pass3.txt`
oraz końcowy PDF:
- **293 strony A4**, pełny tom;
- **3** skuteczne kompilacje `pdflatex`;
- **0 bajtów** w pliku ostrzeżeń
  `graph_and_knot_full_warnings.txt`.

W chwili tej kontroli dodatkowa kompilacja
w przebiegu 45271265050 była jeszcze
w toku, dlatego nie przypisujemy jej
przedwcześnie statusu success.
Weryfikacja PDF opiera się na
zakończonym przebiegu dla
**identycznych źródeł LaTeX**
oraz na niezależnym pozytywnym
przebiegu strukturalnym po
dołączeniu ostatnich testów.

### C. Oględziny wszystkich stron 37–39 — PASS

Położenie rozdziałów w tomie
wynika z kolejności modułów.
Źródłowe 37–39 są drukowanymi
rozdziałami 6–8, a **nie**
ostatnimi rozdziałami książki.

Wyrenderowano i obejrzano:
- **42–48** — źródłowy 37,
  rozdział drukowany 6:
  BFS, warstwy, twierdzenia
  DFS, nowy test punktów
  artykulacji, przykład
  dwóch trójkątów, diagram BFS,
  cykle skierowane;
- **49–55** — źródłowy 38,
  rozdział drukowany 7:
  Dijkstra, nowy dowód
  zasięgu ujemnych cykli
  Bellmana–Forda (strona 51),
  Floyd–Warshall, A*,
  dwukierunkowy Dijkstra i CH;
- **56–61** — źródłowy 39,
  rozdział drukowany 8:
  własności przekroju i cyklu,
  nowe kryterium optymalności
  i jednoznaczności MST
  (strony 57–58),
  DSU, Prim, Kruskal,
  wykres ważonego grafu.

Nie znaleziono obciętych wzorów,
nakładających się napisów,
uciętych węzłów diagramów,
kolizji podpisów ani wyjścia
tekstu poza marginesy.
Wykonano inspekcję kompletu
**20 stron** tego bloku.
PDF na stronie 62 rozpoczyna
kolejny, niezwiązany z audytem
rozdział algorytmów przepływowych.

## Werdykt audytu 28

**PIERWSZE SZCZEGÓŁOWE PRZEJŚCIE: PASS.**

Rzeczywiste zmiany matematyczne
w trzech plikach, niezależne
regresje, kontrola struktury
44 rozdziałów, trzykrotna
kompilacja pełnej książki
z identycznego stanu źródeł
oraz wizualna kontrola
wszystkich stron 37–39
zakończyły się pomyślnie.

**Rozdziały 37–39 nadal są
W STABILIZACJI.**
Warunkiem lokalnej stabilności
jest **audyt 29** — drugie
niezależne przejście, własne
poprawki i regresje, końcowa
bramka CI oraz PDF.

**Rozdziały 01–36 pozostają
lokalnie stabilne.**
Ogólny audyt wszystkich 44
rozdziałów nadal trwa.
