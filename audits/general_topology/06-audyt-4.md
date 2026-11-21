# Topologia ogólna — rozdział 06 — audyt 4

**Data:** 21 listopada 2026 r.  
**Wersja:** 0.4.  
**Status:** audyt zakończony z jedną korektą dowodową; **0/2 kolejnych czystych audytów**.  
**SHA-256 źródła:** `f93d19b39fd4cbdf0ee2db32cdd1bfc6b183ea5d46baf31e986b0f93af93eeae`.

## Zakres kontroli

Całość 855 wierszy źródła: zbieżność ciągów, pierwsza przeliczalność, sieci i ciągi uogólnione, podsieci, punkty skupienia sieci, iloczyny, właściwe filtry i równoważność zbieżności sieci i filtrów. Ponownie zbadano wszystkie założenia, zwłaszcza niehausdorffowskie przestrzenie i zbiory skierowane niebędące porządkami częściowymi. Uzasadniono konstrukcję sieci w topologii koprzeliczalnej bez niejawnego aksjomatu wyboru. Sprawdzono etykiety i widok PDF.

## Poprawka

W dowodzie wniosku `cor:topog-filtr-ciaglosc-hausdorff` wcześniej bez uzasadnienia używano filtru obrazowego generowanego przez rodzinę $\{f(F):F\in\mathcal F\}$. Dodano sprawdzenie, że jest ona bazą filtru: każdy obraz $f(F)$ jest niepusty, a dla $F,G\in\mathcal F$ mamy $F\cap G\in\mathcal F$ i $f(F\cap G)\subseteq f(F)\cap f(G)$. Nie dodano nowego twierdzenia ani przykładów.

## Testy i kompilacja

- `bash tools/validate_general_topology_ch06.sh` — **PASS** (rozdziały 01–06).
- Modelowa weryfikacja baz filtrów obrazowych — **38 490 przypadków PASS**.
- Sieci nad skierowanymi przedporządkami — **41 350 przypadków PASS**.
- Indeksowanie sieci z wyjątkiem przeliczalnym — **4448 testów skończonych analogów PASS**.
- Filtry, domknięcie, ciągi — **21 934 przypadki PASS**.
- Kryteria ciągłości przez filtry — **24 907 przypadków PASS**.
- Kompilacja samodzielnego rozdziału — **9 stron**, całej książki 01–06 — **55 stron**, bez ostrzeżeń `Overfull`, `Underfull`, `LaTeX Warning` i niezdefiniowanych odsyłaczy.
- Sprawdzono wizualnie dziewięć stron — **PASS**.

## Rekomendacje bez dopisywania treści

W przyszłej części dotyczącej zwartości rozważyć charakteryzację zwartości przez ultrafiltry i zbieżne podsieci; nie zmienia to obecnego audytu.

## Decyzja

Audyt wykrył wymagający poprawy brak uzasadnienia konstrukcji filtru obrazowego. Wersja 0.4 przyjęta do dalszej kontroli, **licznik czystych audytów 0/2**. Następny: audyt 5 niezmienionej wersji 0.4. Brak GitHub push przed stabilizacją.
