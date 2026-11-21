# Topologia ogólna — rozdział 06, audyt 1

- Data: 21 listopada 2026 r.
- Rozdział: **Zbieżność topologiczna** (805 wierszy źródła).
- Wersja: **0.1**, audyt zakończony z poprawkami, zatem **0/2** kolejnych czystych audytów.
- SHA-256 źródła: `096c321e8f17c27bbcf2ddc0a531f483740d298ec32ed632ad1b4552be49925d`.
- Stan GitHuba: źródło pozostaje lokalne do stabilizacji.

## Zakres

1. Definicja zbieżności ciągów, bazy otoczeń i metryki, podciągi, obrazy odwzorowań ciągłych, jednoznaczność granic w T2.
2. Pierwsza przeliczalność, domknięcie ciągowe i kryterium ciągłości, kontrprzykład z topologią koprzeliczalną.
3. Skierowane zbiory indeksów, sieci, domknięcie i ciągłość przez sieci, charakteryzacja aksjomatu T2.
4. Podsieci, punkty skupienia, zbieżność współrzędnych w iloczynach.
5. Filtry właściwe, bazy filtrów, zbieżność, domknięcie, odpowiadanie filtrów sieciom i kryteria ciągłości.

## Poprawki audytu 1

- Rozwinięto dowód równoważności ciągłości z zachowywaniem zbieżności filtrów. Jawnie pokazano własność filtru obrazowego oraz porównanie filtrów ogonów sieci i obrazów sieci.
- Dopisano uzasadnienie braku pierwszej przeliczalności przestrzeni z topologią koprzeliczalną przez odwołanie do udowodnionego kryterium domknięcia ciągowego.
- W nowym teście skończonym poprawiono obliczanie obrazów podzbiorów dla nieiniektywnych odwzorowań i uwzględniono przypadek pustej przeciwdziedziny. Problem dotyczył kodu testowego, nie treści twierdzeń.

## Kontrole

- `bash tools/validate_general_topology_ch06.sh` — **PASS**.
- Zachowano regresję wszystkich rozdziałów 01–05 — **PASS**.
- Wszystkie 390 topologii na zbiorach 0–4 punktów, testy filtrowe, domknięcia i ciągów — **21 934 przypadki**, PASS.
- Ciągłość przez filtry na odwzorowaniach skończonych — **24 907 przypadków**, PASS.
- Kontrola źródeł — 251 różnych etykiet, 38 poprawnie rozwiązanych odsyłaczy — PASS.
- Samodzielny `general_topology_ch06.tex` — **8 stron**, bez ostrzeżeń LaTeX.
- Cała książka `general_topology.tex` (rozdziały 01–06) — **54 strony**, bez ostrzeżeń LaTeX.
- Wizualny przegląd wszystkich stron i obu rysunków — bez dostrzeżonych wad.

## Propozycje, bez automatycznego dodawania

W przyszłej części o zwartości można rozważyć pełne kryterium zwartości przez punkty skupienia sieci i zbieżność ultrafiltrów, wykorzystujące definicje z tego rozdziału. Do decyzji użytkownika; **nie dodano** do rozdziału 06.

**Decyzja:** rozdział 06 pozostaje w audycie; następny etap to niezależny audyt 2 wersji 0.1.
