# Logika matematyczna i teoria mnogości — audyt III rozdziału 35

**Data:** 22 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Źródło:** chapters/pl/logic_and_set_theory/35-modele-boolowskie-i-wzgledna-niesprzecznosc-ch.tex.  
**Status:** poprawki matematyczne wprowadzone; stabilność niepotwierdzona.

## Matematyka — niezależne sprawdzenie po audycie II

1. **Definicja wartości i równość.** Klauzule atomowe maleją ze względu na sumę naturalną rang. Zbiór różnych wartości formuły jest podzbiorem algebry Boole'a, a nie zbiorem wszystkich nazw. Uzupełniono skrótowy dowód tożsamości równości i podstawiania: osobne nierówności dla argumentów relacji przynależności, kontrola mniejszej rangi w indukcji, negacja na fragmencie równości oraz egzystencja z rozdzielnością kresów.
2. **Pełność.** Ponownie sprawdzono zagęszczenie poniżej wartości egzystencji, minimalizację rang, ograniczenie świadków do wspólnego zbioru nazw oraz mieszanie po maksymalnym antyłańcuchu. Żaden krok nie wymaga wyboru z klasy właściwej.
3. **Ufundowanie, zbiór potęgowy, zastępowanie.** Poprawione w audycie II argumenty zostały zbadane ponownie. W ufundowaniu minimalizuje się rangę wśród wszystkich nazw spełniających nierówność na niezerowym fragmencie; w zbiorze potęgowym należy uwzględnić nie tylko literalnie te same dziedziny; w zastępowaniu świadków trzeba ograniczyć do zbioru i sprawdzić oba kierunki równości na fragmencie funkcjonalności.
4. **Aksjomat wyboru.** Zastąpiono zbyt skrótowy argument nazwą zbioru indeksów K, nazwą grafu F surjekcji z K na zadany zbiór oraz wybraniem najmniejszych indeksów przeciwobrazów. Przez wyróżnianie i zastępowanie uzyskuje się bijekcję z dobrze uporządkowanym podzbiorem liczby porządkowej, bez błędnego założenia wyboru w modelu boolowskim.
5. **Iloraz przez dowolny ultrafiltr.** Lemat prawdy dla kwantyfikatora egzystencjalnego korzysta z lematu pełności. Dodano objaśnienie na przykładzie niegłównego ultrafiltru na P(omega): supremum singletonów jest równe jedynce, lecz żaden singleton nie należy do ultrafiltru. Nie wystarcza więc gołe przejście od supremum do składnika.
6. **Względna niesprzeczność.** Ponownie skontrolowano przejście od twierdzeń ZFC o wartościach boolowskich CH i jej zaprzeczenia do modeli ilorazowych. Z niesprzeczności ZFC twierdzenie o pełności logiki daje model zbiorowy, niekoniecznie tranzytywny. Zewnętrzny ultrafiltr w wewnętrznie zupełnej algebrze daje model wszystkich standardowych instancji ZFC. Nie użyto kolapsu Mostowskiego.

## Przykłady, regresje i walidacja

- W przykładzie czteroelementowej algebry skonstruowano konkretną nazwę a z wartością {0} dla formuły z parametrem, zamiast sugerować to bez przykładu dla zdania bez parametrów.
- Dodano piętnasty test: test_choice_via_least_preimage_on_both_atoms. Lokalna niezależna realizacja obliczeń w Pythonie: 128/128 przypadków PASS.
- Ponowna kontrola źródła: 8 definicji, 8 lematów, 6 twierdzeń, 4 uwagi, 1 przykład, 14 dowodów; 28 unikatowych etykiet, 30 odsyłaczy; brak niedomkniętych środowisk i zgodna liczba 56 otwierających/zamykających delimiterów matematycznych.
- Commity zmian: 76d73224c25361a77c5643dff27e5a0452897580 (dowody i przykład) oraz 7597567165e0f4e07587cb5f96ef9e2532dde929 (test).
- Blob źródła po zmianach: 3b4738a1a284a290eb7482fb5ce09b1b85964dc8.
- [Workflow GitHub Actions 45046759924](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45046759924): w trakcie podczas pisania raportu. Wyniku CI nie uznajemy za PASS przed potwierdzeniem zakończenia.
- Nie przeprowadzono w bieżącej sesji bezpośredniego renderowania i oględzin stron PDF. Poprzedni ogląd z audytu II pozostaje odnotowany, lecz nie zastępuje kontroli nowej wersji.

## Werdykt

Audyt III **nie jest czysty**, ponieważ wymagał poprawek źródła. Rozdział pozostaje otwarty. Po potwierdzeniu CI należy wykonać osobny audyt IV na niezmienionym blobie; do uznania za stabilny są potrzebne dwa niezależne czyste audyty oraz dodatkowy końcowy audyt na tej samej wersji. Testy Python i CI nie stanowią formalnej weryfikacji Lean.
