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
| **18** | **Przestrzenie odwzorowań, topologia zwarto-otwarta, zbieżność jednostajna na zbiorach zwartych, ewaluacja, prawo wykładnicze, metryzacja i zupełność** | **stabilny — audyt 03; pełne dowody i walidacja CI/PDF** |
| **19** | **Przestrzenie polskie, podprzestrzenie G-delta, zbiory borelowskie i hierarchia indeksowana przeliczalnymi liczbami porządkowymi** | **stabilny — audyt 03; CI/PDF PASS; 590 unikatowych etykiet i 138 poprawnych odsyłaczy w książce** |
| **20** | **Zbiory analityczne, rzuty zbiorów domkniętych, operacja Suslina, zbiór analityczny nieborelowski; bez powielania determinacji i redukcji Wadge’a z logiki** | **utworzony; audyt 01 i walidacja CI/PDF w toku** |

Zakresy 12–13 oraz 16–17 są rozdzielone według tematyki, żeby unikać powtarzania dowodów. Zgodnie z zasadą projektu nowe rozdziały nie oznaczają automatycznie ich stabilności.

## Procedura

Dla każdego nowego rozdziału: (1) przygotowanie samodzielnego tekstu z motywacją, przykładami i dowodami bez nieuzasadnionych przeskoków; (2) matematyczny i redakcyjny audyt, także terminologii i odsyłaczy; (3) kontrola rysunków i układu; (4) testy źródeł i kompilacja samodzielnego PDF oraz całej książki; (5) powtarzanie kontroli do uzyskania stabilnej wersji, następnie dopiero przejście dalej. Każda iteracja dokumentuje status poszczególnych rozdziałów. Nie dopisujemy twierdzeń do audytowanych rozdziałów bez szczególnego uzasadnienia.

## Konwencje terminologiczne

- Używamy **uzwarcenie**, nie **zwartościowanie** (również: uzwarcenie Aleksandrowa i uzwarcenie Čecha–Stone’a).
- Używamy **topologia zbieżności jednostajnej na zbiorach zwartych**, nie skrótu „topologia zbieżności zwartej”.
- Przestrzeń **spełnia pierwszy/drugi aksjomat przeliczalności**, nie jest „pierwszo-/drugoprzeliczalna”.
- Angielskie *chart* tłumaczymy jako **mapa**, *sequence* jako **ciąg**; *net* jako **sieć**.
- Wymagamy precyzyjnie sformułowanych twierdzeń i uzasadnionych nietrywialnych przejść (w tym wskazania właściwego wcześniejszego wyniku, jeśli jest użyty).

## Zamknięcie rozdziału 19 (2026-11-22)

Niezależny [audyt 03](../../audits/general_topology/19-przestrzenie-polskie-iteracja-03.md) potwierdził poprawność uzupełnionych dowodów dotyczących podprzestrzeni typu G-delta, przykładów polskich przestrzeni, śladu sigma-algebry borelowskiej oraz skończonej i pozaskończonej hierarchii borelowskiej. Źródło: blob `dd05dd723a4e92756d1e339309079c68a4580485` — bez zmian podczas audytu 03. [GitHub Actions 45019373792](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45019373792) completed/success na tym samym blobie, a w audycie 02 wizualnie sprawdzono 6 stron PDF. Przejście do rozdziału **20** nie wymaga dalszych poprawek rozdziału 19, o ile jego źródło pozostaje niezmienione.


## Rozdział 20 — decyzja po kontroli powtórzeń

Porównano źródła skryptu \`Logika matematyczna i teoria mnogości\`,
zwłaszcza rozdział 30 \`30-gry-nieskonczone-i-aksjomat-determinacji.tex\`,
z rozdziałem 19 topologii i planem rozdziału 20.
W rozdziale 30 logiki występują definicja zbioru analitycznego,
wprowadzenie do klas projektywnych, aksjomatu determinacji,
własności regularności oraz redukcji Wadge’a.
Pełne dowody równoważności reprezentacji analitycznej,
operacji Suslina i konstrukcji nieborelowskiego zbioru
analitycznego **nie** stanowią tam osobnego wykładu.
Wprost przywołano jako zewnętrzny wynik
uniwersalną mierzalność zbiorów analitycznych.

Aby nie powielać materiału, rozdział 20 topologii obejmuje
tylko brakujące podstawy topologiczne z dowodami:
ciągłe obrazy przestrzeni Baire’a, rzuty zbiorów domkniętych,
przeliczalne działania na zbiorach analitycznych, operację Suslina
i zbiór analityczny nieborelowski przez uniwersalny rzut.
Nie zawiera dowodów determinacji, teorii gier, redukcji Wadge’a
ani twierdzeń o regularności z rozdziału 30 logiki.
Teoremat o uniwersalnej mierzalności **nie** został tu wykazany
i nie jest deklarowany jako pokryty.

Źródło: \`chapters/pl/general_topology/20-zbiory-analityczne-i-operacja-suslina.tex\`.
Testy: \`tools/tests/test_general_topology_ch20.py\`;
punkt wejścia \`books/pl/general_topology_ch20.tex\`.
Do czasu zakończenia audytów i zielonego CI
**nie** oznaczać rozdziału 20 jako stabilnego.
