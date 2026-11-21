# Topologia ogólna — rozdział 07 — audyt 4

**Data:** 21 listopada 2026 r.  
**Wersja po audycie:** 0.4.  
**Wynik:** audyt z poprawkami; **0/2** kolejnych czystych audytów.  
**SHA256 źródła:** `528f3167889132482ed34c3d4f6c8079dd2d08493a8011ebbb4773eb05f1c904`.

## Zakres

Kontrola wszystkich definicji, twierdzeń, kontrprzykładów i dowodów w rozdziale 07 (zwartość przez pokrycia, własność skończonych przecięć, własności Hausdorffa, Weierstrass, normalność, sieci i podsieci, ultrafiltry, Zorn, Tychonoff, Heine–Borel, zanurzenie w kostkę i uzwarcenie), spójności z rozdziałami 05 i 06, aksjomatu wyboru, przypadków pustych, LaTeX i rysunków.

## Wykryte i poprawione usterki

1. **Niespójność definicji podsieci.** W twierdzeniu `prop:topog-zwartosc-podsiec` tekst błędnie twierdził, że definicja z rozdziału 06 wymaga monotoniczności odwzorowania indeksów. Rozdział 06 wymaga tylko ostatecznej współkońcowości. Sprostowano odsyłacz i sformułowanie; dowód pozostaje poprawny, ponieważ zbudowane odwzorowanie rzeczywiście jest monotoniczne i ostatecznie współkońcowe. Dodano test regresji między rozdziałami oraz jawny przykład niemonotonicznego odwzorowania spełniającego warunek podsieci.
2. **Uzasadnienie otwartości otoczenia przy zanurzeniu.** Wyjaśniono, że `[0,1/2)` jest otwarty w podprzestrzeni `[0,1]`, a rzutowanie współrzędne jest ciągłe, więc przeciwobraz i przecięcie z `e(X)` są otwarte.
3. **Uzasadnienie ciągłości maksimum skończonego.** W dowodzie całkowitej regularności kostki dopisano, że `g_j ∘ p_j` są ciągłe oraz że `max(a,b)=(a+b+|a-b|)/2`; indukcja uzasadnia ciągłość maksimum skończonej liczby funkcji.
4. **Skład PDF.** Skrócono końcową redakcję przykładu zanurzenia prostej w przedział, usuwając wiszący fragment akapitu z początku strony 9. Treść matematyczna przykładu nie zmieniła się.

Nie dodawano nowych twierdzeń ani tematów, zgodnie z procedurą audytu.

## Walidacja

- `bash tools/validate_general_topology_ch07.sh`: **PASS** dla pełnej regresji rozdziałów 01–07.
- Rozdział 07: 390 skończonych topologii, 1542 sprawdzenia ultrafiltrów, 390 sprawdzeń oddzielania, 184 testy ciągłych bijekcji, 384 sprawdzenia iloczynów, 29 577 modeli Weierstrassa (w tym 2379 ciągłych).
- Regresja rozdziału 06: 41 350 testów sieci nad relacjami skierowanymi, 4448 testów jawnego przykładu, 38 490 filtrów obrazowych, 21 934 testy filtrów/domknięcia i 24 907 testów odwzorowań.
- Testy zgodności definicji podsieci między rozdziałami 06–07 oraz niemonotonicznej ostatecznie współkońcowej mapy indeksowej: **PASS**.
- Etykiety, odsyłacze, środowiska i terminologia: **PASS**.
- PDF rozdziału: 9 stron A4, bez ostrzeżeń LaTeX; PDF książki: 64 strony, bez ostrzeżeń LaTeX.
- Po ponownym renderze sprawdzono wszystkie strony; na stronie 9 nie występuje osierocony fragment poprzedniego akapitu.

## Decyzja

Audyt 4 nie jest czysty, ponieważ wymagał poprawek. Seria **0/2**. Rozdział 07 nie trafia jeszcze na GitHub. Następnie audyt 5 wersji 0.4.

**Propozycja do decyzji użytkownika:** lemat Aleksandra o podbazie (bez dodawania do obecnego rozdziału).
