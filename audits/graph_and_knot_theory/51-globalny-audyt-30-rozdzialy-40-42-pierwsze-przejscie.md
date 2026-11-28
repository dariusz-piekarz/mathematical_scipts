# Teoria grafów i węzłów — audyt globalny 30: rozdziały 40–42, pierwsze przejście

Data: 2026-11-23. Repozytorium: dariusz-piekarz/mathematical_scipts.
Gałąź istniejąca: biblioteka-matematyczna-iteracja-6.
Poprzednio stabilne lokalnie rozdziały 01–39 (dwa niezależne przejścia).
Przedmiot niniejszego audytu: źródłowe rozdziały 40 (przepływy), 41 (ekstremalna teoria grafów) i 42 (grafy losowe).

## Reguły kontroli

Weryfikowano jawność hipotez, poprawność argumentacji, kwantyfikatory, zakres wartości parametrów, przykłady i kontrprzykłady, zgodność terminologii matematycznej, kompletność odsyłaczy, testowalność wyniku, skład LaTeX i rysunki. Matematyczne poprawki wprowadzono bezpośrednio do wszystkich trzech plików źródłowych; raport nie jest substytutem zmian.

### 40 — rozkład przepływu i skierowana wersja twierdzenia o drogach rozłącznych

W pliku chapters/pl/graph_and_knot_theory/40-algorytmy-przeplywowe-ford-fulkerson-edmonds-karp-dinic.tex dodano twierdzenie thm:tg-flow-integral-paths i przykład ex:tg-flow-integral-paths.

Dokładna teza: dla skończonej sieci skierowanej bez pętli, z różnymi s,t, nieujemnymi całkowitymi pojemnościami i dowolnym dopuszczalnym przepływem całkowitoliczbowym f o wartości k, istnieje skończony rozkład tego przepływu na proste skierowane drogi s–t o dodatnich całkowitych krotnościach sumujących się do k oraz proste cykle skierowane o dodatnich całkowitych krotnościach. Dla pojemności 0/1 istnieje dokładnie k parami rozłącznych krawędziowo dróg s–t. W rezultacie maksymalna liczba takich dróg jest równa minimalnej liczbie łuków, których usunięcie rozdziela s i t.

Dowód:
1. Jeśli wartość dodatnia, wsparcie przepływu zawiera drogę s–t. W przeciwnym razie zbiór S wierzchołków osiągalnych po dodatnich łukach miałby zerowy przepływ wychodzący i niedodatni bilans przez przekrój, wbrew dodatniej wartości.
2. Odejmujemy minimalny dodatni przepływ na prostej drodze. Każda operacja zachowuje całkowitość i prawo zachowania oraz zeruje przynajmniej jeden łuk, więc proces jest skończony.
3. Po osiągnięciu wartości zero reszta jest cyrkulacją. Każda niezerowa skończona cyrkulacja zawiera skierowany cykl; iteracyjne odjęcie jego minimalnej krotności wyczerpuje resztę.
4. Przy pojemnościach 0/1 współczynniki dróg równe są jeden, a ich łuki są rozłączne. Górne ograniczenie wynika z dowolnego przekroju; dolne z twierdzenia maxflow–mincut i istnienia całkowitego maksimum przez Forda–Fulkersona.

Zwrócono szczególną uwagę na oryginalne łuki przeciwne, pojemności resztowe i cykle: nie wolno z sumy wartości przepływu wywnioskować nieistnienia cykli, dlatego cykle w rozkładzie są jawnie uwzględnione.

### 41 — nierówność Caro–Weiego i oszacowanie przez stopień średni

W pliku chapters/pl/graph_and_knot_theory/41-twierdzenia-mantela-turana-i-ramseya.tex dodano sekcję sec:tg-caro-wei, twierdzenie thm:tg-caro-wei, wniosek cor:tg-caro-wei-average i przykład ex:tg-caro-wei-two-cliques.

Dla każdego skończonego niepustego grafu prostego o n wierzchołkach i m krawędziach:

α(G) ≥ Σ_v 1/(d_G(v)+1) ≥ n²/(n+2m).

Dowód pierwszej nierówności: wybieramy jednostajnie losową permutację V i zaznaczamy v, jeśli jest wcześniejszy niż wszyscy jego sąsiedzi. Zaznaczone wierzchołki są niezależne, a prawdopodobieństwo zaznaczenia v to 1/(d_G(v)+1). Liniowość wartości oczekiwanej daje istnienie permutacji z niezależnym zbiorem liczności co najmniej średniej. Druga nierówność wynika z Cauchy'ego–Schwarza i sumy stopni równej 2m.

Wniosek α(G) ≥ ⌈n/(1+2m/n)⌉ oraz oszacowanie przy średnim stopniu ≤d. Przykład K3 ⊔ K5: α=2 i pierwsza suma wynosi dokładnie 2, podczas gdy n²/(n+2m)=64/34<2. Przedstawiono również przypadek równości obu nierówności dla pełnych grafów.

### 42 — brakująca druga strona progu pojawiania się K_r

W pliku chapters/pl/graph_and_knot_theory/42-grafy-losowe-i-metoda-probabilistyczna.tex dodano twierdzenie thm:tg-random-clique-threshold i przykład ex:tg-random-clique-threshold.

Dla stałego r≥3 i p_n∈[0,1] zachodzą:
- jeśli n^{2/(r−1)}p_n→0, prawdopodobieństwo istnienia K_r w G(n,p_n) dąży do zera;
- jeśli n^{2/(r−1)}p_n→∞, prawdopodobieństwo istnienia K_r dąży do jedności.

Pierwszy kierunek wynika z oszacowania oczekiwanej liczby klik Z_r przez n^r p_n^{r(r−1)/2}/r! i z nierówności Markowa.
Drugi kierunek:
1. Rozpisano Z_r jako sumę wskaźników I_S, po jednym na r-elementowy zbiór S.
2. Wskaźniki różnych klik są niezależne dla przecięcia S∩T o liczności 0 lub 1. Dla przecięcia liczności j≥2 wspólnych krawędzi jest C(j,2), więc kowariancja wynosi p^{2C(r,2)−C(j,2)}−p^{2C(r,2)}.
3. Liczba T o przecięciu wielkości j z ustalonym S wynosi C(r,j)C(n−r,r−j). Dokładnie policzono wkład wszystkich takich par do wariancji i oszacowano Var(Z_r)/(E Z_r)^2 przez 1/E Z_r + Σ_{j=2}^{r−1} O(n^{-j}p^{-C(j,2)}).
4. Dla λ_n=n^{2/(r−1)}p_n→∞ mamy E Z_r~λ_n^{C(r,2)}/r!→∞ i n^j p_n^{C(j,2)} = λ_n^{C(j,2)} n^{j(r−j)/(r−1)}→∞ dla j=2,…,r−1. Stosując drugi moment otrzymujemy P(Z_r>0)→1.

Przykład porównujący K3 i K4: p_n=n^{-3/4}, a więc prawdopodobieństwo K3 dąży do jedności, podczas gdy prawdopodobieństwo K4 dąży do zera.

## Niezależne regresje matematyczne

Dodano plik:
tools/tests/test_graph_and_knot_flow_extremal_random_first_pass.py

Dodano osobny krok i wyzwalacz do:
.github/workflows/graph-and-knot-global-audit.yml

Testy opierają się na innych algorytmach niż twierdzenia w tekście:
- maxflow z dokładnymi pojemnościami całkowitymi porównano z wyczerpującym sprawdzaniem wszystkich przekrojów s,t; sprawdzono zachowanie przepływu w wierzchołkach wewnętrznych, dokładny rozkład integralnego przepływu na drogi i cykle oraz przepustowości jednostkowe;
- α(G) policzono niezależnie przez wyczerpującą enumerację wszystkich podzbiorów wierzchołków i porównano z oboma oszacowaniami Caro–Weiego;
- wariancje i kowariancje klik porównano w dokładnej arytmetyce wymiernej, niezależnie licząc pary zbiorów i liczbę ich wspólnych krawędzi. W osobnym oraklu policzono całą przestrzeń G(n,1/2) dla n≤5.

W zakończonym zadaniu structural-audit przebiegu
https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45279941031
uzyskano:
- przepływy: PASS — 2050 grafów testowanych z pojemnościami losowymi i jednostkowymi; 1550 wydzielonych ścieżek w rozkładach testowych;
- Caro–Wei: PASS — 3200 grafów losowanych, plus szczególne przykłady równości;
- wariancje klik: PASS — 54 zestawy parametrów i 6 pełnych enumeracji małych przestrzeni losowych;
- kontrola źródeł: 44/44, duplicate_labels=0, unresolved_references=0, environment_errors=0, forbidden_language=0;
- wszystkie wcześniej dołączone moduły matematyczne również PASS.

Przebieg źródłowo-testowy: commit 8bcc7d0c5f544e67bcf4e4fed4279f3823ca6462.
Ostatni commit zmieniający źródła TeX: 7f4664958cd8f5732b11ed5784fc742c9d262667.

## Wyniki końcowe CI, pełnego PDF i oględzin — PASS

### Niezależne regresje — PASS

Końcowy przebieg
https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45279941031
dla commitu 8bcc7d0c5f544e67bcf4e4fed4279f3823ca6462
potwierdził pomyślne zakończenie obu zadań:

1. structural-audit = success:
   - katalog źródeł 44/44;
   - duplicate_labels = 0;
   - unresolved_references = 0;
   - environment_errors = 0;
   - forbidden_language = 0;
   - nowe testy PASS: 2050 sieci przepływowych oraz
     osobno 2050 wariantów z pojemnościami 1,
     1550 wydzielonych ścieżek przepływu,
     3200 losowych grafów dla Caro–Weiego,
     54 porównania analitycznej wariancji klik
     z wyliczeniem zależności wspólnych krawędzi
     oraz 6 pełnych enumeracji modelu G(n,1/2);
   - wszystkie pakiety regresji wcześniejszych rozdziałów PASS.
2. full-book-pdf = success, z potrójną kompilacją pdflatex.

Nie traktujemy liczby 1550 ścieżek jako
niezależnych sieci. Jest to dodatkowa
liczba obiektów weryfikowanych
w ramach 2050 instancji przepływowych.

### Pełny skład 44-rozdziałowego tomu — PASS

Pobrano artefakt GitHub Actions
graph-and-knot-complete-book-audit,
**ID 14869880839**, z tego samego przebiegu.
Weryfikacja faktycznych plików artefaktu:

- PDF: **298 stron A4**;
- trzy istniejące logi pass1, pass2 i pass3
  zakończonych pomyślnie kompilacji pdflatex;
- plik graph_and_knot_full_warnings.txt
  o rozmiarze **0 bajtów**;
- tekst końcowego PDF zawiera
  nowy rozkład całkowitoliczbowego przepływu,
  nierówność Caro–Weiego
  i dwustronny próg występowania kliki.

W szczególności jest to **skład dla wersji
z trzema nowymi twierdzeniami i
z podłączonymi testami audytu 30**,
a nie wyłącznie PDF z poprzedniej iteracji.

### Oględziny wizualne źródłowych rozdziałów 40–42 — PASS

Rzeczywisty układ drukowanej książki:
źródłowe rozdziały 40, 41 i 42
odpowiadają drukowanym rozdziałom **9, 10, 11**.

Wyrenderowano i obejrzano wszystkie
**20 stron PDF 64–83** na pięciu arkuszach kontaktowych:

- **64–70**: źródłowy rozdział 40,
  pełny blok przepływów. Nowe twierdzenie
  o rozkładzie przepływów na str. **65–66**,
  poprawny układ wzoru i dowodu,
  diagram przepływu i przekroju na str. 67 i 69.
- **71–76**: źródłowy rozdział 41,
  twierdzenia Mantela, Turána i Ramseya.
  Nowa nierówność Caro–Weiego na str.
  **73–74**, przykład sumy klik,
  rysunki grafów dwudzielnych i C5.
- **77–83**: źródłowy rozdział 42,
  modele G(n,p), liczby trójkątów
  i izolowanych wierzchołków,
  próg spójności i nowy dwustronny próg
  klik na str. **81–82**,
  zastosowanie probabilistyczne do Ramseya.

Kontrola wizualna: nie znaleziono
uciętych wzorów, tekstu poza marginesami,
nakładających się podpisów rysunków,
kolizji etykiet ani urwanych diagramów.
Każda strona została rzeczywiście
wyrenderowana z końcowego PDF
i obejrzana.

## Końcowy werdykt audytu 30

**PIERWSZE SZCZEGÓŁOWE PRZEJŚCIE: PASS.**

Kryteria pierwszego przejścia zostały
spełnione łącznie: rzeczywiste matematyczne
zmiany w źródłach 40–42, niezależny
zestaw testów, sukces obu zadań CI,
trzy kompilacje pełnego 298-stronicowego
tomu i oględziny wszystkich 20 stron
audytowanego bloku.

Wyniki skryptów testowych oraz
składu LaTeX nie są formalnym
dowodem ogólnych twierdzeń.
Ich pełne dowody matematyczne
znajdują się w rozdziałach;
testy stanowią kontrolę
regresyjną i dodatkową weryfikację
przypadków skończonych.

**Rozdziały 40–42 pozostają
W STABILIZACJI**: wymagają
**audytu 31 — drugiego niezależnego przejścia**
z własnymi sprawdzeniami matematycznymi,
poprawkami, nowymi regresjami i
końcową bramką PDF/CI.

**Rozdziały 01–39 pozostają
LOKALNIE STABILNE.**
Do ukończenia całej książki
pozostała również kontrola
rozdziałów źródłowych 43–44.
Globalny audyt tomu 44 rozdziałów
nadal jest otwarty.
