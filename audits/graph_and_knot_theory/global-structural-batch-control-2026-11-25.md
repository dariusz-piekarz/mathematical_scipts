# Globalna kontrola strukturalna — 2026-11-25

Gałąź: biblioteka-matematyczna-iteracja-6.

Rzeczywisty odczyt 44 źródeł wskazanych przez books/pl/graph_and_knot_theory.tex w pięciu partiach, z pominięciem komentarzy i listingów. Kontrola zagnieżdżenia środowisk, etykiet i odsyłaczy w każdej partii:

| ID źródeł | etykiety | odsyłacze | błędy środowisk | duplikaty wewnątrz partii |
| --- | ---: | ---: | ---: | ---: |
| 00–05, 37–39 | 148 | 54 | 0 | 0 |
| 40–43, 06–10 | 203 | 129 | 0 | 0 |
| 11–19 | 92 | 70 | 0 | 0 |
| 20–28 | 128 | 35 | 0 | 0 |
| 29–36 | 139 | 57 | 0 | 0 |
| Razem | 710 | 345 | 0 | 0 |

W dodatkowych dwóch odczytach potwierdzono istnienie wszystkich 24 różnych celów odsyłaczy wychodzących poza ich partie: rozdziały 01, 02, 04, 05, 06, 07, 08, 09, 17, 29, 35, 37, 43. W każdej partii wszystkie pozostałe odsyłacze mają lokalny cel. Nie wykryto brakujących celów.

Ograniczenia: to kontrola zdalna partiami, nie uruchomienie narzędzia tools/tests/test_graph_and_knot_global.py --strict. Nie porównano globalnie wszystkich etykiet między partiami ani całego katalogu plików na dysku. Odczyty nie były przypięte do jednego SHA; nie stanowią atomowego obrazu gałęzi. Lokalny git ls-remote zakończył się błędem DNS, mimo dostępności pdflatex. Nie potwierdzono CI ani kompilacji i wizualnej kontroli PDF. Nie zamykać stabilizacji technicznej.

Następnie: pełna kontrola globalna unikatowości, test --strict, CI i PDF. Nie utożsamiać kontroli strukturalnej z audytem poprawności matematycznej wszystkich rozdziałów.
