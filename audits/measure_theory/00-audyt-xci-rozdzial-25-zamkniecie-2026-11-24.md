# Audyt XCI (91) — rozdział 25: zamknięcie stabilizacji

Data: 2026-11-24. Gałąź: biblioteka-matematyczna-iteracja-6.

## Wersja i testy
Aktualny blob d74356d24685f8e5d6f3395e83c72a96b65da921 zgodny z wersją źródłową z przebiegu https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45299484681 (commit f8b77ef7dabadce80a84f81923e2138589605cc9). Wszystkie trzy zadania CI zakończone success.
Logi jobów 138128746064 i 138128745663: 7 testów rozdziału oraz 4 testy integralności tomu zaliczone; 21 etykiet lokalnych i 8 wymaganych etykiet zewnętrznych, wszystkie odsyłacze rozwiązane. Pełny tom: 266 stron, 1939421 bajtów. Samodzielny rozdział: 8 stron, 284318 bajtów.

## Rzeczywista kontrola artefaktów
Pobrano ZIP 14877363728 (4129241 bajtów). Niezależnie obliczony SHA256: 1e2f159e24f28639326ea3ef5caab0b418e59caad3e43a033e6fe957ee4ca006, zgodny z metadanymi. Rozpakowano oba PDF, oba logi i osiem obrazów CI. Wszystkie osiem stron samodzielnego rozdziału niezależnie wyrenderowano przez PyMuPDF (skala 1,6) i obejrzano.
- Strony 1–2: punkty Lebesgue'a, nierówność maksymalna, początek dowodu różniczkowania; wzory i odsyłacze czytelne.
- Strony 3–4: gęstość, kontrprzykład funkcji signum, zanik gęstości miary osobliwej i różniczkowanie względem Lebesgue'a; brak uciętych wzorów.
- Strony 5–6: dystrybuanta, kostki, względna nierówność maksymalna; poprawne rozmieszczenie wzorów.
- Strony 7–8: różniczkowanie względem Radona, miary ze znakiem i zespolone, przykład braku jednostajnej kontroli mas powiększonych kul; poprawny skład.
Odczyt tekstu: 0 wystąpień ?? na wszystkich ośmiu stronach. Log samodzielnego rozdziału: 0 Overfull, 0 Underfull, 0 ostrzeżeń o nierozwiązanych odsyłaczach. Log pełnego tomu: 0 Overfull, 14 Underfull, 0 ostrzeżeń o nierozwiązanych odsyłaczach. Nie oglądano wszystkich 266 stron tomu.

## Werdykt matematyczny
W połączeniu z niezależnymi przeglądami LXXXVIII–XC potwierdzono zachowanie nowych dowodów dotyczących mierzalności, dodatniości mianownika na nośniku, różniczkowania części osobliwej oraz miar ze znakiem i zespolonych. Przykład niepodwajającej miary jest zgodny z obliczonymi masami kul. W tej iteracji bez zmian źródła; nie stwierdzono nowych usterek wymagających modyfikacji. Skończone regresje nie zastępują dowodów ogólnych.

## Stan
Rozdział 25 ustabilizowany w zakresie wykonanych audytów, regresji i składu. Stan 25/31. Następny audyt XCII: pierwszy szczegółowy przegląd rozdziału 26.
