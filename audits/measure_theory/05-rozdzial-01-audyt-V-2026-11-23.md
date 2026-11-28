# Teoria miary / Miara i całka — audyt V, wyłącznie rozdział 01

Data: 2026-11-23. Gałąź: `biblioteka-matematyczna-iteracja-6`. Plik: `chapters/pl/measure_theory/01-rodziny-zbiorow-i-przestrzenie-mierzalne.tex`. **Wynik: pierwszy czysty audyt po poprawce z audytu IV; brak nowych zmian w źródle; stabilizacja NIEZATWIERDZONA (brak pełnej kompilacji i przeglądu PDF).**

## Stan i proweniencja

Przed pracą pobrano bieżący HEAD gałęzi (w chwili pierwszego odczytu `296a15693c98a822d8d9bd9deea5d566a92b1699`), spis raportów w `audits/measure_theory/` i najnowszy raport `04-rozdzial-01-audyt-IV-2026-11-23.md`. Raport IV opisuje uzupełnienie dowodu identyfikacji rosnącej sumy σ-algebr z algebrą zbiorów skończonych i kofinitywnych, commit `c426ca4e24462ae009bfff2e76a0f7e72837858c`. Ponownie pobrano pełne źródło R01: blob `a7c8610bf1eb9e4612e96df9f038679af4d4d2fb`, 537 linii. Odczytano `AGENTS.md`, `docs/pl/standardy_terminologiczne.md` i plik główny książki. Innych rozdziałów nie audytowano; R02 wykorzystano jedynie jako kontekst istniejącego odsyłacza.

## Niezależna kontrola matematyczna

Przejrzano kolejno sześć sekcji: (1) pierścienie, algebry i σ-algebry; (2) generowanie, przekroje, ślad i pułapkę rosnącej sumy; (3) układy π, układy Dynkina, lemat i twierdzenie π–λ; (4) klasy monotoniczne i ich twierdzenie; (5) borelowskie generatory na R i R^d; (6) mierzalność, kryteria przez generatory, złożenia i działania na funkcjach rzeczywistych. **Nie wykryto nowej nieprawdziwej tezy ani nowej luki wymagającej poprawki.**

Szczególna kontrola sceptyczna:
- W przykładzie `\mathcal F_n=\sigma(\{\{1\},\ldots,\{n\}\})` atomami podziału są pierwsze `n` singletonów i nieskończony ogon. Zatem element `\mathcal F_n` jest sumą wybranych singletonów, ewentualnie z całym ogonem; jest odpowiednio skończony lub kofinitywny. Każdy zbiór skończony/kofinitywny występuje w pewnym `\mathcal F_n`, ponieważ jego skończona część/dopełnienie jest ograniczona w N. Obie inkluzje są poprawne.
- W twierdzeniu π–λ sprawdzono, że rodziny pomocnicze `\mathcal L_A` i `\mathcal K_B` zawierają `X`, są zamknięte na różnice zbiorów zagnieżdżonych i rozłączne sumy; dwukrotne użycie minimalności układu Dynkina jest uprawnione.
- W twierdzeniu o klasie monotonicznej rodziny pomocnicze są klasami monotonicznymi; dopełnienia wymieniają granice rosnące i malejące, a sumy z ustalonym zbiorem zachowują oba typy granic. Domknięcie na skończone sumy i następnie na sumy przeliczalne jest uzasadnione.
- Generatory borelowskie: przeliczalna baza przedziałów/prostokątów wymiernych i obrazy odwrotne rzutów uzasadniają wszystkie wskazane inkluzje; kryterium mierzalności działa przez σ-algebrę obrazów odwrotnych.
- Kontrprzykłady: rodzina skończono-kofinitywna na N, układ Dynkina na czterech punktach i nieciągłość `\chi_{\mathbb Q}` są poprawne. Rozdział nie zawiera rysunków.

## Kontrola strukturalna i CI

Bezpośrednio wykonano ponowne statyczne sprawdzenie bieżącego bloba: 19 etykiet, 0 duplikatów, 12 odsyłaczy, z których 10 ma cele w R01, a 2 odnoszą się do `ch:miary-wlasnosci` w R02; 43 poprawnie zagnieżdżone pary środowisk; 0 niedomknięć; brak `\mathbf{1}`, `\mathbb{1}`, `\mathds{1}` i niepożądanej nazwy „zbieżność zdominowana”. Istniejące etykiety i odsyłacze nie zostały zmienione.

Dla commita poprawki IV `c426ca4e24462ae009bfff2e76a0f7e72837858c` oba przebiegi GitHub Actions zakończyły się **success**: [Polish mathematical terminology](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45090419040) i [Mathematical library application checks](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45090419038). Nie należy utożsamiać tych workflow z pełną kompilacją książki.

**Nie wykonano pełnej kompilacji PDF ani kontroli wizualnej aktualnej książki.** Lokalny kontener ma `pdflatex`, ale bezpośredni `git ls-remote` nie zadziałał z powodu błędu DNS dla `github.com`, a pełny projekt nie był dostępny w kontenerze. Nie przypisywać temu audytowi nieuruchomionych testów ani kontroli PDF.

## Status i następny krok

**R01: matematycznie i statycznie czysty audyt V po ostatniej poprawce, ale status formalny „niestabilny” do zakończenia pełnego buildu i kontroli PDF.** W następnym przebiegu nadal kontrolować tylko R01, pozyskać komplet źródeł do rzeczywistej kompilacji, sprawdzić wynik i wygląd PDF oraz przeprowadzić niezależny końcowy przegląd. Dopiero po spełnieniu wszystkich kryteriów oznaczyć R01 jako stabilny i w następnej iteracji przejść do R02. Nie scalano skryptów ani nie zmieniano źródeł rozdziałów.
