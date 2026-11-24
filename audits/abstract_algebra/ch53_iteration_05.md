# AA-53 — audyt V: ogólny wzór Moliena i spójność odsyłaczy

Data: 24 listopada 2026 r. Gałąź biblioteka-matematyczna-iteracja-6.
Źródło: blob 5675bf04c336a76e6424eeca337f24b5f211aeb5, bez zmian.

## Kontrola matematyczna i spójność
Ponownie sprawdzono, że ślad działania na wielomianach dotyczy wartości własnych g^(-1), a wzór z g wynika z bijekcji inwersji na całej grupie, nie z równości pojedynczych śladów. Jest to istotne poza SL2. Przypadki m=1 oraz stopień d=0 są poprawne. Odczytano AA-52 i AA-53: wszystkie 6 wystąpień odsyłaczy AA-53 (5 różnych celów) ma dokładnie jedną odpowiadającą etykietę w tych plikach. Nie stwierdzono potrzeby zmian źródła.

## Wykonany niezależny test
JavaScript, dokładna arytmetyka BigInt. Dla m=1,...,12 i trzech reprezentacji diagonalnych C_m o wagach (1,2,3), (1,-1,0), (1,1,1) rozwinięto iloczyn trzech formalnych szeregów geometrycznych do stopnia 40 w pierścieniu grupowym Z[C_m], tzn. tablice współczynników indeksowane stopniem i klasą reszty modulo m. Współczynnik klasy zerowej odpowiada uśrednieniu po pierwiastkach jedności. Obliczenie wykonano oddzielnie dla wag dodatnich i odwróconych; oba wyniki porównano z bezpośrednią enumeracją wszystkich trójek wykładników o sumie d i zerowej sumie ważonej modulo m. 1476/1476 przypadków poprawnych, w tym 738 przypadków dla reprezentacji o nietrywialnym wyznaczniku. Nie przypisujemy testowi skończonemu statusu dowodu ogólnego.

## CI
Run 45348236656, job 138287946248, head 3d9d4373b9a1c3e369394912a6dbdf27c752ee7d. Stan in_progress, conclusion brak, kroki {"success":11,"in_progress":1,"pending":103}. Dostępne artefakty: brak. Oględziny PDF w tej iteracji nie zostały wykonane.

## Werdykt
Trzeci czysty przegląd matematyczny po II. AA-53 pozostaje W AUDYCIE, do potwierdzenia pełnego CI i obejrzenia aktualnego PDF. AA-54 nieotwarty. Nie zmieniano źródła, workflow ani innych rozdziałów.
