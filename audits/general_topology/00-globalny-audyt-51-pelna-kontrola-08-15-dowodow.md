# Topologia ogólna — globalny audyt 51: pełna kontrola 15 dowodów rozdziału 08

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Źródło:** `chapters/pl/general_topology/08-spojnosc.tex`; aktualny blob `51b5cd2adf19a0345510bd14d5c0ac318cef3ae1`.

## Metoda

Odczytano wszystkie **15 aktualnych środowisk `proof`** wraz z hipotezami ich twierdzeń, ponownie sprawdzając poprawność obu kierunków równoważności, pustych przestrzeni i iloczynów, warunków maksymalności składowych oraz konkatenacji dróg. Ponadto sprawdzono konstrukcyjne przykłady krzywej sinusowej topologa i zbioru Cantora. To indywidualna kontrola matematyczna, a nie wyłącznie indeks, uruchomienie testów czy deklaracja formalizacji Lean. Nie modyfikowano źródeł.

## Dowód po dowodzie

| ID | Etykieta i początkowy wiersz proof | Weryfikacja niezależna |
|---|---|---|
| 08-01 | `thm:topog-spojnosc-charakteryzacje`, 40 | Rozdzielenie X=U∪V jest równoważne istnieniu niepustego właściwego zbioru otwarto-domkniętego U. Jego funkcja charakterystyczna do dyskretnego {0,1} jest ciągła i niestała; w drugą stronę przeciwobrazy obu singletonów rozdzielają X. Dla X pustego wszystkie trzy warunki są prawdziwe. |
| 08-02 | `thm:topog-spojnosc-przedzialy`, 88 | Dla odcinka [a,b] przy hipotetycznym rozdzieleniu wybór u<v i c=sup(U∩[u,v]) jest uzasadniony zupełnością R. Domkniętość U w odcinku daje c∈U, otwartość U zaprzecza c<v, a c=v przeczy rozłączności. Przedział dowolny zawiera odcinek między każdymi dwoma punktami, więc rozdzielenie byłoby niemożliwe. Dla nieprzedziałowego A luka c∉A rozdziela je; przypadki pusty i jednopunktowy uwzględniono. |
| 08-03 | `thm:topog-spojnosc-obraz-ciagly`, 135 | Ograniczenie f|A:A→f(A) jest ciągłą surjekcją. Hipotetyczne rozdzielenie obrazu ma niepuste rozłączne otwarte przeciwobrazy w A. Obrazy homeomorfizmów i odwzorowań ilorazowych są szczególnymi przypadkami; nic nie zakłada Hausdorffowości. |
| 08-04 | `cor:topog-spojnosc-wartosci-posredniej`, 157 | f(X) jest spójny jako obraz ciągły i dlatego jest przedziałem R. Każda liczba między f(x),f(y) należy do obrazu. Warunek x,y∈X rozwiązuje także przypadek pustej X (twierdzenie puste). |
| 08-05 | `cor:topog-spojnosc-zwarty-przedzial`, 174 | Dla X niepustej zwartej Weierstrass daje rzeczywiste osiągane m,M. Z poprzedniej własności wartości pośredniej obraz zawiera [m,M], a z ograniczeń kresowych jest w [m,M], więc f(X)=[m,M]. Nie ma zbędnej hipotezy T2 dla X. |
| 08-06 | `thm:topog-spojnosc-suma`, 194 | Dla I niepustego wspólny punkt p wszystkich A_i należy do jednej strony hipotetycznego rozdzielenia, a spójność A_i wymusza każdorazowo A_i w tej samej stronie. Zatem druga strona jest pusta. Dla I pustego suma jest pusta i spójna, mimo nieadekwatności punktu wspólnego. |
| 08-07 | `thm:topog-spojnosc-domkniecie`, 233 | Gdyby A⊂B⊂cl A miało rozdzielenie U,V, spójność A umieszcza A po jednej stronie; druga, niepusta otwarta w B, jest przecięciem B z otwartym W w X i przecina A dzięki B⊂cl A — sprzeczność. Działa też dla A=∅, bo wtedy B=∅. |
| 08-08 | `thm:topog-spojnosc-iloczyn`, 267 | Skończone iloczyny spójne: bazowy przekrój B=X×{y0} oraz włókna {x}×Y są spójne i przecinają B. Dla dowolnego niepustego iloczynu wybiera się jeden punkt p; punkty o skończenie wielu współrzędnych różnych od p tworzą gęstą spójną sumę połączonych zbiorów Y_J. Gęstość wynika ze skończonego nośnika bazowego cylindra. Pusty iloczyn przestrzeni lub produkt z pustym czynnikiem obsłużone osobno. |
| 08-09 | `thm:topog-spojnosc-skladowe`, 353 | C(x) jest sumą wszystkich spójnych zbiorów zawierających x; ich wspólne x daje spójność. Maksymalność wymusza cl C(x)=C(x). Przecinające się składowe muszą być równe przez spójność ich sumy; składowe pokrywają X. Nie ma nieuprawnionego stwierdzenia, że składowe są otwarte. |
| 08-10 | `lem:topog-spojnosc-skladanie-drog`, 487 | Odwrócenie t↦1−t zachowuje ciągłość; konkatenacja na dwóch domkniętych przedziałach [0,1/2],[1/2,1] jest poprawnie sklejona, bo γ(1)=δ(0). Nie wymaga iniektywności dróg. |
| 08-11 | `thm:topog-spojnosc-droga-implikuje`, 512 | Droga łącząca punkty po dwóch stronach rozdzielenia miałaby spójny obraz [0,1], który rozdzielałby się przez oba przecięcia. Dla ciągłego f:X→Y obraz dowolnej drogi γ jest drogą f∘γ w f(X); surjekcja na własny obraz wystarcza. |
| 08-12 | `prop:topog-spojnosc-skladowe-drogowe`, 562 | Istnienie drogi stałej, odwróconej i złożonej daje relację równoważności. Każda klasa P(x) jest drogowo spójna przez połączenie y→x→z i zawiera się w składowej spójnej C(x). Otwartość i domkniętość P(x) nie są postulowane. |
| 08-13 | `thm:topog-spojnosc-lokalna-komponenty`, 718 | W lokalnie spójnej X małe otwarte spójne otoczenie V_x⊂U przecina składową C_U(x), więc z jej maksymalności V_x⊂C. Składowa jest sumą takich V_x i otwarta. W odwrotną stronę otwarte składowe U są wymaganymi małymi otwartymi spójnymi otoczeniami. Wersja drogowa korzysta z konkatenacji dróg w punkcie wspólnym, nie tylko ze zwykłej spójności. |
| 08-14 | `cor:topog-spojnosc-lokalna-drogowa`, 754 | Składowe drogowe lokalnie drogowo spójnej X są otwarte; ich dopełnienia są sumami innych otwartych składowych drogowych, więc są one także domknięte. Każda składowa spójna C może zawierać tylko jedną taką klasę P, inaczej P∩C,C\P rozdzieliłyby C. |
| 08-15 | `cor:topog-spojnosc-euklidesowe`, 775 | Dla otwartego U⊂R^n każde x∈U ma zawartą w U wypukłą kulę, która jest spójna drogowo drogami liniowymi. U jest lokalnie drogowo spójna, więc jej spójność implikuje spójność drogową. Odwrotnie spójność drogowa zawsze daje spójność; U=∅ również spełnia obie własności. |

## Przypadki konstrukcyjne poza środowiskami proof

**Krzywa sinusowa topologa `ex:topog-spojnosc-sinus`: PASS.** Graf G={(x,sin(1/x)):0<x≤1} jest ciągłym obrazem przedziału, zatem spójny drogowo. Ciągami `x_n=1/(θ+2πn)` dochodzi do każdego (0,y), y∈[-1,1]; ciągłość sin(1/x) przy x>0 eliminuje punkty poza grafem i odcinkiem. Dowód braku drogi z odcinka do G wybiera *ostatni* parametr t₀, dla którego pierwsza współrzędna znika, i dzięki własności wartości pośredniej znajduje po t₀ dowolnie małe dodatnie argumenty funkcji sin o wartościach +1 i -1. Przeczy to ciągłości drugiej współrzędnej w t₀. Odcinek i graf są dokładnie dwiema składowymi drogowymi, graf jest niedomknięty, odcinek nieotwarty.

**Zbiór Cantora `ex:topog-spojnosc-cantor`: PASS.** Rozwinięcia na cyfrach 0,2 w systemie trójkowym są jednoznaczne, bo pierwsza różnica pozycji k dominuje cały ogon `2·3^{-k}-∑_{n>k}2·3^{-n}=3^{-k}>0`. Cylindry o zadanych prefiksach długości m tworzą skończony rozkład na względnie otwarto-domknięte podzbiory, więc oddzielają każde dwa punkty Cantora. Zstępujące sumy zamkniętych przedziałów K_m dają dokładnie Cantora i jego zwartość jako domkniętego podzbioru [0,1].

## Werdykt i zależności

**15/15 PASS**, wszystkie źródłowe etykiety dowodów `08-01...08-15` wpisano do powyższej macierzy. Nie odnaleziono nowej luki matematycznej wymagającej edycji LaTeX. Odróżniono spójność, spójność drogową, ich wersje lokalne oraz otwartość składowych — wszystkie hipotezy weryfikowano oddzielnie.

Rozdział 08 zachował pierwotny SHA; wcześniejsze reaudytowanie zmian terminologicznych w audycie 36 nie jest przepisywane jako nowe 2+1. Po raportach 46–47, 49–50 pełna indywidualna dokumentacja wynosiła **211/325**. Ten raport zwiększa ją do **226/325**. Pozostają **99** dowodów: 09 (10), 10–13 (45), 24–26 (44).

CI należy sprawdzić po zapisaniu raportu; nie można utożsamiać zapisu raportu z sukcesem workflow. W tym audycie nie przebudowywano rysunków ani PDF, bo nie zmieniono źródeł. Następny krok: rozdział 09 (10 dowodów). Automatyzacja audytów pozostaje aktywna.
