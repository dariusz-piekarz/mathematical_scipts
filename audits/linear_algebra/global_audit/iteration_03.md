# Globalny audyt algebry liniowej — iteracja 03/09

**Data:** 22 listopada 2026, 03:00 CET.  
**Wejściowy HEAD:** `b357ef0508cf5d452a2d7acb56ea17e5ac8d1e1f`.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Zakres:** rozdziały 09–12.  
**Instrukcje:** `AGENTS.md`, `docs/pl/standardy_terminologiczne.md`, `books/pl/linear_algebra.tex`, `catalog/books.json`, raporty iteracji 01 i 02.

## Kontrola źródeł i matematyki

Odczytano pełne źródła czterech rozdziałów (32 056, 34 688, 42 119 i 26 641 znaków). Zweryfikowano obecność i strukturę 66 dowodów (14 + 20 + 19 + 13). Ponadto szczegółowo sprawdzono wybrane dowody i rachunki:

- **09:** wzór \(\dim U^{\perp_b}=n-\dim U+\dim(U\cap\operatorname{Rad}b)\), ortogonalną sumę prostą, diagonalizację form symetrycznych i polaryzację w charakterystyce 2. Argumenty wykorzystują jawnie niezdegenerowanie lub jego brak.
- **10:** konstrukcję iloczynu tensorowego jako ilorazu przestrzeni wolnej; odwzorowanie \(W\otimes V^*\to\operatorname{Hom}(V,W)\) z obrazem operatorów skończonego rzędu; dokładność \(U\otimes W\to V\otimes W\to(V/U)\otimes W\), udowodnioną przez algebraiczne dopełnienie.
- **11:** uniwersalną własność algebry zewnętrznej nad dowolnym ciałem; wzór na iloczyn zewnętrzny form przez przetasowania i rozwinięcie Laplace'a; symetryzatory i antysymetryzatory pod warunkiem \(k!1_K\ne0\).
- **12:** zespoloną tożsamość polaryzacyjną przy antyliniowości pierwszego argumentu (znak \(-i\) jest poprawny); reprezentację Riesza z poprawnym sprzężeniem współczynników; ortogonalizację Grama--Schmidta; przykład dodatnio określonej macierzy Grama z wyrazem \(i\).

Nie znaleziono błędów matematycznych w szczegółowo sprawdzonych fragmentach. Samo istnienie dowodu przy pozostałych twierdzeniach nie jest poświadczeniem pełnej niezależnej weryfikacji każdego kroku.

## Rzeczywiście poprawione usterki

1. **Rozdział 10:** zastąpiono niedopuszczony samodzielny rzeczownik „dualami” przez „przestrzeniami dualnymi”.
2. **Rozdział 12:** poprawiono osiem wystąpień niegramatycznego „sprzężenie liniowa/liniowy/liniowe/liniowym” na „antyliniowa/antyliniowy/antyliniowe/antyliniowym”, w definicjach, przykładach, dowodach i podsumowaniu. Zachowano konwencję matematyczną.

Nie dodano twierdzeń, nie zmieniono etykiet. Rozdziały 09 i 11 pozostały bez zmian.

## Rysunki, skład i ograniczenia

Źródła 09–12 zawierają odpowiednio 1, 1, 2 i 0 rysunków. Skontrolowano ich obecność i strukturę w źródłach; **nie wykonano wizualnej inspekcji stron PDF**. Nie wygenerowano osobnego PDF. Po zapisie konieczna jest weryfikacja CI dla aktualnego SHA; nie deklarujemy PASS bez wyniku. Bezpośrednie porównanie z DG-01 nie zostało przeprowadzone, ponieważ wstępnie sprawdzona ścieżka źródła DG-01 nie istnieje.

**Status:** iteracja 03 wykonana, ale nie czysta (wprowadzono korekty; PDF/CI do potwierdzenia). Wcześniejsze otwarte kontrole 01–08 pozostają otwarte. Następny blok: 13–16.
