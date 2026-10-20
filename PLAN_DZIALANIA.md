# Aktualny plan i pokrycie przeglądem

Stan: 20 października 2026. Gałąź: `review/rozdzialy-matematyka`.
Książka ma **38 rozdziałów, pięć części i trzy dodatki**. Numery w nazwach
plików są historyczne; numer w PDF ustala kolejność importów.
Skład roboczy podzielono na trzy tomy: rozdziały 1–10, 11–22 oraz
23–38 z dodatkami. Plik zbiorczy pozostaje dostępny do okazjonalnego składu.

To jedyna bieżąca lista zadań i propozycji. Uzasadnienia zmian oraz wyniki
sprawdzania konkretnych wersji są w [PRZEGLAD.md](PRZEGLAD.md), a budowanie
i organizacja plików w [README.md](README.md).

## Bieżący zakres i kolejność

1. Doprowadzić wykład wymiarów co najmniej pięć do pełnego dowodu
   twierdzenia Walla o przeszkodzie chirurgicznej (rozdziały 27–28).
   Rozpisano wersję $s$ w przypadkach parzystym $n\geq6$ i
   nieparzystym $n\geq5$, wraz z bazami nad $\Z[\pi]$,
   formacjami i ciągiem chirurgii. Krok geometryczny lematu 5.5
   oraz rozłączność obramowanych sfer w przypadku nieparzystym
   wyprowadzono z twierdzenia 1.1 Walla. Lokalny rachunek ruchu $T1$
   wyprowadzono z rozkładu dysku i ciągu Mayera--Vietorisa, a dla ruchów
   $T2$--$T4$ rozpisano zmianę bazy hiperbolicznej. Wyprowadzono też lokalny
   efekt pojedynczej chirurgii na środkowej sferze; pozostałe głębokie lematy
   geometryczne nadal są jawnymi wejściami zewnętrznymi. Wersję $h$ i ciąg
   Rothenberga wskazano osobno jako wyniki zewnętrzne. Przed oznaczeniem
   dowodu jako samodzielnie pełnego trzeba je wyprowadzić i przeprowadzić
   końcowy audyt nowego tekstu.
   W rozdziale 29 rozpisano oba twierdzenia Bardena (2.2 i 2.3)
   wraz z ich modelami oraz jawnie wskazanymi wynikami wejściowymi;
   kontrola twierdzeń 2.2 i 2.3 ze źródłem oraz składu trzech tomów
   jest zakończona, pełny audyt całego
   rozdziału pozostaje w kolejce. Audyt sfer Milnora
   (rozdział 30) zakończono 19 października. Twierdzenia
   czterowymiarowe (rozdziały 34–38) kontynuować według
   zakresu poniżej; wymiary cztery pozostają
   wykładem informacyjnym. Zwykła iteracja obejmuje jeden rozdział,
   chyba że etap wymaga wspólnego dowodu. Wcześniejszy audyt
   każdego z tych rozdziałów pozostaje ważny w swoim wskazanym zakresie,
   ale nie oznacza wykonania nowej rozbudowy.
2. Dokończyć audyt według numeracji PDF: najbliższy niezweryfikowany
   rozdział to 29. Rozdziały 26–28 mają wcześniejsze przeglądy,
   a rozdział 30 pełny audyt z 19 października;
   rozdziały 31–33 wymagają pełnych audytów lub kontroli nowych rysunków
   i zależności. Dalej sprawdzić zaległe części rozdziałów 15–18
   oraz dodatki A i B według tabeli. Rozdział 1 z nowymi wiązkami
   sprawdzono 13 października; §1.10 ponownie skontrolowano 14 października.
3. Przed każdą iteracją pobierać zmiany współautora. Zmieniać źródło
   w odpowiednim pliku rozdziału, zapisywać uzasadnienia w
   `PRZEGLAD.md`, składać odpowiedni tom i sprawdzać zmienione strony.
   Przed wypchnięciem uruchamiać `buduj_tomy.ps1`, kontrolować indeksy
   i odsyłacze między tomami, aktualizować PDF-y tomów, zatwierdzać
   i wypychać ukończony etap. Skład zbiorczy jest okazjonalny.

Nie dodajemy zadań. Rozmaitości z brzegiem, grupy wolne, iloczyny wolne,
geometria Kleina i geometrie Thurstona już są w źródłach; nie tworzymy ich
duplikatów. Freedman, Donaldson i egzotyczne R⁴ pozostają w tomie III,
w osobnych rozdziałach.

## Zlecone rozbudowy dowodów

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
   i źródłem. Przed oznaczeniem całości jako samodzielnie pełnego
   dowodu pozostaje wyprowadzenie tych lematów i końcowy audyt;
   porównanie dekoracji $s/h$ pozostaje osobnym wynikiem zewnętrznym.
2. **Klasyfikacja Bardena — rozdział 29.** Rozpisano twierdzenie 2.2
   o realizacji zadanego izomorfizmu $H_2$ oraz twierdzenie 2.3
   o kanonicznych modelach i pełności $(H_2,\iota)$. Dowody obejmują
   ograniczenia algebraiczne, kobordyzm, chirurgię na $\pi_1$ i $H_2$,
   lematy 4.1–4.4, indukcję, sześciowymiarowy $h$-kobordyzm,
   konstrukcje modeli oraz porównanie spin/niespin. Jawne wejścia
   zewnętrzne to wyniki Thoma, Nowikowa, Walla, Whiteheada,
   Haefligera, Milnora i Smale'a. Skład i odsyłacze między tomami
   sprawdzono; pełny audyt całego rozdziału pozostaje otwarty.
3. **Sfery Milnora — rozdział 30: etap ukończony.**
   Rozpisano konstrukcję wiązek, klasy charakterystyczne,
   homologię i typ homotopijny ich sfer jednostkowych.
   Niezmiennik Milnora uzupełniono o spinowy niezmiennik
   Eellsa--Kuipera i przykłady rozróżniające struktury gładkie
   także bez wyboru orientacji. Twierdzenie Hirzebrucha,
   całkowitość indeksu Diraca i wysokowymiarowe twierdzenie
   Poincarégo pozostają jawnymi wejściami zewnętrznymi.
   Audyt całego rozdziału, w tym rysunku i zależności
   między twierdzeniami, zakończono 19 października.
4. **Twierdzenia wymiaru cztery — rozdziały 34–38.**
   Po ukończeniu głównych dowodów dla wymiarów co najmniej pięć
   utrzymać wykład informacyjny z dokładnymi hipotezami i źródłami.
   Rozbudować kolejno rachunek form przecięcia i obramowań
   (w tym E₈ i 2E₈), geometryczne przygotowanie do twierdzenia
   o zanurzaniu dysku i roli uchwytów Cassona, konsekwencje
   klasyfikacji Freedmana, przeszkodę Donaldsona dla form
   określonych oraz konstrukcje egzotycznych R⁴. Dla każdego
   twierdzenia podać kategorię topologiczną lub gładką,
   warunki dotyczące grupy podstawowej i brzegu, zależności
   logiczne, obliczalny przykład i zakres dowodu. Analizę
   przestrzeni moduli, twierdzenie o zanurzaniu dysku oraz
   klasyfikację pozostawiać nazwanymi wejściami, dopóki
   ich wymagane lematy nie zostaną rzeczywiście wyprowadzone.

## Pokrycie audytem

Wpisy o sprawdzeniu pochodzą z dziennika wskazanych iteracji. Deklaracje
współautora (w szczególności o chirurgii, sferach Milnora, wymiarze 4
i dodatku C) są zachowane, ale pobranie commitów **nie jest ponownym
niezależnym audytem**. Zmiany po dacie danego przeglądu wymagają kontroli
różnic. Dawne liczby stron dotyczą wyłącznie historycznych składów.
Poprzedni audyt 18-rozdziałowej wersji `a36c920` nie zastępuje tej tabeli.

| Numer i temat | Plik w `tex/rozdzialy/` | Stan przeglądu | Kontrola / pozostały zakres |
|---|---|---|---|
| 1. Rozmaitości | `01-rozmaitosci.tex` | 13 października zakończono audyt dodatków o wiązkach wektorowych i kostycznych; 14 października ponownie sprawdzono §1.10; 18–19 października sprawdzono intuicję podrozmaitości i różniczkę w §1.11 | Skontrolowano sklejanie wiązek, funkcje przejścia, sekcje, sumę i wiązkę dualną, przykład Möbiusa, rachunek różniczki, przykład injektywnej immersji o gęstym obrazie, atlasy `TM` i `T*M`, diagramy oraz odsyłacze. W §1.11 połączono wcześniejszy wzór z §1.8 z różniczką odwzorowania, wyprowadzono macierz Jacobiego z działania na lokalne współrzędne i objaśniono utożsamienie $T_{f(p)}\R\cong\R$ przez funkcję $t$. Lokalność derywacji uzasadnia użycie współrzędnych na otoczeniu. |
| 2. Pola wektorowe | `02-pola-wektorowe.tex` | Audyt dodatków zakończony 6 października; §2.1 ponownie przejrzano 18 października | Sprawdzono konstrukcje $X\mapsto D_X$ i $D\mapsto X$, dowód gładkości, rozróżnienie przestrzeni stycznych w przykładzie okręgu i pole wzdłuż odwzorowania. Wcześniej sprawdzono powiązanie z brzegiem, przykład przepływu jednostronnego, bibliografię i rysunki. Pozostałe sekcje rozdziału nie były przedmiotem bieżącej iteracji. |
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
| 15. Grupy Liego | `29-grupy-liego.tex` | Sprawdzono nakrycie kwaternionowe 7 października; pełny audyt całości czeka | Przykłady, nawias, eksponenta, działanie adjungowane i jawne nakrycie $\mathrm{SU}(2)\to\mathrm{SO}(3)$; później sprawdzić zastosowania w Chernie–Weilu i wymiarze cztery |
| 16. Geometria Kleina (plik 29a) | `29a-geometria-kleina.tex` | Sekcję o ilorazach rozbudowano 11–12 października; audyt reszty oczekuje | Dowody uśredniania, właściwości działania na $G/H$, zupełności, ilorazu przez grupę dyskretną i lokalnego modelu orbifoldu; zgodność map orbifoldowych rozpisano przez homomorfizm grup, podniesienie i wspólne uszczegółowienie. Pozostałe modele Kleina wymagają osobnego przeglądu. |
| 17. Chern–Weil | `27-chern-weil.tex` | Oczekuje | Normalizacje i transgresja; uzasadnić model względnej kohomologii de Rhama przy identyfikacji klasy Eulera, granicę całek wokół zer i wersję brzegową |
| 18. Hodge–Bochner | `28-hodge-bochner.tex` | Sprawdzono kluczowe wzory 7 października; pełny audyt całości czeka | Jawne wejście analityczne; własne dowody wzoru Weitzenböcka, znikania Bochnera i rozkładu sygnatury; sprawdzić zgodność z przyszłą teorią czterowymiarową |
| 19. Sard i transwersalność | `15-sard-transwersalnosc.tex` | Audyt dodatków zakończony 6 października; bez poprawek treści | Pięć wpisów indeksu, cztery ilustracje i warunki transwersalności przy brzegu sprawdzone; PDF 401 stron |
| 20. Zanurzenia i otoczenia | `16-zanurzenia-otoczenia.tex` | Audyt dodatków zakończony 6 października; PDF 401 stron | Sześć haseł indeksu, cztery ilustracje i kołnierze sprawdzone; poprawiono terminologię odwzorowań oraz zdanie o homotopii do odwzorowania stałego |
| 21. Przecięcia, dualność i klasy | `17-przeciecia-dualnosc-klasy.tex` | Audyt dodatków zakończony 6 października | Sprawdzone indeks, konwencje znaków i cztery ilustracje; ujednolicono terminologię i rozwinięto argument Leraya–Hirscha dla wiązki rzutowej |
| 22. Teoria Morse'a | `18-morse.tex` | Audyt dodatków zakończony 8 października | Sprawdzone definicje i pięć ilustracji; jawne współrzędne krytyczne torusa, dokładne prowadnice podpisów i poprawiona terminologia |
| 23. Kobordyzmy i uchwyty | `19-kobordyzmy-uchwyty.tex` | Audyt dodatków zakończony 8 października; PDF 443 strony | Sprawdzone trzy hasła i pięć ilustracji; przywrócony warunek orientacji w podpisie, jawny opis sklejenia pierścieni i rozwinięty lokalny ruch Whitneya przy zachowanych założeniach o dyskach |
| 24. h-kobordyzm | `20-h-kobordyzm.tex` | Audyt i uzupełnienia zakończone 9 października; skład po scaleniu do `2777149`: 503 strony | Rozpisano wymianę 1→3, dopełnienia w kowymiarze 2, wstęgi i homologię wyciętej sfery. Dokładne założenia obramowanego lematu Whitneya podano jako jawny wynik zewnętrzny. Trzy rysunki, odsyłacze i indeks sprawdzone. |
| 25. Torsja i s-kobordyzm | `21-torsja-s-kobordyzm.tex` | Pełny audyt i uzupełnienia zakończone 11 października; PDF 505 stron | Poprawiono bazy i konwencje macierzowe, dowód niezależności kontrakcji, zakres lematu Whitneya, obramowania i dualność w realizacji torsji. Strony 390–401, oba schematy, odsyłacze i indeks sprawdzone; głębokie wejścia zewnętrzne wskazano dokładnie. |
| 26. Chirurgia geometryczna | `22-chirurgia-geometryczna.tex` | Pełny audyt zakończony 8 października; treść bez poprawek | Sprawdzone obramowania, ślad i uchwyt dualny, homologia, $\pi_1$, forma jądra i rysunki |
| 27. Przeszkoda chirurgiczna | `23-przeszkoda-chirurgiczna.tex` | Pełny audyt starszej treści zakończony 7 października; 14 października rozpisano oba przypadki $n\geq5$; 19 października wyprowadzono krok geometryczny lematu 5.5, rozłączne reprezentowanie generatorów i ruch $T1$ w wymiarze nieparzystym | Dodano rachunek baz i torsji nad $\Z[\pi]$, $SU/RU$, ruchy $T1$--$T4$, osobny wymiar pięć, dowód stabilizacji hiperbolicznej dla chirurgii na klasie zerowej, rozłączne sfery z ramami i drogami bazowymi, lokalny rachunek $\alpha\oplus\sigma$ oraz porównanie $L^s/L^h$ ciągiem Rothenberga. Twierdzenie 1.1 i pozostałe głębokie lematy Walla, twierdzenie dla dekoracji $h$ i relacja formacji pozostają jawnie zewnętrzne; samodzielny dowód i pełny audyt całego rozdziału pozostają otwarte. |
| 28. Ciąg chirurgii | `24-ciag-chirurgii.tex` | Pełny audyt starszej treści zakończony 8 października; próg $n\geq5$ sprawdzony 14 października | Uściślono naturę obu strzałek przeszkody, realizację przez twierdzenia 5.8 i 6.5 oraz przejście do $s$-kobordyzmu; bijekcja z $[X,G/O]$ i działanie grupy $L$ pozostają jawnymi wynikami Walla |
| 29. Poincaré | `25-poincare.tex` | Pełny audyt rozdziału oczekuje; twierdzenia 2.2 i 2.3 Bardena rozpisano 14 października i porównano z oryginałem 19 października | Wymiar 2, osobno 5 i wyższe; homeomorfizm a dyfeomorfizm; lematy 3.1 i 4.1–4.4, indukcja, modele $M_k,X_j$, formy wiązania i przykłady spin/niespin; skład trzech tomów i odsyłacze sprawdzone |
| 30. Sfery Milnora | `26-sfery-milnora.tex` | Pełny audyt rozdziału zakończony 19 października po uzupełnieniu niezmiennika Eellsa--Kuipera | Sprawdzono sklejanie, klasy $e,p_1$, ciąg Mayera--Vietorisa, kryterium Whiteheada, obie sygnatury, $\lambda$, $\mu$ i przykłady, rysunek oraz odsyłacze. Poprawiono terminologię i uzasadniono rozkład formy przecięcia po sklejeniu. Wzór Hirzebrucha i indeks Diraca pozostają jawnymi wejściami zewnętrznymi. |
| 31. Potok Ricciego (plik 30) | `30-potok-ricciego.tex` | Sprawdzono równania ewolucyjne i poprawkę DeTurcka 7 października; pełny audyt całości i nowego rysunku z `2777149` czeka | Ewolucja skalara i pola powierzchni, zasada maksimum, DeTurck; zgodność schematu deformacji z zakresem równań i podpisem. Istnienie i jednoznaczność PDE pozostają jawnym wejściem analitycznym. |
| 32. Poincaré w wymiarze trzy (plik 30a) | `30a-poincare-trzy.tex` | Dodano 8 października; niezależny audyt oczekuje | Dla głębokich twierdzeń Perelmana i Hamiltona zachować jawne hipotezy i źródła; sprawdzić topologiczny wniosek z wygaśnięcia oraz użycie twierdzenia Moise'a |
| 33. Geometrie Thurstona (plik 30b) | `30b-geometrizacja-thurstona.tex` | Rozbudowano sekcję 33.1 i orbifoldy bazy Seiferta 11–12 października; audyt reszty oczekuje | Warunki modelu, ilorazy, lokalna jednorodność i maksymalność; nienumerowane podsekcje 33.1, charakterystyka orbifoldowa, dobre i złe bazy oraz lokalny model Seiferta. Pełny audyt ośmiu modeli, rozkładu pierwszego, JSJ i założeń geometryzacji nadal oczekuje. |
| 34. Formy przecięcia i uchwyty w wymiarze cztery (plik 31) | `31-freedman-formy-przeciecia.tex` | Przegląd matematyczny 7 października; kontrola rysunku Whitneya 12 października | Rachunek $E_8$ i forma splotu sprawdzone wcześniej; poprawiono położenie punktu $q$ i płata na rysunku |
| 35. Uchwyty Cassona (plik 32) | `32-uchwyty-cassona.tex` | Przegląd skutków osadzania 7 października; kontrola terminologii 12 października | Immersje z punktami podwójnymi oddzielono od topologicznych zanurzeń; pełne osadzanie i standardowość uchwytu pozostają zewnętrzne |
| 36. Klasyfikacja Freedmana (plik 33) | `33-freedman-klasyfikacja.tex` | Przegląd 7 października; kontrola przejścia do sfer i przykładu $2E_8$ 12 października | Rozpisano warunek $\lambda=2\mu+e=0$ dla homotopii regularnej; klasyfikacja, chirurgia i niezmiennik Kirby'ego--Siebenmanna pozostają zewnętrzne |
| 37. Donaldson (plik 34) | `34-donaldson.tex` | Niezależny przegląd konwencji, przykładów i zastosowań 12 października | Sprawdzono znak $c_2$ oraz energii ASD, zakres diagonalizacji i przykład $2E_8$; analiza moduli i twierdzenie Donaldsona pozostają zewnętrzne |
| 38. Egzotyczne $\R^4$ (plik 35) | `35-egzotyczne-r4.tex` | Niezależny przegląd wejść i indukcji Gompfa 12 października; uzupełniono przebieg lematów 1.1 i 1.2 | Dowiedziono kierunku od dysków plastra do zanurzenia śladu, obliczono kratę $-E_8$ w rozmaitości otaczającej i rozpisano etapy wygładzania, wież Cassona oraz zastąpienia dysków. Pełne twierdzenia Quinna, Cassona, Freedmana i Gompfa oraz wynik De Michelisa–Freedmana pozostają zewnętrzne. |
| Podział źródeł i importy | — | Zakończono, `9148128` | Kontrola regresji przy dalszych zmianach |
| Dodatek A o wynikach zewnętrznych | — | Uzupełniany przez autora do 386ecb6; pełny niezależny audyt oczekuje | Zgodność katalogu z rzeczywistymi dowodami, zwłaszcza Walla, geometrii globalnej oraz wymiarów 3 i 4. |
| Dodatek B: homologia singularna i Euler | — | Dodany w `59fd235`; audyt oczekuje | Skończoność, przykłady i wzory Eulera; odsyłacze do homologii oraz przecięć i dualności (obecnie rozdziały 8 i 21). |
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
