# Teoria miary — audyt VIII, wyłącznie rozdział 01

Data: 2026-11-23. Gałąź: `biblioteka-matematyczna-iteracja-6`.
Rozdział: `chapters/pl/measure_theory/01-rodziny-zbiorow-i-przestrzenie-mierzalne.tex`.
**Status: matematycznie bez nowych usterek; stabilizacja formalna wstrzymana do wyniku i kontroli PDF.**

## Stan wejściowy

Pobrano bieżący HEAD `854785a460178f5ad09458c94c82882add4019ce`, wszystkie siedem poprzednich raportów w katalogu, aktualny rozdział (blob `a7c8610bf1eb9e4612e96df9f038679af4d4d2fb`), plik główny `books/pl/measure_theory.tex`, `AGENTS.md` i `docs/pl/standardy_terminologiczne.md`. Zweryfikowano, że audyt VII był ostatnim zakończonym przebiegiem, bez zmian źródła od audytu IV. Rozdziały 02–31 nie były przedmiotem audytu ani zmian.

## Przeprowadzona kontrola matematyczna

Ponownie sprawdzono zakres wszystkich sześciu sekcji rozdziału 01: aksjomaty σ-algebr, przykłady skończono-kofinitywne i podziałowe, ślad, generowanie, układy π i Dynkina, twierdzenie π–λ, klasy monotoniczne, generatory borelowskie w R i R^d oraz mierzalność funkcji. W szczególności sprawdzono, że:
- rosnąca suma σ-algebr singletonowych daje dokładnie rodzinę zbiorów skończonych/kofinitywnych, a nie σ-algebrę;
- w dowodzie π–λ dwukrotne zastosowanie minimalności układu Dynkina nie wymaga dodatkowych założeń;
- w dowodzie twierdzenia o klasie monotonicznej przejście od sum skończonych do przeliczalnych odbywa się przez ciąg rosnący;
- w kryterium mierzalności przez generatory obrazy odwrotne zachowują dopełnienia i sumy przeliczalne.

Dodatkowa regresja skończona: uruchomiono enumerację wszystkich **65 536** rodzin podzbiorów zbioru czteroelementowego, sprawdzając aksjomaty algebry i σ-algebry. Znaleziono **15** algebr i **15** σ-algebr, bez rozbieżności. Dla skończonej przestrzeni każda rodzina jest klasą monotoniczną, bo ciągi monotoniczne zbiorów stabilizują się; zatem dla wszystkich 15 algebr twierdzenie o klasie monotonicznej zachodzi, choć ten model nie sprawdza jego nietrywialnego aspektu nieskończonego. **Nie znaleziono nowego błędu w źródle.**

## Nowy, mierzalny postęp techniczny

Dotychczasowe audyty V–VII były blokowane przez brak pobrania repozytorium do lokalnego kontenera (DNS). W tej iteracji utworzono **rzeczywisty, ograniczony do rozdziału 01 workflow CI** `.github/workflows/measure-theory-ch01.yml`, commit `6b20a5650cd744dc4321e269e8963f7d5c1a8d9b`. Workflow:
1. pobiera pełne repozytorium przez `actions/checkout@v4` na runnerze GitHub;
2. instaluje TeX Live z obsługą języka polskiego, TikZ oraz `pdfinfo` i `pdftotext`;
3. tworzy dokument tylko rozdziału 01 z **oryginalną preambułą** `books/pl/measure_theory.tex` (bez zmiany źródła książki);
4. dwukrotnie uruchamia `pdflatex -interaction=nonstopmode -halt-on-error -file-line-error`, kontroluje istnienie PDF, metadane i obecność tytułu w ekstrakcji tekstu;
5. udostępnia PDF, log i tekst jako artefakt do rzeczywistej oceny.

Workflow jest celowo ograniczony do rozdziału 01, więc **nie stanowi pełnej kompilacji 31-rozdziałowej książki**. Dwa odsyłacze do rozdziału 02 mogą być nierozwiązane w samodzielnym PDF; workflow je loguje, nie traktuje ich jako błędu, ponieważ ich cel `ch:miary-wlasnosci` istnieje w R02. Odczyt z API potwierdził uruchomienie workflow pod numerem [45113110234](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45113110234); **w chwili tworzenia raportu miał status `in_progress`**. Nie deklarujemy wyniku przed zakończeniem.

## Ponowna statyczna kontrola aktualnego źródła

- Blob R01: `a7c8610bf1eb9e4612e96df9f038679af4d4d2fb`, **537 linii**.
- **19** etykiet, wszystkie różne; **12** odsyłaczy, w tym 10 lokalnych i dwa do R02.
- **43** poprawnie sparowane środowiska LaTeX; 0 niedomknięć.
- **11** wystąpień `\\chi_`; brak `\\mathbf{1}`, `\\mathbb{1}` i `\\mathds{1}`.
- Rozdział 01 nie zawiera rysunków. Wciąż wymagana rzeczywista kontrola stron i łamania w artefakcie PDF.

## Stan stabilizacji i następna iteracja

**ROZDZIAŁ 01 NIE ZOSTAŁ JESZCZE FORMALNIE UZNANY ZA STABILNY.** Po ostatniej poprawce źródła odbyły się kolejne czyste audyty V–VIII. Nowością jest odblokowanie drogi do powtarzalnej kompilacji na GitHub Actions, a nie uzyskany już wynik pełnego buildu. W następnej iteracji odczytać zakończony workflow, pobrać i obejrzeć PDF oraz log, rozstrzygnąć ewentualne błędy techniczne, a następnie — jeśli wszystkie wymagane kontrole zakończą się sukcesem — nadać status stabilności rozdziałowi 01. Dopiero w osobnej iteracji przejść do rozdziału 02.
