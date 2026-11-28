# PDE — rozdział 09 — iteracja 146: trzecia lektura 062–081

Data: 2026-11-25. Gałąź: biblioteka-matematyczna-iteracja-6.
Źródło lektury: blob 89a29c43f713f2e4b304e201fdd0c4518a3cf9ac.

| Kryteria | Wynik kontroli |
| --- | --- |
| 062–063 | Poprawne: przesunięcie testu, zachowanie norm na P_h, niezależne przedłużenia składowych, identyfikacja lokalna splotu i zbieżność diagonalna. Argument globalnej zbieżności splotu wynika z oszacowania Minkowskiego i ciągłości przesunięć w dowodzie thm:pde7-approx-id, sprawdzonym w źródle 07. |
| 064–065 | Poprawne: przeciwne wyrazy brzegowe, znak pochodnej normalnej, zachowanie pochodnych stycznych, czynnik 2^(1/p) i identyfikacja granic składowych L^p. |
| 066–067 | Poprawne: odwracalność Vandermonde'a, dopasowanie do rzędu k-1, indukcyjna tożsamość testowa ze skokiem wartości, przypadek d=1, czynniki j^(m-1/p) i stała operatora. |
| 068–069 | Poprawne: odcięcia na warstwie, testy z odcięciem, odbicie po zmianie t na 1-t, gęstość globalna bez wymogu zerowego śladu. W uwadze o jądrze śladu doprecyzowano p skończone, zgodnie z hipotezą thm:pde10-trace-zero odczytaną w aktualnym źródle 10. |
| 070–072 | Poprawne: oszacowanie przekrojów, Tonelli i Minkowski, konstrukcja przez domknięcie, stała 2^(1-1/p), jednoznaczność, drugi ślad i zanik na W_0. |
| 073–075 | Poprawne: konstrukcja F,c,u, słabe pochodne i H², odcięcie brzegowe i kontrola błędu, wygładzanie bez założenia twierdzenia o jądrze śladu, obie granice w tożsamości wariacyjnej. |
| 076–077 | Poprawne: Fubini, wzór Greena, skok -1, delta z poprawnym znakiem, rozwiązanie dla f=1, jednoznaczność i oszacowanie energetyczne. |
| 078–081 | Poprawne: jakobian, reguła łańcuchowa, istotne supremum, konieczność równości wykładników przez obie granice, nadkrytyczny kontrprzykład do ciągłości, zakres podsumowania. |

Bilans: 20/20 kryteriów, 0 błędów w dowodach, jedno doprecyzowanie hipotezy uwagi. Commit e7f5fbf9495709d859c7dd06a84feb2485478251, blob 30091fad12a19e8bc03c3067f84f30c847e43dfe. Nie zmieniono żadnego dowodu ani etykiety.
Trzecia lektura: 81/81 kryteriów; łącznie w iteracjach 143–146 wykryto niespójność geometrii rysunku, skorygowano położenie oznaczeń, interpunkcję i zakres wykładnika w uwadze. Nie jest to recenzja przez inną osobę ani formalizacja Lean.

CI 45615088872 (commit 13313d1d9318a48e7b2f8aa2714c08b8998947ac): success, obejmuje 5 testów. CI 45615511704 (commit ec008cd2d4ed4c55bb8505bec389b08265a3f63e): queued w chwili odczytu. Po ostatniej korekcie wymagane CI aktualnego źródła oraz inspekcja renderu; poprzedni PDF nie jest końcowym artefaktem.
Nie kompilowano pełnej książki. Nie uznawać rozdziału za ustabilizowany przed potwierdzeniem ostatniego przebiegu oraz kontroli wizualnej.
Następna iteracja 147: ostatnie CI, log i porównanie renderów po drobnych korektach; kontrola różnic względem lektury i decyzja o stabilizacji. Jeśli wszystkie bramki przejdą, zamknąć rozdział 09 i rozpocząć 10 w kolejnej iteracji.
