# Synchronizacja aplikacji Biblioteki matematycznej z GitHub — 20 XI 2026

Repozytorium: `dariusz-piekarz/mathematical_scipts`.
Gałąź: `biblioteka-matematyczna-iteracja-6` (nie `main`).
Zweryfikowany HEAD po przesłaniu: `b7108a1ecae1cfe568cadbff362539337a0bedfa`.

## Co rzeczywiście przesłano

W tej sesji dodano 25 nowych plików do gałęzi: 2 benchmarki w `application/scripts/`, 7 testów w `application/tests/`, 12 szablonów preambuł w `application/config/preambles/`, konfigurację aliasów i trzy pliki stanu/raportów (`ROADMAP_I_DZIENNIK.md`, `raport_v19.json`, `benchmark_process_v19.json`). Wcześniej dodane zostały dodatkowo benchmark procesowy i jego test, które pozostają w gałęzi. Łącznie w katalogu `application/` po synchronizacji występuje 47 plików śledzonych przez Git.

Nie zmieniano gałęzi `main`, `chapters/`, `books/` ani kanonicznych źródeł matematycznych. Zmiany w istniejącym kodzie `application/backend/` i `application/frontend/` **nie** były automatycznie nadpisywane: repozytorium ma równoległą i różną od ZIP v0.19 wersję generatora. To wymaga przeglądu funkcja po funkcji, a nie podmiany całego katalogu.

## Weryfikacja

- GitHub: odczyt listy plików z drzewa gałęzi (`recursive=1`, `truncated=false`); 47 plików `application/`.
- Testy: na odtworzonej z ZIP v0.19 lokalnej migawce wykonano `python -W default -m unittest discover -s tests -q`; **84/84 testów przeszło**, kod 0 (4.388 s). Jest to test migawki, **nie** wynik testów zhybrydyzowanej gałęzi GitHub.
- Nie przeprowadzono kompilacji LaTeX, testu przeglądarkowego ani testu CI na aktualnym HEAD GitHub.
- Repozytorium nadal nie zawiera całego archiwum ZIP, jego bazy SQLite ani 352 rozdziałów-snapshotów z ZIP; `chapters/pl/` jest kanonicznym źródłem i nie należy nadpisywać go historyczną migawką.

## Pozostałe prace

1. Porównać treść i publiczne API `backend/generator.py`, `backend/api.py`, testów już istniejących na GitHub oraz wersji Biblioteki; scalać selektywnie bez utraty nowszych zmian z repozytorium.
2. Zbudować indeks aplikacji z aktualnego `chapters/pl/` (nie ze snapshotu ZIP), a następnie uruchomić testy z gałęzi GitHub.
3. Zweryfikować eksporty międzydziedzinowe i pełny `xr-hyper`, sprawdzić w przeglądarce Explorer, czytnik i graf.
4. Dopiero po sukcesie testów określić wersję wdrożeniową i rozważyć PR do `main`.

Status: **synchronizacja częściowa, bez deklaracji zakończenia etapu**.