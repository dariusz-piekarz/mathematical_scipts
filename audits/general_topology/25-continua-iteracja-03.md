# Topologia ogólna — rozdział 25, audyt 03 (drugi czysty)

**Data:** 2026-11-22.
**Źródło i blob:** `chapters/pl/general_topology/25-continua-i-ich-struktura.tex`,
`7b772123870296af95d3ce951ccddb65685af7aa`.
**Wynik:** CZYSTY 2/2; bez zmian źródła od audytu 02.

## Druga kontrola: przypadki puste, degenerate i odwrotne

1. Continuum jest **niepuste**, więc rodzina
   podcontinuów nie zawiera ∅. Zbiory
   zwartych i spójnych podprzestrzeni
   są domknięte w Hausdorffowym X;
   wykorzystanie normalności jest poprawne.
2. Jednopunktowe continuum jest dopuszczalne:
   jest nierozkładalne w zadanej definicji,
   ale nie jest nietrywialne.
   Przykład Knastera jest nietrywialny,
   ponieważ surjektywny obraz jego
   zerowego rzutowania to cały [0,1].
3. Przecięcie zstępującego ciągu
   K_n ma własność skończonych przecięć
   także wtedy, gdy wszystkie K_n
   są równe; spójność przecięcia
   udowodniono niezależnie od tej niepustości.
4. Łańcuch podcontinuów w lemacie
   nie musi być przeliczalny.
   Nie przechodzi się do bezpodstawnie
   wybranego ciągu współkońcowego;
   zamiast tego wykorzystano
   skończone podpokrycie zwartego X.
5. Jeśli a=b, lemat Zorna nadal działa:
   singleton {a} jest najmniejszym
   podcontinuum zawierającym oba punkty.
   Gdy a≠b, minimalne podcontinuum
   jest nietrywialne.
6. "Nierozkładalne" nie znaczy
   "nieprzywiedlne między wybranymi punktami":
   odcinek jest nieredukowalny
   między końcami, ale jest rozkładalny
   jako suma dwóch mniejszych odcinków.
7. Konstrukcja granicy odwrotnej
   wymaga surjektywności każdej mapy
   wiążącej. Bez tego nie deklarujemy
   surjektywności rzutowań ani
   utrzymania spójności w podanej postaci.
   Potrzebny wybór kolejnych
   przeciwobrazów został odnotowany.
8. Przy sprawdzaniu spójności
   granicy odwrotnej nie wywnioskowano
   znikąd, że dwa rozłączne zbiory
   mają różne projekcje na każdym
   poziomie: wykazano istnienie
   *jednego* poziomu rozróżniającego,
   stosując zwartość A×B i zstępujące
   zbiory F_n.
9. W mapie namiotowej,
   nawet jeśli U⊂[0,1] zawiera tylko
   punkt graniczny 0 lub 1
   z otwartości względnej,
   jego przeciwobraz spotyka
   każdą pełną gałąź T^r:
   każde ograniczenie jest bijekcją
   na cały przedział.
   W szczególności pierwsza
   i ostatnia gałąź są wystarczające
   do otrzymania środka przedziału
   w p_m(C).
10. W nierozkładalności Knastera
    dla dowolnego ustalonego j
    dobiera się m większe
    jednocześnie od j+1 i k+1;
    nie używa się jednego
    nieistniejącego "nieskończonego" poziomu.
    Dla j<k surjektywność
    T^{k-j} na [0,1] daje
    pozostałe pełne rzuty.
11. W solenoidzie ciągi współrzędnych
    są pierwiastkami kwadratowymi
    w S1; każdy punkt z0 ma
    dwa różne pierwiastki,
    więc dwie wartości epsilon
    naprawdę odróżniają gałęzie.
    Łuk U ma długość parametrów
    <1; to warunek gwarantujący
    jednoznaczny kąt t0∈J.
12. Lokalna spójność nie jest
    mylona ze spójnością całej
    przestrzeni: solenoid jest
    spójny na mocy twierdzenia
    o granicy odwrotnej,
    ale nie ma spójnych otwartych
    otoczeń wewnątrz
    p0^-1(U)≅J×Cantor.
13. Graf bez krawędzi i z
    jednym wierzchołkiem jest
    osobno uwzględniony.
    Dla niepustego zbioru krawędzi
    wybór wspólnego wierzchołka
    i skończenie wielu powracających
    spacerów daje ciągłą surjekcję;
    nie trzeba założyć istnienia
    cyklu Eulera.
14. Kodowanie Peana dla n=1
    redukuje się do klasycznej
    surjekcji Cantora na przedział,
    a dla n=2 daje rzeczywistą
    krzywą wypełniającą kwadrat.
    Brak jednoznaczności rozwinięć
    dwójkowych nie przeszkadza:
    potrzebujemy tylko
    istnienia *jednego* rozwinięcia
    dla każdej współrzędnej.
    Własność przedłużania zachowującego
    [0,1] jest jawnie częścią
    wcześniej udowodnionego Tietzego.
15. Twierdzenie Hahna–Mazurkiewicza
    jest podane wyłącznie jako
    klasyczny wynik do dalszego
    pełnego opracowania.
    Nie oznaczono go jako twierdzenie
    z udawanym dowodem.
    Ukończone dowody grafów
    i surjekcji na kostki są
    odrębnymi wynikami.

## Integracja i rzeczywisty PDF

- Ponownie pobrano aktualny blob
  i potwierdzono identyczność
  z audytem 02.
- 35 etykiet i 15 odsyłaczy
  mają poprawny układ,
  a 14 dowodów ma
  otwarte i zamknięte środowiska.
- Samodzielny punkt wejścia
  importuje etykiety wcześniejszych
  rozdziałów 05, 08 i 23,
  bez kopiowania dowodów.
- Artefakt CI 45056802863
  obejmuje 8 stron rozdziału
  i 183 strony całej książki.
  Stronę z rysunkiem namiotu
  i stronę z wynikiem Peana
  obejrzano w większej skali;
  brak nakładania się tekstów,
  ucięć i osieroconego podsumowania.
- Logi pełnej książki i rozdziału
  nie zawierają ostrzeżeń
  Overfull, Underfull ani
  LaTeX Warning.

**Stan: CZYSTY 2/2.**
Wymagany jeszcze audyt dodatkowy
na tym samym blobie i
potwierdzenie końcowych testów
regresyjnych, po czym można
oznaczyć rozdział 25 jako stabilny.
