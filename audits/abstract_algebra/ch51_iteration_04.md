# AA-51 — audyt IV: bramka typograficzna

Data: 24 listopada 2026 r. Gałąź: biblioteka-matematyczna-iteracja-6.

## Wynik poprzedniego CI
Run 45295683486 (ae70f8a654a77d220a9cb7e2695cec11a9594a4b), job 138115334419: failure w kroku Verify PDF and references (no undefined refs). Dedykowane testy AA-51 4/4 + 3/3 PASS; AA GLOBAL 01-51 SOURCE INTEGRITY PASS: 51 rozdziałów, 1054 unikatowe etykiety, 576 wystąpień odsyłaczy, zero brakujących i powielonych celów. Kompilacja PDF zakończyła się, ale końcowy log zawiera Overfull hbox 102.93979 pt, linie 290–298, przykład czworościanu i sześcianu. Wcześniejsze przebiegi kompilatora zawierały przejściowe ostrzeżenia o odsyłaczach; przyczyna końcowego błędu bramki to przepełnienie łamu. Artefakt tego runu 14876363993 nie stanowi zatwierdzonego PDF.

## Poprawka
Commit 5a43b83dcba946ada40fc541e84250e4fc6791f6, blob b8c68c540f6ddb3f4b1f2741385ed60af752e120. Zapis czterech wierzchołków czworościanu przeniesiono z jednego długiego wzoru w tekście do dwuwierszowego gathered. Analogicznie rozłożono dwie listy współrzędnych dwudziestościanu, aby zapobiec podobnemu problemowi. Treść matematyczna pozostaje bez zmian; bramka Overfull nie została osłabiona.

## Status
Run 45295903422 (db7c0bff485f6ce7ea88c3eaf84048d449712a24) przy odczycie nadal in_progress: 105 kroków success, jeden in_progress, pięć pending. Dotyczy wcześniejszego źródła, bez powyższej poprawki układu. Run najnowszego commita nie był jeszcze widoczny w pierwszym odczycie. Nie wykonano wizualnych oględzin najnowszego PDF. AA-51 W AUDYCIE, AA-52 nieotwarty. Następny krok: pełny CI po poprawce i kontrola finalnego PDF.