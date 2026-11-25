# PDE — rozdział 10 — trwałe kryteria regresyjne

Pierwsza lektura, iteracja 148. Kryteria semantyczne nie są wykonanymi testami automatycznymi ani formalizacją Lean.

| ID | Etykieta | Kryterium | Metoda |
| --- | --- | --- | --- |
| PDE-10-001 | chap:pde-embeddings | Zakres d,p, niepusty zbiór otwarty, funkcje rzeczywiste, rozróżnienie zanurzeń ciągłych i zwartych; norma euklidesowa gradientu a norma składowych z rozdziału 09, również p=infty. | semantyczna |
| PDE-10-002 | lem:pde10-LW | Nieujemne mierzalne funkcje, przypadki całek zerowych i nieskończonych, konwencja iloczynu przez granicę obcięć. | semantyczna |
| PDE-10-003 | lem:pde10-LW | Baza d=2 przez Tonellego; pierwszy Hölder dla d-1 czynników, niezależność G_j od x_j. | semantyczna |
| PDE-10-004 | lem:pde10-LW | Drugi Hölder z wykładnikami d-1 i (d-1)/(d-2), hipoteza indukcyjna, Fubini i poprawne potęgi. | semantyczna |
| PDE-10-005 | lem:pde10-LW | Jawne obcięcia min(F_j,n) na [-n,n]^(d-1), zbieżność monotoniczna także przy całkach 0 i nieskończonych. | semantyczna |
| PDE-10-006 | thm:pde10-Sob1 | Całkowanie od minus nieskończoności dzięki zwartemu nośnikowi, iloczyn d oszacowań, Loomis–Whitney i Tonelli. | semantyczna |
| PDE-10-007 | thm:pde10-Sob1 | Potęga (d-1)/d, średnie geometryczna i arytmetyczna, jawna stała 1/sqrt(d) dla gradientu euklidesowego. | semantyczna |
| PDE-10-008 | thm:pde10-Sobp | Dla 1<p<d gamma>1, abs(t)^gamma klasy C¹ także w zerze, zwarty nośnik v, zastosowanie twierdzenia dla p=1. | semantyczna |
| PDE-10-009 | thm:pde10-Sobp | Hölder z p,p', rachunek gamma*d/(d-1)=p*, (gamma-1)*p'=p*, dzielenie wyłącznie przy u niezerowym. | semantyczna |
| PDE-10-010 | thm:pde10-Sobp | Gęstość z rozdziału 09, Cauchy w L^{p*}, identyfikacja granic przez Czebyszewa także przy nieskończonej mierze; zachowanie stałej. | semantyczna |
| PDE-10-011 | rem:pde10-critical | Zakres 1<=p<d, 1<=q<=infty, skalowanie norm również dla q=infty, ograniczenie W^{1,p}, rozbieżność dla q>p*. | semantyczna |

| PDE-10-012 | def:pde10-Lipschitz | Lokalny opis grafu, strona wnętrza i mniejsze otoczenia; w dowodzie jawne U,Q,Q_+, także d=1. | semantyczna |
| PDE-10-013 | lem:pde10-extension | Phi i Psi wzajemnie odwrotne dwulipschitzowskie, dokładne zachowanie miary z Tonellego i pionowego podstawienia, zbiory zerowe, normy L^p. | semantyczna |
| PDE-10-014 | lem:pde10-extension | Pochodne cząstkowe phi przez AC na odcinkach, mierzalność, ograniczenie L, klasyczna reguła łańcuchowa i testowa identyfikacja słabych pochodnych złożeń. | semantyczna |
| PDE-10-015 | lem:pde10-extension | Oszacowania pochodnych złożenia, przybliżenie Meyersa–Serrina dla p skończonego, Cauchy i granice L^p, odwrotność oraz pełne otoczenie. | semantyczna |
| PDE-10-016 | lem:pde10-extension | p=infty przez p=1 na ograniczonych otoczeniach, wzory słabych pochodnych w L^infty; bez Morreya i bez aproksymacji w normie W^{1,infty}. | semantyczna |
| PDE-10-017 | lem:pde10-extension | Lokalny iloczyn chi u, A zwarte w Q, lokalność pochodnych, odcięcie zeta i tożsamość testowa przedłużenia przez zero na P bez założenia zerowego śladu na t=0. | semantyczna |
| PDE-10-018 | lem:pde10-extension | Odbicie dla p skończonego z rozdziału 09; dla p=infty zwarty nośnik pozwala użyć p=1 i wzorów pochodnych; zachowanie normy maksimum. | semantyczna |
| PDE-10-019 | lem:pde10-extension | A wraz z odbiciem zwarte w Q; powrót przez Psi, przedłużenie zwartego iloczynu, restrykcja E_chi równa chi u, liniowość i ograniczoność. | semantyczna |
| PDE-10-020 | lem:pde10-extension | Skończone pokrycie brzegu, zwarta reszta wewnętrzna, odcięcia, normalizacja rozkładu jedynki, suma przedłużeń i jeden ustalony nośnik. | semantyczna |
| PDE-10-021 | cor:pde10-density-boundary | Gęstość przez przedłużenie, odcięcie, zbieżność ogonów oraz splot dla p skończonego; restrykcja nie zwiększa normy; brak wymogu zerowego śladu. | semantyczna |
| PDE-10-022 | thm:pde10-domain-embed | p<d: nierówność Sobolewa dla Eu i Hölder na Omega, zakres q<=p*. | semantyczna |
| PDE-10-023 | thm:pde10-domain-embed | p=d: wybór 1<p_0<d, ustalony nośnik Eu oraz Hölder, twierdzenie Sobolewa na R^d (nie twierdzenie dla ograniczonego obszaru na R^d), restrykcja i Hölder dla q<=p_0^*. | semantyczna |
| PDE-10-024 | thm:pde10-domain-embed | p>d i p=infty: odłożone do dowodu Morreya, sprawdzić pełną normę i reprezentanta na domknięciu; nie stosować tego wyniku w dowodzie przedłużania. | semantyczna |

| PDE-10-025 | lem:pde10-point-average | Wypukłość kuli, reguła łańcuchowa po odcinku, uśrednienie i Tonelli. | semantyczna |
| PDE-10-026 | lem:pde10-point-average | Dla t>0 podstawienie z=x+t(y-x), jakobian t^(-d), obraz kuli, ograniczenie od dołu t przez odległość/(2R). | semantyczna |
| PDE-10-027 | lem:pde10-point-average | Jawne obliczenie całki t^(-d-1), stała 2^d/(d*omega_d), omega_d objętością kuli, całkowalność jądra i pominięcie singletonu. | semantyczna |
| PDE-10-028 | thm:pde10-Morrey | Kula wspólna dla x,y; Hölder, całka biegunowa, d-(d-1)p'>0 równoważne p>d, wykładnik 1-d/p. | semantyczna |
| PDE-10-029 | thm:pde10-Morrey | Oszacowanie supremum bezpośrednio na kuli jednostkowej przez lemat i średnią; równoważność norm gradientu. | semantyczna |
| PDE-10-030 | thm:pde10-Morrey | Gęstość z rozdziału 09, Cauchy w supremum, granica jednostajna, identyfikacja przez podciąg o sumowalnych błędach, Tonelli; jednoznaczność i liniowość. | semantyczna |
| PDE-10-031 | thm:pde10-Morrey | p=infty: lokalny splot, nieujemne znormalizowane jądro, ograniczenie modułu i euklidesowego gradientu, globalna stała Lipschitza. | semantyczna |
| PDE-10-032 | thm:pde10-Morrey | p=infty: diagonalny wybór sumowalnych błędów L^1 na kulach, zbiór pełnej miary gęsty, przedłużenie przez granice, niezależność ciągu, równość supremum i istotnego supremum. | semantyczna |
| PDE-10-033 | cor:pde10-Morrey-domain | Przedłużenie pierwszego rzędu i Morrey, pełna norma na domknięciu, jednoznaczność przez gęstość obszaru, liniowość; d=1 przez twierdzenia z rozdziału 09. | semantyczna |
| PDE-10-034 | cor:pde10-Morrey-domain | Dla k>=2 każda pochodna do rzędu k-1 należy do W^{1,p}, ograniczenie jej normy i reprezentant Höldera na domknięciu. | semantyczna |
| PDE-10-035 | cor:pde10-Morrey-domain | Lokalne wygładzanie ciągłych reprezentantów, jednostajna zbieżność na mniejszej kuli, całkowanie wzdłuż osi i przejście do granicy, identyfikacja klasycznych pochodnych przez ilorazy różnicowe. | semantyczna |
| PDE-10-036 | cor:pde10-Morrey-domain | Interpretacja C^{k-1,alpha} na domknięciu bez założenia klasycznego przedłużenia wyższych rzędów, d=1, p=1 bez wspólnego dodatniego wykładnika, p=infty Lipschitz. | semantyczna |

| PDE-10-037 | lem:pde10-cube-approx | Kostka otwarta o osiowych krawędziach, N>=1, rozłączne podkostki pokrywają poza zbiorem miary zero; średnie i liniowość dobrze określone. | semantyczna |
| PDE-10-038 | lem:pde10-cube-approx | Kontrakcyjność P_N przez Jensena, zsumowanie po kostkach i p-ty pierwiastek. | semantyczna |
| PDE-10-039 | lem:pde10-cube-approx | Poincaré–Wirtinger na podkostkach, Jensen dla sumy d składników, sumowanie norm, jawne rozróżnienie normy składowych i euklidesowej, stała dh. | semantyczna |
| PDE-10-040 | thm:pde10-Rellich-p | Przedłużenia o wspólnym ograniczonym nośniku, kostka zawiera domknięcie Omega, ograniczenie gradientów, wybór N wspólny dla ciągu. | semantyczna |
| PDE-10-041 | thm:pde10-Rellich-p | Wymiar V_N=N^d, niezależność funkcji charakterystycznych, jawna norma współczynników, kontrakcyjność i skończona sieć z argumentu skończenie wymiarowego. | semantyczna |
| PDE-10-042 | thm:pde10-Rellich-p | Przeniesienie sieci przez oszacowanie błędu, zagnieżdżone nieskończone zbiory indeksów, rosnąca przekątna i odległość <2^(1-m), zupełność i restrykcja; również p=1. | semantyczna |
| PDE-10-043 | lem:pde10-interpolation | Sprzężone wykładniki Höldera, skończoność J_q, q-ty pierwiastek i przypadki zerowych norm. | semantyczna |
| PDE-10-044 | thm:pde10-Rellich-q | p<d: podciąg Cauchy w L^p, jednostajna granica norm L^{p*}, interpolacja różnic z theta, q<=p przez skończoną miarę, zupełność i ciągłość. | semantyczna |
| PDE-10-045 | thm:pde10-Rellich-q | p=d: wybrać podciąg w L^d, skończone r>q, interpolacja różnic, q<=d jak wcześniej. | semantyczna |
| PDE-10-046 | thm:pde10-Rellich-q | p>d także p=infty: ciągłe reprezentanty, jednostajna ograniczoność i jednakowa ciągłość na zwartym domknięciu, Arzelà–Ascoli, granica zachowuje półnormę alpha. | semantyczna |
| PDE-10-047 | thm:pde10-Rellich-q | Dla beta<alpha rozdzielenie par punktów według delta, kontrola obu wyrazów w prawidłowej kolejności granic, beta=0 jako C, ciągłość zanurzenia z diametrem. | semantyczna |
| PDE-10-048 | ex:pde10-noncompact-critical | Dowolny niepusty otwarty zbiór, kula wewnętrzna, konkretny ciąg promieni, jednostajna norma Sobolewa i stała dodatnia norma krytyczna; granica a.e., sprzeczność przez podciąg z sumowalnymi błędami. | semantyczna |
| PDE-10-049 | ex:pde10-translation | Przesunięcia zachowują normy i pochodne, rozłączne nośniki, dodatnia stała odległość w L^p i brak podciągu Cauchy. | semantyczna |

| PDE-10-050 | ex:pde10-Moser | Ciągłość na sferach epsilon i 1, klasyczny gradient na pierścieniu, całkowanie przez części ze znoszeniem wyrazów brzegowych i identyfikacja słabego gradientu. | semantyczna |
| PDE-10-051 | ex:pde10-Moser | Biegunowe całki norm, d*omega_d, podstawienie t=log(1/r), ograniczenie obu składników normy L^d, rozbieżność istotnego supremum dla d>=2. | semantyczna |
| PDE-10-052 | ex:pde10-Moser | Funkcja log log(e/r), dokładna całka gradientu d*omega_d/(d-1), skończona norma funkcji, wyraz brzegowy na sferze eta zanika, brak przynależności do L^infty. | semantyczna |
| PDE-10-053 | sec:pde10-Moser | Skalowanie rodziny dla p>d i dwóch punktów o różnych wartościach funkcji, beta>alpha do 1: brak ciągłości; beta=alpha: brak zwartości mimo jednostajnej zbieżności do zera, także p=infty. | semantyczna |
| PDE-10-054 | sec:pde10-traces | Znormalizowana miara Hausdorffa, porównanie miary wykresu i podstawy przez oszacowania średnic pokryć dla G i rzutu, skończona miara brzegu, d=1 miara licząca. | semantyczna |
| PDE-10-055 | sec:pde10-traces | Porównanie całek nieujemnych przez funkcje proste i zbieżność monotoniczną, odpowiadanie zbiorów zerowych, bez korzystania z nieudowodnionego dokładnego wzoru powierzchniowego. | semantyczna |
| PDE-10-056 | thm:pde10-trace | Płaska warstwa: wystarcza C¹ w pionowych przekrojach, jawne potęgi a, p=1, wypukłość i Tonelli; wymiar 1 przez ślady końcowe rozdziału 09. | semantyczna |
| PDE-10-057 | thm:pde10-trace | Odcięcia w otoczeniach wykresowych z dowodu przedłużania, pionowa pochodna złożenia, zachowanie miary, porównanie miar na brzegu; brak założenia gładkości wykresu. | semantyczna |
| PDE-10-058 | thm:pde10-trace | Skończony rozkład jedynki na brzegu, zerowanie części wewnętrznej, oszacowanie globalne przez sumę lokalnych stałych. | semantyczna |
| PDE-10-059 | thm:pde10-trace | Konstrukcja przez gęstość, Cauchy w L^p brzegu, niezależność aproksymacji, liniowość, ograniczoność, zgodność ze wszystkimi gładkimi restrykcjami i jednoznaczność. | semantyczna |

## Iteracja 148
Źródło przed 22b013b3e972ece5feaa83488df6fdc89a1f3bfe; po 7678d73026ba49e7060cda158e4286c2e559f165, commit e504d11f70adbc028f346cab57807d5ed40c22b8. Przejrzano wstęp, Loomisa–Whitneya, Sobolewa dla p=1 i 1<p<d, skalowanie. Jedenaście zmian źródłowych: hipotezy i norma, przypadki całek 0 i nieskończonych, baza indukcji, obcięcia, całkowanie po prostej, stała gradientowa, regularność potęgi w zerze, wykładniki, identyfikacja granic, hipotezy i ograniczenie norm w skalowaniu. Zachowano kolejność 32 etykiet; stos środowisk poprawny; materiał od definicji obszaru Lipschitzowskiego bez zmian. Dodano trzy odsyłacze do rozdziału 09. Nie uruchamiano testów Python, CI, kompilacji ani Lean w tej iteracji. Pierwsza próba zapisu raportu: konflikt współbieżnej aktualizacji gałęzi, ponowiono zapis. Następny etap: obszary Lipschitzowskie, przedłużanie, gęstość i zanurzenia. Pierwsza lektura otwarta.

## Iteracja 149
Źródło przed 7678d73026ba49e7060cda158e4286c2e559f165, po b3e4b53d5f24ad3b09b95370064a4a386c0424a4, commit c4ccebae29c837bf32df7e08c5ea89b80cc8730e. Dwie wcześniejsze próby zapisu odrzucone przez konflikt współbieżnych zmian gałęzi; po odczytaniu tego samego bloba zapis zakończył się sukcesem. Przebudowano dowód przedłużania (trzy kroki) i skorygowano odwołanie przy p=d. Przejrzano również definicję, gęstość i zanurzenia dla p<=d. Zachowano 32 etykiety w tej samej kolejności, 33 wystąpienia odsyłaczy, stos środowisk poprawny. Nie wykonywano testów Python, kompilacji ani Lean. Kryteria 012–023 poddane pierwszej lekturze; 024 pozostaje otwarte do audytu Morreya. Potrzebna druga lektura szczegółów nowego dowodu, kontrola odsyłaczy i walidacja techniczna. Następny etap: nierówność Morreya i wniosek na obszarze, w tym końcowy przypadek p=infty.

## Iteracja 150
Źródło przed b3e4b53d5f24ad3b09b95370064a4a386c0424a4, po 594d5789127fcea5ba8dd70b1634c645ef864f8a, commit 7cca1b887d44b4972e73981321458e26b67c595d. Dwanaście zmian w sekcji Morreya: szczegółowe uśrednienie, podstawienie i całka jądra, rachunek wykładników, oszacowanie supremum, identyfikacja granicy, przypadek p=infty przez gęsty zbiór pełnej miary, pełna norma Höldera na obszarze, pochodne wyższych rzędów przez lokalny splot, przypadek d=1. Kryterium 024 i nowe 025–036 po pierwszej lekturze. Kontrola odczytanych plików 09 i 10: 32 unikatowe etykiety rozdziału 10, 41 wystąpień odsyłaczy, wszystkie cele istnieją (13 różnych celów z rozdziału 09); stos środowisk poprawny. Następna sekcja bez zmian. Nie uruchamiano testów Python, kompilacji, CI ani Lean. Pierwsza lektura otwarta: następny etap aproksymacja kostkami, Rellich–Kondrachov i interpolacja.

## Iteracja 151
Źródło przed 594d5789127fcea5ba8dd70b1634c645ef864f8a, po a647b682a0e9bb2b983d8d014e03ccd99576c007, commit 735bff6c9320a33cb5198e088ca6ead8c5e453a4. Czternaście zmian źródłowych; korekta pomieszania norm gradientu, jawna konstrukcja sieci i przekątnej, interpolacja, granica Höldera, dwa kontrprzykłady. Kryteria 037–049 pierwsza lektura. Odczyt źródeł 09 i 10 potwierdza 32/32 unikatowe etykiety i 46/46 rozwiązanych wystąpień odsyłaczy; stos środowisk poprawny, dalsza część od przypadku granicznego bez zmian. Testów wykonywalnych, kompilacji, CI i Lean nie uruchamiano. Pierwsza lektura otwarta: następny etap przypadek graniczny p=d (ciąg Mosera) oraz teoria śladów.

## Iteracja 152
Źródło przed a647b682a0e9bb2b983d8d014e03ccd99576c007, po 920f2f484ed6beb87cb307fa7b27d4853baa3854, commit bd507b7e9ff16a259f6a9d6ab1e7d09597b8a31c. Dziewięć zmian źródłowych: ciąg Mosera, dokładne normy, nowa funkcja nieograniczona log log(e/r), ostrość i brak zwartości Morreya, oszacowanie miary wykresu przez definicję Hausdorffa (zamiast przyjmowania dokładnego wzoru powierzchniowego), lokalne oszacowanie śladu, pokrycie i konstrukcja operatora przez gęstość. Kryteria 050–059 po pierwszej lekturze. Zachowano 32 etykiety, stos środowisk poprawny, 52/52 wystąpienia odsyłaczy rozwiązane w 09 i 10. Dalsza część od definicji H^{1/2} bez zmian. Nie uruchamiano testów wykonywalnych, kompilacji, CI ani Lean. Następna iteracja: przestrzeń śladów i podnoszenie, szczególnie dowód jądra śladu bez błędnego koła (przedłużenie przez zero i aproksymacja w oryginalnych współrzędnych), Poincare oraz podsumowanie.
