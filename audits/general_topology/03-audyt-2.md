# Audyt 2 — Topologia ogólna, rozdział 03 „Odwzorowania ciągłe"

- Data: 2026-11-21.
- Wersja: 0.1 (niezmieniona).
- Status: **pierwszy czysty audyt (1/2)**.
- Nie wprowadzono nowych twierdzeń, definicji ani zmian w rozdziale.
- SHA256 pliku rozdziału: `dd568d119fdf9ee051cb6701ec966cc6da1ef1a4dcd569fe88bfd8010fabe554`.

## Kontrola matematyczna

Zweryfikowano niezależnie:
- cztery kryteria ciągłości (otwarte, domknięte, obraz domknięcia, przeciwobraz domknięcia), a także kryterium przez wnętrze;
- warunek lokalny przez otoczenia i równoważność metryczną epsilon–delta;
- kryterium ciągłości przez bazę i podbazę, również gdy rodzina zawiera zbiór pusty lub jest pusta;
- składanie, ograniczanie do podprzestrzeni, sklejanie na otwartych i skończonych domkniętych pokryciach;
- charakteryzacje odwzorowań otwartych i domkniętych, kryteria homeomorfizmu oraz zanurzenia;
- przykłady z topologiami dyskretną, antydyskretną, Sorgenfreya i Sierpińskiego, funkcją skokową oraz kontrprzykład dla nieskończonego domkniętego pokrycia;
- pustą dziedzinę oraz pustą przeciwdziedzinę, bez założeń T1 lub Hausdorffa.

Brak błędów matematycznych lub nieprecyzyjnych założeń wymagających zmian tekstu.

## Testy

- Zestaw standardowy `bash tools/validate_general_topology_ch03.sh` — **PASS** (rozdziały 01–03; 24 907 par odwzorowanie/przestrzenie).
- Niezależna kontrola poprawności kryteriów przez wszystkie bazy i podbazy na przestrzeniach do 3 punktów — **PASS**, 334 294 asercje.
- Niezależna kontrola sklejania na wszystkich dwuelementowych otwartych i domkniętych pokryciach przestrzeni do 3 punktów — **PASS**, 468 206 asercji.
- Łącznie 390 topologii na zbiorach do 4 punktów w teście rozdziału 02; 50 etykiet w rozdziale 01, 124 unikatowe etykiety w książce.
- LaTeX (rozdział i pełna książka) — **PASS**, brak ostrzeżeń składu i niezdefiniowanych odsyłaczy w logu; osobny PDF: 8 stron A4.
- Kontrola wizualna wszystkich 8 stron PDF — **PASS**, bez nakładania napisów i wychodzenia poza marginesy.
- GitHub Actions — nieuruchomione dla wersji roboczej rozdziału 03, bez zmian w repozytorium.

## Decyzja

**Czysty audyt 1/2**. Następna iteracja: niezależny audyt 3 bez rozszerzania materiału. Jeśli będzie czysty, rozpocząć integrację repozytorium i pełne CI.
