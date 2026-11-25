# PDE-08 — trwałe kryteria regresyjne

Rozdział 08: Transformata Fouriera, przestrzeń Schwartza i dystrybucje temperowane.
Kryteria semantyczne wymagają ręcznej lektury matematycznej; nie są wykonanymi testami automatycznymi ani dowodami Lean. ID pozostają stałe. Testy wykonywalne będą przygotowane na etapie stabilizacji.

| ID | Kotwica LaTeX | Kryterium i metoda weryfikacji | Rodzaj |
|---|---|---|---|
| PDE-08-001 | eq:pde8-convention | Konwencja nieunitarna: znaki wykładników, czynnik (2pi)^(-d) tylko w całce odwrotnej, dziedzina L¹ obu całek, odwracalność na przestrzeni Schwartza dopiero po dowodzie. Rozróżnienie współczynników szeregów na torusie i transformaty na R^d. | semantyczna |
| PDE-08-002 | def:pde8-schwartz | Definicja wielowskaźnikowa z konwencją potęgi zerowej, skończone półnormy, liniowość, aksjomaty półnorm i rozdzielanie punktów przez p_0,0, charakterystyka zbieżności. | semantyczna |
| PDE-08-003 | lem:pde8-seminorms | Równoważność p i q przez dominację monomianu oraz rozwinięcie wielomianowe (1+suma modułów współrzędnych)^N ze współczynnikami wielomianowymi. | semantyczna |
| PDE-08-004 | lem:pde8-seminorms | Jawne oszacowania mnożenia przez x_j i różniczkowania w q_N,m; składnik beta_j pomijany, gdy beta_j=0. Ciągłość obu włożeń do L¹ i L² przez całkę radialną dla Np>d, osobno d=1. | semantyczna |
| PDE-08-005 | sec:pde8-schwartz | Ważony zanik pochodnych do zera przez półnormę z dodatkową potęgą; gaussowska rekurencja wielomianów i dominacja wykładnicza, funkcje testowe w S, kontrprzykład (1+norma x²)^(-1) dla każdego d>=1. | semantyczna |
| PDE-08-006 | sec:pde8-schwartz | Zupełność przestrzeni Schwartza: rosnące Q_n, metryka niezmiennicza względem przesunięć, obustronne oszacowania kul i warunku Cauchy'ego. Granice jednostajne pochodnych, tożsamość całkowa na odcinku, identyfikacja pochodnych granicy, przejście do granicy punktowo w oszacowaniu ważonym przed supremum. | semantyczna |
| PDE-08-007 | thm:pde8-density | Gładka funkcja odcinająca psi zbudowana przez splot funkcji charakterystycznej kuli o promieniu 3/2 z przybliżoną jedynką o parametrze 1/4; 0<=psi<=1, wartości 1 na kuli jednostkowej i 0 poza kulą o promieniu 2. Symbol chi zastrzeżony dla funkcji charakterystycznej. | semantyczna |
| PDE-08-008 | thm:pde8-density | Gęstość testów w S: jawna wielowskaźnikowa reguła Leibniza dla f-f_R, przypadek pochodnej rzędu zero czynnika odcinającego, oszacowanie przez C/(1+R) razy q_N+1,m i R>=1. | semantyczna |
| PDE-08-009 | thm:pde8-density | Gęstość w L^p dla 1<=p<infty: obcięcie do kuli przez całkowalność modułu do potęgi p, wygładzenie obciętej funkcji, wspólny zwarty nośnik w kuli R+1 przenosi lokalną zbieżność na normę globalną. Dobór R i epsilon w poprawnej kolejności. | semantyczna |

## Iteracja 103 — 2026-11-25

Pierwsza lektura wprowadzenia i sekcji 8.1. Rozdział ma 11 sekcji merytorycznych i podsumowanie. Sprecyzowano konwencję transformaty całkowej i status symbolu odwrotności przed twierdzeniem o odwróceniu. Rozpisano definicje, równoważność półnorm, oszacowania operatorów, ciągłość włożeń do L¹ i L², szybki zanik i przykłady. Dodano dowód zupełności przestrzeni Frécheta jako uzupełnienie pierwszej lektury, potrzebne do dalszej teorii. Skonstruowano funkcję odcinającą i rozpisano obie części twierdzenia o gęstości, bez kołowego odwołania do teorii Fouriera. Zmieniono również symbol tej funkcji z chi na psi w późniejszym przykładzie, bez audytowania jego dowodu w tej iteracji. Commit źródła 2b5c05b70e3281f614000d9e5a8103e52fea760f, blob e3e2941069a7fe259c2f1cc3cbe9347d9bbc75c0. Zachowano wszystkie 39 etykiet, 21 wystąpień odsyłaczy, poprawne zagnieżdżenie środowisk. Nowe odsyłacze do rozdziału 07 mają istniejące cele; pełna kontrola zewnętrzna pozostaje do wykonania. Dodano 9 kryteriów. Nie uruchomiono testów wykonywalnych, CI, kompilacji PDF ani Lean. Następna iteracja 104: sekcja 8.2 — Transformata Fouriera na przestrzeni Schwartza.
