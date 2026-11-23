# Teoria miary / Miara i całka — rozdział 04, audyt X (iteracja XXVI)

**Data:** 2026-11-23. **Gałąź:** biblioteka-matematyczna-iteracja-6 (istniejąca; bez tworzenia nowych).  
**Jedyny audytowany rozdział:** chapters/pl/measure_theory/04-miara-lebesguea-na-przestrzeni-euklidesowej.tex.  
**Blob źródła R04:** ce0105f63aa4da494cf5f2f5e9e2b26fc6389fd4 — źródło matematyczne w tej iteracji niezmienione.

## 1. Kontynuacja od rzeczywistego stanu

Przed pracą sprawdzono najnowsze commity gałęzi po poprzednim raporcie (commit ab6cc63c7ec77812b5056e508f570eeb556dadec), odczytano audyt XXV (plik 25-rozdzial-04-audyt-IX-2026-11-23.md, blob 90dcab69ab5f4ca8cb31e57d3b0b8c71d2f42992), R04 i workflow. Nie było raportu XXVI ani nowych zmian treści R04. Przyjęto dotychczasowy stan reguł AGENTS.md i docs/pl/standardy_terminologiczne.md. R01–R03 są wyłącznie kontekstem odsyłaczy, a R05–R31 nie były audytowane ani edytowane. Nie dokonano scalania, usuwania treści ani zmiany stabilnych etykiet.

## 2. Rzeczywisty, nieudany przebieg CI — diagnoza

Odkryto właściwą listę GitHub Actions dla zdarzeń push w API GitHub, zamiast wcześniej używanego ograniczonego endpointu przebiegów PR. Pobrano listę zadań i logi faktycznego przebiegu [45142563108](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45142563108) na commicie f70575a208603517fe91ac1f2420d613ff208f37.

- Job chapter-04-exact-geometry: SUCCESS.
- Job chapter-04-pdf-and-references: FAILURE, podczas analizy wydrukowanego izolowanego PDF; kompilacje pdflatex jednak zakończyły się sukcesem i wygenerowano prawidłowy PDF 10 stron.
- Konkretny wyjątek: xml.etree.ElementTree.ParseError, invalid token, linia 5585, kolumna 82 w ch04_bbox.html. Powodem okazały się dwa znaki sterujące U+0010 i U+0011 wyemitowane przez pdftotext -bbox w słowach ze znakami matematycznymi. XML 1.0 odrzuca te znaki niezależnie od poprawności LaTeX i PDF. Etap pełnej książki w tym przebiegu został pominięty.

Pobrano i lokalnie rozpakowano rzeczywisty artefakt runu 45142563108, ID 14801689751; obejmował prawdziwy PDF, bbox XHTML, tekst i logi.

## 3. Poprawka testu oraz weryfikacja po poprawce

W tools/test_measure_theory_ch04_pdf_layout.py zastąpiono bezpośrednie ET.parse odczytem XHTML do tekstu, wymianą wyłącznie niedozwolonych w XML 1.0 znaków C0 (U+0000–0008, U+000B, U+000C, U+000E–001F) na U+FFFD oraz ET.fromstring. Zachowano ramki słów i kontrolę pionowego odstępu podpisu od obu etykiet osi.

**Commit poprawki:** [b7bf59948d48a99f43035a807516af5a8a0bae4b](https://github.com/dariusz-piekarz/mathematical_scipts/commit/b7bf59948d48a99f43035a807516af5a8a0bae4b); **nowy blob skryptu:** 18446f7cb62f3a8f20c5f45de4a649d93321a653. Ponownie pobrano plik po zapisie i potwierdzono treść oraz SHA.

Z autentycznym bbox.xhtml pobranym z GitHub:
- pełny test **PASS: 10 stron, 5821 słów w obrębie strony, podpis Cantora odseparowany na stronie 7**;
- test mutacyjny **PASS jako test wykrywania usterek**: po przesunięciu w XHTML pierwszego słowa rzeczywistego podpisu o 22 punkty test odrzucił wadliwy układ z kodem wyjścia 1;
- po usunięciu dwóch niedozwolonych znaków cały XHTML prawidłowo parsuje się jako dokument zawierający dziesięć stron.

## 4. Ponowny przebieg CI: pełne 2/2 SUCCESS

Zmiana testu uruchomiła automatycznie [run 45143823731](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45143823731) na commicie b7bf59948d48a99f43035a807516af5a8a0bae4b. Sprawdzono faktyczne statusy jobów, ich kroków, rzeczywiste logi i artefakty:

1. **chapter-04-exact-geometry — SUCCESS.** Oba kroki testowe (arytmetyka wymierna oraz struktura źródła i współrzędne Cantora) zakończyły się sukcesem.
2. **chapter-04-pdf-and-references — SUCCESS.** Dwie rzeczywiste kompilacje pdflatex izolowanego R04, kontrola PDF 10 stron A4 i 5821 słów, odstępu podpisu Cantora na stronie 7, wygenerowanie i potwierdzenie dokładnie 10 podglądów PNG oraz trzykrotna rzeczywista kompilacja kompletnej książki i kontrola odsyłaczy.

**Wynik pełnej książki:** 256 stron A4. W końcowym logu brak nierozwiązanych referencji, błędów powielonych etykiet, ostrzeżeń LaTeX oraz przepełnionych wierszy. W całej książce jest 14 ostrzeżeń Underfull hbox; izolowany R04 ma ich 0 (i 0 Overfull hbox). Nie przypisujemy globalnych ostrzeżeń innych rozdziałów bez przeprowadzenia ich odrębnego audytu.

Pobrano artefakt nowego przebiegu **14803650991**. Potwierdzono fizycznie 10 osobnych PNG, izolowany PDF 10 stron, wygenerowany bbox XHTML i logi izolowanego R04 oraz pełnej książki. Kontrola 31 rozdziałów całej książki w tym punkcie dotyczy wyłącznie technicznej kompilacji i wzajemnych referencji, nie jest audytem matematycznym pozostałych rozdziałów.

## 5. Weryfikacja wizualna wszystkich stron R04

Pobrany 10-stronicowy PDF ze źródła R04 na tej samej wersji blob został wyrenderowany na wszystkie strony (1–10) i obejrzany w zbiorczym widoku; osobno w pełnym powiększeniu skontrolowano stronę 7 z diagramem Cantora. Podpis leży pod rysunkiem i oznaczeniami 0 i 1. Nie zaobserwowano widocznych kolizji tekstu i wypełnień TikZ. Sprawdzono obecność kolejnych sekcji od konstrukcji miary, przez regularność i Cantora, do Vitaliego oraz podsumowania. Automatyczny test położeń całych 5821 słów zakończył się sukcesem, a log izolowanego PDF nie ma problemów Overfull i Underfull.

Kontrola ramkowa nie zastępuje sprawdzenia każdej możliwej kolizji symboli; wizualnie najdokładniej zbadano najbardziej ryzykowną stronę z rysunkiem.

## 6. Decyzja i następny krok

**Status R04: TECHNICZNIE ZWERYFIKOWANY, ALE JESZCZE FORMALNIE NIESTABILNY.** Przebieg CI 2/2 zielony oraz autentyczna kontrola wszystkich 10 stron zamykają najpoważniejszą otwartą lukę techniczną. Przeglądy matematyczne po ostatniej zmianie treści R04 nie wykazały nowych usterek. Jednak w tej iteracji naprawiono test PDF, dlatego zgodnie z rygorem projektu nie nadaje się statusu stabilnego przed **jeszcze jednym, kolejnym niezależnym czystym audytem tego samego R04 po ostatniej poprawce technicznej**. Audyt ten ponownie obejmie matematyczne założenia i dowody, terminologię, źródła, odsyłacze i gotowy PDF.

**Następna iteracja: audyt XXVII, R04 XI. Nie przechodzić do R05 przed jawnym zatwierdzeniem R04.**
