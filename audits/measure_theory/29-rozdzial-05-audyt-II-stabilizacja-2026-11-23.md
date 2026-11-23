# Teoria miary / Miara i całka — rozdział 05, audyt II (globalny XXIX): niezależny audyt czysty i stabilizacja

**Data:** 2026-11-23. **Jedyna gałąź:** biblioteka-matematyczna-iteracja-6.  
**Jedyny audytowany rozdział:** chapters/pl/measure_theory/05-struktura-przestrzeni-mierzalnych.tex.  
**Zamrożony blob źródła R05 przed/po audycie:** ad8382d2b331d26c16612430dcd4b7d8f132a2d2.

## 1. Stan wejściowy, zakres, niezależność

Na początku odczytano najnowszy stan gałęzi względem commitu poprzedniego raportu f7d8414e224465b42c90f56e3ef24b85b6340cc0: **0 nowych commitów**, brak zmian źródła R05, testów i workflow. Zweryfikowano ostatni rzeczywisty raport audits/measure_theory/28-rozdzial-05-audyt-I-2026-11-23.md (blob 3a4175e047777ce22b9006fa76d65543f668ba4d), który wyszczególnia cztery poprawki tego rozdziału i dwuzadaniowy pozytywny CI. Raport XXIX przed rozpoczęciem nie istniał. Sprawdzono AGENTS.md (blob 32de9b61a368cfdce4923c8f81f9f7014da533fc) oraz docs/pl/standardy_terminologiczne.md (blob bdbfc9923e1d7224b2c19a2ba8d459eaf72cdbdf).

Wykonano **nowy niezależny przegląd matematyki R05**, bez przenoszenia ocen z raportu poprzedniego. R01–R04 odczytano wyłącznie jako źródła odsyłaczy i kontekst definicji, books/pl/measure_theory.tex jako kontekst kompilacji, zaś books/pl/integration_theory.tex jako kontekst organizacyjny uprzednio sprawdzony przy audycie I. Nie wykonywano żadnych zmian w innych rozdziałach, nie scalano i nie usuwano treści.

**W tym audycie nie zmodyfikowano źródła R05 ani infrastruktury CI:** jest to wymagany przez projekt, kolejny **czysty** audyt *po* ostatniej poprawce z audytu XXVIII, a jego wyniki utrwalono w osobnym raporcie.

## 2. Niezależna kontrola 10/10 dowodów i argumentów

Rozdział ma obecnie 406 wierszy, 8 sekcji, 3 definicje, 1 lemat, 7 twierdzeń, 2 wnioski, **10 środowisk dowodu**, 5 przykładów i 2 uwagi. Sprawdzono kolejno:

1. **Lemat o śladzie i generowaniu:** obie inkluzje; pomocnicza rodzina D zawiera X i jest zamknięta na dopełnienia i przeliczalne sumy, więc zawiera sigma_X(E). Poprawność dla A niebędącego elementem F nie wymaga dodatkowej hipotezy.
2. **Borelowskie podprzestrzenie:** otwarte zbiory A mają dokładnie postać A∩U; lemat stosuje się do zbiorów otwartych T i daje B(A)=B(T)|_A także dla A nieborelowskiego.
3. **Prawostronny test mierzalności:** półproste (q,∞) o wymiernych q generują B(R). Z dopełnień otrzymujemy (-∞,q], z przeliczalnych sum (-∞,b), a przez sumy i przekroje półproste (a,∞) oraz przedziały (a,b) także dla rzeczywistych a,b. Zastosowanie kryterium generatorów jest poprawne.
4. **Mierzalność ograniczenia:** dla każdego B∈G zachodzi (f|_A)^{-1}(B)=A∩f^{-1}(B); ślad F|_A jest właściwą strukturą nawet dla A∉F.
5. **Minimalność sigma(f):** rodzina wszystkich przeciwobrazów jest sigma-algebrą dzięki zachowaniu dopełnień i sum przeliczalnych; dla dowolnego indeksu I wspólna sigma-algebra przeciwobrazów jest minimalna.
6. **Produkt i rzutowania:** pasy A×Y i X×B są przeciwobrazami rzutowań, prostokąt jest ich przecięciem; obie strony inkluzji generatorów dają równość. Kryterium mierzalności h przez współrzędne ma sprawdzone oba kierunki.
7. **Borelowska struktura produktu:** rzutowania zapewniają jedną inkluzję, przeliczalne bazy obu topologii zapewniają przeliczalną bazę prostokątów i inkluzję odwrotną. Hipoteza drugiego aksjomatu przeliczalności jest jawna i poprawnie nazwana.
8. **Borelowskie odwzorowania wektorowe:** dla d≥1 indukcja daje B(R^d)=⊗_{j=1}^d B(R); wielokrotne zastosowanie własności produktu sprowadza mierzalność do wszystkich współrzędnych.
9. **Przeliczalne generowanie standardowej przestrzeni borelowskiej:** z metryki zupełnej i separowalnej powstaje przeliczalna baza kul, a jej przeciwobrazy przy izomorfizmie generują F i rozdzielają punkty. Sprawdzono konieczność mierzalnej odwrotności b.
10. **Funktorialność miar obrazowych:** dla C∈H równość ((g∘f)_#μ)(C)=μ(f^{-1}(g^{-1}(C)))=(g_#(f_#μ))(C) jest poprawna bez założeń skończoności miary.

**Wynik matematyczny: 10/10 PASS.** Nie stwierdzono nowej wykazanej luki uzasadnienia, brakującego założenia lub błędnej implikacji.

## 3. Weryfikacja 5/5 przykładów, dwóch uwag i istotnych przypadków brzegowych

- **Nie-Borelowski A:** B(R)|_A jest zawsze sigma-algebrą na A, chociaż rodzina podzbiorów A będących borelowskimi w R może nie zawierać A; rozróżnienie jest prawidłowe.
- **Skończona sigma(f):** wartości funkcji grupują punkty w dokładnie dwie nierozróżnialne pary; wyliczone cztery zbiory sigma(f) są poprawne.
- **Standardowe przestrzenie borelowskie:** R^d, N z metryką dyskretną i {0,1}^N z metryką rho są polskie; sprawdzono zupełność rho, zgodność z topologią produktową i gęstość ciągów ostatecznie zerowych. Definicja metryki rho została potwierdzona w przywołanym R04.
- **Uzupełnienie Lebesgue'a:** każda sigma-algebra przeliczalnie generowana ma moc co najwyżej continuum (preobrazy zbiorów borelowskich przestrzeni Cantora); L_1 zawiera 2^continuum podzbiorów zbioru Cantora, więc nie może być standardowa borelowska.
- **Funkcja stała i miara obrazowa:** przeciwdziedzina (Y,G), źródło (X,F), punkt y0, μ i kwantyfikacja B∈G zostały doprecyzowane w audycie XXVIII. Osobno zbadano μ(X)<∞, μ(X)=∞ i sytuację, gdy singleton {y0} nie jest mierzalny; funkcja B↦χ_B(y0) nadal definiuje miarę na dowolnej G.

**Uwagi:** dla dyskretnego D o mocy większej niż continuum przekątna Δ jest zamknięta, lecz nie jest w P(D)⊗P(D). Każdy zbiór z sigma-algebry generowanej przez dowolną rodzinę pochodzi z przeliczalnej podrodziny; argument z rozróżnianiem (x,x) i (x,y) wymusza iniekcję D→{0,1}^N i sprzeczność. Definicja standardowości przez pewną polską topologię jest równoważna z definicją przez izomorfizm mierzalny.

**Wynik: 5/5 przykładów i 2/2 uwag bez nowych usterek.** Rozdział R05 nie zawiera rysunków, zatem nie ma etykiet graficznych do skorygowania.

## 4. Nowa niezależna regresja rachunkowa (rzeczywiście uruchomiona)

Napisano i uruchomiono w tej sesji **osobną lokalną implementację** skończonej sigma-algebry przez iterowanie zamknięcia na dopełnienia i **binarne sumy** zbiorów; jest to inny algorytm niż test repozytorium korzystający z podziałów na atomy. Wyniki lokalnego Pythona:

- **2048/2048** przypadków śladu i generowania: PASS;
- **675/675** przypadków minimalności sigma(f) dla różnych mierzalnych struktur na trójelementowych zbiorach X i Y: PASS;
- **10/10** par sigma-algebr na zbiorach odpowiednio 2- i 3-elementowych dla produktu przez prostokąty versus rzutowania: PASS;
- **576/576** przypadków funktorialności miar obrazowych z wagami (2,0,3): PASS.

Skończone regresje **nie są dowodem** twierdzeń ogólnych o dowolnych przestrzeniach ani kontrprzykładu kardynalnego.

## 5. Niezależne kontrole źródła, odsyłaczy, języka i PDF

Aktualne źródło R05 i kontekst etykiet R01–R04 pobrano ponownie przez GitHub API. R05: **15 etykiet, 15 odsyłaczy, 0 brakujących celów, 0 duplikatów etykiet w R01–R05, 0 nieparzystych środowisk**. Brak terminów „drugoprzeliczalny”, „pierwszoprzeliczalny”, „unia zbiorów”, „zbieżność zdominowana” oraz zabronionych oznaczeń funkcji charakterystycznej. Konsekwentnie stosowana jest notacja χ_A (także χ_{B_n} w dowodzie o przekątnej). Dotychczasowe stabilne etykiety zachowane.

Odczytano **rzeczywiste logi PDF** z artefaktu 14803168957 i ponownie wizualnie obejrzano wszystkie pięć pełnowymiarowych stron /mnt/data/measure_ch05_render/page-1.png … page-5.png. Brak uciętych wzorów, nakładających się napisów i zniszczonych nagłówków. **Izolowany PDF R05: 5 stron A4, 0 Overfull hbox, 0 Underfull hbox.** Nierozwiązane odsyłacze międzyrozdziałowe w izolowanym PDF są spodziewane, gdyż źródła R01–R04 nie są w nim włączone. W pełnej książce referencje są rozwiązane. Niezależna lokalna kontrola granic słów za pomocą PyMuPDF wykazała 1967 tokenów/wyrazów według jego własnego podziału, **0 poza stronami**; Poppler w CI wykazał 2313 wyrazów według innej tokenizacji, również **0 poza stronami**.

Ponownie odczytano rzeczywisty przebieg CI: [45145807540](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45145807540) na commicie 0998b705520c0144fb72fea6165abad34809fea4: **2/2 zakończone joby SUCCESS**; testy, dwukrotna kompilacja izolowanego R05, pięć podglądów PNG i trzykrotna kompilacja kompletnej książki (256 stron) zostały faktycznie wykonane. Zmiana samego raportu audytu XXVIII nie modyfikowała źródła ani testów, więc wskazany zielony run pozostaje adekwatny dla obecnego bloba R05. Ostrzeżenia Underfull globalnej książki nie są nowymi problemami R05; izolowane R05 ma ich zero.

## 6. Jednoznaczny status stabilizacji

**ROZDZIAŁ 05 — STABILNY / FORMALNIE ZATWIERDZONY.**

Uzasadnienie: audyt I wykrył i poprawił cztery usterki sformułowań i hipotez, następnie pomyślnie przeszedł pełny CI i inspekcję PDF. Bieżący **kolejny, niezależny audyt II po ostatniej poprawce źródła** ponownie objął matematykę (10/10 dowodów, 5/5 przykładów, 2/2 uwag), język, hipotezy, terminologię, strukturę LaTeX, 15/15 odsyłaczy, PDF 5/5 stron, automatyczne CI 2/2 oraz niezależne regresje. **Nie znaleziono nowych usterek, więc nie wykonywano poprawek i nie ma potrzeby ponawiania audytu po zmianie.**

**Status poprzednich rozdziałów R01–R04: STABILNE, bez zmian.** Nie audytowano ani nie edytowano R06–R31.

**Następna iteracja:** rozpocząć audyt I rozdziału 06 „Funkcje mierzalne i ich aproksymacja”. Zgodnie z zasadą jednego rozdziału na iterację nie rozpoczynać R06 w tym audycie.
