# AM II 28 — audyt kontrolny

Data: 2026-11-28. Źródło niezmienione od commitu 26cf2005c1ee73b33689dc6264817e5e397bfa83, blob ee1a42454dddb5e0846eb454e3af9fc709c2cc51, 625 wierszy. Poprzedni raport: 28-audyt-stabilizacyjny-2026-11-28.md.

## Kontrola
- Lokalna dominacja, ciągłość i zgodność całek na zwartych zbiorach Jordana: założenia i wnioski zgodne z ME 11 i AM II 26.
- Wielowymiarowe różniczkowanie: przekroje mierzalne, wspólny zbiór zerowy, lokalne majoranty wszystkich pochodnych, redukcja do prostych, indukcja i twierdzenie Schwarza; poprawne. Całkowalność w jednym punkcie każdej składowej wynika z lokalnego oszacowania przyrostu.
- Wzory gradientu i Hessianu: skończona suma całek skalarnych; rachunki radialne i logarytmiczne poprawne.
- Dwa kontrprzykłady: gładkość w otwartej dziedzinie, wartość całki |t|, brak różniczkowalności; brak dominacji w przykładzie ucieczki do nieskończoności wynika z rozbieżności szeregu harmonicznego po rozłącznych kulach. Rysunek schematyczny zgodny z opisem; wygląd PDF niezweryfikowany.
- Ruchoma kula: zerowość sfery, wspólne ograniczenie na zbiorze zwartym, translacja, moment drugiego rzędu i pochodne poprawne.
- Leibniz i kontrola ogonów: orientacja, lokalne ograniczenia, warunki ciągłości i wzór radialny poprawne.

## Statyka i technika
26 odsyłaczy wewnętrznych (AM II 13, 15, 26, 27, 28), 11 zewnętrznych (AM I 32, ME 04 i 11): wszystkie cele istnieją. 16 etykiet rozdziału, bez duplikatów w pięciu sprawdzonych rozdziałach AM II. Bilans klamer i środowisk poprawny. Katalog i entrypoint: 27, 28, 36 w prawidłowej kolejności. Próba jednorazowej kontroli etykiet całego tomu przekroczyła limit wywołań; nie stwierdza się globalnej unikatowości na tej podstawie.
CI źródła 26cf200: terminologia #46131014577 success, walidacja AM II #46131014567 pending, dodatkowa walidacja #46131021164 skipped, aplikacja #46131014534 cancelled. Nie uruchomiono dodatkowego CI. Aktualny PDF niezweryfikowany.

Wynik: zero nowych uwag matematycznych i redakcyjnych, źródło bez zmian. Odbiór techniczny pozostaje otwarty.

## Przygotowanie AM II 29
Sprawdzono rzeczywiste tezy AM I 33: ma1:def:curve-length, ma1:thm:curve-length, ma1:cor:arc-reparametrization, ma1:cor:polar-length. Nie powielać dowodu wzoru długości dla C^1. DG 11 obejmuje ogólną geometrię riemannowską, której nie przenosimy do AM II. ME 28: def:multiplicity-28, thm:immersion-area-28, thm:lipschitz-area-coarea-28 — podstawa związku długości z H^1 oraz krotnością. Rozwinąć długość jako wahanie, addytywność, prostowalność, parametryzację długością łuku, przypadek krzywych absolutnie ciągłych (po sprawdzeniu AM I 37), rozróżnienie długości drogi od H^1 obrazu, przykłady i kontrprzykłady. Nie wprowadzano jeszcze rozdziału 29.
