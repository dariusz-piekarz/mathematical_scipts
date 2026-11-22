# Algebra liniowa — rozdział 30, niezależny audyt korekcyjny (03; 2026-11-22)

**Gałąź:** \`biblioteka-matematyczna-iteracja-6\`; **rozdział:** 30 „Algebry Clifforda”, 308 wierszy. **Wynik:** NIE-CZYSTY; poprawki w źródle, reset do **0/2** na nowym blobie. Dodatkowy audyt końcowy: NIE. Status: OTWARTY.

## Wersje i wyścig równoległy

- Początkowy HEAD: \`667360836caa2ccbfe0efe9cb6b5c5a4721ee34e\`. HEAD bezpośrednio przed zapisem: \`860a3bae93082060c9c478796ff0931fbba95202\`.
- Źródło przed zmianą: \`chapters/pl/linear_algebra/30-algebry-clifforda.tex\` blob \`7a0a02da8836336cb43df52e4dc41d6697600bd4\`.
- Źródło po zmianie: blob **\`6d90013dd6c66d347e5ae2ac78b4c1a194aa979e\`**. Commit źródłowy: [f629b926](https://github.com/dariusz-piekarz/mathematical_scipts/commit/f629b926d93d76f7d09018feeb0c4c06c847f928).
- Raporty [30_iteration_01_2026-11-22.md](30_iteration_01_2026-11-22.md) i [30_iteration_02_2026-11-22.md](30_iteration_02_2026-11-22.md) pojawiły się na gałęzi **równolegle** po rozpoczęciu obecnej pracy. Oba dotyczą **starego bloba** i nie mogą być zaliczone jako czyste kontrole po tej korekcie. Nie nadpisywano ich ani nie usuwano.

## Przeprowadzony pełny audyt

Przed rozpoczęciem pobrano HEAD, \`AGENTS.md\`, \`docs/pl/standardy_terminologiczne.md\`, \`books/pl/linear_algebra.tex\`, katalog 01–32, rzeczywisty pełny tekst LA-30, katalog audytów i postęp. Zweryfikowano definicje i odsyłacze do LA-11 oraz standard szczegółowości z rozdziału 01 geometrii różniczkowej.

Przeczytano cały LA-30, krytycznie sprawdzono iloraz \`T(V)/I_q\`, \`Z/2Z\`-stopniowanie, dowód antykomutacji przez polaryzację, własność uniwersalną, poprawność redukcji słów, niezależność uporządkowanych monomów przez reprezentację na \`ΛV\`, znak i dobrze określoną kontrakcję \`ι_v\`, wymiar \`2^n\`, przypadek \`n=0\`, bazę parzystą/nieparzystą, antysymetryzację, przykłady \`Cl(R)≅C\`, \`Cl(R²)≅H\`, rozkład iloczynu dwóch wektorów i schemat geometryczny. Nie wykryto błędu matematycznego w tych obliczeniach ani koła logicznego.

### Wykryte i faktycznie poprawione usterki

1. Stwierdzenie \`prop:lin30-cliff-wedge\` miało niejawnie przyjęte wektory \`v,w\`. Dodano jawne „Dla dowolnych \`v,w∈V\`” oraz odsyłacz do istniejącego izomorfizmu \`rem:lin30-cliff-zewnetrzna\`. Wszystkie \`\\label\` zachowano.
2. W oryginalnym rysunku \`fig:lin30-cliff-iloczyn\` długi podpis wewnątrz równoległoboku przecinał pionową linię przerywaną i prawą krawędź. Skrócono tekst wewnątrz do \`u∧v\` i przesunięto punkt osadzenia na \`(3.2,1.25)\`. Wzór na iloczyn Clifforda pozostaje w tekście i podpisie rysunku.

### Testy rzeczywiste

| Kontrola | Wynik |
|---|---|
| Algorytm bitowy Clifforda, dokładne testy Python (skrypt lokalny \`/mnt/data/la30_audit/test_clifford.py\`) | **43 921 PASS, 0 FAIL**: łączność, tablica działania na bazie algebry zewnętrznej, antykomutatory, kwadraty wszystkich wektorów całkowitoliczbowych z zakresu −2,…,2 w wymiarach 1–5 i przykłady |
| Integralność TeX sprzed zmiany | **11 unikalnych etykiet**, 11 odsyłaczy (zewnętrzne sprawdzono w LA-11), 14 zagnieżdżonych poprawnie par środowisk, 1 rysunek |
| Terminologia | Nie wykryto zakazanych form „unia”, samodzielne „dual”, „tensorowanie”, „sekwencja”, „rozszczepia” dla wielomianu, „karta” dla chart |
| PDF sprzed korekty | Pobierano rzeczywisty ZIP pełnej książki z [CI 45038590196](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45038590196), zawierający **stary identyczny blob**. Obejrzano strony fizyczne 293–295 i powiększenie rysunku, wykryto kolizję |
| Nowy sam rysunek | **Lokalny pdflatex PASS**, render PNG obejrzany, brak kolizji. Nie jest to pełny PDF źródła po korekcie |
| CI nowego bloba | [45039090215](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45039090215) dla commitu \`f629b926…\`: **in_progress przy ostatnim odczycie**, zatem NIE deklarować CI success |

## Decyzja i kontynuacja

**Status LA-30: OTWARTY; czyste kontrole po poprawce 0/2; osobny końcowy audyt: NIE.** Następny rzeczywisty przebieg ma wykonać niezależny pełny audyt poprawionego bloba \`6d90013dd6c66d347e5ae2ac78b4c1a194aa979e\` i sprawdzić zielone CI dokładnie dla niego. Po dwóch kolejnych czystych audytach i właściwym CI przeprowadzić jeszcze trzeci oddzielny sceptyczny audyt. Nie przechodzić do LA-31.
