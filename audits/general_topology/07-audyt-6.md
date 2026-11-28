# Topologia ogólna — rozdział 07 — audyt 6

**Data:** 21 listopada 2026 r.  
**Wersja:** 0.4 (bez zmian).  
**Wynik:** **drugi czysty audyt z rzędu — 2/2; rozdział stabilny matematycznie**.  
**SHA256 źródła przed i po audycie:** `528f3167889132482ed34c3d4f6c8079dd2d08493a8011ebbb4773eb05f1c904`.

## Kontrola matematyczna

- Definicja zwartości, zwartość pustej przestrzeni, zbiorów skończonych i przedziału domkniętego; własność skończonych przecięć z rozróżnieniem pustej rodziny i pustej przestrzeni.
- Zwartość obrazów ciągłych i domkniętych podzbiorów; domkniętość zbiorów zwartych w przestrzeni Hausdorffa, normalność przestrzeni zwartych Hausdorffa i homeomorficzność ciągłych bijekcji na przestrzenie Hausdorffa.
- Twierdzenie Weierstrassa: niepusta dziedzina, brak potrzeby założenia Hausdorffa, dowód osiągania obu kresów oraz kontrprzykłady.
- Punkty skupienia sieci i filtrów; konstrukcja zbieżnej podsieci na zbiorze skierowanym trójek; warunek ostatecznej współkońcowości zgodny z rozdziałem 06.
- Kryterium zwartości przez sieci i konstrukcja indeksów `(J,x)` unikająca jednoczesnego wybierania nieskończonej rodziny punktów.
- Kryterium ultrafiltru, lemat Zorna, kryterium zwartości przez zbieżność ultrafiltrów; role aksjomatu wyboru.
- Twierdzenie Tychonoffa dla pustego zbioru indeksów, pustego czynnika i niepustych rodzin; ultrafiltry projekcyjne i zbieżność w topologii produktowej.
- Twierdzenie Heinego–Borela i identyczność topologii iloczynowej z euklidesową.
- Zanurzenie w kostkę: ciągłość współrzędnych, rozdzielanie punktów i zbiorów domkniętych, ciągłość odwrotności, dowód całkowitej regularności kostki, przypadki puste i zwartość uzwarcenia.

Wynik niezależnego przeglądu: **brak błędów i brak koniecznych zmian w źródle**.

## Walidacja i PDF

- `bash tools/validate_general_topology_ch07.sh` — **PASS**.
- 390 modeli topologicznych, 1542 testy ultrafiltrów, 390 testów oddzielania, 184 testy ciągłych bijekcji, 384 testy iloczynów, 29 577 testów Weierstrassa — **PASS**.
- Regresja rozdziałów 01–06 (w tym 41 350 testów sieci i 38 490 testów baz filtrów obrazowych) — **PASS**.
- Kompilacja samodzielnego rozdziału 07: 9 stron, bez ostrzeżeń LaTeX. Książka 01–07: 64 strony, bez ostrzeżeń.
- Wizualna inspekcja renderów dziewięciu stron, podpisów rysunków, tabeli i przełomów stron: **PASS**.

## Niezatwierdzone propozycje rozbudowy

Lemat Aleksandra o podbazie: nadal proponowany, ale nie dodany, ponieważ brak akceptacji. Nie jest wymogiem uznania audytu za czysty.

## Decyzja

**2/2 czystych audytów.** Rozdział 07 w wersji 0.4 zakwalifikowany do integracji na istniejącej gałęzi GitHuba, z rozszerzeniem testów CI i kontrolą wygenerowanych PDF-ów.
