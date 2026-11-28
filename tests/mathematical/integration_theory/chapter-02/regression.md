# IT-02 — trwałe kryteria audytu

| ID | Miejsce | Kryterium | Metoda |
|---|---|---|---|
| IT-02-001 | ma1:def:riemann-sum i następujące stwierdzenie | Jednoznaczność granicy; najpierw wybór średnicy, potem ustalenie podziału i zmiana znacznika tylko na jednej komórce | semantyczna + Python (1/x) |
| IT-02-002 | thm:riemann-criterion | Oscylacja zerowa iff ciągłość; domkniętość D_epsilon; kontrola długości i wybór O także dla D_epsilon pustego oraz M=0 | semantyczna + Python (skończone pokrycia, nie dowód twierdzenia) |
| IT-02-003 | końcowy przykład niezupełności | Norma ilorazowa; całka obcięć 2-1/n; Cauchy; jednoznaczność granicy L1 i brak ograniczonego reprezentanta | semantyczna + Python (rachunek dokładny) |
| IT-02-004 | ma1:thm:riemann-darboux-equivalence | Dowolne znaczniki; wspólne zagęszczenie; k=0; oba kierunki i równość wartości | semantyczna |
| IT-02-005 | ma1:thm:riemann-algebra, ma1:thm:riemann-additivity, ma1:thm:riemann-mean-value, ma1:thm:riemann-fundamental, ma1:thm:newton-leibniz | Hipotezy i oszacowania, przypadki zerowe, orientacja, końce przedziałów, przejście do granicy | semantyczna |

Audyt I: 4e789c0cba7cfdc07954a942a8566988b1c4a0e7; testy: fdc75a69ec2fd23991ae492b1b8c4f5d4226507b. Kontrola II źródła c281a0014e1953b7e3004d7d83972ee92db113e8: ponownie odczytano wszystkie dowody, sprawdzono ograniczoność i wybór znaczników, k=0, oba kierunki kryterium Lebesgue'a, operacje i orientację, jednostajną granicę oraz przykład Cauchy'ego; bez nowej istotnej luki matematycznej. 15 etykiet zachowanych; 8 różnych odsyłaczy do IT-01/02 rozwiązywalnych. Zbieżność monotoniczna w końcowym przykładzie jest prawie wszędzie (punkt 0 jest zerowy miarowo). CI 45618910028: regresje sukces, kompilacja przerwana przez podwójne etykiety równania Haara w IT-14; naprawa 606070af689709dbf530c4ee0c3049995d7cce77 rozdziela etykiety na równanie miarowe i równoważny wzór całkowy. Pełna stabilizacja techniczna wymaga ponownego CI i kontroli PDF. Nie uruchomiono Lean.
