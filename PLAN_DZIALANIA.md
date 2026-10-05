# Plan rozbudowy skryptu „Geometria i topologia różniczkowa”

Stan roboczy: 5 października 2026. Tekstem źródłowym pozostaje
`geometria_i_topologia_rozniczkowa.tex`. Istniejące niezapisane w Git zmiany
w tym pliku należą do bieżącej pracy i zostają zachowane.

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
- [ ] Przejrzeć różnice, zatwierdzić etap pierwszy i wypchnąć go na gałąź
  `review/rozdzialy-matematyka`.
- [ ] Po pierwszym commicie i pushu wydzielić rozdział algebry abstrakcyjnej
  przed algebrą homologiczną: grupy i prezentacje, pierścienie i ideały,
  moduły, iloczyn tensorowy modułów, własność uniwersalna i przykłady.
- [ ] Złożyć i skontrolować nowy rozdział, zatwierdzić drugi etap i wypchnąć.

## Przyjęte granice dowodów

Dowody elementarne będą rozpisane krok po kroku. Długie twierdzenia, które
stanowią odrębne teorie (klasyfikacja powierzchni, geometryczne lematy Walla,
twierdzenie o $h$-kobordyzmie, twierdzenie Hirzebrucha),
otrzymają dokładne założenia, źródła i wyraźne oznaczenie jako wyniki
zewnętrzne, jeśli ich pełnego dowodu tu nie ma. Punkt 4 (zadania) i punkt 12
(egzotyczne $\mathbb R^4$) oraz dowód dla wymiaru 4 pozostają poza zakresem.
Sfery Milnora należą do tego skryptu: skonstruowane rozmaitości mają wymiar 7.

## Rozdział algebry abstrakcyjnej — decyzja

Osobny rozdział jest uzasadniony. Obecne sekcje o grupach i modułach
zostaną przeniesione przed algebrę homologiczną z zachowaniem etykiet.
Rozdział o tensorach przestrzeni liniowych pozostaje w swoim miejscu,
ponieważ jest potrzebny wcześniej w geometrii; nowy iloczyn tensorowy
modułów uogólni tamtą konstrukcję. „Domknięcie iloczynu tensorowego”
nie jest standardową nazwą w tym kontekście: chodzi o podmoduł
generowany przez relacje zbiliniowości i zbalansowania. Domknięcie
normalne dotyczy relacji grupowych. Dokładność ciągów i kompleksy
pozostaną w rozdziale homologicznej.

## Dalsze tematy geometrii różniczkowej do osobnej decyzji

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
  Pierwszy pełny skład `pdflatex` przeszedł. Trwa ponowny skład po poprawkach,
  wykonanie `makeindex`, przegląd stron rysunkowych i kontrola ostrzeżeń.
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
