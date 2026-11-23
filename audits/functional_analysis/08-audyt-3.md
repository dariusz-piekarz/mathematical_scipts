# Analiza funkcjonalna — rozdział 08 — audyt 03 (kontrola niezależna)

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/functional_analysis/08-pary-dualne-i-topologie-slabe.tex`.  
**Blob SHA źródła:** `a01d4316fdeacef759c89955b14bc062abedbcd4` (niezmieniony od audytów 08/01–08/02).

## Kontrola stanu

Przed rozpoczęciem odczytano katalog raportów i stwierdzono istnienie 08/01 i 08/02, ale brak 08/03. Odczytano oba raporty, całe źródło rozdziału i plik 17 testów. Raport 08/02 dokumentuje 1/2 czystych przeglądów, a 08/01 wcześniejsze poprawki. Nie rozpoczynano rozdziału 09.

## Przegląd matematyczny (12 dowodów, 5 przykładów)

Ponownie przeanalizowano wszystkie 12 argumentów: konstrukcję topologii początkowej i kryterium sieciowe; ograniczoność słabą; reprezentację funkcjonałów ciągłych przez skończony układ; inkluzję topologii; domknięcie podprzestrzeni przez anihilator; brak ograniczonych otoczeń; słabe domknięcie sfery; porównanie słabej i słabej-*; zupełność algebraicznej przestrzeni sprzężonej z topologią punktową i gęstość kanonicznego obrazu; niezupełność nieskończenie wymiarowej przestrzeni unormowanej ze słabą topologią; topologię silną na E'; seminormy Mackeya.

W szczególności:
- Argument o gęstości `J(E)` w `F^*` prawidłowo wykorzystuje surjekcję `E→G^*` dla skończenie wymiarowego `G⊂F`, wynikającą z niezdegenerowania parowania.
- Niezupełność nie jest wnioskowana z zachowania ciągów; dowód używa nieciągłego algebraicznego funkcjonału i skierowanej sieci po skończenie wymiarowych podprzestrzeniach `E'`.
- Definicja topologii Mackeya wykorzystuje **absolutnie wypukłe słabo zwarte** podzbiory `F`; dowód skończoności seminorm i własności Hausdorffa jest poprawny. Nie przedstawia się twierdzenia Mackeya–Arensa jako udowodnionego.
- Przypadki zerowego wymiaru i przestrzeni zespolonych nie ujawniają sprzeczności z założeniami.

Wszystkie **12/12 dowodów i 5/5 przykładów** przechodzą ten niezależny przegląd tekstowy; nie oznacza to formalnego dowodu komputerowego.

## Rzeczywista poprawa testu

W `tools/tests/test_functional_analysis_ch08.py` wykryto wcześniej odnotowaną słabość: tautologię `values[j] == values[j]`. Zastąpiono ją testem dokładnej interpolacji na wszystkich 16 podzbiorach czteroelementowego zbioru indeksów, z kontrolą zgodności dla każdej inkluzji `G⊂H` i stabilizacji na ogonach skierowanego zbioru. Obliczenie modelu z `fractions.Fraction` przeszło lokalną kontrolę. Zmiana nie dotyczy źródła matematycznego, lecz testu; commit `702b871236ddaa6f3ab8c16cddd123547a8dc2c9`.

## CI i PDF — stan uczciwie rozdzielony

Audyt 08/01 dokumentuje ukończone z sukcesem CI `45196353669`, 17 testów, kompilację książki i wizualną kontrolę stron 43–48. Audyt 08/02 dokumentuje ukończone CI `45197404525` dla tego samego SHA źródła. Dla **nowego commita testu** `702b871236ddaa6f3ab8c16cddd123547a8dc2c9` wywołanie API `fetch_commit_workflow_runs` zwróciło pustą listę; nie wolno przypisać mu zielonego CI. W tej iteracji nie pobierano ani nie renderowano ponownie PDF.

## Werdykt

**Matematyka i redakcja źródła: audyt 08/03 czysty, drugi kolejny czysty przegląd tej samej wersji (2/2).** W testach wykonano realną poprawkę, lecz bez zmiany źródła rozdziału. **Stabilizacja techniczna pozostaje warunkowa:** trzeba potwierdzić ukończony CI na commicie zawierającym nowy test, w szczególności uruchomienie 17 testów i kompilację LaTeX. Nie ogłaszać jeszcze ostatecznej stabilności i nie otwierać 09.

## Uzupełnienie po zakończeniu CI — zamknięcie stabilizacji 08

Po sporządzeniu raportu ustalono przyczynę błędu GitHub Actions dla wcześniejszego testu: użyto asercji wyszukującej dwa dosłowne znaki ukośnika odwrotnego przed `mathcal G`, podczas gdy rzeczywisty LaTeX zawiera pojedynczy ukośnik. Była to **usterka testu**, nie błąd rozdziału. Poprawiono ją w commicie [`3a56f12ffc03053cef9e203925de2bacd6f5db88`](https://github.com/dariusz-piekarz/mathematical_scipts/commit/3a56f12ffc03053cef9e203925de2bacd6f5db88). Dodana w audycie 08/03 rzeczywista próba interpolacji na wszystkich 16 podzbiorach i kontrola zgodności na ogonach pozostały bez zmian.

Dedykowany [GitHub Actions **#45206271068**](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45206271068) dla poprawionego testu zakończył się statusem **SUCCESS** (uruchomiony na commicie `3a56f12ffc03053cef9e203925de2bacd6f5db88`). Poszczególne etapy: **17 testów regresyjnych PASS**, przygotowanie kontekstu LaTeX 01–08 PASS, kompilacja LaTeX PASS, kontrola PDF i odsyłaczy PASS oraz publikacja artefaktu PASS. Nie oznacza to nowej wizualnej inspekcji PDF (ta została udokumentowana w 08/01), lecz potwierdza kompilację i automatyczne kontrole bieżącej wersji.

SHA źródła rozdziału 08 pozostaje **`a01d4316fdeacef759c89955b14bc062abedbcd4`**. Audyty 08/02 i 08/03 są dwoma następującymi po sobie **czystymi przeglądami matematycznymi tej samej wersji**. Korekta dotyczyła wyłącznie kodu testu, który jest już objęty zielonym CI.

**Ostateczny werdykt: rozdział 08 STABILNY — 2/2 czystych audytów + zielony CI. Wolno rozpocząć audyt rozdziału 09.**
