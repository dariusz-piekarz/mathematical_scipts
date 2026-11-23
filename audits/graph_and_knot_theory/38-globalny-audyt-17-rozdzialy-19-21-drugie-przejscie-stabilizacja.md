# Teoria grafów i węzłów — globalny audyt 17: rozdziały 19–21, drugie przejście

Data: 2026-11-23. Gałąź: `biblioteka-matematyczna-iteracja-6`.
Kontynuacja [audytu 16](37-globalny-audyt-16-rozdzialy-19-21-pierwsze-przejscie.md).

## Zakres

Ponownie, niezależnie zrewidowano:
- **19.** grafy Taita, związek nawiasu Kauffmana z wielomianem Tutte'a i podpisane macierze Goeritza;
- **20.** zewnętrza węzłów, chirurgię Dehna, integralne macierze chirurgii, homologię nakryć rozgałęzionych i formy splecenia torsyjnego;
- **21.** torusy nieściśliwe, grafy grup JSJ, przypadki amalgamacji, HNN i wiązki torusowe.

Szczególnie skontrolowano znaki, orientacje, warunki injektywności,
nieosobliwość macierzy, związek równoważności geometrycznej
z niezmiennikami algebraicznymi, rysunki i odsyłacze.

## 19 — ważona dualność i znaki Goeritza

**Uzupełnienie dowodu:** dodano
`cor:tg-tait-weighted-dual`.
Dla spójnego grafu sferycznego `G` i przypisania
niezerowych wag `w_e` pokazano tożsamość
`τ_w(G)=(∏_e w_e)τ_{w^{-1}}(G*)`,
przy wagach dualnych `w*_{e*}=1/w_e`.
Dowód wykorzystuje dokładną bijekcję
`T↦{e*:e∉T}` drzew rozpinających obu grafów.
Działa dla wag ujemnych, nie wymaga dodatniej
określoności laplasjanu. Założenie
`w_e≠0` służy zdefiniowaniu odwrotności;
wagę zerową obsługuje zwykła formuła
ważonego twierdzenia Kirchhoffa.

**Przykład kontrolny konwencji znaków:** po
zmianie jednego skrzyżowania alternującego
trójlistnika podpisany graf Taita `C3`
ma wagi `(1,1,-1)`. Jego macierz
`G=[[0,-1,1],[-1,2,-1],[1,-1,0]]`
ma zredukowany wyznacznik `-1`,
co zgadza się z ważoną sumą drzew
`1-1-1=-1` i
`det(unknot)=1`. Bez zachowania znaków
zwykłe `τ(C3)=3` dawałoby błędny wynik.
Zapisano przykład
`ex:tg-goeritz-crossing-change`
oraz konkretną regresję.

Dwa wyniki **zewnętrzne** pozostają
jawne: klasyczne twierdzenie Goeritza
`|det G_reduced|=|Δ_K(-1)|`
oraz topologiczna realizowalność przejścia
między odpowiednimi diagramami przez
ruchy Reidemeistera. Testy skończonych
grafów nie zastępują ich dowodów.

## 20 — rachunek Kirby'ego, homologia i forma splecenia

**Nowe stwierdzenie** `st:kt-kirby-matrix`,
z pełnym dowodem. Dla symetrycznej całkowitej
macierzy chirurgii `Q` przesunięcie uchwytu
zmienia ją na `Q'=P^T Q P`,
`P∈GL_r(Z)`. Obejmuje to dodatnią
i ujemną orientację kopii drugiego
uchwytu. Odwzorowanie
`[x]↦[P^T x]` daje izomorfizm
`coker Q≅coker Q'`.

Jeżeli `det Q≠0`, to
`(Q')^-1=P^-1 Q^-1(P^T)^-1`;
stąd dokładnie
`-(P^T x)^T(Q')^-1(P^T y)=-x^T Q^-1y`.
Zatem zachowana jest forma splecenia
w `Q/Z`, nie tylko rząd homologii.
Dodanie rozdzielnego `±1`-ramowanego
węzła daje `Q⊕[±1]`:
koker ostatniego bloku jest zerowy,
a jego wkład do formy jest całkowity.
Oba ruchy zachowują więc również
torsyjną formę splecenia.

Doprecyzowano rozróżnienie:
wykazana **algebraiczna niezmienniczość**
nie jest pełnym twierdzeniem Kirby'ego,
którego zasadniczą treścią jest zupełność
ruchów opisujących wszystkie prezentacje
tej samej orientowanej trójrozmaitości.
Nie odtwarzano dowodów głębokich
twierdzeń Gordona–Lueckego,
Mostowa–Prasada, Lickorisha–Wallace'a
ani Thurstona.

Wnioski o homologii po `p/q`-chirurgii
sprawdzono z pełnej prezentacji
`<μ,ν|pμ=0,rμ−ν=0>`
(`ps−qr=1`). Cykliczne nakrycia
rozgałęzione porównano na blokowych
macierzach Alexandera dla trójlistnika
i węzła ósemkowego. Weryfikacja
znaku formy splecenia uwzględnia
przyjętą orientację brzegu śladu
czterowymiarowej chirurgii.

## 21 — grupa grafu JSJ i homologia wiązki torusowej

Zachowano jawne założenia
twierdzenia JSJ: spójna, zwarta,
orientowalna, nieprzywiedlna
trójrozmaitość z pustym lub
toroidalnym brzegiem.
Twierdzenie o istnieniu i jednoznaczności
minimalnego rozkładu jest przyjętym
głębokim wynikiem topologii.

Ponownie przeanalizowano konstrukcję
`π1(M)≅π1(𝒢)` dla grafu grup:
wybór drzewa rozpinającego
daje `s−1` amalgamacji, a
pozostałe krawędzie `m−s+1`
rozszerzeń HNN. Uwzględniono
pętle i dwa różne monomorfizmy
grupy krawędzi do grupy wierzchołka.

**Nowe stwierdzenie**
`st:tg-jsj-mapping-torus-h1`:
dla każdej monodromii `A∈SL2(Z)`
torusa odwzorowania `M_A` mamy
`H1(M_A;Z)≅Z⊕coker(A−I2)`.
Dowód przez abelianizację
`π1(M_A)=Z²⋊_A Z`;
stabilna litera pozostaje
generatorem wolnego składnika.
Dla `A=[[2,1],[1,1]]`
macierz `A−I2` jest unimodularna,
stąd `H1(M_A)=Z`.

**Nowy kontrprzykład**
`ex:tg-jsj-same-graph-different-h1`:
dla drugiej hiperbolicznej monodromii
`B=[[3,2],[1,1]]`
postac Smitha `B−I2` ma przekątną
`(1,2)`; stąd
`H1(M_B)=Z⊕Z/2Z`.
Obie rozmaitości mają geometrię Sol
oraz graf JSJ o jednym wierzchołku
i jednej pętli, ale różnią się
pierwszą homologią, więc nie są
homeomorficzne. To konkretne
uzasadnienie, dlaczego sam nieoznakowany
graf nie wystarcza bez danych sklejenia.

## Niezależna regresja

W istniejącym pliku
`tools/tests/test_graph_and_knot_tait_dehn_jsj.py`
dodano trzy rodziny dokładnych testów
bez wymagania zewnętrznych bibliotek:
- **648** kontroli ważonej dualności
  dla cyklu trójkątnego, trzech
  krawędzi równoległych i drzewa,
  przy dodatnich i ujemnych wagach
  niezerowych w pierścieniu liczb
  wymiernych;
- **2226** sprawdzeń kongruencji
  macierzy integralnej `P^TQP`,
  zgodności niezmienników Smitha,
  dokładnej wartości formy
  `Q^-1` i operacji `±1`;
- **116** macierzy monodromii z `SL2(Z)`
  i przypadków rang oraz torsji
  abelianizacji `Z²⋊_A Z`.

Zachowano poprzednie **894**
przypadki testowe (ważone
Kirchhoff, Tutte, chirurgia Dehna,
nakrycia, forma splecenia, JSJ).
Łącznie w obecnym teście:
**3884 przypadki z dziewięciu grup**
oraz dodatkowa jawna kontrola
`det(G_T^{(r)})=-1`
po zmianie skrzyżowania trójlistnika.

**Przebieg strukturalny**:
[GitHub Actions 45200337579](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45200337579),
`structural-audit=success`,
`44/44` rozdziały,
`0` powtórzonych etykiet,
`0` nierozwiązanych odsyłaczy,
`0` błędów środowisk,
`0` zakazanych terminów.

Nie należy utożsamiać sukcesu
skończonych testów z dowodem
ogólnych twierdzeń geometrycznych.

## Bramka końcowej stabilizacji

Do zamknięcia pozostaje sprawdzenie
rzeczywiście wygenerowanego końcowego
PDF 44-rozdziałowego tomu po wszystkich
zmianach audytu 17:
pełna trzykrotna kompilacja, brak
ostrzeżeń i przepełnień,
inspekcja rysunków, stron,
nowych macierzy, dowodów
i odsyłaczy. Po zakończeniu
tych kontroli blok 19–21
może uzyskać status
**lokalnie stabilny**, a
następny audyt obejmie 22–24.

Globalny audyt całego tomu
pozostaje otwarty.
