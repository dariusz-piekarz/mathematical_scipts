# Topologia ogólna — rozdział 07 — audyt 1

**Data:** 21 listopada 2026 r.
**Tytuł:** Zwartość i jej charakterystyki.
**Wersja:** 0.1, audyt 1 zakończony z poprawkami, **0/2 kolejnych czystych audytów**.
**SHA256 źródła:** `e104ccfa7519174c4c8f93d82240da830bb0f5cec8ada2d93199d55a6295565d`.

## Pokrycie materiału

- Zwartość przez pokrycia otwarte i skończone podpokrycia, z uwzględnieniem przestrzeni pustej i topologii podprzestrzeni.
- Zwartość przedziału domkniętego z dowodem przez supremum; przykłady niezwartości.
- Własność skończonych przecięć dla niepustych rodzin zbiorów domkniętych, trwałość zwartości, zwartość i normalność w przestrzeniach Hausdorffa, kryterium homeomorfizmu.
- Charakteryzacja przez punkty skupienia sieci, zbieżne podsieci, filtry i ultrafiltry (z pełnym dowodem lematu Zorna).
- Twierdzenie Tychonoffa o zwartości dowolnego iloczynu; jawne wskazanie użycia aksjomatu wyboru.
- Twierdzenie Heinego--Borela w R^n.
- Zatwierdzone do części o zwartości twierdzenie o zanurzaniu przestrzeni Tychonoffa w kostkę [0,1]^I i konstrukcja kostkowego uzwarcenia.

## Poprawki pierwszego audytu

1. W początkowej wersji rysunku Heinego--Borela układ współrzędnych był zbyt schematyczny. Przebudowano ilustrację na dwie jasno podpisane części, bez sugerowania niepoprawnego położenia początku układu.
2. W dowodzie zwartości przez sieci poprawiono konstrukcję przeciwną: zbiór indeksów to pary (J,x), zatem nie wymaga niejawnego globalnego wyboru punktu z każdej reszty pokrycia. W dowodzie w drugą stronę zastąpiono wybór otoczeń dla wszystkich punktów jedną rodziną wszystkich otwartych zbiorów o właściwości omijania przez ogon.
3. W dowodzie Heinego--Borela wpisano jawne nierówności porównujące metrykę maksimum i metrykę euklidesową, zamiast pozostawiać tylko aluzję.
4. Usunięto niezdefiniowane polecenie LaTeX oraz odsyłacz do rozdziału 06 z samodzielnego PDF; zachowano uzasadnienie źródłowe w tekście.
5. Dopracowano formatowanie rysunków, przenoszenie ilustracji do kolejnej sekcji i sprawdzono terminologię.

## Testy i kompilacja

- `bash tools/validate_general_topology_ch07.sh`: PASS, w tym regresja rozdziałów 01--06.
- 390 wszystkich topologii na zbiorach do 4 punktów: PASS; skończone modele ultrafiltrów: 1542 sprawdzenia; własności oddzielania: 390; ciągłe bijekcje: 184; iloczyny: 384.
- Etykiety rozdziału 07: 35; odsyłacze: 21; brak kolizji i brak niezdefiniowanych odsyłaczy w całej roboczej książce.
- `latexmk` samodzielny rozdział: 8 stron, bez ostrzeżeń; książka 01--07: 63 strony, bez ostrzeżeń.
- Kontrola wizualna wszystkich 8 stron: PASS.

## Wynik

Pierwszy audyt zakończony z poprawkami; nie jest czysty. **0/2**. Nowy rozdział nie został wypchnięty na GitHuba.

## Propozycja niezatwierdzona

**Lemat Aleksandra o podbazie** wraz z niezależnym dowodem stanowi użyteczne uzupełnienie i alternatywną drogę do twierdzenia Tychonoffa. Nie dodano, oczekuje na decyzję użytkownika. Propozycja sama w sobie nie blokuje audytu.
