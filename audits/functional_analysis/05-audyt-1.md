# Analiza funkcjonalna — rozdział 05 — audyt 01

**Data:** 23 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Źródło:** chapters/pl/functional_analysis/05-przestrzenie-lokalnie-wypukle-i-seminormy.tex.  
**Wynik:** wykonany z poprawkami merytoryczno-redakcyjnymi; **NIE JEST CZYSTYM AUDYTEM**, rozdział 05 wymaga dwóch kolejnych niezależnych czystych kontroli po tych zmianach.

## Zakres

Niezależny przegląd całego rozdziału, wszystkich 13 dowodów, pięciu środowisk przykładów i rysunku funkcjonału Minkowskiego, w tym założeń o lokalnej wypukłości, Hausdorffie, pochłanianiu, zrównoważeniu i otwartości, topologii generowanych seminormami, kryterium ciągłości operatorów, ograniczoności, normowalności i metryzowalności, zupełności Frécheta oraz konstrukcji produktów i ilorazów. Wykonano też kontrolę terminologii i odsyłaczy do rozdziałów 02–04.

## Weryfikacja 13 dowodów

1. **Absolutna wypukłość i kombinacje dwóch punktów:** dla |α|+|β|≤1 normalizacja współczynników i wypukłość po uwzględnieniu czynników modułu jeden; osobno α=β=0. Implikacja odwrotna przez β=0 i kombinacje wypukłe. **PASS**.
2. **Absolutnie wypukła baza otoczeń:** wewnątrz wypukłego V wybiera się otwarte zrównoważone O; otoczka wypukła O pozostaje wewnątrz V i jest zrównoważona. Otwartość wykazana przez perturbowanie składnika wypukłej reprezentacji z dodatnim współczynnikiem. **PASS**.
3. **Topologia generowana rodziną seminorm:** baza skończonych warunków p_j(x)<ε, ciągłość działań, minimalność topologii względem ciągłości rodziny, Hausdorff przez wspólne jądro i opis granic sieci. **PASS**.
4. **Funkcjonał Minkowskiego:** pochłanianie i zrównoważenie dają dodatnią jednorodność, wypukłość daje podaddytywność, a otwartość A zapewnia równoważność A={p_A<1} i ciągłość p_A. Nie wyciągano wniosku o dodatniej określoności bez ograniczoności. **PASS**.
5. **Charakteryzacja lokalnej wypukłości:** funkcjonały Minkowskiego otwartych absolutnie wypukłych otoczeń odtwarzają bazę; w przypadku Hausdorffa rozdzielają punkty. **PASS**.
6. **Ciągłość liniowa przez seminormy:** oszacowanie q(Tx)≤C max p_j(x) przez jednorodność i oddzielne traktowanie r(x)=0; odwrotna implikacja przez zbieżność wszystkich seminorm docelowych. **PASS**.
7. **Ograniczoność przez seminormy:** ciągłość p implikuje ograniczoność p(B), a ograniczoność wszystkich p(B) daje wspólne skalowanie skończonej liczby seminorm. Pusty B rozpatrzony zgodnie z konwencją sup∅=0. **PASS**.
8. **Otoczka absolutnie wypukła zbioru ograniczonego:** ograniczoność seminorm wszystkich kombinacji z sumą modułów współczynników ≤1; każda wypukła otoczka jest podzbiorem absolutnie wypukłej. **PASS**.
9. **Kryterium normowalności Kolmogorowa:** lokalna wypukłość pozwala wybrać otwarte absolutnie wypukłe ograniczone U; jego funkcjonał Minkowskiego ma zerowe jądro przez ograniczoność U i Hausdorff X; rodzina kul homotetycznych U generuje wyjściową topologię. **PASS**.
10. **Przeliczalna rodzina seminorm i metryzowalność:** suma dyadyczna min(1,p_n) jest metryką translacyjnie niezmienniczą i odtwarza wszystkie seminormy, także przy kontroli ogona; odwrotnie z przeliczalnej bazy i lokalnej wypukłości otrzymuje się przeliczalny zbiór seminorm. **PASS**.
11. **Kryterium Cauchy'ego dla seminorm:** siatka jest Cauchy wtedy i tylko wtedy, gdy różnice są ostatecznie małe względem każdej seminormy; skierowanie D umożliwia wspólny późny indeks dla skończenie wielu p_j. **PASS**.
12. **Zupełność C∞([0,1]):** jednostajnie Cauchy'ego pochodne wszystkich rzędów zbiegają do funkcji ciągłych g_j, fundamentalne twierdzenie rachunku całkowego daje g_j'=g_{j+1}, zatem g_0 jest gładka, a zbieżność dotyczy wszystkich p_m; metryzowalność redukuje zupełność sieci do ciągowej. **PASS**.
13. **Podprzestrzenie, produkty i ilorazy lokalnie wypukłych:** przecięcie z podprzestrzenią, skończenie kontrolowane współrzędne produktu i obrazy przez otwarte rzutowanie ilorazowe zachowują wypukłość bazowych otoczeń. Hausdorff ilorazu wymaga domkniętości podprzestrzeni. **PASS**.

## Pięć środowisk przykładów — 5/5

1. Seminormy p_n(x)=|x_n| w K^N, seminormy pochodnych w C∞([0,1]) i seminormy supremum na zwartych podzbiorach obszaru: poprawne.
2. Na R² pasek A={|x|<1} ma p_A(x,y)=|x|, a więc seminormę niebędącą normą: poprawne.
3. Na c_00 zbiór A={sup_n n|x_n|≤1} jest pochłaniający, ale jego funkcjonał Minkowskiego nie jest ciągły w normie supremum: poprawne.
4. K^N z topologią produktu jest przestrzenią Frécheta, lecz nie jest normowalna: poprawne.
5. C∞([0,1]) z seminormami p_m jest przestrzenią Frécheta, ale nie jest normowalna. Rodzina sinusoid o częstotliwości N ma p_m małe przy p_{m+1} rosnącej do nieskończoności: poprawne.

## Wprowadzone poprawki

- **Uzasadniono istniejącą tezę w motywacji**: dla nieatomowej miary Lebesgue'a na [0,1] i 0<p<1 każdy ciągły funkcjonał liniowy na L^p jest zerowy. Z ciągłości uzyskuje się oszacowanie |L(f)|≤C||f||_p, następnie mierząc |f|^p dzieli się [0,1] na n części równej masy. Dla f=sum fχ_{E_j} zachodzi |L(f)|≤C n^(1-1/p)||f||_p→0. Dodano również jawny wybór δ i skalowania δg/(2||g||_p) do uzyskania C.
- **Poprawiono błędny odsyłacz słowny** „funkcjonał Minkowskiego z następnej podsekcji” na „z poprzedniej podsekcji”.
- **Zastrzeżono przy rysunku**, że etykieta x/p_A(x) i interpretacja punktu na brzegu A dotyczą przypadku p_A(x)>0; ogólny funkcjonał Minkowskiego może mieć niezerowe jądro.
- **Ujednolicono terminologię**: „zupełność ciągowa” zamiast „zupełność sekwencyjna” i „przestrzeń sprzężona D'(Ω)” zamiast samodzielnego angielskiego rzeczownika „dual”.
- Pozostawiono oryginalne 19 etykiet, 13 środowisk dowodów i pięć środowisk przykładów. Rysunek nie został usunięty ani zastąpiony.

## Kontrole techniczne

- Dodano tools/tests/test_functional_analysis_ch05.py: **12 testów** dotyczących integracji w książce, referencji, terminologii, absolutnej wypukłości, funkcjonału Minkowskiego w wymiarze 2 i na c_00, argumentu podziału nieatomowej miary, sinusoidalnego kontrprzykładu dla C∞, metryki od seminorm, granic i konstrukcji ilorazowej.
- Dodano .github/workflows/functional-analysis-ch05.yml: dedykowana kontrola rozdziału 05 z oryginalną preambułą i tekstami rozdziałów 01–05, testami, kompilacją PDF, kontrolą brakujących odsyłaczy, ostrzeżeń i przepełnionych wierszy oraz zapisem artefaktów.
- Początkowy przebieg [45160274967](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45160274967) zakończył się **SUCCESS** przy pierwszej wersji poprawek i 12 testach; po dalszym rozwinięciu uzasadnienia oszacowania dla L poprawny końcowy przebieg jeszcze wymaga potwierdzenia.
- Kontrola wizualna finalnego PDF, w tym podpisu i etykiety rysunku Minkowskiego, wymaga zakończenia przebiegu po ostatniej zmianie źródła.

## Decyzja

**Audyt 05/01 wykonany z poprawkami i niezaliczany jako czysty. Rozdział 05 NIEUSTABILIZOWANY.** Kolejny krok to niezależna kontrola 05/02 po potwierdzeniu końcowego CI i poprawnego PDF; dalej dwie kolejno czyste iteracje, bez przechodzenia do rozdziału 06 przed stabilizacją.
