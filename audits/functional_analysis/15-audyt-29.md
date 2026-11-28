# Rozdział 15 — audyt 29 (czysty, 2/2 — stabilny)

Data: 24 listopada 2026. Gałąź biblioteka-matematyczna-iteracja-6.
Punkt wyjścia raport 28, commit 903000ae609a7a4975441f9b7d6a0806c67b0824 (1/2).
Źródło 66074009c8c4be39f19659ca126940ec03e3326b, 361 wierszy, 25 etykiet, 14 dowodów, 6 przykładów. Bez zmian źródła, testów i workflow.

## Kontrola matematyczna i redakcyjna
Ponownie przeczytano wszystkie siedem podsekcji. Zweryfikowano normę wieloliniową i jej zupełność, utożsamienie operatorów nad R i C, rekurencyjną definicję klasy C^m, rachunek wielomianów, symetrię pochodnych przez zamiany sąsiednich argumentów, drugą regułę łańcuchową, wzór Taylora i oszacowanie reszty. W kontrprzykładzie dodatniego hesjanu sprawdzono C^2 normy do trzeciej potęgi oraz wartości f(e_n/n). W twierdzeniach lokalnych sprawdzono oszacowanie kontrakcji, otwartość obrazu, resztę różniczki odwrotności, ciągłość odwracania operatorów między różnymi przestrzeniami, wybór prostokątów w twierdzeniu uwikłanym, regularność rozwiązania i jego pochodne. W części operatorowej sprawdzono znak i kolejność czynników we wzorze na wszystkie pochodne odwrotności, jednostajne majoranty dla szeregu pochodnych eksponenty oraz dowód całki na sympleksie. Brak koniecznych korekt.

Dodatkowo wykonano 360 dokładnych rachunków wymiernych dla całek jednomianów na sympleksach wymiaru 1–4, dla wszystkich wykładników z {0,1,2}. Rozwinięto (1-sum t_i)^k0 wielomianem wielomianowym i porównano sumę całek jednomianów bez czynnika t0 z formułą silniową obejmującą t0. Wszystkie wyniki zgodne. Jest to sprawdzenie algebraicznej spójności wzoru, nie niezależny dowód ogólny (całki jednomianów bez t0 obliczano ze wzoru silniowego). Wykorzystano również 28 zaliczonych rachunków macierzowych z audytu 28. Nie dodawano zagadnień.

## Technika
Ponowne dedykowane CI dla raportu 28: przebieg 45357978253, job 138320490190, 9/9 etapów, 8/8 testów, trzy przebiegi pdflatex, 138 stron, końcowy PDF 1358916 bajtów; artefakt 14902314090. Diagnostyka zaliczona, znane ostrzeżenie underfull hbox 1127. Weryfikacja struktury: 25 unikalnych etykiet, 10 rozwiązanych odsyłaczy, poprawne zagnieżdżenie środowisk. Źródło, testy i workflow niezmienione względem audytu 28; wykorzystano oględziny stron 86–94 przeprowadzone w tamtej iteracji, bez deklarowania ponownego renderowania. Testy blob 4c16180034c8d734c92eb0dd279ac57e09df740b, workflow 365bf13c5ebe02372a529f8d74b410156a082f97.

## Decyzja
Rozdział 15: drugi kolejny czysty audyt, 2/2, STABILNY. Rozdział 14 pozostaje stabilny. Następna iteracja 30: moduł 15A (całkowanie w przestrzeniach lokalnie wypukłych), 0/2. Potem 15B, 16, 17 itd., po stabilizacji każdego poprzednika. Zakres zamknięty, wyłącznie niezbędne poprawki.