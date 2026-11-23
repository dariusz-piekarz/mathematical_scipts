# ALG-00 — kontrola regresyjna 07 (23.11.2026)

## Podstawa i zakres
Gałąź `biblioteka-matematyczna-iteracja-6`; HEAD odczytany na początku: `a7f8ea27a3e078e12bad0805c29816257af75183`. Źródło `chapters/pl/algebraic_geometry/00-teoria-pierscieni-od-arytmetyki-do-geometrii-rownan.tex`, blob `daedcd38d31e42c738df7f7d12a66d3994ebda8a`, 1727 wierszy. Odczytano rejestr `STATUS.md`, raport globalny IV, raport reuse AA-09–AA-12, raport regresji 06, `README.md`, `catalog/books.json`, `books/pl/algebraic_geometry.tex`, standard `application/docs/MATHEMATICAL_WRITING_GRANULARITY_STANDARD.md`, źródło rozdziału i workflow ALG-00. Rejestr wskazuje wcześniejsze zamknięcie wszystkich ALG-00–ALG-10; nie ma otwartego rozdziału. Przedmiotem niniejszej kontroli jest wyłącznie ALG-00.

## Kontrola matematyczna i redakcyjna
Odczytano pełne źródło rozdziału i ponownie przeanalizowano jego konstrukcje: pierścienie i ilorazy, jednostki, homomorfizmy i jądra, ideały, CRT, ideały pierwsze i maksymalne, pierwiastniki, dzielenie wielomianów, podstawienie w punkcie, parabolę, dwie osie, niegłówność (x,y), lemat Gaussa i UFD. Kontrola krytyczna zwracała uwagę na warunki niezerowości, pierwotności, rozróżnienie wielomianów formalnych od funkcji nad ciałami skończonymi oraz na kwantyfikatory. Nie stwierdzono jednoznacznej nowej usterki wymagającej edycji .tex. Kontrola dowodów bazowych opiera się na wcześniej zweryfikowanych AA-09 (CRT, ideały), AA-10 (Bézout), AA-11 (Gauss, UFD) i AA-12 (pierwiastniki); nie zmieniano AA.

Zweryfikowano obecność 11 wpisów katalogu ALG-00–ALG-10 i odpowiadających im 11 `\\input` w punkcie wejścia. Workflow ALG-00 wykonuje testy regresyjne, tworzy osobny punkt wejścia, kompiluje przez latex-action oraz sprawdza log i artefakt. Samo istnienie tego workflow **nie stanowi** nowego pozytywnego wyniku CI.

## Ograniczenia i decyzja
Bezpośredni `git ls-remote` w środowisku wykonawczym zakończył się `Could not resolve host: github.com`. Dostęp do treści przez konektor GitHub działa, ale nie zapewnia lokalnego pełnego drzewa do uruchomienia nowego dwukrotnego składu. Nie przeprowadzono nowej kompilacji LaTeX, inspekcji PDF ani pełnej weryfikacji końcowego CI na tym HEAD. Nie zaliczać tej kontroli jako pełnego audytu stabilizacyjnego ani jako dodatkowego czystego audytu; licznik pozostaje bez zmian. Nie zmieniono źródeł matematycznych. Nie tworzyć pozornych korekt.

| Zakres | Stan |
|---|---|
| ALG-00 | Wcześniej STABILNY/ZAMKNIĘTY; regresja 07 częściowa technicznie, bez nowego PASS |
| ALG-01–ALG-10 | Wcześniej STABILNE/ZAMKNIĘTE, nieaudytowane w tym przebiegu |
| Globalne III–IV | Wcześniej zakończone; bez nowego potwierdzenia |
