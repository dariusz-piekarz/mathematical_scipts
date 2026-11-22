# Topologia ogólna — rozdział 13: audyt iteracja 03

Data: 2026-11-22. Źródło: `chapters/pl/general_topology/13-zupelnosc-jednostajna-i-uzupelnienia.tex`.

## Niezależna kontrola matematyczna

- Ponownie prześledzono definicję bliskości filtrów Cauchy'ego, symetrię i przechodniość oraz argument minimalizacji `F°`. W konstrukcji minimalnego przedstawiciela sprawdzono, że każdy filtr bliski `F` zawiera `F°`, a więc `F°` jest rzeczywiście minimalny i jednoznaczny.
- Sprawdzono, że relacje `\\widehat E` spełniają warunki bazy struktury jednostajnej, że `x↦N_x` zachowuje strukturę jednostajną na obraz i że obraz jest gęsty.
- Powtórzono szczegółową kontrolę kwantyfikatorów w kroku zupełności `\\widehat X`, po poprawce z iteracji 02: wybór `H=H_0∩H_1`, `W⊂V∩D` pozwala jednocześnie zapewnić `B(H,W)⊂A` i `H×H⊂\\widehat D`.
- Doprecyzowano ostatnią inkluzję: jeśli `u∈T[x]`, `c∈C`, to `(u,x)∈T` przez symetrię oraz `(x,c)∈D` przez `x∈A` i `A×C⊂D`. Zatem `(u,c)∈T∘D⊂D²`. Dopiero stąd wynika `(\\iota(x),F_0)∈\\widehat{D²}`, a dzięki symetrii i złożeniu `(F_0,K)∈\\widehat{D⁴}⊂\\widehat E`.
- W lemacie o rozszerzaniu przez gęstość prześledzono wykorzystanie filtrów indukowanych przez `A∩E[z]`, zupełności `Y` i argument zamykania relacji w topologii `Y×Y`, używając `T³⊂V`. Nie wykryto kolejnej luki wymagającej zmiany tez.

## Testy: rzeczywiste wzmocnienie zakresu

Zastąpiono uproszczony test rozdziału 13 enumeracją wszystkich podziałów zbiorów o rozmiarach 0–4 (liczby Bella: 1, 1, 2, 5, 15). Dla właściwych filtrów głównych na niepustych zbiorach:
- rozpoznawana jest własność Cauchy'ego względem relacji równoważności, która generuje strukturę jednostajną;
- minimalizacja filtra jest porównywana z pełną klasą relacji równoważności;
- sprawdzany jest zbiór wszystkich minimalnych filtrów, o liczności równej liczbie klas;
- bliskość dwóch filtrów Cauchy'ego porównuje się ze zgodnością ich minimalnych przedstawicieli.

Testy na modelach skończonych nie zastępują dowodu dla ogólnych przestrzeni jednostajnych, ale lepiej kontrolują samą konstrukcję uzupełnienia niż poprzedni test.

## Commity

- `2e0ff9c1a3b26b904f0efd25cb9ded6aa3f3660b`: wzmocnienie testu skończonych przestrzeni.
- `149d0c15131e55ed565be3ebbc301d1f11a8d692`: szczegółowe uzasadnienie składania relacji.

## Walidacja

Właściwy przebieg CI na dokładnym commicie `149d0c15131e55ed565be3ebbc301d1f11a8d692`:
https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45006347152

W chwili redagowania raportu testy Python dotarły do fazy kompilacji książki, a końcowy status CI i PDF nie były jeszcze potwierdzone. Odczytać wynik po zakończeniu workflow, nie oznaczać przedwcześnie jako PASS.

## Status

| Kontrola | Wynik |
| --- | --- |
| Kontrola konstrukcji filtrów minimalnych | PASS (ponowny audyt) |
| Poprawność kroku zbieżności w uzupełnieniu | PASS po doprecyzowaniu |
| Własność uniwersalna | PASS w przeglądzie matematycznym |
| Rozszerzony test skończonych modeli | Zapisany; wynik CI należy potwierdzić |
| Pełny PDF i czysty log | WERYFIKACJA W TOKU |
| Stabilizacja rozdziału | OTWARTA — przed kolejnym audytem |

