# Topologia ogólna — globalny audyt 10: rozdział 16, istnienie i porządek uzwarceń

**Data:** 2026-11-22.
**Źródło:** `chapters/pl/general_topology/16-funkcje-ciagle-i-uzwarcenia.tex`.
**Badany niezmieniony blob:** `1c2fcb925d62120feaea468400e48842a508a062`.
**Zakres:** samodzielna kontrola dowodów
funkcyjnej charakterystyki przestrzeni Tychonoffa,
istnienia uzwarceń Hausdorffa,
jednoznaczności oraz porządku
na klasach równoważności.

## Funkcyjna charakterystyka całkowitej regularności

W `thm:topog-uzwarcenia-funkcyjny-opis`
przestrzeń jawnie spełnia T1.
W kierunku całkowita regularność ⇒
własność oddzielania funkcjami
dla danego x∈U wykorzystano
domknięty F=X\U oraz ciągłą h
równą 0 na x i 1 na F.
Funkcja f=1-h ma zadane
wartości 1 i 0.
Dla różnych punktów x≠y
T1 zapewnia otwartość X\{y},
a więc oddzielanie punktów.

W kierunku własność funkcji ⇒
topologia początkowa,
dla każdego x∈U zbiór
f^{-1}((1/2,1]) jest otwarty
w topologii początkowej,
zawiera x i leży w U.
Zatem nie otrzymujemy
jedynie słabszej topologii.

W kierunku topologia początkowa ⇒
całkowita regularność,
jeśli x nie należy do
domkniętego F, wybieramy
podbazowe skończone przecięcie
W=∩_j f_j^{-1}(V_j)
z x∈W⊂X\F.
Dla każdego j istnieje
h_j:[0,1]→[0,1] równy 0
w f_j(x) i 1 na [0,1]\V_j.
Funkcja max_j h_j∘f_j
jest ciągła, równa 0
w x i 1 na całym
X\W, a zatem na F.
Przypadek F=∅
rozstrzygnięto funkcją stałą.
Wybór h_j wykorzystuje
całkowitą regularność
metrycznego odcinka, nie
nieudowodnione wcześniej
założenie o X.

## Istnienie uzwarcenia Hausdorffa

W `thm:topog-uzwarcenia-istnienie`
przestrzeń ma zwarte
uzwarcenie Hausdorffa wtedy
i tylko wtedy, gdy jest
Tychonoffa. Jeśli X
jest podprzestrzenią
zwartej Hausdorffa K,
dziedziczy T1 i całkowitą
regularność, co stanowi
konieczność.
W kierunku wystarczającym
istniejące zanurzenie
X w kostkę [0,1]^I
oraz domknięcie obrazu
daje kompakt Hausdorffa.
Zwartość wynika z Tychonoffa,
a gęstość obrazu w jego
domknięciu jest tautologiczna.
Żadna z implikacji nie wymaga
lokalnej zwartości X.

## Jednoznaczność oraz porządek uzwarceń

Odwzorowania K_1→K_2
zgodne z gęstym zanurzeniem
X są co najwyżej jedno:
zbiór zgodności dwóch map
jest przeciwobrazem
domkniętej przekątnej
w K_2×K_2, a zawiera
gęsty e_1(X).
Odwzorowanie zgodne
z zanurzeniami jest
automatycznie surjektywne:
jego zwarty obraz
jest domknięty w
Hausdorffowym K_2
i zawiera gęsty e_2(X).

Zwrotność i przechodniość
relacji porównywania
uzwarceń wynikają z
identyczności i składania
map. Jeśli ciągłe mapy
K_1→K_2 i K_2→K_1
istnieją w obu kierunkach
i są zgodne z zanurzeniami,
ich złożenia są identycznościami
na gęstych obrazach X.
Z jednoznaczności rozszerzenia
są identycznościami wszędzie;
mapy są więc wzajemnymi
homeomorfizmami.
Antysymetria dotyczy
**klas równoważności**,
a nie dosłownych par (K,e);
to rozróżnienie jest
jawnie obecne w źródle.

## Wynik

W sprawdzonych dowodach
nie znaleziono nowego
błędu matematycznego.
Stabilny rozdział 16
pozostawiono bez zmian.
Jest to kontrola wskazanych
wyników; pozostałe
przykłady i wszystkie
ilustracje pełnej książki
nie zostały objęte
globalną certyfikacją.
