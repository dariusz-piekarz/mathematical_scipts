# Topologia ogólna — plan rozdziałów i audytów

Stan: 22 listopada 2026. Źródłem prawdy dla rozdziałów włączonych do książki jest `catalog/books.json`, a dla wyników kompilacji i testów: GitHub Actions na gałęzi `biblioteka-matematyczna-iteracja-6`.

## Zakres i kolejność

| Nr | Zakres | Stan |
| --- | --- | --- |
| 01 | Przestrzenie topologiczne | po audytach |
| 02 | Operacje topologiczne na zbiorach | po audytach |
| 03 | Odwzorowania ciągłe | po audytach |
| 04 | Konstrukcje przestrzeni topologicznych | po audytach |
| 05 | Aksjomaty oddzielania | po audytach |
| 06 | Zbieżność topologiczna, sieci i filtry | po audytach |
| 07 | Zwartość, twierdzenie Tychonoffa, zanurzanie w kostkę | po audytach |
| 08 | Spójność i spójność łukowa | po audytach |
| 09 | Aksjomaty przeliczalności i własność Lindelöfa | po audytach |
| 10 | Metryzowalność i twierdzenie Urysohna | po audytach |
| **11** | **Zupełność, kategoria i twierdzenie Baire'a (wersja metryczna)** | **stabilny — audyt 6** |
| **12** | **Przestrzenie jednostajne, jednostajna ciągłość, ciągi, sieci i filtry Cauchy'ego** | **stabilny — audyt 3** |
| **13** | **Zupełność jednostajna i uzupełnienia metryczne/jednostajne** | **stabilny — audyt 05** |
| **14** | **Zwartość lokalna, twierdzenie Baire'a, podprzestrzenie, iloczyny, przeliczalność w nieskończoności i wyczerpania zwarte** | **stabilny — audyt 03** |
| **15** | **Parazwartość, lokalnie skończone pokrycia i podziały jedności; związki z metryzowalnością** | **stabilny — audyt 06; twierdzenia Stone’a i Nagaty–Smirnowa z pełnymi dowodami** |
| **16** | **Topologia wyznaczona przez funkcje, przestrzenie całkowicie regularne, uzwarcenia i ich równoważność** | **stabilny — audyt 03** |
| **17** | **Uzwarcenie Aleksandrowa i uzwarcenie Čecha–Stone’a: konstrukcje, własności uniwersalne, minimalność, maksymalność i przykłady** | **stabilny — audyt 03; pełne dowody konstrukcji i własności uniwersalnych** |
| **18** | **Przestrzenie odwzorowań, topologia zwarto-otwarta, zbieżność jednostajna na zbiorach zwartych, ewaluacja, prawo wykładnicze, metryzacja i zupełność** | **rozdział napisany — audyt 01** |
| 19 | Przestrzenie polskie i hierarchia zbiorów borelowskich | plan |
| 20 | Podstawy opisowej teorii mnogości i jej związki z topologią | plan |

Zakresy 12–13 oraz 16–17 są rozdzielone według tematyki, żeby unikać powtarzania dowodów. Zgodnie z zasadą projektu nowe rozdziały nie oznaczają automatycznie ich stabilności.

## Procedura

Dla każdego nowego rozdziału: (1) przygotowanie samodzielnego tekstu z motywacją, przykładami i dowodami bez nieuzasadnionych przeskoków; (2) matematyczny i redakcyjny audyt, także terminologii i odsyłaczy; (3) kontrola rysunków i układu; (4) testy źródeł i kompilacja samodzielnego PDF oraz całej książki; (5) powtarzanie kontroli do uzyskania stabilnej wersji, następnie dopiero przejście dalej. Każda iteracja dokumentuje status poszczególnych rozdziałów. Nie dopisujemy twierdzeń do audytowanych rozdziałów bez szczególnego uzasadnienia.

## Konwencje terminologiczne

- Używamy **uzwarcenie**, nie **zwartościowanie** (również: uzwarcenie Aleksandrowa i uzwarcenie Čecha–Stone’a).
- Używamy **topologia zbieżności jednostajnej na zbiorach zwartych**, nie skrótu „topologia zbieżności zwartej”.
- Przestrzeń **spełnia pierwszy/drugi aksjomat przeliczalności**, nie jest „pierwszo-/drugoprzeliczalna”.
- Angielskie *chart* tłumaczymy jako **mapa**, *sequence* jako **ciąg**; *net* jako **sieć**.
- Wymagamy precyzyjnie sformułowanych twierdzeń i uzasadnionych nietrywialnych przejść (w tym wskazania właściwego wcześniejszego wyniku, jeśli jest użyty).
