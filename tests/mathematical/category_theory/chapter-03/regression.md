# CAT-03 — audyt I, rozszerzenie i trwałe kryteria regresyjne

Źródło: chapters/pl/category_theory/03-funktory-odwzorowania-miedzy-kategoriami.tex.
Commit 5c284576ed9fc80220819e5031ed59e37b5ade6c; blob 7722d3d50755970a91bfac2910a6e037a036a8f8.

## Zmiany
- Uzupełniono dowód funktorialności potęgi symetrycznej, składowych spójnych i obu funktorów Hom; zapisano jawnie aksjomat identyczności dla funktora kontrawariantnego.
- Rozróżniono składowe spójne c(X) od składowych łukowej spójności pi_0(X); zgodność notacji w pozostałych rozdziałach do kontroli przy stabilizacji.
- Dodano dowód odzwierciedlania mono i epi przez funktor wierny, zachowywania rozszczepień przez dowolny funktor i kontrprzykłady dotyczące pełności, wierności oraz zachowywania izomorfizmów.
- Dodano kategorie iloczynowe, bifunktory Hom i tensorowy, z kontrolą typów i kolejności składania.
- Dodano kontrawariantne spektrum jako funktor do Top (nie utożsamiono go z pełną konstrukcją schematów), homologię kompleksów, cofnięcie form i kohomologię de Rhama.
- Zachowano dotychczasowe etykiety; sprawdzono stos środowisk podczas zapisu.

## Wykorzystanie źródeł
- AA-18, blob faaa972f8d1a7625d42c856d78c6f58ee7ad3564: własność uniwersalna iloczynu tensorowego (aa:tw:tensor-universal), moduł nad pierścieniem przemiennym, element neutralny. Zastosowano konstrukcję, bez kopiowania dowodu istnienia. Istnieje raport stabilizacji.
- ALG-04, blob ab1344ed93a02bb757e5a78cb3833d6c4a18079c: spektrum i bazowe otwarte Zariskiego. W CAT udowodniono funktorialność samej przestrzeni topologicznej.
- AT-03, blob 03ee5b773493ee95746413aabd760d54b6a640e6: prop:homologia-funktor, definicja homologii; wykorzystano konstrukcję i jej argument.
- DG-10, blob 858d30abdfb27335f8194740f2304ee98d5ca15a: prop:formy-wedge-pullback, eq:pullback-formy, def:de-rham-cohomology; wykorzystano cofnięcie i jego zgodność z różniczką zewnętrzną, bez powielania pełnego dowodu tego ostatniego wyniku.
Nie potwierdzano w tej iteracji osobnego CI AT/DG. Odwołania do innych książek tekstowe, bez nowych konfliktów etykiet.

## Kryteria regresyjne
| ID | Odsyłacz | Metoda i kryterium |
|---|---|---|
| CAT-03-001 | cat:prop:hom-bifunctor | Python + semantyczna: kolejność składania w obu argumentach |
| CAT-03-002 | przeciwobraz i obraz | Python + semantyczna: właściwe wariancje |
| CAT-03-003 | cat:ex:tensor-bifunctor | Python + semantyczna: utrata moniczności po tensorze z Z/2 |
| CAT-03-004 | cat:ex:spec-functor | Python + semantyczna: kontrakcja ideałów pierwszych i przeciwobrazy bazowych otwartych w modelu skończonym |
| CAT-03-005 | cat:ex:homology-functor | Python + semantyczna: niezależność reprezentanta i składanie na ilorazie |
| CAT-03-006 | sec:funktory | Python: etykiety i środowiska |
| CAT-03-007 | cat:prop:faithful-reflect, cat:ex:functor-limits | semantyczna: zakres wniosków i kontrprzykłady |
| CAT-03-008 | cat:ex:derham-functor | semantyczna: typy cofnięć, reguła łańcuchowa, przejście do kohomologii |
| CAT-03-009 | potęgi symetryczne, składowe spójne, def:hom-funktory | semantyczna: identyczności, składanie i zgodność notacji |

Testy w tools/tests/test_category_theory_ch03.py (112ede03252d8cb9645b2e844ca35e80e7220f44), objęte istniejącym discovery CI. Nie potwierdzono jeszcze wykonania testów ani kompilacji. Nie wykonano formalizacji Lean. Stabilizacja otwarta, kolejny audyt bez rozszerzania zakresu.
