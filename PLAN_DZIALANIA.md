# Plan rozbudowy skryptu „Geometria i topologia różniczkowa”

## Kontynuacja po zmianach autora i podział źródeł

5 października 2026 pobrano `19fa283` i porównano go z `66b220f`.
Na aktualną prośbę użytkownika dokument zostaje podzielony na pliki
rozdziałów, przy zachowaniu jednego pliku głównego i jednego PDF.
Zastępuje to wcześniejszą zasadę jednego źródła w `AGENTS.md`.

- [x] Pobrać zmiany i porównać je z wcześniejszymi propozycjami.
- [x] Potwierdzić obecność rozmaitości z brzegiem, grupy wolnej i iloczynu wolnego.
- [x] Wydzielić preambułę, wstęp, 27 rozdziałów, dodatek i indeks.
- [x] Potwierdzić identyczność rozwiniętego źródła i składu przed/po podziale (384 strony, także porównanie pikselowe).
- [x] Wysłać podział wraz z instrukcją wspólnej edycji i kompilacji (`9148128`).
- [x] Przejrzeć merytorycznie zmienione fragmenty rozdziału 1; uzupełnić model przestrzeni stycznej przy brzegu.
- [ ] Przejrzeć nowy rozdział 5 i odsyłacze do algebry.
- [ ] Skontrolować pozostałe zmiany w dotychczasowych rozdziałach.
- [ ] Przejrzeć nowe rozdziały 20–27 oraz dodatek, po jednym rozdziale w iteracji.

Nie dublować tematów już dodanych. Dalsza teoria Freedmana i egzotyczne
R⁴ pozostają przeznaczone do osobnego skryptu. Istniejący rozdział
o sferach Milnora zachowujemy. Nowe propozycje należy odróżniać od
koniecznych napraw dowodów. Bieżące uzasadnienia zmian: `PRZEGLAD.md`.

## Zakończony plan autora — zapis historyczny

Stan końcowy: 5 października 2026. Wszystkie zadania objęte tym planem
zostały wykonane i wypchnięte na `review/rozdzialy-matematyka` w dwóch
etapach: `4233e60` i `b2635d0`. Tekstem źródłowym pozostaje
`geometria_i_topologia_rozniczkowa.tex`; sprawdzony PDF ma 384 strony.

## Kolejność i kontrola postępu

- [x] Przeczytać `AGENTS.md`, `PROPOZYCJE_UZUPELNIEN.md` i sprawdzić stan repozytorium.
- [x] Rozwinąć argument przy twierdzeniu Walla: dokładne hipotezy, część
  algebraiczną i geometryczną, wskazanie głębokich lematów oraz źródeł.
- [x] Zakończyć chirurgię: zbiór struktur, normalne niezmienniki, ciąg dokładny
  chirurgii, interpretacja dokładności i przykłady zastosowań.
- [x] Dodać rysunki do chirurgii i sprawdzić wcześniejsze torusy względem
  jasnej niebieskiej stylistyki sfery z rozdziału 1.
- [x] Dodać dowód twierdzenia Poincarégo dla powierzchni, oparty na
  klasyfikacji zwartych powierzchni z jawnym wskazaniem użytego twierdzenia.
- [x] Dodać argument dla gładkich sfer homotopijnych wymiaru co najmniej 5,
  odróżniając homeomorfizm od dyfeomorfizmu. Wymiar 4 pozostaje poza tą sesją.
- [x] Opracować sfery Milnora: wiązki nad $S^4$, homologia, argument
  homeomorfizmu i niezmiennik wykrywający egzotyczną strukturę; wskazać
  użyte głębokie wyniki.
- [x] Zrealizować punkt 1 propozycji: rozmaitości z brzegiem i spójne
  konwencje w rozdziale 1.
- [x] Zrealizować punkt 2: wstęp do teorii grup przed van Kampenem.
- [x] Zrealizować punkt 3: nawigacja, spis oznaczeń, mapa zależności,
  jednolitsze odsyłacze i bibliografia.
- [x] Zrealizować punkt 5: katalog użytych wyników zewnętrznych i zakres
  samowystarczalności; wybrane krótkie dowody, bez pozorowania dowodu
  triangulacji.
- [x] Zrealizować punkt 6: teoria Cherna–Weila, transgresja oraz zakres
  dowodu twierdzenia Cherna–Gaussa–Bonneta, z wersją brzegową.
- [x] Rozpisać słowa w grupie wolnej, redukcję, działanie na słowach,
  własność uniwersalną i dodać rysunek grafu słów.
- [x] Ponownie skontrolować rozdziały 22–26 i dodatek pod kątem
  matematycznym, językowym i bibliograficznym; nanieść poprawki.
- [x] Uruchomić polecenie `latexmk` z `AGENTS.md` i, przy braku Perla
  w MiKTeX, złożyć dokument przez `pdflatex` oraz `makeindex`;
  skontrolować błędy, odsyłacze i strony z rysunkami.
- [x] Przejrzeć różnice, zatwierdzić etap pierwszy i wypchnąć go na gałąź
  `review/rozdzialy-matematyka`.
- [x] Po pierwszym commicie i pushu wydzielić rozdział algebry abstrakcyjnej
  przed algebrą homologiczną: grupy i prezentacje, pierścienie i ideały,
  moduły, iloczyn tensorowy modułów, własność uniwersalna i przykłady.
- [x] Złożyć i skontrolować nowy rozdział, zatwierdzić drugi etap i wypchnąć.

## Przyjęte granice dowodów

Dopisane dowody elementarne rozpisano krok po kroku. Długie twierdzenia, które
stanowią odrębne teorie (klasyfikacja powierzchni, geometryczne lematy Walla,
twierdzenie o $h$-kobordyzmie, twierdzenie Hirzebrucha),
otrzymały dokładne założenia, źródła i wyraźne oznaczenie jako wyniki
zewnętrzne, jeśli ich pełnego dowodu tu nie ma. Punkt 4 (zadania) i punkt 12
(egzotyczne $\mathbb R^4$) oraz dowód dla wymiaru 4 pozostają poza zakresem.
Sfery Milnora należą do tego skryptu: skonstruowane rozmaitości mają wymiar 7.

## Rozdział algebry abstrakcyjnej — decyzja

Osobny rozdział był uzasadniony. Sekcje o grupach i modułach
przeniesiono przed algebrę homologiczną z zachowaniem etykiet.
Rozdział o tensorach przestrzeni liniowych pozostaje w swoim miejscu,
ponieważ jest potrzebny wcześniej w geometrii; iloczyn tensorowy
modułów uogólnia tamtą konstrukcję. „Domknięcie iloczynu tensorowego”
nie jest standardową nazwą w tym kontekście: chodzi o podmoduł
generowany przez relacje zbiliniowości i zbalansowania. Domknięcie
normalne dotyczy relacji grupowych. Dokładność ciągów i kompleksy
pozostały w rozdziale algebry homologicznej.

## Propozycje poza ukończonym planem

1. Twierdzenie Hodge'a i wzory Bochnera–Weitzenböcka: łączą formy,
   krzywiznę Ricciego i ograniczenia topologiczne; wymagają jawnego
   wskazania analitycznego twierdzenia o operatorach eliptycznych.
2. Holonomia koneksji i rozkład de Rhama: rozwijają transport równoległy
   i wyjaśniają, kiedy metryka rozkłada się lokalnie na produkt.
3. Geometria podrozmaitości: równania Gaussa–Codazziego, krzywizna średnia
   i pierwsze przykłady powierzchni minimalnych; korzysta z już
   wprowadzonej drugiej formy podstawowej.

## Dziennik

- 2026-10-05: sprawdzono stan plików i gałęzi; w TeX-u są 22 rozdziały oraz
  obszerne, niezatwierdzone zmiany rozdziałów 19–22. Przeczytano propozycje;
  rozpoczęto kontrolę merytoryczną i redakcyjną.
- 2026-10-05: dopisano rozwinięcie Walla, ciąg chirurgii, Poincarégo dla
  wymiarów 2 i co najmniej 5, sfery Milnora, teorię Cherna–Weila i
  Cherna–Gaussa–Bonneta oraz dodatek źródłowy. Po audycie skorygowano
  zmienną wiązkę docelową w normalnych niezmiennikach, stopień z lokalnym
  systemem orientacji i przestrzeń styczną na brzegu. Rozbudowano indeks.
- 2026-10-05: polecenie `latexmk` uruchomiono; MiKTeX zgłosił brak Perla.
  Pierwszy pełny skład `pdflatex` przeszedł; następnie wykonano `makeindex`,
  kolejne przebiegi składu, przegląd stron rysunkowych i kontrolę ostrzeżeń.
- 2026-10-05: obejrzano w PDF torusy na stronach 307 i 321 oraz nowe schematy
  Walla, ciągu chirurgii, Poincarégo i Milnora na stronach 361, 365, 368
  i 370. Poprawiono odstępy podpisów w schemacie ciągu. Indeks ma 146
  odsyłaczy i jest widoczny na końcowych stronach PDF; uzupełniono
  odsyłacze bibliograficzne przy rozdziałach 2 i 3.
- 2026-10-05: na prośbę użytkownika dopisano pełną konstrukcję grupy
  wolnej przez słowa i algorytm redukcji oraz rysunek grafu. Ponowiono
  audyt rozdziałów 22–26; poprawiono precyzję dowodów Walla i Milnora,
  kilka sformułowań i wskazania źródeł. Zaplanowano drugi etap algebry.
- 2026-10-05: po ostatnich poprawkach `latexmk` nadal nie może wystartować
  bez Perla. Dwa przebiegi `pdflatex` i `makeindex` dały 381 stron;
  w logu nie ma brakujących odsyłaczy ani błędów składu. Obejrzano
  nowy graf słów na stronie 103 i wcześniej poprawione torusy oraz
  schematy dalszych rozdziałów.
- 2026-10-05: etap pierwszy zatwierdzony jako `4233e60` i wypchnięty
  na `origin/review/rozdzialy-matematyka`. Rozpoczęto wydzielanie
  podstaw algebry do osobnego rozdziału.
- 2026-10-05: w etapie drugim powstał rozdział 5 z grupami, pierścieniami,
  modułami, iloczynem tensorowym i modułami projektywnymi. Dawny rozdział
  homologiczny zaczyna się teraz od ciągów dokładnych jako rozdział 6.
  Usunięto powtórzony opis tensoru z późniejszej części homologicznej;
  audyt matematyczny potwierdził konstrukcję i przykłady. Ostateczny
  PDF ma 384 strony. `makeindex` przyjął 152 wpisy; ostatni log nie
  zgłasza błędów, brakujących odsyłaczy ani potrzeby kolejnego przebiegu.
  Obejrzano strony 103–107 z grafem słów i nowymi sekcjami algebry.
- 2026-10-05: drugi etap zatwierdzono jako `b2635d0` i wypchnięto
  na `origin/review/rozdzialy-matematyka`. Wszystkie pozycje kontrolne
  tego planu są zakończone; trzy pomysły geometryczne powyżej nie należą
  do jego zakresu.
