# Etap VI — audyt porównawczy AT-18 / DG-18: teoria Morse'a, kompleks trajektorii i grafy Reeba

**Data:** 21 listopada 2026 r.  
**Repozytorium:** dariusz-piekarz/mathematical_scipts, gałąź biblioteka-matematyczna-iteracja-6.  
**Audyt:** dokładnie **dwa całe rozdziały**, AT-18 *Homologia Morse'a: od punktów krytycznych do homologii singularnej* i DG-18 *Teoria Morse'a: punkty krytyczne, uchwyty i przepływ*.  
**Status scalania:** zachowanie źródeł; automatyczne scalanie zabronione, main niezmieniony.

## 1. Rzeczywisty zakres porównania

AT-18 ma 13 etykiet, DG-18 po uzupełnieniu 52 etykiety; nie występuje żadna wspólna nazwa \label. Nie oznacza to braku duplikacji merytorycznej. Oba rozdziały mają wspólne tematy: lemat Morse'a, gradient, transwersalność Morse'a--Smale'a, zorientowane liczenie trajektorii, kompaktyfikacja, różniczka kwadratująca się do zera, izomorfizm z homologią singularną oraz nierówności Morse'a. Tymczasem własności geometryczne i topologiczne opracowano na różnym poziomie szczegółowości.

**Unikalny wkład DG-18:** bardzo dokładny dowód lematu Morse'a z dopełnieniem Schura; jawne obszary uchwytów i ich kołnierz; istnienie metryk Morse'a--Smale'a z parametryczną transwersalnością; rozwiązanie równania wariacyjnego; stabilne i niestabilne rozmaitości z mapami; sklejanie trajektorii po lokalnej analizie ODE; grafy Reeba i twierdzenie Reeba; kolorowe wykresy torusa i trajektorii.

**Unikalny wkład AT-18:** samodzielny skrót pełnej teorii Morse'a z rozróżnieniem przyjmowanego twierdzenia analitycznego i wyników algebraicznych; lemat o kilku punktach krytycznych na tym samym poziomie; szczegółowy przykład \mathbb RP^2 pokazujący całkowitą torsję \mathbb Z/2; osobna analiza niedoskonałej funkcji Morse'a na okręgu; dowód silnych nierówności za pomocą równości rang nad \mathbb Q.

Manifest etykiet, hipotez i decyzji:
application/config/KANDYDACI_SCALEN_AT_DG_ETAP_06.json.

## 2. AT-18: dokładna rekonstrukcja lematu Morse'a

Pierwotna wersja dowodu po wzorze
f(x)-f(0)=x^\mathsf{T}A(x)x,
A(x)=\int_0^1(1-t)\operatorname{Hess}_{tx}f\,\mathrm dt,
odwoływała się do „gładkiej eliminacji bloków” i gładkości pierwiastka macierzy, bez wzoru wykonawczego.

Dopisano kompletny rachunek dla 0<\lambda<n:
A=\begin{psmallmatrix}P&Q\\Q^\mathsf{T}&C\end{psmallmatrix},
P<0 i S=C-Q^\mathsf{T}P^{-1}Q>0 blisko punktu.
Z równości
x^\mathsf{T}Ax=(x_-+P^{-1}Qx_+)^\mathsf{T}P(x_-+P^{-1}Qx_+)+x_+^\mathsf{T}Sx_+
otrzymujemy jawne współrzędne
y_-=(-P)^{1/2}(x_-+P^{-1}Qx_+), y_+=S^{1/2}x_+.
Sprawdzono gładkość dodatniego pierwiastka, różniczkę zmiany współrzędnych w punkcie krytycznym i zastosowano twierdzenie o funkcji odwrotnej.
Osobno opisano przypadki \lambda=0 i \lambda=n, aby nie odwracać pustej macierzy.
Wynik: dokładna kwadratowa postać lokalna, a nie tylko jej przybliżenie do drugiego rzędu.

## 3. AT-18: niezależny, bezpośredni rachunek całkowitych znaków na RP²

Funkcja
f([x])=(\lambda_0x_0^2+\lambda_1x_1^2+\lambda_2x_2^2)/\sum x_i^2
dla \lambda_0<\lambda_1<\lambda_2 ma trzy punkty krytyczne p_0,p_1,p_2 o indeksach 0,1,2.
Po podniesieniu do S² przepływ gradientu ujemnego jest jawny: x_i(t) jest proporcjonalne do e^{-2\lambda_i t}x_i(0).

W karcie x_2=1, u=x_0/x_2, v=x_1/x_2, równania to
\dot u=2(\lambda_2-\lambda_0)u, \dot v=2(\lambda_2-\lambda_1)v.
Dla regularnego poziomu \lambda_1<c<\lambda_2 trajektorie p_2→p_1 przecinają go w dokładnie dwóch punktach
u=0, v=\pm\sqrt{(\lambda_2-c)/(c-\lambda_1)}.
Orientujemy W^u(p_2) przez du∧dv, a W^u(p_1) przez wzrost współrzędnej a=x_0/x_1=u/v. Koorientacja W^s(p_1) ma lokalnie znak da=du/v.
Orientacja śladu W^u(p_2) w poziomicy jest -du dla v>0, a +du dla v<0 (porządek „kierunek przepływu, potem poziomica”).
W obu punktach da na dodatnim wektorze jest ujemna; znaki trajektorii są zgodne, zatem n(p_2,p_1)=-2.
Po zmianie orientacji niestabilnej p_2 mamy +2. Dwie trajektorie p_1→p_0 odpowiadają przeciwległym półprostym a>0, a<0 i mają przeciwne znaki, więc n(p_1,p_0)=0.
Uzyskano kompleks całkowity
0→Z --2→ Z --0→ Z→0, stąd H_1=Z/2.
**To bezpośrednia kontrola przepływem** niezależna od stopnia komórkowej mapy przyłączającej.
Potwierdza, że sam rachunek Betti'ego nad Q nie wykryje torsji.

## 4. DG-18: rzeczywisty kontrprzykład do nieuprawnionego uogólnienia twierdzenia o grafie Reeba

Twierdzenie thm:graf-reeba-rodzaj-22 mówi, że dla prostej funkcji Morse'a na orientowalnej zamkniętej powierzchni rodzaju g graf Reeba ma H_1=Z^g, a wierzchołki siodeł stopień 3.
Dodano przykład prz:reeb-rp2-siodlo-stopien-dwa-18 oraz rysunek fig:reeb-rp2-siodlo-stopien-dwa-18.

Na RP² powyższa funkcja ma jedno minimum, jedno siodło i jedno maksimum. Tuż powyżej minimum podpoziomica jest dyskiem. Po dołączeniu uchwytu indeksu 1 jej charakterystyka Eulera staje się zerem. Pozostała jedna 2-komórka maksimum musi zamknąć cały brzeg, więc przed maksimum podpoziomica ma dokładnie jeden okrąg brzegowy.
Jest nieorientowalna, ponieważ przy chi=0, b=1 wzór chi=2−2g−b dla orientowalnej powierzchni wymagałby g=1/2.
Zatem jest wstęgą Möbiusa, a nie pierścieniem. W obu regularnych przedziałach wartości krytycznych poziomica jest pojedynczym okręgiem.
Graf Reeba jest przedziałem z trzema wyróżnionymi wierzchołkami o stopniach (1,2,1); siodło ma stopień 2.
Jego H_1 jest zerowe, podczas gdy H_1(RP²;Z)=Z/2.
**Wniosek:** hipoteza orientowalności jest konieczna dla podanego opisu stopni siodeł; sam graf nie wykrywa torsji.

## 5. Kontrola pozostałych wspólnych twierdzeń

- **Zwarta przestrzeń trajektorii.** AT-18 jawnie traktuje fakt gładkiego sklejania i orientowania brzegów jako używane zewnętrzne twierdzenie geometryczne. Nie wywodzi go błędnie z samego ograniczenia energii i zwartości ODE. DG-18 zawiera znacznie bardziej szczegółową konstrukcję kołnierza przełamanej trajektorii oraz kontrolę znaków za pomocą kontrakcji i równań mieszanych.
- **Różniczka kwadratująca się do zera.** W obu wersjach współczynnik przy generatorze indeksu k−2 jest sumą signed produktów liczb trajektorii p→r i r→q, która odpowiada zorientowanemu brzegowi zwartej 1-rozmaitości. Suma znaków na brzegu znika. Nie mylimy samej zwartości moduli z istnieniem gładkiej struktury kołnierza.
- **Zgodność z homologią singularną.** AT-18 odwołuje się do twierdzenia o zgodności zorientowanych incydencji uchwytów i liczb trajektorii, a DG-18 wyprowadza je z brzegów dysków niestabilnych, przecięć ze sferami pasa i dokładnych ciągów par. W przyszłym scalaniu zachować pełny dowód DG i dodatkowe przykłady AT.
- **Silne nierówności Morse'a.** W obu tekstach wykorzystuje się wzór c_k=b_k+r_k+r_{k+1} nad ciałem. AT podaje także wzór wielomianowy z Q(t) o nieujemnych współczynnikach i płaskość Q; DG rozwija jawny rachunek naprzemiennej sumy nad dowolnym ciałem.
- **Równe wartości krytyczne.** AT zawiera osobny lemat o jednoczesnym dołączeniu rozłącznych uchwytów przy kilku punktach na tym samym poziomie; DG wprowadza perturbację rozdzielającą wartości przed dołączaniem pojedynczych uchwytów. Nie należy mieszać tych dwóch strategii ani zgubić żadnej podczas deduplikacji.

## 6. Testy, CI, PDF

Test:
application/tests/test_at_dg_pairwise_18_18.py,
dziesięć niezależnych testów: dokładna tożsamość dopełnienia Schura w małych macierzach, indeksy i znaki trajektorii RP², homologia integralna i redukcja modulo dwa, stopnie grafu Reeba i wzór na rodzaj, antysymetryczna różniczka okręgu, nierówności Morse'a, bilans etykiet, środowisk i źródłowych \input.

GitHub Actions:
https://github.com/dariusz-piekarz/mathematical_scipts/actions/workflows/paired-at-dg-morse-homology-audit.yml

Workflow uruchamia trzy przebiegi pdflatex dla pełnego tomu AT-01–30 i bieżącego DG-01–20, sprawdza stabilność odsyłaczy i przepełnione wiersze oraz blokuje nieoczekiwane niezdefiniowane etykiety (dla DG zachowuje znaną listę odwołań do niezaimportowanych części 21–36).

**Status testów, liczby stron i oględzin PDF:** do uzupełnienia wyłącznie na podstawie rzeczywistego wyniku uruchomienia. Poprzednich wyników AT/DG nie należy przepisywać jako testów obecnego etapu.

## 7. Następne pary

Kolejną merytorycznie nakładającą się parą jest AT-17 / DG-19: konstrukcja Pontriagina–Thoma i podstawy kobordyzmów kontra kobordyzmy i rachunek uchwytów. Należy też później porównać AT-20 (analityczna zwartość i sklejanie trajektorii) z obecnym DG-18 oraz AT-21 (indeks pól i Poincaré–Hopf) z DG-17, jeżeli audyt relacji dowodowych wykaże brak bezstratnej kanonicznej wersji.
