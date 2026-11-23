# Teoria miary / Miara i całka — rozdział 09, audyt I (iteracja globalna XXXVI)

**Data:** 2026-11-23. **Gałąź:** biblioteka-matematyczna-iteracja-6 (istniejąca, bez tworzenia nowej).  
**Jedyny audytowany rozdział:** chapters/pl/measure_theory/09-rodzaje-zbieznosci-funkcji-mierzalnych.tex.  
**Blob wejściowy R09:** 8595574911fd5b0edb902236bf9d97661ef18ee6.  
**Blob R09 po poprawkach:** 54e07e3433ca0569bdc0ba7c302ed143d21fe994.

## 1. Rzeczywisty punkt wznowienia i ograniczenie zakresu

Przed rozpoczęciem odczytano bieżącą gałąź względem commitu c1a4d45a31d5c6ac2aea458ed64430fd40fce02b. Nowsze commity w tym momencie dotyczyły innych skryptów, a źródło R09 nie było zmieniane. Potwierdzono istniejący raport audits/measure_theory/35-rozdzial-08-audyt-II-stabilizacja-2026-11-23.md (blob 07c1de57653433b6223675642022b35cecddae2f), jednoznacznie zatwierdzający rozdział 08 jako **STABILNY**. Raport XXXVI jeszcze nie istniał.

Zapoznano się z AGENTS.md, docs/pl/standardy_terminologiczne.md oraz plikiem books/pl/measure_theory.tex. Rozdziały 01–08 odczytano **wyłącznie jako źródła definicji i etykiet do odsyłaczy R09**; nie przeprowadzano w nich nowych audytów, nie zmieniano ich źródeł i nie scalano materiałów. R10–R31 pozostawiono bez zmian. Cała iteracja dotyczy wyłącznie R09 i jego nowych testów/CI.

## 2. Kontrola matematyczna rozdziału

Po poprawkach R09 liczy **601 wierszy** (potwierdzone końcowym odczytem GitHub), **8 sekcji, 7 twierdzeń, 4 wnioski, 3 definicje, 10 środowisk dowodu, 5 przykładów, 4 uwagi oraz 1 rysunek TikZ**.

Sprawdzono następujące argumenty i przypadki brzegowe:

1. **Podstawowe relacje:** zbieżność jednostajna implikuje punktową i według miary bez warunku skończoności miary; zbieżność prawie jednostajna implikuje zbieżność prawie wszędzie i według miary. W dowodzie wzór na zbiór punktów bez zbieżności punktowej jest przeliczalną kombinacją zbiorów mierzalnych. Zbieżność prawie wszędzie implikuje zbieżność według miary przy skończoności μ(X).
2. **Twierdzenie Jegorowa:** przy μ(X)<∞ dla ustalonego progu 1/m ogony złych zbiorów mają miarę dążącą do zera dzięki ciągłości z góry; odpowiednie progi m i sumowanie błędów miary dają jeden mierzalny zbiór wyjątkowy o mierze <η. Poza nim zbieżność jest jednostajna. **Doprecyzowano przypadek X\E=∅**, by zapis przez supremum był jednoznaczny.
3. **Wersja lokalna Jegorowa:** przy wyczerpaniu X przez rosnące zbiory skończonej miary można użyć progów η·2^{-(j+1)}, a suma zbiorów wyjątkowych ma miarę <η. Wniosek dotyczy zbieżności jednostajnej na każdym X_j\E osobno, nie globalnie.
4. **Kryterium wszystkich podciągów:** w kierunku do (ii) stosuje się wcześniejsze twierdzenie Riesza; odwrotnie wybiera się podciąg z odchyleniami o mierze co najmniej δ. Dalsza zbieżność prawie wszędzie daje sprzeczność z kontrolą według miary **właśnie dzięki μ(X)<∞**.
5. **Czebyszew i Lp:** próg ε^p dla |f_n−f|^p; zbieżność w Lp implikuje zbieżność według miary także przy μ(X)=∞, jeżeli normy różnic dążą do zera.
6. **Zupełność dla ciągów Cauchy'ego według miary:** dobór n_k z błędami i miarami <2^{-k}, pierwsza część lematu Borela–Cantellego i sumowalność przyrostów na zbiorze dobrym dają skończoną granicę punktową. Kontrola miary sumy złych zbiorów pozwala uzyskać zbieżność podciągu według miary **bez finitości μ(X)**. Warunek Cauchy'ego przenosi zbieżność na pełny ciąg. Zastosowano właściwą konwencję mierzalnego zbioru zerowego w przestrzeni niezupełnej.
7. **Metryka zbieżności według miary:** wzór rho([f],[g])=∫min(1,|f−g|) dμ definiuje wartość skończoną dla μ(X)<∞ i nie zależy od reprezentantów. Nierówność trójkąta wynika z min(1,a+b)≤min(1,a)+min(1,b); tożsamość nierozróżnialnych jest równością prawie wszędzie. Oba kierunki równoważności zbieżności rho i zbieżności według miary wynikają z oszacowań ze stałym ε.
8. **Zupełność rho:** z Cauchy'ego w rho wynika Cauchy według miary; wcześniejsze twierdzenie z punktu 6 daje granicę, a wynik metryzacyjny zapewnia zbieżność rho.
9. **Zbieżność lokalna i globalna:** warunek (i) kontroluje błędy na każdym X_j, a (ii) zabezpiecza przed ucieczką masy poza wyczerpanie. Oba warunki są konieczne; ich łączna dostateczność wynika z podaddytywności i kolejności granic limsup_n oraz j→∞.
10. **Lemat Scheffégo:** dla nieujemnych całkowalnych f_n,f i zbieżności prawie wszędzie mamy min(f_n,f)→f i 0≤min(f_n,f)≤f, więc zbieżność zmajoryzowana daje zbieżność całek minimum. Tożsamość |f_n−f|=f_n+f−2min(f_n,f) kończy dowód bez nieokreślonych wyrażeń ∞−∞.

Zbadano również **5/5 przykładów** (brak implikacji p.w.→według miary na mierze nieskończonej, niewykonalność globalnego Jegorowa na R, „maszyna do pisania”, koncentracja masy przy zbieżności p.w. bez L¹, zbieżność lokalna bez globalnej) oraz **4/4 uwagi**. W testowanych stwierdzeniach i argumentach nie wykazano nowego błędnego wzoru ani niepoprawnego twierdzenia wymagającego zmiany zakresu rozdziału.

## 3. Zmiany wykonane w źródle

Wprowadzono **wyłącznie niezbędne doprecyzowania istniejących wyników** — bez nowych rozdziałów, twierdzeń, zmian etykiet i bez edycji wcześniejszych rozdziałów:

1. **Commit d66285eef54dd520570919eff19dfa0b8e4ecbd5:** uzupełniono jawnie przestrzeń z miarą oraz mierzalne funkcje w definicji pięciu rodzajów zbieżności, definicji zbieżności Lp i ciągu Cauchy'ego według miary; także we wnioskach o lokalnym Jegorowie, kryterium wszystkich podciągów, zupełności metryki oraz gęstościach prawdopodobieństwa.
2. **Commit a767b5a652034fc7619fadbbfbfe9ac8024c453c:** doprecyzowano twierdzenie Jegorowa dla X\E=∅; przyjmujemy supremum nieujemnej funkcji po zbiorze pustym równe 0, zgodnie z definicją zbieżności jednostajnej.
3. **Commit 60385f8e0e8a73b4668a72e72a3d60ed95d4ea7f:** uzupełniono jawnie przestrzeń z miarą w twierdzeniu Czebyszewa, metryzacji zbieżności według miary, kryterium lokalnego/globalnego i lemacie Scheffégo.
4. **Commit d969846f39f9c649baf36baa75c183b918ffb88e:** usunięto powtórzenie hipotezy mierzalności zbiorów w kryterium lokalnym/globalnym i skorygowano zgodność gramatyczną w sformułowaniu lematu Scheffégo.

**Aktualny źródłowy blob: 54e07e3433ca0569bdc0ba7c302ed143d21fe994.** Każda zmiana została potwierdzona przez ponowny odczyt GitHub API.

## 4. Nowe dokładne regresje i faktyczny GitHub Actions

Dodano tools/test_measure_theory_ch09.py, commit **b776518468ec1a813b4d09fb06c577ffbc545b62**, oraz poprawiono kontrolę poruszającego się nośnika tak, aby zamiast tautologii porównywała dokładnie długości przecięć z przedziałami [-R,R] (commit **266f876716c4a3dccab9531b3b3a3c0f575fce07**). Ostateczny blob testu: **1a9e5dca5137fc712161ff09941ed41296bf8cd8**.

Nowy workflow .github/workflows/measure-theory-ch09.yml, commit **e6b916ba5303ef47161090ceda9703a75a27d97c**, blob **3e950859790e3906b35c5b447313afee128e5f7c**. Uruchamia niezależnie test matematyczny i kompilację PDF/całej książki, weryfikuje 20 odsyłaczy, kontrolę położenia wszystkich słów oraz generuje PNG dla każdej strony rozdziału.

**Ostateczny, rzeczywiście zakończony przebieg po wszystkich korektach źródła:** [GitHub Actions 45155567451](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45155567451), commit **d969846f39f9c649baf36baa75c183b918ffb88e**, **2/2 joby completed SUCCESS**. W autentycznym logu testów:
- **36 864 PASS** — wszystkie badane nierówności trójkąta rho z uwzględnieniem zerowych atomów i ilorazu przez równość p.w.;
- **2025 PASS** — dokładne oszacowania Czebyszewa dla wag i p=1,2,3;
- **2304 PASS** — dyadyczne bloki funkcji „maszyny do pisania”;
- **200 PASS** — dokładne modele gęstości prawdopodobieństwa w lemacie Scheffégo;
- **PASS** — przypadek Egorowa z zerowym atomem oraz pustym dopełnieniem;
- **448 PASS** — dokładne długości przecięć ruchomych nośników z [-R,R];
- **PASS** — 20 odsyłaczy R09, wszystkie środowiska LaTeX, terminologia i podstawowe hipotezy.

Skończone testy są regresją, **nie stanowią dowodu twierdzeń ogólnych**.

## 5. Skład izolowanego rozdziału i kompletnej książki

Przebieg CI wykonał **2 rzeczywiste kompilacje pdflatex izolowanego R09** oraz **3 kompilacje całej książki**. W izolowanym rozdziale powstało **7 stron A4**, kontrola Popplera potwierdziła **3497 słów w granicach stron** oraz **7/7 podglądów PNG**. Pełna książka ma **257 stron**; workflow nie wykrył brakujących odsyłaczy, duplikatów etykiet ani przepełnionych wierszy.

Pobrano prawdziwy ZIP artefaktu CI **14808292798** i rozpakowano go lokalnie do /mnt/data/r09_audit36_final. Zweryfikowano fizyczną obecność źródłowego PDF, wszystkich siedmiu podglądów oraz logów. Izolowany R09: **0 Overfull hbox, 0 Underfull hbox**; pełna książka: **0 Overfull hbox i 14 globalnych nieblokujących Underfull hbox** (pochodzą z całego skryptu, nie z izolowanego R09).

**Inspekcja wizualna wszystkich 7 stron:** utworzono zbiorczy podgląd i osobno obejrzano ostatnią stronę ze schematem implikacji. Wszystkie strzałki i podpisy są czytelne, bez nachodzących na siebie elementów, uciętych tekstów i błędnego kierunku implikacji. **Uwaga nieblokująca:** strona 7 jest niemal pusta poza schematem; można rozważyć jej lepsze zagospodarowanie w późniejszym audycie składu książki, ale nie wymaga to zmiany matematyki w tej iteracji. Ten sam wykres na starszym przebiegu był zgodny, a po aktualnych zmianach poprawna paginacja i rysunek zostały ponownie potwierdzone.

## 6. Odsyłacze, terminologia, poziom stabilizacji

Po poprawkach źródło R09 ma **22 etykiety, 20 odsyłaczy, 0 brakujących celów w R01–R09, 0 duplikatów etykiet, 0 niesparowanych lub niezamkniętych środowisk**. Nie znaleziono niezgodnych słów „sekwencji”, „unia zbiorów”, „zbieżność zdominowana”, „pierwszoprzeliczal”, „drugoprzeliczal” ani zastępczych oznaczeń funkcji charakterystycznych. We wszystkich wzorach stosowana jest konwencja \chi_A. Historyczne etykiety zachowano.

**R09 — NIESTABILNY / W TOKU STABILIZACJI.** Audyt I przeprowadził matematyczną i techniczną kontrolę całego rozdziału, doprecyzował formalne hipotezy i przypadek pustego zbioru, dodał nowe regresje i potwierdził 2/2 zielony CI oraz poprawny PDF. Ponieważ jednak **źródło zostało poprawione w tej samej iteracji**, warunkiem zatwierdzenia stabilności jest **kolejny, niezależny, pełny i czysty audyt rozdziału 09 już po tych zmianach**. Jeżeli audyt ten wykaże nowe błędy, należy je poprawić i kontynuować audyty R09.

**R01–R08 — STABILNE**, bez nowych audytów i zmian w tej iteracji. **R10–R31 — nieaudytowane i nieedytowane**.

**Następna iteracja:** globalny audyt XXXVII / R09 II, wyłącznie rozdział 09. Dopiero po jawnym zatwierdzeniu R09 można przejść do rozdziału 10.