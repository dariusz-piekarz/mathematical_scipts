# CAT-05 — audyt I i trwałe kryteria regresyjne

Źródło: chapters/pl/category_theory/05-obiekty-uniwersalne-poczatkowe-koncowe-zerowe.tex.
Commit a91cc5f7b1a0f216ac5bcd5e86c0f9776c5f75e0, blob 34cf412b2a5190ecf4bb7f99e81c43c5298d4d4e.

## Zmiany
- Uzupełniono dowody początkowości i końcowości w podstawowych kategoriach, w tym przypadek pustej dziedziny. Rozpisano argument jednoznaczności obiektów końcowych bez skrótu dualności.
- Dodano Z jako obiekt początkowy pierścieni przemiennych z jedynką, pierścień zerowy jako końcowy, oraz dowód nieistnienia końcowego po wykluczeniu pierścienia zerowego przez charakterystyki 2 i 3.
- Dodano moduł zerowy, Top_*, Rel, grupę jednoobiektową i kategorię iniekcji jako przykłady i kontrprzykłady.
- Dowiedziono rozszczepienia morfizmów wychodzących z końcowego i wchodzących do początkowego. Zdefiniowano ścisły obiekt początkowy z przykładami.
- Zdefiniowano morfizmy zerowe, udowodniono niezależność wyboru obiektu zerowego, pochłanianie w składaniu, kryterium id_A=0_{A,A} oraz zachowywanie zer przez funktor zachowujący obiekt zerowy.
- Wyjaśniono, że jednoznaczność porównań konstrukcji uniwersalnych dotyczy morfizmów zgodnych z dodatkowymi danymi. Zapisano zgodność kanonicznych porównań przy składaniu.
- Zachowano istniejące etykiety i sprawdzono stos środowisk przy zapisie.

## Wykorzystane źródła
- AA-09, blob c6a5ac5d6f8f067a051c49860eae815915bff7d0, wiersze 35–48: konwencja dopuszczająca pierścień zerowy. Nowy dowód własności początkowej i końcowej w CAT.
- AA-16, blob 319cbac9af83a819e0d375fc282284c62638c3ac, definicja modułu wolnego i przypadek pustego zbioru generatorów. Użyto konstrukcji, bez powielania dowodu istnienia; wcześniej potwierdzony raport stabilizacji.
- CAT-01: Rel, Top_*; CAT-02: rozszczepione mono/epi. Zweryfikowano etykiety sec:kategorie, sec:morfizmy oraz sec:produkty w istniejących źródłach.
- ALG-04 przejrzano pod kątem konwencji pierścieni i spektrum; bez bezpośredniego importu na tym etapie. Nie weryfikowano nowego CI innych tomów.

## Kryteria regresyjne
| ID | Odsyłacz | Metoda i kryterium |
|---|---|---|
| CAT-05-001 | def:poczatkowy | Python + semantyczna: pusta dziedzina, singleton, nieistnienie końcowego w kategorii iniekcji |
| CAT-05-002 | cat:ex:pointed-zero, cat:prop:zero-absorption | Python + semantyczna: Rel, relacja pusta, pochłanianie, identyczność zerowa tylko na pustym zbiorze |
| CAT-05-003 | cat:ex:pointed-zero | Python + semantyczna: skończone zbiory z wyróżnionym punktem jako dyskretne przestrzenie; jednoznaczność i pochłanianie |
| CAT-05-004 | cat:ex:initial-ring | Python + semantyczna: model Z/n, warunki 2=0 i 3=0, wzór homomorfizmu z Z |
| CAT-05-005 | sec:uniwersalne | Python: zachowanie etykiet i środowisk |
| CAT-05-006 | tw:unique-universal, cat:rem:universal-coherence | semantyczna: jedyność izomorfizmu i zgodność porównań |
| CAT-05-007 | cat:prop:initial-terminal-arrows, cat:def:strict-initial | semantyczna: kierunki rozszczepień i ścisła początkowość |
| CAT-05-008 | cat:prop:zero-absorption | semantyczna: niezależność obiektu zerowego i równoważność id_A=0 |
| CAT-05-009 | cat:prop:zero-functor | semantyczna: zachowywanie zer przy zachowaniu obiektu zerowego |

Testy: tools/tests/test_category_theory_ch05.py, commit 8a5961f5101942fd7970f9613f2582de142a279f. Istniejący workflow discovery obejmuje nowy plik. Nie potwierdzono jeszcze uruchomienia testów ani kompilacji. Bez formalizacji Lean.

Status: otwarty. Kolejna iteracja stabilizacyjna, bez rozszerzania zakresu.
