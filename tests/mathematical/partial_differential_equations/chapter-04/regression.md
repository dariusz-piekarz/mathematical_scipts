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
| PDE-04-008 | thm:pde4-cauchy | Indukcja dla wszystkich mieszanych pochodnych jądra jako wielomianów w z o gładkich współczynnikach czasowych razy jądro; na [a,b] i ograniczonych x wspólna całkowalna majoranta C(1+abs(y))^d exp(-abs(y)^2/(8 kappa b)), także dla ilorazów różnicowych. Gładkość i równanie punktowo. | semantyczna |
| PDE-04-009 | thm:pde4-cauchy | Niezmienniczość BUC i silna ciągłość dla t≥0, zbieżność jednostajna do danych, jawny dowód ciągłości łącznej w (t,x), kontrakcja, nieujemność i przynależność do klasy jednoznaczności. Brak kołowości: jednoznaczność z późniejszej zasady maksimum, niezależnie od wzoru całkowego. | semantyczna |
| PDE-04-010 | cor:pde4-positive | Nieujemne niezerowe dane ciągłe o zwartym nośniku należą do BUC; kula z g≥c>0, dodatnie minimum jądra na jej domknięciu i dodatnia objętość. Ścisła dodatniość dla każdego t>0 i x, bez wniosku o dodatniości danych zmieniających znak. | semantyczna |
| PDE-04-011 | prop:pde4-mass | Tonelli dla modułu i normalizacja, Fubini dla danych ze znakiem; zachowanie całki odróżnione od zachowania normy L^1 (równość dla danych nieujemnych). Jawne maksimum jądra i obliczenie kwadratu normy L^2 jako (8 pi kappa t)^(-n/2), Minkowski i skończoność normy splotu. | semantyczna |

## Iteracja 42 — 2026-11-24

Stan wejściowy: blob 3c281979a0eaa131b1cb0ba2fe6a7e69e56bfc59, 10 sekcji, 16 dowodów, jeden TikZ, 45 etykiet i 21 odsyłaczy. Pierwsza kontrola objęła wprowadzenie i pełne sekcje 4.1–4.2. Zapisano poprawki w commicie f799156c446c364436004ec36c5447c9d810742a, blob b806dcc2fd705678c2b85fdb5969aeaa73f6e7a4. Ponownie sprawdzono unikatowość i zachowanie wszystkich 45 etykiet, 21 odsyłaczy, zagnieżdżenie środowisk oraz jedyny cel zewnętrzny eq:pde3-green1 w rozdziale 03. Siedem trwałych kryteriów ma istniejące kotwice. Nie uruchomiono kompilacji, testów wykonywalnych, audytu wizualnego ani Lean. Pozostałe osiem sekcji i rysunek są otwarte.

Następny zakres: zagadnienie Cauchy'ego na całej przestrzeni, klasy regularności i dane początkowe, zachowanie masy i tłumienie norm; następnie zasada maksimum i jednoznaczność, wygładzanie, generator, Duhamel, energia, asymptotyka i przykład Tychonoffa.

## Iteracja 43 — 2026-11-24
Opracowano pełną sekcję 4.3 w commicie 087d92a12907cce1597054c9d73e9b15f03a775c, blob 7dff17fb097f2e2307c9eb6b5c9586542adf24db. Uzupełniono indukcję i lokalnie jednostajną całkowalną majorantę wszystkich pochodnych mieszanych jądra, ciągłość łączną również przy t=0, ścisłą dodatniość dla danych nieujemnych i niezerowych oraz rachunek masy i norm. Sprawdzono, że dowód jednoznaczności w następnej sekcji nie korzysta z reprezentacji całkowej; nie przeprowadzono jeszcze pełnego audytu tej sekcji. Zachowano 45 etykiet i poprawną strukturę środowisk; 23 odsyłacze, jedyny cel zewnętrzny eq:pde3-green1 w rozdziale 03. Dodano cztery trwałe kryteria, łącznie 11 unikatowych ID z istniejącymi kotwicami. Nie uruchomiono kompilacji, testów wykonywalnych, kontroli wizualnej ani Lean. Następny zakres: sekcja 4.4, zasada maksimum i jednoznaczność na całej przestrzeni.
