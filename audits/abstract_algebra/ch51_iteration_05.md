# AA-51 — audyt V: dokładna enumeracja grupy obrotów

Data: 24 listopada 2026 r. Gałąź: biblioteka-matematyczna-iteracja-6.
Źródło: commit 5a43b83dcba946ada40fc541e84250e4fc6791f6, blob b8c68c540f6ddb3f4b1f2741385ed60af752e120; odczyt potwierdza trzy dwuwierszowe bloki gathered.

## Niezależne obliczenia
Wykonano lokalnie Python/SymPy, w ciele K=QQ.algebraic_field(sqrt(5)), bez liczb zmiennoprzecinkowych. Z kolumn B=(v,w0,w1), C=(v,w1,w2) odtworzono R=CB^{-1}. Generatory: R, cykliczna permutacja współrzędnych (x,y,z)->(y,z,x) oraz diag(1,-1,-1). Od I iterowano kolejkę, domykając zbiór przez prawostronne mnożenie przez generatory. Każdy nowy element zapisywano jako krotkę dziewięciu dokładnych elementów K. Otrzymano 60 różnych macierzy. Dla każdej sprawdzono zachowanie zbioru X dwunastu wierzchołków, a kolejnymi potęgami wyznaczono rząd.
Histogram: rząd 1 — 1 element; 2 — 15; 3 — 20; 5 — 24. Dla wszystkich dwunastu wierzchołków bezpośrednio zliczono pięć macierzy ustalających każdy z nich. Wszystkie asercje przeszły, kod wyjścia 0. Niezależna kontrola modelu nie zastępuje dowodu klasyfikacji.
Reprodukcja: K.from_sympy dla wpisów, mnożenie jako sumy trzech iloczynów, BFS od I, histogram rzędów i stabilizatorów. Nie zmieniono rozdziału ani workflow.

## CI
Run 45297142088, job 138120290048, head 5a43b83dcba946ada40fc541e84250e4fc6791f6, przy ostatnim odczycie in_progress: 7 kroków success, 1 in_progress, 103 pending. Lista artefaktów pusta. Terminologia 45297142099: success. Run 45295903422 dotyczy źródła sprzed poprawki typograficznej.
Nie dokonano oględzin najnowszego PDF, nie zamknięto bramki. Pierwszy zapis raportu zwrócił konflikt 409, ponowiono po potwierdzeniu braku pliku.

## Werdykt
AA-51 W AUDYCIE do końcowego CI i kontroli stron aktualnego PDF. AA-52 nieotwarty.
