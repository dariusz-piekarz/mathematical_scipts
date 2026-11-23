# Teoria grafów i węzłów — audyt globalny 16: historyczne rozdziały 19–21, pierwsze przejście

Data: 2026-11-23. Gałąź: `biblioteka-matematyczna-iteracja-6`.  
Poprzedni blok: rozdziały 16–18, lokalnie stabilne po audycie 15.

## Zakres i werdykt

Pierwsze szczegółowe przejście rozdziałów:
- **19.** Grafy Taita, wielomian Tutte'a i macierze Goeritza (pierwotnie 287 wierszy);
- **20.** Uzupełnienia węzłów, geometria i chirurgia Dehna (pierwotnie 767 wierszy);
- **21.** Grafy rozkładów JSJ i grupy trójrozmaitości (pierwotnie 210 wierszy).

Kontrola obejmuje hipotezy i kwantyfikatory, algebraiczne i
topologiczne szczegóły dowodów, zgodność konwencji, zależności
od twierdzeń zewnętrznych, LaTeX, odsyłacze, testy i rysunki.

**Werdykt: pierwsze przejście matematyczne PASS po uzupełnieniach,
ale blok 19–21 pozostaje W STABILIZACJI.** Należy powtórzyć
niezależnie kontrolę najtrudniejszych twierdzeń i diagramów
oraz zweryfikować końcowy skład PDF. Audyt całego
44-rozdziałowego tomu pozostaje otwarty.

## Rozdział 19 — grafy Taita, Tutte, Goeritz

1. Sprawdzono argument barwienia szachownicowego
   planarnych diagramów i dualności dwóch grafów Taita.
   Barwienie wynika z parzystości przecięć zamkniętej
   krzywej z czteroregularnym diagramem jako cyklem nad
   `F_2` na sferze.
2. Ponownie przeprowadzono identyfikację stanu
   wygładzeń ze spójnymi składowymi regularnego otoczenia
   podgrafu `(V,F)`. Liczba okręgów stanu to
   `b(F)=2k(F)-v+|F|`; podstawienie do
   sumy stanu nawiasu i sumy Tutte'a zgadza się
   dla `x=-A^-4`, `y=-A^4`, z prefaktorem
   `A^(2v-e-2)`. Kluczowa jest spójność grafu i
   jednolita konwencja czarnego wygładzenia.
3. Z Cauchy'ego–Bineta sprawdzono podpisane twierdzenie
   Kirchhoffa dla macierzy
   `L=B diag(w_e) B^T`, także dla wag ujemnych
   i krawędzi pętlowych (zerowe kolumny incydencji).
4. **Nowy dowód** `thm:tg-tait-dual-trees`: dla spójnego
   sferycznego grafu `G` drzewo `T` ma `v-1`
   krawędzi; jego dualne dopełnienie ma `f-1`
   krawędzi i jest spójne, ponieważ dopełnienie
   realizacji drzewa na sferze jest spójne.
   Uzyskujemy bijekcję drzew rozpinających
   `G` i `G^*` i równość `τ(G)=τ(G^*)`.
   W twierdzeniu Goeritza dopisano
   `det(K)=τ(G_B)=τ(G_W)` dla diagramu
   alternującego przy jednolitych znakach.
5. **Nowy kontrprzykład ostrzegawczy**: dwie równoległe
   krawędzie o wagach `+1` i `-1` dają
   `τ=2`, a podpisany laplasjan zerowy i
   sumę ważoną `0`. Dlatego w przypadku
   niealternującym nie wolno zastępować
   ważonej sumy drzew zwykłą liczbą drzew.
6. Identyfikacja wyznacznika Goeritza z
   `|Δ_K(-1)|` pozostaje jawnym klasycznym
   twierdzeniem o dwukrotnym nakryciu
   rozgałęzionym; sam wzór Kirchhoffa
   nie jest jego dowodem.

## Rozdział 20 — chirurgia, geometria i nakrycia

1. Ponownie skontrolowano parę meridian–długość
   i argument, że nieściśliwość brzegu
   zewnętrza węzła jest równoważna nietrywialności
   węzła. **Uzupełnienie:** uzasadniono geometrycznie
   istnienie pierścienia pomiędzy krzywą podłużną
   na brzegu torusa pełnego a jego rdzeniem.
   Sama równość klas homologii była poprzednio
   zbyt krótkim uzasadnieniem istnienia pierścienia.
2. Wypełnienie Dehna o nachyleniu `p/q`:
   przy `ps-qr=1` krzywe
   `pμ+qλ` i `rμ+sλ` tworzą bazę.
   Pierwsza daje relację `p[μ]=0`;
   druga relację `r[μ]-ν=0`,
   gdzie `ν` jest rdzeniem doklejonego
   torusa pełnego. Po eliminacji `ν`
   otrzymujemy `H1(S³_{p/q}(K))=Z/(p)`,
   w tym rangę jeden dla `p=0`.
   To **nowy pełny rachunek Mayera–Vietorisa**.
3. Kontrola integralnej chirurgii na splocie:
   klasa preferowanej długości `λ_i`
   w zewnętrzu całego splotu to
   `Σ_{j≠i}lk(K_i,K_j)[μ_j]`.
   Stąd `H1(M_L)=coker(Q_L)`.
   Dla `det Q≠0` rząd wynosi `|det Q|`.
4. Nakrycia rozgałęzione: zweryfikowano
   wyprowadzanie macierzy `V+V^T` dla
   `Σ_2(K)` z modelu uchwytowego
   rozgałęzionego nakrycia czterokuli.
   Konstrukcja uchwytowa pozostaje
   jawnie założonym lematem geometrycznym.
   Dla `Σ_d(K)` analiza `tV-V^T`
   po `t^d=1` daje iloczyn
   `∏_{j=1}^{d-1}Δ_K(ζ_d^j)` przy
   niezerowych czynnikach.
5. Forma splecenia na wymiernej sferze
   homologicznej: sprawdzono niezmienniczość
   formuły `-x^T Q^-1 y mod Z` pod
   `x→x+Qz` i analogicznym przesunięciem
   `y`; znak zależy od przyjętej konwencji
   orientacji czterorozmaitości.
6. Twierdzenia Gordona–Lueckego,
   Mostowa–Prasada, hiperbolizacji,
   Lickorisha–Wallace'a, Kirby'ego i
   hiperbolicznej chirurgii Dehna są
   świadomie traktowane jako zaawansowane
   twierdzenia zewnętrzne, a nie dowody
   wynikające wyłącznie z wcześniejszych
   obliczeń. Konwencje nachylenia i
   orientacji wymagają jeszcze niezależnej
   kontroli w drugim przejściu.

## Rozdział 21 — rozkład JSJ i teoria Bassa–Serre'a

1. Sprawdzono założenia twierdzenia
   Jaco–Shalena–Johannsona:
   zwartość, orientowalność, spójność,
   nieprzywiedlność oraz pusty lub
   toroidalny brzeg. Istnienie i
   jednoznaczność minimalnej rodziny
   torusów JSJ pozostają jawnie przyjęte.
2. Dowód spójności grafu JSJ wykorzystuje
   ścieżkę w rozmaitości poprzeczną
   do skończonej rodziny torusów.
3. **Nowe Twierdzenie**
   `thm:tg-jsj-graph-of-groups`:
   przypisując częściom `π1(M_v)`,
   a torusom `π1(T_e)=Z²`,
   otrzymujemy graf grup o
   `π1(M)≅π1(𝒢)`.
   Po wybraniu drzewa rozpinającego
   grafu o `s` wierzchołkach i
   `m` krawędziach `s-1`
   sklejeń daje amalgamacje,
   zaś `m-s+1=b1(Γ)`
   pozostałych krawędzi daje HNN.
   Dowód używa kołnierzy, van Kampena
   i injektywności grup torusów.
4. **Nowy przykład** `ex:tg-jsj-sol-torus-bundle`:
   wiązka torusowa o monodromii
   `A=[[2,1],[1,1]]`, `det A=1`,
   `tr A=3`, ma nierozdzielające
   włókno torusowe, graf z jednym
   wierzchołkiem i krawędzią pętlową.
   Przedstawiono grupę
   `Z²⋊_A Z` z relacjami HNN.
   Klasyfikacja geometrii Sol i
   kanoniczny status torusa włóknowego
   są klasycznymi wynikami zewnętrznymi.
5. Graf dualny sam nie określa
   orientacji torusów, obrazów
   monomorfizmów w grupach części
   ani pełnych danych homeomorfizmów
   sklejeń.

## Niezależne regresje algebraiczne

Dodano `tools/tests/test_graph_and_knot_tait_dehn_jsj.py`
do `.github/workflows/graph-and-knot-global-audit.yml`.

W zadaniu `structural-audit` przebiegu
[45186268759](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45186268759)
test nowych rozdziałów zakończył się sukcesem:
- **377** instancji podpisanej tożsamości
  macierz–drzewo, w tym znoszenie dodatnich
  i ujemnych wag;
- **5** niezależnych porównań wzoru
  nawiasu Kauffmana ze specjalizacją
  wielomianu Tutte'a dla małych
  grafów planarnych;
- **176** przypadków nachyleń
  `p/q` z rozwiązaniami Bézouta
  i pełną prezentacją `H1`;
- **12** przypadków zgodności
  wyznacznika macierzy blokowej
  nakrycia cyklicznego z
  `det Δ(C_d)` dla trójlistnika
  i węzła ósemkowego;
- **318** przypadków formy splecenia
  z całkowitych macierzy chirurgii
  i niezmienniczości przy przesunięciu
  o wektor relacji;
- **6** modeli grafów JSJ
  sprawdzających liczbę
  krawędzi drzewa i HNN.

Globalna regresja strukturalna:
`44/44` pliki i katalog,
`0` duplikatów etykiet,
`0` brakujących odsyłaczy
oraz `0` błędów struktury środowisk.
Wyniki skończone nie zastępują dowodów
twierdzenia Goeritza, JSJ, Lickorisha
ani innych twierdzeń ogólnych.

## Stabilizacja przed 22–24

1. **Drugie niezależne przejście**
   szczególnie rozdziałów 19 i 20:
   znaki macierzy Goeritza, orientacje
   chirurgii i formy splecenia,
   rozróżnienie nakrycia rozgałęzionego
   i nierozgałęzionego, liczby
   homologii po wypełnieniu.
2. **Sprawdzić końcowy rzeczywisty PDF**
   po najnowszym commicie:
   ilustracje Taita, model torusa,
   diagram nachylenia i graf JSJ;
   sprawdzić ostrzeżenia i marginesy.
3. Dopiero po tych bramkach
   oznaczyć rozdziały 19–21
   jako lokalnie stabilne i
   rozpocząć audyt 22–24.
