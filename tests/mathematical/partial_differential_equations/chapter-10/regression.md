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
| PDE-10-024 | thm:pde10-domain-embed | p>d i p=infty: odłożone do dowodu Morreya, sprawdzić pełną normę i reprezentanta na domknięciu; nie stosować tego wyniku w dowodzie przedłużania. | semantyczna (otwarte do następnej iteracji) |

## Iteracja 148
Źródło przed 22b013b3e972ece5feaa83488df6fdc89a1f3bfe; po 7678d73026ba49e7060cda158e4286c2e559f165, commit e504d11f70adbc028f346cab57807d5ed40c22b8. Przejrzano wstęp, Loomisa–Whitneya, Sobolewa dla p=1 i 1<p<d, skalowanie. Jedenaście zmian źródłowych: hipotezy i norma, przypadki całek 0 i nieskończonych, baza indukcji, obcięcia, całkowanie po prostej, stała gradientowa, regularność potęgi w zerze, wykładniki, identyfikacja granic, hipotezy i ograniczenie norm w skalowaniu. Zachowano kolejność 32 etykiet; stos środowisk poprawny; materiał od definicji obszaru Lipschitzowskiego bez zmian. Dodano trzy odsyłacze do rozdziału 09. Nie uruchamiano testów Python, CI, kompilacji ani Lean w tej iteracji. Pierwsza próba zapisu raportu: konflikt współbieżnej aktualizacji gałęzi, ponowiono zapis. Następny etap: obszary Lipschitzowskie, przedłużanie, gęstość i zanurzenia. Pierwsza lektura otwarta.

## Iteracja 149
Źródło przed 7678d73026ba49e7060cda158e4286c2e559f165, po b3e4b53d5f24ad3b09b95370064a4a386c0424a4, commit c4ccebae29c837bf32df7e08c5ea89b80cc8730e. Dwie wcześniejsze próby zapisu odrzucone przez konflikt współbieżnych zmian gałęzi; po odczytaniu tego samego bloba zapis zakończył się sukcesem. Przebudowano dowód przedłużania (trzy kroki) i skorygowano odwołanie przy p=d. Przejrzano również definicję, gęstość i zanurzenia dla p<=d. Zachowano 32 etykiety w tej samej kolejności, 33 wystąpienia odsyłaczy, stos środowisk poprawny. Nie wykonywano testów Python, kompilacji ani Lean. Kryteria 012–023 poddane pierwszej lekturze; 024 pozostaje otwarte do audytu Morreya. Potrzebna druga lektura szczegółów nowego dowodu, kontrola odsyłaczy i walidacja techniczna. Następny etap: nierówność Morreya i wniosek na obszarze, w tym końcowy przypadek p=infty.
