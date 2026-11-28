# PDE — rozdział 09 — iteracja 144: trzecia lektura 023–048

Data: 2026-11-25. Gałąź: biblioteka-matematyczna-iteracja-6.
Źródło poddane lekturze: b14ed2a90f238b9b1429b49712f6b933b1075bf4.

| Kryteria | Wynik kontroli |
| --- | --- |
| 023–024 | Bez zmian. Sprawdzono thm:pde7-mollify i thm:pde7-approx-id w źródle rozdziału 07: lokalna dziedzina, pochodne dystrybucyjne, zbieżność na K, skończona liczba norm. |
| 025–027 | Bez zmian. Poprawna indukcja wielowskaźnikowa, zwarty nośnik, globalizacja zbieżności dla p skończonego, kontrprzykład dla p=infty i lokalne włożenia. |
| 028 | Usterka rysunku: nominalny odstęp pionowy K od brzegu U wynosił 0.50 przy promieniu 0.80, wbrew warunkowi jednolitego odstępu w podpisie. Zmieniono wysokość K na [-.25,.25], odstęp pionowy 0.90, poziomy 1.35; przesunięto podpis K i zmniejszono zaokrąglenie K. K + domknięta kula promienia .80 mieści się w centralnym pionowym pasie U także po uwzględnieniu zaokrągleń. |
| 029–033 | Bez zmian. Wyczerpanie, przypadki pustych zbiorów, monotoniczne odcięcia, lokalna skończoność V_j, aproksymacja przez splot i sumowalność błędów (nie wymaga się globalnej zbieżności szeregu w_j). |
| 034–036 | Bez zmian. Odczytano konstrukcję odcięcia w thm:pde8-density; poprawne ogony L^p, pochodne skalowania, kontrprzykład dla p=infty i stała na przedziale z niezerowym śladem. |
| 037–041 | Bez zmian. Izometria przedłużenia z domknięcia testów, identyfikacja wszystkich słabych pochodnych przez granice L^p, domkniętość obrazu; znak delta_0-delta_1 i kontrprzykład na przedziale z usuniętym zerem. |
| 042–046 | Bez zmian. Jednowymiarowe czynniki długości, Jensen i Fubini dla uśredniania, różniczkowanie pod całką, przejścia na kostkach wewnętrznych i granica q do nieskończoności. |
| 047–048 | Bez zmian. Wersja zerowego warunku brzegowego w każdym kierunku, przypadki p=1 i d=1, równoważność norm z podanymi stałymi. |

Bilans: 26/26 kryteriów poddano lekturze, 25 bez zmian, 1 poprawka rysunku. Trzecia lektura obejmuje dotąd 48/81 kryteriów. Nie zmieniono dowodów ani treści twierdzeń.
Poprawka: e79208d26de9eae9ed1e951fb0afdfe524f979a4, blob 2cd9a78d25e10189f0f6979e78c2844d791e549b.
Dodano test PDE-09-028 w test_sobolev.py: 13313d1d9318a48e7b2f8aa2714c08b8998947ac. Test odczytuje współrzędne TikZ i kontroluje warunek jednolitego odstępu z konserwatywnym marginesem na zaokrąglone narożniki. Nie zastępuje inspekcji wizualnej. Pierwsza próba zapisu testu otrzymała konflikt współbieżnej aktualizacji gałęzi; ponownie odczytano plik, następny zapis powiódł się.
Run 45615011459 dla poprawki rysunku: in_progress w chwili kontroli. Wynik testu dodanego w następnym commicie i nowy render nie są jeszcze potwierdzone. Nie wykonywano Lean ani pełnej kompilacji książki.

Następna iteracja 145: kontrola wyników CI dla nowego testu i rysunku, inspekcja renderu oraz trzecia lektura kryteriów od PDE-09-049. Nie zamykać rozdziału przed zakończeniem audytu i rewalidacji.
