# Topologia ogólna — audyt globalny 09, techniczne dowody rozdziałów 12–18

**Data:** 2026-11-22.
**Zakres:** ponowna niezależna kontrola wybranych
trudnych argumentów z rozdziałów 12, 14, 16, 17
i 18, po audytach 07 (uzupełnienie jednostajne)
i 08 (Nagata--Smirnow).
**Wynik:** w sprawdzonych twierdzeniach nie znaleziono
błędów wymagających zmian w źródłach.
**Nie jest to reaudyt każdego środowiska proof
w rozdziałach 12–18.**

## Pliki i niezmienione identyfikatory źródła

- 12 `12-przestrzenie-jednostajne.tex` — `13597073db07742089b82ae3fc9878733dea5e88`.
- 14 `14-zwartosc-lokalna.tex` — `24ca61f0e19fe6674719fc76e53073aa82cc755c`.
- 16 `16-funkcje-ciagle-i-uzwarcenia.tex` — `1c2fcb925d62120feaea468400e48842a508a062`.
- 17 `17-uzwarcenia-aleksandrowa-i-cecha-stonea.tex` — `6c4e76dd0d2ea1e75a830f858af9d77d163bf7c4`.
- 18 `18-przestrzenie-odwzorowan-i-topologia-zwarto-otwarta.tex` — `f7340514548ed3dfb5d98793bf7068fd84276c30`.

## Rozdział 12 — struktury jednostajne, iloczyny i sieci Cauchy'ego

Sprawdzono twierdzenie o strukturze jednostajnej
produktu (linie 305–369) oraz kryterium Cauchy'ego
dla sieci w produkcie (581–609).

W relacji bazowej `E(F,(E_i))` ograniczenia dotyczą
**skończenie wielu** współrzędnych.
Przecięcie dwóch relacji realizuje się na sumie
skończonych zbiorów współrzędnych, a złożenie
kontroluje się przez wybór `H_i∘H_i⊂E_i`
dla wszystkich indeksów w danym skończonym zbiorze.
Przekroje relacji w punkcie są otoczeniami,
a odwrotnie dowolny otwarty cylinder zawiera taki przekrój.
Zgadza się to z topologią produktową.

Przy sieciach Cauchy'ego warunek współrzędny dla
każdego `i∈F` ma osobny indeks początkowy,
a skierowanie wspólnego zbioru indeksów
zapewnia wspólne ograniczenie górne
tej **skończonej** liczby indeksów.
Nie założono niesłusznie jednego indeksu
działającego dla wszystkich współrzędnych
jednocześnie. Pusta rodzina indeksów
jest obsłużona osobno.

## Rozdział 14 — zwartość lokalna dowolnych iloczynów

Prześledzono twierdzenie na liniach 148–195.
Dla iloczynu niepustych przestrzeni Hausdorffa
lokalna zwartość oznacza, że każdy czynnik
jest lokalnie zwarty oraz wszystkie poza
skończenie wieloma są zwarte.
Wystarczalność wynika z twierdzenia Tychonoffa
dla zwartych czynników i lokalnej zwartości
skończonego iloczynu. W konieczności
zwarty zbiór `K` zawiera otwarty cylinder
`B` ograniczający tylko skończenie wiele
współrzędnych `F`. Dla `i∉F`
rzutowanie `p_i(B)=X_i`, a zatem
`X_i=p_i(K)` jest zwarta.
Dla `i∈F` obraz zwartego `K`
zawiera otwarte otoczenie wybranej współrzędnej.
Powtarzając dla dowolnego punktu produktu
uzyskujemy lokalną zwartość wszystkich czynników.
Niepustość iloczynu z niepustych czynników
wykorzystuje zwykły wybór,
dopuszczony już w rozdziale Tychonoffa.

## Rozdział 16 — funkcje ciągłe i całkowita regularność

Sprawdzono twierdzenie funkcyjnego opisu
przestrzeni Tychonoffa (61–124).
Wynik wymaga aksjomatu `T_1`.
Całkowita regularność oddziela punkt
od zbioru domkniętego funkcją z wartościami
w `[0,1]`; w szczególności oddziela różne
punkty, ponieważ singletony są domknięte.
Od strony topologii początkowej
dla `x∈U` przeciwobraz
`(1/2,1]` przez dobraną funkcję
jest otwartym otoczeniem zawartym w `U`.
Dla kierunku odwrotnego z
bazy skończonych przecięć preobrazów
funkcji wybiera się funkcje
`h_j` oddzielające wartości `f_j(x)`
od dopełnienia stosownego przedziału;
maksimum skończenie wielu `h_j∘f_j`
daje oddzielenie punktu od
wyjściowego domkniętego `F`.
Nie znaleziono ukrytego założenia,
że rozdzielanie punktów samo wystarczy
do opisania całej topologii — rozdział
zawiera odpowiedni kontrprzykład.

## Rozdział 17 — uzwarcenia Aleksandrowa i Čecha--Stone'a

Kontrola objęła:
- przedłużanie właściwych odwzorowań
  `f:X→Y` do uzwarceń jednopunktowych
  (164–210): przeciwobraz otoczenia
  punktu nieskończoności jest otwarty
  dokładnie wtedy, gdy przeciwobrazy
  zwartych podzbiorów `Y`
  są zwarte w `X`;
- minimalność uzwarcenia Aleksandrowa
  (212–278): gęsty obraz lokalnie zwartego
  `X` jest otwarty w każdym uzwarceniu
  Hausdorffa, ponieważ odpowiedni
  lokalny kompakt `e(C)` jest
  domknięty w przestrzeni zwartej.
  Pozostałe punkty można utożsamić
  z jedynym punktem nieskończoności.
  Surjektywność zależy od **niezwartości**
  `X`, która zapewnia niepuste dopełnienie;
- uniwersalną własność `βX` (394–450):
  dla `g∈C(L,[0,1])`
  współrzędna przedłużenia ma postać
  `z_{g∘f}`. Obraz całego `βX`
  leży w domkniętym `e_L(L)`
  dzięki gęstości `e_X(X)`, a
  jednoznaczność daje Hausdorffowość `L`.

Równolegle potwierdzono, że dowód
całkowitej regularności przestrzeni
lokalnie zwartej Hausdorffa
używa Urysohna tylko na
**zwartym domknięciu** otoczenia,
a przedłużenie przez zero
skleja funkcje na dwóch zbiorach
domkniętych. Nie wymaga normalności
całej przestrzeni `X`.

## Rozdział 18 — topologia zwarto-otwarta i zupełność

1. Równoważność topologii zwarto-otwartej
   oraz zbieżności jednostajnej na
   zbiorach zwartych (170–255)
   nie wymaga Hausdorffowości `X`.
   Dla zwartego `K` obraz `f(K)`
   ma dodatnią odległość od
   domkniętego dopełnienia otwartego
   `U⊂Y`. W przeciwną stronę
   skończone pokrycie `g(K)`
   kulami prowadzi do zwartych
   `K_j=K∩g^{-1}(\overline B_j)`;
   domknięta podprzestrzeń zwartego `K`
   jest zwarta bez założenia T2.
   Oszacowanie trójkątne daje
   wymagane otoczenie zwarto-otwarte.
2. Ewaluacja i prawo wykładnicze
   (306–417) korzystają z
   **lokalnej zwartości Hausdorffa `X`**.
   W kierunku `F→\widehat F`
   zwartość `K` daje skończone
   podpokrycie dziedziny parametrów.
   W przeciwnym kierunku
   `F=ev∘(\widehat F×id_X)`,
   a ciągłość ewaluacji wymaga
   lokalnego zwartego otoczenia.
3. Metryka `D` z wyczerpania zwartego
   (468–537) wykorzystuje
   `K_n⊂int K_{n+1}`,
   by każdy zwarty podzbiór `X`
   mieścił się w pewnym `K_N`.
   Ogony szeregu metrycznego
   mają sumowalne oszacowanie;
   oszacowania dla skończonych
   `n≤N` dają zbieżność
   na dowolnym zwartym zbiorze.
4. Zupełność `C(X,Y)` dla zupełnej
   metrycznej `Y` (540–601)
   dowodzi jednostajnej zbieżności
   ciągu Cauchy'ego na `K_n`,
   a następnie ciągłości granicy
   lokalnie na `int K_n`.
   Nie wyprowadza błędnie
   ciągłości z samej
   punktowej zbieżności.

## Wynik

W sprawdzonych twierdzeniach
**nie znaleziono istotnych luk**;
żaden stabilny plik LaTeX
nie został zmieniony.
Raport uzupełnia wcześniejsze
audyty rozdziałów 13 i 15,
ale nie zamyka pełnej
weryfikacji wszystkich
dowodów rozdziałów 12–18.
Do osobnej kontroli wizualnej
służy audyt 10.
