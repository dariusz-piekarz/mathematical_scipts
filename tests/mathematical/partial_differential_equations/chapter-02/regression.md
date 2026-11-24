# PDE-02 — trwałe kryteria regresyjne

Źródło: [rozdział 02](../../../../chapters/pl/partial_differential_equations/02-charakterystyki-i-pde-pierwszego-rzedu.tex).
Kryteria semantyczne nie są testami automatycznymi ani formalizacją Lean. Identyfikatory zgodne z [przeglądem przygotowawczym](../../../../audits/partial_differential_equations/chapter-02/preflight.md).

| ID | Etykieta | Kryterium | Metoda |
|---|---|---|---|
| PDE-02-001 | eq:pde2-constant-formula | Całka czasowa względem λ₁, lokalne ograniczenia pochodnych podcałkowych, reguła Leibniza, weryfikacja równania w całej przestrzeni i danych przy t=0. | semantyczna |
| PDE-02-002 | thm:pde2-linear | Gronwall dla 1+abs(X), ograniczenie trajektorii, granica i przedłużenie; istnienie przepływu wstecznego z polem -b(t-s,x) i tymi samymi ograniczeniami, obie tożsamości odwrotności. | semantyczna |
| PDE-02-003 | thm:pde2-linear | Wspólna regularność odwrotności względem (t,x) przez blokową macierz pochodnej i lokalne odwrotności; przedłużenie C¹ przez odbicie na obu końcach czasu. | semantyczna |

## Pierwszy właściwy przebieg — 2026-11-24

Poprawki źródła w commicie fc5a93a0c90004507219da4882c84b57adc1b309. Sprawdzono semantycznie trzy poprawione fragmenty, zachowano wszystkie 51 etykiet i 55 wystąpień odsyłaczy (w tym istniejący cel zewnętrzny chap:pde-code w rozdziale 33); środowiska poprawnie zagnieżdżone. Nie uruchomiono kompilacji, renderowania, testów wykonywalnych ani Lean dla rozdziału 02. Otwarte usterki PDE-02-004–010 oraz dalszy audyt rozdziału. Rozdział otwarty.
