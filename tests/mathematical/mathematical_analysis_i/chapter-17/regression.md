# MA1-17 — trwałe kryteria regresyjne
Testy Python sprawdzają skończone świadki i tożsamości w dokładnej arytmetyce. Nie zastępują dowodów granicznych ani twierdzeń o przeliczalności.
| ID | Etykieta | Kryterium | Metoda |
|---|---|---|---|
| MA1-17-001 | ma1:def:monotone-function, ma1:ex:monotone-basic | Cztery rodzaje monotoniczności, negacja, przykład kwadratu i podłogi | semantyczna + Python |
| MA1-17-002 | ma1:thm:monotone-one-sided | Niepuste części dziedziny, supremum i infimum, granice skończone i niewłaściwe, właściwe kierunki | semantyczna |
| MA1-17-003 | ma1:cor:monotone-interior-limits | Skończoność, nierówności, kryterium ciągłości, końce i singleton | semantyczna + Python (świadki stron) |
| MA1-17-004 | ma1:thm:monotone-at-infinity | Nieograniczoność dziedziny, progi, redukcja przez g(t)=-f(-t) | semantyczna |
| MA1-17-005 | ma1:def:discontinuity-types, ma1:ex:monotone-jump | Usuwalna, skokowa, drugiego rodzaju; dla monotonicznej wewnątrz tylko skoki; c w [0,1] | semantyczna + Python |
| MA1-17-006 | ma1:lem:disjoint-jump-intervals | Środkowy punkt przedziału, rozłączność otwartych przedziałów skoków | semantyczna + Python |
| MA1-17-007 | ma1:thm:monotone-countable-discontinuities | Wybór najmniejszego indeksu wymiernego, iniekcja, co najwyżej dwa końce | semantyczna |
| MA1-17-008 | ma1:thm:finite-large-jumps | Sumowanie skoków, teleskopowanie, oszacowanie liczności | semantyczna + Python |
| MA1-17-009 | ma1:ex:dense-monotone-jumps | Zbieżność szeregu, monotoniczność, dolne ograniczenie skoku w r_k | semantyczna + Python |
| MA1-17-010 | ma1:ex:dense-monotone-jumps | Ogon 2^(-N), promień od skończonej liczby punktów, ciągłość poza Q i na końcach | semantyczna + Python |
| MA1-17-011 | ma1:def:darboux-property, ma1:thm:monotone-darboux-continuity | Obie implikacje, rozdzielenie dwóch luk, końce i singleton | semantyczna |
| MA1-17-012 | ma1:thm:strict-monotone-inverse | Iniekcja, monotoniczność odwrotności, dobór a,b i dodatniego promienia, brak stron, negacja | semantyczna + Python |
| MA1-17-013 | ma1:ex:inverse-of-jump | Rozłączny obraz, poprawna odwrotność, względna ciągłość przy 1 | semantyczna + Python |
| MA1-17-014 | ma1:thm:continuous-injective-monotone | Wartość środkowa między skrajnymi, sprzeczność z iniekcją, uporządkowanie czterech punktów | semantyczna |
| MA1-17-015 | ma1:cor:monotone-homeomorphism | Obraz przedziałem, ścisła monotoniczność, ciągła odwrotność | semantyczna |
| MA1-17-016 | ma1:ex:dense-monotone-jumps | Ciągłość szeregu po wyłączeniu k-tego składnika w r_k, dokładny skok 2^(-k), ciągłość prawostronna i suma skoków 1 | semantyczna + Python (test_exact_jump_and_right_continuity) |
