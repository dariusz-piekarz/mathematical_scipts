# PDE — rozdział 09 — iteracja 145: trzecia lektura 049–061

Data: 2026-11-25. Gałąź: biblioteka-matematyczna-iteracja-6.
Źródło poddane lekturze: 2cd9a78d25e10189f0f6979e78c2844d791e549b.

| Kryteria | Wynik kontroli |
| --- | --- |
| 049 | Poprawne: mnożnik C¹, lokalne wygładzenie w W^{1,1}, klasyczne całkowanie przez części bez podstawiania niegładkiego testu, globalna całkowalność. |
| 050–052 | Poprawne: rozkład różnicy iloczynów, Hölder, przypadki sprzężone 1 i nieskończoność przez ograniczenie wygładzeń oraz wspólny podciąg z sumowalnymi błędami; lokalizacja dla algebry W^{1,infty}. |
| 053–055 | Poprawne: warunek F(0)=0, wyjątki, oszacowanie Lipschitza, Tonelli i zmajoryzowanie przy przejściu do granicy pochodnych; przypadek p=infty przez lokalne p=1. |
| 056–057 | Poprawne: całka zorientowana, błąd min(abs(t),4/n), majoranty L^p, zamkniętość pojedynczej pochodnej i jednoczesne zanikanie składowych gradientu na poziomicy. Poprawiono wyłącznie interpunkcję przed „Istotnie”. |
| 058–061 | Poprawne: normalizacja wygładzeń G_n w zerze, ograniczenie pochodnych, zbieżność poza punktami załamania i zanik gradientu na ich przeciwobrazach; obcięcia, znaki części ujemnej, zbieżność ogonów przy skończonym p i zakres twierdzenia. |

Bilans: 13/13 kryteriów w tej lekturze, 0 usterek matematycznych, jedna korekta interpunkcyjna. Łącznie 61/81 kryteriów trzeciej lektury.

## Walidacja techniczna
Run 45615011459 dla geometrii rysunku: success. Artefakt 15021323855 pobrany, SHA-256 48032980f03c54dccefaa10d3f87eb7480b07ba13251867b2bafa7c379d6398d zgodny z metadanymi. Porównano 25 renderów z poprzednią wersją: 24 identyczne, jedyna różnica na stronie 9, bbox (425,848,562,906). Krytycznych diagnostyk z listy workflow w logu nie znaleziono. Obejrzano stronę 9; geometria spełnia warunek odstępu, natomiast oznaczenia x i epsilon dotykały konturu zwężonego K. Przesunięto oba oznaczenia pionowo bez zmiany współrzędnych środka, promienia i zbiorów.
Run 45615088872 dla testu geometrycznego (commit 13313d1d9318a48e7b2f8aa2714c08b8998947ac): rzeczywisty etap wykonywalnych testów oraz przygotowania rozdziału zakończony sukcesem według API jobs; kompilacja trwała przy odczycie. Nie potwierdzono końcowego wyniku.
Korekta oznaczeń i interpunkcji: commit ec008cd2d4ed4c55bb8505bec389b08265a3f63e, blob 89a29c43f713f2e4b304e201fdd0c4518a3cf9ac. Po tej korekcie wymagane ponowne CI i kontrola renderu. Nie wykonywano Lean ani pełnej kompilacji książki.
Następna iteracja 146: lektura kontrolna od PDE-09-062, odczyt CI i walidacja nowego renderu. Pozostało 20 kryteriów trzeciej lektury.
