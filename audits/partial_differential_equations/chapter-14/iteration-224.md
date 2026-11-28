# RRC 14 — iteracja 224: pierwsza lektura 045–058

Źródło przed 99ba6a2ae7b7f04146a7b540248fea76dfd07a48, po 769eb0a329439062f16dd9aac6f3f5899e5ef11e; commit 7ec348b2617500628c1a7c43a93a7d84370700fd. Odczytano sekcję 8 i odpowiednie wyniki RRC 03 o rozwiązaniu fundamentalnym, definicji Greena, kuli oraz reprezentacji i tożsamościach Greena.

| Kryterium | Wynik |
|---|---|
| PDE-14-045 | Rozwiązanie fundamentalne, normalizacja, lokalna całkowalność i pochodna radialna z RRC 03. |
| PDE-14-046 | Jawne założenie istnienia harmonicznej poprawki; nie deklarujemy rozwiązywalności dowolnego problemu Dirichleta. |
| PDE-14-047 | Tożsamość dystrybucyjna po przesunięciu bieguna; ciągłość i zerowe wartości na brzegu. |
| PDE-14-048 | Równoważność definicji z RRC 03 przez lemat Weyla i jednoznaczność harmonicznej poprawki. |
| PDE-14-049 | Nieujemność przez zasadę maksimum na zbiorze z wyciętą kulą, bez wymagania jego spójności. |
| PDE-14-050 | Spójność obszaru po usunięciu punktu dla d>=2 przez drogę omijającą biegun; ścisła dodatniość przez mocną zasadę i osobliwość. |
| PDE-14-051 | Formuły kuli z RRC 03 w obu wymiarach, wspólna regularna część Q_R i jawna formuła w środku. |
| PDE-14-052 | Symetria, dodatniość Q_R, gładkość poprawki na otoczeniu domknięcia kuli, zerowy brzeg i geometria odwróconego bieguna. |
| PDE-14-053 | Pochodna normalna: gradient rozwiązania fundamentalnego, czynnik (|x|/R)^2, skrócenie iloczynów skalarnych, oba wymiary i bezpośredni przypadek x=0. |
| PDE-14-054 | Osłabiono zbędne założenie g w C² do ciągłości; nie zmieniono wymogu C¹ rozwiązania aż do brzegu. |
| PDE-14-055 | Naprawiono lukę w stosowaniu drugiej tożsamości Greena: najpierw na mniejszej kuli B_s z wyciętą kulą, potem s rośnie do R, z kontrolą całek i normalnych. |
| PDE-14-056 | Rozpisano trzy składniki całki na wewnętrznej sferze, normalną do środka oraz zanik błędów rzędu rho lub rho*abs(log rho). |
| PDE-14-057 | Całkowalność Gf, przejście przez zbieżność zmajoryzowaną, znaki i dokładny wzór reprezentacyjny. |
| PDE-14-058 | Dodatniość, porównanie dwóch rozwiązań i jednoznaczność; rozróżnienie reprezentacji istniejącego rozwiązania od istnienia klasy C² przy ciągłym f. |

9 zamian blokowych; 1143 wiersze, 34 etykiety zachowane w kolejności. 57/57 wystąpień odsyłaczy, 39 różnych celów, rozwiązane jednoznacznie na przypiętym commicie w RRC 01,03,07,09,10,13,14,15,17; stos środowisk poprawny. 360/360 pomocniczych skończonych kontroli rachunku pochodnej normalnej i tożsamości Q_R na sferze (nie dowód ani testy CI; połowa kontroli to elementarna tożsamość geometryczna). Nie wykonano dedykowanej kompilacji, kontroli wizualnej PDF ani Lean.

Pierwsza lektura 58/64, 8/10 sekcji. Następna: 059–064, rysunek bariery, zakres twierdzeń, struktura i odsyłacze; zamknięcie pierwszej lektury, następnie druga lektura.