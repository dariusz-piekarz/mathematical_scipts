# PDE-02 — przygotowanie audytu, 2026-11-24 (iteracja 12 PDE)

Rozdział 01 nadal otwarty: aktualny blob aeea9d0a8c39cb2a2049d0cd982688dd370fc874, workflow 45406319616 i 45406654400 w kolejce. Rzeczywiście uruchomiono ponownie lokalną kopię test_energy_hadamard.py z identycznym Git blob SHA 1d8609e78e4887cde7164a5a65d65d9d7db6cdd2: 3/3 OK. Nie wykonano pełnej aktualnej kompilacji ani Lean.

## Rozdział 02: stan wyjściowy

Źródło [02-charakterystyki-i-pde-pierwszego-rzedu.tex](../../../chapters/pl/partial_differential_equations/02-charakterystyki-i-pde-pierwszego-rzedu.tex), blob ce204c8e2fb6202e4310c4e5ceb9a571bd660e57.
Kontrola automatyczna źródła: 10 sekcji, 12 środowisk proof, 2 rysunki TikZ, 51 unikalnych etykiet, 55 wystąpień odsyłaczy, prawidłowe zagnieżdżenie środowisk. Jedyny zewnętrzny cel chap:pde-code istnieje w rozdziale 33 (blob c6368b450bd0ea2f0837d4d3dcfc4b17951d48e1). W kompilacji izolowanej należy uwzględnić ten cel jawnie, a nie zgłaszać go jako brak w książce.

## Usterki do poprawy podczas właściwego audytu

Poniższe identyfikatory są identyfikatorami otwartych usterek, nie zaliczonymi testami. Właściwe kryteria regresyjne należy zachować po wprowadzeniu poprawek.

| ID | Etykieta | Usterka i kryterium zamknięcia |
|---|---|---|
| PDE-02-001 | eq:pde2-constant-formula | Zapis całki czasowej zgodnie z konwencją miary Lebesgue'a oraz uzasadnienie różniczkowania całki z parametrem i jednostronnej regularności. |
| PDE-02-002 | thm:pde2-linear | Uzupełnić oszacowanie Gronwalla dla trajektorii: 1+abs(X(t)) <= (1+abs(xi)) exp(Mt); uzasadnić przedłużenie do końca przedziału przez pozostawanie w zwartym podzbiorze przestrzeni. Dla przepływu wstecznego użyć pola -b(t-s,x) o tych samych ograniczeniach. |
| PDE-02-003 | thm:pde2-linear | Sama regularność odwrotności dla ustalonego t nie wykazuje wspólnej regularności względem (t,x). Użyć blokowej macierzy pochodnej odwzorowania (t,xi) -> (t,X(t;xi)), niezerowego wyznacznika D_xi X i lokalnego twierdzenia o funkcji odwrotnej; jednoznaczność składa lokalne odwrotności. Uzasadnić regularność na końcach przedziału. |
| PDE-02-004 | prop:pde2-liouville | Wyprowadzić równanie wariacyjne przez zróżniczkowanie równania całkowego przepływu i twierdzenie o całce z parametrem; jawnie wskazać macierz jednostkową I_d. |
| PDE-02-005 | thm:pde2-mass | Przed zastosowaniem zmiany zmiennych wykazać supp rho(t,.) = X_t(supp rho_0), ponieważ J>0, X_t jest homeomorfizmem, a wzór transportu gęstości zachowuje zbiór punktów niezerowych. Zwarty nośnik zapewnia całkowalność także dla rho o zmiennym znaku. |
| PDE-02-006 | prop:pde-v31-transport-lp | Przyjąć jawną normę operatorową indukowaną przez normę euklidesową i wykazać abs(tr A) <= sum_j abs(<Ae_j,e_j>) <= dM. Rozróżnić supremum i supremum istotne; dla funkcji ciągłej są równe. |
| PDE-02-007 | thm:pde2-cauchy | W dowodzie lokalnego zagadnienia Cauchy'ego użyć prostokątnego otoczenia (-delta,delta) x V', aby całe odcinki od (0,y) do (s,y) pozostawały w dziedzinie. Wykazać, po zmniejszeniu otoczenia, że przecięcie U z Sigma jest dokładnie obrazem {0} x V'. |
| PDE-02-008 | thm:pde2-quasilinear | Jawnie zapewnić wspólny przedział istnienia ODE dla xi w otoczeniu xi_0, zapisać blokową macierz pochodnej i wybrać prostokątne otoczenie do dowodu jednoznaczności. Zastąpić słowo mapa określeniem odwzorowanie w kontekście funkcji między przestrzeniami. |
| PDE-02-009 | thm:pde2-breaking | Wykazać wspólną regularność odwrotności X_t względem (t,x), skonstruować u(t,x)=u_0(X_t^{-1}(x)), zróżniczkować względem czasu i zweryfikować równanie oraz dane początkowe; obecny dowód wyprowadza tylko wzór na u_x. |
| PDE-02-010 | ex:pde2-rarefaction | Weryfikację słabego rozwiązania z danymi początkowymi przeprowadzić na t>=epsilon i wykazać przejście epsilon->0: różnica od u_0 wsparta w przedziale między min(0,u_L t) i max(0,u_R t), z długością O(t) oraz jednolitym ograniczeniem. |

Rozdział 02 nie został zmieniony. To przegląd przygotowawczy, nie pełny audyt wszystkich dowodów, rysunków i kodu. Priorytetem pozostaje pełna kompilacja i końcowy układ stron rozdziału 01. Raport nie wyzwala workflow PDE.
