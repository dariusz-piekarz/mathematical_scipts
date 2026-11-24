# MA1-21 — trwałe kryteria regresyjne
Testy w dokładnej arytmetyce sprawdzają skończone świadki oraz tożsamości algebraiczne i współrzędne. Nie zastępują dowodów twierdzeń.
| ID | Etykieta | Kryterium | Metoda |
|---|---|---|---|
| MA1-21-001 | ma1:def:local-extremum, ma1:thm:fermat | Lokalne ekstremum względne, punkt wewnętrzny, znaki ilorazów jednostronnych | semantyczna + Python |
| MA1-21-002 | ma1:ex:fermat-assumptions | x³, wartość bezwzględna i końce przedziału; brak implikacji odwrotnej | semantyczna + Python |
| MA1-21-003 | ma1:thm:rolle | Ekstrema osiągane, przypadek stały, co najmniej jedno ekstremum wewnętrzne | semantyczna + Python |
| MA1-21-004 | ma1:ex:rolle-assumptions | Trzy kontrprzykłady po usunięciu pojedynczych założeń | semantyczna |
| MA1-21-005 | ma1:thm:lagrange | Funkcja pomocnicza, równe wartości na końcach, zastosowanie Rolle'a | semantyczna + Python |
| MA1-21-006 | ma1:ex:lagrange-witnesses | Świadek jedyny, dwa świadki i każdy punkt dla funkcji afinicznej | semantyczna + Python |
| MA1-21-007 | ma1:thm:cauchy-mvt | Tożsamość iloczynowa, bez dzielenia, funkcja pomocnicza | semantyczna + Python |
| MA1-21-008 | ma1:cor:cauchy-ratio, ma1:ex:cauchy-degenerate | Niezerowość przyrostu g przez Rolle'a, mianowniki, przypadek zdegenerowany | semantyczna + Python |
| MA1-21-009 | ma1:thm:derivative-monotonicity | Obie implikacje dla nieostrych znaków, ostre znaki wystarczają, stałość i przedział | semantyczna + Python |
| MA1-21-010 | ma1:cor:strict-monotone-nonflat | Nieujemna pochodna i dodatnia wartość w każdym podprzedziale, oba kierunki | semantyczna |
| MA1-21-011 | ma1:cor:equal-derivatives | Różnica stała; kontrprzykład dla niespójnej dziedziny | semantyczna |
| MA1-21-012 | ma1:thm:mvt-increment-bounds | Oszacowania dwustronne, kolejność punktów i równoważność Lipschitza z ograniczoną pochodną | semantyczna + Python |
| MA1-21-013 | ma1:cor:inverse-lipschitz-mvt | Dolne dodatnie ograniczenie, iniektywność, stała 1/m odwrotności | semantyczna + Python |
| MA1-21-014 | ma1:ex:mvt-elementary-bounds | Sinus, cosinus i logarytm; ścisłe nierówności dla x>0 | semantyczna + Python |
| MA1-21-015 | ma1:thm:derivative-endpoint-limit | Ciągłość na końcu, obie strony, granica skończona lub niewłaściwa, brak implikacji odwrotnej | semantyczna + Python |
| MA1-21-016 | ma1:thm:rolle, ma1:thm:lagrange | Punkty, obecność dokładnie jednej stycznej poziomej Rolle'a, obecność obu prostych Lagrange'a i ich nachylenia oraz przechodzenie przez właściwe punkty z rzeczywistego źródła TikZ; poprawność składu | Python + PDF |


## Niezależny przegląd stabilizacyjny — 2026-11-24, 23:43 CET

Sprawdzono wszystkie siedem sekcji źródła (blob `2a5919bcd4239d01d5cfbbe4420aa5283688aba5`) i 16 kryteriów. W szczególności:
- Fermat: znak ilorazu dla ujemnego przyrostu, przejście do minimum przez zmianę znaku; Rolle: istnienie ekstremum wewnętrznego również gdy wartość końcowa jest jednym z ekstremów.
- Lagrange i Cauchy: poprawne funkcje pomocnicze; przypadki zerowych przyrostów bez dzielenia, niezerowość przyrostu g w wersji ilorazowej oraz świadek 14/9.
- Monotoniczność i Lipschitz: ciągłość na końcach podprzedziału, oba kierunki implikacji dla słabych znaków, kontrprzykład dla ścisłej monotoniczności; warunek Lipschitza odwrotności z dolnego ograniczenia pochodnej przez oszacowanie przyrostów (bez założenia górnego ograniczenia f').
- Granice pochodnej: ciągłość wymagana wyłącznie na badanym końcu, punkty pośrednie pozostają wewnątrz przedziału, poprawny znak lewego ilorazu, przypadki skończone i niewłaściwe.
- Rysunki: sprawdzono z kodu TikZ współrzędne, nachylenia i przechodzenie prostych przez właściwe punkty. Nie wykonano niezależnej wizualnej inspekcji PDF w tej iteracji.

Wynik: brak nowych błędów merytorycznych w przeglądzie; bez zmiany treści matematycznej ani zakresu rozdziału. CI [45502844761](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45502844761), commit `7e670aeaeaf14727bf5dea7131b74f04ec0968bb`: wszystkie regresje zaliczone (rozdział 21: 14/14), obie kompilacje LaTeX zakończone pomyślnie, końcowy PDF 129 stron, kontrola odsyłaczy zaliczona. To wynik istniejącego wykonania CI, nie nowego uruchomienia ani formalizacji Lean. Pełna stabilizacja wymaga jeszcze potwierdzenia wizualnego PDF.
