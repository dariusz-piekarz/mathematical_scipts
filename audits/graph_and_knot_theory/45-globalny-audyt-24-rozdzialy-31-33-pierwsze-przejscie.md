# Teoria grafów i węzłów — audyt globalny 24: rozdziały 31–33, pierwsze przejście

Data: 2026-11-23. Gałąź: `biblioteka-matematyczna-iteracja-6`.  
Dotychczasowe źródła **01–30 lokalnie stabilne** po drugich niezależnych przejściach.
Zakres: **pierwsze** szczegółowe przejście źródeł **31–33**.
Nie należy oznaczać tych rozdziałów jako lokalnie stabilnych przed audytem 25.

## Zakres przeglądu matematycznego

- **31** — konstrukcja Parka w `E(1)#4 CP²-bar`, klasa sfery
  o samoprzecięciu `−9`, konfiguracja `C_7`,
  liniowy graf plumbingu i brzeg `L(49,−6)`,
  równanie van Kampena, grupa `π_1`, rachunek
  `e,σ,b_2^±`, nieparzystość formy i Freedman.
- **32** — klasy pięciu sfer o samoprzecięciu `−2`,
  klasa kanoniczna, pierwsza kolumna `Q_7^{-1}`,
  formuła parowania po wymiernej kontrakcji,
  jawny dodatni rozkład `K_7·[ω_7]`,
  wybór komory przy `b_2^+=1`,
  zastosowanie Taubesa–Li–Liu i odróżnienie
  homeomorfizmu od dyfeomorfizmu.
- **33** — chirurgia wzdłuż węzła Fintushela–Sterna,
  część dołączana `S¹×E_K`, długość preferowana
  i meridian, ciągi Mayera–Vietorisa,
  warunki prostej spójności, formuła
  `SW_{X_K}=SW_XΔ_K(exp(2[T]))`,
  wielomiany dla K3, ograniczenia
  wykrywania struktur gładkich.

Dodatkowo sprawdzono zależności od
rozdziałów 23–30 i konsekwencję
konwencji orientacji brzegu.
Wyniki **Parka, Cassona–Harera,
Symington, Freedmana, Taubesa–Li–Liu
i Fintushela–Sterna** pozostają
jawnymi rezultatami zewnętrznymi,
nie są mylone z niezależnie
udowodnionymi tożsamościami
algebraicznymi.

## Rozdział 31 — bezpośredni metabolizer brzegu Parka

Dodano **lemat `lem:tg-park-metabolizer`**
z pełnym rachunkiem w cyklicznej
grupie `H_1(Y_7;Z)=Z/49`.
Dla meridianu składowej
o wadze `−9` mamy
`λ([μ_0],[μ_0])=−6/49 mod Z`
przy **jawnie przyjętej** konwencji
`λ=Q_7^{-1}`.

Z `gcd(6,49)=1`
wynika, że `[μ_0]` ma rząd 49.
Podgrupa
`M=7<[μ_0]>` ma rząd siedem;
jest izotropowa, ponieważ
`λ(7[μ_0],7[μ_0])=−6=0 mod Z`.
Jej ortogonalność charakteryzuje
warunek `−6x/7=0 mod Z`,
czyli dokładnie `7|x`.
Stąd **`M=M^⊥`**.

Z twierdzenia Cassona–Harera
pochodzi surjekcja
`H_1(Y_7)→H_1(B_7)=Z/7`.
Jej jądro ma rząd 7, a
w cyklicznej grupie rzędu
49 istnieje dokładnie jedna
podgrupa takiego rzędu.
A zatem **jądro jest `M`**.

To niezależne, konkretne
uzasadnienie mechanizmu
metabolizera; wyznacznik
macierzy sam w sobie nie
konstruuje wymiernej
kuli homologii.

## Rozdział 32 — oszacowanie ilościowe zamiast samego znaku

Dodano wniosek
`cor:tg-park14-quantitative-positive`
z pełnym dowodem:
dla liczb `b_j>0`,
`b_2≥b_3`,
`3a≥Σb_j` i
`B=b_{10}+b_{11}+b_{12}+b_{13}`
algebraiczny wzór na
`P=K_7·[ω_7]` daje
`7P=18(3a−Σb_j)+2(b_2−b_3)+
2b_5+b_6+b_8+2b_9+13B`.
Każdy składnik poza
ostatnim jest nieujemny,
a `B>0`. Otrzymujemy
ostre, ilościowe oszacowanie
**`P≥(13/7)B>0`**.

W szczególności do samego
rachunku znaku wystarcza
**słabszy warunek `3a≥Σb_j`**,
nie ścisła nierówność.
Zaznaczono jawnie, że
spełnianie tego algebraicznego
warunku nie gwarantuje
istnienia symplektycznej
reprezentacji klasy `[ω]`.
Geometryczny wybór formy
i jej zgodność z sześcioma
sferami pozostają zewnętrzną
częścią konstrukcji Parka.

## Rozdział 33 — wielomian Alexandera sumy spójnej i ograniczenia liczenia klas

Dodano stwierdzenie
`prop:tg-ks-connected-sum`,
z samodzielnym dowodem opartym
na powierzchniach Seiferta:
dla węzłów `K,J`
macierz Seiferta sumy
spójnej ma postać
`V_{K#J}=V_K⊕V_J`.
Wyznacznik `V−zV^T`
mnoży się na blokach,
a po symetrycznej
normalizacji otrzymujemy
`Δ_{K#J}(z)=Δ_K(z)Δ_J(z)`.
Zewnętrzna formuła
Fintushela–Sterna zastosowana
do K3 daje dalej
`SW_{E(2)_{K#J}}=Δ_K(u)Δ_J(u)`
dla `u=exp(2[T])`.

Dodano przykład
`ex:tg-ks-connected-trefoils`.
Dla dwóch dodatnich trójlistników:
`Δ_{T#T}(z)=z^(−2)−2z^(−1)+3−2z+z²`.
Dla węzła torusowego
`T(2,5)`:
`Δ(z)=z^(−2)−z^(−1)+1−z+z²`.

Obie chirurgicznie skonstruowane
czterorozmaitości mają po **pięć**
klas podstawowych, ale różne
multizbiory modułów współczynników
Seiberga–Wittena:
`{1,1,2,2,3}`
wobec `{1,1,1,1,1}`.
Są więc **homeomorficzne
z K3**, lecz **nie są
dyfeomorficzne między sobą**.
Pokazuje to, że
**sama liczba klas podstawowych**
nie zawsze wystarcza, choć
pełny wielomian rozróżnia te
dwie konstrukcje.

Formułę chirurgiczną i zależność
zmiennej `u=exp(2[T])`
sprawdzono względem
[wykładów Fintushela i Sterna](https://bpb-us-e2.wpmucdn.com/faculty.sites.uci.edu/dist/3/246/files/2011/03/57_Six_Lectures.pdf),
gdzie spotyka się równoważny
zapis z `Δ_K(t²)`.

## Niezależne regresje matematyczne

Utworzono
`tools/tests/test_graph_and_knot_park_knot_surgery.py`
i włączono do
`.github/workflows/graph-and-knot-global-audit.yml`.
Testy wykonują dokładne rachunki
na całych liczbach i ułamkach,
bez zaokrągleń zmiennoprzecinkowych.

Kontrole:
1. **38** dokładnych rachunków
   w bazie `h,e_1,…,e_13`:
   `f²=0`, przecięcia
   `f·e_j=1`, `s²=−9`,
   pełna macierz przecięcia
   sześciu klas `u_i`
   oraz parowania klasy
   kanonicznej `K_R·u_i`.
2. **2401** par elementów
   cyklicznej grupy `Z/49`:
   symetria formy splecenia,
   jej zgodność z dodawaniem,
   ortogonalność do `M`
   i izotropowość `M`.
3. **4001** przykładów
   parametrów `a,b_1,…,b_13`:
   niezależne obliczenie
   parowań z klasami sfer,
   rozwinięcie współczynników,
   dekompozycja na
   nieujemne składniki
   i dolne oszacowanie
   `P≥13B/7`, wraz z
   modelem liczbowym
   podanym w rozdziale.
4. **65** sprawdzeń
   iloczynów symetrycznie
   znormalizowanych
   wielomianów Alexandera
   dla `T(2,2n+1)`,
   `1≤n≤8`,
   i sum spójnych,
   z przykładem porównania
   `T#T` i `T(2,5)`.

Łącznie **6505 nowych
dokładnych przypadków**.
Testy sprawdzają jedynie
konsekwencje algebraiczne
hipotez twierdzeń —
nie dowodzą istnienia
konkretnego zanurzenia
`C_7`, regularności
przestrzeni moduli ani
globalnej formuły
sklejania niezmienników.

## CI i bramka pierwszego przejścia

Uruchomienie końcowe:
[GitHub Actions 45233297909](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45233297909)
dla commitów źródeł i testów
zawierających wszystkie
powyższe poprawki.

Wymagamy niezależnie:
- `structural-audit=success` z **44/44** źródeł,
  bez duplikatów etykiet,
  nierozwiązanych odsyłaczy
  i błędów środowisk;
- **6505** nowych przypadków `PASS`,
  a także wykonania wcześniejszych regresji;
- `full-book-pdf=success`,
  trzech pełnych kompilacji `pdflatex`,
  braku ostrzeżeń i przekroczonych marginesów;
- oględzin rzeczywistego PDF
  wszystkich stron rozdziałów 31–33,
  zwłaszcza rysunków sfer Parka,
  macierzy formy przecięcia,
  diagramu wymiernej kontrakcji
  i schematów `knot surgery`.

**Werdykt tymczasowy: pierwszy audyt 31–33
w realizacji; status lokalnej
stabilizacji nadal OTWARTY.**
Po potwierdzeniu bramki pierwszy
audyt otrzyma PASS, ale rozdziały
31–33 nadal wymagają drugiego
niezależnego przejścia,
czyli audytu 25.

Rozdziały **01–30** pozostają
lokalnie stabilne. Audyt globalny
wszystkich 44 rozdziałów trwa.
