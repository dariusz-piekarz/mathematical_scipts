# Logika matematyczna i teoria mnogości — rozdział 09, audyt II

**Data:** 21 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/logic_and_set_theory/09-jezyki-formalne-termy-i-formuly.tex`, niezmieniony Git blob `5015a7b838bebef105ccbe915c2e986e801e0c46` po audycie I.  
**Cel:** niezależny, drugi przegląd całego istniejącego materiału; bez nowych definicji, twierdzeń, lematów, przykładów i bez zmian pliku `.tex`.

## Wynik

**Audyt matematyczny i redakcyjny jest czysty: nie stwierdzono nowego błędu ani luki wymagającej korekty źródła.** Wcześniejsze doprecyzowania zachowują znaczenie zdań i usuwają niejasność między ścisłą gramatyką a dopuszczonymi skrótami zapisu.

Ponownie sprawdzono **2 twierdzenia, 5 lematów, 1 stwierdzenie, 8 dowodów, 7 definicji, 13 przykładów, 3 uwagi i 1 rysunek**.

## Szczegółowa ponowna kontrola matematyczna

1. **Alfabet, słowa i monoid wolny.** Weryfikacja jednoznaczności konkatenacji, słowa pustego, addytywności długości, istnienia i jednoznaczności przedłużenia funkcji `j:Σ→M` do homomorfizmu monoidów, włącznie z `Σ=∅` i monoidem nieprzemiennym. Dowód nie wymaga aksjomatu wyboru.
2. **Sygnatura i termy.** Odmienność rodzajów symboli, nadane arności, jednoznaczne rozdzielenie argumentów termu mimo zagnieżdżonych przecinków; rozróżnienie warstwy ścisłej gramatyki od drukarskich skrótów. Termy bez stałych i pusta sygnatura nie unieważniają konstrukcji termów ze zmiennych.
3. **Formuły.** Jednoznaczność ostatniego kroku konstrukcji dla atomów, negacji, spójników binarnych i obu kwantyfikatorów; zakaz traktowania nadmiarowych nawiasów grupujących jako nowych kroków gramatycznych.
4. **Wolne i związane zmienne.** Definicje rekurencyjne, zakres kwantyfikatora, jednoczesne wolne i związane wystąpienia tej samej zmiennej, puste zbiory wolnych zmiennych i zdania.
5. **Podstawienie termu w termie.** Wzór na zbiór zmiennych po podstawieniu: dwa przypadki zależne od `x∈FV(t)`, prawidłowe sumowanie zmiennych argumentów.
6. **Podstawienie w formule.** Rozróżnienie zastępowania tylko wolnych wystąpień i niedopuszczalnego przechwycenia; dokładny przypadek kwantyfikatora zasłaniającego `Qx`, warunki dopuszczalności pod `Qy`, w tym `x∉FV(ψ)`; prawo wolnych zmiennych po dopuszczalnym podstawieniu.
7. **Zmiana nazwy zmiennej związanej.** W przykładzie `∀v₁(v₀=v₁)` nie wolno podstawiać `v₀:=v₁` bez wcześniejszego przemianowania `v₁` na świeżą zmienną; uwaga o `α`-równoważności pozostaje w rozdziale na poziomie motywacji.
8. **Indukcja strukturalna.** Sprawdzono podstawę dla wszystkich atomów i termów bazowych, zamknięcie na każdą operację gramatyczną oraz wykorzystanie minimalności zbioru obiektów generowanych. Obejmuje także sygnaturę bez stałych.

## Dodatkowe niezależne testy skończonych modeli

W audycie II przygotowano **niezależny parser tokenowej, ścisłej gramatyki** testowej z wyróżnionymi symbolami logicznymi, zmiennymi, stałą, symbolem funkcyjnym i symbolem relacyjnym. Przetestowano:
- **2098** wygenerowanych formuł; każdą zserializowano do tokenów, sparsowano ponownie i porównano z pierwotnym drzewem budowy. Wszystkie serializacje różne, wszystkie dekodowania zgodne, bez niejednoznaczności.
- **6** przykładowych niepoprawnych napisów, w tym pozbawione wymaganych argumentów lub błędnie nawiasowane. Wszystkie zostały odrzucone.
- **7180** przypadków bezpiecznego przemianowania zmiennej wiązanej w różnie zagnieżdżonych formułach, z kontrolą zachowania zbioru zmiennych wolnych i poprawnego pomijania wystąpień przesłoniętych przez wewnętrzny kwantyfikator.

Wynik: **0 kontrprzykładów**. Kontrole próbek skończonych **nie zastępują dowodów ogólnych** ani nie dowodzą rozstrzygalności dla nieograniczonych struktur.

Regresje z audytu I zapisane w `tools/tests/test_logic_and_set_theory_ch09.py` nadal stanowią część CI: sprawdzają monoid wolny, składnię termów, **44 112** kombinacji formuł, termów i zmiennych, w tym 37 612 podstawień dopuszczalnych i 6500 niedopuszczalnych.

## Integralność i CI

- Zawartość rozdziału 09 i jego **19 etykiet** jest niezmieniona względem audytu I; nie usunięto ani nie dodano środowiska matematycznego. Bilans: 2 twierdzenia, 5 lematów, 1 stwierdzenie, 8 dowodów.
- Zintegrowane rozdziały 01–09 zawierają **269 unikatowych etykiet** i **96 odsyłaczy**. Dwa brakujące cele `ch:semantics-fol` i `ch:zf-axioms` są udokumentowanymi odsyłaczami do jeszcze niezaimportowanych rozdziałów.
- Diagram `fig:syntax-tree-xlv` nie był modyfikowany; poprzedni przegląd obrazu ze strony 90 całego skryptu nie wykazał kolizji ani obcięcia elementów.
- CI po audycie I zakończyło się sukcesem (GitHub Actions `44922050814`, **85 stron PDF**, 11 testów regresyjnych rozdziałów 07–09, bez nieoczekiwanych brakujących odsyłaczy oraz `Overfull \\hbox`). Bieżący raport wyzwala nową kontrolę na swoim commicie; jej wynik trzeba potwierdzić przed formalnym zamknięciem rozdziału.

## Konkluzja i kolejność prac

**Rozdział 09 jest stabilny merytorycznie po audycie II.** Nie wymaga zmian źródłowych. Zgodnie z przyjętą strategią jego formalne domknięcie następuje po zielonym CI na commicie z niniejszym raportem. Następny etap: audyt I rozdziału 10 („Semantyka języka pierwszego rzędu”), bez rozszerzania istniejącego materiału.
