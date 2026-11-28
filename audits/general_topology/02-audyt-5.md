# Topologia ogólna — rozdział 02 — audyt 5

**Data:** 21 listopada 2026 r.  
**Wersja:** 0.3 (bez zmian).  
**SHA-256 źródła:** `6449f391ca3edfbeeb247ebd246faff4fb9f7c9ea258a0a9be1b28d0291de2ab`.

## Przedmiot kontroli

Cały tekst 780 wierszy: wnętrze, domknięcie, brzeg, zewnętrze, zbiór pochodny, punkty izolowane, gęstość, nigdziegęstość oraz aksjomaty Kuratowskiego. Sprawdzono założenia (także przypadki nietypowe, np. przestrzenie niespełniające T1 i przestrzeń pusta), poprawność dowodów i kontrprzykładów oraz terminologię i rysunek. Nie znaleziono błędów wymagających zmiany.

## Testy

- Testy lokalne: `bash tools/validate_general_topology_ch02.sh` — PASS.
- Niezależna kontrola skończonych modeli: 390 topologii na zbiorach 0–4 punktów — PASS.
- Operatory Kuratowskiego na zbiorze dwupunktowym: 256 możliwości, dokładnie 4 spełniają aksjomaty — PASS.
- Kompilacja `general_topology_ch02.tex` (8 stron) i `general_topology.tex` (19 stron) — PASS, bez ostrzeżeń.
- Kontrola graficzna wszystkich stron — PASS.

**Decyzja:** Audyt 5 czysty. Poprzedni audyt 4 był czysty, zatem 2/2. Rozdział 02 stabilny matematycznie; integracja i CI wymagają odrębnej kontroli.
