# Audyt CXLVI (146) — twierdzenie Whitneya
Data 2026-11-24. Gałąź biblioteka-matematyczna-iteracja-6.

Poprzedni przebieg 45377789549: statusy regresji i PDF success (ffac587f8c66468eeefbe0e4f176ba5dbb50c9a9).

## Korekty
Commit d6e80543b7ac80da047f67b65bc6b4af4dfdc67c, blob 028d8388d85054abc1091ffe1aa41fa420f8bbce, 1163 → 1337 wierszy, 30 etykiet bez zmian.
- Poprawne pokrycie przez domknięte kostki o rozłącznych wnętrzach, nie przez same wnętrza.
- Konstrukcja kostek maksymalnych, jawne stałe odległości 8 i 18 razy pierwiastek z n; dla powiększeń 7 i 20; porównywalność boków, ograniczona krotność przez objętość, lokalna skończoność na zwartych podzbiorach dopełnienia K.
- Rozkład jedności: przeskalowanie funkcji obcięcia, indukcyjny wzór na pochodne odwrotności sumy i oszacowania Leibniza, uwzględnienie nośników pochodnych.
- Konieczność warunku Whitneya: reszta całkowa i jednostajna kontrola na zbiorze zwartym; jawna indukcja dla K równego całej przestrzeni.
- Wystarczalność: punkty najbliższe, lokalny moduł reszty, dokładne przepisanie wielomianu w innym środku; pełna suma Leibniza i redukcja potęg r.
- Przejście przez K: funkcje H_beta, osobne oszacowania na K i poza K oraz jawna różniczkowalność i ciągłość gradientów. Uwzględniono k=0.

## Regresje
Commit e0d60416fef822500cbd37fac4f3332677bb20b8: dodano MT31-006–008 (łącznie 8 testów). Niezależne kontrole JS: 72 przypadków kostek jednowymiarowych, 22500 przypadków przepisania wielomianu, 10 warunków źródłowych; zaliczone. Nie uruchomiono lokalnie Python ani nie oglądano nowego PDF. Status najnowszego CI: [].

## Następny krok
Mierzalność różniczki przybliżonej (mierzalny zbiór istnienia, obcięcia, granice), Whitney–Luzin (Jegorow, wspólny zbiór dobrych punktów, zwartość i zgodność), wyższe rzędy. Bez rozbudowy zakresu. Rozdział otwarty; 30/31.
