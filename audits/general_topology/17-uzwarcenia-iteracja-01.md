# Topologia ogólna — rozdział 17, audyt iteracja 01

Data: 2026-11-22; gałąź: `biblioteka-matematyczna-iteracja-6`.
Źródło: `chapters/pl/general_topology/17-uzwarcenia-aleksandrowa-i-cecha-stonea.tex`.
Status: **W AUDYCIE** (nie oznaczać stabilności po pierwszej kontroli).

## Zawartość i integracja

Rozdział obejmuje dwie konstrukcje: uzwarcenie Aleksandrowa niezwartych przestrzeni lokalnie zwartych Hausdorffa oraz uzwarcenie Čecha–Stone’a przestrzeni Tychonoffa. Przeprowadzono szczegółowe dowody topologii i zwartości, kryterium Hausdorffowości, własności przedłużania odwzorowań właściwych, minimalności i jednoznaczności uzwarcenia jednopunktowego, funkcjonalnej konstrukcji `βX`, własności uniwersalnej, przedłużania funkcji ograniczonych, maksymalności oraz porównania na przykładzie dyskretnej przestrzeni N.

Zintegrowano pliki: `books/pl/general_topology_ch17.tex`, `books/pl/general_topology.tex`, `catalog/books.json`, `docs/pl/plan_topologii_ogolnej.md`, `.github/workflows/general-topology-chapter.yml`; utworzono `tools/tests/test_general_topology_ch17.py`. Test rozdziału 16 uniezależniono od dokładnej liczby rozdziałów, zachowując sprawdzanie jego pozycji w książce.

## Audyt dowodów

1. **Topologia Aleksandrowa:** rodziny otwartych zbiorów X oraz dopełnień zwartych podzbiorów X są zamknięte na skończone przecięcia i dowolne sumy; dla dowolnych rodzin zwartych C_i ich niepuste przecięcie jest zwarte dzięki domkniętości w ustalonym zwartym C_j, zaś przy sumach mieszanych `C\setminus U` jest zwarte. Hausdorffowość X jest użyta do domkniętości zwartych zbiorów.
2. **Zwartość i gęstość:** otwarte pokrycie zawiera zbiór obejmujący ∞, a jego dopełnienie jest zwarte w X; skończone podpokrycie tego dopełnienia wraz z otoczeniem ∞ pokrywa X*. Niezwartość X gwarantuje gęstość X (∞ nie jest izolowany).
3. **Kryterium Hausdorffa:** lokalna zwartość zapewnia dla x otwarte U o zwartym domknięciu C. Wtedy U i X*\C rozdzielają x od ∞. Odwrotnie otwarta podprzestrzeń zwartej przestrzeni Hausdorffa jest lokalnie zwarta (wynik rozdziału 14).
4. **Odwzorowania właściwe:** `f*:X*→Y*` o ustalonych wartościach na X i w ∞ jest ciągłe wtedy i tylko wtedy, gdy przeciwobrazy zwartych C⊂Y są zwarte w X. W obie strony wykorzystuje się opis otoczeń ∞ i domkniętość zwartych w Hausdorffa Y*. Nie korzysta się z niejawnego założenia surjektywności f.
5. **Minimalność:** dla dowolnego uzwarcenia (K,e) przestrzeni lokalnie zwartej X dowiedziono, że e(X) jest otwarty w K: otwarte O o `O∩e(X)=e(U)` zawiera się w domknięciu e(U), a to w domkniętym, zwartym e(C)⊂e(X). Następnie całą resztę K\e(X) zwija się do ∞. Ciągłość sprawdzono na obu typach otwartych zbiorów X*. Jednoznaczność wynika z gęstości e(X). Przy jednopunktowej reszcie mapa jest bijekcją, więc homeomorfizmem.
6. **Lokalnie zwarte Hausdorffa ⇒ Tychonoff:** osobny lemat: przy x i domkniętym F wybiera się W o zwartym domknięciu C⊂X\F; lemat Urysohna w C oddziela x i C\W, a funkcję skleja się z funkcją zerową na domkniętym X\W. Dostaje się funkcję oddzielającą x od F, z pełnym uzasadnieniem ciągłości.
7. **Własność uniwersalna βX:** dla `f:X→L` do zwartej przestrzeni Hausdorffa `e_L(L)` jest domknięty w kostce `[0,1]^{C(L,[0,1])}`. Odwzorowanie współrzędnych `Φ(z)_g=z_(g∘f)` jest ciągłe. Obraz gęstej e_X(X) leży w e_L(L), więc obraz całej βX również; stąd przedłużenie `e_L^{-1}∘Φ` jest poprawne i jednoznaczne.
8. **Przedłużanie funkcji ograniczonych:** sprowadzenie do przedziału zwartego [a,b] jest dopuszczalne, również w przypadku funkcji stałej; nie potrzeba zupełności ani metryzowalności X.
9. **Maksymalność:** każde uzwarcenie K jest zwartą przestrzenią Hausdorffa, więc własność uniwersalna daje jedyny ciągły czynnik βX→K; zwarty obraz zawierający gęste e(X) zapewnia surjektywność. Jeśli wszystkie funkcje X→[0,1] przedłużają się do K, równości współrzędnych po złożeniu z czynnikiem dowodzą jego iniektywności. Otrzymujemy homeomorfizm zgodny z zanurzeniami.
10. **Porównanie i przykłady:** αX jest najmniejsze, βX największe w porządku z rozdziału 16; dla dyskretnej N funkcja naprzemienna nie przedłuża się do αN, lecz przedłuża się do βN. Przykład prostej z okręgiem jest zgodny z konstrukcją Aleksandrowa i nie używa jednoznaczności granic bez jej hipotez.

## Testy i skład

Zastosowano testy etykiet, domknięcia odsyłaczy i poprawności struktury LaTeX oraz skończone modele operacji na dopełnieniach zbiorów skończonych i separację punktów funkcjami charakterystycznymi w skończonej przestrzeni dyskretnej. Takie testy są kontrolą regresji, a nie formalnym dowodem nieprzeliczalnych przypadków.

Workflow dla źródła z pełnymi dowodami i testem:
https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45013696240

Workflow [45013696240](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45013696240) dla kompletnego rozdziału, wniosku o jednoznaczności uzwarcenia jednopunktowego i testu: **completed/success**, bez nieudanych kroków. Pobierano artefakt `14751001466`, zawierający samodzielny `general_topology_ch17.pdf` (**5 stron A4**) oraz log. Sprawdzono logi samodzielnego rozdziału i całej książki: brak `Overfull`, `Underfull`, `Missing character`, `LaTeX Warning`, `Undefined control sequence` i `Fatal error`. Wyrenderowano i skontrolowano wszystkie pięć stron PDF: brak kolizji, ucięć wzorów i problemów z czcionkami. Ostatnia strona jest krótsza, lecz czytelna, i nie wymaga sztucznego uzupełniania.

| Element | Status |
| --- | --- |
| Matematyczna kontrola konstrukcji Aleksandrowa | PASS — audyt 01 |
| Matematyczna kontrola konstrukcji Čecha–Stone’a | PASS — audyt 01 |
| Własności uniwersalne, minimalność, maksymalność | PASS — audyt 01 |
| Terminologia, założenia i przykłady | PASS — audyt 01 |
| Testy i CI / logi / kontrola PDF | **PASS — run 45013696240; PDF 5 stron** |
| Stabilizacja | **W AUDYCIE — wymagana niezależna iteracja 02** |
