# Teoria grafów i węzłów — audyt globalny 25, rozdziały 31–33: drugie niezależne przejście

Data: 2026-11-23. Gałąź: `biblioteka-matematyczna-iteracja-6`.
Pierwsze przejście: [audyt 24](45-globalny-audyt-24-rozdzialy-31-33-pierwsze-przejscie.md).
Blok 01–30 pozostaje lokalnie stabilny.

**Przedmiot:** rozdział 31 — konstrukcja i topologia egzotycznej rozmaitości Parka; rozdział 32 — niezmienniki SW i egzotyczność Parka; rozdział 33 — chirurgia wzdłuż węzła.

Drugi audyt wykonuje nowe, niezależne kontrole. Nie powtarza wyłącznie tabel regresji audytu 24.

## Matematyczna kontrola dotychczasowych twierdzeń

**Rozdział 31.** Ponownie sprawdzono macierz przecięcia
`Q_7`, wyznacznik `49`, określoność ujemną,
łańcuchowy ułamek `49/6`, orientację formy splecenia,
cykliczność `H_1(Y_7)`, użycie normalnej generacji grupy fundamentalnej oraz oddzielenie twierdzenia Parka o geometrii i prostej spójności dopełnienia od rachunku macierzowego.
Bez zmian pozostają jawne założenia zewnętrzne: istnienie symplektycznego zanurzenia, konstrukcja Cassona–Harera, symplektyczna wymierna kontrakcja Symington i klasyfikacja Freedmana.

**Rozdział 32.** Sprawdzono pierwszą kolumnę `Q_7^{-1}`,
tożsamość parowania kanonicznego, dwa niezależne rozwinięcia współczynników,
nierówność ilościową oraz miejsce twierdzenia o istnieniu zgodnej formy symplektycznej.
Zidentyfikowano rzeczywiste niebezpieczeństwo logiczne: nierówności formalnych współczynników nie gwarantują dodatnich pól wszystkich sfer, zatem nie można traktować ich jako pełnego kryterium geometrycznego. Sprawdzono także użycie małych perturbacji i rozróżnienie komór przy `b_2^+=1`; twierdzenie Taubesa–Li–Liu pozostaje zewnętrzne.

**Rozdział 33.** Przejrzano identyfikację brzegową
`m_T↔λ_K`, homologię `S^1×E_K`, warunki van Kampena i Freemana, zmienną `u=exp(2[T])`, niezmienniczość multizbioru modułów współczynników SW oraz logiczne ograniczenia wykrywania struktur gładkich. Odróżniono niezmiennik grupowy od twierdzenia o dyfeomorfizmie. Formuła Fintushela–Sterna pozostaje twierdzeniem zewnętrznym, zgodnie z [wykładami Fintushela–Sterna](https://bpb-us-e2.wpmucdn.com/faculty.sites.uci.edu/dist/3/246/files/2011/03/57_Six_Lectures.pdf).

## 31 — pełna odwrotność macierzy Parka

Dodano lemat `lem:tg-park-Q-inverse-full` z kompletnym algebraicznym dowodem. Dla `0≤i,j≤5`:
`(Q_7^{-1})_{ij}=−[(8 min(i,j)+1)(6−max(i,j))]/49`.

Dowód konstruuje macierz kandydatkę `G`,
sprawdza kolejno wszystkie wewnętrzne wiersze trójdiagonalnego `Q_7G`,
wiersze brzegowe i przypadek `i=j`, uzyskując `Q_7G=I_6`.
To wzmacnia wcześniejszy rachunek tylko pierwszej kolumny.

W szczególności diagonalne ułamki formy splecenia
mają liczniki (ze znakiem ujemnym)
`6,45,68,75,66,41`,
ze wspólnym mianownikiem `49`.
Wszystkie te liczby są względnie pierwsze z `49`.
Biliniowość niezdegenerowanej formy splecenia
dowodzi więc, że **każdy** z sześciu
meridianów składowych jest generatorem
`H_1(Y_7;Z)=Z/49`.

Lemat jest zgodny z metabolizerem `M=7Z/49`
z audytu 24. Nie zakłada realizacji samego plumbingu
w powierzchni eliptycznej.

## 32 — kontrprzykład do nieuprawnionego wnioskowania geometrycznego

Dodano przykład `ex:tg-park14-cone-not-sufficient`.
Ustalmy
`a=10, b_1=b_2=b_3=4, b_4=…=b_13=1`.
Wtedy:
- `a≥b_1≥…≥b_13>0`,
- `3a=30>22=Σ b_j`,
- jednak dla rzeczywistej klasy `v_3=h−e_1−e_2−e_3`
  otrzymujemy
  `[β]·v_3=10−4−4−4=−2`.

Jeżeli `v_3` ma reprezentanta będącego
symplektyczną sferą w ustalonej orientacji i
`[β]` jest klasą zgodnej formy,
jej pole musi być **ściśle dodatnie**.
Ponieważ tutaj pole byłoby ujemne, formalne
nierówności na współczynniki **nie stanowią
warunku wystarczającego** zgodności geometrii.

To nie przeczy poprawnie sformułowanemu
Twierdzeniu `thm:tg-park14-cone`, które
**zewnętrznie zakłada jednoczesne istnienie**
formy i realizacji symplektycznych sfer.
Usuwa jednak ryzyko fałszywego utożsamienia
arytmetyki ze złożoną konstrukcją Parka.

## 33 — rodzina par nierozróżnialnych samą liczbą klas podstawowych

Dodano twierdzenie `thm:tg-ks-equal-basic-count`
z pełnym dowodem kombinatorycznym.
Dla `n≥2` weźmy:
- `K_n=#^n T(2,3)` — suma spójna `n` trójlistników;
- `J_n=T(2,2n+1)` — węzeł torusowy.

Multiplikatywność Alexandera i twierdzenie Fintushela–Sterna dają dla K3:
`SW_{E(2)_{K_n}}=(u^{-1}−1+u)^n` oraz
`SW_{E(2)_{J_n}}=Σ_{j=−n}^n (−1)^{n−j}u^j`.

W dowodzie wykazano, że wszystkie `2n+1`
współczynniki pierwszego wielomianu są niezerowe:
dla składnika o wykładniku `j`
każda kombinacja czynników ma
ten sam znak `(−1)^{n−j}`;
nie występuje znoszenie współczynników.
Współczynnik przy `u^{n−1}` jest dokładnie `−n`,
a więc dla `n≥2` jego moduł jest większy od jedności.
W wielomianie drugiej rodziny wszystkie
moduły współczynników są równe jedności.

Włókno K3 ma klasę pierwotną, a zatem
różne wykładniki opisują różne klasy podstawowe.
Obie rozmaitości mają **po `2n+1`
klas podstawowych** i są **homeomorficzne z K3**,
ale nie są dyfeomorficzne między sobą,
ponieważ różne są multizbiory modułów
niezerowych współczynników SW.
Ta rodzina wyjaśnia, dlaczego sama
liczba klas podstawowych jest
niewystarczającym niezmiennikiem.

## Nowe, niezależne testy regresyjne

Utworzono
`tools/tests/test_graph_and_knot_park_knot_surgery_second_pass.py`
i włączono do
`.github/workflows/graph-and-knot-global-audit.yml`
w oddzielnym kroku, zachowując regresje audytu 24.

Wyniki potwierdzone w zadaniu `structural-audit`
przebiegu [45247833818](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45247833818):

1. **42** dokładne kontrole: niezależna
   eliminacja Gaussa–Jordana w `Q`,
   wszystkie **36** wpisów `Q_7^{-1}`
   i sześć wartości diagonalnych.
2. **1802** kontrole uogólnionych macierzy
   `C_p` dla `2≤p≤18`,
   za każdym razem z niezależną odwrotnością
   liczona nad ułamkami.
3. **504** kontroli formalnych klas
   spełniających nierówności „stożkowe”,
   lecz mających ujemne pole na sferze
   `v_3`, w tym nowy przykład źródłowy.
4. **1839** sprawdzeń wielomianów
   `(z^{-1}−1+z)^n`
   dla `1≤n≤40`, w tym niezerowości
   współczynników, znaków, symetrii,
   wartości `−n`, mnożenia
   wielomianów i różnicy multizbiorów
   modułów dla `n≥2`.

Łącznie **4187 NOWYCH przypadków, PASS**.
Wraz z audytem 24: **10 692 przypadki**
dwóch niezależnych modułów dotyczących Parka
i chirurgii wzdłuż węzła.

Ponadto CI wykonał wcześniejsze
testy całego tomu, w tym regresje
rozdziałów 01–30. W tych testach
nie przypisuje się dowodom analitycznym
statusu potwierdzenia formalnego.

## CI i kontrola składu PDF

Końcowy przebieg dla źródeł i testów:
[GitHub Actions 45247833818](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45247833818),
commit źródłowo-testowy
`092613a1ab3bf0d16943b3526803b950d9caa168`.

Zadanie **`structural-audit=success`**:
- **44/44** rozdziały;
- **0** duplikatów etykiet, **0** niezwiązanych odsyłaczy;
- **0** błędów środowiska i **0** zakazanych terminów;
- wszystkie **4187** nowych przypadków: PASS.

Do pełnego zamknięcia bramki należy jeszcze
potwierdzić `full-book-pdf=success`
po trzech kompilacjach `pdflatex`,
sprawdzić brak ostrzeżeń i obejrzeć
strony rozdziałów 31–33,
w szczególności nowe długie macierze
i dowód rodzin węzłów.

**Status rozdziałów 31–33 pozostaje
„w stabilizacji” do zamknięcia
tej ostatniej bramki.**
Wówczas będzie można uznać
rozdziały 01–33 za lokalnie stabilne.
Następna iteracja: audyt 26
(pierwsze przejście rozdziałów 34–36).
Audyt globalny 44 rozdziałów
pozostaje otwarty.
