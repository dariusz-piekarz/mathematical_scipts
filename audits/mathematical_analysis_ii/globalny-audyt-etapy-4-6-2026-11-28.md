# AM II — globalny audyt, etapy 4–6

Data: 2026-11-28. Migawka kontrolna źródeł: `e0c7fc4a2038590de4a8e2c178097d0065028ea2`.

## Zmiany merytoryczne

- `e2f09a1`: AM2-34 — formy zamknięte i dokładne, powiązanie z niezależnością całki od drogi, warunki jednokrotnej parametryzacji. Porównano z DG i TOP.
- `4cbdd48`: AM2-34 — całka formy z krotnością ze znakiem i przykład przeciwnych orientacji.
- `ad8de2f`: AM2-32 — korekta gęstości drutu przez krotność i przykład powtórnego przejścia.
- `4b70b4a`: AM2-28 — ciągłość całki na ruchomych zbiorach przy lokalnej zbieżności w mierze i przykład dyadyczny.
- `fc6172e`, `e0c7fc4`: AM2-37 — zerowość miary zbioru zer funkcji analitycznej i identyczność na zbiorze dodatniej miary; dowód przeniesiono za analityczne twierdzenie o funkcji uwikłanej, z samodzielnym oszacowaniem miary wykresu.

## Kontrola integralności źródeł

Porównano 38 plików rozdziałów z 38 wpisami `books/pl/mathematical_analysis_ii.tex` i planem `catalog/mathematical_analysis_ii_structure_plan.json`. Kolejność identyczna, każdy plik występuje raz, wszystkie numery kolejności od 1 do 38, żadnego brakującego pliku.

Przeskanowano wystąpienia `label`, `ref`, `eqref`, `pageref` w czterech grupach (kontrola tekstowa, nie parser TeX):

| Grupa | Etykiety | Odsyłacze | Duplikaty wewnątrz grupy |
|---|---:|---:|---:|
| 01–10 | 180 | 213 | 0 |
| 11–20 | 191 | 272 | 0 |
| 21–30 | 230 | 320 | 0 |
| 31–38 | 255 | 416 | 0 |
| Razem | 856 | 1221 | 0 wewnątrz grup |

Zweryfikowano istnienie celów odsyłaczy między grupami; nie wykryto brakującego celu lokalnego. Nie jest to jeszcze globalna kontrola powtórzeń etykiet między grupami ani pełna kontrola odsyłaczy `atlasref` do innych książek. Kompilacja TeX w CI sprawdza m.in. niezdefiniowane odsyłacze i wielokrotnie zdefiniowane etykiety; przebieg 46189819134 był w toku podczas kontroli. Terminologia w przebiegu 46189819046: success.

## Zakres dalszej kontroli

Sprawdzono dowody rozbieżności interpolacji Rungego i lematy użyte w twierdzeniu o alternansie. Pozostaje dokończenie kontroli aproksymacji, weryfikacja odsyłaczy zewnętrznych, wynik kompilacji aktualnego PDF i oględziny figur. Nie ogłasza się jeszcze stabilizacji całego tomu.

## Uzupełnienie: kontrola odsyłaczy zewnętrznych

Sprawdzono 187 wystąpień `atlasref` w AM II: 0 w AM2-01–10, 50 w AM2-11–20, 101 w AM2-21–30 oraz 36 w AM2-31–38. Dla każdej różnej pary identyfikatora rozdziału i etykiety odczytano rozdział docelowy i potwierdzono obecność etykiety. Wszystkie 38 rozdziałów docelowych znajduje się w katalogu `catalog/books.json`. Zakres: AM I, FA, LA, DT, PDE, ME, DG i TOP. Nie wykryto brakujących celów. Kontrola dotyczy źródeł i rejestracji, nie działania każdego odsyłacza w przeglądarce. Nie zmieniano treści rozdziałów. Przebieg kompilacji 46189819134 pozostawał w toku podczas kontroli.
