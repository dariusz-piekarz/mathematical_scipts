# AA-68 — otwarcie etapu D i audyt I

24 listopada 2026 r. AA-67 zamknięty według ch67_iteration_05.md. Zakres AA-68 zgodnie z końcem planu: charaktery formalne jako elementy pierścienia grupowego, suma prosta, iloczyn tensorowy, przestrzeń sprzężona, niezmienniczość Weyla, trójkątność i baza niezmienników, jednoznaczność modułu i przykład sl2. Wzór charakterów Weyla pozostawiono na później.

Audyt własny:
- skończony nośnik i krata wag wynikają z rozkładu AA-65; działanie W zachowuje mnożenie formalne;
- rozkład iloczynu tensorowego uzasadniony bazami i porównaniem składowych, znak na przestrzeni sprzężonej zweryfikowany;
- trójkątność pochodzi z konstrukcji ilorazu Verma; najwyższa składowa zachowuje wymiar jeden;
- dowód bazy niezmienników nie wymaga wzoru Weyla ani nieudowodnionej skończoności zbioru wag poniżej danej wagi: funkcjonał wysokości jest wymierny na kracie, maksymalna waga niezmiennika jest dominująca, jej wysokość nieujemna wynika z uśredniania AA-67. Każdy krok usuwa wagę maksymalną i nie wprowadza wag na tej wysokości, a możliwe nieujemne wysokości są dyskretne i ograniczone;
- identyfikacja modułów stosuje pełną redukowalność i niezależność charakterów; uwzględnia moduł zerowy;
- przykład sl2: obie liczby par sprawdzono w dwóch zakresach k<=a i k>a; przypadek a<b przez zamianę czynników.

Regresje wykonane bezpośrednio w JavaScript (dokładne współczynniki BigInt):
AA-68-CH-01: PASS {"products":441,"coefficients":9261,"virtual":31}
AA-68-CH-02: PASS {"models":22,"products":121,"reflections":25586,"weights":12793}
AA-68-CH-01: rozkłady iloczynów, wymiar, symetria i odzyskiwanie kombinacji wirtualnych. AA-68-CH-02: modele potęg symetrycznych standardowej reprezentacji A2 i przestrzeni sprzężonej, symetrie, wymiar, najwyższa krotność oraz stożek korzeniowy. Są to testy skończonych modeli, nie formalizacja Lean ani ogólny dowód. Integracja z książką, katalogiem, workflow i globalną bramką źródłową przygotowana. Pełny CI i oględziny PDF niepotwierdzone. AA-68 pozostaje otwarty, AA-69 nieotwarty.
