# IT-09 — szeroka całka Denjoya: kryteria regresji

| ID | Etykieta / zakres | Kryterium | Metoda |
|---|---|---|---|
| IT-09-001 | it:def:approx-derivative, it:lem:approx-derivative | Mierzalność złych ilorazów, gęstość zero, jednoznaczność, liniowość | semantyczna + Python |
| IT-09-002 | it:def:denjoy-broad | AC(E), domknięte pokrycie, skończone wartości, przypadek jednopunktowy | semantyczna |
| IT-09-003 | it:lem:ac-affine-extension | Przedłużenie dla pustego i jednopunktowego E, ciągłość, sumowalność przyrostów w lukach, AC | semantyczna + Python |
| IT-09-004 | it:lem:ac-affine-extension | Oszacowanie miary zewnętrznej obrazu przez całkę modułu pochodnej, regularność i rozkład otwartego pokrycia | semantyczna |
| IT-09-005 | it:thm:acg-uniqueness | Punkty gęstości, kontrola złych ilorazów przez dopełnienie E_n, mierzalność reprezentanta | semantyczna + Python |
| IT-09-006 | it:thm:acg-uniqueness | Zerowa pochodna aproksymatywna, zerowa miara obrazów zwartych E_n, ciągłość i jednoznaczność modulo stałą | semantyczna |
| IT-09-007 | it:ex:broad-denjoy-strict | Ciągłość funkcji w lukach Cantora; domknięte pokrycie ACG; Baire i wybór przedziału podstawowego, suma oscylacji i malejące długości | semantyczna + Python |
| IT-09-008 | it:ex:broad-denjoy-strict, prz:ac-kontra-acstar | Ścisła inkluzja HK, jednoznaczność ACG, rozbieżność całki modułu pochodnej | semantyczna + Python |
| IT-09-009 | tw:denjoy-szeroka-ftc, st:denjoy-szeroka-lokalnosc | Ograniczanie, sklejanie z przesunięciem o stałą, pochodna poza zbiorem wyjątkowym i c | semantyczna + Python |
| IT-09-010 | it:cor:acg-bv | Własność Luzina (N) dla dowolnego zbioru zerowego; ACG∩BV=AC; wariacja i L1 | semantyczna |

Audyt (2026-11-25): commit f86e3267204fd9f8874347c8cf1189d5df81c11e, blob 9fbd4468a05dfb196475da47c2b71452057ae878. Przeczytano cały rozdział, uzupełniono definicję pochodnej aproksymatywnej, przypadki zdegenerowane, argument gęstości, mierzalności i jednoznaczności, liniowość ACG, ciągłość i argument Baire'a w przykładzie Cantora, sklejanie z przesunięciem i kontrolę wyjątków. Zachowano 7/7 dawnych etykiet, dodano trzy; środowiska sparowane. Sprawdzono cele nowych odsyłaczy do IT-05,08,11. Testy: commit a1be1ce4e0173caf1842da699cdc425967f1d4b4 (5 metod; świadkowie skończeni, nie dowody ogólne). CI po zmianach, kontrola PDF i formalizacja Lean niepotwierdzone. Następny etap: kontrola stabilizacyjna, w tym ponowne sprawdzenie dowodu inkluzji właściwej.
