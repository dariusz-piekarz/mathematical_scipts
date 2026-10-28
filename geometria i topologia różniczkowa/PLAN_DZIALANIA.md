# Aktualny plan i pokrycie przeglądem

Stan: 28 października 2026. Gałąź: `review/rozdzialy-matematyka`.
Książka ma **38 rozdziałów, pięć części i trzy dodatki**. Numery w nazwach
plików są historyczne; numer w PDF ustala kolejność importów.
Skład roboczy podzielono na cztery tomy: rozdziały 1–10, 11–22,
23–30 oraz 31–38 z dodatkami. Plik zbiorczy pozostaje dostępny
do okazjonalnego składu.

To jedyna bieżąca lista zadań i propozycji. Uzasadnienia zmian oraz wyniki
sprawdzania konkretnych wersji są w [PRZEGLAD.md](PRZEGLAD.md), a budowanie
i organizacja plików w [README.md](README.md).

## Bieżący zakres i kolejność

1. Niezależny audyt dodatków A i B zakończono 25 października.
   W dodatku A skorygowano zakres twierdzenia Walla do $n\geq5$
   i uzupełniono katalog o rzeczywiście używane wyniki zewnętrzne,
   w tym wersję $h$, ciąg Rothenberga, ciąg chirurgii, torsję
   Whiteheada, geometrię globalną, Bardena i klasyfikację sfer
   wymiaru siedem. W dodatku B sprawdzono rachunki homologii lokalnej,
   cechy Eulera, uchwytów i modeli powierzchni; doprecyzowano
   homeomorfizm, skończony typ CW kobordyzmu i związek z dualnością
   Poincarégo. Pełny skład oraz strony obu dodatków sprawdzono.
2. Rozdziały 36 i 37 sprawdzono wspólnie 27 października na prośbę autora.
   Tego samego dnia zakończono pełny audyt rozdziału 38, ostatniego
   numerowanego rozdziału. Po podziale tomu III na III i IV
   sprawdzono mapę, numerację, odsyłacze i indeksy w czterech PDF-ach.
   Trzy zaplanowane uzupełnienia tomu III zakończono 28 października.
   Na prośbę autora dopisano następnie wizualne przykłady
   dwóch kolejnych uchwytów oraz przeplatania dwóch
   uchwytów sfery w rozdziale 26; aktualny zakres tych zmian
   jest opisany w tabeli pokrycia poniżej.
   Pierwsze trzy punkty planu tomu IV opracowano 28 października.
   Most między wymiarami trzy i cztery dopisano 28 października
   na początku rozdziału 34; cztery punkty planu tomu IV zakończono.
   Wymiary cztery pozostają wykładem informacyjnym z dokładnymi
   hipotezami i źródłami. Zwykła iteracja obejmuje jeden rozdział,
   chyba że etap wymaga wspólnego dowodu.
3. Przed każdą iteracją pobierać zmiany współautora. Zmieniać źródło
   w odpowiednim pliku rozdziału, zapisywać uzasadnienia w
   `PRZEGLAD.md`, składać odpowiedni tom i sprawdzać zmienione strony.
   Przed wypchnięciem uruchamiać `buduj_tomy.ps1`, kontrolować indeksy
   i odsyłacze między tomami, aktualizować PDF-y tomów, zatwierdzać
   i wypychać ukończony etap. Skład zbiorczy jest okazjonalny.

Nie dodajemy zadań. Rozmaitości z brzegiem, grupy wolne, iloczyny wolne,
geometria Kleina i geometrie Thurstona już są w źródłach; nie tworzymy ich
duplikatów. Freedman, Donaldson i egzotyczne R⁴ należą do tomu IV,
w osobnych rozdziałach.

## Dotychczasowe rozbudowy i zakres wyników zewnętrznych

Każdy punkt realizować etapami w odpowiednich rozdziałach, z teorią,
szczegółowymi dowodami dostępnych kroków, przykładami i rysunkami.
Przed rozbudową porównać istniejący tekst z oryginalnymi źródłami;
głębokiego wyniku użytego z zewnątrz nie nazywać własnym pełnym dowodem.

1. **Twierdzenie Walla o przeszkodzie chirurgicznej — rozdziały 27–28.**
   Rozpisano zakres twierdzeń 5.6 i 6.4 Walla dla wszystkich grup
   podstawowych i wymiarów $n\geq5$: wersję parzystą nad
   $\Z[\pi]$, preferowane bazy i prostą torsję, wersję nieparzystą
   przez $SU/RU$ i ruchy $T1$--$T4$, a także przypadek $n=5$.
   W rozdziale 28 wskazano oddzielnie realizację przez twierdzenia
   5.8 i 6.5 oraz zakres gładkiego $s$-kobordyzmu. Rachunki
   i przejścia algebraiczne są rozpisane. Krok izotopii obramowanej
   sfery z lematu 5.5 oraz rozłączne reprezentowanie generatorów
   w przypadku nieparzystym wyprowadzono z twierdzenia 1.1 Walla,
   dla ruchu $T1$ rozpisano lokalny rachunek dwóch lagranżjanów,
   dla $T2$--$T4$ rachunek bazy dualnej oraz zmianę lagranżjanu
   po pojedynczej chirurgii;
   chirurgie poniżej środka, reprezentację sfer w środku wymiaru,
   przygotowanie kobordyzmu oraz część
   relacji $SU/RU$ przyjęto jako jawne lematy Walla z hipotezami
   i źródłem. Autor zaakceptował je jako wejścia zewnętrzne;
   końcowy audyt nowego tekstu przeprowadzono 20 października;
   porównanie dekoracji $s/h$ pozostaje osobnym wynikiem zewnętrznym.
2. **Klasyfikacja Bardena — rozdział 29.** Rozpisano twierdzenie 2.2
   o realizacji zadanego izomorfizmu $H_2$ oraz twierdzenie 2.3
   o kanonicznych modelach i pełności $(H_2,\iota)$. Dowody obejmują
   ograniczenia algebraiczne, kobordyzm, chirurgię na $\pi_1$ i $H_2$,
   lematy 4.1–4.4, indukcję, sześciowymiarowy $h$-kobordyzm,
   konstrukcje modeli oraz porównanie spin/niespin. Jawne wejścia
   zewnętrzne to wyniki Thoma, Nowikowa, Walla, Whiteheada,
   Haefligera, Milnora i Smale'a. Pełny audyt całego rozdziału
   zakończono 20 października, pozostawiając te wejścia jawnie zewnętrzne.
3. **Sfery Milnora — rozdział 30: etap ukończony.**
   Rozpisano konstrukcję wiązek, klasy charakterystyczne,
   homologię i typ homotopijny ich sfer jednostkowych.
   Niezmiennik Milnora uzupełniono o spinowy niezmiennik
    Eellsa--Kuipera i klasyfikację rodziny wiązek: dokładnie 16
    z 28 zorientowanych typów. Sumy spójne $M_3$ dają wszystkie
    28 klas zorientowanych i 15 klas bez wyboru orientacji.
    Zupełność $\mu$ oraz $\Theta_7\cong\Z/28$ są jawnymi wynikami
    zewnętrznymi Eellsa--Kuipera i Kervaire'a--Milnora.
    Twierdzenie Hirzebrucha,
   całkowitość indeksu Diraca i wysokowymiarowe twierdzenie
   Poincarégo pozostają jawnymi wejściami zewnętrznymi.
    Audyt wcześniejszej treści, w tym rysunku i zależności
    między twierdzeniami, zakończono 19 października;
    klasyfikację dopisano i sprawdzono 20 października.
4. **Twierdzenia wymiaru cztery — rozdziały 34–38.**
   Rachunki form przecięcia i obramowań, uchwyty Cassona,
   klasyfikację Freedmana, przeszkodę Donaldsona i konstrukcje
   egzotycznych $\R^4$ opracowano oraz poddano audytom do
   27 października. Analiza przestrzeni moduli, twierdzenie
   o zanurzaniu dysku i klasyfikacja pozostają nazwanymi
   wejściami z dokładnymi hipotezami i źródłami. Dalsze
   uzupełnienia dydaktyczne są zaplanowane poniżej.

## Plan uzupełnień po podziale na tomy III i IV

Plan dla tomu III potwierdzono z autorem 27 października 2026.
Kolejność: najpierw konstrukcyjne uzupełnienie rozdziału 28,
następnie jeden przykład prowadzony przez rozdziały 26–28,
na koniec zbiorcza mapa hipotez.
Kolejność poniżej zapisuje etapy i priorytet pozostałych prac. Każdą zmianę prowadzić
w odpowiadającym jej rozdziale, z definicją, intuicją, obliczalnym
przykładem i dokładnym źródłem dla wyników głębokich. Po każdym
etapie sprawdzić skład czterech tomów, indeksy, odsyłacze i strony
ze zmienionymi rysunkami.

### Tom III — kobordyzmy i chirurgia, rozdziały 23–30

1. **Rozdział 28 (`24-ciag-chirurgii.tex`) — ciąg chirurgii; etap zakończony 27 października.**
   Rozpisać konstrukcyjne znaczenie kolejnych strzałek od danych
   normalnych i $[X,G/O]$ przez przeszkodę $\theta$ oraz działanie
   $L_{n+1}$ na zbiorze struktur. Diagram kobordyzmu nad $X\times I$
   ma objaśnić dokładność przez orbity i stabilizatory oraz różnicę
   wymiarów $n$ i $n+1$. Dodać wersję względną do brzegu z pełnymi
   hipotezami. Powiązać zbiór struktur gładkich sfery $S^7$ ze sferami Milnora
   z rozdziału 30, bez sugerowania obliczenia całego ciągu.
   Identyfikacja danych z $G/O$, realizacja działania i dokładność
   Walla pozostają jawnymi wynikami zewnętrznymi.
2. **Rozdziały 26–28 — jeden śledzony przykład; etap zakończony 27 października.**
   Standardową chirurgię $S^6\to S^3\times S^3$ przeprowadzono przez
   ślad uchwytu, jądro hiperboliczne, zerową klasę w $L_6^s(\Z)$
   i punkt bazowy ciągu chirurgii. Wskazano wybrane dane normalne
   i odesłano do istniejących rachunków rozdziału 27.
3. **Mapa hipotez — etap zakończony 28 października.** W rozdziale 28
   zestawiono DIFF/TOP, granice wymiarowe, założenia o $\pi_1$
   i ustalonym brzegu oraz różnicę dekoracji $s/h$. Osobno
   wyjaśniono rozmaitość wymiaru pięć i ślad wymiaru sześć,
   rozróżniając kryterium od twierdzeń realizacyjnych Walla.
   Mapa syntetyzuje istniejące wyniki; wariant TOP pozostaje
   jawnym wejściem zewnętrznym.

### Tom IV — wymiary trzy i cztery, rozdziały 31–38 i dodatki

1. **Rozdziały 34–36 — droga do klasyfikacji TOP; etap zakończony 28 października.**
   W rozdziale 34 dodano diagram obramowanego splotu Hopfa i niewęzła,
   a w rozdziale 36 tabelę form $H$, $[1]$, $E_8$ i $2E_8$ z parzystością,
   sygnaturą, niezmiennikiem Kirby'ego--Siebenmanna oraz istnieniem
   struktur TOP i DIFF. Schemat zależności łączy dyski immersyjne,
   wieże Cassona, lokalnie płaskie dyski i sfery dualne z chirurgią,
   kontrolą $\pi_1$ i klasyfikacją. Istniejących rachunków $E_8$
   ani drzewa Cassona nie powielono; twierdzenia Freedmana--Quinna
   i o sferach dualnych pozostają jawnymi wynikami zewnętrznymi.
2. **Rozdział 37 — Donaldson; etap zakończony 28 października.**
   Dodano obliczalny przykład instantonu BPST na $S^4$ z energią
   $8\pi^2$ i $c_2=1$, w tym drugą trywializację przy nieskończoności.
   Mapa wejść zestawia cechowanie, indeks i regularność przestrzeni moduli,
   rozwiązania redukowalne, koncentrację krzywizny, wyniki Uhlenbeck
   oraz konstrukcję końca Taubesa i Donaldsona. Skorygowano przejście
   od rachunku sygnatury do liczby klas o kwadracie $-1$.
   Analiza przestrzeni moduli i diagonalizacja Donaldsona pozostają
   wynikami zewnętrznymi. Skład i zmienione strony sprawdzono.
3. **Rozdział 38 — egzotyczne $\R^4$; etap treści zakończony
   28 października.** Wyjaśniono topologiczną rodzinę radialną
   małych struktur De Michelisa--Freedmana: wspólny zwarty rdzeń,
   rozróżnienie par przez analizę końców okresowych i przejście
   od przeliczalnej krotności każdego typu do kontinuum typów.
   Diagram porównuje te wejścia z indukcją dużych struktur Gompfa
   przez zwarty blok $X$ i świadków $K_n$. Zachowano warunki
   zanurzeń i orientacje; głęboki wynik De Michelisa--Freedmana
   jest cytowany. Skład i zmienione strony sprawdzono.
4. **Most między wymiarami trzy i cztery; etap zakończony
   28 października.** Na początku rozdziału 34 porównano cięcie
   kontrolowanej szyjki $S^2\times D^1$ w potoku Ricciego z
   wypełnieniem Dehna na brzegu po przyczepieniu czterowymiarowego
   uchwytu $2$. Osobno wskazano przeszkodę przecięć dysków Whitneya
   i hipotezy topologicznego twierdzenia o zanurzaniu dysków.
   Nie powielono geometrii Thurstona ani dowodu Perelmana.

## Pokrycie audytem

Wpisy o sprawdzeniu pochodzą z dziennika wskazanych iteracji. Deklaracje
współautora (w szczególności o chirurgii, sferach Milnora, wymiarze 4
i dodatku C) są zachowane, ale pobranie commitów **nie jest ponownym
niezależnym audytem**. Zmiany po dacie danego przeglądu wymagają kontroli
różnic. Dawne liczby stron dotyczą wyłącznie historycznych składów.
Poprzedni audyt 18-rozdziałowej wersji `a36c920` nie zastępuje tej tabeli.

| Numer i temat | Plik w `tex/rozdzialy/` | Stan przeglądu | Kontrola / pozostały zakres |
|---|---|---|---|
| 1. Rozmaitości | `01-rozmaitosci.tex` | 13 października zakończono audyt dodatków o wiązkach wektorowych i kostycznych; 14 października ponownie sprawdzono §1.10; 18–19 października sprawdzono intuicję podrozmaitości i różniczkę w §1.11; 20 października uzupełniono §1.12 o przestrzeń styczną podrozmaitości, przykład i rysunek oraz o wzór z wektorami normalnymi | Skontrolowano sklejanie wiązek, funkcje przejścia, sekcje, sumę i wiązkę dualną, przykład Möbiusa, rachunek różniczki, przykład injektywnej immersji o gęstym obrazie, atlasy `TM` i `T*M`, diagramy oraz odsyłacze. W §1.11 połączono wcześniejszy wzór z §1.8 z różniczką odwzorowania, wyprowadzono macierz Jacobiego z działania na lokalne współrzędne i objaśniono utożsamienie $T_{f(p)}\R\cong\R$ przez funkcję $t$. Lokalność derywacji uzasadnia użycie współrzędnych na otoczeniu. Nowy wynik opisuje przestrzeń styczną podrozmaitości jako obraz różniczki inkluzji, z dowodem przez współrzędne wycinające i krzywe; towarzyszą mu przykład okręgu i rysunek. Wzór ogólny opisuje styczność przez jądra różniczek i prostopadłość do gradientów lokalnych równań. Ta iteracja nie stanowi ponownego audytu całego rozdziału. |
| 2. Pola wektorowe | `02-pola-wektorowe.tex` | Audyt dodatków zakończono 6 października; §2.1 ponownie przejrzano 18–21 października; 22 października uzupełniono §2.2 oraz dowód Twierdzenia 2.3.2 | W §2.1 sprawdzono pola jako derywacje, przykłady na okręgu i sferze oraz pole wzdłuż odwzorowania. W §2.2 doprecyzowano nawias Liego i kryterium Frobeniusa. W §2.3 rozpisano przeniesienie równania do mapy, zakres czasów operatora Picarda oraz etapy dowodu gładkiej zależności. Nie przeprowadzono ponownego audytu całego rozdziału. |
| 3. Algebra tensorowa | `03-algebra-tensorowa.tex` | Audyt z 6 października; notacja poprawiona 9 października | Formalne generatory par zapisano jako [(v,w)]; zakres tej poprawki nie obejmuje ponownego audytu całego rozdziału. |
| 4. Grassmanniany, Clifford i spinory | `04-grassmanniany-clifford-spinory.tex` | Wcześniejszy audyt z 6 października; 8 października dodano grupę Pin | Sprawdzono nakrycie $\operatorname{Pin}(n)\to O(n)$ i stronę 100 PDF |
| 5. Algebra abstrakcyjna | `05-algebra-abstrakcyjna.tex` | Audyt i poprawki w `dbfe600`; porównano późniejsze różnice do `2777149` | Zachowano wprowadzone przez autora nienumerowane podsekcje i nazewnictwo iloczynu tensorowego; poprawiono „Iloczn”. Dowody dziedziny, ciała ułamków i lokalizacji zachowane. Opcjonalne definicje są w rejestrze poniżej. |
| 6. Algebra homologiczna | `06-algebra-homologiczna.tex` | Audyt dodatków zakończony 6 października; PDF 387 stron | Zachowana kompletność po przeniesieniu, przywrócone założenie o R i związek redukcji modulo m z tensorem |
| 7. Homotopia, nakrycia i CW | `07-homotopia-nakrycia-cw.tex` | Wcześniejszy audyt z 6 października; 8 października dodano minimalną teorię grafów | Drzewo, las, korzeń, liść i rachunek krawędzi sprawdzone na stronie 151 PDF |
| 8. Homologia przestrzeni | `08-homologia.tex` | Audyt dodatków zakończony 6 października; treść bez poprawek | Sprawdzone pięć wpisów indeksu, definicje, bibliografia i trzy ilustracje; PDF 397 stron |
| 9. Wyższe grupy homotopii | `09-wyzsze-grupy-homotopii.tex` | Audyt dodatków zakończony 6 października; PDF 397 stron | Sprawdzone indeks, definicje i cztery rysunki; poprawiono 19 użyć słowa „mapa” na „odwzorowanie” |
| 10. Formy i de Rham | `10-formy-de-rham.tex` | Audyt dodatków zakończony 6 października; bez poprawek treści | Siedem wpisów indeksu, pięć ilustracji i zgodność konwencji przy brzegu; PDF 397 stron |
| 11. Metryka, długość i miara | `11-metryka-dlugosc-miara.tex` | Audyt dodatków zakończony 6 października; PDF 397 stron | Sprawdzone definicje i dwie ilustracje; usunięty powtórzony wpis indeksu |
| 12. Koneksje i transport | `12-koneksje.tex` | Audyt dodatków zakończony 6 października; bez poprawek treści | Cztery wpisy indeksu, definicje i dwa rysunki sprawdzone; PDF 397 stron |
| 13. Geodezyjne i zupełność | `13-geodezyjne.tex` | Audyt dodatków zakończony 6 października; 13 października dodano miejsce cięcia i promień injektywności | Definicje, dowód związku z czasem cięcia, alternatywa dla miejsca cięcia, pełne rachunki sfery i płaskiego torusa oraz dwa nowe rysunki sprawdzone w tomie II (180 stron) |
| 14. Krzywizna | `14-krzywizna.tex` | Audyt dodatków zakończony 6 października; 13 października dodano holonomię i rozkład de Rhama oraz powiązano §14.9 z miejscem cięcia w §13.6 | Grupa holonomii, zasada pól równoległych, pełny dowód lokalnego iloczynu, przykłady i dwa rysunki; globalny krok de Rhama oraz Ambrose–Singer są jawnymi wynikami zewnętrznymi. Powiązanie sprzężenia, alternatywy w miejscu cięcia i promienia injektywności sprawdzone. |
| 15. Grupy Liego | `29-grupy-liego.tex` | Pełny audyt zakończony 20 października | Sprawdzono przykłady, nawias, eksponentę, działanie adjungowane i nakrycie $\mathrm{SU}(2)\to\mathrm{SO}(3)$; doprecyzowano torus i oszacowanie pochodnych szeregu. |
| 16. Geometria Kleina (plik 29a) | `29a-geometria-kleina.tex` | Pełny audyt zakończony 20 października | Sprawdzono uśrednianie, właściwość działania na $G/H$, zupełność, ilorazy dyskretne, orbifoldy i modele Kleina; zawężono deklarację o izometriach hiperbolicznych do dowiedzionego działania $\mathrm{PSL}(2,\R)$. |
| 17. Chern–Weil | `27-chern-weil.tex` | Pełny audyt zakończony 20 października | Sprawdzono normalizacje i transgresję; rozpisano model względny klasy Eulera, granicę wokół zer i wersję brzegową. Zgodność zespolonej formy Cherna z całkowitą klasą pozostaje jawnym wejściem zewnętrznym. |
| 18. Hodge–Bochner | `28-hodge-bochner.tex` | Pełny audyt zakończony 20 października | Sprawdzono wejście analityczne, znaki Weitzenböcka i Bochnera oraz rozkład sygnatury; dopisano zakres stopni i przykład $S^2\times S^2$. |
| 19. Sard i transwersalność | `15-sard-transwersalnosc.tex` | Audyt dodatków zakończony 6 października; bez poprawek treści | Pięć wpisów indeksu, cztery ilustracje i warunki transwersalności przy brzegu sprawdzone; PDF 401 stron |
| 20. Zanurzenia i otoczenia | `16-zanurzenia-otoczenia.tex` | Audyt dodatków zakończony 6 października; PDF 401 stron | Sześć haseł indeksu, cztery ilustracje i kołnierze sprawdzone; poprawiono terminologię odwzorowań oraz zdanie o homotopii do odwzorowania stałego |
| 21. Przecięcia, dualność i klasy | `17-przeciecia-dualnosc-klasy.tex` | Audyt dodatków zakończony 6 października | Sprawdzone indeks, konwencje znaków i cztery ilustracje; ujednolicono terminologię i rozwinięto argument Leraya–Hirscha dla wiązki rzutowej |
| 22. Teoria Morse'a | `18-morse.tex` | Audyt dodatków zakończony 8 października | Sprawdzone definicje i pięć ilustracji; jawne współrzędne krytyczne torusa, dokładne prowadnice podpisów i poprawiona terminologia |
| 23. Kobordyzmy i uchwyty | `19-kobordyzmy-uchwyty.tex` | Audyt dodatków zakończony 8 października; PDF 443 strony | Sprawdzone trzy hasła i pięć ilustracji; przywrócony warunek orientacji w podpisie, jawny opis sklejenia pierścieni i rozwinięty lokalny ruch Whitneya przy zachowanych założeniach o dyskach |
| 24. h-kobordyzm | `20-h-kobordyzm.tex` | Audyt i uzupełnienia zakończone 9 października; skład po scaleniu do `2777149`: 503 strony | Rozpisano wymianę 1→3, dopełnienia w kowymiarze 2, wstęgi i homologię wyciętej sfery. Dokładne założenia obramowanego lematu Whitneya podano jako jawny wynik zewnętrzny. Trzy rysunki, odsyłacze i indeks sprawdzone. |
| 25. Torsja i s-kobordyzm | `21-torsja-s-kobordyzm.tex` | Pełny audyt i uzupełnienia zakończone 11 października; PDF 505 stron | Poprawiono bazy i konwencje macierzowe, dowód niezależności kontrakcji, zakres lematu Whitneya, obramowania i dualność w realizacji torsji. Strony 390–401, oba schematy, odsyłacze i indeks sprawdzone; głębokie wejścia zewnętrzne wskazano dokładnie. |
| 26. Chirurgia geometryczna | `22-chirurgia-geometryczna.tex` | Pełny audyt zakończony 8 października; 27 października osobno sprawdzono przykład śladu $S^6\to S^3\times S^3$; 28 października dodano dwa wizualne przykłady uchwytów | Wcześniej sprawdzono obramowania, ślad i uchwyt dualny, homologię, $\pi_1$, formę jądra i rysunki. Przykład śladu wskazuje indeksy uchwytów i standardowe dane normalne. Pierwszy nowy rysunek pokazuje $S^2\sqcup S^2\to S^2\to T^2$, wybór dysków, $b_0$, $\chi$ i orientowalność, z odsyłaczem do wcześniejszej wersji jednej sfery. Drugi pokazuje cięcie, pełny skręt i sklejenie pierwotnych par końców dwóch uchwytów sfery; wynik nadal ma rodzaj dwa. Nie ponawiano audytu reszty rozdziału. |
| 27. Przeszkoda chirurgiczna | `23-przeszkoda-chirurgiczna.tex` | Pełny audyt także nowego tekstu zakończony 20 października względem §§1–2, 5–6 Walla; zmianę z 27 października sprawdzono osobno | Sprawdzono parzyste i nieparzyste kryterium, bazy i torsję nad $\Z[\pi]$, $SU/RU$, ruchy $T1$--$T4$, wymiar pięć i chirurgię środkową. Poprawiono stronę $\lambda$ w dualności, terminologię immersji i hipotezy lematu 5.7. Doprecyzowano zależność $\mu=0$ od wybranych danych normalnych w przykładzie lokalnej stabilizacji; nie ponawiano audytu reszty rozdziału. Głębokie lematy Walla, wersja $h$ i relacja formacji pozostają jawnymi wynikami zewnętrznymi. |
| 28. Ciąg chirurgii | `24-ciag-chirurgii.tex` | Pełny audyt wcześniejszej treści zakończony 20 października względem §10 oraz twierdzeń 5.8 i 6.5 Walla; uzupełnienia z 27–28 października sprawdzono osobno | Sprawdzono dokładność, działanie $L_{n+1}^s$, zakres $n\geq5$, lewą strzałkę i przejście do $s$-kobordyzmu; doprecyzowano racjonalne jądro w rachunku sygnatury. Nowe fragmenty objaśniają strzałki, ślad nad cylindrem, warunek brzegowy, przykład $S^7$, przejście śladu $S^6\to S^3\times S^3$ przez Arfa i punkt bazowy $[S^6,G/O]$. Mapa hipotez rozdziela DIFF/TOP, $n=5$ od śladu wymiaru sześć, dowolność $\pi_1$, ustalony brzeg i dekoracje $s/h$; nie ponawiano audytu reszty rozdziału. Bijekcja z $[X,G/O]$ i działanie grupy $L$ pozostają wynikami Walla, a wariant TOP jest osobnym wynikiem zewnętrznym. |
| 29. Poincaré | `25-poincare.tex` | Pełny audyt rozdziału zakończony 20 października; twierdzenia 2.2 i 2.3 Bardena porównano z oryginałem | Wymiar 2, osobno 5 i wyższe; homeomorfizm a dyfeomorfizm; lematy 3.1 i 4.1–4.4, indukcja, modele $M_k,X_j$, formy wiązania i przykłady spin/niespin. Doprecyzowano źródło triangulacji, mieszaną parę torsyjną, hipotezy lematu 4.4 i orientację przy wniosku pięciowymiarowym. Głębokie wejścia pozostają zewnętrzne. |
| 30. Sfery Milnora | `26-sfery-milnora.tex` | Audyt wcześniejszej treści zakończony 19 października; klasyfikację dopisano 20 października | Sprawdzono sklejanie, klasy $e,p_1$, ciąg Mayera--Vietorisa, kryterium Whiteheada, obie sygnatury, $\lambda$, $\mu$, przykłady i rysunek. Nowy rachunek klasyfikuje 16 typów wiązkowych oraz 28 klas $\Theta_7$ (15 bez orientacji) przez sumy $M_3$. Zupełność $\mu$, $\Theta_7\cong\Z/28$, wzór Hirzebrucha i indeks Diraca pozostają jawnymi wejściami zewnętrznymi. |
| 31. Potok Ricciego (plik 30) | `30-potok-ricciego.tex` | Pełny audyt zakończony 20 października; rysunek 31.1 sprawdzony na stronie PDF 100 | Rachunki skalowania, ewolucji, zasady maksimum i DeTurcka spójne; istnienie i jednoznaczność PDE pozostają jawnym wejściem analitycznym. |
| 32. Poincaré w wymiarze trzy (plik 30a) | `30a-poincare-trzy.tex` | Pełny audyt zakończony 20 października | Hipotezy niezapadania i wygasania, chirurgia, odtworzenie topologii oraz Moise sprawdzone względem źródeł; poprawiono tytuł cytowanej pracy i terminologię. Głębokie wyniki Perelmana pozostają zewnętrzne. |
| 33. Geometrie Thurstona (plik 30b) | `30b-geometrizacja-thurstona.tex` | Pełny audyt zakończony 20 października | Osiem modeli, tabela Seiferta, orbifoldy, rozkład pierwszy i JSJ sprawdzone; dopisano definicję dysku ściskającego i źródło twierdzenia o pętli oraz skorygowano opis dowodu w rozdziale 31. Geometryzacja pozostaje wynikiem zewnętrznym. |
| 34. Formy przecięcia i uchwyty w wymiarze cztery (plik 31) | `31-freedman-formy-przeciecia.tex` | Pełny audyt rozdziału zakończony 25 października; 28 października dodano osobno diagram obramowanych splotów | W audycie sprawdzono definicję i unimodularność formy, parzystość, sygnaturę, pełny rachunek $E_8$, macierz splotu, homologię brzegu i ograniczenie triku Whitneya. Dopisano jawny rachunek $2E_8$, rozróżnienie od macierzy skalarnej $2\cdot E_8$, wpływ orientacji komponentów na macierz oraz granicę między korpusem uchwytowym a zamkniętą rozmaitością. Nowy rysunek odczytuje macierze $H$ i $[1]$ z obramowanego splotu Hopfa i niewęzła; nie ponowiono audytu całego rozdziału. Głębokie domknięcie topologiczne pozostaje wynikiem zewnętrznym Freedmana. |
| 35. Uchwyty Cassona (plik 32) | `32-uchwyty-cassona.tex` | Pełny audyt rozdziału zakończony 26 października | Sprawdzono model uchwytu z załamaniami, rachunek $\pi_1$ pięter, rozróżnienie $\mu$ i $\widetilde\mu$, hipotezy oraz konkluzje twierdzeń Freedmana--Quinna i Powell--Raya--Teichnera, geometryczną dualność i $\pi_1$-pomijalność. Poprawiono numerację wyników i opis zakresu grup. Powierzchnie z dyskami zamykającymi, uogólnione wieże, twierdzenie o zanurzaniu oraz standardowość uchwytu Cassona pozostają jawnymi wynikami zewnętrznymi. |
| 36. Klasyfikacja Freedmana (plik 33) | `33-freedman-klasyfikacja.tex` | Pełny audyt zakończony 27 października; 28 października dodano osobno schemat zależności i tabelę przykładów | W audycie sprawdzono klasyfikację TOP, wzór $\operatorname{ks}\equiv\sigma/8$, zakres twierdzenia o zanurzaniu sfer, rachunek $\pi_1$ chirurgii, wniosek Poincarégo i przykłady $H$, $[1]$, $E_8$, $2E_8$. Nowy schemat porządkuje drogę od dysków i wież Cassona do klasyfikacji w przypadku $\pi_1=1$, a tabela zestawia parzystość, sygnaturę, $\operatorname{ks}$ i istnienie wygładzenia, w tym oba typy o formie $[1]$; nie ponowiono audytu całego rozdziału. Rozróżnienie oryginalnego twierdzenia Freedmana od pełnej wersji Freedmana--Quinna zachowano; klasyfikacja, zanurzanie i topologiczny $s$-kobordyzm pozostają zewnętrzne. |
| 37. Donaldson (plik 34) | `34-donaldson.tex` | Pełny audyt wcześniejszej treści zakończony 27 października; uzupełnienie i jego skład sprawdzono 28 października | W audycie sprawdzono lokalność trywializacji, ASD, całkowity $c_1$, znaki $c_2$ i energii, orientację w źródłowym dowodzie oraz wnioski $E_8$ i $2E_8$. Nowy przykład BPST oblicza krzywiznę, energię $8\pi^2$, $c_2=1$ i gładkie przedłużenie na $S^4$. Mapa wejść podaje operator deformacji, indeks $5$, regularność, punkty redukowalne, koncentrację krzywizny, zwartość Uhlenbeck i kołnierz Taubesa--Donaldsona. W rachunku sygnatury poprawiono wniosek na $n(Q_X)\geq b_2(X)$, a przeciwną nierówność wyprowadzono algebraicznie. Konstrukcja i analiza przestrzeni moduli oraz twierdzenie Donaldsona pozostają zewnętrzne; nie ponawiano audytu całego rozdziału. |
| 38. Egzotyczne $\R^4$ (plik 35) | `35-egzotyczne-r4.tex` | Pełny audyt wcześniejszej treści zakończony 27 października; uzupełnienie i jego skład sprawdzono 28 października | W audycie sprawdzono obie przeszkody Gompfa, lematy 1.1–1.2, rachunek dopełnienia charakterystycznego wektora i indukcję ze zwartymi świadkami. Nowy opis małej rodziny rozdziela topologiczny promień, wspólny zwarty rdzeń $K$, zewnętrzną analizę końców okresowych i przeliczalność klas izotopii osadzeń $K$. Diagram zestawia tę drogę z dużą rodziną Gompfa oraz zachowuje warunki orientacji i ogolenia. Twierdzenia o uchwytach Cassona, wyniki Freedmana, Gompfa oraz De Michelisa–Freedmana pozostają zewnętrzne; nie ponawiano audytu całego rozdziału. |
| Podział źródeł i importy | — | Zakończono, `9148128` | Kontrola regresji przy dalszych zmianach |
| Dodatek A o wynikach zewnętrznych | — | Pełny niezależny audyt zakończono 25 października | Skorygowano zakres Walla do $n\geq5$ i rozdzielono kryterium od twierdzeń realizacyjnych. Uzupełniono wersję $h$, Rothenberga, ciąg chirurgii, Whiteheada, miarę Hausdorffa i Haara, Ambrose'a--Singera, globalny de Rham, normalizację Cherna--Weila, wejścia Bardena, Eellsa--Kuipera, Kervaire'a--Milnora i Quinna. Doprecyzowano hipotezy w wymiarach 3 i 4; źródła oraz strony 149–154 sprawdzono. |
| Dodatek B: homologia singularna i Euler | — | Pełny niezależny audyt zakończono 25 października | Rachunki są poprawne. Nazwano użyty homeomorfizm, uzasadniono skończony model CW kobordyzmu z rozkładu uchwytowego i dodano konsekwencję dualności Poincarégo $\chi(M)=0$ w nieparzystym wymiarze. Odsyłacze do rozdziałów 8, 21 i 23 oraz strony 155–158 sprawdzono. |
| Dodatek C: grupy macierzowe | — | Definicje, algebry i wymiary sprawdzone 8 października; tabela czytelna w PDF | Przy dalszej rozbudowie zachować rozróżnienie wymiaru rzeczywistego i zespolonego oraz $Sp(n)$ od $Sp(2n,\mathbb K)$ |
| Końcowa kontrola całości | — | Częściowo: ujednolicono „Dalszą lekturę” i sprawdzono odsyłacze do źródeł | Mapa książki, oznaczenia, terminologia i pełny przegląd treści nadal wymagają osobnej kontroli; skład, indeks i PDF sprawdzane przy każdym etapie. |

## Rejestr pojęć do decyzji autora

Pierwsza partia z 9 października: lektura rozdziału 5 oraz wskazanych
fragmentów geometrii Kleina i Thurstona, z wyszukaniem wyjaśnień w całym
źródle. To **nie jest jeszcze kompletny audyt słownika wszystkich 38
rozdziałów**. Rejestr uzupełniamy podczas kolejnych przeglądów.
Poniższych opcjonalnych rozszerzeń nie dopisano automatycznie.
W przeglądzie rozdziału 25 z 11 października uzupełniono potrzebne
na miejscu objaśnienia wolnej ściany i zwinięcia CW, homologicznego
stożka odwzorowania oraz charakteru orientacji. Twierdzenia o prostej
homotopii i porównaniu triangulacji z rozkładem Morse'a mają dokładne
źródła i pozostają jawnie zewnętrzne; nie dopisujemy ich ponownie
jako brakujących definicji.

| Pojęcie i miejsce | Czego brakuje | Możliwe uzupełnienie |
|---|---|---|
| Monoid — plik 05, między `def:free-groups-5` a `prop:free-reduction-5` | Nazwa występuje raz, bez definicji; przykład słów jest już podany. | Jedno zdanie: łączne działanie z jedynką, bez wymogu odwrotności; odnieść do konkatenacji. |
| Pierścień główny — plik 05, uwaga po `prop:ranga-ilorazu` | Brak definicji i twierdzenia o strukturze. Założenie skończonego generowania poprawiono we wcześniejszym audycie. | Zdefiniować jako dziedzinę, w której każdy ideał jest główny; podać Z i K[t]. Pełne twierdzenie strukturalne wymaga osobnego dowodu lub jawnego źródła. |
| Indeks podgrupy i „wirtualnie” — plik 30b, przykłady geometrii euklidesowej, hiperbolicznej i Sol | Zdefiniowano warstwy, lecz nie ich liczbę jako indeks ani własność posiadaną przez podgrupę skończonego indeksu. | Definicja indeksu i własności wirtualnej, przykład grupy zawierającej Zⁿ ze skończonym indeksem. |
| Grupa nilpotentna i rozwiązalna — plik 30b, modele Nil i Sol | Nazwy są użyte do porównania grup, bez szeregów centralnego i pochodnego. | Krótki blok algebraiczny z komutatorami; obliczyć te szeregi dla podanych grup zamiast tylko dopisywać nazwy. |
| Ostrzyk hiperboliczny — plik 30b, przykład H³ | Jest informacja o torusowym przekroju, bez modelu metryki końca. | Model ilorazu horokuli i krótki rachunek skończonej objętości; odróżnić torusowy przekrój od całego końca. |
| Wypełnienie Dehna — plik 30b, przykład H³ | Jest odwołanie do twierdzenia, ale bez definicji operacji i nachylenia na torusie. | Opisać doklejenie pełnego torusa i meridian; powiązać z istniejącą chirurgią, a hiperboliczne twierdzenie pozostawić z dokładnym źródłem. |

**Już obecne albo uzupełnione:** grupa wolna i iloczyn wolny mają konstrukcje,
postać normalną i własności uniwersalne w rozdziale 5. Dziedzinę całkowitości,
ciało ułamków i działanie skalarów na lokalizacji uzupełniono 9 października.
Geometria Kleina ma definicję `def:klein-geometria` w pliku 29a oraz przykłady.
Geometria modelowa ma `def:thurston-model` w pliku 30b; zaraz potem zdefiniowano
rozmaitość geometryczną, także w wersji niezamkniętej; w pliku 29a
podano miarę Haara jako wynik zewnętrzny oraz dowód uśredniania
i konstrukcji gładkiego ilorazu. Dalej podano osiem modeli i ilorazy.
Potrzebny jest audyt ich pozostałych założeń i wyjaśnień, bez drugiej
konkurencyjnej definicji.

## Dalsze rozszerzenia i granice dowodów

- Pełne triangulacje, porównanie kohomologii Čecha i singularnej oraz
  dalsze grupy sfer homotopijnych są większymi możliwymi rozszerzeniami,
  nie krótkimi naprawami obecnych dowodów.
- Dawna warunkowa propozycja dowodów Brouwera i niezmienniczości obszaru
  pozostaje odłożona do sprawdzenia homologii lokalnej i potrzebnych
  narzędzi. Nie dopisywać pozornie pełnego dowodu z ukrytym wejściem.
- Głębokie wyniki Walla, Bardena, Hirzebrucha, Perelmana, Freedmana,
  Donaldsona i Gompfa oraz analityczne twierdzenia o PDE pozostają
  jawnymi wejściami z dokładnymi założeniami i źródłami. Kontrola ich
  zastosowania nie jest dowodem tych twierdzeń. W chirurgii sprawdzić
  również realizację obramowanych immersji, prostą dualność i bazowość
  oraz przygotowanie kobordyzmu.

Źródła i szczegółowe deklaracje wykonania zachowuje [PRZEGLAD.md](PRZEGLAD.md)
oraz bibliografia odpowiednich rozdziałów. Pozostałe propozycje
oceniać na podstawie rzeczywistych braków stwierdzonych w audycie.
