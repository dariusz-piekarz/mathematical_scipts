# GT — audyt kontrolny 323

GT18: sprawdzono definicję pochodnej Foxa, fundamentalną tożsamość i prezentację modułu Alexandera z diagramu Wirtingera. Dodano bezpośredni dowód niezależności skreślanej kolumny (minory różnią się znakiem) przez zerową sumę kolumn i wieloliniowość wyznacznika. Commit cb0d8498abb110448f0e207070b53d169eaf80ea.
GT19: sprawdzono wzór na podpisaną sumę drzew (Cauchy–Binet także przy pętlach i krawędziach równoległych) i specjalizację nawiasu w exp(i pi/4). Bez nowych luk w tych dowodach, bez zmian.
GT20: sprawdzono redukcję homologii nakrycia rozgałęzionego do ilorazu modułu Alexandera, homomorfizm łączący, wypełnienie torusa, rozkład na bloki i rangę. Uzupełniono jawne wektory Fouriera, postać operatora przez iloczyny Kroneckera oraz uzasadnienie liczności kokernu przez postać Smitha. Commit 00439a375d01ebbda4eb4e8c9273295b0df300f8.
GT21: sprawdzono obliczenie H1 przez abelianizację i Mayera–Vietorisa, w tym pętle i rozkład pusty, oraz homologię wiązki torusowej. Doprecyzowano, że sumy krawędziowe obejmują jedną orientację każdej krawędzi geometrycznej. Commit 46f6eee62187af5d3ce5f07134e305d6972d3aba.
GT22: sprawdzono lemat sygnaturowy i faktoryzację Foxa–Milnora. Uzasadniono nieparzystość f(-1) przez redukcję modulo 2. Commit ff154771fb60538a73063a68adb16d557be1efd8.

Walidacja: 625/625 całkowitych macierzy 2x3 o zerowych sumach wierszy (wpisy pierwszych dwóch kolumn od -2 do 2), kontrola relacji znaków minorów; 209/209 wektorów Fouriera dla d=2..20, maksymalny błąd numeryczny 1.71e-14. Zagnieżdżenie środowisk poprawne w czterech zmienionych rozdziałach, wszystkie cztery bloby potwierdzone ponownym odczytem. Konflikty równoległych zapisów rozwiązano po odświeżeniu źródeł. Testy są kontrolami algebraicznymi, nie zastępują dowodów topologicznych.

CI pełne 45986017320, algorytmy 45986017482, aplikacja 45986017440, terminologia 45986017288 — queued przy odczycie. Brak wizualnego odbioru PDF. Nie jest to odbiór wszystkich twierdzeń GT18–22. Następny etap: GT23–27 — plumbing, rozmaitości Seiferta, rachunek Kirby'ego oraz wymierna kontrakcja.
