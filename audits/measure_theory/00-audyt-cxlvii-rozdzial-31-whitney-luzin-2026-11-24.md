# Audyt CXLVII (147) — mierzalność i Whitney–Luzin
Data 2026-11-24. Gałąź biblioteka-matematyczna-iteracja-6.

## Korekty
Commit 97d8b808ac747fe06af20124f0f1e9d4cdd49b3c; blob 99c8ad64ce568d89f37dbf935f7d8a6303c6682d; 1337 → 1470 wierszy; 30 etykiet bez zmian.
- Mierzalność różniczki przybliżonej: borelowski przedstawiciel dla argumentu przesuniętego, zachowanie wartości w punkcie bazowym, mierzalność całek przez niezależne parametry, ilościowe oszacowanie obciętej średniej, symetrie momentu kątowego, konstrukcja mierzalnego G oraz przeliczalna charakterystyka dokładnego zbioru D.
- Whitney–Luzin: jednoczesne zastosowanie Luzina do danych wektorowych, przypadek pustego K, kontrola utraty miary w wyborze Jegorowa, jawne oszacowanie przecięcia kul i tożsamość reszt, kwantyfikatory jednostajnej zgodności, przedłużanie wszystkich składowych na tym samym K.
- Odwrotność: przeliczalne pokrycie z dokładnością do zbioru zerowego i twierdzenie o gęstości.
- Wniosek Lipschitzowski: wybór K w zbiorze zwykłej różniczkowalności, aby DF=Df zachodziło w każdym punkcie K, nie tylko prawie wszędzie.
- Wyższe rzędy: jawny mierzalny pełnomiarowy zbiór D z rozwinięciami w każdym jego punkcie, przeliczalne suprema, obcięcie ewentualnie nieskończonych funkcji przed zastosowaniem Jegorowa, regularność miary i kontrola jednostajna bez obcięcia.

## Regresje i CI
MT31-009–011: commit 508d787a7a513f5c5f854cce5d03662ec6d8b500; 11 trwałych testów. Niezależne kontrole JS: 204 momentów kątowych w modelu skończonym, 6561 tożsamości reszt, 20 nierówności objętości, 9 warunków źródłowych; zaliczone. Testów Python lokalnie nie uruchomiono. Poprzednie CI: [{"context":"measure-theory/ch31-regressions","state":"success","target_url":"https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45379130118"},{"context":"measure-theory/ch31-pdf","state":"success","target_url":"https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45379130118"}]. Aktualne CI: []. Bez oględzin PDF w tej iteracji.

## Następny krok
Kontrola przekrojowa pozostałych sekcji: regularność i holonomiczność, symbole główne, Sobolew i BV, wzory pola i koobszaru, terminologia oraz precyzja odsyłaczy do rozdziałów 25, 28–30. Diagnostyka CI i PDF. Rozdział pozostaje otwarty; 30/31. Bez rozszerzania zakresu.
