# Analiza funkcjonalna — rozdział 09 — audyt 01 (kontrola matematyczna, redakcyjna i CI)

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/functional_analysis/09-banach-alaoglu-krein-milman-i-topologia-mackeya.tex`.  
**Blob SHA przed poprawkami:** `aa172dd7cac7e0687c4dc75eb85bc0443bed7fee`.  
**Blob SHA po poprawkach:** `b633df1875b710c361912a39bee277b11eca26e5`.  
**Werdykt:** **Z POPRAWKAMI — nieczysty, stabilizacja 0/2**. Rozdział 10 nie może jeszcze wejść do audytu stabilizacyjnego.

## Zakres i sposób oceny

Odczytano całe źródło rozdziału 09 oraz źródła 01–08 istotne dla założeń i odsyłaczy. Niezależnie skontrolowano **14 dowodów, 8 przykładów, definicje, uwagi i jeden rysunek TikZ**. W przypadku twierdzenia Banacha–Alaoglu sprawdzono brak założenia Hausdorffa i lokalnej wypukłości; przy metryzowalności rola ośrodkowości i równociągłości; przy twierdzeniu Kreina–Milmana zwartość niepustych ścian i właściwe oddzielanie przez funkcjonały; przy twierdzeniu Mackeya–Arensa zgodność topologii z parą dualną oraz lemat dominacji; przy kryterium interpolacji możliwość powtarzania indeksów i przypadek promienia zero. Testy skończenie wymiarowych modeli nie zastępują tych dowodów.

## Kontrola wszystkich 14 dowodów

1. **Równociągłość i polary:** równoważność `H⊂U°` z równociągłością wynika ze skalowania `U`; pochłanianie otoczenia daje punktową ograniczoność `H`. PASS.
2. **Banach–Alaoglu–Bourbaki:** dla dowolnej TVS wartości `f(x)` w polarnym zbiorze są jednostajnie ograniczone dzięki pochłanianiu `U`; umieszczenie `U°` w produkcie dysków i zamkniętość warunków liniowości oraz nierówności daje zwartość przez Tychonowa. Funkcja spełniająca ograniczenia jest ciągła po skalowaniu `U`. PASS.
3. **Słabo-* zwarta kula:** dla `R>0` polar normowej otwartej kuli promienia `1/R` to `B'_R`; dla `R=0` pozostaje zwarty singleton. PASS.
4. **Domknięty podzbiór kuli:** dziedziczenie zwartości przez domknięty podzbiór zwartej przestrzeni. PASS.
5. **Metryzowalność na rodzinie równociągłej:** odczyty na przeliczalnym gęstym zbiorze rozdzielają funkcjonały; równociągłość pozwala przenieść ciągłość wartościowania z gęstego zbioru na całe `E`. PASS.
6. **Kryterium ośrodkowości normowanej `E`:** w kierunku wprost rodzina `B'_{E'}` jest równociągła; odwrotnie przeliczalna baza otoczeń zera w metryzowalnej słabo-* kuli daje przeliczalny układ wektorów, których rozpiętość jest gęsta przez Hahna–Banacha. PASS.
7. **Ściana poziomicy maksymalnej:** niepustość i zwartość wynikają z maksimum ciągłego funkcjonału na zwartym `K`; warunek ekstremalności poziomicy jest wnioskiem z liniowości; przechodniość ścian jest poprawna. PASS.
8. **Istnienie punktu ekstremalnego:** łańcuch niepustych domkniętych ścian ma niepuste przecięcie przez zwartość; Zorn daje minimalną ścianę, a oddzielenie dwóch jej punktów prowadzi do właściwej mniejszej ściany. PASS.
9. **Krein–Milman:** gdy domknięta otoczka wypukła punktów ekstremalnych nie pokrywa `K`, ścisłe oddzielenie pozwala skonstruować zwartą ścianę maksymalną z punktem ekstremalnym łamiącym nierówność. PASS.
10. **Zasada maksimum Bauera:** zbiór maksimów wypukłej, półciągłej z góry funkcji jest domknięty i ma własność ekstremalności; minimalizacja takich podzbiorów przez Zorna daje ekstremalny punkt maksimum. PASS.
11. **Lemat dominacji przez `p_K`:** skończone projekcje `T_S(K)` są zwarte i absolutnie wypukłe; silne oddzielenie i zrównoważenie prowadzą do sprzeczności z `|g|≤p_K`. Własność skończonych przecięć daje reprezentację elementem `K`. PASS.
12. **Mackey–Arens:** funkcjonał ciągły dla `τ(E,F)` jest dominowany seminormą pewnej zwartej absolutnie wypukłej sumy Minkowskiego, więc reprezentowany przez `F`. Każda ciągła seminorma topologii zgodnej `ρ` równa się supremum po polarnym słabo zwartym `K_p` przez Hahn–Banacha, skąd `ρ⊂τ(E,F)`. PASS.
13. **Ekstremalne topologie zgodne z parowaniem:** minimalność `σ(E,F)` pochodzi z definicji topologii początkowej, maksymalność `τ(E,F)` z poprzedniego twierdzenia. PASS.
14. **Kryterium interpolacji z dowolnie wieloma warunkami:** nierówność na kombinacjach zapewnia jednoznaczne zadanie `g_J` na skończonym rozpięciu i kontrolę normy; Hahn–Banach + zwartość `B'_R` + własność skończonych przecięć umożliwiają równoczesne spełnienie wszystkich warunków. PASS.

## Kontrola 8 przykładów

1. Kula `ℓ¹` jako słabo-* zwarta, lecz nie zwarta w normie. PASS.
2. Nieprzeliczalny produkt dysków i sieć skończonych nośników, której nie może zastąpić ciąg. PASS.
3. Słabo-* zwarty, lecz nierównociągły zbiór `{0}∪{n·e_n^*}` na niezupełnej przestrzeni `c_{00}`. PASS.
4. **Wielokąt i kula Hilberta: NIEPOPRAWNE ZAŁOŻENIE W PIERWOTNYM TEKŚCIE.** Sformułowanie „nieosobliwy wielokąt” nie wymusza wypukłości, natomiast twierdzenie o punktach ekstremalnych odnosi się do zbiorów wypukłych. **Poprawiono** na „wypukły wielokąt o niepustym wnętrzu” i zachowano argument o ściśle wypukłej kuli Hilberta. PASS po zmianie.
5. Produkt przedziałów `[-1,1]^I` i charakterystyka punktów ekstremalnych poprzez współrzędne `±1`. PASS.
6. Słabo-* zwarta kula rzeczywistej `ℓ¹` i jej punkty ekstremalne `±e_n`. PASS.
7. Ścisła inkluzja topologii słabej w Mackey na nieskończenie wymiarowej przestrzeni Banacha. PASS.
8. Przedłużenie z wartości na współrzędnych w `ℓ¹`, równoważne ciągowi `b∈ℓ∞`. PASS.

## Korekty i powiązania

- Poprawiono brak niezbędnej hipotezy **wypukłości wielokąta** w przykładzie dotyczącym punktów ekstremalnych; wcześniej teza mogła być fałszywa.
- Uporządkowano terminologię: **przestrzeń sprzężona / przestrzeń algebraicznie sprzężona** zamiast niejednolitych określeń, oraz **zwartość ciągowa** zamiast sformułowań z „sekwencyjny”.
- W przykładzie sieci skończonych nośników zastosowano notację **`\\chi_F`**, bez zmiany treści przykładu.
- Doprecyzowano uwagę o zwartości produktu nieprzeliczalnego, oddzielając rolę twierdzenia Tychonowa od własności ciągów.
- Zachowano wszystkie istniejące etykiety i odsyłacze; nie rozszerzano zatwierdzonego zakresu rozdziału o nowe twierdzenia.

## Rzeczywiste kontrole strukturalne i regresyjne

Na pobranych źródłach 01–09 po poprawkach niezależnie zliczono: **14 par środowisk `proof`, 8 przykładów, 23 etykiety rozdziału 09 i 14 odsyłaczy**. Jest **0 nieistniejących celów odsyłaczy** i **0 duplikatów etykiet** w całym kontekście 01–09.

Utworzono `tools/tests/test_functional_analysis_ch09.py` z **18 testami**: spójność książki, liczba środowisk, etykiety/odsyłacze, polska terminologia, hipoteza wypukłości wielokąta, polary i równociągłość, modele Banacha–Alaoglu, metryka z odczytów, sieć po skończonych nośnikach, kontrprzykład na `c_{00}`, przykłady Hilberta i `ℓ¹`, lemat dominacji, rekonstrukcja seminormy Mackeya, interpolacja z powtarzaniem indeksów, promień `R=0`, rysunek TikZ.

Utworzono też `.github/workflows/functional-analysis-ch09.yml`, uruchamiający testy, budowę kontekstu LaTeX 01–09, kompilację PDF, automatyczną kontrolę odsyłaczy i artefaktu. W przebiegu [CI #45207624031](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45207624031) **wszystkie 18 testów, przygotowanie kontekstu 01–09, kompilacja LaTeX, kontrola PDF i odsyłaczy oraz publikacja artefaktu przeszły pomyślnie (SUCCESS)**. Dodatkowo pobrano rzeczywisty artefakt PDF tego przebiegu i przeprowadzono niezależną inspekcję stron 48–55, obejmującą rysunek TikZ na stronie 51.

## Propozycje uzupełnień, niewprowadzone do źródła

1. Po twierdzeniu o słabo-* metryzowalnej kuli przydatna byłaby krótka osobna uwaga o różnicy między zwartością ciągową a własnością Frécheta–Urysohna dla topologii niemetryzowalnych (opcjonalne).
2. Można rozważyć osobny diagram obrazujący różnicę między domkniętą otoczką wypukłą a skończoną otoczką wypukłą punktów ekstremalnych (opcjonalne). Każda taka rozbudowa wymaga uprzedniej zgody użytkownika.

## Decyzja

**Audyt 09/01: Z POPRAWKAMI (0/2)**. Najpierw potwierdzić końcowy sukces dedykowanego CI i wykonać niezależny przegląd 09/02 na niezmienionym źródle; dopiero dwa kolejne czyste audyty pozwolą przejść do rozdziału 10.

## Niezależna inspekcja PDF po zakończeniu CI

Pobrano oryginalny artefakt `functional-analysis-ch09-pdf` z [udanego CI #45207624031](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45207624031) (ID artefaktu `14833303556`). PDF ma **55 stron formatu A4**; rozdział 09 rozpoczyna się na **stronie 48**, a kończy na **stronie 55**. Dokument ma 640283 bajty. Wyrenderowano i obejrzano wszystkie **8 stron 48–55**, w szczególności rysunek z wielokątem i wspierającą poziomicą na stronie 51. Rysunek, podpis oraz sąsiadujące akapity nie nachodzą na siebie i nie zostały ucięte. Kontrola współrzędnych bloków tekstowych przez PyMuPDF wykazała **0 bloków poza granicami strony** na stronach 48–55. Automatyczna kontrola logu LaTeX i odsyłaczy zakończyła się sukcesem.

**Wynik techniczny: PASS. Werdykt matematyczno-redakcyjny 09/01 pozostaje Z POPRAWKAMI, 0/2 czystych audytów.** Następny etap to 09/02 na tym samym blob SHA źródła.
