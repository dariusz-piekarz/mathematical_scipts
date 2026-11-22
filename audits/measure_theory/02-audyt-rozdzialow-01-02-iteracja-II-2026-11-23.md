# Teoria miary / Miara i całka — audyt II, rozdziały 01–02

Data: 2026-11-23. Gałąź: `biblioteka-matematyczna-iteracja-6`. Stan gałęzi na początku: `29fe9ba44aeca7a154c0359e13adf65d1abc1518`. Kontynuacja raportu `01-audyt-rozdzialow-01-02-iteracja-I-2026-11-23.md` (pierwszy przebieg wykonany, blok nieustabilizowany).

## Zakres niezależnego przebiegu

Ponownie pobrano źródła R01 `01-rodziny-zbiorow-i-przestrzenie-mierzalne.tex` oraz R02 `02-miary-i-ich-podstawowe-wlasnosci.tex`, `AGENTS.md`, `docs/pl/standardy_terminologiczne.md` oraz pliki główne `books/pl/measure_theory.tex` i `books/pl/integration_theory.tex`. Kontrolowano definicje i argumenty o układach Dynkina, klasach monotonicznych, generatorach borelowskich, mierzalności, ciągłości miary, uzupełnieniu miary, jednoznaczności miar i atomach. Bez nowych twierdzeń, bez zmian etykiet, bez przechodzenia do R03.

## Zmiana w źródle (rzeczywisty postęp)

R02, wniosek `cor:countably-many-disjoint-atoms`: poprzedni dowód opierał się na opisowym stwierdzeniu, że „dowolnie wiele” rozłącznych fragmentów o mierze co najmniej `1/k` przekroczyłoby miarę skończonego zbioru. Dopisano jawne zbiory indeksów `I_{n,k}` i nierówność
`m/k <= sum_{j=1}^m mu(A_{i_j} cap E_n) <= mu(E_n)<infty`
dla dowolnych parami różnych indeksów. Z nierówności wynika skończoność `I_{n,k}`, a z `I=union_{n,k} I_{n,k}` — przeliczalność całej rodziny. Uzasadniono każdy krok bez nowych założeń. Commit źródła: `ed2c2d6c654dc7efeabe3d34339c385602499342`.

Po zapisie ponownie odczytano R02 z GitHub i potwierdzono nowy blob SHA `b48e368acfa0b8fffaeed59f7d33ad5ab75a3d20` oraz obecność pełnej nierówności i domknięcia argumentu. R01 pozostał bez zmian, blob SHA `a79669559d7ee351f9ac4cf7c72763d7e2ca479b`.

## Weryfikacja techniczna i ograniczenia

W obu rozdziałach zachowano historyczne etykiety i odsyłacze; poprawka nie wprowadza nowych `label`, `ref` ani nowych środowisk. Wcześniejsza statyczna kontrola 53 etykiet, 29 odsyłaczy i 110 par środowisk jest opisana w audycie I; nie przedstawiamy jej jako ponownego niezależnego testu tej iteracji. Nie uruchomiono lokalnie `pdflatex`, testów terminologicznych, przeglądu PDF ani pełnego CI na nowym commitcie. Zapytanie o łączny status nowego commita zwróciło pustą listę statusów; to nie jest wynik pozytywny. W API Actions widoczne są wcześniejsze zakończone sukcesem przebiegi dla `a591e0a7` (2026-11-22 23:35 UTC), nie dla bieżącej poprawki. Przykład: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45084036098 .

Spójność strukturalna: `books/pl/measure_theory.tex` nadal deklaruje 31 rozdziałów i suplementy; `books/pl/integration_theory.tex` pozostaje odrębnym skryptem (00–16). W tym drugim utrzymuje się makro `\\ind` rozwijane do `\\mathbf 1`, wymagające osobnego audytu użyć i ewentualnej korekty, nieautomatycznego scalenia.

## Status i dalsze kroki

**R01: po drugim przeglądzie merytorycznym, ale bez pełnego testu PDF/CI; nieoznaczony jako stabilny. R02: jedna dalsza luka uzasadnienia zamknięta; wymaga ponownej niezależnej kontroli oraz kompilacji.** Nie przechodzić do R03 przed zamknięciem tego bloku. W następnej iteracji przejrzeć R01–R02 ponownie, wykonać rzeczywisty build i przegląd wizualny, jeśli środowisko umożliwia, oraz potwierdzić wyniki Actions dla nowych commitów. Opcjonalna propozycja z audytu I dotycząca powtórzenia przykładu `\\chi_{\\mathbb Q}` pozostaje bez zmian i bez samowolnej ingerencji.
