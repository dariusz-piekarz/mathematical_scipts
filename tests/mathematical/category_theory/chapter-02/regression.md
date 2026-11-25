# CAT-02 — pierwszy audyt i trwałe kryteria regresyjne

Źródło: chapters/pl/category_theory/02-izomorfizmy-monomorfizmy-i-epimorfizmy.tex. Commit 318e548ec9a87c803b7aaa8efd04de7e66748b9b, blob 189e58009836c8077788f3e5530e71f8c548c6cd.

## Wykonane zmiany
- Reguły skracania, domknięcie monomorfizmów i epimorfizmów na składanie, kryteria izomorfizmu z odwrotnością jednostronną, pojęcie bimorfizmu.
- Dowód surjektywności epimorfizmów grup przez dwa działania na H×{0,1}, bez założenia normalności obrazu.
- Charakterystyka mono- i epimorfizmów modułów nad dowolnym pierścieniem z jedynką, zrównoważenie.
- Kontrprzykłady topologiczne i różniczkowe, lokalizacja jako epimorfizm, regularne mono- i epimorfizmy wraz z dowodami i przykładami Set.
- Zachowano istniejące etykiety; włożenie zastąpiono zanurzeniem; dopisano bezpośredni dowód dla rozszczepionych epimorfizmów.
- Odsyłacz do sec:equalizatory zweryfikowano w CAT-07.

## Wykorzystanie wcześniejszych skryptów
AA-16 (319cbac9af83a819e0d375fc282284c62638c3ac): homomorfizmy i ilorazy modułów, raport stabilizacji istnieje. AA-12 (f64ec91a7fcc58557dba8b13f75b74f6b2ca788d): własność uniwersalna lokalizacji; AA-09 (c6a5ac5d6f8f067a051c49860eae815915bff7d0): homomorfizmy pierścieni, kontekst. DG-01 (8636e1a7477d6130b0387d71ec24bd1ec290e5ab): gładkie odwzorowania. Sprawdzono również GT-01, bez bezpośredniego importu. Nie kopiowano całych dowodów ze źródeł; użyto istniejących konstrukcji w nowym kontekście. Nie potwierdzano odrębnego CI wszystkich źródeł.

## Kryteria
| ID | Odsyłacz | Metoda i kryterium |
|---|---|---|
| CAT-02-001 | cat:thm:epi-grp | Python + semantyczna: świadkowie nieepiczności dla właściwych podgrup, także nienormalnych |
| CAT-02-002 | cat:def:regularne, cat:prop:bimorfizm-rozszczepiony | Python + semantyczna: jednoznaczne faktoryzacje w Set, puste zbiory, odwrotności jednostronne |
| CAT-02-003 | cat:ex:mono-epi-top | Python + semantyczna: bijekcja ciągła bez ciągłej odwrotności |
| CAT-02-004 | cat:thm:mono-epi-mod | Python + semantyczna: iloraz przez obraz wykrywa brak surjektywności |
| CAT-02-005 | sec:morfizmy | Python: etykiety i środowiska |
| CAT-02-006 | cat:ex:epi-lokalizacja | semantyczna: jednoznaczność przedłużenia, bez iniektywności |
| CAT-02-007 | cat:prop:skracanie, cat:prop:regularne-mono-epi | semantyczna: typy i kierunki skracania |
| CAT-02-008 | przykład gładkiej bijekcji | semantyczna: brak różniczkowalności odwrotności w zerze |

Testy automatyczne w tools/tests/test_category_theory_ch02.py (9811216fa141e8a0bbf618fc64af1cda35420147), istniejący workflow discovery obejmuje nowy plik. Sprawdzono zagnieżdżenie środowisk przy zapisie; wynik uruchomienia CI wymaga potwierdzenia. Nie wykonano formalizacji Lean. Stabilizacja otwarta; następny audyt bez rozszerzeń.
