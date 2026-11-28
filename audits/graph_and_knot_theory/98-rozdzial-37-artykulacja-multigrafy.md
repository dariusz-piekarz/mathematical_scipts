# Rozdział 37 — audyt indywidualny 03

2026-11-24. Poprzednie CI: 45374709020 (regresja LOW, 7643fec) oraz 45374689125 (pełna książka, 54f7ee0) completed/success; 45374729575 również success. Kontrola wizualna PDF nadal otwarta.

Źródło 3b9a37a61430b3a72ea058c2f92e01ceafb5bb2f: rozwinięto obie implikacje kryterium artykulacji, jawnie wykluczono połączenia z innymi gałęziami DFS, wyjaśniono przypadek izolowanego korzenia, zapisano rekurencję low z identyfikatorami krawędzi i ograniczono warunek dla wierzchołków niebędących korzeniami. Łamanie wzoru: 9ea1b1afaeb3895a8b9fbbda101c8d58617f53b1.

TG37-MULTI-01 (81f88a5600f87b781234c9c778b018fe2d416119): enumeracja 761 multigrafów bez pętli na 0–4 wierzchołkach z krotnościami 0,1,2; porównanie mostów i artykulacji z niezależnym oraklem usuwania krawędzi według ID i wierzchołków. Wynik nowego CI jeszcze niepotwierdzony. Nie rozszerzano zakresu rozdziału. Następnie zweryfikować CI, skontrolować PDF i pozostałe dowody oraz przypadki brzegowe. Status OTWARTY.
