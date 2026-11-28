# Logika matematyczna i teoria mnogości — audyt X rozdziału 35

**Data:** 22 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/logic_and_set_theory/35-modele-boolowskie-i-wzgledna-niesprzecznosc-ch.tex`.  
**Blob źródła:** `1d510628d52469ef8aa00ad021125192c54ec439` (bez zmian w audycie X).  
**Werdykt końcowy: audyt X CZYSTY (1/2).** Nie ujawniono nowego błędu ani koniecznej poprawki treści. Pełne GitHub Actions przebiegu 45061439175, analiza logu i nowa wizualna kontrola wszystkich 16 stron rozdziału zakończyły się pomyślnie. Poprzedni audyt IX pozostaje nieczysty; pierwszy czysty audyt dotyczy dokładnie bloba wskazanego wyżej.

## 1. Niezależne ponowne sprawdzenie dowodu

1. **Regularna algebra:** ograniczenie RO(X) do niepustego X usuwa przypadek degeneracji 0=1. Przy topologii stożków obrazy warunków są niezerowe i gęste; zgodność i niezgodność warunków odpowiadają niezerowości/przeciwieństwu ich przecięć.
2. **Rekurencja nazw:** każda współrzędna nazwy ma niższą rangę; klauzule atomowe wyznaczają element algebry. Dla ustalonej formuły zbiór *różnych* wartości jest podzbiorem B, mimo że klasa nazw jest właściwa.
3. **Równość i świadkowie:** ponownie prześledzono równoczesną indukcję dla przechodniości i podstawiania, lemat mieszania z możliwymi zbieżnościami nazw oraz ograniczenie rang kandydatów przed wyborem na zbiorze. Pełność nie zakłada domknięcia ultrafiltru na dowolne kresy.
4. **Wszystkie aksjomaty:** dla `check a` zachowujemy atomowe wartości 0/1. Przeanalizowano szczególnie konstrukcję nazwy pary, `check omega` jako zbioru induktywnego, nazwę sumy, zbioru potęgowego, obraz przez funkcję przy zastępowaniu, minimalizację rang przy ufundowaniu i odwzorowanie surjektywne z podzbioru liczby porządkowej przy wyborze.
5. **Iloraz:** w przypadku dowolnego zewnętrznego ultrafiltru poprawność klas i indukcja po standardowej formule wynikają z podstawiania i pełności wartości. Nie utożsamiano modelu nieufundowanego z modelem tranzytywnym.
6. **CH i jej zaprzeczenie:** niezależnie skontrolowano argument ccc dla Add(omega,omega_2), brak surjekcji z mniejszych porządków na omega_1 i omega_2, iniekcję omega_2 w zbiór reals, przeliczalną domkniętość Coll(omega_1,2^aleph_0), brak nowych podzbiorów omega, zachowanie omega_1 i konstrukcję surjekcji omega_1 na stary zbiór reals. Wyprowadzenie względnej niesprzeczności używa pełności logiki pierwszego rzędu i modeli ilorazowych; nie zakłada istnienia przeliczalnego modelu tranzytywnego.

Żaden z ponownie przeanalizowanych kroków nie wymagał zmiany źródła w tej iteracji. Nie dodawano niezatwierdzonego materiału ani nie zmieniano ustalonego zakresu.

## 2. Nowa, niezależna regresja mieszania

Dodano `test_mixing_for_nonmaximal_antichains_and_zero_coefficients` do `tools/tests/test_logic_and_set_theory_ch35.py` (commit `7112f096338146174995447d5ddf50ef0110089d`). Test oblicza wartości równości i przynależności przez niezależną, rekurencyjną semantykę na 8-elementowej algebrze Boole'a. Obejmuje cztery rodzaje antyłańcuchów, w tym niemaksymalne, pary składające się z nieatomowych wartości, współczynniki zerowe i nazwy z identycznymi argumentami. Wykonuje **960** sprawdzeń nierówności `a <= [[mixed = tau_a]]`.

Kontrolny rachunek lokalny o tych samych parametrach dał **960/960 zgodności**. W przebiegu GitHub Actions **[45061439175](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45061439175)** krok testów rozdziału 35 (23 metody po uzupełnieniu) zakończył się **SUCCESS**.

## 3. Pełne CI i niezależna inspekcja rzeczywistego PDF

**GitHub Actions [45061439175](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45061439175): SUCCESS**, commit `7112f096338146174995447d5ddf50ef0110089d`. Przebieg obejmował 23 testy rozdziału 35, testy pozostałych rozdziałów, inwentarz i odsyłacze, pełną kompilację książki oraz kontrolę logu i gotowego PDF.

Pobrano rzeczywisty ZIP artefaktu **14769179583** z przebiegu. Dokument `logic_and_set_theory.pdf` ma **311 stron**. Rozdział 35 obejmuje strony PDF **296–311** (16 stron). Wyrenderowano wszystkie 16 stron w nowym montażu 4 × 4 i niezależnie skontrolowano układ, brak uciętych wzorów oraz brak nakładających się elementów. Nie stwierdzono nowej usterki wizualnej.

Analiza logu kompilacji: **0** komunikatów `Overfull \\hbox`, **0** nierozwiązanych odsyłaczy, **0** brakujących znaków, **0** błędów `LaTeX Error`, **0** błędów `Undefined control sequence`; jedno ostrzeżenie `Underfull \\hbox` w całym dokumencie, bez wpływu na czytelność rozdziału.

## 4. Werdykt i dalszy etap

**Pierwszy niezależny czysty audyt źródła `1d510628d52469ef8aa00ad021125192c54ec439`: 1/2.** Test został rozszerzony bez zmiany źródła rozdziału. Następna iteracja to audyt XI na tym samym blobie, z własną kontrolą przypadków brzegowych, dowodów zachowania ZFC i przejścia do CH oraz ¬CH. Następnie wymagany jest dodatkowy audyt potwierdzający stabilność, zanim rozpocznie się rozdział 36.

Sukces CI i testów skończonych algebr Boole'a nie oznacza weryfikacji dowodów w Lean.
