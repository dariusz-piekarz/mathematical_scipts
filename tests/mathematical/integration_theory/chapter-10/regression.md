# IT-10 — miary związane z całkowaniem: kryteria regresji

| ID | Etykieta / zakres | Kryterium | Metoda |
|---|---|---|---|
| IT-10-001 | it:thm:jordan-criterion | Równoważność zawartości, całkowalności charakterystyki i zerowości brzegu; końce przedziału | semantyczna |
| IT-10-002 | it:thm:jordan-criterion | Algebra na ustalonym przedziale, pierścień na R, kontrprzykład przeliczalnej sumy, miary wewnętrzne i zewnętrzne | semantyczna + Python |
| IT-10-003 | it:thm:stieltjes-construction | Przedmiara na pierścieniu, teleskopowanie, zwarte przybliżenia, ciągłość z góry, generowanie zbiorów borelowskich | semantyczna + Python |
| IT-10-004 | it:thm:stieltjes-construction | Jednoznaczność przez sigma-skończoność, konstrukcja odwrotna również dla u<0<=v, masa punktowa | semantyczna + Python |
| IT-10-005 | def:ac-measure-17, def:atom, thm:atomic-cont-singular-17 | Bezwzględna ciągłość i wariacja, przeliczalność atomów, argument z zagnieżdżonymi przedziałami | semantyczna |
| IT-10-006 | lem:integration-density-18 | Aproksymacja prosta, MCT, 0 razy nieskończoność, całkowalność ważonego modułu funkcji zespolonej | semantyczna + Python |
| IT-10-007 | it:thm:stieltjes-decomposition | Hipotezy rozkładu Lebesgue'a i Radona–Nikodyma, część atomowa i osobliwa ciągła, wzór dla modułu i funkcji ze znakiem | semantyczna + Python |
| IT-10-008 | ex:cantor-measure-17 | Mierzalność odwzorowania cyfrowego, masy cylindrów, brak atomów, osobliwość, dystrybuanta | semantyczna + Python |
| IT-10-009 | Momenty miary Cantora | Niezależność cyfr i drugi moment 3/8; zgodność całek dla ciągłej funkcji, nieistnienie RS dla charakterystyki | semantyczna + Python |
| IT-10-010 | st:ks-miara-konwencja | Miara kanoniczna na [a,b] a miara na (a,b], skoki jednostronne, impuls punktowy, utrata atomu w a po zmianie integratora | semantyczna + Python |
| IT-10-011 | def:hausdorff-measure-26, lem:hausdorff-outer-26 | Koszt dla s=0, pokrycia w przestrzeni nieośrodkowej, podaddytywność bez zamiany supremum z sumą | semantyczna |
| IT-10-012 | lem:hausdorff-metricity-26, lem:hausdorff-caratheodory-selfcontained-26, lem:hausdorff-metric-open-26 | Dodatnia odległość, kryterium Carathéodory'ego, zupełność, warstwy parzyste i nieparzyste | semantyczna |
| IT-10-013 | thm:hausdorff-borel-26, thm:hausdorff-line-26 | Mierzalność borelowska, równość miar zewnętrznych na R, otwarte pokrycia zbiorów średnicy zero | semantyczna + Python |
| IT-10-014 | lem:hausdorff-threshold-26, def:hausdorff-dimension-26 | Próg zerowania, konwencje dla pustego zbioru i nieskończonego wymiaru | semantyczna |
| IT-10-015 | thm:mass-distribution-26, thm:cantor-dimension-26 | Niemierzalne zbiory pokrycia, średnica zero, oszacowanie masy kul na wszystkich skalach i dodatnia skończona miara krytyczna | semantyczna + Python |
| IT-10-016 | it:cor:cantor-hausdorff | Skalowanie podobieństw, cylindry generujące B(K), jednoznaczność miar i wzór całkowy | semantyczna + Python |

Audyt 2026-11-25: commit b678296810e95af5dbbf57c65c102b8968c30970, blob 536937e3e0e5de5718ba7c8fe5277f7599914d40. Przeczytano całość rozdziału i sprawdzono powiązania z IT-02,03,06,11. Zachowano 23/23 etykiet, dodano 2; środowiska sparowane. Doprecyzowano algebrę/pierścień Jordana, miarę wewnętrzną i addytywność, konstrukcję Stieltjesa, masę punktową, gęstości zespolone, wzór całkowy dla rozkładu, dystrybuantę i momenty Cantora, miary na końcach przedziału oraz przejścia w dowodach Hausdorffa. Zachowano dowody metryczności, mierzalności Carathéodory'ego i wymiaru Cantora. Twierdzenia o rozszerzeniu przedmiary, rozkładzie Lebesgue'a i Radona–Nikodyma pozostają jawnie cytowanymi wynikami skryptu Teoria miary. Regresje: commit 70d2da301805bda5b2835eefa676781c1cb00e51, 7 metod, skończone świadectwa nie zastępują dowodów. CI po zmianach oraz wizualna kontrola PDF oczekują; Lean nieuruchamiany.
