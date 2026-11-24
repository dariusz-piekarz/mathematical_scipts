# MA1-16 — trwałe kryteria regresyjne
Testy Python w dokładnej arytmetyce sprawdzają skończone świadki i oszacowania. Dowody graniczne pozostają przedmiotem audytu semantycznego.
| ID | Etykieta | Kryterium | Metoda |
|---|---|---|---|
| MA1-16-001 | ma1:def:uniform-continuity, ma1:thm:uniform-sequential | Kolejność kwantyfikatorów, oba kierunki, wspólne epsilon_0, brak wymogu zbieżności ciągów | semantyczna |
| MA1-16-002 | ma1:ex:square-not-uniform, ma1:ex:reciprocal-not-uniform | Dwie pary świadków, dokładne różnice, ograniczony przedział dla x^2 | semantyczna + Python |
| MA1-16-003 | ma1:thm:heine-cantor, ma1:cor:interval-uniform | Podciąg x_n, wspólna granica y_n w K, sprzeczność przez ciągłość | semantyczna |
| MA1-16-004 | ma1:lem:holder-powers | Jednoznaczność pierwiastków, potęgi wymierne, istnienie granicy po wykładniku, przypadki podstawy, ciągłość w zerze i dodatnich punktach | semantyczna + Python |
| MA1-16-005 | ma1:def:holder-lipschitz, ma1:thm:holder-uniform | Dopuszczalne wykładniki i C=0, ciągłość potęgi w zerze | semantyczna |
| MA1-16-006 | ma1:ex:sqrt-holder | Oszacowanie różnicy pierwiastków, nieograniczony iloraz Lipschitza | semantyczna + Python |
| MA1-16-007 | ma1:ex:uniform-no-holder | Zwartość ciągowa zbioru, izolacja punktów, ciągłość w zerze, dolne oszacowanie ilorazu dla każdego alpha | semantyczna + Python |
| MA1-16-008 | ma1:def:modulus-continuity, ma1:thm:modulus-uniform | Niepusty zbiór par, dopuszczalna nieskończoność, monotoniczność, epsilon/2 i obie implikacje | semantyczna |
| MA1-16-009 | ma1:ex:modulus-exact | Dokładny moduł pierwiastka i identyczności, przykład nieskończonego modułu dla t>=1 | semantyczna + Python |
| MA1-16-010 | ma1:thm:uniform-operations | Ograniczenie, złożenie, wspólny promień, ograniczoność czynników i mianownik oddalony od zera | semantyczna + Python |
| MA1-16-011 | ma1:thm:uniform-preserves-cauchy | Definicja Cauchy'ego, odwrotność fałszywa dla x^2 na R | semantyczna |
| MA1-16-012 | ma1:def:metric-closure | Domknięcie, kryterium ciągowe, domkniętość i przypadek pusty | semantyczna |
| MA1-16-013 | ma1:thm:uniform-extension | Zupełność Y, niezależność od ciągu, zgodność, delta/3 i epsilon/2, jednoznaczność, zachowanie stałej Höldera | semantyczna + Python |
| MA1-16-014 | ma1:ex:uniform-extension-incomplete, ma1:ex:dense-extension | Brak przedłużenia do niezupełnej przestrzeni, Q gęste w R i zachowanie stałej Lipschitza | semantyczna + Python |
