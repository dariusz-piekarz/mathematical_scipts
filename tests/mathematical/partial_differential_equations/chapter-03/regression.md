# PDE-03 — trwałe kryteria regresyjne

Źródło: [rozdział 03](../../../../chapters/pl/partial_differential_equations/03-rownania-laplace-a-i-poissona.tex).
Kolejka wejściowa: [przegląd przygotowawczy](../../../../audits/partial_differential_equations/chapter-03/preflight.md).

Kryteria semantyczne wymagają ponownego sprawdzenia argumentu matematycznego, nie tylko obecności etykiety. Testy wykonywalne i rzeczywista formalizacja Lean są odrębnymi rodzajami kontroli.

| ID | Etykieta | Kryterium | Metoda |
|---|---|---|---|
| PDE-03-001 | thm:pde3-mean | Jawne założenia wymiaru i funkcji rzeczywistych, definicja średniej dla funkcji ciągłej; skalowanie miary sferycznej, dominacja pochodnej względem promienia, normalna jednostkowa, Gauss, granica w zerze i pełne obliczenie średniej po kuli. | semantyczna |
| PDE-03-002 | prop:pde3-converse | Reszta Taylora z ciągłości hesjanu, oszacowanie jednostajne, znikanie nieparzystych i mieszanych momentów przez odbicia, diagonalne momenty równe omega_n/n; obliczenie średniej po kuli z resztą o(r²), współczynniki 1/(2n) i 1/(2(n+2)). | semantyczna |
| PDE-03-003 | thm:pde-v31-continuous-mean | Lokalny splot tylko w dziedzinie u, normalizacja i gładkość przez dominację pochodnych jądra; radialne jądro daje dokładną równość u_epsilon=u przez współrzędne biegunowe i własność średniej, następnie odwrotność dla C². Dowód podstawowy bez zależności od twierdzenia Poissona. Zachować alternatywę z nieradialnym jądrem, Fubinim, jednostajną zbieżnością i późniejszą reprezentacją Poissona. | semantyczna |

## Pierwszy właściwy przebieg — 2026-11-24 (iteracja 28)

Poprawki 001–003 w commicie dccdb69ce20950abb613d8ed7d79bde11a2f6d3e, blob 89326ba8cc987959d885145014f1d6dc6db80069. Ponownie sprawdzono zmianę zmiennych na sferze, rachunek promieniowy, resztę Taylora i momenty sfery. W twierdzeniu dla funkcji ciągłych radialne jądro o całce 1 daje dokładną równość splotu z u lokalnie, bez użycia granicy ani późniejszego twierdzenia Poissona. Zachowano poprzednią metodę jako alternatywny argument z nieradialnym jądrem. Zachowano 47 unikatowych etykiet i 26 odsyłaczy; oba zewnętrzne cele thm:laplace-max i chap:pde-intro znaleziono dokładnie raz w rozdziale 01. Zagnieżdżenie środowisk poprawne. Kryteria 001–003 mają istniejące kotwice i były sprawdzone semantycznie w zakresie zmienionych fragmentów. Nie wykonano jeszcze testów wykonywalnych, kompilacji, kontroli wizualnej ani Lean dla rozdziału 03. Pozostałe punkty kolejki przygotowawczej są otwarte.
