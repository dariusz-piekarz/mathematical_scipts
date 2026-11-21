# AA-06 — audyt II, 21 listopada 2026

## Decyzja
Iteracja bez nowych poprawek matematycznych, językowych i edytorskich. Źródło identyczne z wersją po audycie I, SHA-256: effc7e3939d59d003a4bdd1e64813b870b116bdce4d6a2956884d1d9d75090bb. Zachowane 21 etykiet, 11 dowodów, 3 definicje, 7 twierdzeń, 3 lematy, 1 stwierdzenie, 8 przykładów i 3 uwagi.

## Kontrola matematyczna i techniczna
- Pełna kontrola dowodów: wewnętrzne/zewnętrzne iloczyny proste i półproste, rozszerzenia i przekroje homomorficzne, Q8 i C4, klasyfikacja grup rzędu pq, normalizatory w grupach nilpotentnych oraz kryterium normalności wszystkich podgrup Sylowa.
- 17/17 niezależnych testów matematycznych PASS; 17/17 PASS w lokalnej strukturze repozytorium.
- LaTeX AA-01–AA-06: PASS, 50 stron; 3 świadome odsyłacze wyprzedzające do AA-08 i AA-18.
- Pełny tom 74 rozdziałów: PASS, 463 strony, 1411 unikatowych etykiet, 952 odsyłacze, bez niezdefiniowanych referencji.
- Kontrola wizualna 8 stron AA-06: PASS, bez kolizji, uciętych wzorów i ostrzeżeń dotyczących AA-06.

## Odsyłacze wyprzedzające
Stabilny tom na razie obejmuje AA-01–AA-06. AA-06 zawiera dokładnie 3 poprawne etykiety z późniejszych rozdziałów: aa:ch:grupy-abelowe, aa:tw:abelian-tensor-cyclic i aa:ch:module-tensor-product. Wszystkie rozwiązują się w pełnym 74-rozdziałowym tomie, lecz nie rozwiązują się w częściowym tomie AA-01–AA-06. Workflow jawnie dopuszcza tylko te trzy, a dowolne inne niezdefiniowane odsyłacze nadal traktuje jako błąd. Po ustabilizowaniu AA-08 i AA-18 wyjątki należy usunąć.

## Integracja
Zarejestrowano AA-06 w catalog/books.json i books/pl/abstract_algebra.tex, dodano niezależne testy tools/tests/test_abstract_algebra_ch06.py oraz rozszerzono workflow CI. Starsze zgłoszenia tools/validate_repository.py nadal pozostają diagnostyczne i dotyczą innych modułów. Wynik GitHub Actions należy zweryfikować na commicie po pushu.
