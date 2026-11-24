# PDE-02 — trwałe kryteria regresyjne

Źródło: [rozdział 02](../../../../chapters/pl/partial_differential_equations/02-charakterystyki-i-pde-pierwszego-rzedu.tex).
Kryteria semantyczne nie są testami automatycznymi ani formalizacją Lean. Identyfikatory zgodne z [przeglądem przygotowawczym](../../../../audits/partial_differential_equations/chapter-02/preflight.md).

| ID | Etykieta | Kryterium | Metoda |
|---|---|---|---|
| PDE-02-001 | eq:pde2-constant-formula | Całka czasowa względem λ₁, lokalne ograniczenia pochodnych podcałkowych, reguła Leibniza, weryfikacja równania w całej przestrzeni i danych przy t=0. | semantyczna |
| PDE-02-002 | thm:pde2-linear | Gronwall dla 1+abs(X), ograniczenie trajektorii, granica i przedłużenie; istnienie przepływu wstecznego z polem -b(t-s,x) i tymi samymi ograniczeniami, obie tożsamości odwrotności. | semantyczna |
| PDE-02-003 | thm:pde2-linear | Wspólna regularność odwrotności względem (t,x) przez blokową macierz pochodnej i lokalne odwrotności; przedłużenie C¹ przez odbicie na obu końcach czasu. | semantyczna |
| PDE-02-004 | prop:pde2-liouville | Równanie wariacyjne z równania całkowego, ciągłość i lokalne ograniczenie pochodnej, I_d, jednostronne pochodne, rozwiązanie równania skalarnego czynnikiem całkującym i dodatniość J. | semantyczna |
| PDE-02-005 | thm:pde2-mass | Istnienie i jednoznaczność z twierdzenia liniowego, reguła iloczynu, wartość początkowa, obraz nośnika przez homeomorfizm, całkowalność także dla gęstości ze znakiem przed zmianą zmiennych. | semantyczna |
| PDE-02-006 | prop:pde-v31-transport-lp | Euklidesowa norma operatorowa, oszacowanie śladu w bazie ortonormalnej, obie nierówności L^p, skończoność normy, równość supremum z supremum istotnym dla funkcji ciągłej. | semantyczna |
| PDE-02-007 | thm:pde2-cauchy | Regularna lokalna funkcja definiująca hiperpowierzchnię, wspólny przedział przepływu, niezerowa pochodna wzdłuż charakterystyk, prostokątne otoczenie i dokładna równość przekroju początkowego; regularność całek, weryfikacja PDE, jednoznaczność na wybranym otoczeniu oraz zarodka. | semantyczna |
| PDE-02-008 | thm:pde2-quasilinear | Wspólny przedział istnienia dla danych z otoczenia, jawna blokowa macierz pochodnej o wyznaczniku 1 w chwili początkowej, dyfeomorfizm z iloczynu na otwarty zbiór Q, wspólny iloczyn dla charakterystyk innego rozwiązania, jednoznaczność na jego otwartym obrazie; terminologia odwzorowanie zamiast mapa. | semantyczna |
| PDE-02-009 | thm:pde2-breaking | Warunek 0≤t<T*, surjektywność z granic w nieskończoności, wspólna odwrotność C¹ wraz z t=0, weryfikacja równania i danych, wzór na gradient oraz dojście charakterystyki do punktu osobliwego. | semantyczna |
| PDE-02-010 | ex:pde2-rarefaction | Całkowanie na t≥ε, zerowe skoki, oszacowanie normy L¹ różnicy danych przez 2Mt(max(0,u_R)-min(0,u_L)), przejście do granicy w całce brzegowej i podwójnej. | semantyczna |
| PDE-02-011 | prop:pde2-rh | Rozróżnienie równania dystrybucyjnego we wnętrzu od zagadnienia z danymi początkowymi; normalne zewnętrzne (-s',1) i (s',-1) po normalizacji, element długości krzywej, jawne znaki wkładów i oba kierunki równoważności. | semantyczna |
| PDE-02-012 | eq:pde2-charpit-system | Wyprowadzenie układu z różniczkowania PDE, symetrii hesjanu, wyboru prędkości F_p i reguły łańcuchowej dla u oraz gradientu. | semantyczna |
| PDE-02-013 | lem:pde2-contact | Jawne dziedziny i regularność rodziny, uzasadnienie mieszanej pochodnej czasowo-parametrowej przez równanie całkowe, skrócenie składników z pochodną F_p, zachowanie F i równanie liniowe na odchylenie od warunku styczności. | semantyczna |
| PDE-02-014 | thm:pde2-charpit | Wspólny przedział istnienia ODE, iloczyn i lokalny dyfeomorfizm, jawna konstrukcja u oraz gradientu, regularność C², obydwa warunki początkowe; jednoznaczność zarodka przez porównanie pełnych układów ODE na wspólnym iloczynie. | semantyczna |
| PDE-02-015 | sec:pde2-charpit | W przykładzie eikonalnym ciągły wybór gałęzi na spójnym przedziale, bezpośrednie sprawdzenie równania i danych dla obu rozwiązań oraz poprzeczność obu wektorów F_p. | semantyczna |
| PDE-02-016 | prop:pde2-hamilton | Wspólny iloczyn istnienia rodziny ODE klasy C¹, blokowa macierz pochodnej i dyfeomorfizm Theta na Q; jawne dziedziny i dane. | semantyczna |
| PDE-02-017 | prop:pde2-hamilton | Uzasadnienie mieszanych pochodnych z równania wariacyjnego, zachowanie R_j=0, odwracalność D_xi X i wyznaczenie gradientu, bezpośrednia weryfikacja PDE i warunku początkowego; wszystkie pierwsze pochodne u są klasy C¹, stąd u jest klasy C². | semantyczna |
| PDE-02-018 | ex:pde2-hj-blowup | Jawne X,P,U, odwrócenie X_t i weryfikacja PDE; brak ciągłego przedłużenia także w (1,0), przez porównanie x=0 i x=sqrt(1-t); kaustyka jako wartość krytyczna rzutu ograniczonego do krzywej fazowej, nie samego rzutu z całej przestrzeni fazowej. | semantyczna |
| PDE-02-019 | sec:pde2-summary | Rozróżnić lokalne istnienie charakterystyk i warunek lokalnego dyfeomorfizmu, nie obiecywać kontynuacji lepkościowej przy dowolnych danych; terminologia odwzorowanie. | semantyczna |
| PDE-02-020 | chap:pde-characteristics | Jawna konwencja funkcji rzeczywistych, wymiarów i miar, regularność do brzegu czasu C¹ i C² także dla funkcji wektorowych. | semantyczna |
| PDE-02-021 | sec:pde2-basic | Przykład tłumienia zawiera dziedzinę, dane, równanie ODE wzdłuż charakterystyk i podstawienie odwrotności. | semantyczna |
| PDE-02-022 | thm:pde2-linear | Przedłużenia przez odbicie tylko w przedziałach, w których argument X należy do [0,T]; czynnik całkujący, różniczkowanie pod całką, weryfikacja PDE i danych. | semantyczna |
| PDE-02-023 | prop:pde-v31-transport-lp | Wskazać klasę rozwiązania i pełne dane początkowe w oszacowaniu norm. | semantyczna |
| PDE-02-024 | def:pde2-weak | Testy są ograniczeniami funkcji gładkich o zwartym nośniku na (-∞,T)×R, mogą być niezerowe przy t=0; całkowalność u i f(u) obejmuje przekrój początkowy. | semantyczna |

## Pierwszy właściwy przebieg — 2026-11-24

Poprawki źródła w commicie fc5a93a0c90004507219da4882c84b57adc1b309. Sprawdzono semantycznie trzy poprawione fragmenty, zachowano wszystkie 51 etykiet i 55 wystąpień odsyłaczy (w tym istniejący cel zewnętrzny chap:pde-code w rozdziale 33); środowiska poprawnie zagnieżdżone. Nie uruchomiono kompilacji, renderowania, testów wykonywalnych ani Lean dla rozdziału 02. Otwarte usterki PDE-02-004–010 oraz dalszy audyt rozdziału. Rozdział otwarty.

## Drugi właściwy przebieg — 2026-11-24
Poprawki 004–006 w commicie dfc0bce4f40e9f3123894b203820e60a62b255db. Sprawdzono semantycznie zmienione fragmenty i strukturę: wszystkie 51 etykiet zachowane, 56 wystąpień odsyłaczy (w tym znany zewnętrzny cel chap:pde-code), środowiska poprawnie zagnieżdżone. Nie wykonano kompilacji, renderowania ani Lean; testy automatyczne będą raportowane oddzielnie od kryteriów semantycznych. Otwarte 007–010 i dalsze sekcje rozdziału.

## Trzeci właściwy przebieg — 2026-11-24
Poprawki 007–008 w commicie f375d519a2cd8898e96023bf3fcdaa92bb303f72. Sprawdzono semantycznie zmienione fragmenty, zachowano 51 etykiet, 57 wystąpień odsyłaczy (w tym cel zewnętrzny chap:pde-code), poprawne zagnieżdżenie środowisk. Nie wykonano kompilacji, renderowania, testów wykonywalnych ani Lean. Otwarte 009–010 i dalszy audyt części o układzie Charpita oraz równaniu Hamiltona–Jacobiego. Rozdział otwarty.

## Czwarty właściwy przebieg — 2026-11-24
Poprawki 009–011 w commicie ee18666407b25cfad07023e382d4013e1cafe5fa. Przejrzano semantycznie zmienione dowody, zachowano 51 etykiet, sprawdzono 59 odsyłaczy (w tym cel zewnętrzny chap:pde-code) oraz zagnieżdżenie środowisk. Poprawiono dwa dalsze użycia słowa mapa w znaczeniu odwzorowania. Nie uruchomiono kompilacji, renderowania, testów wykonywalnych ani Lean. Wszystkie dziesięć usterek przeglądu przygotowawczego poprawiono w źródle; pozostają dalszy audyt, kontrole techniczne i niezależna stabilizacja. Rozdział otwarty.

## Piąty właściwy przebieg — 2026-11-24
Poprawki 012–015 w commicie 2c6ad0fe000e9c1c47e4a1dfc9eb637f95646fde. Przejrzano semantycznie zmienione dowody i przykład. Zachowano 51 etykiet, sprawdzono 60 odsyłaczy (w tym zewnętrzny cel chap:pde-code), poprawne zagnieżdżenie środowisk oraz ciągłość ID i istnienie etykiet dla wszystkich 15 kryteriów. Nie uruchomiono kompilacji, renderowania, testów wykonywalnych ani Lean. Pozostaje audyt równania Hamiltona–Jacobiego, kontrole techniczne i niezależna stabilizacja. Rozdział otwarty.

## Szósty właściwy przebieg — 2026-11-24
Poprawki 016–019 w commicie 79f47c64f338247502dbb15f8b761eb892292550. Sprawdzono semantycznie zmienione dowody, przykład i podsumowanie. Zachowano 51 etykiet, sprawdzono 61 odsyłaczy (w tym istniejący zewnętrzny cel chap:pde-code), poprawne zagnieżdżenie środowisk, ciągłość ID i istnienie etykiet wszystkich 19 kryteriów. Pierwszy przegląd wszystkich sekcji zakończony, rozdział nadal otwarty. Nie uruchomiono kompilacji, renderowania, testów wykonywalnych ani Lean. Następne: trwałe testy wykonywalne adekwatnych obliczeń, kompilacja, kontrola rysunków i niezależna stabilizacja.

## Pierwszy przebieg stabilizacyjny — 2026-11-24 (iteracja 20)
Poprawki 020–024: c87f9159554a77ca552052f2fe5f3547039c99f1. Ponowna kontrola początkowych sekcji, warunków brzegowych czasu i definicji rozwiązania słabego; zachowano 51 etykiet, 62 rozwiązywalne odsyłacze (w tym zewnętrzny cel chap:pde-code), poprawne zagnieżdżenie środowisk. Lokalnie ponownie uruchomiono sześć testów z pliku o Git blob SHA 805ac866415f304d7df385a0c0d4530db0a25c92: 6/6 OK. Przebieg CI 45424483056: testy i struktura success, kompilacja failure z powodu użycia polecenia newlabel po begin{document} w generowanym dokumencie, bez renderów. Poprawiono generator w commicie 8e4c40a885c751f553bf059cf1f35e619ad04f02, definiując etykietę w preambule przez @namedef. Lokalna minimalna próba pdflatex (dwa przebiegi) potwierdziła rozdział 2 i odsyłacz 33; hyperref sygnalizuje celowo pominięty link o pustym celu. To nie jest pełna kompilacja rozdziału. W tej iteracji nie wykonano pełnej kontroli wizualnej ani Lean. Przebieg nie jest czysty, ponieważ wykryto i poprawiono usterki; rozdział pozostaje otwarty.
