# Audyt 233 — drukowany rozdział 25, końcowa kontrola strukturalna

Data: 2026-11-25. Kontynuacja 232, bez rozszerzania treści.
Wersja badana: 8f5159ac558cb3d00ea695a972dbb7c3d80f3dbd. Źródło rozdziału 18-teoria-wezlow-od-diagramow-do-rozmaitosci-czterowymiarowych.tex, blob 08aa394e69c5136c3f0d1203329b9bff6aa48b99.

## Kontrola różnicowa
Porównano listy 44 nazw i blobów rozdziałów między wersją z pomyślnym globalnym CI fcce40f7b25b4aa8db9b7f75974a2986330d33dc i badaną wersją; tylko plik 18 uległ zmianie, pozostałe 43 są identyczne. Wszystkie 44 bloby zgodne z bieżącą gałęzią przy odczycie. Plik główny 9298d7d95e1787db19382449018320ac3cb91a79, katalog 81d1b4f905b12bf190ff4f3a4085d303f335e36a. 44 wejścia, 44 pozycje katalogu, dokładna zgodność kolejności katalogu, pliku głównego i zbioru plików, 44 unikatowe ID.
Odczytano pełny rozdział w starej i nowej wersji i wykonano niezależny parser z usuwaniem komentarzy TeX z uwzględnieniem parzystości ukośników. Zestaw 21 etykiet niezmieniony, żadnych duplikatów. Dwa nowe cele (sec:kt-seifert, sec:kt-fox-calculus) istnieją; wszystkie 8 odsyłaczy mają cele lokalne. 170 poprawnych par środowisk, 32 środowiska proof, 7 rysunków. Brak błędów zagnieżdżenia, zakazanych wzorców terminologicznych i ręcznej numeracji rozdziałów w zmienionym pliku.
Kontrola różnicowa PASS. Próba ponownego pobrania wszystkich 44 plików w jednym wywołaniu przekroczyła limit narzędzia; nie deklaruje się pełnego świeżego przebiegu skryptu globalnego ani świeżego audytu powtórzeń między rozdziałami. Pozostają bramką CI.

## Stan bramek
Run 45596400156 dla badanego SHA: po ostatniej kontroli struktural-audit 139143497091 queued, full-book-pdf 139143496435 in_progress; artefakt pełnego tomu 15013936392 pojawił się dla właściwego SHA. Nie wykonano jeszcze oględzin. Nie uruchamiano dodatkowego workflow, nie zmieniano źródeł.
Kolejność: potwierdzić pełny structural-audit (w tym log nowych regresji i powtórzenia tekstu) oraz full-book-pdf, następnie obejrzeć PDF rozdziału, następnie niezależny audyt kontrolny i dopiero zamknąć rozdział. Postęp 24/44.
