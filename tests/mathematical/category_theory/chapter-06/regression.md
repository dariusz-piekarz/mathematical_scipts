# CAT-06 — audyt I i trwałe kryteria regresyjne

Źródło chapters/pl/category_theory/06-iloczyny-koprodukty-i-konstrukcje-uniwersalne.tex, commit 14552777d914bf4e907819d5e7c5c70f86146ec5, blob d080944ade403fc3ee859b37547611610ff150ca.

## Zmiany
- Rozpisano własność uniwersalną iloczynu grup i przestrzeni topologicznych, jednoznaczność koproduktu i przenoszenie własności przez izomorfizm.
- Zamiast intuicyjnego opisu iloczynu wolnego podano konstrukcję z grupy wolnej na oznaczonych elementach czynników przez normalne domknięcie relacji mnożenia; dowiedziono własności uniwersalnej i iniektywności zanurzeń. Kontrprzykład do iloczynu prostego wykorzystuje dwie niekomutujące transpozycje S3.
- Zdefiniowano iloczyny i koprodukty rodzin indeksowanych dowolnym zbiorem oraz naturalne bijekcje Hom, z przypadkiem pustym i uwagą o aksjomacie wyboru.
- Udowodniono własności uniwersalne konstrukcji w Set, Grp, Top, modułach i grupach abelowych. Rozróżniono sumę prostą i iloczyn prosty nieskończonej rodziny, także na przykładzie różnej mocy grup.
- Udowodniono funktorialność wybranych iloczynów i koproduktów, naturalność kanonicznych izomorfizmów łączności, symetrii i jednostki. Nie deklarowano jeszcze pełnego zestawu aksjomatów kategorii monoidalnej.
- Skonstruowano kanoniczne porównanie koproduktu z iloczynem w kategorii z obiektem zerowym i wykazano, że w Grp nie musi być izomorfizmem.
- Zachowano dotychczasowe etykiety, zastąpiono termin „włożenie” terminem „zanurzenie”, sprawdzono stos środowisk.

## Wykorzystanie źródeł
- AA-06 e504d9d70bc66e0307c466e4be1a0fb2d33dfe30: konstrukcja iloczynu prostego grup.
- AA-07 931eb83323a543e55cc9e4c439ab864111d65264: własność uniwersalna grupy wolnej (aa:def:free-universal) i prezentacje; konstrukcję koproduktu dopisano w CAT.
- AA-08 d6de6b6cb0e01449c8f976b662960cd0425abd90: aa:def:abelian-directsum, aa:lem:abelian-sum-product, przykład różnej mocy.
- AA-16 319cbac9af83a819e0d375fc282284c62638c3ac: aa:def:modules-direct-sum; wykorzystano konstrukcję i dopisano własności kategorialne.
- GT-04 a7c1dac3b2f9dcc709a6f47bc4566d9740ef2081: def:topog-iloczyn, thm:topog-iloczyn-baza; wykorzystano podbazę.
- AA-18 sprawdzono pod kątem istniejącego przykładu tensorowego; nie powielano dowodów istnienia tensoru. Nie potwierdzano w tej iteracji odrębnych przebiegów CI źródeł.

## Kryteria regresyjne
| ID | Odsyłacz | Metoda i kryterium |
|---|---|---|
| CAT-06-001 | def:produkt | Python + semantyczna: bijekcja Hom dla zbiorów skończonych, w tym pustych |
| CAT-06-002 | def:koprodukt | Python + semantyczna: jednoznaczność i istnienie sklejenia funkcji |
| CAT-06-003 | cat:prop:product-functor | Python + semantyczna: składanie morfizmów iloczynowych i koproduktowych |
| CAT-06-004 | cat:prop:coprod-product | Python + semantyczna: nieprzemienność transpozycji i niezerowy komutator |
| CAT-06-005 | przykład biproduktu | Python + semantyczna: relacje rzutów i zanurzeń nad F2 |
| CAT-06-006 | cat:prop:product-coherence | Python + semantyczna: naturalność zmiany nawiasowania |
| CAT-06-007 | sec:produkty | Python: etykiety i środowiska |
| CAT-06-008 | tw:produkt-unique | semantyczna: jednoznaczność porównań i transport przez izomorfizm |
| CAT-06-009 | przykład iloczynu wolnego | semantyczna: normalne domknięcie relacji, faktoryzacja, zanurzenia |
| CAT-06-010 | cat:def:indexed-products, cat:ex:indexed-set-top | semantyczna: naturalność Hom, rodzina pusta, ciągłość i wybór |
| CAT-06-011 | cat:ex:module-indexed | semantyczna: skończony nośnik, suma, argument przekątniowy |
| CAT-06-012 | cat:prop:product-coherence, cat:prop:coprod-product | semantyczna: jednostka, symetria, naturalność i porównanie z użyciem zer |

Testy tools/tests/test_category_theory_ch06.py, commit 94899205a11064f1db6b4672fd0dc2dc7530862f; istniejący workflow discovery obejmuje plik. Wykonania nowych testów i kompilacji nie potwierdzono. Nie wykonano formalizacji Lean.

Status otwarty: kolejna iteracja stabilizacyjna bez rozszerzania zakresu.
