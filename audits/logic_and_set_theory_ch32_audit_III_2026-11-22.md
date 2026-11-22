# Logika matematyczna i teoria mnogości — rozdział 32, audyt III

**Data:** 22 listopada 2026 r.  
**Gałąź:** \`biblioteka-matematyczna-iteracja-6\`.  
**Źródło:** \`chapters/pl/logic_and_set_theory/32-podstawy-wymuszania-i-modele-generyczne.tex\`.  
**Zakres:** ponowne sprawdzenie wszystkich definicji, twierdzeń i dowodów; szczególnie absolutności nazw, zakresu lematu Rasiowej–Sikorskiego, wymagań dotyczących elementu największego, semantyki $M[G]$, przypadków Cohena, testów i składu.

## Usterki znalezione i naprawione

### 1. Niespójna definicja pojęcia wymuszania

Po audycie II ogólny lemat Rasiowej–Sikorskiego dotyczył już **dowolnego niepustego pojęcia wymuszania** w ZFC, lecz pierwsza definicja mogła być odczytana jako wymagająca *zawsze* warunku największego. Jest to niepotrzebne: np. dwu-elementowy porządek dyskretny nie ma elementu największego, a lemat nadal działa.

**Korekta:** definicja wymaga wyłącznie niepustości, zwrotności i przechodniości; element największy $1_{\mathbb P}$ zdefiniowano oddzielnie. Jego istnienie jest jawnie wymagane jedynie tam, gdzie korzystamy z nazw kanonicznych $\check x$, nazwy $\dot G$ i definicji $M[G]$ w tej wersji podręcznika. W ten sposób nie ma pozornej sprzeczności z lematem Rasiowej–Sikorskiego ani z gęstymi podporządkami.

### 2. Niedowiedzione wprost rozpoznawanie nazw wewnątrz modelu

Przy konstrukcji $M[G]$ nie wystarczy formalnie powiedzieć, że $\tau\in M$ i jest nazwą w otaczającym uniwersum; trzeba jeszcze upewnić się, że **model $M$ rozpoznaje tę samą własność**. Dotychczasowy argument ograniczania rang nazw z audytu II był poprawny, lecz nie wskazywał absolutności.

**Korekta:** rozszerzono istniejącą uwagę o rangach nazw. Jeśli $M$ jest tranzytywnym modelem ZFC, $\mathbb P\in M$ i $\tau\in M$, to bycie nazwą $\mathbb P$ jest absolutne między $M$ i otaczającym uniwersum. Dowód przebiega indukcją po **zwykłej randze zbioru** $\tau$: dla każdej pary $(\sigma,p)\in\tau$ mamy $\sigma\in M$ oraz rangę $\sigma$ mniejszą niż ranga $\tau$. Własność $p\in\mathbb P$ jest absolutna. Na mocy indukcji rozpoznanie nazwy $\sigma$ jest takie samo w obu strukturach. W przypadku pozytywnym $M$ przez zastępowanie zbiera wewnętrzne rangi pierwszych współrzędnych, ogranicza je wspólnym indeksem $\alpha$ i stwierdza $\tau\in N_{\alpha+1}^M$. W przeciwnym kierunku ta sama indukcja daje rozpoznanie nazwy w otaczającym uniwersum. Nie przypisujemy temu argumentowi statusu formalizacji w Lean; jest to dowód matematyczny w tekście.

### 3. Niejawne parametry definicji

W audycie uzupełniono założenia w definicjach **zgodności i antyłańcucha**, **gęstości**, **gęstego podporządku** i **wartości nazwy**: we wszystkich jawnie wskazano pojęcie wymuszania $(\mathbb P,\leq)$ oraz odpowiednie dziedziny zmiennych. Podobnie lemat o gęstości zbiorów $D_n$ explicite wskazuje, że dotyczy $\mathbb P_{\mathrm C}=\operatorname{Fn}(\omega,2)$ z porządkiem odwrotnego zawierania funkcji.

## Niezależna kontrola pozostałej treści

1. **Porządek i zgodność:** w dowodach kierunek $q\leq p$ konsekwentnie oznacza silniejszy warunek; implikacje dla zgodności i niezgodności są poprawne dla preporządku.
2. **Filtry:** definicja jest prawidłowo odwrócona względem kierunku wzmacniania; lemat o $D^\downarrow$ i przechodzenie do słabszych warunków nie zamieniają kierunków.
3. **Generyczność:** gęstość i zgodność z parametrami z $M$ są absolutne dla tranzytywnego modelu z relacją porządku należącą do $M$. Argument z $D_p$ jest poprawny.
4. **Rasiowa–Sikorski:** uogólnienie z audytu II jest poprawne w zewnętrznym ZFC. Użycie dobrego uporządkowania $\mathbb P$ daje ściśle zdefiniowane kolejne wzmocnienia, a otrzymany filtr przecina przeliczalną rodzinę gęstych zbiorów.
5. **Cohen:** gęstość $D_n$ i $E_x$ jest wykazana; każda para warunków w filtrze jest zgodna, zatem $\bigcup G$ jest funkcją; gęstość $E_x$ zapewnia, że jest różna od wszystkich ciągów binarnych modelu $M$.
6. **Gęsty podporządek:** konstrukcja $G$ z filtru $H$ i przenoszenie generyczności przez gęsty zbiór $D_{\mathbb Q}$ są poprawne.
7. **Nazwy i interpretacja:** rekurencja po rangach, ograniczoność rang zbioru pierwszych współrzędnych, interpretacje $(\check x)^G=x$ i $(\dot G)^G=G$ pozostają poprawne; uzupełniono absolutność rozpoznawania nazw.
8. **Zakres twierdzenia o $M[G]$:** nadal udowodniono jedynie tranzytywność i zawierania $M\subseteq M[G]$, $G\in M[G]$, bez nieuprawnionego stwierdzenia $M[G]\models\mathrm{ZFC}$. Pełne twierdzenie o wymuszaniu pozostaje w rozdziale 33.

## Regresje i technikalia

- Nie dodano twierdzeń ani lematów; zachowano wszystkie **33 etykiety** oraz **11 odsyłaczy**, 8 sekcji, 11 definicji, 7 lematów, 4 twierdzenia, 1 wniosek, 4 przykłady, 4 uwagi i 12 dowodów.
- W \`tools/tests/test_logic_and_set_theory_ch32.py\` dodano przypadek modelowego dwuelementowego porządku bez elementu największego i kontrolę obecności argumentu absolutności nazw. Te testy **nie są formalnym dowodem teorii mnogości**; służą wykryciu regresji.
- Wstępne przebiegi CI po korekcie definicji wykazały niezgodność **sztywno ustawionego licznika odsyłaczy** w istniejącym teście integracyjnym: nowa pomocnicza referencja zwiększyła inwentarz o jeden. Usunięto zbędny odsyłacz, przywracając pierwotną liczbę **11 odsyłaczy w rozdziale 32 i 590 w całej książce**, bez zmiany matematycznej treści.
- [GitHub Actions — wersja audytu III po poprawkach](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45016413451). **Status kompilacji i wizualnego przeglądu najnowszego PDF wymaga jeszcze odczytu z artefaktu**; wynik zostanie zaktualizowany po zakończeniu tego przebiegu.

## Werdykt wstępny

Audyt III naprawił niespójność definicyjną i doprecyzował absolutność nazw; dodatkowo uściślił samodzielność czterech definicji i jednego lematu. **Ocena stabilności wymaga jeszcze końcowego wyniku CI i inspekcji aktualnego PDF.** W kolejnym audycie należy ponownie rozważyć typografię ostatniej strony rozdziału, bez utraty matematycznych uzasadnień.
