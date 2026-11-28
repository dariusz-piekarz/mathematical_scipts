# Logika matematyczna i teoria mnogości — audyt II rozdziału 37

**Data:** 22 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Źródło:** chapters/pl/logic_and_set_theory/37-duze-liczby-kardynalne-nieosiagalnosc-i-mierzalnosc.tex.  
**Blob:** 3e0ae67b1b6a9abb5a4ff93691a2947d207647c4 (niezmieniony po audycie I).  
**Werdykt matematyczny:** czysty; **pierwszy czysty audyt (1/2)** pod warunkiem zakończenia CI dla bieżącej iteracji.

## 1. Niezależna kontrola definicji i rachunków kardynalnych

Regularność liczby kardynalnej κ została sformułowana przez cf(κ)=κ, zaś silna graniczność przez 2^λ<κ dla każdej liczby kardynalnej λ<κ. W definicji nieosiągalności konieczny jest osobny warunek nieprzeliczalności, gdyż ω jest regularną i silnie graniczną liczbą kardynalną. Nie zrównano słabej nieosiągalności z silną. Argument, że silnie nieosiągalna liczba kardynalna nie jest następnikiem innej liczby kardynalnej, poprawnie wykorzystuje λ^+≤2^λ.

W indukcji po rangach V_α dla α<κ krok następnika korzysta z silnej graniczności, a krok graniczny z regularności: mniej niż κ zbiorów, każdy mocy mniejszej niż κ, ma sumę mocy mniejszej niż κ. W dowodzie V_κ ⊨ ZFC oddzielnie skontrolowano pusty zbiór, parę, sumę, nieskończoność, potęgowanie, wyróżnianie, zastępowanie i wybór. Szczególnie ograniczenie rang zbioru wartości formuły definiowanej nad V_κ używa dwóch niezależnych przesłanek: moc dziedziny jest <κ, a κ jest regularny. Zwykła graniczność κ nie wystarczyłaby.

Wniosek o niemożliwości udowodnienia istnienia nieosiągalnego w niesprzecznej ZFC jest względny do formalnej reprezentacji Con(ZFC) i drugiego twierdzenia Gödla, nie jest dowodem niesprzeczności żadnej teorii bez założeń.

## 2. Niezależna kontrola mierzalności

Z niegłównych singletonów i κ-zupełności wynika brak wszystkich małych zbiorów w U. Regularność: partycja κ na μ=cf(κ)<κ małych kawałków prowadziłaby do pustego przecięcia μ elementów U. Silna graniczność: iniekcja f:κ→P(λ), λ<κ, w połączeniu z wyborem jednej wartości bitu dla każdej współrzędnej ξ<λ dałaby zbiór miary jeden, na którym f jest stała, a więc co najwyżej jednoelementowy. W obu rozumowaniach jawnie wykorzystuje się, że U jest ultrafiltrem, a nie tylko filtrem.

Przykład niegłównego ultrafiltru na ω nie prowadzi do fałszywej mierzalności ω: jego ω-zupełność oznacza wyłącznie skończone przecięcia, a ciąg zbiorów ogonowych przeczy przeliczalnej zupełności.

## 3. Niezależna kontrola Łosia i zanurzenia

W formule egzystencjalnej wyboru świadków dokonuje się dla indeksów z jednego zbioru D⊆κ w otaczającym ZFC. Nie potrzeba wyboru dla klasy właściwej. Klasa ilorazowa zostaje przedstawiona za pomocą zbiorowych kodów Scotta. Dzięki ograniczeniu zakresów funkcji reprezentujących poprzedniki dowolnej klasy do jednego zbioru relacja jest zbiorolokalna. Jej dobrze ufundowanie jest zapewnione przez ω-zupełność (κ>ω), gdyż rzekomy ciąg malejący dałby ciąg malejący w relacji ∈ dla pojedynczego indeksu α.

Dla każdego α<κ, jeżeli [f]∈j(α), to f przyjmuje wartości <α na zbiorze U-dużym. Rozbicie tego zbioru na mniej niż κ włókien prowadzi do jednego włókna U-dużego, co daje j(α)=α. Wartość funkcji identycznościowej leży ponad wszystkimi j(α) i poniżej j(κ), więc punkt krytyczny wynosi κ. Nie utożsamiono funkcji identycznościowej z κ przy dowolnej, nienormalnej mierze.

W dowodzie istnienia miary normalnej W={X⊆κ:κ∈j(X)} sprawdzono definowalność W jako zbioru, niegłówność, κ-zupełność z j(μ)=μ i normalność przez wartość j(f)(κ)<κ. Równoważność normalności z domknięciem na przecięcia diagonalne wykorzystuje rzeczywiste indeksy ξ<α w obu kierunkach.

## 4. Język, odsyłacze, LaTeX i PDF

Bez zmian: 775 wierszy, 26 unikalnych etykiet, 18 odsyłaczy, 7 definicji, 4 lematy, 7 twierdzeń, 1 wniosek, 5 uwag, 1 przykład i 12 dowodów. W toku niezależnej analizy nie odnaleziono nowych obowiązkowych poprawek; wszystkie środowiska pozostają poprawnie sparowane.

**GitHub Actions [45066748548](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45066748548): SUCCESS** dla źródła z audytu II, wraz ze wszystkimi ośmioma testami nowego rozdziału i pełną kompilacją. Pobranie artefaktu 14771483430 i rozpakowanie potwierdziło **326 stron PDF A4**. Rozdział 37 zajmuje strony PDF **321–326**. Wyrenderowano sześć stron przy 100 dpi i zmontowano w układzie 3×2, po czym obejrzano układ, podpisy twierdzeń, wzory i zakończenia stron. Nie zaobserwowano kolizji ani ucięcia. Log zawiera **0** przepełnionych wierszy, **0** nierozwiązanych odsyłaczy i **1** ostrzeżenie underfull w całej książce.

## 5. Werdykt

Nie było potrzeby ingerować w tekst rozdziału. **Audyt II: pierwszy czysty (1/2)**. Kolejny audyt III przeprowadzić na tym samym źródle, a następnie wykonać dodatkowy audyt IV weryfikujący stabilność. Zielone CI i skończone przykłady ultrafiltrów nie są formalizacją w Lean.
