# Teoria miary / Miara i całka — audyt I, rozdziały 01–02

Data: 2026-11-23. Gałąź: `biblioteka-matematyczna-iteracja-6`.
Przedmiot: `chapters/pl/measure_theory/01-rodziny-zbiorow-i-przestrzenie-mierzalne.tex` i `02-miary-i-ich-podstawowe-wlasnosci.tex`.
Status: **pierwszy przebieg ukończony; blok NIE jest jeszcze ustabilizowany**. Przed przejściem do rozdziału 03 potrzebny kolejny niezależny audyt oraz pełna kompilacja.

## Rzeczywiste poprawki matematyczno-redakcyjne

1. **R01, twierdzenie o generatorach borelowskich `thm:borel-generators-R`:** uzasadnienie, że każdy zbiór otwarty jest sumą przeliczalnie wielu przedziałów o końcach wymiernych, rozwinięto o konstrukcję przedziału wokół dowolnego punktu, wykorzystującą otwartość zbioru i gęstość `\mathbb Q`. Zachowano wszystkie oryginalne etykiety. Commit: `b727efb78f77211c64681307e839565de6f58e6e`.
2. **R02, przykład miary liczącej `ex:counting`:** wyeliminowano przeskok przy nieskończonej sumie rozłącznych zbiorów. Rozróżniono przypadek jednego nieskończonego składnika oraz nieskończenie wielu niepustych składników, wykazując w obu przypadkach nieskończoność sumy miar. Commit: `a591e0a75d3f723f35535b8586d137a2d0ff0677`.
3. **R02, przykład ważonej miary dyskretnej `ex:weighted-discrete`:** przestawienie szeregów o nieujemnych wyrazach uzasadniono wprost przez kresy górne sum po skończonych prostokątach indeksowych `F×G`, bez korzystania z wprowadzanego dopiero później twierdzenia Tonellego. Ujednolicono zapis sumy w indeksie funkcji charakterystycznej do `\chi_{\bigcup_k A_k}`. Ten sam commit co w punkcie 2.

Zmiany nie rozszerzają merytorycznie zatwierdzonego zakresu rozdziałów; domykają istniejące uzasadnienia.

## Kontrole źródeł po commitach

Ponownie pobrano z GitHub źródła obu rozdziałów po zmianach i zweryfikowano obecność poprawek oraz SHA blobów:
- R01: `a79669559d7ee351f9ac4cf7c72763d7e2ca479b`, 509 linii, 19 etykiet, 12 odsyłaczy.
- R02: `b0cca040ad3571aeb5290d8d87a53d28eeb0c956`, 786 linii, 34 etykiety, 17 odsyłaczy.
- Łącznie **53 etykiety**, **29 odsyłaczy**; 0 powtórzonych etykiet i 0 niezdefiniowanych odsyłaczy *w tym dwurozdziałowym zakresie*.
- Pary `\\begin{...}` / `\\end{...}`: 43 w R01, 67 w R02, brak niesparowanych lub niezgodnych środowisk w sprawdzeniu statycznym.
- W tych dwóch rozdziałach brak zapisów funkcji charakterystycznej przez `\mathbf{1}` / `\mathbb{1}`.
- Książka `books/pl/measure_theory.tex` włącza 31 rozdziałów i 2 suplementy. Katalog `chapters/pl/measure_theory/` ma odpowiednie 31 plików rozdziałów i folder suplementów. Sprawdzenie odsyłaczy i integralności powyżej **nie obejmuje jeszcze całej książki**.

## Zakres równoległy i potencjalne problemy

- Repozytorium zawiera również `books/pl/integration_theory.tex` i 17 plików `chapters/pl/integration_theory/` (rozdziały 00–16). Dokument ma niezależny zakres całkowania; w dalszych audytach należy sprawdzić zgodność i nakładki, nie scalać automatycznie.
- W preambule `books/pl/integration_theory.tex` występuje stara definicja `\ind` przez `\mathbf 1`. Wymaga odrębnego sprawdzenia jej zastosowań i migracji zgodnej z konwencją `\chi_A` bez naruszenia semantyki; nie zmieniano jej w tej iteracji.
- Opcjonalne wzbogacenie do decyzji użytkownika: R01 dwukrotnie omawia nieciągłość funkcji `\chi_{\mathbb Q}`. Można w jednym z miejsc wprowadzić inny kontrprzykład lub odesłanie zamiast duplikacji; bez zgody nie zmieniano zaakceptowanego przykładu.

## Uczciwy status weryfikacji

Przeprowadzono merytoryczny audyt wskazanych fragmentów oraz statyczne kontrole etykiet, odsyłaczy i środowisk. **Nie uruchomiono w tej iteracji `pdflatex`, pełnego testowania repozytorium, wizualnego audytu PDF ani niezależnego CI**. Zapytania o statusy i powiązane przebiegi GitHub Actions dla drugiego commita zwróciły puste listy — nie oznacza to pozytywnego wyniku CI. Historyczny raport `audits/iteration_5_measure_theory.md` opisuje udaną kompilację wcześniejszej wersji, a nie tych zmian.

## Kolejny krok

1. Ponownie przeczytać R01–R02 niezależnie, z naciskiem na twierdzenie Dynkina, twierdzenie o klasie monotonicznej, uzupełnianie miar i jednoznaczność miar przy wspólnym wyczerpaniu.
2. Sprawdzić spójność całej książki, kompilację LaTeX i czytelność PDF na aktualnym commitcie; jeśli brak środowiska umożliwiającego rzeczywisty build, jawnie oznaczyć ograniczenie.
3. Dopiero po stabilizacji R01–R02 przejść do R03–R04; zapisywać kolejne raporty w tym samym katalogu.

Przestrzegane zasady: `AGENTS.md`, `docs/pl/standardy_terminologiczne.md`, zachowanie stabilnych `\label`/`\ref`, brak niezatwierdzonych rozszerzeń materiału.
