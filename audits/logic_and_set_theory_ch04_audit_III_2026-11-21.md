# Audyt III — rozdział 04 „Pary uporządkowane i relacje”

**Data:** 21 listopada 2026 r.  
**Punkt wyjścia:** `chapters/pl/logic_and_set_theory/04-pary-uporzadkowane-i-relacje.tex`, po audycie II, blob Git `d4dcb300b9f16fdba31e71365762d43d0cfed5e0`.  
**Zakres:** kolejny audyt wyłącznie istniejących twierdzeń, lematów, definicji, dowodów, przykładów, terminologii, diagramów i odsyłaczy. Nie dodano nowego wyniku ani przykładu.

## Wykryte i naprawione niedokładności

1. **Puste zbiory w przykładzie składania macierzy relacji** (`sec:relation-matrices`). Zapis `A={a_1,...,a_m}` i `B={b_1,...,b_n}` sugerował istniejący ostatni element nawet przy `m=0` lub `n=0`, choć przykład obejmuje takie przypadki. Zastąpiono go deklaracją skończonych `A,B`, liczności `m,n∈ℕ` i wyliczeń pustych, gdy liczność wynosi zero. Analogicznie doprecyzowano wyliczenie `C` przy `p=0`. Wzór składania i przykład liczbowy są niezmienione.
2. **Puste zbiory w twierdzeniu o transpozycji macierzy relacji** (`thm:lxiv-relation-matrix-transpose`). Również tu zapis `a_1,...,a_m` nie uwzględniał dosłownie `m=0`, mimo że twierdzenie dopuszczało zbiory puste. Ustalono jawnie liczności i konwencję pustego wyliczenia. Teza `M_{R^{-1}}=M_R^{\mathsf T}` oraz dowód pozostają bez zmian.
3. **Definicja podzielności na ℤ w przykładzie.** Po wcześniejszym zdefiniowaniu podzielności na dodatnich liczbach naturalnych tekst przechodził do ℤ bez wskazania, że mnożnik może być ujemny. Dopisano jego dziedzinę `k∈ℤ`. Kontrprzykład dla antysymetrii pozostaje poprawny i niezmieniony.

Nie zmieniono żadnych tez, dowodów, etykiet, nazw środowisk ani istniejącego materiału ilustracyjnego.

## Weryfikacja matematyczna

Ponownie zbadano **12 twierdzeń, 3 lematy, 15 dowodów, 11 definicji, 17 przykładów i 6 uwag**. Skontrolowano jednoznaczność kodowania Kuratowskiego, konstrukcję iloczynu kartezjańskiego, obrazy i przeciwobrazy relacji, warunki jednoznaczności włókien, kolejność składania, odwracanie relacji, asymetrię, własności potęg, ścieżki, minimalność domknięć, relację równoważności generowaną przez relację oraz interpretację macierzową. W szczególności zbadano przypadki pustych zbiorów i relacji. **Nie stwierdzono błędów w tezach ani dowodach.**

Powtórzono enumerację **187 714** przypadków (`independent_check.py`) oraz dodatkowe **499** przypadków składania i odwracania relacji dla **27** konfiguracji rozmiarów zbiorów 0–2 (`matrix_edge_check.py`). Wszystkie testy zaliczono. Testy skończone nie zastępują formalnych dowodów dla dowolnych zbiorów.

## Kompilacja, odsyłacze i grafika

- Pełny skrypt: `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex` — **kod 0; 44 rozdziały, 376 stron**. Łącznie **1075 różnych etykiet, 866 odsyłaczy, 0 powielonych etykiet, 0 brakujących celów, 0 `Overfull \hbox`**.
- Książka repozytoryjna 01–04: **kod kompilacji 0, 41 stron**, bez `Overfull \hbox`. Odsyłacze do `ch:functions`, `ch:syntax-fol`, `ch:semantics-fol`, `ch:zf-axioms` pozostają nierozwiązane tylko w tym częściowym imporcie i są poprawne w pełnym skrypcie.
- Zachowano **35/35 etykiet**, ich kolejność oraz wszystkie środowiska: 12 twierdzeń, 3 lematy, 15 dowodów, 11 definicji, 17 przykładów, 6 uwag.
- Wyrenderowano i obejrzano wszystkie **10 stron** rozdziału 04 (strony 42–51 pełnego pliku), w tym dwa diagramy TikZ oraz zmienione fragmenty. Brak zauważonych nałożeń i obcięć tekstu. Rozdział nie ma zewnętrznych zależności graficznych.

## Status

**Audyt III wykonany.** Naprawiono trzy grupy drobnych luk formalnych, bez rozszerzania materiału. Ponieważ tekst wymagał korekty, **rozdział 04 pozostaje otwarty do audytu IV**. Po publikacji na GitHubie sprawdzamy również CI (indeksowanie, parser, testy regresyjne i Chromium).
