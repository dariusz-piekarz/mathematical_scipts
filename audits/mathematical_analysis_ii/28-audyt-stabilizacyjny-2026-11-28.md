# AM II 28 — audyt stabilizacyjny bez nowych uwag

Data: 2026-11-28. Sprawdzone źródło: commit 26cf2005c1ee73b33689dc6264817e5e397bfa83, blob ee1a42454dddb5e0846eb454e3af9fc709c2cc51 (625 wierszy).

## Kontrola matematyczna i redakcyjna

- Ciągłość: lokalna dominacja i mierzalność przekrojów, ciągłość w normie L1; w przypadku zwartego zbioru Jordana ograniczenie na iloczynie zbiorów zwartych oraz zgodność całek — poprawne.
- Różniczkowanie: wspólny zbiór zerowy, mierzalność pochodnych przez ilorazy różnicowe, lokalne majoranty na kuli, stosowanie twierdzenia jednowymiarowego do prostych współrzędnościowych, indukcja i przemienność pochodnych mieszanych — poprawne.
- Całkowalność w jednym punkcie składowej: oszacowanie przyrostu na odcinku w kuli, otwartość zbioru parametrów o całkowalnych przekrojach i jego dopełnienia, spójność — poprawne.
- Gradient, różniczka i Hessian: skończona suma całek skalarnych, zgodność z AM II 13 i 15 — poprawne.
- Przykłady radialne: czynniki n v_n, silnia, potęgi parametru, momenty logarytmiczne, lokalna całkowalność majorant dla p<n — poprawne.
- Kontrprzykład uciekającego nośnika: gładkość w otoczeniu każdego (0,x), całka |t|, brak majoranty pochodnej; rozłączne kule i rozbieżny szereg harmoniczny dowodzą braku wspólnej majoranty samej funkcji. Rysunek jest jawnie schematyczny, zgodny z położeniem nośników i proporcjami wysokości. Brak kontroli wizualnej PDF.
- Koncentracja przy brzegu (0,1): gładkość na otwartej dziedzinie, stała majoranta, podstawienie i całka |t| — poprawne.
- Ruchoma kula: zbieżność funkcji charakterystycznych poza sferą zerowej miary, wspólne ograniczenie na zwartej kuli; translacja i różniczkowanie środka; moment drugiego rzędu i Hessian — poprawne.
- Reguła Leibniza: ograniczenie do prostej współrzędnościowej, orientacja przedziałów, zbieżność zmajoryzowana przy ruchomych końcach, przypadek radialny — poprawne.
- Kontrola ogonów: wyczerpanie zbiorami mierzalnymi skończonej miary, całkowalność na obcięciach, relacja z lokalną majorantą — poprawne.

## Statyka

26 odsyłaczy wewnętrznych (cele w 13, 15, 26, 27, 28), 11 kwalifikowanych (AM I 32, ME 04 i 11): wszystkie cele istnieją. 16 etykiet rozdziału, bez duplikatów w kontrolowanych pięciu rozdziałach AM II. Zagnieżdżenie środowisk i bilans nawiasów klamrowych poprawne. Katalog oraz entrypoint zawierają 28 w kolejności po 27 i przed 36; preambuła zawiera TikZ i środowisko stwierdzenie.

## Odbiór techniczny

Dla commitu 26cf200: Polish mathematical terminology #46131014577 success; Mathematical library application checks #46131014534 cancelled; Mathematical analysis II validation #46131014567 pending, dodatkowy przebieg #46131021164 skipped. Nie potwierdzono kompilacji aktualnego PDF ani pełnego CI. Nie uruchamiano dodatkowego workflow.

Wynik: zero nowych uwag w bieżącym audycie merytorycznym i statycznym. Źródło rozdziału pozostawiono bez zmian. Następny etap: niezależny audyt kontrolny, odbiór techniczny i rozdział 29 (krzywe, długość i prostowalność).
