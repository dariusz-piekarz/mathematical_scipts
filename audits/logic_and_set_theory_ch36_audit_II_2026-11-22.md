# Logika matematyczna i teoria mnogości — audyt II rozdziału 36

**Data:** 22 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Źródło:** chapters/pl/logic_and_set_theory/36-modele-symetryczne-i-niezaleznosc-aksjomatu-wyboru.tex.  
**Blob:** 6891b26609ccf77a0aaddc28653bb872f05a1701, niezmieniony od poprawek audytu I.  
**Werdykt matematyczno-redakcyjny:** bez nowego błędu lub koniecznej poprawki. Pierwszy kandydat na czysty audyt; zamknięcie wymaga nowego zielonego CI.

## 1. Niezależna kontrola konstrukcji

**Działanie grupy i nośniki.** Porządek na skończonych funkcjach częściowych jest porządkiem przez rozszerzenie, zgodność przez równość na wspólnych współrzędnych. Permutacje pierwszej współrzędnej zachowują oba warunki. Stabilizatory skończonych zbiorów są zamknięte na skończone przecięcia oraz koniugacje; klasa dziedzicznie symetrycznych nazw jest definiowalna rekurencją po rangach i nie jest traktowana jako zbiór.

**Relatywne wymuszanie.** Sprawdzono klauzule atomowe, koniunkcję, negację i egzystencję. W szczególności negacja wymaga braku wszystkich wzmocnień wymuszających daną formułę, a egzystencja gęstości wzmocnień ze świadkami HS. W poprawionym dowodzie lematu prawdy gęsty jest zbiór warunków *samych* wymuszających zdanie albo jego negację, nie zbiór warunków jedynie mających możliwe wzmocnienie. To usuwa lukę znalezioną w audycie I.

**Aksjomaty ZF.** Para posiada wspólny skończony nośnik, nazwa sumy jest niezmiennicza pod stabilizatorem argumentu. Wyróżnianie wymaga jedynie podzbioru dziedziny nazwy razy zbiór warunków. Przy zbiorze potęgowym wszystkie nazwy kandydatów są ograniczone do podzbiorów dziedziny wyjściowej nazwy i zbioru warunków; nazwa ograniczona do właściwych elementów jest w HS. Rozróżniono zbiór potęgowy obliczony w N od pełnego zbioru potęgowego w M[G].

**Zbieranie i zastępowanie.** Indeksami ograniczania rang są pary z *jednego zbioru* warunków i elementów dziedziny. Minimum rangi świadka istnieje po ograniczeniu jednym znalezionym świadkiem, a zastępowanie w modelu wyjściowym daje wspólne ograniczenie \(\alpha\). Nazwa kolekcji zbiera wszystkich takich świadków i jest symetryczna; argument nie wykorzystuje AC w modelu końcowym.

**Zbiór Dedekinda skończony.** Dla każdych dwóch różnych indeksów gęsty jest zbiór warunków rozróżniających dwa ciągi Cohenów. Jeżeli domniemana funkcja ma nośnik E, a jej wartość ma indeks k spoza E, permutujemy k ze świeżym indeksem \(\ell\), nieobecnym w skończonej dziedzinie warunku. Warunek i jego obraz są zgodne, co daje wymuszoną sprzeczność. Obejmuje to wszystkie funkcje HS, nie tylko standardową enumerację. Dodatkowe wyjaśnienie przynależności dowolnej nazwy do kanonicznego \(\check\omega\) usuwa niedopowiedzenie kwantyfikacji.

**Modele wyjściowe.** W końcowym dowodzie względnej niesprzeczności przyjęto *dowolny przeliczalny model zbiorowy ZFC*, a nie przeliczalny model tranzytywny. Zewnętrzny filtr generyczny przecina wszystkie wewnętrzne zbiory gęste; iloraz wewnętrznych nazw daje model zbiorowy, bez odwołania do zewnętrznego dobrego ufundowania. Zachowano rozróżnienie między niezależnością AC od ZF a niezgodnością AC z AD.

## 2. Sytuacje graniczne i testy

Każdy pojedynczy wiersz Cohenów oraz zbiór wszystkich wierszy należą do N, lecz sama enumeracja wierszy w rozszerzeniu M[G] nie musi należeć do N. Brak jednej wskazanej enumeracji nie dowodzi nieistnienia wszystkich iniekcji: w tekście użyto silniejszego lematu o skończonym nośniku. Przetestowano skończone przypadki zgodności automorfizmów, 729 przypadków rozdzielenia wierszy i 5103 przypadki świeżego indeksu w transpozycji; testy CI przechodzą.

## 3. Inwentarz, odsyłacze i rzeczywisty PDF

Ponownie zweryfikowano: 938 wierszy, 21 różnych etykiet, 27 odsyłaczy, 5 definicji, 7 lematów, 4 twierdzenia, 3 uwagi, 1 przykład i 12 dowodów. Poprawne parowanie środowisk i podstawowe terminy polskie; bez nowych koniecznych zmian.

**GitHub Actions [45064877027](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45064877027): SUCCESS**, artefakt **14770024176**, zawierający rzeczywisty PDF i log. Książka ma **320 stron** A4; rozdział 36 zajmuje strony **313–320**. Obejrzenie wszystkich ośmiu stron w montażu 4×2 nie ujawniło kolizji lub obcięć. Log: 0 błędów LaTeX, 0 przepełnionych wierszy, 0 nierozwiązanych odsyłaczy, 0 brakujących znaków, jedno ostrzeżenie underfull w książce.

## 4. Werdykt

Audyt II **czysty merytorycznie**, bez zmiany bloba rozdziału. Po pozytywnym zakończeniu nowego CI z tego zapisu licznik czystych audytów wynosi **1/2**. Następny krok to niezależny audyt III na niezmodyfikowanym źródle, a potem dodatkowy audyt IV potwierdzający. Testy Python, LaTeX i PDF nie są formalizacją w Lean.
