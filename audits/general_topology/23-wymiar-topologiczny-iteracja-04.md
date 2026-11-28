# Topologia ogólna — rozdział 23, audyt 04 (czysty 1/2)

**Data:** 2026-11-22.
**Źródło:** chapters/pl/general_topology/23-wymiar-topologiczny.tex.
**Niezmieniony blob:** `9dc1ed4784d929b405d00a3216865418f240a37c`.
**Wynik:** CZYSTY, pierwsza kontrola 1/2 na nowym blobie.
**CI:** [45051754287](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45051754287), completed/success.
**Artefakt:** general-topology-ch01-ch23, ID `14766071024`.

## Matematyka: kontrola hipotez i przypadków skrajnych

- Wymiar pokryciowy definiowany jest dla zwartych
  przestrzeni Hausdorffa, także przestrzeni pustej
  (wartość -1), i nie jest utożsamiany z wymiarem
  Hausdorffa. Rozdrobnienia są indeksowane;
  ta konwencja jest zachowana w dowodach.
- Homeomorfizm przenosi rozdrobnienia,
  zachowując rząd; podprzestrzeń domknięta F
  jest badana przez pokrycie X rozszerzone
  o X\F, bez założenia, że F jest otwarta.
- Charakterystyka dim=0 przez clopen otoczenia
  ma obie implikacje: z rozdrobnienia rzędu 1
  otrzymuje się clopen bazę, a z clopen bazy
  skończony rozłączny podział rozdrabniający
  dowolne skończone pokrycie. Dla ind i Ind
  granica \(\partial V=\varnothing\) jest warunkiem
  równoważnym byciu clopen, co uzasadnia zgodność
  trzech wymiarów przy wartości zero.
- Cantor: kodowanie przez \{0,1\}^N jest homeomorfizmem,
  a baza cylindrów jest clopen; iloczyny przestrzeni
  zwartych wymiaru 0 mają clopen bazę bez
  założenia przeliczalności rodziny.
- Liczba Lebesgue'a dodatnia dzięki zwartemu
  podpokryciu kul o podwójnym promieniu.
  Rozdrobnienie przedziałami siatki hZ ma
  rząd co najwyżej dwa i rozdrabnia
  przy 2h<delta; stąd dim K<=1 dla
  zwartych podzbiorów R i dim[a,b]=1
  dla nieosobliwych odcinków.

## Matematyka: wyższe wymiary

- Nerw ma wierzchołki tylko dla niepustych
  elementów pokrycia; mapa barycentryczna
  używa funkcji odległości od dopełnień
  i osobnego przypadku U_i=X.
- Triangulacja siatki R^n przez porządek
  współrzędnych pokrywa każdy sześcian;
  otwarte gwiazdy wierzchołków mają
  rząd co najwyżej n+1 i średnicę
  co najwyżej 2h sqrt(n).
  Na zwartym K jedynie skończenie wiele
  gwiazd jest aktywnych.
- Przed wykorzystaniem twierdzenia Brouwera
  sześcian identyfikuje się z kulą
  domkniętą przez jawny homeomorfizm radialny.
  Własność Poincarégo–Mirandy wynika
  z równości punktu stałego projekcji
  \(P(x-f(x))=x\) i ścisłych znaków na ścianach.
- Dla hipotetycznej dim Q<=n-1
  dobieramy wektory w otwartych ortantach
  w położeniu liniowo ogólnym.
  Przy co najwyżej n aktywnych współczynnikach
  niezerowa kombinacja tych wektorów
  nie może dać zera. Przeciwne znaki
  składowych na ścianach przeczą
  Poincarému–Mirandzie; stąd dim Q=n.
- Ciągły obraz zbioru Cantora w [0,1]
  skonstruowano z sumy rozwinięcia dwójkowego,
  co poprawnie pokazuje wzrost wymiaru
  pod ciągłą surjekcją.

## LaTeX, integracja i wizualizacja

Zebrano 40 różnych etykiet i 23 odsyłacze;
dwa odsyłacze są z rozdziału 07 (zwartość).
Środowiska twierdzeń, definicji,
dowodów, wyliczeń i rysunku mają
zgodną liczbę początków i końców.
Nie wykryto niedozwolonej terminologii.

CI 45051754287 zbudowało wszystkie
samodzielne rozdziały oraz całą książkę
i przeszło wszystkie testy matematycznych
modeli skończonych, w tym radialnego homeomorfizmu.
Po pobraniu rzeczywistego artefaktu
wyrenderowano wszystkie 9 stron PDF rozdziału 23,
obejrzano je w zestawieniu oraz osobno stronę 9.
Podsumowanie znajduje się na końcu strony 9
i nie tworzy osieroconej strony.
W logach samodzielnego rozdziału
i pełnej książki nie ma ostrzeżeń
Overfull, Underfull, Missing character ani LaTeX Warning.
Cała książka na tym etapie ma 165 stron PDF.

**Wynik: czysty 1/2 na blobie 9dc1ed... .
Źródła rozdziału nie zmieniono podczas audytu.**
