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

| PDE-10-060 | def:pde10-halftrace | Przestrzeń obrazu śladu i norma ilorazowa; bez powoływania się na niedowiedzioną identyfikację z przestrzenią Gagliarda. | semantyczna |
| PDE-10-061 | lem:pde10-halftrace-rightinverse | Domknięte jądro operatora, ciąg minimalizujący i tożsamość równoległoboku, rzut ortogonalny, istnienie i jednoznaczność rozkładu. | semantyczna |
| PDE-10-062 | lem:pde10-halftrace-rightinverse | Niezależność podniesienia od reprezentanta, liniowość, prawostronna odwrotność i unikalna minimalna norma z Pitagorasa. | semantyczna |
| PDE-10-063 | lem:pde10-halftrace-rightinverse | Izometryczna bijekcja na ortogonalne dopełnienie, iloczyn skalarny, zupełność oraz ciągłe zanurzenie w L² brzegu. | semantyczna |
| PDE-10-064 | thm:pde10-trace-zero | Implikacja od domknięcia funkcji testowych do zerowego śladu, przez ciągłość operatora. | semantyczna |
| PDE-10-065 | thm:pde10-trace-zero | Aproksymanty gładkie aż do brzegu, lokalne iloczyny i prostowanie, zbieżność W^{1,p} na Q_+, zanik wartości brzegowych w L^p z porównania miar; d=1 osobno. | semantyczna |
| PDE-10-066 | thm:pde10-trace-zero | Całkowanie przez części pionowych przekrojów aproksymantów, poprawny znak składnika brzegowego, granica przez Höldera także dla p=1. | semantyczna |
| PDE-10-067 | thm:pde10-trace-zero | Test z pionowym odcięciem dla pochodnych stycznych, brak pochodnej odcięcia w kierunku stycznym, zbieżność zmajoryzowana. | semantyczna |
| PDE-10-068 | thm:pde10-trace-zero | Przedłużenie przez zero na pełnym Q, powrót przez Psi i zwarte odcięcie w U, bez korzystania z dowodzonej charakterystyki. | semantyczna |
| PDE-10-069 | thm:pde10-trace-zero | Przesunięcie w oryginalnych współrzędnych o a*epsilon, a>1+Lip(phi), dodatnia odległość od sztucznych ścian i oszacowanie y_d-phi(y')>0, zwarty nośnik we wnętrzu. | semantyczna |
| PDE-10-070 | thm:pde10-trace-zero | Splot po przesunięciu, oszacowanie błędu przez ciągłość przesunięć i przybliżoną jedynkę, p skończone, suma skończenie wielu aproksymacji oraz fragment wewnętrzny. | semantyczna |
| PDE-10-071 | cor:pde10-Poincare | Zaprzeczenie nierówności, normalizacja po odjęciu średniej, zwartość Rellicha, zachowanie normy i średniej przez granicę. | semantyczna |
| PDE-10-072 | cor:pde10-Poincare | Zamkniętość pochodnych, lokalna stałość z Poincarégo–Wirtingera na kostkach, łańcuchy kostek i spójność, przeliczalne pokrycie i jeden zbiór miary zero. | semantyczna |
| PDE-10-073 | cor:pde10-Poincare | Druga nierówność: aproksymacja z W_0^{1,p}(Omega), przedłużenie do większej kostki, zachowanie norm i pochodnych, nierówność na kostce. | semantyczna |
| PDE-10-074 | cor:pde10-zeroextension | Przedłużenie przez zero po ustaleniu jądra śladu, granice w L^p i W^{1,p}, identyfikacja pochodnych i zachowanie norm, brak błędnego koła. | semantyczna |
| PDE-10-075 | sec:pde10-summary | Rysunek: d>=2, p* przy p<d, skończone q przy p=d, beta<alpha przy p>d, alpha=1 dla p=infty. Kontrola wizualna pozostaje otwarta. | semantyczna + PDF |

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

## Iteracja 153
Źródło przed 920f2f484ed6beb87cb307fa7b27d4853baa3854, po dcfd5d9b5ee51864321624e0a5cf93bef4ace49b, commit e1af18fbdb61020e5f91cc56775ce88ba9342cd3. Jedenaście zmian: norma ilorazowa i rzut ortogonalny, pełny dowód jądra śladu przez tożsamości testowe na spłaszczonym wykresie oraz przesuwanie i splot w oryginalnych współrzędnych, dowód Poincarégo z łańcuchami kostek, przedłużanie przez zero, zakresy wykładników na schemacie. Nie dowodzimy identyfikacji normy śladu z normą Gagliarda. Pierwsza lektura kryteriów 060–075 oraz całego rozdziału zakończona. 32 unikatowe etykiety i 60 rozwiązanych odsyłaczy w źródłach 09 i 10, stos środowisk poprawny. Nie uruchamiano testów wykonywalnych, kompilacji, CI ani Lean; wizualna kontrola rysunku otwarta. Następny etap: druga lektura stabilizacyjna od kryterium 001 i trwałe testy wykonywalne tam, gdzie można określić automatyczną kontrolę.

## Iteracja 154 — druga lektura 001–011
Źródło przed dcfd5d9b5ee51864321624e0a5cf93bef4ace49b, po 896d52cded37551a2734e356dee1999d326f22c5, commit 186daf9112e748a6cf16a8640e8c851292145381. Ponownie odczytano cały zakres od wstępu do uwagi o krytycznym wykładniku i odpowiednie źródło rozdziału 09.

| Kryterium | Wynik drugiej lektury |
| --- | --- |
| PDE-10-001 | Doprecyzowano iniektywne odwzorowanie i jawne stałe równoważności norm składowych z normą euklidesową, także p=infty. |
| PDE-10-002 | Uzupełniono mierzalność złożeń z rzutem i zachowanie zbiorów zerowych przez przeciwobraz rzutu. |
| PDE-10-003 | Poprawna baza d=2 i pierwszy Hölder; jawny wzór G_j, mierzalność, ograniczoność i zwarte nośniki. |
| PDE-10-004 | Doprecyzowano tożsamość z H oraz podniesienie hipotezy indukcyjnej do właściwej potęgi. |
| PDE-10-005 | Bez zmiany: poprawne monotoniczne obcięcia i przypadki zerowych lub nieskończonych całek. |
| PDE-10-006 | Bez zmiany: całkowanie po prostych, potęgowanie i Tonelli. |
| PDE-10-007 | Bez zmiany: średnie i Cauchy–Schwarz dają 1/sqrt(d) dla gradientu euklidesowego. |
| PDE-10-008 | Jawnie oddzielono przypadek p=1 dla gładkich funkcji od wspólnego przejścia do W^{1,p}. |
| PDE-10-009 | Dodatniość i skończoność normy przed dzieleniem; jawna dopuszczalna (niekoniecznie optymalna) stała p(d-1)/(sqrt(d)(d-p)). |
| PDE-10-010 | Jawny zakres 1<=p<d, zachowanie tej samej stałej; rozpisano sumę zbiorów w oszacowaniu Czebyszewa i przeliczalne przejście do równości a.e. |
| PDE-10-011 | Jawna konwencja 1/infty=0; skalowanie zgodne z rozdziałem 09. |

Druga lektura: 11/75; 8 kryteriów doprecyzowanych, 3 bez zmian, jedenaście zmian źródłowych. 32 etykiety zachowane w tej samej kolejności, 61 wystąpień odsyłaczy ma cele w rozdziałach 09 i 10, stos środowisk poprawny. Dalsza część od definicji obszaru Lipschitzowskiego bez zmian. Nie wykonywano testów Python, kompilacji, CI ani Lean. Następna iteracja: druga lektura 012–024, szczególnie dowód przedłużania i brak błędnego koła w przypadku p=infty.

## Iteracja 155 — druga lektura 012–024
Źródło przed 896d52cded37551a2734e356dee1999d326f22c5, po 07a6cd32e34ff2028b8b3b9e5ffc6bcdbe9ea5b8, commit 705d07a2f06d2e9cced318b64558e308dca46d9e. Odczytano całą sekcję przedłużania, gęstości i zanurzeń oraz zależności w rozdziale 09.

| Kryterium | Wynik drugiej lektury |
| --- | --- |
| PDE-10-012 | Jawna definicja otoczenia wykresowego, strona wnętrza, konwencja R^0 i lambda_0 dla d=1, zwartość brzegu. |
| PDE-10-013 | Jawne wzory odwrotności i stałe Lipschitza <=1+L; zachowanie miary przez Tonellego bez zmian. |
| PDE-10-014 | Absolutna ciągłość ograniczeń phi, mierzalne ilorazy różnicowe, ograniczenie pochodnej, szczegóły absolutnej ciągłości złożenia. |
| PDE-10-015 | Bez zmian: Meyers–Serrin, Cauchy, identyfikacja złożenia i pochodnych w L^p. |
| PDE-10-016 | Rozpisano skończoność miary otoczeń i przejście od W^{1,infty} do W^{1,1}, potem odzyskanie oszacowań L^infty. |
| PDE-10-017 | Jawny sens nośnika klasy L^p i lokalność pochodnych przez testowanie poza A. |
| PDE-10-018 | Bez zmian: odbicie według twierdzenia rozdziału 09, p=infty przez p=1 i ograniczony nośnik. |
| PDE-10-019 | Bez zmian: zwarty nośnik odbicia w Q, powrót przez Psi i przedłużenie przez zero z odcięciem. |
| PDE-10-020 | Szczegóły normalizacji odcięć, suma równa jeden także na brzegu, słaba reguła łańcuchowa dla ruchu sztywnego i równoważność norm. |
| PDE-10-021 | Uproszczenie gęstości: bez dodatkowego odcięcia, ponieważ Eu ma już zwarty nośnik. Jawny nośnik splotu i norma błędu restrykcji. |
| PDE-10-022 | Rozpisano oszacowanie przez Eu, sprzężone wykładniki i osobny przypadek q=p*. |
| PDE-10-023 | Dla q>d jawny p_0=dq/(d+q), p_0*=q; oszacowanie składowych na Omega i zastosowanie części (i), zamiast dodatkowego przedłużenia. |
| PDE-10-024 | Zdefiniowano normę i półnormę Höldera, wskazano istniejący dowód we wniosku o Morreyu; brak zależności kołowej. Szczegóły dowodu Morreya będą objęte następną lekturą 025–036. |

Druga lektura 24/75; w tej iteracji 10 kryteriów doprecyzowanych, 3 bez zmian, 11 zmian źródłowych. Zachowano 32 etykiety w tej samej kolejności; wszystkie 62 wystąpienia odsyłaczy mają cele w rozdziałach 09 i 10; stos środowisk poprawny; materiał przed i po kontrolowanym fragmencie bez zmian. Nie uruchamiano testów wykonywalnych, kompilacji, CI ani Lean. Następna iteracja: druga lektura 025–036, Morrey i reprezentanci wyższych rzędów.

## Iteracja 156 — druga lektura 025–036
Źródło przed 07a6cd32e34ff2028b8b3b9e5ffc6bcdbe9ea5b8, po dffafe3cd6a585d7a8ea8aa32e9707e77202ae56, commit 59f83c50c4392f2ea19db3c335aef5598aee6fb5. Odczytano pełną sekcję Morreya oraz odpowiednie twierdzenia o wygładzaniu i reprezentantach jednowymiarowych z rozdziału 09.

| Kryterium | Wynik drugiej lektury |
| --- | --- |
| PDE-10-025 | Doprecyzowano R>0, znaczenie C^1 na domknięciu i miarę kuli; poprawne uśrednianie. |
| PDE-10-026 | Jawna całka po obrazie kuli, uzasadnienie zawierania i mierzalności zbioru par (t,z), Tonelli. |
| PDE-10-027 | Bez zmian: całka t^(-d-1), stała, całkowalność jądra i pominięcie singletonu. |
| PDE-10-028 | Rozpisano całkę biegunową z d*omega_d, promień, oszacowanie gradientu na całej przestrzeni i jawną dopuszczalną stałą. |
| PDE-10-029 | Bez zmian: oszacowanie supremum na kuli jednostkowej i równoważność norm. |
| PDE-10-030 | Uzupełniono zbieżność aproksymantów również w półnormie krytycznego wykładnika Höldera, przez przejście m do nieskończoności w oszacowaniu różnic. |
| PDE-10-031 | Bez zmian: poprawne lokalne wygładzanie, nieujemne jądro i ograniczenie euklidesowego gradientu dla p=infty. |
| PDE-10-032 | Rozpisano warunek Cauchy'ego i niezależność ciągów ze zbioru pełnej miary; identyfikację supremum z istotnym supremum. |
| PDE-10-033 | Bez zmian: pełna norma przez przedłużenie, przypadek d=1 i jednoznaczność. |
| PDE-10-034 | Jawna norma wyższego rzędu, ciągłość zanurzenia przez oszacowania każdej składowej normy także dla p=infty. |
| PDE-10-035 | Uściślono zawieranie odcinka w mniejszej kuli i orientację całki dla t<0; identyfikacja pochodnych poprawna. |
| PDE-10-036 | Uzasadniono pełną normę, liniowość i iniektywność zanurzenia oraz rozpisano kontrprzykład x^theta dla dowolnego beta>theta>0 (beta<=1) w wymiarze 1. |

Druga lektura 36/75. W tej iteracji 8 kryteriów doprecyzowanych, 4 bez zmian, 11 zmian źródłowych. Kontrola źródeł 09 i 10: 32 unikatowe etykiety, 61/61 rozwiązanych odsyłaczy; stos środowisk poprawny, materiał przed i po sekcji bez zmian. Nie uruchamiano testów wykonywalnych, kompilacji, CI ani Lean. Następna iteracja: druga lektura 037–049, aproksymacja na kostkach, Rellich–Kondrachov, interpolacja i kontrprzykłady.

## Iteracja 157 — druga lektura 037–049
Źródło przed dffafe3cd6a585d7a8ea8aa32e9707e77202ae56, po 958cf2e404490f88b60dbd5729acfc1e2e0ebfe0, commit cee550d2c734346c3edc3a20fe2de7eed1ee7bf0. Odczytano pełną sekcję zwartości i odpowiednie twierdzenie Poincarégo–Wirtingera oraz skalowanie w rozdziale 09.

| Kryterium | Wynik drugiej lektury |
| --- | --- |
| PDE-10-037 | Jawnie wskazano całkowitość N i niezależność średnich od reprezentanta. |
| PDE-10-038 | Uzupełniono własność P_N^2=P_N; dowód kontrakcyjności poprawny. |
| PDE-10-039 | Uzasadniono restrykcję słabych pochodnych przez funkcje testowe; dopuszczalna dokładniejsza stała h*d^max(1/2,1-1/p) przez porównanie norm wektorów dla p<2 oraz p>=2. Nie twierdzimy, że jest optymalna. |
| PDE-10-040 | Jawny wybór kostki osiowej i długości L, normy na Q i znaczenie restrykcji Eu_n. |
| PDE-10-041 | Rozpisano wymiar N^d, ograniczenie współczynników w normie l^p i konstrukcję sieci przez Heinego–Borela. |
| PDE-10-042 | Bez zmian: zagnieżdżone zbiory indeksów, przekątna, oszacowanie odległości, zupełność i restrykcja, także p=1. |
| PDE-10-043 | Jawny wzór na theta i jego jednoznaczność. |
| PDE-10-044 | Bez zmian: interpolacja różnic i przypadki q<=p, ciągłość i zupełność. |
| PDE-10-045 | Rozpisano interpolację różnic przy p=d wraz z parametrem i stałą oraz odwołanie do ciągłości. |
| PDE-10-046 | Bez zmian: Arzelà–Ascoli, zachowanie półnormy granicy i przypadek p=infty. |
| PDE-10-047 | Jawny wybór delta dla C>0, osobno C=0 i przejście do pełnej normy Höldera. |
| PDE-10-048 | Jawne równości norm W^{1,p} i L^{p*} na Omega z nośnika i skalowania. |
| PDE-10-049 | Rozszerzono kontrprzykład translacyjny na p=infty; odległość supremum stała i dodatnia. |

Druga lektura 49/75. Dziesięć kryteriów doprecyzowanych, trzy bez zmian, 10 zmian źródłowych. 32 unikatowe etykiety zachowane w kolejności, 62/62 wystąpień odsyłaczy ma cele w rozdziałach 09 i 10; stos środowisk poprawny, poza kontrolowaną sekcją brak zmian. Nie wykonywano testów Python, kompilacji, CI ani Lean. Następna iteracja: druga lektura 050–059, przypadek krytyczny, ostrość Morreya i operator śladu.

## Iteracja 158 — druga lektura 050–059
Źródło przed 958cf2e404490f88b60dbd5729acfc1e2e0ebfe0, po c9e0238c27f8cf7b8b836cf1a87ddb9ad3d9e1ec, commit b77769852319943c531881ce5cbbb3f11432ff64. Odczytano sekcję przypadku krytycznego, ostrość Morreya oraz definicję miary brzegowej i twierdzenie o śladzie.

| Kryterium | Wynik drugiej lektury |
| --- | --- |
| PDE-10-050 | Rozpisano tożsamość testową z normalną zewnętrzną i znoszeniem całek po wspólnych sferach. |
| PDE-10-051 | Jawna całka gradientu, wartość całki t^d exp(-dt) przez całkowanie przez części, zbieżność normy L^d do zera, istotne supremum na kuli dodatniej miary. |
| PDE-10-052 | Rozpisano zanik wyrazu brzegowego przez podstawienie s=log(e/eta), zbieżność zmajoryzowaną w całkach testowych oraz jawny promień zbioru v>M. |
| PDE-10-053 | Uzasadniono wybór punktów o różnych wartościach funkcji, zbieżność jednostajną i sprzeczność z dodatnią dolną granicą półnormy przy beta=alpha. |
| PDE-10-054 | Jawna nierówność dla obciętych miar Hausdorffa H^s_{K delta}, przejście do granicy i niezmienniczość względem ruchów sztywnych. |
| PDE-10-055 | Uzupełniono borelowskość wykresu, homeomorfizm podstawy i wykresu, przejście od funkcji charakterystycznych przez proste do nieujemnych mierzalnych. |
| PDE-10-056 | Mierzalność wartości brzegowych przez średnie pionowe, mierzalny reprezentant pochodnej, skończoność norm przekrojów z Fubiniego; oszacowanie dla p=1 i d=1 bez zmian. |
| PDE-10-057 | Jawna lokalna nierówność z czynnikiem (1+L_j^2)^((d-1)/2), wysokością h_j oraz kontrolą kierunkowej pochodnej przez euklidesowy gradient i regułę iloczynu. |
| PDE-10-058 | Bez zmian: skończony rozkład jedynki na brzegu, część wewnętrzna zerowa, suma stałych. |
| PDE-10-059 | Rozpisano liniowość przez kombinacje aproksymantów i ograniczoność przez ciągłość normy. |

Druga lektura 59/75. Dziewięć kryteriów doprecyzowanych, jedno bez zmian, 13 zmian źródłowych. Zachowano wszystkie 32 etykiety w kolejności, 62/62 wystąpień odsyłaczy ma cele w rozdziałach 09 i 10; stos środowisk poprawny; poza kontrolowanym fragmentem brak zmian. Nie uruchamiano testów wykonywalnych, kompilacji, CI ani Lean. Następna iteracja: druga lektura 060–075 (przestrzeń śladów, jądro śladu, Poincare, przedłużenie przez zero i schemat), zamknięcie drugiej lektury.

## Iteracja 159 — druga lektura 060–075
Źródło przed c9e0238c27f8cf7b8b836cf1a87ddb9ad3d9e1ec, po 0fafe67db377f216e923f6a241bddb0a10b5220c, commit 9edcd598db929c93a4cce9a32f16be9e522a2901. Odczytano cały końcowy fragment i zależności o zamkniętości pochodnych, zwartym iloczynie oraz Poincarém na kostce w rozdziale 09.

| Kryterium | Wynik drugiej lektury |
| --- | --- |
| PDE-10-060 | Bez zmian: definicja przestrzeni śladów, bez identyfikacji z normą Gagliarda. |
| PDE-10-061 | Jawny iloczyn skalarny H^1, uzasadnienie zupełności, środek ciągu minimalizującego i rozwinięcie wielomianu dla ortogonalności. |
| PDE-10-062 | Bez zmian: niezależność reprezentanta, liniowość i unikalne minimum. |
| PDE-10-063 | Korekta językowa iniektywności, izometria i zupełność poprawne. |
| PDE-10-064 | Uzasadniono gładkość przedłużenia przez zero funkcji testowych i zastosowanie klasycznej restrykcji. |
| PDE-10-065 | Bez zmian: zbieżność aproksymantów w Q_+ i zanikanie śladów, również d=1. |
| PDE-10-066 | Jawne oszacowania błędów trzech całek przez Höldera także przy p=1 i końcowa tożsamość na Q. |
| PDE-10-067 | Wskazano całkowalne majoranty i tożsamość testową dla pochodnej stycznej. |
| PDE-10-068 | Bez zmian: powrót przez Psi i przedłużenie zwartego fragmentu bez błędnego koła. |
| PDE-10-069 | Rozpisano kontrolę odległości od ścian i nierówność wysokości względem grafu, jawny nośnik splotu. |
| PDE-10-070 | Rozpisano różnicę splotów, kontrakcyjność przez Jensena i Tonellego, komutację słabych pochodnych z przesunięciem i splotem. |
| PDE-10-071 | Jawny kwantyfikator u, ponowne oznaczenie wybranego podciągu. |
| PDE-10-072 | Bez zmian: argument łańcuchów kostek, spójność, przeliczalne pokrycie. |
| PDE-10-073 | Uzupełniono równoważność normy gradientowej z normą Sobolewa na W_0^{1,p}. |
| PDE-10-074 | Jawnie wskazano zachowanie pełnej normy W^{1,p}; identyfikacja słabych pochodnych poprawna. |
| PDE-10-075 | Doprecyzowano opis ciągów ograniczonych oraz wyłączenie d=1 ze schematu. Kontrola wizualna nadal otwarta. |

Druga lektura 75/75 (warstwa semantyczna): w tej iteracji 11 kryteriów doprecyzowano, 5 bez zmian, 16 zmian źródłowych. Łącznie w drugiej lekturze 56 kryteriów doprecyzowanych i 19 bez zmian (iteracje 154–159). Kontrola źródła: 32 etykiety w tej samej kolejności, 65/65 rozwiązanych wystąpień odsyłaczy w rozdziałach 09 i 10, stos środowisk poprawny; wcześniejszy materiał bez zmian. Nie uruchamiano testów wykonywalnych, kompilacji, CI ani Lean. Nie ogłaszamy stabilizacji rozdziału. Następny etap: trwałe wykonywalne testy regresyjne, kontrola strukturalna i dedykowane CI z kompilacją oraz renderem PDF, następnie niezależna trzecia lektura.

## Iteracja 160 — testy wykonywalne i CI
Po odświeżeniu gałęzi potwierdzono, że iteracje 157–159 już zakończyły drugą lekturę 75/75. Nie powtarzano audytu ani nie modyfikowano źródła rozdziału (blob odczytany: 0fafe67db377f216e923f6a241bddb0a10b5220c).

Dodano testy w `test_embeddings.py` (commit 666c664e33efa35eb0db53fc5dd1cad8c15b619e): 009–011, 023/028, 037–039, 043, 051–052, 069 oraz 075. Są to skończone kontrole wzorów i zakresów, nie dowody twierdzeń analitycznych. Dodano workflow `.github/workflows/partial-differential-equations-ch10.yml` (commit 1884559084ee186ca9ed275b83ad5a85f9e2eb77): kontrola rejestru, odsyłaczy i środowisk, kolejności książki i manifestu, zgodności preambuły, kompilacja samodzielnego rozdziału z numerycznymi etykietami zewnętrznymi, diagnostyka i render PDF.

Rzeczywisty przebieg CI: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45629813428, job 139259658303, head 1884559084ee186ca9ed275b83ad5a85f9e2eb77. W chwili odczytu API kroki testów wykonywalnych i kontroli strukturalnej zakończyły się sukcesem; kompilacja trwała, render i artefakty oczekiwały. Nie stwierdzono jeszcze sukcesu całego CI ani poprawności wizualnej PDF; Lean nie uruchamiano. Następny etap: odczyt zakończonego CI, kontrola wszystkich stron i niezależna trzecia lektura (001–075).

## Iteracja 161 — kontrola PDF i trzecia lektura 001–011
Rzeczywisty przebieg 45629813428, job 139259658303: 7 testów PASS (0.009 s), 75 kotwic kryteriów, 32 etykiety i 65 wystąpień odsyłaczy; kompilacja PASS, diagnostyka FAIL z powodu jednego Overfull hbox 15.01184 pt w linii 1445. Artefakt 15030093521 (SHA256 1f3560e89c5f4efe59a633ea6cdac2281255027fc7bbf9312b95588b2c2827c3, zgodny z metadanymi) pobrano i odczytano. PDF 22 strony; obejrzano wszystkie 22 strony w arkuszach kontaktowych oraz stronę 16 w pełnym rozmiarze. Schemat na stronie 22 bez widocznej kolizji. W finalnym logu 1 overfull, 1 underfull (badness 1127), 34 ostrzeżenia hyperref o pustych celach samodzielnego PDF (numery odsyłaczy zewnętrznych bez kotwic), brak niezdefiniowanych odsyłaczy i brakujących znaków. Poprawiono wyłącznie układ dwóch całek dla log log(e/r) na stronie 16: osobne wiersze align*, bez zmiany matematycznej. Commit 76b5ced862edcc1ad50c9f67a7b48fe5394aff2e, blob af063e08bc56cbf84bac37795bbe741eae8bc996. 32 etykiety, 65 wystąpień odsyłaczy, zrównoważone środowiska. Poprawiony PDF nie został jeszcze zweryfikowany. Nie ogłaszamy sukcesu CI.

Trzecia lektura 001–011: ponownie odczytano źródło od wstępu do uwagi o krytycznym wykładniku oraz rzeczywisty dowód gęstości i skalowania w rozdziale 09. Wszystkie 11 kryteriów bez nowych usterek: 001 równoważność norm i definicje; 002 konwencje i mierzalność; 003–004 oba zastosowania Höldera i indukcja; 005 obcięcia i zbieżność monotoniczna; 006–007 całkowanie po prostych, średnie i stała; 008–009 reguła łańcuchowa oraz wykładniki; 010 gęstość i identyfikacja granic także na nieskończonej mierze; 011 skalowanie krytyczne i nadkrytyczne. Nie zmieniano kontrolowanego zakresu. Trzecia lektura 11/75. Następna iteracja: kontrola poprawionego przebiegu CI i PDF oraz kryteria 012–024. Lean nie uruchamiano.

## Iteracja 162 — poprawiony PDF i trzecia lektura 012–024
Przebieg 45630403835 (head 9a1b051153eea19ccd36a1276a9fe508721e5eda), job 139261715939: wszystkie kroki zakończone sukcesem, w tym 7 testów, preflight, kompilacja, diagnostyka/render oraz upload. Artefakt 15029774956 pobrano; SHA256 4f01479d6dc4b1ac4aa09c574feb1801bb61f16d93b8dbeec76f3416a47648ba zgodny z metadanymi. PDF 22 strony A4. Porównanie pikselowe z artefaktem 15030093521: 15 stron identycznych (1–15), zmienione 16–22 przez przełamanie wzoru i przesunięcie tekstu. Obejrzano wszystkie 7 zmienionych stron w arkuszach kontaktowych; wzór na s. 16 mieści się w marginesach, schemat na s. 22 czytelny. Finalny log: brak overfull, niezdefiniowanych odsyłaczy, brakujących znaków i Undefined control sequence; jeden underfull (badness 1127) oraz 33 ostrzeżenia o pustych celach linków zewnętrznych w izolowanym rozdziale. Nie jest to kompilacja całej książki.

Trzecia lektura źródła af063e08bc56cbf84bac37795bbe741eae8bc996, zakres 012–024, wraz z rzeczywistymi dowodami rozdziału 09 (Meyers–Serrin, reguła iloczynu, odbicie, zwarte odcięcie) oraz wcześniej zweryfikowanymi nierównościami Sobolewa. 012–013 poprawna definicja wykresu, przypadek d=1, dwulipschitzowskość, zachowanie miary. 014–016 poprawne pochodne po prostych i testowanie, przejście przez gęstość dla skończonego p i redukcja do p=1 na zbiorach skończonej miary dla p=infty. 017–019 poprawne odcięcie przy sztucznych ścianach, odbicie z normą 2^(1/p) i powrót do oryginalnych współrzędnych. 020 poprawny rozkład jedynki i wspólny zwarty nośnik. 021 poprawna gęstość przez splot. 022–023 poprawne przypadki q<=p* oraz p=d, jawny wybór p_0. 024 prawidłowe odesłanie do dowodu Morreya (ponowna kontrola tego dowodu w 025–036). Wszystkie 13 kryteriów bez nowych usterek, bez zmian źródła. Trzecia lektura 24/75. Lean nie uruchamiano. Następna iteracja: 025–036, nierówność Morreya i reprezentanci wyższych rzędów.

## Iteracja 163 — trzecia lektura 025–036
Odczytano całą sekcję Morreya (blob af063e08bc56cbf84bac37795bbe741eae8bc996) i rzeczywiste dowody lokalnego wygładzania, charakterystyki absolutnej ciągłości i oszacowań jednowymiarowych w rozdziale 09. 025–027: prawidłowy wzór całkowy po odcinku, mierzalność zbioru par, jakobian i całka t^(-d-1), lokalna całkowalność jądra. 028–029: poprawny warunek p>d, wykładnik 1-d/p, dopuszczalna stała, kontrola supremum. 030: gęstość, identyfikacja granicy przez sumowalny podciąg i zbieżność w pełnej normie Höldera. 031–032: przypadek p=infty przez lokalny splot, wybór diagonalny, gęsty zbiór pełnej miary, jednoznaczne przedłużenie Lipschitzowskie bez aproksymacji W^{1,infty}. 033: przedłużenie na całe Rd, ograniczenie na domknięcie i przypadek d=1. 034–035: przynależność pochodnych do W^{1,p}, lokalne wygładzanie i przejście w tożsamości całkowej, ciągłość pochodnych klasycznych. 036: poprawna interpretacja normy na domknięciu, przypadki d=1 i p=1. Bez nowych błędów matematycznych. Dwie korekty notacyjne: wielowskaźnik gamma zamiast alpha w tezie wniosku Morreya (alpha oznacza wykładnik Höldera), jawne przypomnienie omega_d w dowodzie twierdzenia. Commit d5690cbeffd1e6a52f36e71a664e1777a57193bc, blob f1df89a4092512e16d79110b5eb5bd48e9556d85. Zachowano kolejność 32 etykiet i 65 wystąpień odsyłaczy, stos środowisk zrównoważony. Trzecia lektura 36/75. Dotychczasowy sukces CI i PDF dotyczy poprzedniego blobu; poprawki notacyjne wymagają ponownego przebiegu i kontroli PDF. Nie uruchamiano Lean. Następna iteracja: 037–049, zwartość Rellicha–Kondrachova i kontrprzykłady.
