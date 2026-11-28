# Topologia ogólna — globalny audyt 09, blok 12–18

**Data:** 2026-11-22.
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Zakres:** następna seria niezależnych kontroli dowodów,
ze skupieniem na rozdziałach 12, 14, 17 i 18.
Rozdziały 13 i 15 poddano
osobnym audytom globalnym 07 i 08.
Żaden zatwierdzony rozdział nie został
zmodyfikowany w tej iteracji.

## Źródła i identyfikatory

| Rozdział | Blob źródła | Liczba dowodów |
| --- | --- | ---: |
| 12 — przestrzenie jednostajne | `13597073db07742089b82ae3fc9878733dea5e88` | 14 |
| 13 — uzupełnienia | `33200912c034f3f946909f00b9e4068deeca4ed0` | 9 |
| 14 — zwartość lokalna | `24ca61f0e19fe6674719fc76e53073aa82cc755c` | 7 |
| 15 — parazwartość | `82e0fb5be75489017c8ea1844c698c87ce580901` | 7 |
| 16 — uzwarcenia ogólne | `1c2fcb925d62120feaea468400e48842a508a062` | 7 |
| 17 — uzwarcenia klasyczne | `6c4e76dd0d2ea1e75a830f858af9d77d163bf7c4` | 10 |
| 18 — przestrzenie odwzorowań | `f7340514548ed3dfb5d98793bf7068fd84276c30` | 9 |

Razem **63 środowiska dowodu** w rozdziałach 12–18.
W bieżącym raporcie sprawdzono poniższe
konkretne argumenty, nie każde z 63 środowisk.

## Rozdział 12: produkt przestrzeni jednostajnych

Sprawdzono twierdzenie
`thm:topog-jednostajne-iloczyn`.
Relacje E(F,(E_i)) zależą od
**skończenie** wielu współrzędnych.
Przecięcie dwóch warunków
odpowiada sumie skończonych zbiorów
indeksów, a powtarzające się współrzędne
obsługuje się przez przecięcie entourages.
Złożenie relacji jest kontrolowane
w każdej wskazanej współrzędnej
przez H_i∘H_i⊂E_i.
Przekrój E(F,(E_i))[x] jest
bazowym cylindrem otoczeń,
więc topologia jest rzeczywiście
topologią produktową.
Rzutowania są jednostajnie ciągłe,
ponieważ dla każdego E_i
przeciwobraz relacji pod π_i×π_i
jest jednym z entourages produktu.
Przypadek pustego zbioru indeksów
daje produkt jednoelementowy,
a pusty czynnik — pustą przestrzeń
z jedyną strukturą jednostajną.
Nie stwierdzono ukrytego użycia
metryzowalności.

## Rozdział 14: zwartość lokalna produktów i wyczerpanie

W twierdzeniu
`thm:topog-lokalna-dowolny-iloczyn`
zakłada się niepustość **każdego**
czynnika Hausdorffa.
W kierunku koniecznym z
kompaktowego otoczenia K punktu x
wybiera się cylinder B⊂K
z nieograniczonymi współrzędnymi
poza skończonym F.
Dla i poza F zachodzi
X_i=π_i(B)⊂π_i(K),
więc X_i jest zwarty.
Rzut π_i(K) jest zwartym
otoczeniem x_i.
Dla arbitralnego y_i∈X_i
niepustość pozostałych
czynników pozwala dopełnić
współrzędną do punktu produktu;
otrzymujemy lokalną zwartość
każdego X_i.
W kierunku wystarczającym
stosuje się Tychonoffa do
zwartych czynników i
stwierdzenie o skończonych produktach
do pozostałych.
Założenie niepustości jest
istotne: bez niego pusty produkt
przestrzeni z pustym czynnikiem
byłby lokalnie zwarty niezależnie
od innych czynników.

W `thm:topog-lokalna-wyczerpanie`
przy hipotezach lokalnej zwartości
i Hausdorffa sprawdzono:
- każde zwarte C mieści się we
  wnętrzu skończonej sumy
  zwartych otoczeń swych punktów;
- rekurencja K_{n+1}
  zawierająca K_n∪C_{n+1}
  **we wnętrzu** daje
  wyczerpanie o wymaganej
  monotoniczności;
- ze skończonego podpokrycia
  przez rosnące int K_n
  wynika, że każdy zwarty C
  mieści się w pewnym K_N.
To uzasadnia metryzację
przestrzeni odwzorowań w rozdziale 18.

## Rozdział 17: przedłużanie właściwych odwzorowań

W `thm:topog-uzwarcenia-aleksandrow-proper`
ciągłe f:X→Y między niezwartymi
lokalnie zwartymi Hausdorffa
przedłuża się ciągle do
f*:X*→Y*, f*(∞_X)=∞_Y,
wtedy i tylko wtedy, gdy f
jest właściwe.
Dla zbiorów otwartych
niezawierających ∞_Y
ciągłość wynika z ciągłości f.
Dla dopełnienia zwartego C⊂Y
przeciwobraz ma postać
X*\ f^{-1}(C), otwarty dokładnie
przy zwartości preobrazu.
W drugą stronę ciągłość
f* oznacza, że
(f*)^{-1}(C)=f^{-1}(C)
jest domkniętym podzbiorem
zwartego X*, a zatem
kompaktem w X.
Uwaga: zbiór zwarty w X*
zawarty w podprzestrzeni X
pozostaje zwarty w X,
ponieważ topologia na X
jest indukowana.
Nie ma tu błędnego
wniosku o domkniętości
w X* bez Hausdorffowości Y*.

W `thm:topog-uzwarcenia-aleksandrow-minimalne`
pokazano, że obraz e(X)
jest otwarty w dowolnym
uzwarceniu Hausdorffa K
lokalnie zwartej Hausdorffa X:
wybieramy U o zwartym
domknięciu C w X,
a gęstość e(X) daje
O⊂cl_K e(U)⊂e(C)⊂e(X).
Zatem dopełnienie e(X)
jest zwarte i niepuste
dla niezwartych X.
Złożenie reszty do jednego
punktu definiuje ciągłe
K→X*, zatem X* jest
minimalnym uzwarceniem
w zadanym porządku.

## Rozdział 18: ewaluacja, prawo wykładnicze i metryzacja

W `thm:topog-odwzorowania-wykladnicze`
dla lokalnie zwartej Hausdorffa X
sprawdzono:
- implikację F ciągłe ⇒
  odwzorowanie z↦F_z
  ciągłe do C_k(X,Y):
  z otwartości F^{-1}(U)
  i zwartości K wybiera się
  skończone pokrycie
  przekrojów po parametrze,
  co daje otwarte O×K
  w F^{-1}(U);
- implikację odwrotną
  przez ciągłość ewaluacji
  i tożsamość
  F=ev∘(\hat F×id_X).
  Nie zamienia się tych
  implikacji bez sprawdzenia
  lokalnej zwartości X.

W przykładzie X=Q
wykazano brak ciągłości
ewaluacji w (0,0).
Skończona suma kompaktów K_j
ma puste wnętrze w Q,
więc otoczenie 0 zawiera
punkt r poza nimi.
Funkcja
g(q)=min(1,d(q,K)/d(r,K))
jest ciągła, zerowa na K
i równa 1 w r.
Współczynnik d(r,K)>0
wynika z domkniętości K w Q;
przy K pustym stosuje się
funkcję stałą 1.
Przykład rzeczywiście
wykazuje brak ciągłości
ewaluacji w podanym punkcie.

W `thm:topog-odwzorowania-metryka-wyczerpanie`
d(x,y) to zbieżny szereg
ograniczonych pseudometryk
ρ_n opartych na wyczerpaniu
zwartym K_n.
Wykazano dodatnią określoność,
nierówność trójkąta oraz
równoważność z topologią
zbieżności jednostajnej
na zbiorach zwartych
dla **sieci**, nie wyłącznie ciągów.

W `thm:topog-odwzorowania-zupelnosc`
ciąg D-Cauchy jest jednostajnie
Cauchy na każdym K_n
i ma punktowe granice
w zupełnym Y.
Oszacowanie jest niezależne
od x∈K_n, więc granica
jest jednostajna na K_n.
Wnętrza K_n pokrywają X,
stąd f jest ciągła
lokalnie przy każdym punkcie.
Następnie zbieżność
jednostajna na zbiorach zwartych
daje D-zbieżność, czyli
zupełność metryki D.

## Wynik

**Brak nowych błędów w skontrolowanych
dowodach.** Zatwierdzone źródła
rozdziałów 12–18 zachowano
bez zmian. Audyt 09 jest
szczegółową kontrolą wybranych
argumentów z tego bloku.
Nie poświadcza audytu
dowód po dowodzie każdego
z 63 środowisk ani
wizualnego sprawdzenia
całego tomu. Globalny audyt
pozostaje otwarty.
