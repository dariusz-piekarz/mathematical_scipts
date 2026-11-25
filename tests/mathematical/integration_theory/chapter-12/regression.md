# IT-12 — całka Daniella–Stone'a: kryteria regresji

| ID | Zakres | Kryterium | Metoda |
|---|---|---|---|
| IT-12-001 | it:def:daniell-lattice, it:def:daniell-functional | Krata wektorowa, ograniczoność, obecność 1, dodatniość, ciągłość porządkowa | semantyczna |
| IT-12-002 | it:lem:daniell-monotone-extension | Niezależność przedłużenia od rosnącego ciągu, także dla nieskończonej granicy | semantyczna |
| IT-12-003 | it:lem:daniell-cover-domination | Reszty dodatnie maleją do zera, oszacowanie kosztu pokrycia | semantyczna + Python |
| IT-12-004 | it:def:daniell-outer, it:lem:daniell-outer | Aksjomaty miary zewnętrznej, skończona masa, minoranta funkcji charakterystycznej | semantyczna |
| IT-12-005 | it:lem:daniell-separated | Rozcięcie kosztu pokrycia za pomocą minimum, bez mnożenia dwóch funkcji z H | semantyczna + Python |
| IT-12-006 | it:lem:daniell-measurability | Warstwy parzyste i nieparzyste, zbieżność ogona bez założenia mierzalności, kryterium Carathéodory'ego | semantyczna + Python |
| IT-12-007 | it:lem:daniell-level | Masa poziomicy przez obcięcia, teleskopowe pokrycie, oba oszacowania | semantyczna + Python |
| IT-12-008 | it:thm:daniell-stone | Istnienie miary na sigma(H), dolne i górne sumy progowe, dokładny rozkład kratowy, funkcje ze znakiem i uzupełnienie | semantyczna + Python |
| IT-12-009 | it:thm:daniell-stone | Jednoznaczność na pi-układzie skończonych przecięć i równość masy całkowitej | semantyczna |
| IT-12-010 | it:cor:daniell-necessity, prz:daniel-koniecznosc | Konieczność ciągłości porządkowej, kontrprzykłady c i ewaluacji brzegowej | semantyczna + Python |
| IT-12-011 | prz:daniell-atoms | Miara atomowa, bezwzględna zbieżność, brak atomu w punkcie skupienia, przykład Riemanna i sigma(H) | semantyczna + Python |

Audyt I 2026-11-25: rozdział 12, pierwotny blob fc1f45fc995891b0051f802ac7690541873787b0. Commit b134769419f331e9187df23bb19e6a305dedf2bf, blob a4f718bf23e482099cc4bb7d0c1efed65df4b253. Wcześniej istnienie reprezentacji Daniella--Stone'a było przyjęte jako wynik zewnętrzny. Wprowadzono pełny dowód skończonej wersji twierdzenia: oszacowanie pokrycia z ciągłości porządkowej, miara zewnętrzna, rozdzielanie wartości przez obcięcia kratowe bez założenia algebry, mierzalność przez warstwy, masa poziomic przez teleskopowanie, aproksymacja całki z błędem delta I_0(1), jednoznaczność oraz konieczność ciągłości porządkowej. Korzystano z udowodnionego w IT-10 lematu Carathéodory'ego oraz twierdzeń IT-11; twierdzenie pi-lambda i Dini pozostają standardowymi przywołanymi wynikami. W tym samym commicie zmieniono status dowodów w IT-16. Rozdział 7894 -> 17107 znaków, 4/4 zachowane etykiety, 10 nowych, 13/13 różnych odsyłaczy ref/eqref z istniejącymi celami w IT-10,11,12, środowiska sparowane. Osiem testów w f4f03fd3d2dd92c3d77b981b016f3baa86b58df6; skończone świadectwa, nie dowody ogólne. CI 45642438127 i 45642530878 zakolejkowane w chwili kontroli, brak jeszcze potwierdzenia kompilacji i kontroli wizualnej. Lean nieuruchamiany. Następny etap: stabilizacja i niezależna kontrola matematyczna IT-12.
