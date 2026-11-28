# AA-43 — audyt 3: końcowa stabilizacja matematyczno-redakcyjna

**Data:** 23 listopada 2026 r.  
**Werdykt:** **AA-43 STABILNY** na istniejącej gałęzi `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/abstract_algebra/43-ciala-rozniczkowe-derywacje-i-rozszerzenia.tex`.  
**Aktualny blob SHA źródła:** `c6563f402b7890e5e0c8f02796ebf649f4336906`; test 1 SHA `b65cbffc504b9c8bf18d3754b12c8a828fec9efe`, test 2 SHA `ce4565343a52df2a01df3a4bcdbba540562416ad`.

## 1. Kontrole matematyczne

Kontrolowano twierdzenia i lemata od definicji derywacji do rozszerzeń elementarnych, w powiązaniu z AA-20 i AA-23. Łącznie **6 pełnych dowodów i 9 przykładów**:

1. Reguły derywacji, pole stałych i funkcje wymierne: szczególne przypadki z zerowym licznikiem, niezerowym mianownikiem i elementami stałymi.
2. Jednoznaczne przedłużenie derywacji na dowolne rozszerzenie algebraiczne **w charakterystyce zero**: sprawdzenie niezerowości $m'(\alpha)$, jednoznaczności przedstawicieli w $K[\alpha]$ i zgodności na wszystkich skończonych podrozszerzeniach.
3. Brak nowych stałych dla rozszerzeń algebraicznych z **algebraicznie domkniętym ciałem stałych**. Kontrprzykład $\mathbb Q(x)\subset\mathbb Q(i)(x)$ bez tego warunku.
4. Derywacja śladu i logarytmicznej normy dla rozszerzeń skończonych, niekoniecznie normalnych; porównanie z AA-23 i ręczny przypadek kwadratowy.
5. Dokładne kryterium braku nowych stałych dla dołączenia przestępnej funkcji pierwotnej $Dt=a$: konieczność i dostateczność braku $b\in K$ z $Db=a$, z obsługą **ujemnych wykładników** w formalnych rozwinięciach Laurenta.
6. Dokładne kryterium dla przestępnego elementu wykładniczego $Dt=ht$: wykluczenie wszystkich par $m\in\mathbb Z\setminus\{0\}$, $u\in K^\times$ spełniających $Du/u=-mh$.

Dodatkowo sprawdzono definicję rozszerzenia elementarnego w odróżnieniu od rozszerzenia liouvillowskiego. Rozdział nie przedstawia jeszcze twierdzenia Liouville'a jako dowiedzionego: pełen dowód jest zaplanowany dla AA-44.

## 2. Rzeczywiście usunięte problemy

**Problem 1 — uzasadnienie interpretacji analitycznej.** W drugim audycie dopisano dowód, że lokalna gałąź $\log x$ jest przestępna nad $\mathbb C(x)$: w przeciwnym razie z różniczkowania śladu wynikałaby wymierna funkcja pierwotna $1/x$, sprzecznie z zerową resztą pochodnej funkcji wymiernej. Commit `200ff367dd85793ab8e01ccedfc12bc8543a8d91`.

**Problem 2 — tautologiczne sprawdzenie w teście.** Usunięto redundantny przypadek sprawdzający równość wyrażenia z samym sobą. Pozostały ścisłe tożsamości równań minimalnych, reguły Leibniza, śladu i normy. Commit `d02dd2da56bd62b236530d4f98e22e1875e86821`.

**Problem 3 — długi nagłówek bieżący.** Pierwsza pełna kompilacja produkowała **pięć ostrzeżeń `Overfull \hbox`**, wszystkie dotyczące powtarzanego, zbyt długiego nagłówka AA-43. GitHub Actions prawidłowo odrzucił ten PDF mimo pozytywnych testów matematycznych. Dodano osobne `\chaptermark{Ciała różniczkowe i derywacje}`, zachowując pełną nazwę rozdziału i tytuł w spisie treści. Commit `bfabbf421e014e238e47e73383ceeb94c5dfc9cd`. Drugi przebieg pełnej kompilacji usunął usterkę.

## 3. Zdalne testy, rzeczywisty przebieg CI

**Zielony pełny przebieg:** [GitHub Actions 45148711050](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45148711050), na commicie `bfabbf421e014e238e47e73383ceeb94c5dfc9cd`.

Stan końcowy: **completed / success**, zadanie `validate-cli` **77/77 kroków zakończonych**, bez porażek. Z rzeczywistych kroków:
- `Run AA-43 algebraic derivations and differential extensions`: **success**, **11/11 metod unittest PASS**, model SymPy.
- `Run AA-43 independent exact rational audit`: **success**, **5/5 metod unittest PASS**, niezależny model `fractions.Fraction` bez SymPy.
- `Run AA-GLOBAL canonical book and audit-coverage gate`: **success**, dokładnie **43 rozdziały**, bez duplikatów ani brakujących odsyłaczy.
- `Compile AA-01 to AA-43 book with latexmk`: **success**.
- `Verify PDF and references (no undefined refs)`: **success**.
- `Archive build output`: **success**.

Dwa zestawy testów nie są równoważne formalnemu dowodowi w Lean; wzajemnie kontrolują jednak niezależnymi obliczeniami główne formuły w licznych dokładnych przypadkach.

**Globalna bramka źródeł w tym przebiegu:**
- **43** pliki rozdziałów, prawidłowa kolejność wszystkich `\input`;
- **864/864** unikatowe etykiety, **0** duplikatów;
- **377** wystąpień odsyłaczy, **246** różnych celów, **0** brakujących celów;
- **405** dowodów, **276** przykładów;
- 11 poprzednich raportów przekrojowych nadal pokrywa **42** historyczne rozdziały; AA-43 ma oddzielny cykl trzech audytów.

## 4. Rzeczywisty finalny PDF i oględziny

Pobrany artefakt **`abstract-algebra-aa01-aa43`**, ID **14806045960**, pochodzi bezpośrednio z ww. udanego workflow. Zawiera:
- `abstract_algebra.pdf` — **275 stron**, **2 057 602 B**, SHA-256 **`d6c57a6d98c58e04d1cc358b5904942d10e1e564de9eae3b4b2f41a068f09fdb`**, `is_repaired=False`;
- `abstract_algebra.log` — **45 434 B**, SHA-256 **`6dc33fabea9a3832002fba15c2d09eea30b250c91cf6d7779008b6aba5efe0bc`**.

**Końcowy log ma 0 błędów `LaTeX Error`, 0 ostrzeżeń `LaTeX Warning`, 0 ostrzeżeń `hyperref`, 0 przepełnionych i niedopełnionych wierszy/kolumn `hbox/vbox`, 0 nierozwiązanych odsyłaczy, 0 żądań ponownego przeliczenia odsyłaczy.**

Nowy AA-43 zajmuje dokładnie **6 stron PDF: 270–275**, o numerach drukowanych 261–266. Wyrenderowano i **obejrzano każdą** z tych sześciu stron z końcowego artefaktu, łącznie z nagłówkami i całym blokiem wzorów. Nie wykryto obcięć, kolizji ani nieprawidłowych symboli.

Dla zachowania poprzedniej stabilnej części książki porównano wszystkie strony PDF **10–269** z finalnym artefaktem poprzedniego globalnego audytu AA-01–AA-42: **260/260 stron pikselowo identycznych** przy 72 dpi i **260/260 identycznych warstw tekstowych**. Współrzędne **143 552** słów w całym nowym 275-stronicowym PDF: **0** pozycji poza granicami stron.

## 5. Decyzja

**AA-43 STABILNY**, bez otwartych usterek w zadeklarowanym zakresie kontroli. Wykonano realną redakcję, dwa następujące po sobie niezależne audyty matematyczne, korekty w źródle i teście, dwa niezależne zestawy regresyjne, pełne CI, weryfikację dokładnych odsyłaczy, całej książki i kontrolę składu każdej nowej strony.

W następnym etapie można rozpocząć **AA-44 — twierdzenie Liouville'a i kryteria całkowalności elementarnej** zgodnie z `docs/pl/plan_algebry_abstrakcyjnej_aa43_plus.md`, nadal z zasadą „jeden rozdział, aż do stabilizacji”. Nie istnieje jeszcze gotowy, stabilny AA-44, więc nie należy uznawać planu za jego wykonanie.
