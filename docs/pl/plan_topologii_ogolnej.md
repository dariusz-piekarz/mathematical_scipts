# Topologia ogólna — plan rozdziałów i audytów

Stan: 22 listopada 2026. Źródłem prawdy dla rozdziałów włączonych do książki jest `catalog/books.json`, a dla wyników kompilacji i testów: GitHub Actions na gałęzi `biblioteka-matematyczna-iteracja-6`.

## Zakres i kolejność

| Nr | Zakres | Stan |
| --- | --- | --- |
| 01 | Przestrzenie topologiczne | po audytach |
| 02 | Operacje topologiczne na zbiorach | po audytach |
| 03 | Odwzorowania ciągłe | po audytach |
| 04 | Konstrukcje przestrzeni topologicznych | po audytach |
| 05 | Aksjomaty oddzielania | po audytach |
| 06 | Zbieżność topologiczna, sieci i filtry | po audytach |
| 07 | Zwartość, twierdzenie Tychonoffa, zanurzanie w kostkę | po audytach |
| 08 | Spójność i spójność łukowa | po audytach |
| 09 | Aksjomaty przeliczalności i własność Lindelöfa | po audytach |
| 10 | Metryzowalność i twierdzenie Urysohna | po audytach |
| **11** | **Zupełność, kategoria i twierdzenie Baire'a (wersja metryczna)** | **stabilny — audyt 6** |
| **12** | **Przestrzenie jednostajne, jednostajna ciągłość, ciągi, sieci i filtry Cauchy'ego** | **stabilny — audyt 3** |
| **13** | **Zupełność jednostajna i uzupełnienia metryczne/jednostajne** | **stabilny — audyt 05** |
| **14** | **Zwartość lokalna, twierdzenie Baire'a, podprzestrzenie, iloczyny, przeliczalność w nieskończoności i wyczerpania zwarte** | **stabilny — audyt 03** |
| **15** | **Parazwartość, lokalnie skończone pokrycia i podziały jedności; związki z metryzowalnością** | **stabilny — audyt 06; twierdzenia Stone’a i Nagaty–Smirnowa z pełnymi dowodami** |
| **16** | **Topologia wyznaczona przez funkcje, przestrzenie całkowicie regularne, uzwarcenia i ich równoważność** | **stabilny — audyt 03** |
| **17** | **Uzwarcenie Aleksandrowa i uzwarcenie Čecha–Stone’a: konstrukcje, własności uniwersalne, minimalność, maksymalność i przykłady** | **stabilny — audyt 03; pełne dowody konstrukcji i własności uniwersalnych** |
| **18** | **Przestrzenie odwzorowań, topologia zwarto-otwarta, zbieżność jednostajna na zbiorach zwartych, ewaluacja, prawo wykładnicze, metryzacja i zupełność** | **stabilny — audyt 03; pełne dowody i walidacja CI/PDF** |
| **19** | **Przestrzenie polskie, podprzestrzenie G-delta, zbiory borelowskie i hierarchia indeksowana przeliczalnymi liczbami porządkowymi** | **stabilny — audyt 03; CI/PDF PASS; 590 unikatowych etykiet i 138 poprawnych odsyłaczy w książce** |
| **20** | **Zbiory analityczne, rzuty zbiorów domkniętych, operacja Suslina, zbiór nieborelowski analityczny** | **stabilny — audyty 05–07 (2/2 + 1); kodowanie drzewa 1/2 poprawione; CI/PDF PASS** |
| **21** | **Topologie na rodzinach podzbiorów: Vietoris, metryka Hausdorffa, zupełność, zwartość, Fell, zbieżność i porównanie** | **stabilny — audyty 03–05 (2/2 + 1); CI/PDF PASS** |
| **22** | **Zbieżność Kuratowskiego, topologia Wijsmana i topologia Attoucha–Wetsa; związek z Fellem, właściwość przestrzeni, kontrprzykłady** | **stabilny — audyty 02–04 (2/2 + 1); CI/PDF PASS** |
| **23** | **Wymiar topologiczny: wymiar pokryciowy Lebesgue’a, wymiary ind/Ind, charakterystyka wymiaru 0, wymiar odcinka i sześcianu, nerwy pokryć** | **stabilny — audyty 04–06 (2/2 + 1), CI 45051754287 PASS, osobny PDF 9 stron** |
| **24** | **Grupy topologiczne, otoczenia elementu neutralnego, podgrupy, przestrzenie warstw i grupy ilorazowe, składowa neutralna, struktury jednostajne, twierdzenie Birkhoffa–Kakutaniego** | **stabilny — audyty 02–04 (2/2 + 1), CI 45053429106 PASS, osobny PDF 10 stron** |

Zakresy 12–13 oraz 16–17 są rozdzielone według tematyki, żeby unikać powtarzania dowodów. Zgodnie z zasadą projektu nowe rozdziały nie oznaczają automatycznie ich stabilności.

## Procedura

Dla każdego nowego rozdziału: (1) przygotowanie samodzielnego tekstu z motywacją, przykładami i dowodami bez nieuzasadnionych przeskoków; (2) matematyczny i redakcyjny audyt, także terminologii i odsyłaczy; (3) kontrola rysunków i układu; (4) testy źródeł i kompilacja samodzielnego PDF oraz całej książki; (5) powtarzanie kontroli do uzyskania stabilnej wersji, następnie dopiero przejście dalej. Każda iteracja dokumentuje status poszczególnych rozdziałów. Nie dopisujemy twierdzeń do audytowanych rozdziałów bez szczególnego uzasadnienia.

## Konwencje terminologiczne

- Używamy **uzwarcenie**, nie **zwartościowanie** (również: uzwarcenie Aleksandrowa i uzwarcenie Čecha–Stone’a).
- Używamy **topologia zbieżności jednostajnej na zbiorach zwartych**, nie skrótu „topologia zbieżności zwartej”.
- Przestrzeń **spełnia pierwszy/drugi aksjomat przeliczalności**, nie jest „pierwszo-/drugoprzeliczalna”.
- Angielskie *chart* tłumaczymy jako **mapa**, *sequence* jako **ciąg**; *net* jako **sieć**.
- Wymagamy precyzyjnie sformułowanych twierdzeń i uzasadnionych nietrywialnych przejść (w tym wskazania właściwego wcześniejszego wyniku, jeśli jest użyty).

## Zamknięcie rozdziału 19 (2026-11-22)

Niezależny [audyt 03](../../audits/general_topology/19-przestrzenie-polskie-iteracja-03.md) potwierdził poprawność uzupełnionych dowodów dotyczących podprzestrzeni typu G-delta, przykładów polskich przestrzeni, śladu sigma-algebry borelowskiej oraz skończonej i pozaskończonej hierarchii borelowskiej. Źródło: blob `dd05dd723a4e92756d1e339309079c68a4580485` — bez zmian podczas audytu 03. [GitHub Actions 45019373792](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45019373792) completed/success na tym samym blobie, a w audycie 02 wizualnie sprawdzono 6 stron PDF. Przejście do rozdziału **20** nie wymaga dalszych poprawek rozdziału 19, o ile jego źródło pozostaje niezmienione.


## Rozdział 20 — decyzja po kontroli powtórzeń

Porównano źródła skryptu \`Logika matematyczna i teoria mnogości\`,
zwłaszcza rozdział 30 \`30-gry-nieskonczone-i-aksjomat-determinacji.tex\`,
z rozdziałem 19 topologii i planem rozdziału 20.
W rozdziale 30 logiki występują definicja zbioru analitycznego,
wprowadzenie do klas projektywnych, aksjomatu determinacji,
własności regularności oraz redukcji Wadge’a.
Pełne dowody równoważności reprezentacji analitycznej,
operacji Suslina i konstrukcji nieborelowskiego zbioru
analitycznego **nie** stanowią tam osobnego wykładu.
Wprost przywołano jako zewnętrzny wynik
uniwersalną mierzalność zbiorów analitycznych.

Aby nie powielać materiału, rozdział 20 topologii obejmuje
tylko brakujące podstawy topologiczne z dowodami:
ciągłe obrazy przestrzeni Baire’a, rzuty zbiorów domkniętych,
przeliczalne działania na zbiorach analitycznych, operację Suslina
i zbiór analityczny nieborelowski przez uniwersalny rzut.
Nie zawiera dowodów determinacji, teorii gier, redukcji Wadge’a
ani twierdzeń o regularności z rozdziału 30 logiki.
Teoremat o uniwersalnej mierzalności **nie** został tu wykazany
i nie jest deklarowany jako pokryty.

Źródło: \`chapters/pl/general_topology/20-zbiory-analityczne-i-operacja-suslina.tex\`.
Testy: \`tools/tests/test_general_topology_ch20.py\`;
punkt wejścia \`books/pl/general_topology_ch20.tex\`.
Do czasu zakończenia audytów i zielonego CI
**nie** oznaczać rozdziału 20 jako stabilnego.

## Audyt 20/02 i zgodność definicji (2026-11-22)

Po audycie 01 dodano dowód zgodności analityczności jako ciągłego
obrazu \(\mathbb N^{\mathbb N}\) z definicją przez rzuty borelowskich
podzbiorów \(\mathbb R^{n+1}\), stosowaną w rozdziale 30 skryptu logiki.
Nowy blob rozdziału 20:
\`73de106461510c1be14419882d3b617602cca177\`.
Drugi raport: [20-zbiory-analityczne-iteracja-02.md](../../audits/general_topology/20-zbiory-analityczne-iteracja-02.md).
Pierwsza **czysta** kontrola nowego bloba: **1/2**;
raport 01 dotyczy pierwotnego bloba i nie zalicza się do stabilizacji
po zmianie. W testach i kompilacji samodzielnej
doprecyzowano import czterech odsyłaczy do rozdziału 19 przez
\`xr-hyper\` w punkcie wejścia rozdziału 20.
Dalszy etap: niezależny audyt 03 tego samego bloba oraz pełny
zielony workflow, w tym kontrola PDF i logów.

## CI dla rozdziału 20 (2026-11-22)

[General topology chapter validation 45022608046](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45022608046)
ma wynik **completed/success**, a zweryfikowany blob rozdziału 20
to \`73de106461510c1be14419882d3b617602cca177\`.
Wszystkie kroki: testy, pełna książka, samodzielny PDF 20 i
kontrola logów LaTeX zakończyły się sukcesem.
Samodzielny punkt wejścia importuje etykiety poprzedniego rozdziału
przez \`xr-hyper\`, bez powielania treści 19.
Status pozostaje **1/2**, ponieważ po uzupełnieniu źródła
o równoważność definicji analityczności wykonano dotąd
jedną niezależną czystą kontrolę.

## Audyt rozdziału 20/03 — 2026-11-22

- Audyt 03 był **korekcyjny**: w podsumowaniu błędnie pominięto przypadek pustego zbioru analitycznego oraz błędnie uogólniono ścisłość klasy analitycznej nad borelowską na wszystkie przestrzenie polskie. Obie poprawki: [commit e9ce798](https://github.com/dariusz-piekarz/mathematical_scipts/commit/e9ce798ade43ff453229f916019686a424917316).
- Nowy blob źródła: `c7644dae32a49ae9ac1403f4932018d440586e9b`. Licznik czystych audytów po zmianie: **0/2**.
- Raport: [20-zbiory-analityczne-iteracja-03.md](../../audits/general_topology/20-zbiory-analityczne-iteracja-03.md), [commit 5ff70fc](https://github.com/dariusz-piekarz/mathematical_scipts/commit/5ff70fcbc8f9daecbbe2f9a8ad145b8c1fc4a33c).
- Dla **poprzedniego** bloba audytor pobrał realny PDF z [zielonego CI 45022608046](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45022608046), wyrenderował i obejrzał wszystkie 6 stron A4 bez zastrzeżeń do składu. Po poprawce trzeba potwierdzić CI i wizualnie zweryfikować nowy PDF, a nie przenosić wyniku CI poprzedniego bloba.
- Następnie **audyt 04 rozdziału 20** (nie rozdział 21), zgodnie z zasadą kolejnych czystych audytów tego samego źródła. Zakres rozdziału pozostaje ograniczony do brakujących topologicznych dowodów, bez powielania teorii gier i determinacji ze skryptu logiki.


## Zamknięcie rozdziałów 20 i 21 (2026-11-22)

Rozdział 20: po audycie 03 znaleziono dodatkowy błąd kodowania
uniwersalnego drzewa (predykat dodatniości nie rozróżnia par,
gdy liczby naturalne są dodatnie). Poprawiono kod na wartości 1 i 2.
Audyty 05, 06 oraz dodatkowy 07 są czyste dla bloba
2607376331f94935063107dee49148b45cc1679f.
Potwierdzono ukończone pomyślnie [CI 45040786110](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45040786110)
i poprawność samodzielnego PDF rozdziału 20.

Rozdział 21: wprowadzono rozdział o hiperprzestrzeniach,
naprawiono kolizję etykiet, niejednoznaczność zapisu
przykładu oraz błędy składni LaTeX (\mathscr i podwójne indeksy dolne).
Audyty 03, 04 oraz dodatkowy 05 są czyste dla bloba
a8e0c4dbcf3c3100bf6b3c9e067b6fce0ddaa73b.
[CI 45042413561](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45042413561)
ukończone sukcesem, zbudowano całą książkę i osobny PDF rozdziału 21.
Sprawdzono wizualnie wszystkie siedem stron, w tym rysunek
oraz dowód zwartości Fella. Status książki 1.21: rozdziały 01–21 stabilne.


## Zamknięcie rozdziału 22 (2026-11-22)

Rozdział 22 zawiera dowody wszystkich głównych relacji
między zbieżnością Kuratowskiego, topologiami Fella, Wijsmana
i Attoucha–Wetsa, z precyzyjnym rozróżnieniem założeń
lokalnej zwartości i właściwości przestrzeni metrycznej.
W audycie 01 dodano ogólny dowód zawierania
topologii Fella w topologii Wijsmana na niepustych
zbiorach domkniętych i doprecyzowano niepuste
ograniczone zbiory w definicji zbieżności AW.
Następne audyty 02, 03 i dodatkowy 04 są czyste
dla niezmienionego bloba
`33765c2bb1b3065f4ad32596795c3d1981b48dda`.
Zielona [walidacja 45047289481](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45047289481)
zbudowała całą książkę oraz samodzielny rozdział 22.
Pobrano i wizualnie sprawdzono wszystkie 7 stron PDF
bez kolizji elementów, ostrzeżeń LaTeX i osieroconego akapitu.
Raporty: [02](../../audits/general_topology/22-zbieznosc-zbiorow-iteracja-02.md),
[03](../../audits/general_topology/22-zbieznosc-zbiorow-iteracja-03.md),
[04](../../audits/general_topology/22-zbieznosc-zbiorow-iteracja-04.md).
Końcowa walidacja 45047835224 (https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45047835224)
zakończyła się completed/success po aktualizacji strony tytułowej
i testów regresyjnych. Pobraną pełną książkę 1.22
(156 stron A4) sprawdzono pod kątem zgodności tytułu,
paginacji końcowego rozdziału i poprawności PDF.

## Zatwierdzony dalszy plan po rozdziale 22

Użytkownik zatwierdził kolejne etapy 1–5 w dniu 22 listopada 2026:

1. **Globalny audyt 01–22**: zależności twierdzeń, pełne dowody,
   terminologia, stabilność LaTeX/PDF, porównanie z innymi skryptami.
   Pierwsza kontrola przekrojowa:
   [audyt 00/01](../../audits/general_topology/00-globalny-audyt-01.md).
   Pełne przejrzenie każdego z dowodów i wszystkich rysunków
   jest oddzielnym zadaniem; nie deklarować go wykonanym na
   podstawie testów strukturalnych.
2. **Rozdział 23: Wymiar topologiczny** — wymiar pokryciowy
   Lebesgue'a, definicje małego i dużego wymiaru indukcyjnego,
   przykłady, niezmienniczość, porównanie wymiaru zero,
   podstawowe oszacowania i twierdzenia z dowodami.
   Najpierw przygotować tekst, potem 2/2 czyste audyty +
   jeden potwierdzający na niezmienionym blobie oraz CI/PDF.
3. **Grupy topologiczne** — działania ciągłe, otoczenia jedynki,
   domknięte podgrupy, ilorazy, przykłady; przed rozpoczęciem
   sprawdzić, które wyniki są już w algebrze abstrakcyjnej
   i topologii algebraicznej.
4. **Continua / przestrzenie continuum** — continua,
   spójność lokalna, struktura i kontrprzykłady.
   Rozdział 08 dostarcza podstaw; nie powielać go.
5. **Zbieżność Mosco i zbieżność epigraficzna**
   — materiał przypisany roboczo do analizy
   funkcjonalnej/wariacyjnej (po sprawdzeniu
   zbieżności zbiorów w rozdziale 22).
   W topologii ogólnej tylko odsyłacze, nie
   duplikacja pełnego wykładu.

**Mapa nakładek dla etapów 23–25 i Mosco/epi:** [zobacz mapę](mapa_nakladek-topologia-ogolna-23-26-i-zbieznosc-wariacyjna.md). Istniejące dowody twierdzenia Brouwera (topologia algebraiczna, rozdział 19) i konstrukcji miary Haara (teoria miary, rozdział 23) nie powinny być duplikowane.

**Reguła kolejności:** audytować już istniejący materiał,
następnie tworzyć i stabilizować dokładnie jeden nowy rozdział.
Wykryte merytoryczne błędy poprawiać; rozszerzenia już zatwierdzonych
rozdziałów przedstawiać osobno jako propozycje.

## Zamknięcie rozdziału 23 (2026-11-22)

Rozdział 23 ma stabilny blob `9dc1ed4784d929b405d00a3216865418f240a37c`.
Zawiera pełny dowód wymiaru sześcianu `dim[0,1]^n=n`,
wykorzystując twierdzenie Brouwera dostępne w AT-19 oraz własność
Poincarégo–Mirandy, a także pełny argument triangulacyjny
na górne oszacowanie dla zwartych podzbiorów przestrzeni euklidesowych.
Audyty [04](../../audits/general_topology/23-wymiar-topologiczny-iteracja-04.md),
[05](../../audits/general_topology/23-wymiar-topologiczny-iteracja-05.md),
[06](../../audits/general_topology/23-wymiar-topologiczny-iteracja-06.md)
były kolejno czyste na identycznym blobie, bez zmian źródła.
[CI 45051754287](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45051754287)
ukończyło się sukcesem. Pobrano artefakt 14766071024,
obejrzano wszystkie 9 stron osobnego PDF, w tym rysunek i końcowe
podsumowanie. Brak ostrzeżeń LaTeX oraz osieroconej strony.
Po aktualizacji oznaczenia książki i regresji należy wykonać
jeszcze kontrolę CI dla tej integracyjnej zmiany.

## Przekrojowy audyt globalny 01–22 — pierwsza seria

Wykonano pierwszą serię pięciu audytów tematycznych
obejmujących wszystkie rozdziały 01–22:
[01 — struktura i zależności](../../audits/general_topology/00-globalny-audyt-01.md),
[02 — podstawy 01–06](../../audits/general_topology/00-globalny-audyt-02-blok-01-06.md),
[03 — zwartość, metryzowalność, Baire 07–11](../../audits/general_topology/00-globalny-audyt-03-blok-07-11.md),
[04 — struktury jednostajne i uzwarcenia 12–17](../../audits/general_topology/00-globalny-audyt-04-blok-12-17.md),
[05 — przestrzenie odwzorowań i zbieżność zbiorów 18–22](../../audits/general_topology/00-globalny-audyt-05-blok-18-22.md).

Test globalny skryptów sprawdza na każdej walidacji
zgodność importów z katalogiem, unikatowość wszystkich etykiet,
rozwiązanie odsyłaczy, bilans środowisk i konwencje terminologiczne.
**Granice audytu:** przeanalizowano wybrane centralne dowody
we wszystkich blokach, ale nie dokonano jeszcze indywidualnego,
w pełni niezależnego przeglądu wszystkich 261 środowisk dowodów
w 01–22, jak również wszystkich ilustracji w kompletnej książce.
Nie przedstawiać tej serii jako ukończonego
całościowego audytu matematycznego.
Przed zamknięciem fazy globalnego audytu
kontynuować kontrolę rozdział po rozdziale
i porównania z innymi skryptami.


## Zamknięcie rozdziału 24 (2026-11-22)

Rozdział `24-grupy-topologiczne-i-przestrzenie-jednorodne.tex`
ma stabilny blob `4b72d373d98eab0c1cc4563b72a6bb8fa62170b6`.
Zawiera szczegółowe dowody regularności grup, kryterium
Hausdorffowości G/H, otwartości projekcji G→G/H,
ciągłości działania na przestrzeni warstw,
topologicznego twierdzenia o izomorfizmie,
normalności składowej spójnej oraz całkowitej
niespójności G/G^0, lewych i prawych struktur
jednostajnych i twierdzenia Birkhoffa–Kakutaniego
z konstrukcją lewostronnie niezmienniczej metryki łańcuchowej.

Audyt [01](../../audits/general_topology/24-grupy-topologiczne-iteracja-01.md)
był korekcyjny: uzupełniono pełny dowód metryzowalności
i ciągłości działania na G/H, a także przykład nienormalnej
podgrupy S3.
Audyty [02](../../audits/general_topology/24-grupy-topologiczne-iteracja-02.md),
[03](../../audits/general_topology/24-grupy-topologiczne-iteracja-03.md)
i dodatkowy [04](../../audits/general_topology/24-grupy-topologiczne-iteracja-04.md)
są czyste na identycznym blobie. Kontrola
[CI 45053429106](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45053429106)
zakończyła się sukcesem: samodzielny rozdział ma 10 stron,
cała książka 175 stron. Pobrano oryginalny artefakt
GitHub Actions ID 14766264355, wyrenderowano i obejrzano
wszystkie 10 stron, a strony 6 (rysunek ilorazu)
i 10 (końcowe podsumowanie) sprawdzono indywidualnie.
Brak ostrzeżeń Overfull/Underfull i LaTeX Warning.

Po zmianie strony tytułowej na „Wersja 1.24 —
rozdziały 01–24 stabilne” należy wykonać końcowe
CI regresyjne dla integracji. Następny etap:
**rozdział 25 o continuach**, ze szczególną uwagą
na brak powtarzania podstaw spójności z rozdziału 08.
