# Topologia ogólna — rozdział 06 „Zbieżność topologiczna” — audyt 2

**Data:** 21 listopada 2026 r.  
**Wersja:** 0.2.  
**Status:** audyt wykonany z poprawkami; seria czystych audytów **0/2**.  
**SHA-256 tekstu rozdziału:** `88843272d1f802fc314ef53afb28d407b9b2983912660ad3ce69045b09e76696`.

## Zakres i ustalenia

Ponowny przegląd definicji, dowodów, przykładów, diagramów, etykiet i przypadków brzegowych dotyczących ciągów, sieci (ciągów uogólnionych), podsieci i filtrów. Przejrzano równoważności kryteriów domknięcia, ciągłości i oddzielania oraz argumenty dla przestrzeni pustych i niet1. Nie dodawano nowych twierdzeń.

## Poprawki

1. **Nazwa „ciągi uogólnione”.** We wprowadzeniu i definicji sieci jawnie wskazano, że sieć (net) jest ciągiem uogólnionym: rodziną indeksowaną dowolnym niepustym zbiorem skierowanym. Zwykły ciąg odpowiada zbiorowi indeksów `\mathbb{N}`.
2. **Rysunek zbieżności.** Poprawiono sprzeczność geometryczną: punkt `x_2=1/2` znajdował się wewnątrz narysowanej otwartej kuli o promieniu `\varepsilon=1/2`. Zmieniono promień ilustracyjny na `2/5` (po przeskalowaniu osi), dzięki czemu punkty `x_1,x_2` są poza kulą, a `x_3,x_5,\ldots` wewnątrz.
3. **Baza skończona.** W dowodzie kryterium domknięcia przez ciągi dopowiedziano, że skończoną bazę otoczeń numerujemy z powtórzeniami, aby uzyskać ciąg `B_n`, jak w dowodzie.
4. **Komentarze źródłowe.** Poprawiono nieaktualne numery rozdziałów w nagłówkach dwóch plików głównych TeX (bez zmian treści matematycznej).

## Testy

- `bash tools/validate_general_topology_ch06.sh` — **PASS**.
- Wszystkie regresje rozdziałów 01–06 — **PASS**.
- 390 topologii skończonych (0–4 punkty) — **PASS**.
- 21 934 testy filtrów i domknięcia oraz 24 907 testów odwzorowań — **PASS**.
- Nowy niezależny test sieci o indeksach w skończonych zbiorach skierowanych (również nieuporządkowanych liniowo) — **41 350 przypadków PASS**.
- Samodzielny PDF rozdziału **8 stron**, książka 01–06 **54 strony**; brak ostrzeżeń LaTeX, komplet odsyłaczy, kontrola wizualna stron — **PASS**.

## Materiał proponowany, niewprowadzony

Rozważyć szczegółowy przykład sieci zbieżnej w topologii koprzeliczalnej do punktu spoza zbioru wyrazów, podczas gdy żaden zwykły ciąg w tym zbiorze nie ma takiej granicy. Można go uzyskać konstrukcją par `(U,a)` występującą już w dowodzie twierdzenia o domknięciu przez sieci. To tylko propozycja, bez zmiany bieżącego zakresu.

## Decyzja

Ponieważ audyt 2 wymagał poprawek, licznik **0/2**. Rozdział pozostaje w stabilizacji, bez wysyłania na GitHub. Następny audyt 3 dotyczy wersji 0.2.
