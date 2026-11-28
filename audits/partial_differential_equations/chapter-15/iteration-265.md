# RRC 15 — iteracja 265: trzecia lektura 059–064

Źródło b4952ce41cfeb61edb446c84bd59948940bed4f6 (1457 wierszy), bez zmian. Ponownie odczytano oba kontrprzykłady, podsumowanie i pełny dowód konstrukcji sektora w uwadze rem:pde12-corners. Sprawdzono programowo odsyłacze i stos środowisk.

| Kryterium | Wynik trzeciej lektury |
|---|---|
| 059 | a przyjmuje wartości 1 oraz 2 na odpowiednich półprzedziałach; u przedziałami afiniczna, ciągła w zerze, słaba pochodna 1 i 1/2. Całkowanie przez części nie daje składnika brzegowego w zerze, strumień au'=1 i równanie jednorodne — poprawne. |
| 060 | Rachunek dystrybucyjny u''=-delta_0/2 i a'=delta_0. Testy zeta(x/epsilon) o nośniku w (-epsilon,epsilon) i normie sqrt(epsilon) razy norma zeta dowodzą braku reprezentanta L²_loc; lokalne L∞ na ograniczonym przedziale implikowałoby L², więc a nie jest W^{1,infty}_loc — poprawne. |
| 061 | Sektor o kącie 3pi/2 jest Lipschitzowski także przy wierzchołku i na połączeniach łuku z odcinkami, zgodnie z RRC 12. beta=2/3, harmoniczność i norma gradientu 4/9 r^{-2/3}; całkowalność i zerowy ślad przez odcięcie wierzchołka z błędem O(epsilon^{4/3}) w kwadracie normy składnika z gradientem odcięcia. F=-2 grad eta dot grad w-w Delta eta ograniczona na pierścieniu. Wierzchołek nie należy do otwartego obszaru, więc nie powstaje wewnętrzny składnik dystrybucyjny — poprawne. |
| 062 | Druga pochodna radialna -2/9 r^{-4/3} sin(2theta/3); na podsektorze argument sinusa należy do (pi/4,3pi/4), moduł >=1/sqrt(2). Norma Frobeniusa dominuje moduł drugiej pochodnej radialnej; po zmianie na współrzędne biegunowe całka r^{-5/3} rozbieżna. Gładkość we wnętrzu nie przeczy brakowi globalnego H² — poprawne. |
| 063 | Podsumowanie podaje lokalne hipotezy H², globalne warunki wystarczające (nie konieczne) i niejednorodny ślad przedłużalny do H², a także gładkość przy gładkich współczynnikach i prawej stronie; nie utożsamia gładkości z analitycznością — poprawne. |
| 064 | 23 etykiety, osiem sekcji, 76/76 odsyłaczy do 35 celów w RRC 07,09,10,12,13,14,15; brak brakujących lub wieloznacznych celów w sprawdzonym zbiorze, stos środowisk pusty bez błędów — poprawne. |

Trzecia lektura 64/64, pełny przebieg 259–265 bez nowych usterek na niezmienionym blobie b4952ce41cfeb61edb446c84bd59948940bed4f6. Nie zmieniano źródła. Nie uruchamiano kompilacji PDF ani CI; kontrola strukturalna nie zastępuje kompilacji. Następna iteracja 266: odrębny audyt kontrolny całego rozdziału i przygotowanie odbioru technicznego (PDF, wizualna kontrola stron, CI).
