# Teoria grafów i węzłów — audyt globalny 07: stabilizacja historycznych rozdziałów 07–09

Data: 2026-11-23.
Gałąź: \`biblioteka-matematyczna-iteracja-6\`.

**WYNIK: PASS — historyczne rozdziały 07–09 są stabilne w zakresie audytu matematycznego, testów modeli skończonych, integracji i składu PDF.**
**Cały 44-rozdziałowy skrypt nadal NIE ma statusu globalnie ustabilizowanego**, ponieważ kolejne historyczne rozdziały 10–36 wymagają oddzielnych audytów.

## Źródła i commity

- Rozdział 07: \`chapters/pl/graph_and_knot_theory/07-graf-jako-przestrzen-topologiczna.tex\`.
- Rozdział 08: \`chapters/pl/graph_and_knot_theory/08-laplasjan-grafu-dyskretna-teoria-hodge-a-i-twierdzenie-kirchho.tex\`.
- Rozdział 09: \`chapters/pl/graph_and_knot_theory/09-grafy-planarne-sciany-i-wzor-eulera.tex\`.
- Nowy test: \`tools/tests/test_graph_and_knot_topology_laplacian_planarity.py\`.
- Wcześniejszy raport szczegółowy: \`audits/graph_and_knot_theory/27-globalny-audyt-06-topologia-laplasjan-planarnosc.md\`.

Pierwsza iteracja:
[commit d754aa9ce49627040e7157ded680a70624f7101c](https://github.com/dariusz-piekarz/mathematical_scipts/commit/d754aa9ce49627040e7157ded680a70624f7101c).
Poprawa dowodu brzegowego i ilustracja:
[commit be2539df1aaf674554409774577943ddda1fe611](https://github.com/dariusz-piekarz/mathematical_scipts/commit/be2539df1aaf674554409774577943ddda1fe611).

## Audyt matematyczny rozdziału 07

- Przeanalizowano dowód ilorazu CW przez kontraktowalny podkompleks, używający własności przedłużania homotopii. Wskazano wyraźną różnicę wobec zwijania dowolnego kontraktowalnego podzbioru.
- Skontrolowano zwijanie drzewa rozpinającego, równoważność z bukietem \`m-n+1\` okręgów oraz obliczenie grupy fundamentalnej przy pomocy van Kampena.
- Weryfikowano konstrukcję nakrycia uniwersalnego ze zredukowanych spacerów, lokalną bijekcję incydencji i argument braku cykli przez jednoznacznego poprzednika.
- Uzupełniono tekst o przypadek drzew: spójne nakrycie drzewa ma tylko jedną kartkę; dla \`r=0\` i \`d>1\` założenia spójnego \`d\`-kartkowego nakrycia nie mogą zachodzić.
- Skontrolowano równości \`n_hat=dn\`, \`m_hat=dm\`, \`r_hat=1+d(r-1)\` i zgodność odległości wierzchołków z metryką długości.

Testy: **4539** rozważonych nakryć dwu- i trójkartkowych skonstruowanych metodą przesunięć arkuszy nad wszystkimi spójnymi grafami na maksymalnie czterech wierzchołkach; wśród nich **3150** nakryć spójnych. Sprawdzono lokalną bijekcję incydencji, liczbę komórek, liczbę składowych oraz wzór Nielsena–Schreiera przy założeniu spójności.

## Audyt matematyczny rozdziału 08

- Przeanalizowano energię \`f^TLf\`, dodatniość i jądro ważonego Laplasjanu, dodatnią określoność problemu Dirichleta i jednoznaczność minimalizatora.
- Zweryfikowano identyfikację \`H^1(G;R)\` z harmonicznymi kołańcuchami oraz zgodność dodatnich wartości własnych \`BB^T\` i \`B^TB\`.
- Skontrolowano krok Cauchy'ego–Bineta w twierdzeniu macierzowo-drzewowym Kirchhoffa i argument \`det B_T^(r)=±1\` dla drzewa.
- Skontrolowano spektralną tożsamość \`det(L+11^T/n)=n tau(G)\`, rozwiązanie \`Lf=b\`, efektywną rezystancję i ortogonalny argument zasady Thomsona.
- Rozdzielono dwa niezmienniki wcześniej zapisane jednakowo: **\`tau_V(G)\`** oznacza minimalną moc pokrycia wierzchołkowego (rozdział 05), a **\`tau(G)\`** liczbę drzew rozpinających (rozdziały 08, 12 i 19). Wstawiono uwagę z precyzyjną konwencją, bez zmiany wyników Kirchhoffa i Tutte'a.

Testy: **1099** wszystkich grafów prostych na 1–5 wierzchołkach, z dokładną (wymierną) kontrolą kofaktorów Laplasjanu i bezpośrednią enumeracją drzew rozpinających, zarówno dla wag jednostkowych, jak i dodatnich wag całkowitych; dodatkowo tam, gdzie graf jest spójny, sprawdzono opór efektywny, zasady energii i Dirichleta.

## Audyt matematyczny rozdziału 09

- Sprawdzono topologiczną definicję osadzenia grafu, charakterystykę Eulera \`n-m+f=1+c\` i rozróżnienie dodania krawędzi zamykającej cykl od połączenia składowych.
- Skontrolowano liczenie długości wszystkich obchodów ścianowych, również przy mostach, a następnie ograniczenia \`m<=3n-6\` oraz \`m<=2n-4\` przy założeniu dwudzielności.
- Sprawdzono dowód dwukolorowania ścian grafów o parzystych stopniach za pomocą parzystości przecięć. Jawnie wyłączono z argumentu korzystającego ze szlaku Eulera przypadek pustego zbioru krawędzi: spójność prowadzi wtedy do \`K_1\`, którego jedyna ściana może otrzymać dowolny kolor.
- Uzupełniono tekst o przykład grafu dwóch trójkątów sklejonych w jednym wierzchołku. Jest eulerowski, ale niedwudzielny; jego dwie ograniczone ściany dostają ten sam kolor, a zewnętrzna przeciwny. Dodano czytelny rysunek TikZ i podpis objaśniający różnicę między kolorowaniem ścian i wierzchołków.

Testy: enumeracja **1099** grafów na 1–5 wierzchołkach; **772** z nich są spójne, a **771** spośród spójnych posiada osadzenie sferyczne. Jedynym nieplanarnym spójnym grafem na maksymalnie pięciu wierzchołkach jest \`K_5\`. Sprawdzono także osobno \`K_5-e\`, \`K_{3,3}\` i dwa trójkąty o wspólnym wierzchołku. Test planaryzacji enumeruje systemy rotacji (porządki cykliczne sąsiadów), oblicza obchody ścianowe jako orbity półkrawędzi, sprawdza \`n-m+f=2\`, ograniczenia planarne i dwukolorowanie grafu dualnego. Jest to niezależny model skończony, nie substytut twierdzenia dla wszystkich grafów.

## Końcowy CI (po obu commitach)

[GitHub Actions: pełny audyt i pełny PDF, przebieg 45159852979](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45159852979):
- \`structural-audit\`: **success** (nowe testy 07–09 oraz wcześniej stabilizowane 01–06);
- \`full-book-pdf\`: **success** (trzy pełne przebiegi \`pdflatex\`, 44 rozdziały, **263 strony A4**, **0** ostrzeżeń w końcowym logu, **0** przepełnień);
- 44/44 pliki zgodne ze spisem i katalogiem; 0 zduplikowanych etykiet, 0 nierozwiązanych referencji, 0 błędnych środowisk i 0 naruszeń sprawdzanych reguł terminologicznych.

[Algorytmiczny CI, przebieg 45159852932](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45159852932): **success**.

[Polish mathematical terminology, 45159852974](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45159852974): **success**.

[Mathematical library application checks, 45159853038](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45159853038): **success**.

## Niezależny przegląd PDF

Pobrano rzeczywisty artefakt pełnej książki ze świeżego CI.
Przeanalizowano strony PDF 86–101 (rozdziały 07–09);
w szczególności strony 89 (nakrycia), 93 (konwencja oznaczeń),
98–100 (osadzenia i wzór Eulera) oraz stronę 101 z nowym
dowodem przypadku \`K_1\` i rysunkiem dwukolorowania ścian.

W nowej wersji ilustracja dwóch trójkątów mieści się wraz
z objaśnieniem na stronie PDF **101**; podpis nie przecina rysunku,
nazwy wierzchołków ani kolory ścian się nie zlewają,
rysunek nie wychodzi poza marginesy. Dzięki temu
strona 101 ma również pełniejszą, bardziej pedagogiczną treść.
Skład całej książki zawiera **263 strony** i nie generuje ostrzeżeń.

## Wynik i dalszy plan

**Rozdziały 07–09: PASS / lokalnie stabilne w podanym zakresie.**
Testy numeryczne i wyczerpujące do pięciu wierzchołków
nie są poświadczeniem formalnym (Lean) ani dowodem
poprawności wszystkich ogólnych twierdzeń, dlatego
nie zastępują przeglądu przedstawionych argumentów.

**Następny blok audytu globalnego: historyczne rozdziały 10–12**:
kryteria planarności (Kuratowski, Wagner, kolorowanie),
grafy na powierzchniach, grafy dualne i homologia komórkowa,
wielomian Tutte'a, kolorowania i dualność algebraiczna.
Zasada pracy pozostaje niezmienna:
jeden blok, szczegółowy audyt i poprawki,
niezależne testy i cały PDF,
dopiero potem raport stabilizacji.
