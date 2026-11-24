# PDE-04 — trwałe kryteria regresyjne

Źródło: chapters/pl/partial_differential_equations/04-rownanie-ciepla.tex.
Kryteria semantyczne oznaczają warunki ponownego audytu dowodów, nie testy wykonywalne ani formalizację Lean. ID pozostają trwałe.

| ID | Etykieta | Kryterium | Metoda |
|---|---|---|---|
| PDE-04-001 | chap:pde-heat | Wymiar całkowity n≥1, kappa>0, rzeczywiste funkcje skalarne domyślnie; lambda_k to miara Lebesgue'a, L^p to klasy równoważności, norma L^infty to istotne supremum modułu, BUC z normą supremum. | semantyczna |
| PDE-04-002 | thm:pde4-gauss-basic | Pochodne czasowa i obie pochodne przestrzenne jądra z poprawnymi czynnikami kappa i t; dodatniość, gładkość dla t>0, normalizacja przez kwadrat całki Gaussa i Tonellego, moduł wyznacznika zmiany zmiennych oraz skalowanie. | semantyczna |
| PDE-04-003 | sec:pde4-gauss | Skalowanie paraboliczne przez regułę łańcuchową, ansatz o stałej masie, równanie dywergencyjne dla profilu i zerowanie pola jako warunek wystarczający (nie równoważność z całym równaniem profilu); stała normalizująca. | semantyczna |
| PDE-04-004 | lem:pde4-convolution | Bezwzględna zbieżność splotu jąder, dopełnienie kwadratu i jawny rachunek stałej z a=ts/(t+s). | semantyczna |
| PDE-04-005 | thm:pde4-approx-identity | Jądro w każdym L^q, Hölder wraz z przypadkami końcowymi, bezwzględna zbieżność dla każdego x i niezależność od reprezentanta; skalowanie ogona i zbieżność zdominowana; zbieżność w BUC i L^p dla p<infty, dowód ciągłości przesunięć przez gęstość i izometrię, kontrakcja dla wszystkich p. | semantyczna |
| PDE-04-006 | sec:pde4-semigroup | P_0 jako identyczność, bezwzględna zbieżność podwójnej całki przez Tonellego i splot jąder, Fubini dla danych ze znakiem, niezmienniczość BUC, ciągłość normowa dla wszystkich t≥0 w L^p (p<infty) i BUC przez kontrakcję i własność półgrupy. | semantyczna |
| PDE-04-007 | sec:pde4-semigroup | Kontrprzykład g=chi_{x_1>0} w L^infty: P_tg(0)=1/2, ciągłość profilu przez zbieżność zdominowaną i hiperpłaszczyznę miary zero; dodatnia miara półkuli daje istotne supremum różnicy co najmniej 1/2 dla każdego t>0. | semantyczna |

## Iteracja 42 — 2026-11-24

Stan wejściowy: blob 3c281979a0eaa131b1cb0ba2fe6a7e69e56bfc59, 10 sekcji, 16 dowodów, jeden TikZ, 45 etykiet i 21 odsyłaczy. Pierwsza kontrola objęła wprowadzenie i pełne sekcje 4.1–4.2. Zapisano poprawki w commicie f799156c446c364436004ec36c5447c9d810742a, blob b806dcc2fd705678c2b85fdb5969aeaa73f6e7a4. Ponownie sprawdzono unikatowość i zachowanie wszystkich 45 etykiet, 21 odsyłaczy, zagnieżdżenie środowisk oraz jedyny cel zewnętrzny eq:pde3-green1 w rozdziale 03. Siedem trwałych kryteriów ma istniejące kotwice. Nie uruchomiono kompilacji, testów wykonywalnych, audytu wizualnego ani Lean. Pozostałe osiem sekcji i rysunek są otwarte.

Następny zakres: zagadnienie Cauchy'ego na całej przestrzeni, klasy regularności i dane początkowe, zachowanie masy i tłumienie norm; następnie zasada maksimum i jednoznaczność, wygładzanie, generator, Duhamel, energia, asymptotyka i przykład Tychonoffa.
