# RRC 14 — iteracja 231: trzecia lektura 001–020

Źródło przed aea713838936decff4ec31bb9c05a226b1160e70, po 52e83d128c67c3d18228f7ffaff226cb6e81b941; commit 58bb697745734709ec249ee00cd75f2847891175. Ponownie odczytano pierwsze trzy sekcje, sprawdzając numerację kryteriów według raportu 221, oraz tezy o śladach, Poincarém, porównaniu z dryfem i mocnej zasadzie maksimum w RRC 03,10,13.

| Kryterium | Trzecia lektura |
|---|---|
| 001 | Konwencje rzeczywiste, wspólny zbiór pełnej miary i niesymetryczna macierz — poprawne. |
| 002 | Forma, ograniczoność i nierówność dla nieujemnych testów — poprawne. |
| 003 | Rozkład testu na części, zgodność śladu, gęstość dodatnich testów przez obcięcie, zbieżność gradientów i wygładzanie — poprawne. |
| 004 | Obcięcie poziomowe, stała w H¹ i gradient — poprawne. |
| 005 | Ślad stałej, części dodatniej, zerowy ślad i H_0¹ — poprawne, także w d=1 zgodnie z RRC 10. |
| 006 | Dopuszczalność testu (u-M)^+ i zachowanie poza zbiorem poziomowym — poprawne. |
| 007 | Eliptyczność, znak członu zerowego, Poincaré, c=0 i przykład ujemnej granicy brzegowej — poprawne. |
| 008 | Porównanie przez różnicę i liniowość śladu — poprawne. |
| 009 | Usunięto niejednoznaczność oznaczeń: w=u-v, funkcja testowa w^+; jawna równość obu postaci składnika dryfu z obcięcia. Warunek c-div b/2>=0 zweryfikowany z RRC 13. |
| 010 | Kontrprzykład rezonansu dla ujemnego c i interpretacja słaba — poprawne. |
| 011 | Weyl, rzeczywistość reprezentanta; drobna korekta językowa zapisu d=1. |
| 012 | Globalne ekstremum w bieżącym rozdziale, lokalne w RRC 03 — poprawne. |
| 013 | Średnia sferyczna, dodatnia miara fragmentu, otwartość i domkniętość poziomicy — poprawne. |
| 014 | Dodatniość i jednoznaczność — poprawne; korekta zgodności gramatycznej. |
| 015 | Kula wewnętrzna i normalna do kuli, niekoniecznie do U — poprawne. |
| 016 | Jednostronna pochodna normalna, znak i związek z gradientem — poprawne. |
| 017 | Drugie pochodne bariery i próg alpha — poprawne. |
| 018 | Wybór epsilon i argument ujemnego minimum — poprawne. |
| 019 | Położenie punktu, pochodna q(0), liminf i znak — poprawne. |
| 020 | Klin: gradienty r,theta, laplasjan, o(r) i brak kuli wewnętrznej — poprawne. |

1 doprecyzowanie matematycznego zapisu (nie zmienia tezy ani wyniku) i 2 korekty językowe. 1418 → 1425 wierszy. 34 etykiety zachowane w kolejności; stos środowisk poprawny; 74/74 odsyłaczy (43 cele) jednoznacznie rozwiązanych w dziewięciu rozdziałach RRC na przypiętym commicie. Trzecia lektura 20/64, nie jest przebiegiem bez zmian. Nie stwierdzono nowych błędnych tez.

Najnowszy sprawdzony globalny workflow 45721042647: reader-ui success, index-and-test failure w Audit repository-wide chapter and graph coverage; log 139579139692 potwierdza wciąż ten sam nowy nierozpoznany odsyłacz CAL-11 AF-12::thm:lp-banach12 (aktualnie linia 1402 w tym przebiegu), 589 indeksowanych rozdziałów, 576 kwalifikowanych odsyłaczy lekturowych, 1 nieprawidłowy. Pozostałe 13 nierozpoznanych wystąpień w DG mają status udokumentowanego niepełnego importu, nie rozwiązanych odsyłaczy. Nie zmieniano CAL, DG ani konfiguracji CI. Dla bieżącego commitu widoczne przebiegi terminologii i PDE chapter 13 oczekują (45721555509, 45721555506); nie ma potwierdzenia dedykowanego CI 14. Brak nowej pełnej kompilacji PDF i kontroli backendu rysunków.

Następna iteracja 232: trzecia lektura 021–032 (Poisson, Harnack, Liouville, gradient i pochodne wyższych rzędów), ponowny odczyt CI.
