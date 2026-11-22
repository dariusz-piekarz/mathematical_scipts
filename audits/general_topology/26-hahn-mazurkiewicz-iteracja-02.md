# Topologia ogólna — rozdział 26, audyt 02 (pierwszy czysty)

**Data:** 2026-11-22.
**Sprawdzany blob:** `c380ca632a43c00f892457583381112d14eeb9c2`.
**Wynik:** CZYSTY 1/2, bez modyfikowania źródła w tej iteracji.
**Zakres:** szczegółowy audyt konstrukcji matematycznej,
hipotez i odsyłaczy; osobne ukończenie CI/PDF jest wymagane.

## Lemat o jednostajnej lokalnej spójności

Dla każdego ε>0 zbiór V_x wybierany
jest jako spójne otwarte otoczenie x
wewnątrz B(x,ε/3). Zatem jego średnica
jest <2ε/3<ε. Dobór 2r_x z kulą
B(x,2r_x)⊂V_x jest możliwy dzięki
otwartości. Po zwartym podpokryciu
kul B(x_i,r_i), dodatnia liczba
δ=min_i r_i zapewnia wspólne V_i
dla wszystkich par o odległości <δ.
Nie zakłada się tu spójności drogowej.

## Lemat o δ-łańcuchach

Klasa wszystkich punktów osiągalnych
skończonymi łańcuchami o odległościach
kolejnych punktów <δ jest niepusta
i otwarta. Jej dopełnienie jest otwarte,
bo punkt odległy o <δ od tej klasy
sam już do klasy należy.
Spójność wymusza pełną osiągalność.
Dowód działa także dla a=b.

## Kluczowa konstrukcja małych dróg

- Poziom n ma skończony podział i
  wszystkie sąsiednie wartości są
  δ_n-bliskie; dla każdego odcinka
  wybiera się spójny zbiór średnicy <ε_n.
- Podział jest rzeczywiście drobniejszy:
  w przypadku jednoodcinkowego łańcucha
  dopisuje się pierwszy punkt drugi raz.
  Rozmiary odcinków czasu maleją co
  najmniej dwukrotnie; wierzchołki
  tworzą zbiór gęsty w [0,1].
- Wartości dodawane w kolejnym
  kroku pozostają w odległości <ε_n
  od starego końca odcinka.
  Indukcja daje kontrolę
  przez ogon S_n=Σ_{k≥n}ε_k.
- Dwa parametry leżące w jednym
  lub dwóch sąsiednich odcinkach
  podziału poziomu n mają obrazy
  w odległości co najwyżej 4S_n.
  Dla skończonego podziału
  istnieje dodatnia najmniejsza
  długość odcinka czasu h_n,
  więc d_t(u,v)<h_n zapewnia
  wymagany przypadek.
- Jednostajna ciągłość na
  gęstym zbiorze i zupełność
  X (wynikająca ze zwartości
  metrycznej) dają jednoznaczne
  ciągłe przedłużenie.
  Obraz ma średnicę ≤2S_0<η.
- Otwartość składowych drogowych
  dowolnego zbioru otwartego
  wynika z lokalnej konstrukcji
  małych dróg. Wówczas
  udowodniony wcześniej wynik
  rozdziału 08 daje lokalną
  spójność drogową, zaś
  spójność X daje spójność drogową.

## Dołączanie pętli i surjekcja

Dla skończenie wielu celów y_i
istnieje skończenie wiele czasów
t_i (z powtórzeniami).
Zgrupowanie równych czasów
i wybranie rozłącznych
krótkich przedziałów czasu
zapewnia zgodność końców
nowej i starej drogi.
Droga z y_i wraca do h(t_i),
więc dodanie pętli nie
zmienia końców całej trajektorii.
Oszacowanie błędu jest
<2ε_n (jedna ε_n z pętli
i druga z oscylacji h).
Każda iteracja wstawia
punkty skończonej
δ_{n+1}/2-sieci;
następna droga ma obraz
δ_{n+1}/2-gęsty.
Suma odległości kolejnych
dróg jest ograniczona
przez zbieżny szereg,
co daje ciągłą granicę
jednostajną. Ponieważ
δ_n→0 i X jest Hausdorffa,
zwarty obraz granicznej
drogi jest domknięty,
a jednocześnie gęsty,
więc równy X.

## Kierunek konieczny

Włókno f^{-1}({x}) jest zwarte,
gdyż X jest Hausdorffa.
Dla drugiego aksjomatu
przeliczalności przechodzi się
od skończonych sum elementów
przeliczalnej bazy odcinka
do W_V=X\f([0,1]\V).
Są one otwarte przez
domkniętość zwartego obrazu
w Hausdorffowym X.
Dla każdego otwartego O
wokół x, pokrycie włókna
przez skończenie wiele bazowych
podzbiorów f^{-1}(O)
daje W_V z x∈W_V⊂O.
Zwartość i Hausdorffowość
implikują normalność,
a twierdzenie Urysohna
metryzowalność.

Do lokalnej spójności
dobiera się skończenie
wiele zamkniętych przedziałów
wewnątrz f^{-1}(O),
każdy spotykający włókno x.
Ich obrazy są spójne
i mają wspólny punkt x,
a ich suma jest spójna.
Otwarty W_V zawarty w tej
sumie daje otwarte otoczenie
w składowej spójnej O.
Powtórzenie dla każdego
punktu składowej oznacza,
że składowa jest otwarta,
a więc X jest lokalnie spójna.

## Kontrprzykłady i terminologia

Dyskretne D={0,1} jest
lokalnie spójne, lecz niespójne.
Zbiór Cantora nie jest
lokalnie spójny, a jego
każdy **niepusty** spójny
podzbiór jest singletonem,
który nie jest otwarty.
Sierpiński dwupunktowy
nie jest Hausdorffa,
lecz stanowi ciągły
surjektywny obraz [0,1].
Nie usunięto żadnej
koniecznej hipotezy.

23 unikatowe etykiety,
24 odsyłacze, 9 dowodów,
rysunek schematyczny i
zrównoważone środowiska.
Nie zmieniono źródła.
**Status: czysty 1/2.**
