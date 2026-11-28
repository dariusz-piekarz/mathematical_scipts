# Teoria miary / Miara i całka — rozdział 09, audyt II (globalny XXXVII): audyt czysty i formalna stabilizacja

**Data:** 2026-11-23. **Gałąź:** biblioteka-matematyczna-iteracja-6 (istniejąca, bez tworzenia nowej).  
**Jedyny audytowany rozdział:** chapters/pl/measure_theory/09-rodzaje-zbieznosci-funkcji-mierzalnych.tex.  
**Niezmieniony blob źródła R09 przed i po audycie:** 54e07e3433ca0569bdc0ba7c302ed143d21fe994.  
**Liczba zmian w źródle R09, jego testach i workflow:** 0 — przeprowadzono niezależny audyt po poprzednich poprawkach.

## 1. Punkt wznowienia i zakres

Przed rozpoczęciem porównano aktualną gałąź z ostatnim commitem raportu audytu XXXVI: 9c909da4e01b098653f8a593870463e4d5b63815. Początkowo istniał jeden nowszy commit dotyczący algebry abstrakcyjnej, bez zmian R09. Odczytano poprzedni raport audits/measure_theory/36-rozdzial-09-audyt-I-2026-11-23.md, blob 9ac04674845f82b96db9e3d7a5233ba70344ab44: audyt XXXVI udokumentował uściślenia hipotez, definicji, gramatyki i przypadku X\E=∅ w twierdzeniu Jegorowa, ale słusznie nie nadał stabilności w iteracji z poprawkami. Raport XXXVII w chwili rozpoczęcia nie istniał.

Pobrano aktualną treść R09, test oraz workflow i ponownie skontrolowano ich niezmienione SHA. Odwołano się do AGENTS.md i docs/pl/standardy_terminologiczne.md. Źródła R01–R08 odczytano **jedynie do sprawdzenia etykiet i wcześniej udowodnionych faktów**. Nie przeprowadzano audytu ani edycji R01–R08; R10–R31 pozostają nietknięte. Nie scalano książek ani nie zmieniano katalogu. Niniejszy audyt dotyczy wyłącznie R09.

## 2. Nowy niezależny przegląd wszystkich 10/10 dowodów

Źródło po ostatnich zmianach ma **601 wierszy, 8 sekcji, 3 definicje, 7 twierdzeń, 4 wnioski, 10 środowisk dowodów, 5 przykładów, 4 uwagi, 1 rysunek TikZ**. Ponownie niezależnie przeanalizowano wszystkie argumenty:

1. **Podstawowe implikacje:** zbieżność jednostajna daje puste zbiory przekroczeń progów nawet przy μ(X)=∞; prawie jednostajna implikuje według miary przez dowolną tolerancję η. Zbiór punktów niezbieżności jest dokładnie sumą przeliczalną odpowiednich limsup zbiorów {|f_n−f|≥1/m}; jest więc mierzalny i miary zero w przypadku zbieżności prawie jednostajnej. Do implikacji p.w.→według miary potrzebna jest skończoność μ(X).
2. **Jegorow:** ogony A_{m,N} są mierzalne i maleją do podzbioru zbioru zerowego; skończoność μ(X) umożliwia ciągłość miary z góry. Wybór progów μ(A_{m,N_m})<η2^{-(m+1)} zapewnia μ(E)<η, a wspólny E działa dla wszystkich m. W nowej wersji jawnie określono supremum nieujemnej funkcji na pustym X\E jako 0 — bez zmiany treści twierdzenia.
3. **Lokalna wersja Jegorowa:** ograniczenie do X_j o skończonej mierze, sumowanie wyjątków E_j z wagami η2^{-(j+1)} i zawieranie X_j\E⊆X_j\E_j dowodzą zbieżności jednostajnej dla każdego ustalonego j. Bez globalnego wniosku o zbieżności jednostajnej.
4. **Kryterium wszystkich podciągów:** zbieżność według miary przenosi się na podciągi, a twierdzenie Riesza dostarcza dalszy podciąg zbieżny p.w.; jeśli zbieżność według miary nie zachodzi, można wybrać podciąg o stale dodatniej mierze przekroczeń progu, sprzeczny z p.w.→według miary na przestrzeni o mierze skończonej.
5. **Czebyszew dla Lp:** właściwy próg ε^p w nierówności Markowa i bezpośrednie przejście od całek |f_n−f|^p→0 do zbieżności według miary, bez wymagania μ(X)<∞.
6. **Zupełność Cauchy'ego według miary:** rekurencyjny podciąg n_k kontroluje różnice z progami 2^{-k}; sumowalność miar złych zbiorów i pierwsza część lematu Borela–Cantellego zapewniają p.w. sumowalne przyrosty, stąd skończoną granicę. Silniejsze oszacowanie przez sumę miar ogonów, a nie sama zbieżność p.w., dowodzi zbieżności podciągu **według miary również przy μ(X)=∞**. Warunek Cauchy'ego przenosi ją na cały ciąg. Granicę na mierzalnym zbiorze wyjątkowym poprawnie przedłużono zerem.
7. **Metryka zbieżności według miary:** ρ([f],[g])=∫min{1,|f−g|}dμ jest skończona przy μ(X)<∞, niezależna od reprezentantów, dodatnio określona na ilorazie i spełnia nierówność trójkąta. Oszacowanie miary przekroczeń przez ρ/min{1,ε} i nierówność odwrotna ρ≤εμ(X)+μ({|f_n−f|>ε}) wyznaczają dokładnie tę samą zbieżność.
8. **Zupełność metryki ρ:** ciąg Cauchy'ego w ρ jest Cauchy według miary, zatem ma mierzalną granicę według miary; poprzednie twierdzenie metryzacyjne zamienia ją na zbieżność w ρ.
9. **Kryterium przejścia od zbieżności lokalnej do globalnej:** zbiory X_j tworzą rosnące wyczerpanie o skończonych miarach. Warunek lokalny kontroluje część błędu wewnątrz X_j, warunek ogonowy (z kolejnością limsup_n, potem lim_j) zapobiega ucieczce masy; podaddytywność daje obie implikacje bez ukrytego założenia skończoności μ(X).
10. **Lemat Scheffégo:** dla nieujemnych, całkowalnych f_n,f, min(f_n,f)→f p.w. i jest zdominowana przez całkowalną f; DCT oraz skończoność wszystkich całek uzasadniają tożsamość dla |f_n−f| bez nieokreślonego ∞−∞.

**Werdykt matematyczny: 10/10 dowodów PASS; zero nowych wykazanych błędów albo brakujących założeń wymagających zmiany źródła.** Uściślenia z audytu XXXVI okazały się poprawne.

## 3. Przegląd przykładów, uwag i schematu implikacji

**5/5 przykładów i 4/4 uwagi — PASS:**

- Ciąg χ_[n,∞) na R: p.w.→0, ale miara błędu jest stale nieskończona, co odróżnia zbieżność według miary.
- Ruchome przedziały [n,n+1): niemożność globalnego Jegorowa przy zbiorze wyjątkowym skończonej miary; również brak globalnej zbieżności według miary przy zbieżności lokalnej.
- „Maszyna do pisania” na [0,1): w każdym bloku dyadycznym dokładnie jedno trafienie w każdy punkt; norma Lp^p równa 2^{-k}, ale nie ma zbieżności punktowej całego ciągu.
- f_n=nχ_(0,1/n): całka modułu jest stale równa 1, mimo zbieżności punktowej i według miary do zera.
- Gęstości prawdopodobieństwa: równość całek 1 oraz zbieżność p.w. prowadzą do L1 przez lemat Scheffégo; nie pomylono tego z wymogiem zbieżności punktowej wszędzie.

Sprawdzono logikę wszystkich strzałek diagramu: jednostajna→prawie jednostajna, prawie jednostajna→p.w. i według miary, Lp→według miary, a p.w.→według miary oraz p.w.→prawie jednostajna **wyłącznie przy μ(X)<∞**, co prawidłowo sygnalizują strzałki przerywane. Nie wskazano błędnej implikacji.

## 4. Niezależne faktycznie wykonane testy rachunkowe

W lokalnym środowisku uruchomiono osobny nowy skrypt **/mnt/data/r09_audit37_independent.py**, nieimportujący modułów repozytorium. Stosuje wyczerpujące modele z dokładną arytmetyką wymierną, osobno od repozytoryjnego tools/test_measure_theory_ch09.py. Wyniki rzeczywistego wykonania:

- **140625/140625 PASS** — nierówności trójkąta ρ i warunek zerowego dystansu na ilorazie dla dwupunktowych zbiorów i mas 0,1,4;
- **4500/4500 PASS** — dokładna nierówność Czebyszewa z różnymi progami, wagami oraz p=1,2,3,4;
- **2560/2560 PASS** — jednoznaczność trafienia punktu przez przedziały wszystkich dziesięciu poziomów dyadycznych;
- **1452/1452 PASS** — dokładny rachunek L1 dla rodzin gęstości o sumie mas 1;
- **1280/1280 PASS** — długość przecięcia ruchomych przedziałów [n,n+1) z [-R,R], a jednocześnie ich stała masa globalna;
- osobny pozytywny kontrprzykład dotyczący braku globalnej wersji Jegorowa przy miarze nieskończonej.

**Ograniczenie:** model skończony jest kontrolą regresyjną, nie dowodzi ogólnego twierdzenia Jegorowa ani zupełności na przestrzeni dowolnej miary. Te argumenty oceniono odrębnie w sekcji 2.

## 5. Język, odsyłacze, LaTeX, PDF i CI

Ponownie odczytano R01–R09 przez GitHub API **wyłącznie w celu weryfikacji odsyłaczy R09**: **22 etykiety w R09, 20 odsyłaczy, 0 niezdefiniowanych celów, 0 zduplikowanych etykiet w R01–R09, 0 niesparowanych i 0 niezamkniętych środowisk**. Nie znaleziono niedozwolonych zamienników χ_A ani terminów „sekwencji”, „unia zbiorów”, „zbieżność zdominowana”, „pierwszoprzeliczal” lub „drugoprzeliczal”. Zachowano wszystkie etykiety i nazwy wyników.

**Rzeczywisty run GitHub Actions** [45155567451](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45155567451) wykonał oba joby ze statusem **completed SUCCESS 2/2** na commicie d969846f39f9c649baf36baa75c183b918ffb88e. Ponownie sprawdzono ich aktualny wynik, dostępność artefaktu **14808292798** oraz różnice bieżącej gałęzi względem commitu CI: nowsze zmiany dotyczyły innych książek, aplikacji i raportu XXXVI; **nie zmieniono R09 ani testu/workflow**. Zielony wynik pozostaje więc odpowiedni dla audytowanego bloba R09.

Przebieg potwierdza dwa kompilowania izolowanego R09, **7 stron A4, 3497 słów Popplera**, 7/7 pełnych podglądów PNG, trzy kompilacje kompletnej książki (257 stron) oraz poprawne rozwiązanie odsyłaczy w całej książce. Nie wykazano błędów Overfull hbox ani brakujących referencji w pełnym składzie.

Lokalnie ponownie sprawdzono **autentyczny PDF** /mnt/data/r09_audit36_final/measure_theory_ch09_ci.pdf, 7 stron. W niezależnym od Popplera odczycie PyMuPDF znaleziono **2870 słów** (inna tokenizacja) i **0 słów wychodzących poza prostokąty stron**. Obejrzano wszystkie strony w zbiorczym podglądzie i powiększono diagram ze strony 7. Nie ma przecięć podpisów i strzałek, utraconych znaków lub błędnych kierunków połączeń. Dla izolowanego R09 log wykazał **0 Overfull hbox i 0 Underfull hbox**; nierozwiązane odsyłacze występują wyłącznie przy składzie izolowanym, kiedy nie dołączono wcześniejszych rozdziałów. W kompletnej książce **0 brakujących odsyłaczy, 0 Overfull hbox, 14 Underfull hbox** (nieblokujące ostrzeżenia globalnego składu).

**Jedyna uwaga estetyczna:** strona 7 zawiera zasadniczo sam schemat implikacji (35 słów według PyMuPDF), przez co jest słabo wykorzystana. Rysunek jest jednak czytelny i merytorycznie prawidłowy, a istniejący styl LaTeX nie generuje naruszeń składu. Nie jest to powód do zmiany matematyki ani do cofnięcia stabilizacji. Ewentualną optymalizację paginacji całej książki rozpatrywać jako oddzielną czynność redakcyjną bez naruszania ustabilizowanych treści.

## 6. Formalna decyzja

**ROZDZIAŁ 09 — STABILNY / FORMALNIE ZATWIERDZONY.**

Uzasadnienie: audyt XXXVI poprawił jawność hipotez, język i przypadek pustego zbioru w twierdzeniu Jegorowa, następnie zakończył rzeczywistym zielonym CI 2/2 i kompletnym PDF. Bieżący **drugi, nowy, niezależny, czysty audyt XXXVII już po tych poprawkach** ponownie zweryfikował wszystkie 10 dowodów, 5 przykładów, 4 uwagi, 22 etykiety, 20 odsyłaczy, obowiązujące standardy, schemat implikacji oraz autentyczny PDF. Nie stwierdzono żadnej nowej usterki wymagającej zmiany źródła; jego blob pozostaje **54e07e3433ca0569bdc0ba7c302ed143d21fe994**.

**R01–R08 — STABILNE**, bez ponownego audytowania i edytowania w tej iteracji. **R10–R31 — nieaudytowane ani niezmienione.**

**Następna osobna iteracja:** globalny audyt XXXVIII / R10 I, wyłącznie rozdział 10, bez rozpoczynania go w obecnym audycie.
