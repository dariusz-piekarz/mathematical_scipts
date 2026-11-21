# Algebra liniowa — rozdział 04, audyt 3 (stabilizacyjny)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Plik:** `chapters/pl/linear_algebra/04-macierze-odwzorowan-liniowych-i-zmiana-bazy.tex`  
**SHA treści:** `a37ab689c60f83d3a137ac35c8a15de14e05bddc`

## Zakres

Ponownie przejrzano definicje, twierdzenia, dowody, przykłady, rysunek współrzędnych, przypadki zerowych wymiarów, kolejność mnożenia oraz zmiany baz. Skontrolowano wszystkie dziewięć części rozdziału, nie dodając nowych wyników ani nie ingerując w już zaakceptowany zakres. W szczególności skontrolowano niezależnie: identyfikację macierzy z odwzorowaniem, złożenie i łączność, wzór rzędu, pięć kryteriów odwracalności, wzory `Q^{-1}AP` i `P^{-1}AP`, transpozycję oraz opis zbioru rozwiązań.

## Wynik

**Nie wykryto nowego błędu matematycznego ani istotnej luki w istniejącym materiale. Plik rozdziału 04 pozostawiono bez zmian.** Audyt 3 jest pierwszym czystym audytem po korektach formalnych z audytu 2, zatem rozdział 04 zostaje uznany za merytorycznie stabilny i zamknięty. Wcześniejszy pełny CI po aktualizacji rozdziału 04: [44906175706](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44906175706) — success, 49 stron PDF; po obecnej iteracji nie zmieniono jego treści.

## Statyczna kontrola rozdziałów 01–04

Bezpośrednio z aktualnej gałęzi pobrano wszystkie cztery rozdziały i niezależnie zweryfikowano: **199 etykiet, 199 unikalnych nazw, 86 odsyłaczy `\\ref`/`\\eqref` bez brakujących celów**, prawidłowe domknięcie i zagnieżdżenie środowisk LaTeX, brak niedozwolonych zwrotów terminologicznych. Zgodność przykładów rachunkowych i wzorów z rozdziału 04 skontrolowano podczas ponownej lektury dowodów. Nie deklaruje się lokalnej kompilacji CLI w tym audycie: aktualna treść pochodzi z konektora GitHub, a środowisko robocze nie ma sieciowego dostępu `git clone`; podstawą poprzedniej weryfikacji składni i renderingu jest wskazany ukończony przebieg GitHub Actions.

## Kolejny etap

Można rozpocząć rozdział 05 o eliminacji Gaussa, nie otwierając ponownie rozdziałów 01–04 bez nowych przesłanek.
