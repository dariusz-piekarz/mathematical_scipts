# CAT-07 — audyt I i trwałe kryteria regresyjne

Źródło: chapters/pl/category_theory/07-equalizatory-koequalizatory-i-kwadraty-kartezjanskie.tex.
Commit 95209080685c6ccc0cd50aef0562ef3f7115548c; blob 688fc2af259de918dde0bf2861c8a9ca8b09bb79.

## Zmiany
- Uzupełniono dowód własności uniwersalnej koequalizatora w Set, epiczności koequalizatora, sklejania zbiorów, homeomorfizmu przy ograniczeniu do podprzestrzeni oraz obliczenia pushoutu Z ← Z → Z. Rozróżniono zanurzenia do sumy rozłącznej od morfizmów do ilorazu.
- Dodano diagram i nazwę kwadratu kokartezjańskiego, konstrukcję pullbacku przez iloczyn i equalizator oraz dualną konstrukcję pushoutu.
- Dodano własności uniwersalne w modułach i Top, lemat o sklejaniu kwadratów z dowodem obu implikacji, stabilność mono przy pullbacku, epi przy pushoucie i izomorfizmów.
- Wykorzystano transwersalność jako warunek wystarczający istnienia pullbacku rozmaitości, a dla f=g:t↦t² dowiedziono nieistnienia kategorialnego pullbacku przez dwie gładkie krzywe i twierdzenie o submersji. Nie ograniczono kontrprzykładu do stwierdzenia, że zbiór zgodności nie jest podrozmaitością.
- Zachowano etykiety, poprawiono termin „włożenie”, sprawdzono stos środowisk przy zapisie.

## Wykorzystane źródła
- AA-16, 319cbac9af83a819e0d375fc282284c62638c3ac: jądro, obraz, moduł ilorazowy i pierwszy izomorfizm; wykorzystano do konstrukcji pullbacku i pushoutu modułów.
- GT-04, a7c1dac3b2f9dcc709a6f47bc4566d9740ef2081: topologia ilorazowa i jej własność uniwersalna.
- DG-15, f6d6ab60598e1ec5b39f7acea37c4953f5565c4b: twierdzenie o przecięciu i iloczynie włóknistym, transwersalność; dodano uzasadnienie własności kategorialnej i osobny kontrprzykład. Nie kopiowano dowodu twierdzenia o transwersalności.
- AA-18 przejrzano bez nowego importu. Nie weryfikowano odrębnych CI innych tomów.

## Kryteria regresyjne
| ID | Odsyłacz | Metoda i kryterium |
|---|---|---|
| CAT-07-001 | def:equalizer | Python + semantyczna: istnienie i jednoznaczność faktoryzacji w Set |
| CAT-07-002 | def:coeq | Python + semantyczna: relacja generowana, faktoryzacja i jednoznaczność |
| CAT-07-003 | cat:thm:pullback-pasting | Python: porównanie iterowanego i bezpośredniego pullbacku; semantyczna: obie implikacje |
| CAT-07-004 | cat:prop:base-change-mono | Python + semantyczna: stabilność iniekcji i surjekcji w Set |
| CAT-07-005 | cat:ex:module-pull-push | Python: niezależność reprezentanta w modelu cyklicznym; semantyczna: własności uniwersalne |
| CAT-07-006 | cat:ex:manifold-pullback | Python: algebraiczne równanie przecięcia i niezależność wektorów; semantyczna: pełny argument różniczkowy |
| CAT-07-007 | sec:equalizatory | Python: etykiety i środowiska |
| CAT-07-008 | cat:prop:pullback-equalizer | semantyczna: typy, faktoryzacja i dualność |
| CAT-07-009 | cat:ex:top-pull-push | semantyczna: topologia podprzestrzeni i ilorazowa |
| CAT-07-010 | cat:prop:base-change-iso | semantyczna: konstrukcja odwrotności |
| CAT-07-011 | cat:ex:manifold-pullback | semantyczna: transwersalność, gładkość faktoryzacji i kontrprzykład |

Testy w tools/tests/test_category_theory_ch07.py, commit a408e8f0a14df0abf4b35260a97c37a03bbba1ea, objęte istniejącym discovery CI. Nie potwierdzono jeszcze wykonania ani kompilacji. Nie uruchomiono Lean. Status otwarty, kolejna iteracja stabilizacyjna bez rozszerzania zakresu.
