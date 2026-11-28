# Topologia ogólna — rozdział 24, audyt 02 (pierwszy czysty)

**Data:** 2026-11-22. **Blok źródła:** `4b72d373d98eab0c1cc4563b72a6bb8fa62170b6`.
**Wynik:** CZYSTY 1/2 dla źródła po korektach audytu 01.
**Ograniczenie:** końcowy PDF musi jeszcze uzyskać zielony CI i oględziny.

## Niezależne sprawdzenie trudniejszych argumentów

### Birkhoff–Kakutani

Dla symetrycznej bazy otoczeń \(U_0=G\),
\(U_{n+1}^3\subseteq U_n\cap B_{n+1}\),
z Hausdorffowości wynika \(\bigcap U_n=\{e\}\).
Funkcja \(\rho(g)=\inf\{2^{-n}:g\in U_n\}\)
jest równa 0 tylko w e, a dla \(g\neq e\)
jest jedną z wag dyadycznych, więc minimum jest osiągnięte.

Kluczowy krok: jeśli \(\sum_{j=1}^m\rho(g_j)<2^{-n}\),
to \(g_1\cdots g_m\in U_n\).
Niezależnie zweryfikowano indukcję po liczbie czynników:
- przy sumie wag mniejszej niż \(h=2^{-(n+1)}\)
  rozdzielamy pierwszy czynnik i resztę, z których
  każda ma sumę mniejszą niż h i liczbę czynników
  mniejszą niż m;
- przy \(h\le S<2h\) rozdzielamy iloczyn
  na prefiks o sumie <h, jeden środkowy czynnik
  o wadze <=h (dyskretność wag dyadycznych)
  i sufiks o sumie <h.
  Każda część jest w \(U_{n+1}\),
  a \(U_{n+1}^3\subseteq U_n\).
Ten podział działa także przy pustym prefiksie/sufiksie
i przy czynniku o wadze zero.

Metryka łańcuchowa jest skończona (\(d\le\rho\le1\)),
symetryczna, spełnia nierówność trójkąta przez
składanie łańcuchów i jest dodatnio określona:
gdy \(x^{-1}y\notin U_n\), żadna ścieżka
łącząca x z y nie ma kosztu <\(2^{-n}\).
Lewostronna niezmienniczość wynika ze wzoru
\((gx)^{-1}(gy)=x^{-1}y\).
Inkluzje \(U_{n+1}\subset B_d(e,2^{-n})\subset U_n\)
i translacje dowodzą zgodności topologii.
Wniosek o metryce prawostronnie niezmienniczej
korzysta wyłącznie z ciągłości odwracania.

### Działanie i ilorazy

Ciągłość całego działania \(G\times G/H\to G/H\)
wynika z faktu, że \(\mathrm{id}_G\times q\) jest
otwartą surjekcją i ilorazowością tej funkcji.
Dla H nienormalnej nadal mamy poprawną,
topologiczną przestrzeń warstw, ale
mnożenie warstw \((gH)(kH)=gkH\)
nie musi być dobrze określone.
Model \(S_3/\langle(1\,2)\rangle\)
pokazuje to w trzech dyskretnych warstwach.

Przypadek H domkniętej, ale nienormalnej:
\(G/H\) jest Hausdorffa mimo braku struktury grupy.
Warunek normalności w twierdzeniu o grupie ilorazowej
jest więc konieczną hipotezą algebraiczną,
nie topologicznym skrótem.
Dla normalnej N ciągłość działania w G/N
wynika z ilorazowości \(q\times q\).
Pierwsze twierdzenie o izomorfizmie
wymaga otwartości f lub równoważnego
warunku ilorazowości; nie wnioskujemy
jej z samej ciągłości i bijektywności.

### Składowa spójna i struktury jednostajne

Dla \(G^0\) spójność iloczynu \(G^0\times G^0\)
i ciągłość \(xy^{-1}\) zapewniają podgrupowość.
Sprzężenia zachowują składową neutralną,
dając normalność. Otwartość q oraz
spójność jego włókien zapewniają,
że przeciwobraz dowolnego spójnego
podzbioru ilorazu jest spójny:
dwa rozłączne nasycone otwarte rozdzielenia
przeniosłyby się przez q na rozdzielenie
spójnego zbioru w ilorazie.
Gdy C zawiera eG^0, jego przeciwobraz
musi być zawarty w składowej G^0,
a zatem C jest jednoelementowy.
Translacje dają całkowitą niespójność.

Lewe i prawe struktury jednostajne
indukują pierwotną topologię i
mają odpowiednie własności niezmienniczości.
Odwracanie jest izomorfizmem
między lewą a prawą strukturą,
lecz bez założenia przemienności
nie deklarowano ich równości.

## Pliki i odsyłacze

Rozdział zawiera 41 różnych etykiet
oraz 14 lokalnych odsyłaczy; wszystkie
mają cele w tym samym pliku.
21 środowisk dowodu i pozostałe
środowiska twierdzeń i rysunków
są poprawnie sparowane.
Sprawdzono zgodność terminologiczną.
Nie zmieniano źródła w tej iteracji.

Test `tools/tests/test_general_topology_ch24.py`
obejmuje modele S3, grup cyklicznych,
ilorazu R/Z, działania na warstwach
i konstrukcji metryki Birkhoffa–Kakutaniego.
Są to testy regresyjne, nie dowód
poprawności ogólnej.

**Status po audycie 02: czysty 1/2 na identycznym blobie.
Oczekiwana dalsza niezależna kontrola matematyczna,
a następnie dodatkowy audyt i oględziny nowego PDF.**
