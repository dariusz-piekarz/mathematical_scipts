# Logika matematyczna i teoria mnogości — rozdział 26, audyt I

**Data:** 22 listopada 2026 r.  
**Rozdział:** `chapters/pl/logic_and_set_theory/26-aksjomat-wyboru-i-jego-rownowazne-postacie.tex`

## Integracja i kontrola zachowania treści
Źródłem był plik `26-axiom-of-choice-and-equivalent-principles.tex` z Biblioteki oraz pełniejsza wersja rozdziału 26 z `logika_teoria_mnogosci_iteracja_79.pdf` (strony 199–207). Zachowano formalizację AC, dobre porządki, twierdzenie Hartogsa, twierdzenie Zermela, lemat Zorna, zasadę maksymalności Hausdorffa i pełny dowód równoważności. Przywrócono też z dłuższej wersji: wybór ze skończonej rodziny, przekroje surjekcji, transwersale relacji równoważności, przykłady sum rozłącznych oraz dowód istnienia bazy przestrzeni wektorowej (w tym przypadek zerowy).

## Audyt matematyczny
1. **AC i pusta rodzina:** określono funkcję wyboru dla indeksowanego zbioru niepustych zbiorów. Dla pustego zbioru indeksów funkcja wyboru jest pusta; nie ma ukrytego wymagania wyboru z pustego zbioru.
2. **Porównanie dobrych porządków:** poprawiono rzeczywisty niedostatecznie uzasadniony krok. Zamiast ogólnego twierdzenia o iterowanej malejącej trajektorii przedstawiono indukcję dla ścisłego zanurzenia `f:W→W`, wykazując `x≤f(x)` przez sprzeczność po podstawieniu `y=f(x)`. Eliminuje to nieuzasadniony przeskok w dowodzie rozłączności przypadków.
3. **Hartogs bez AC:** konstrukcja zbioru klas izomorfizmu dobrych porządków na podzbiorach `A` opiera się na potęgowaniu i separacji, a nie na przyjętym wcześniej dobrym uporządkowaniu całego `A`. Wyjaśniono nieistnienie iniekcji `H(A)→A`.
4. **AC⇒dobre uporządkowanie:** jedna funkcja wyboru na niepustych podzbiorach `A`, uporządkowany argument Hartogsa oraz zgodność częściowych konstrukcji dają bijekcję z początkowego odcinka `H(A)` do `A`.
5. **Dobry porządek⇒Zorn:** konstrukcja maksymalnego łańcucha wybiera kandydatów względem pomocniczego dobrego porządku na zbiorze częściowo uporządkowanym. Rozróżniono maksymalny łańcuch, maksymalny element i największy element.
6. **Zorn⇒AC:** posłużono się częściowymi funkcjami wyboru uporządkowanymi przez przedłużanie; dla łańcuchów weryfikuje się istnienie ograniczenia górnego przez sumę, również dla łańcucha pustego.
7. **Pozostałe równoważności:** przekrój surjekcji odpowiada wyborowi z włókien; transwersala relacji równoważności odpowiada wyborowi po jednym reprezentancie klasy. W drugą stronę zastosowano indeksowaną sumę rozłączną, a nie zwykłą sumę.
8. **Baza przestrzeni wektorowej:** liniowo niezależne podzbiory tworzą zbiór w `P(V)`; suma łańcucha jest niezależna, maksymalność daje generowanie, niezależność jednoznaczność skończenie nośnych współczynników. Osobno sprawdzono `V={0}`.

## Inwentarz i walidacja
5 definicji, 10 przykładów, 1 lemat, 8 twierdzeń, 1 wniosek, 2 uwagi, 10 dowodów. 20 etykiet i 17 odsyłaczy. Testy `tools/tests/test_logic_and_set_theory_ch26.py`: PASS. GitHub Actions `45003169518`: SUCCESS, bez przepełnień i nierozwiązanych odsyłaczy. PDF rozdziału: 8 stron, wszystkie wyrenderowane i skontrolowane wizualnie.

**Werdykt:** audyt I wykonany z rzeczywistą poprawką matematyczną; zalecany drugi niezależny audyt stabilizacyjny.
