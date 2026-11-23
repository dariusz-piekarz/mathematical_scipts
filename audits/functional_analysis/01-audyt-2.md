# Analiza funkcjonalna — rozdział 01 — audyt 2 (niezależny)

**Data:** 23 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6  
**Rozdział:** chapters/pl/functional_analysis/01-przestrzenie-liniowo-topologiczne-definicje-i-przyklady.tex  
**Punkt odniesienia:** audyt 1; aktualny rozdział zachowuje wersję po poprawkach.  
**Decyzja:** CZYSTY AUDYT MATEMATYCZNO-REDAKCYJNY 1/2; nie przechodzić do rozdziału 02.

## Metoda niezależnej kontroli

Niezależna lektura całego rozdziału, bez opierania się na ocenach „PASS” zapisanych w audycie 1. Przetestowano krytyczne miejsca pod kątem możliwych kontrprzykładów, przypadków skrajnych i poprawności kwantyfikatorów. Sprawdzono strukturę LaTeX, etykiety, terminologię, aktualny sześciostronicowy artefakt PDF i log kompilacji. Nie dodawano sugerowanych rozszerzeń, ponieważ nie zostały zatwierdzone.

## Pełna ponowna kontrola dziewięciu dowodów

1. **Przesunięcia i homotetie:** ciągłość odwzorowań wynika z ciągłości działań; odwrotności T_{-a} i M_{1/λ} mają właściwe dziedziny, są ciągłe i nie wymagają Hausdorffa. **PASS**.
2. **Przenoszenie otoczeń do zera:** U jest otoczeniem x dokładnie wtedy, gdy U-x jest otoczeniem zera; homeomorfizm zachowuje wszystkie, także nieotwarte, otoczenia. **PASS**.
3. **Baza otoczeń zera:** V+V⊆U wynika z ciągłości dodawania w (0,0); U∩(-U) jest symetryczne; otwarte zrównoważone W otrzymuje się ze zwartości dysku D, pokrycia skończonego i W=int(DV). U pochłania X przez ciągłość λ↦λx w 0. Sprawdzono także λ=0 i brak założenia Hausdorffa. **PASS**.
4. **Hausdorff i domknięcie zera:** udowodniono obie inkluzje N=cl({0})=∩N(0), wykorzystując symetryczne otoczenia. Dla x≠y otoczenia x+V i y+V są rozłączne, jeśli V+V⊆U i y-x∉U. N jest podprzestrzenią, również dla zerowego skalara. **PASS**.
5. **Ciągłość liniowego T w zerze:** przesunięcia otoczeń zera i liniowość T(x+U)=T(x)+T(U) implikują ciągłość w każdym x. Definicja ciągłości pracuje z otoczeniami, nie tylko zbiorami otwartymi. **PASS**.
6. **Domknięcie jądra:** T^{-1}({0}) jest domknięte, gdy przestrzeń docelowa jest Hausdorffa; założenie to jest jawne. **PASS**.
7. **Kryterium ograniczoności:** B⊆tU i zrównoważenie dają λB⊆U dla |λ|≤1/t. Odwrotna implikacja korzysta ze zrównoważonej bazy otoczeń, wybierając dodatni λ=ε. Przypadek B=∅ jest poprawny. **PASS**.
8. **Ograniczoność zbiorów zwartych oraz obrazów:** dla każdego x pochłanianie daje x∈tV, a zrównoważenie i n≥t dają x∈nV. Wstępujące otwarte pokrycie (nV) i zwartość pozwalają wybrać jedno n. Dla liniowego ciągłego T przeciwobraz otoczenia zera jest otoczeniem zera. Dowód dotyczy również K=∅ i nie zakłada Hausdorffa. **PASS**.
9. **Metryka i zerowość funkcjonałów na L^p, 0<p<1:** subaddytywność t↦t^p gwarantuje nierówność trójkąta i ciągłość działań. Z Cauchy'ego wybrano podciąg z sumowalnymi metrycznymi przyrostami; twierdzenie o zbieżności monotonicznej, warunek p<1 i nierówność Fatou dają granicę w L^p i zbieżność całego ciągu. Ciągłość funkcjonału daje oszacowanie C‖f‖_p (jako nierówność, nie aksjomat normy), bezatomowość Lebesgue'a pozwala rozbić dowolny zbiór mierzalny na n części równej miary, a n^{1-1/p}→0. Gęstość funkcji prostych obejmuje przypadek zespolony dzięki aproksymacji wartości ograniczonych funkcji w kwadracie. **PASS**.

Nie znaleziono nowej niepoprawnej tezy ani luki wymagającej zmiany źródła.

## Ponowna kontrola siedmiu przykładów

1. Topologia trywialna: ciągłość obu działań i brak Hausdorffa dla X≠{0}. **PASS**.
2. Suma dwóch prostokątów zrównoważonych: algebraiczna niezmienniczość względem |λ|≤1, oba krańcowe punkty należą do zbioru, ich środek nie. **PASS**.
3. Identyczność między normami supremum i całkową na C([0,1]): f_n(x)=max(1-nx,0) ma normy odpowiednio 1 i 1/(2n); ciąg ciągłych aproksymantów funkcji skokowej jest Cauchy'ego w normie całkowej, ale bez ciągłej granicy. **PASS**.
4. Ograniczoność normowa i topologiczna: równoważność wynika z kul otwartych; sprawdzono również konwencję dla ∅. **PASS**.
5. Iloczyn K^N: ograniczając skończenie wiele współrzędnych, pozostawiamy inną bez ograniczenia; to przeczy ograniczoności każdego otoczenia zera. e_n→0 współrzędnie. **PASS**.
6. Zbieżność punktowa: rzutowania definiują topologię podprzestrzeni, a zbieżność sieci w produkcie jest równoważna zbieżności każdej współrzędnej. **PASS**.
7. Funkcjonał p↦p'(0): p_n(t)=(1-t)^n ma normę supremum 1 i |p'_n(0)|=n; to wyklucza ciągłość. **PASS**.

## Kontrole skrajne i kontrprzykłady

- Warunek Hausdorffa nie został niejawnie wprowadzony w początkowych twierdzeniach.
- Definicja otoczenia dopuszcza otoczenia nieotwarte; zastosowania funkcji ciągłych zachowują tę wersję.
- W dowodzie zerowości funkcjonałów używa się bezatomowości Lebesgue'a: analogiczne rozumowanie dla przestrzeni czysto atomowej nie daje zerowego funkcjonału. Przy p=1 kluczowy czynnik n^{1-1/p} nie dąży do zera. Nie są to kontrprzykłady do twierdzenia przy sformułowanych założeniach.
- Weryfikacja przypadków f=0, λ=0, B=∅, K=∅ i funkcji o wartościach zespolonych.
- Uruchomiono 732 dodatkowe pomocnicze sprawdzenia na modelach skończonych i dokładnych liczbach wymiernych: **PASS**. Testy nie zastępują powyższych dowodów.

## Terminologia, struktura i skład

- Zachowano 15 unikatowych etykiet, wszystkie 4 odsyłacze wskazują istniejące lokalne etykiety; 9 środowisk proof i 7 środowisk przyklad.
- Bez niepożądanego rzeczownika „dual” poza historyczną etykietą, bez zapisu funkcji charakterystycznych przez \mathbf1; stosowana konwencja \chi_A.
- Rozdział pozostaje podłączony do książki; żadnych nowych twierdzeń i rozszerzeń w rozdziale nie wprowadzono.
- Oryginalny sześciostronicowy PDF kompilacji z poprzedniej iteracji odtworzono z artefaktu GitHub Actions; sprawdzono log końcowy: brak błędnych odsyłaczy, brak przepełnionych wierszy, brak niepoprawnych znaków. Powtórnie obejrzano komplet 6 stron: **PASS**.
- Wzmocniono istniejące testy regresyjne w tools/tests/test_functional_analysis_ch01.py z 8 do 11 testów, w tym testy czynnika n^{1-1/p}, współrzędnej niekontrolowanej w iloczynie i aproksymacji funkcji skokowej. Rozdział źródłowy **nie zmienił się**.
- GitHub Actions: [dedykowany przebieg po rozszerzeniu testów](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45151106431), weryfikacja stanu CI przy zamknięciu raportu.

## Propozycje bez automatycznej ingerencji

Pozostają wyłącznie propozycje opisane w audycie 1: porównanie L^p i ℓ^p dla p<1 oraz charakterystyka ograniczoności w K^N. Nie są to obowiązkowe poprawki i nie wpływają na ocenę czystego audytu.

## Wniosek

**Czysty audyt 1/2**, jeśli dedykowany CI zakończy się sukcesem: brak nowych korekt merytorycznych, językowych, referencyjnych i składowych. Według przyjętych zasad potrzebny jeszcze jeden niezależny czysty audyt potwierdzający rozdział 01. Nie przechodzimy do rozdziału 02.
