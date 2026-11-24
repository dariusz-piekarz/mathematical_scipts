# PDE-03 — przegląd przygotowawczy (iteracja 27, 2026-11-24)

Źródło: chapters/pl/partial_differential_equations/03-rownania-laplace-a-i-poissona.tex, blob 2813ce108eac607788bad18c72f905d03ed77056.

Stan wejściowy: 10 sekcji, 18 środowisk proof, 2 rysunki TikZ, 47 unikatowych etykiet, 26 odsyłaczy. Cele zewnętrzne: thm:laplace-max i chap:pde-intro, wymagają kontroli względem rozdziału 01. Zagnieżdżenie środowisk poprawne. Nie wykonano kompilacji ani formalizacji.

Pierwsza kolejka usterek i luk dowodowych (status: otwarte):

| ID | Kotwica | Zakres kontroli / poprawki |
|---|---|---|
| PDE-03-001 | thm:pde3-mean | Uzasadnić różniczkowanie pod całką, zmianę zmiennych na sferze i wyprowadzenie średniej po kuli przez całkowanie promieniowe. Ujednolicić założenie wymiaru oraz regularności w definicji i wprowadzeniu. |
| PDE-03-002 | prop:pde3-converse | Uzasadnić jednostajną resztę Taylora i momenty sfery, a także obliczyć współczynnik średniej objętościowej 1/(2(n+2)). |
| PDE-03-003 | thm:pde-v31-continuous-mean | Doprecyzować dziedzinę lokalnego splotu (nie definiować u poza obszarem przez niezdefiniowany iloczyn), gładkość, Fubiniego, jednostajną zbieżność i brak kołowości względem twierdzenia Poissona. |
| PDE-03-004 | thm:pde3-strong-max | Dowód zasady dla ekstremum lokalnego odwołuje się do analityczności; sprawdzić graf zależności i zastąpić niepełne uzasadnienie zasady identyczności argumentem otwarto-domkniętym dla zbioru punktów, w których wszystkie pochodne u-M znikają. |
| PDE-03-005 | prop:pde3-gradient | Ustalić promień rho<R przed różniczkowaniem ruchomej średniej; jawnie dobrać otoczenie środka i uzasadnić różniczkowanie oraz zastosowanie Gaussa. |
| PDE-03-006 | thm:pde3-phi | Wyprowadzić radialny laplasjan, normalizację i całkowalność w obu wymiarach; jawnie oszacować obie całki brzegowe, poprawność orientacji i granicę całki objętościowej. |
| PDE-03-007 | thm:pde3-newton | Uściślić lokalną dominację wszystkich pochodnych splotu i zastosowanie tożsamości dystrybucyjnej. |
| PDE-03-008 | prop:pde3-ball-green | Rozwinąć tożsamość inwersji, rozpatrzyć biegun zerowy oraz użycie zapisu Phi_n(R) dla funkcji na R^n. Zweryfikować symetrię i gładkość harmonicznej poprawki także przy y=0. |
| PDE-03-009 | thm:pde3-poisson | Wyprowadzić normalną pochodną jawnie także w n=2, sprawdzić przypadek środka bez nieuzasadnionego przejścia granicznego; uzasadnić komutację pochodnych i niezależną normalizację. |
| PDE-03-010 | thm:pde3-ball-poisson | Uzasadnić jednostajne oszacowania harmonicznej poprawki H_R(x,y) i jej pochodnych dla y w zwartym nośniku obejmującym ewentualnie 0. |
| PDE-03-011 | thm:pde3-analytic | Jawne rozwinięcie dwumianowe z oszacowaniem wspólnego promienia i bezwzględnej zbieżności szeregu wielowymiarowego. |
| PDE-03-012 | prop:pde3-conjugate | Uzasadnić regularność C^2 funkcji sprzężonej i obliczyć okres formy w kontrprzykładzie. |

Kolejka nie jest wyczerpująca. Pozostają kontrola pełnej sekcji Greena, dalszych sekcji Fouriera i ogólnych zagadnień brzegowych, rysunków, terminologii, zależności i testów wykonywalnych. Żadnego z powyższych kryteriów nie oznaczono jako zaliczonego; źródła rozdziału 03 w tej iteracji nie zmieniono.
