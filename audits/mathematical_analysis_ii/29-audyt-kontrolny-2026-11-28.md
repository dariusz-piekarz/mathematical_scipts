# AM II 29 — audyt kontrolny

Data: 2026-11-28. Źródło niezmienione od commitu 9fb478eadd3e59976824b2dca4546c834ff2e6ac, blob 97a931a11b67ff5ec81a81b29fe948b97c45b76f, 637 wierszy.

## Kontrola merytoryczna
- Długość: addytywność także przy wartości nieskończonej, nierówności współrzędnościowe, reparametryzacja monotoniczna oraz zbieżność łamanych dla dowolnych podziałów o średnicy dążącej do zera — poprawne.
- Krzywe absolutnie ciągłe: reprezentacja współrzędnych przez całki, oszacowanie przyrostu i argument z ilorazami na podziałach dyadycznych oraz lematem Fatou — poprawne.
- Parametryzacja długością łuku: ciągłość funkcji długości, jednoznaczność faktoryzacji, własność Lipschitza i jednostkowa prędkość prawie wszędzie; przypadki postojów i długości zerowej; regularność C1 i równoważność absolutnej ciągłości funkcji długości — poprawne.
- Miara Hausdorffa: elementarne oszacowanie rzutem skalarnym dla podłuków, addytywność z pominięciem skończonych przecięć zerowej miary, wzór także dla różnowartościowych krzywych nieprostowalnych — poprawne.
- Krotność: borelowskość przez przeliczalne sumy zwartych obrazów krotek parametrów; zastosowanie wzoru ME 28 do przedłużonej parametryzacji Lipschitzowskiej z ograniczeniem do [0,L]; wyjątki odpowiadające postojom tworzą przeliczalny zbiór obrazu; kryterium równości długości i miary obrazu poprawne.
- Przykłady: okrąg, helisa, funkcja Cantora, ostrze (t²,t³), wykres t sin(1/t) — zgodne z twierdzeniami i rachunkami.

## Statyka i technika
21 etykiet, 21 odsyłaczy wewnętrznych (AM II 26, 29), 11 zewnętrznych (AM I 33, 37; ME 17, 26, 28). Wszystkie cele sprawdzone w aktualnych źródłach. Bez duplikatów etykiet w kontrolowanych rozdziałach 26 i 29. Bilans klamer i środowisk poprawny; katalog i entrypoint zawierają 29 po 28, przed 36. Dwa rysunki bez zmian; nie powtarzano ich kompilacji.

CI źródła 9fb478e: terminologia #46132174238 success, walidacja AM II #46132174235 in_progress, dodatkowa walidacja #46132180231 skipped, aplikacja #46132174264 cancelled. Pełny PDF niepotwierdzony. Nie uruchomiono dodatkowego workflow.

Wynik: zero nowych uwag merytorycznych i statycznych, źródło bez zmian. Odbiór techniczny otwarty.

## Przygotowanie rozdziału 30
Sprawdzono rzeczywiste źródła:
- ME 12: thm:lebesgue-products-12, thm:completed-product-fubini-12, thm:tonelli-12, thm:fubini-12, cor:practical-fubini-12, cor:associative-product-12. Wykorzystać wersję dla uzupełnionej miary produktowej, uwzględnić wyjątki przekrojowe.
- ME 13: thm:linear-change-13, thm:change-variables-13, cor:change-subdomain-13. Nie powielać konstrukcji miary ani pełnego dowodu zamiany zmiennych; rozwinąć rachunek na zbiorach mierzalnych w R^n.
- AM II 24: ma2:thm:riemann-box-lebesgue, ma2:thm:jordan-criterion. Dodać wersję iterowania całek Riemanna i wyraźnie oddzielić jej warunki od Lebesgue'a.
- AM II 18: ma2:cor:inverse-global-injective, ma2:cor:inverse-jacobian. Sprawdzanie dyfeomorfizmu i wyznacznika.
Plan: przekroje obszaru, iterowanie i zmiana kolejności całkowania, kontrprzykłady bez całkowalności bezwzględnej, podstawienia liniowe i nieliniowe, współrzędne biegunowe, walcowe i sferyczne, zbiory wyjątkowe miary zero, przykłady obliczeniowe i rysunki. Nie utworzono jeszcze rozdziału 30.
