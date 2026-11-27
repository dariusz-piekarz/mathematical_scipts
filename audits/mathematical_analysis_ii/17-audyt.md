# AM II 17 — Ekstrema swobodne i wypukłość

Data: 27.11.2026. Gałąź: biblioteka-matematyczna-iteracja-6.

## Historia
- 2153a27 — ekstrema swobodne, warunki drugiego rzędu, przypadki zdegenerowane i rysunek.
- 479dea4 — włączenie do książki; 3605218 — rejestracja rozdziałów 16 i 17 w katalogu.
- 432f4b4 — kryteria wyższych rzędów, wypukłość i silna wypukłość, istnienie minimum.
- fa3d081 — 18 poprawek pierwszego audytu, m.in. polaryzacja, zwartość sfery, rachunki macierzy Hessego.
- 9249928 — 11 poprawek drugiego audytu, w tym jawna hipoteza wypukłości w kryterium stacjonarności, dowody silnej wypukłości i ciągu minimalizującego.

## Stabilizacja
Dwa kolejne pełne odczyty bez zmian źródła, blob 3fb8f2f0acd472c9b8a50e85413e93cf607a50be, 810 wierszy. Sprawdzono warunki punktowe, przypadek przestrzeni zerowej, formy kwadratowe, przykład w przestrzeni Hilberta, test w dwóch zmiennych, wielomiany jednorodne, polaryzację, kontrprzykład testowania prostych, kryteria wypukłości i silnej wypukłości, dowód istnienia minimum z zupełności oraz przykład równania operatorowego. Nie stwierdzono nowych usterek wymagających zmian.

Kontrola strukturalna: 22 etykiety, brak duplikatów w badanych rozdziałach 01, 15–17; 16/16 różnych odsyłaczy wewnętrznych i 7/7 zewnętrznych (AM1-25, FA-15, FA-16), cele potwierdzone w źródłach. Stos środowisk LaTeX poprawny. Rozdział występuje dokładnie raz w książce i katalogu. Stabilizacja merytoryczna 2/2.

## Odbiór techniczny
Kompilacja wcześniejszego źródła 432f4b4: AM II 46032622123 success. Dla ostatniej zmiany 9249928: AM II 46033711857, AM I 46033711863, terminologia 46033698795, aplikacja 46033698844 — queued przy ostatnim odczycie. Nie przeprowadzono kontroli wizualnej aktualnego PDF ani lokalnego testu globalnych listingów. Odbiór techniczny pozostaje otwarty. Następny etap: odbiór aktualnego PDF i CI, następnie AM II 18 — twierdzenie o funkcji odwrotnej.


## Odbiór kompilacji i PDF — 27.11.2026

Przebieg AM II 46033698790 dla 924992808bbeefecab8b2ff9ca9787c46af03b7a zakończony sukcesem; terminologia 46033698795 również success. Pobrano artefakt 15215468215, rozpakowano rzeczywisty PDF (151 stron, 1287133 bajty). Rozdział 17: strony fizyczne 136–144, drukowane 132–140. Wyrenderowano i obejrzano wszystkie dziewięć stron, w tym rysunek powierzchni. Brak widocznych obcięć i kolizji, brak ciągów ?? w ekstrakcji i bloków tekstu poza stroną; 31 adnotacji odsyłaczy. Nie sprawdzano indywidualnie klikalności w aplikacji ani pozostałych rozdziałów wizualnie. Aktualne bloby rozdziału (3fb8f2f0acd472c9b8a50e85413e93cf607a50be) i książki (67213ffad448fc28fa1b23bce086887225ec3805) identyczne z testowanym snapshotem. Pozostałe przebiegi AM II 46033711857, AM I 46033711863 i aplikacja 46033698844 nadal queued przy ostatnim odczycie.

Stabilizacja merytoryczna 2/2 oraz odbiór kompilacji i składu rozdziału 17 zaliczone. Pełny odbiór integracyjny aplikacji nadal otwarty.

## Przygotowanie rozdziału 18

Sprawdzono rzeczywiste deklaracje i dowody FA-15: thm:inverse15 (twierdzenie o funkcji odwrotnej), cor:inverse-ck15 (regularność), prop:inverse-operator15 i thm:inverse-derivatives15 (odwracanie operatorów), ex:inverse-hilbert15 (przykład lokalny, nieglobalny), rem:limits-inverse15 (rola zupełności i pochodnej Frécheta). AM II 07 zawiera ma2:thm:neumann, ma2:thm:inverse-perturbation, ma2:cor:inverse-linear. W nowym rozdziale wykorzystać te wyniki z pełnymi hipotezami i odsyłaczami, nie powielać dowodów; rozwinąć zastosowania i kryterium w skończonym wymiarze zgodnie z planem. W tej iteracji nie utworzono jeszcze rozdziału 18.
