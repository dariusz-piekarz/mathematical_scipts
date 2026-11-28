# IT-05 — całka Perrona: kryteria regresji

| ID | Etykieta / zakres | Kryterium | Metoda |
|---|---|---|---|
| IT-05-001 | it:def:perron, it:lem:perron-order | Niepuste rodziny; porządek kresów; monotoniczność z dolnej pochodnej Diniego; końce | semantyczna |
| IT-05-002 | it:thm:perron-hk, st:perron-sumy | Oba znaki mianownika; znaczniki na końcach; sumowanie teleskopowe | semantyczna + Python |
| IT-05-003 | it:lem:perron-null-correction | Przedłużenie afiniczne; oszacowanie R; obie obwiednie w luce, ciągłość i masa; luki brzegowe | semantyczna + Python |
| IT-05-004 | it:lem:perron-null-correction | Skończona suma oscylacji, bezatomowość, regularność uzupełnionej miary, budżet szeregu korekt | semantyczna + Python |
| IT-05-005 | it:thm:perron-hk | HK => Perron: ACG_*, pochodna p.w., korekta punktowa także na końcach | semantyczna + Python |
| IT-05-006 | Odtwarzanie pochodnej | Ciągłość F na domkniętym przedziale wystarcza; dowolne skończone wartości f na końcach | semantyczna |
| IT-05-007 | Przykład Dirichleta | Istnienie przed użyciem symbolu całki; ściskanie dwóch kresów do zera | semantyczna |
| IT-05-008 | tw:perron-wyjatki, wn:perron-kawalkami | Kontrola siecznych; jawna globalna stała Lipschitza; dowolne wartości na punktach podziału | semantyczna + Python |

Audyt: commit 99e94bd15ed3826d923c51128cf68c7e8a43823f, blob cd9ce349de276d4b54ff76b1454bbc9306c5ae84. Zachowano 6/6 dawnych etykiet i dodano dwie; pary środowisk sprawdzone. Skontrolowano główną konstrukcję HK => Perron z zależnościami w IT-08 i IT-11; zachowano dowód z miarami kontrolującymi przyrosty. Rozpisano znaki w implikacji przeciwnej, wzmocniono odtwarzanie pochodnej na końcach zgodnie z IT-04, jawnie wykazano istnienie całki w przykładzie Dirichleta, sprecyzowano kawałkami C^1 i kontrolę Lipschitza. Testy (5 metod): 789082ab0dbda7c39abef583f9ca0143a060cf36; wykonanie i CI po zmianach jeszcze niepotwierdzone. Poprzedni CI 45623034829: 29/29, dwie kompilacje, 131 stron; nie dotyczy nowych zmian. Nie przeprowadzono kontroli wizualnej PDF ani Lean.
