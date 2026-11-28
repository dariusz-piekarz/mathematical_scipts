# Teoria miary / Miara i całka — audyt IV, wyłącznie rozdział 01

Data: 2026-11-23. Gałąź: `biblioteka-matematyczna-iteracja-6`.
Plik: `chapters/pl/measure_theory/01-rodziny-zbiorow-i-przestrzenie-mierzalne.tex`.
Wcześniejszy raport: `03-rozdzial-01-audyt-III-2026-11-23.md`.

## Stan wejściowy i zakres

Przed audytem pobrano aktualny rozdział 01, najnowszy raport III, `AGENTS.md`, `docs/pl/standardy_terminologiczne.md`, `books/pl/measure_theory.tex` i historię commitów. Początkowy SHA bloba R01: `c2f4d454523928188af36368e02348cc5771c6d2`. W raporcie III rozdział 01 był niestabilny po czterech poprawkach; żaden nowszy raport nie potwierdzał jego stabilności. W tej iteracji nie audytowano ani nie zmieniano R02–R31.

Ponownie przejrzano definicje pierścienia, algebry i σ-algebry, generowanie i ślady, przykłady rodzin zbiorów, układy Dynkina i twierdzenie π–λ, klasy monotoniczne, generatory borelowskie, mierzalność odwzorowań i operacje na funkcjach. Osobny sceptyczny przegląd wykazał **jedno niewyjaśnione przejście w istniejącym przykładzie**: stwierdzenie, że rosnąca suma σ-algebr generowanych przez singletony jest dokładnie algebrą zbiorów skończonych i kofinitywnych, nie zawierało dowodu obu inkluzji.

## Poprawka matematyczna

W uwadze `Pułapka dotycząca sumy rodzin` rozpisano jawnie elementy `\mathcal F_n` jako sumy bloków podziału
`\{\{1\},\ldots,\{n\},\mathbb N\setminus\{1,\ldots,n\}\}`.
Każdy taki element jest skończony albo ma skończone dopełnienie. Odwrotnie, dla każdego zbioru skończonego lub kofinitywnego można wybrać `n`, dla którego odpowiedni skończony zbiór (lub dopełnienie) mieści się w `\{1,\ldots,n\}`; stąd należy on do `\mathcal F_n`. W konsekwencji `\bigcup_n\mathcal F_n` jest dokładnie wskazaną algebrą, która nie jest σ-algebrą (wcześniejszy kontrprzykład). Nie dodano nowego twierdzenia, etykiet ani zakresu materiału.

Commit źródła: `c426ca4e24462ae009bfff2e76a0f7e72837858c`.
Po aktualizacji ponownie odczytano plik z GitHuba: blob SHA `a7c8610bf1eb9e4612e96df9f038679af4d4d2fb`; 537 linii; nowy argument jest obecny.

## Weryfikacja

- 19 etykiet, wszystkie różne; 12 odsyłaczy, w tym 2 odsyłacze do `ch:miary-wlasnosci` w R02 (cel potwierdzony w poprzedniej iteracji); bez zmian istniejących `\label`/`\ref`.
- 43 pary środowisk LaTeX; brak niedomknięć i niezgodności w statycznej kontroli.
- Brak niedozwolonych form `\mathbf{1}`, `\mathbb{1}`, `\mathds{1}` w R01.
- **Nowy test skończonych modeli (PASS, 7 przypadków):** dla `n=1,\ldots,7` oraz ośmioelementowego uniwersum wyliczono wszystkie sumy bloków podziału `\{\{1\},\ldots,\{n\},\{n+1,\ldots,8\}\}` (dla `n=7` ostatni blok jest singletonem) i porównano je z rodziną podzbiorów, które albo zawierają cały ogon, albo są z nim rozłączne. W każdym z siedmiu przypadków otrzymano identyczne rodziny. To skończony test konstrukcji, a nie dowód przypadku nieskończonego; ten podano w tekście.
- Dla poprzedniego commita `3ffb542ce3385c01630a4daff9c7dffa0975fdd0` oba przebiegi CI zakończyły się sukcesem (`Polish mathematical terminology` oraz `Mathematical library application checks`). Dla **nowego** commita `c426ca4e...` oba przebiegi były **queued** podczas sprawdzenia: [terminologia](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45090419040), [aplikacja](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45090419038). Nie zaliczać ich przed zakończeniem.
- **Nie uruchomiono pełnego `pdflatex` ani nie obejrzano aktualnego PDF.** Nie twierdzić, że pełna kompilacja lub audyt wizualny przeszedł. Brak rysunków wymagających oceny wizualnej w tym rozdziale.

## Stabilizacja

**R01 — nadal nieustabilizowany.** W audycie IV pojawiła się nowa poprawka; wymagany jest kolejny niezależny czysty audyt całego R01 po tym commitcie, a także pełna kompilacja i kontrola PDF. R02 nie był audytowany w tym przebiegu. Nie przechodzić do R02 przed spełnieniem kryteriów stabilności R01.

## Następny krok

Pobrać najnowszy blob R01 i historię raportów; ponownie zbadać wszystkie dowody i przykłady, szczególnie nowo rozwinięty argument o rosnącej sumie σ-algebr, sprawdzić zakończenie dwóch przebiegów CI, przeprowadzić pełną kompilację aktualnego dokumentu i wizualną kontrolę PDF. Po ewentualnej poprawce rozpocząć niezależny audyt od nowa; bez nowych usterek odnotować czysty audyt, nie deklarując stabilności bez kontroli technicznej.
