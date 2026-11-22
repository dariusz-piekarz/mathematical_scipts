# Logika matematyczna i teoria mnogości — audyt I rozdziału 36

**Data:** 22 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/logic_and_set_theory/36-modele-symetryczne-i-niezaleznosc-aksjomatu-wyboru.tex`.  
**Blob po poprawkach:** `6891b26609ccf77a0aaddc28653bb872f05a1701`.  
**Werdykt:** audyt I **nieczysty**: znaleziono i poprawiono dwie luki argumentacyjne oraz terminologię w świeżo utworzonym rozdziale. Licznik czystych audytów **0**.

## 1. Zakres

Skontrolowano samowystarczalność i formalną precyzję: definicję wymuszania Fn(ω×ω,2,<ω), działanie grupy permutacji, klasę dziedzicznie symetrycznych nazw, symetrię relacji wymuszania, dowód prawdy dla relatywizowanych kwantyfikatorów, aksjomaty ZF (szczególnie potęgowanie i Collection), konstrukcję nieskończonego zbioru Dedekinda skończonego, przejście do dowolnego przeliczalnego modelu ZFC oraz wniosek o niezależności AC od ZF.

## 2. Poprawki wymagane w audycie

1. **Negacja w lemacie prawdy.** W pierwotnym dowodzie podano gęstość warunków, które wymuszają negację **lub mają pewne wzmocnienie** wymuszające formułę. Samo posiadanie takiego wzmocnienia nie daje, że dany filtr generyczny zawiera to wzmocnienie. Poprawiono argument: właściwy zbiór gęsty składa się z warunków, które **same** wymuszają formułę lub **same** wymuszają jej negację. Jest to krok konieczny do poprawnego dowodu lematu prawdy. Commit `9e5a7a26e13300917a20c92f5023ea592a1252a6`.
2. **Kwantyfikacja po dowolnych nazwach elementów ω.** Z samego argumentu dla wszystkich nazw kanonicznych \(\check m\) trzeba jeszcze uzasadnić kwantyfikator ogólny dla każdej nazwy \(\dot m\), która może być z wartością dodatnią równa kanonicznemu elementowi \(\check\omega\). Dodano dokładne rozwinięcie przynależności do \(\check\omega\) i przejście po fragmentach wymuszania.
3. **Wniosek \(\operatorname{Con}(\mathrm{ZF})\Rightarrow\operatorname{Con}(\mathrm{ZFC})\).** Dodano jawny syntaktyczny argument: dowolny hipotetyczny dowód sprzeczności z ZFC jest skończony i można przenieść jego aksjomaty do interpretacji wewnętrznej \(L\) z rozdziału 31; uzyskałoby się sprzeczność z ZF.
4. **Terminologia.** Zmieniono nagłówek definicji na „Nazwy dziedzicznie symetryczne”.

Poprawki 2–4 znajdują się w commicie `5be4ad4f01f660511187b3b071c1d81197e515fc`.

## 3. Regresje i integracja

Nowy plik `tools/tests/test_logic_and_set_theory_ch36.py` zawiera **7 metod**: spójność wpisów w książce i katalogu, inwentarz LaTeX, znaczenie wniosku, zgodność działania permutacji z porządkiem wymuszania, 729 przypadków zagęszczania nierówności dwóch wierszy, 5103 przypadki konstrukcji świeżej współrzędnej dla argumentu o nośniku oraz rozróżnienie konstrukcji generycznej nad modelem nietranzytywnym. Testy są skończonymi regresjami, nie dowodem relatywnej niesprzeczności.

Dodano `\input` w `books/pl/logic_and_set_theory.tex`, wpis katalogu (36 rozdziałów) i zaktualizowano workflow `.github/workflows/logic-and-set-theory-chapter.yml` do rozdziałów 01–36. Po korektach inwentarza oczekiwane wartości: **900 etykiet i 701 odsyłaczy w całej książce**.

## 4. Statyczny inwentarz i dalsza walidacja

Dla bloba `6891b26609ccf77a0aaddc28653bb872f05a1701` zliczono: **938 wierszy, 21 różnych etykiet, 27 odsyłaczy, 5 definicji, 7 lematów, 4 twierdzenia, 3 uwagi, 1 przykład i 12 dowodów**. Środowiska LaTeX są poprawnie sparowane, nie wykryto naruszeń podstawowych zakazów terminologicznych.

Pierwszy nowy przebieg GitHub Actions, z poprawionymi licznikami i testami, to **[45064877027](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45064877027)**. W chwili zapisu niniejszego raportu **7 testów rozdziału 36 zakończyło się sukcesem**, a kompilacja całej książki trwała. Nie deklarujemy zakończenia całego CI przed potwierdzeniem jego wyniku i wizualnym sprawdzeniem rzeczywistego PDF.

**Następna iteracja:** audyt II od nowa na niezmienionym blobie `6891b26609ccf77a0aaddc28653bb872f05a1701`; każda kolejna konieczna poprawka resetuje licznik czystych audytów. Dopiero 2 czyste audyty oraz 1 audyt potwierdzający dają status stabilny.
