# RRC 14 — iteracja 226: druga lektura 001–020

Źródło przed 5243acd91b5769211b26efc92b9b7f56cf929c48, po f8d608fbb8c50561f060c95700c27b1e1f3714de; commit 9df3a04660a931e9f074ac0ab05319b879549ba6. Ponowna lektura pierwszych trzech sekcji oraz faktycznych tez zależności w RRC 01,03,07,09,10,13.

| Kryterium | Druga lektura |
|---|---|
| 001 | Wspólny zbiór pełnej miary, rzeczywistość, brak symetrii A, miara brzegu — poprawne. |
| 002 | Forma z b=0, ograniczoność i znak testów — poprawne. |
| 003 | Doprecyzowano wybór zwartego K_n, zachowanie nośników funkcji i pochodnych, zbieżność lokalną w L² przechodzącą w globalną H¹ oraz przypadek v_n=0. |
| 004 | Rozkład testu na części, zerowy ślad każdej i liniowość — sprawdzone z tezami RRC 09,10,13. |
| 005 | Uzasadniono ślad stałej odsyłaczem do twierdzenia o śladzie; obcięcie i jądro operatora śladu poprawne. |
| 006 | Argument energetyczny, eliptyczność i Poincaré przy zerowym śladzie — poprawne, również dla niesymetrycznej A. |
| 007 | M>=0 oraz kontrprzykład cosh przy M<0; kontrola kresu istotnego — poprawne. |
| 008 | Porównanie przez różnicę; warunek c-div b/2>=0 sprawdzony z treścią RRC 13. |
| 009 | Sinus przy c=-pi²: rezonans, ślad i całkowanie przez części poprawne. |
| 010 | Lemat Weyla dla d>=2 i realność reprezentanta z iniektywności; przypadek d=1 afiniczny — poprawne. |
| 011 | Własność średniej i ścisła dodatniość całki z ciągłej nieujemnej funkcji na fragmencie sfery — poprawne. |
| 012 | Zbiór poziomowy otwarty i domknięty; jawnie dodano rzeczywistość funkcji do tezy. |
| 013 | Dodatniość i jednoznaczność przez RRC 01; jawnie zapisano, że U jest obszarem. |
| 014 | Doprecyzowano wprowadzenie do słabej zasady minimum; normalna odnosi się do kuli. |
| 015 | Odejmowanie minimum, dodatniość, domknięcie kuli zawarte w domknięciu U — poprawne. |
| 016 | Rachunek bariery i próg alpha>2d/R² poprawne. |
| 017 | Dodatnie minimum na wewnętrznej sferze i wybór epsilon — poprawne. |
| 018 | Rozpisano położenie punktu x0-t nu i pochodną funkcji q w zerze; rozróżnienie liminf i skończonej pochodnej poprawne. |
| 019 | Rozpisano gradienty i laplasjany r,theta, ortogonalność i zastosowanie reguły łańcuchowej w klinie. |
| 020 | Brak kuli stycznej przez odległości od prostych; kąt mniejszy niż pi/2 — poprawne. |

7 zamian blokowych; 1244 → 1270 wierszy. Zachowano 34 etykiety w kolejności. 66/66 wystąpień odsyłaczy (41 różnych celów) jednoznacznie rozwiązanych w dziewięciu rozdziałach RRC na przypiętym commicie; stos środowisk poprawny. Pierwsza lektura 64/64, druga 20/64. Druga lektura nie jest czysta — wymagała uzupełnień. Dla commitu źródłowego w momencie kontroli oba przebiegi CI były w toku (45719013749 i 45719013432); nie ma potwierdzonego PASS. Dedykowana kompilacja rozdziału, aktualny render TikZ/PDF oraz kontrola rysunku RRC 02 niewykonane.

Następna iteracja 227: druga lektura 021–032 według numeracji raportów 221–222, jądro Poissona, Harnack, Liouville i pochodne; sprawdzić CI oraz możliwość renderowania.
