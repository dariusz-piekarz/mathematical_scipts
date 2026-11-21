# Topologia ogólna — rozdział 07 — audyt 5

**Data:** 21 listopada 2026 r.  
**Wersja:** 0.4 (bez zmian).  
**Wynik:** **audyt czysty; 1/2 kolejnych czystych audytów**.  
**SHA256 źródła (przed i po audycie):** `528f3167889132482ed34c3d4f6c8079dd2d08493a8011ebbb4773eb05f1c904`.

## Niezależna kontrola matematyczna

- Zwartość i warunek skończonych przecięć, uwzględniając `X=∅`, pokrycia puste i rodziny skończone.
- Dowód zwartości domkniętych odcinków przez supremum; pokrycie przez otwarte przedziały; własności domkniętych podprzestrzeni i obrazów ciągłych.
- Domkniętość zwartych podzbiorów przestrzeni Hausdorffa oraz normalność przestrzeni zwartych Hausdorffa, ze skończonym wyborem par otoczeń.
- Twierdzenie Weierstrassa, obie skrajne wartości i kontrprzykłady, bez założenia Hausdorffa.
- Definicja punktu skupienia sieci; istnienie zbieżnej podsieci ze skierowanego zbioru trójek. Spójność z rozdziałem 06: wymagana ostateczna współkońcowość, bez konieczności monotoniczności.
- Kryterium zwartości przez sieci i konstrukcja indeksów `(J,x)` eliminująca niejawny wybór.
- Kryterium ultrafiltru przez alternatywę podzbioru i dopełnienia; przedłużenie przez lemat Zorna; kryterium zwartości przez ultrafiltry.
- Twierdzenie Tychonoffa: przypadki pustych czynników i pustego zbioru indeksów, użycie wyboru i ciągłość rzutowań.
- Twierdzenie Heinego–Borela i równoważność metryk maksimum i euklidesowej.
- W obu kierunkach twierdzenie o zanurzaniu przestrzeni Tychonoffa w kostkę: injektywność, topologia podprzestrzeni, ciągłość funkcji oddzielających, dodatniość mianownika, ciągłość maksimum, przypadki pustych rodzin oraz zwartość uzwarcenia.

**Wynik:** nie stwierdzono błędów, luk wymagających poprawek ani nieuzasadnionych istotnych wzorów. Bez nowych treści i bez zmian źródła.

## Walidacja

Komenda: `bash tools/validate_general_topology_ch07.sh` — **PASS**.

- Rozdział 07: 390 modeli topologicznych, 1542 testy ultrafiltrów, 390 sprawdzeń oddzielania, 184 testy ciągłych bijekcji, 384 testy iloczynów, 29 577 testów funkcji z twierdzenia Weierstrassa.
- Regresja rozdziałów 01–06, w tym 41 350 testów sieci i 38 490 testów filtrów obrazowych — **PASS**.
- Kontrola etykiet, odsyłaczy, terminologii, środowisk — **PASS**.
- PDF rozdziału 07: **9 stron A4**, bez ostrzeżeń LaTeX. PDF książki 01–07: **64 strony**, bez ostrzeżeń.
- Kontrola układu i rysunków (w tym stron 7–9 oraz przykładu Weierstrassa): **PASS**.

## Propozycje niezatwierdzone

Lemat Aleksandra o podbazie — nadal do decyzji użytkownika; nie dodany, nie wpływa na licznik audytów.

## Decyzja

Rozdział pozostaje w wersji 0.4, **1/2** kolejnych czystych audytów. Następny: audyt 6. GitHub push i CI dopiero po drugim czystym audycie.
