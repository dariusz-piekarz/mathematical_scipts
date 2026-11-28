# Teoria miary / Miara i całka — audyt III, WYŁĄCZNIE rozdział 01

Data: 2026-11-23 (Europe/Warsaw). Gałąź: `biblioteka-matematyczna-iteracja-6`.
Źródło: `chapters/pl/measure_theory/01-rodziny-zbiorow-i-przestrzenie-mierzalne.tex`.
Kontynuacja: `01-audyt-rozdzialow-01-02-iteracja-I-2026-11-23.md` i `02-audyt-rozdzialow-01-02-iteracja-II-2026-11-23.md`.

**Zasada obowiązująca od tego etapu: dokładnie jeden rozdział na iterację, wielokrotne niezależne audyty do stabilności, w tym dodatkowy czysty audyt po ostatniej poprawce.** Rozdział 02 i dalsze nie zostały w tej iteracji audytowane ani zmienione.

## Stan wejściowy i zakres

Odczytano aktualne źródło R01 z gałęzi (blob `a79669559d7ee351f9ac4cf7c72763d7e2ca479b`), oba wcześniejsze raporty, `AGENTS.md`, `docs/pl/standardy_terminologiczne.md`, plik główny `books/pl/measure_theory.tex`, a `books/pl/integration_theory.tex` i początek R02 wykorzystano wyłącznie do sprawdzenia kontekstu odsyłaczy i rozdzielenia skryptów. Wcześniejsze raporty potwierdzały korekty generatorów borelowskich w R01 i fragmentów R02; R01 nie miał potwierdzonej stabilności ani aktualnego pełnego buildu PDF.

Niezależnie sprawdzono następujące zagadnienia R01: definicje pierścienia/algebry/σ-algebry, przykłady rodzin skończonych/kofinitywnych i przeliczalnych/koprzeliczalnych, σ-algebry z podziału, generatory i ślady, układy π i Dynkina, twierdzenie π–λ, klasy monotoniczne, twierdzenie o klasie monotonicznej, generatory borelowskie w R i R^d, mierzalność odwzorowań, działania na funkcjach i przykłady nieciągłości.

## Cztery rzeczywiste uzupełnienia uzasadnień

1. **Przykład rodziny zbiorów skończonych i kofinitywnych (`ex:finite-cofinite`).** Dodano niezależny argument zamknięcia na sumę oraz rozbicie dowodu zamknięcia na różnicę `A\setminus B`: wynik jest skończony, jeśli `A` jest skończony lub `X\setminus B` jest skończony; w jedynym pozostałym przypadku `X\setminus(A\setminus B)=(X\setminus A)\cup B` jest skończony. Zachowano istniejący kontrprzykład do σ-addytywnego zamknięcia rodziny na sumy przeliczalne.
2. **σ-algebra generowana przez podział.** Wprowadzono notację `E_J=\bigcup_{i\in J}E_i` oraz wprost sprawdzono `E_I=X`, `X\setminus E_J=E_{I\setminus J}` i `\bigcup_n E_{J_n}=E_{\bigcup_n J_n}`.
3. **Sześcioelementowy przykład układu Dynkina.** Uzasadniono zamknięcie na dopełnienia, różnice zbiorów zagnieżdżonych i przeliczalne sumy rozłącznych elementów, przy zachowaniu kontrprzykładu `\{1,2\}\cap\{1,3\}=\{1\}\notin\mathcal D`. Uwaga: jest to uściślenie istniejącego przykładu, nie nowe twierdzenie.
4. **Nieciągłość `\chi_{\mathbb Q}`.** Doprecyzowano, że w każdym otoczeniu dowolnego punktu są liczby wymierne i niewymierne, na których funkcja przyjmuje różne wartości.

Commit źródła: `3ffb542ce3385c01630a4daff9c7dffa0975fdd0`.
Ponowne odczytanie źródła z GitHub potwierdziło obecność wszystkich czterech uzupełnień i blob SHA `c2f4d454523928188af36368e02348cc5771c6d2`.

## Kontrole niezależne i wyniki

- R01 po zmianach: **529 linii**, **19 różnych etykiet**, **12 odsyłaczy**, **43 pary środowisk**. Nie wykryto duplikatów etykiet ani niesparowanych środowisk.
- Dziesięć odsyłaczy wskazuje lokalne etykiety R01; dwa wystąpienia `ch:miary-wlasnosci` mają cel w R02 (potwierdzono jego deklarację przez odczyt kontekstowy). W pliku głównym książki R01 jest włączany.
- Brak starych notacji `\mathbf{1}`, `\mathbb{1}` i `\mathds{1}` w R01. Nie zmieniono żadnych istniejących `\label` ani `\ref`.
- Niezależny test enumeracyjny dla układu Dynkina na zbiorze czteroelementowym: sprawdzono dopełnienia, wszystkie różnice zagnieżdżonych zbiorów, wszystkie rozłączne pary i wszystkie skończone rodziny parami rozłączne spośród sześciu elementów; układ spełnia aksjomaty Dynkina i nie zawiera singletonu `\{1\}` będącego przekrojem dwóch jego elementów. **PASS**.
- Test enumeracyjny rodziny sum bloków podziału na trzy bloki: osiem różnych elementów, domknięcie na dopełnienia i wszystkie dwuargumentowe sumy; w przestrzeni skończonej zapewnia to również zamknięcie na sumy przeliczalne. **PASS**.
- Lokalny `pdflatex -interaction=nonstopmode -halt-on-error` uruchomiony na **pomocniczym dokumencie A4** zawierającym zaktualizowane fragmenty przykładów o zbiorach skończonych/kofinitywnych i podziale: PDF 1-stronicowy, 0 `Overfull \\hbox`. **PASS**, ale to nie jest kompilacja pełnego pliku R01 ani całej książki.
- GitHub Actions dla commita źródłowego: `Polish mathematical terminology`, przebieg `45084718813`, zakończony sukcesem; `Mathematical library application checks`, przebieg `45084718832`, był w trakcie ostatniego odczytu. Nie przedstawiać nieukończonego przebiegu jako sukcesu.

## Status stabilizacji i ograniczenia

**ROZDZIAŁ 01: NADAL NIESTABILNY W PROCEDURZE AUDYTOWEJ.** To audyt wprowadzający cztery uzupełnienia, a nie dodatkowy czysty audyt po ostatniej poprawce. Wymagany jest następny pełny, sceptyczny przegląd R01 na nowym blobie, pełna kompilacja aktualnych źródeł i rzeczywista kontrola PDF. Nie wykonano jeszcze pełnej kompilacji książki (31 rozdziałów) ani wizualnego sprawdzenia PDF. Nie zgłaszano żadnej poprawki w R02–R31.

**Propozycja opcjonalna (bez zmian źródła):** przykład `\chi_{\mathbb Q}` występuje dwa razy w R01, w dwóch różnych kontekstach. Ewentualne zastąpienie jednego wystąpienia innym kontrprzykładem/odsyłaczem wymaga zgody użytkownika i nie jest warunkiem stabilności aktualnej wersji.

## Następna iteracja

Ponownie pobrać rozdział 01, przeprowadzić pełny niezależny audyt na aktualnym SHA, zweryfikować stan drugiego przebiegu CI i — jeżeli dostępne są kompletne źródła — skompilować aktualny plik książki, przejrzeć PDF. Jeżeli nie pojawią się błędy, udokumentować pierwszy czysty przegląd po poprawkach, a dopiero po dodatkowym niezależnym potwierdzeniu nadać stabilność R01. Rozdział 02 pozostaje bez zmian do stabilizacji R01.