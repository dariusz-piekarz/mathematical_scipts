# Audyt 19 nierozstrzygniętych odsyłaczy po wdrożeniu rejestru etykiet

**Data:** 20 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Źródło:** artefakt GitHub Actions `reference-provenance-audit` z udanego przebiegu `44743646693`, generowany na podstawie 355 rozdziałów. To **nowszy indeks** niż pierwotna migawka z 257 przypadkami.

## Bilans

Początkowo: **257** nierozstrzygniętych odsyłaczy, w tym 166 niejednoznacznych. Po wdrożeniu kontekstowego indeksowania: **19** wpisów `missing`, **0** `ambiguous`, **72** `external_resolved`.

Po sprawdzeniu wszystkich 19 z oryginalnymi rozdziałami:

- **1** — `cross_script_unverified`.
- **3** — `mathematical_target_mismatch`.
- **12** — `not_in_imported_scope`.
- **1** — `possible_local_reference_mismatch`.
- **2** — `shared_input_confirmed`.

Zatem jedynie **2/19** mają jednoznacznie potwierdzone istniejące deklaracje `\label` w dołączanych plikach wspólnych; pozostałe wymagają weryfikacji importu lub osobnej korekty matematycznej. Nie należy oznaczać ich automatycznie jako rozwiązanych.

## Pełna tabela 19 przypadków

| Nr | Wystąpienie | Etykieta | Diagnoza | Uzasadnienie / dalsze działanie |
|---:|---|---|---|---|
| 1 | `ALG-10:240` | `tw:ga10-weak` | `shared_input_confirmed` | Plik shared/pl/slabe_twierdzenie_lefschetza.tex zawiera dokładnie \label{tw:ga10-weak}; ALG-10:219 wykonuje \input. |
| 2 | `ALG-10:385` | `thm:xvii-blowup` | `shared_input_confirmed` | Plik shared/pl/rozdmuchanie_punktu_kohomologia.tex zawiera dokładnie \label{thm:xvii-blowup}; ALG-10:359 wykonuje \input. |
| 3 | `DG-05:730` | `app:grupy-algebry-macierzowe` | `not_in_imported_scope` | Dodatek o grupach macierzowych nie figuruje w aktualnie zaindeksowanej części DG. Wymaga sprawdzenia pełnego skryptu i dodatków. |
| 4 | `DG-11:693` | `prz:thur-dop-nil-kontakt` | `possible_local_reference_mismatch` | DG-11 zawiera przykład o metrykach Nil/Sol pod etykietą prz:thur-dop-metryki-nil-sol; brak osobnego prz:thur-dop-nil-kontakt. Nie zakładać automatycznej równoważności przykładów. |
| 5 | `DG-11:1452` | `sec:rownanie-diraca` | `not_in_imported_scope` | Zapowiedziana sekcja o równaniu Diraca; wymaga weryfikacji dalszych rozdziałów DG. |
| 6 | `DG-12:1271` | `subsec:dirac-koneksja` | `not_in_imported_scope` | Zapowiedziana podsekcja o koneksji spinorowej; wymaga weryfikacji dalszych rozdziałów DG. |
| 7 | `DG-14:2232` | `sec:algebra-liego` | `not_in_imported_scope` | Definicja algebry Liego przywoływana przy holonomii; brak etykiety w obecnym indeksie DG. |
| 8 | `DG-14:2537` | `cor:bochner-vanishing` | `not_in_imported_scope` | Wniosek Bochnera o harmonicznych 1-formach; wymaga importu bądź wskazania kanonicznego twierdzenia. |
| 9 | `DG-14:2541` | `cor:hodge-de-rham` | `not_in_imported_scope` | Wniosek Hodge’a–de Rhama; wymaga importu bądź wskazania kanonicznego twierdzenia. |
| 10 | `DG-14:4619` | `ch:chern-weil` | `not_in_imported_scope` | Rozdział o teorii Cherna–Weila; jego brak w obecnych 20 rozdziałach nie świadczy o braku w skrypcie 36-rozdziałowym. |
| 11 | `DG-14:4622` | `prop:euler-identification-26` | `not_in_imported_scope` | Stwierdzenie identyfikujące klasę Eulera, oznaczenie -26 sugeruje późniejszy rozdział. |
| 12 | `DG-14:4624` | `lem:angular-form-26` | `not_in_imported_scope` | Lemat o formie kątowej i normalizacji, oznaczenie -26 sugeruje późniejszy rozdział. |
| 13 | `DG-14:4704` | `thm:CGB-boundary-26` | `not_in_imported_scope` | Rzeczywiste odniesienie do formuły Gaussa–Bonneta z poprawką brzegową; zapowiedziane twierdzenie -26. |
| 14 | `DG-16:1200` | `thm:CGB-boundary-26` | `mathematical_target_mismatch` | Niezerowość e(TS²) dla S² bez brzegu. Bezpośrednim celem jest twierdzenie dla rozmaitości zamkniętych lub klasa Eulera, nie wersja z brzegiem -26. |
| 15 | `DG-16:1879` | `ch:grafy-wezly-cztery` | `cross_script_unverified` | Odsyłacz do rozdziału o grafach i węzłach z przykładem chirurgii. Wymaga jawnej mapy zależności między skryptami, bez automatycznego wybierania celu. |
| 16 | `DG-17:733` | `prz:hodge-dwie-sfery-18` | `not_in_imported_scope` | Przykład obliczenia okresów na S²×S² oznaczony -18; należy sprawdzić rozdział 18 pełnej geometrii różniczkowej. |
| 17 | `DG-17:1840` | `ch:chern-weil` | `not_in_imported_scope` | Ponowne odwołanie do przyszłego rozdziału Cherna–Weila. |
| 18 | `DG-17:1888` | `thm:CGB-boundary-26` | `mathematical_target_mismatch` | e(TS²)=2 na zamkniętej S²; naturalny cel to wersja Gaussa–Bonneta dla rozmaitości zamkniętych, nie -26 z brzegiem. |
| 19 | `DG-17:2182` | `thm:CGB-boundary-26` | `mathematical_target_mismatch` | Samoprzecięcie przekątnej w S²×S² wymaga e(TS²)=2. Twierdzenie dla rozmaitości zamkniętych jest wystarczające i bliższe kontekstowi. |

## Wniosek z analizy `ALG-10`

Dwa cytowania są fałszywie zgłaszane jako `missing` przez **nieindeksowanie podłączanych plików `shared/pl/`**:
- `ALG-10:219` używa `\input{../../shared/pl/slabe_twierdzenie_lefschetza.tex}`, a plik zawiera `\label{tw:ga10-weak}`.
- `ALG-10:359` używa `\input{../../shared/pl/rozdmuchanie_punktu_kohomologia.tex}`, a plik zawiera `\label{thm:xvii-blowup}`.

Oba pliki zawierają również dodatkowe historyczne etykiety w tych samych twierdzeniach. Ich warunkowe zabezpieczenie przed wielokrotnym włączeniem (`\ifcsname`) oznacza, że parser powinien zachować **informację o źródłowym pliku** oraz kontekście importu; nie wystarczy bezmyślnie dopisać etykiety do najbliższego rozdziału. Proponuję osobny mechanizm `include provenance` i test importu plików `shared`.

## Uwaga matematyczna o `thm:CGB-boundary-26`

W `DG-14:4704` odwołanie do twierdzenia Gaussa–Bonneta **z brzegiem** jest merytorycznie uzasadnione, ponieważ tekst zawiera formułę z członem brzegowym. Natomiast `DG-16:1200`, `DG-17:1888` oraz `DG-17:2182` wykorzystują fakt `e(TS²)[S²]=χ(S²)=2` dla **sfery bez brzegu**. W odpowiednich miejscach istnieje już kanoniczny wynik `DG-14:4604`, `\label{thm:chern-gauss-bonnet}`. Przy przyszłej korekcie źródeł warto zastąpić wskazane trzy cytowania odpowiednim twierdzeniem o przypadku zamkniętym, z ewentualnym odsyłaczem do klasy Eulera. Nie przepisano automatycznie oryginalnych `\ref`.

## Zależności i materiał jeszcze niezaimportowany

Pełna geometria różniczkowa ma **36 rozdziałów**, lecz gałąź obejmuje pierwszych **20**. Oznaczenia `-26`, tytuł „Cherna–Weila”, Hodge, Bochner i Dirac są silnymi przesłankami istnienia późniejszych celów, ale **bez wczytania pozostałych 16 rozdziałów nie przypisuję konkretnych właścicieli i nie twierdzę, że każda deklaracja na pewno istnieje**. Dotyczy to także źródeł w dodatkach. Identyfikatory `ch:grafy-wezly-cztery` i `app:grupy-algebry-macierzowe` wymagają osobnego sprawdzenia w odpowiednich skryptach bądź dodatkach.

## Stan realizacji i dalsze kroki

1. Audyt semantyczny **19/19 wykonany**, z zachowaniem oryginalnych etykiet.
2. Dwa cele `ALG-10` wymagają wsparcia indeksowania transkrypcji `\input` / `shared/pl`, z ochroną warunkowych importów.
3. Trzy cytowania do `thm:CGB-boundary-26` wymagają matematycznego zastąpienia przy przyszłym audycie kanonicznych rozdziałów; nie zmieniać bez uzasadnienia.
4. Brakujące rozdziały DG należy zweryfikować dopiero po ich imporcie i zbudowaniu nowego indeksu.
5. Oddzielny rzeczywisty test LaTeX czterech tomów z `.aux` i `xr-hyper` jest uruchamiany przez workflow `.github/workflows/probability-xr-hyper.yml`. Raport tego przebiegu nie jest częścią statycznego audytu i wymaga osobnego statusu.
6. Bez zmian źródłowych `chapters/pl/`, oryginalnych `\label`, `\ref`, `\eqref`, bez scalania i bez zmian `main`.

**Uwaga:** „19/19 zbadanych” nie oznacza „19/19 naprawionych w aplikacji”. Wszystkie 19 nadal znajdują się w wyjściowym indeksie; dwa mają potwierdzone zewnętrzne źródło, pozostałe nie mają jeszcze przypisanego poprawnego celu technicznego.