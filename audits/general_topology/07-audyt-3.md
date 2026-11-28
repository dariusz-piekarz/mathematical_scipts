# Topologia ogólna — rozdział 07 — audyt 3

**Data:** 21 listopada 2026 r.  
**Wersja:** 0.3.  
**Status:** audyt z poprawkami; **0/2** kolejnych czystych audytów.  
**SHA256 źródła:** `988ca00c8f3c3f56e2aa08430a9013f720cdfdfd77d5a7d72996f6a773b6129b`.

## Zakres audytu

Ponowna kontrola kompletu definicji, twierdzeń, przykładów i dowodów: pokrycia otwarte, warunek skończonych przecięć, zamkniętość zwartych podzbiorów Hausdorffa, Weierstrass, normalność zwartych przestrzeni Hausdorffa, sieci/podsieci, ultrafiltry, Zorn, twierdzenie Tychonoffa, Heine–Borel, zanurzenie w kostkę i uzwarcenie. Kontrola założeń dla zbiorów pustych, terminologii, odsyłaczy i rysunków.

## Poprawki matematyczne i redakcyjne

1. **Nieuzasadniona ciągłość funkcji odległości w dowodzie zanurzenia w kostkę:** dopisano argument `|d(s,F)-d(u,F)| <= |s-u|` z nierówności trójkąta i przejścia do infimum oraz dokładne wyjaśnienie, dlaczego `|s-t|+d(s,F)>0` dla każdego `s` (osobno `s=t`). Dowód nie wymaga odsyłacza do innego rozdziału w samodzielnym PDF.
2. **Niejawne wybory nieskończonych rodzin otoczeń:** w dowodzie domkniętości zwartego podzbioru przestrzeni Hausdorffa i w dowodzie normalności zwartej przestrzeni Hausdorffa zastąpiono wybory otoczeń dla każdego punktu rozpatrzeniem zbioru **wszystkich** dopuszczalnych par. Zwartość pozwala na wybór tylko skończenie wielu par. Przywraca to jawny rygor dotyczący aksjomatu wyboru, bez niepotrzebnego założenia wyboru dla tych dwóch twierdzeń.
3. Rozpisano rozgałęzienie przypadków `F=∅` lub `G=∅` w dowodzie normalności i usunięto zbędną spację w sformułowaniu twierdzenia Weierstrassa.
4. Nie dodano żadnych nowych twierdzeń ani przykładów bez zgody użytkownika.

## Testy i wynik techniczny

- `bash tools/validate_general_topology_ch07.sh`: **PASS**, pełna regresja rozdziałów 01–07.
- Rozdział 07: 390 topologii skończonych; 1542 sprawdzenia ultrafiltrów; 390 testów oddzielania; 184 testy ciągłych bijekcji zwarte/Hausdorff; 384 testy iloczynów; 29 577 skończonych modeli Weierstrassa (2379 ciągłych).
- Regresja rozdziału 06: 41 350 przypadków sieci skierowanych, 4448 testów przykładu sieci, 38 490 testów filtrów obrazowych, 21 934 testy filtrów i domknięcia oraz 24 907 testów ciągłości.
- Etykiety, referencje i środowiska: PASS.
- `general_topology_ch07.pdf`: **9 stron**, bez ostrzeżeń LaTeX.
- `general_topology.pdf`: **64 strony**, bez ostrzeżeń LaTeX.
- Przegląd renderu 9 stron: bez kolizji tekstu, rysunków i podpisów.

## Status i dalszy krok

Z powodu stwierdzonych i naprawionych braków uzasadnienia audyt 3 **nie jest czysty**: seria **0/2**. Rozdział 07 pozostaje poza GitHubem do stabilizacji. Kolejny krok: audyt 4 wersji 0.3.

**Propozycja oczekująca na decyzję użytkownika:** lemat Aleksandra o podbazie. Nie wprowadzono go.
