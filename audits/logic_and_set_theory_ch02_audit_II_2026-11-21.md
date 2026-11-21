# Audyt II — rozdział 02 „Kwantyfikatory i podstawowe metody dowodzenia”

Data: 21 listopada 2026. Materiał źródłowy: plik `02-quantifiers-and-proofs.tex` po audycie I, zgodny z rewizją GitHub `1a69b9548ef179827a25db24e145f0ca140045e3` na początku iteracji. Weryfikacja ograniczona do już istniejącego zakresu rozdziału: **bez dodawania twierdzeń, lematów, przykładów czy sekcji**.

## Wykryte i naprawione kwestie

1. **Kwantyfikatory ograniczone a ich rozwinięcia w języku pierwszego rzędu.** Pojęcie predykatu w początkowej definicji dopuszczało interpretację tylko na `D`. Natomiast wzory `∀x (x∈D ⇒ P(x))` i `∃x (x∈D ∧ P(x))` wymagają, by `P(x)` miało określony sens na całym uniwersum zmiennej `x`, również poza `D`. W uwadze „Skrót formalny” jawnie wprowadzono niepuste uniwersum `U`, założenie `D⊆U` oraz interpretację `P` na `U`. Nie zmieniono definicji kwantyfikatorów ograniczonych ani twierdzeń.
2. **Wystąpienia zmiennych związanych.** W istniejącej definicji zakresu działania kwantyfikatora doprecyzowano sytuację wewnętrznego kwantyfikatora tej samej zmiennej, który przesłania zewnętrzne wiązanie. To rozróżnienie jest istotne przy wcześniejszym przykładzie przechwytywania zmiennej.
3. **Negacja zdania z uczniami.** Niejednoznaczne językowo sformułowanie „wszyscy uczniowie nie zdali” zastąpiono jednoznacznym „żaden uczeń nie zdał” jako zaprzeczenie zdania „istnieje uczeń, który zdał”.
4. **Dowód jednoznacznego istnienia.** Poprawiono instrukcję „podajemy świadka” na „wykazujemy istnienie (na przykład wskazując świadka)”, aby nie sugerować, że dowód klasyczny musi zawsze dostarczać świadka w postaci jawnej. Zachowano wymóg osobnego dowodu jednoznaczności.

## Kontrola drugiego przejścia

- Przejrzano wszystkie istniejące definicje, przykłady, twierdzenia i ich dowody oraz przypadki pustych dziedzin. Tezy twierdzeń o zmianie nazwy zmiennej związanej, prawach de Morgana, zamianie dwóch kwantyfikatorów tego samego rodzaju, jednostronnej zamianie kwantyfikatorów mieszanych, jednoznacznym istnieniu i indukcji pozostały poprawne. Indukcja nadal jest jawnie przyjęta jako podstawowa własność `ℕ`, bez udawania dowodu z samych praw logiki.
- Test niezależnych wyczerpujących wartościowań: 1364 przypadki kwantyfikatorów ograniczonych i ich rozwinięć w niepustym uniwersum o rozmiarze 1–5, po 1364 przypadki praw de Morgana i jednoznacznego istnienia, 689 przypadków kolejności kwantyfikatorów nad dziedzinami o rozmiarze 0–3, 201 kontrprzykładów do implikacji odwrotnej i 6 skończonych kontrprzykładów ilustrujących przechwytywanie zmiennej. Wszystkie kontrole zakończyły się sukcesem.
- Bez zmian: **6 twierdzeń, 5 definicji, 28 przykładów, 12 uwag, 5 dowodów i wszystkie 39 etykiet**. Nie dodano nowego materiału ani nie przemianowano etykiet.
- Pełna kompilacja `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex`: kod wyjścia 0, 376 stron i 44 rozdziały; 1075 etykiet bez duplikatów, 866 odsyłaczy bez brakujących celów, 0 ostrzeżeń `Overfull \\hbox`. Trzy `Underfull \\hbox` dotyczą innych fragmentów skryptu i nie blokują kompilacji.
- Kompilacja częściowej książki z rozdziałami 01–02 i preambułą repozytorium: kod 0, 20 stron, bez `Overfull \\hbox`. Dwa odsyłacze do `ch:syntax-fol` (09) i `ch:semantics-fol` (10) pozostają nierozwiązane tylko w tej częściowej książce, ponieważ docelowe rozdziały jeszcze nie zostały zaimportowane do repozytorium. W pełnym skrypcie oba cele istnieją.
- PDF rozdziału 02 wyodrębniono ze składu pełnego i sprawdzono wizualnie wszystkie 9 stron. Nie zauważono nachodzących na siebie elementów ani błędów składu.

## Status

**Audyt II rozdziału 02 wykonany**: naprawiono cztery wykryte nieścisłości, po czym testy merytoryczne i kompilacja przeszły. W obecnie skontrolowanym zakresie nie ma nowych wykrytych błędów. Pozostaje zgodnie z ustalonym planem powtórzyć audyt tego samego rozdziału, zamiast automatycznie przechodzić do 03. Weryfikacja GitHub Actions po wypchnięciu jest osobnym krokiem.
