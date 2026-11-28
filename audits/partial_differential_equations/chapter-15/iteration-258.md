# RRC 15 — iteracja 258: druga lektura 059–064

Źródło przed ebf06e497a4180f2c5705857772746b73da6adf3 (1453 wiersze), po b4952ce41cfeb61edb446c84bd59948940bed4f6 (1457 wierszy); commit 0546cf6b9b55e2f49678e7c1cdb4b3780a4c5fc1.

| Kryterium | Wynik drugiej lektury |
|---|---|
| 059 | Skok a: 1<=a<=2, u ciągła i przedziałami afiniczna; rachunek słabej pochodnej bez składnika brzegowego, stały strumień au'=1, f=0 — poprawne. |
| 060 | Ujemny skok u' i dodatni skok a; u''=-delta_0/2, a'=delta_0; testy zeta(x/epsilon) o normie sqrt(epsilon) dowodzą braku reprezentacji L²_loc, a zatem także braku W^{1,infty}_loc dla a na ograniczonym otoczeniu — poprawne. |
| 061 | Odczytano pełną uwagę rem:pde12-corners: sektor Lipschitzowski, beta=2/3, harmoniczność, norma gradientu, odcięcie narożnika i błąd kwadratu normy O(epsilon^{4/3}), ślad zero i f wsparta w pierścieniu. Nie ma składnika Diraca w wierzchołku poza otwartym obszarem — poprawne. |
| 062 | Druga radialna pochodna -2/9 r^{-4/3} sin(2theta/3), podsektor 3pi/8<theta<9pi/8 odpowiada argumentom pi/4..3pi/4, norma Frobeniusa dominuje moduł pochodnej, całka r^{-5/3} rozbieżna; odróżnienie H²_loc od H² — poprawne. |
| 063 | Uściślono podsumowanie globalnej regularności: warunki są wystarczające, nie konieczne dla poszczególnych rozwiązań; jawna jednostajna eliptyczność, W^{1,infty}, H_0¹ i niejednorodny ślad przedłużalny do H². |
| 064 | 23 etykiety, 76/76 odsyłaczy do 35 celów rozwiązanych jednoznacznie w sprawdzonych RRC 07,09,10,12,13,14,15; osiem sekcji, poprawny stos środowisk. Zmiana podsumowania nie zmienia zestawu odsyłaczy. |

Druga lektura 64/64, z poprawkami w 252,255,258; nie jest jeszcze pełnym czystym przebiegiem. Nie uruchamiano kompilacji PDF ani CI. Następna iteracja 259: III/001–012, początek trzeciej lektury stabilizacyjnej.
