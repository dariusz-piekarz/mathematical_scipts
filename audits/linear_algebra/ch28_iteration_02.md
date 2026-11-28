# Algebra liniowa — rozdział 28, audyt II

**Data:** 21 listopada 2026  
**Zakres:** ponowny niezależny audyt sformułowań twierdzeń, pełności założeń i dowodów.

## Matematyka
- Wariacja stałych: sprawdzono rolę warunku początkowego, ciągłości wymuszenia i rozszerzenie na L¹ oraz właściwy sposób odczytania wyjścia z członem bezpośrednim.
- Modele dyskretne: przeanalizowano indeksowanie `CA^{k-1-j}B` i indeksy splotu; wszystkie przypadki brzegowe k=0 są poprawne.
- Laplace/Z: sprawdzono istnienie i obszary zbieżności transformat oraz tożsamości rezolwentowe z transformacją równania stanu.
- Funkcje wymierne: poprawnie odróżniono widmo A od biegunów G i podano kontrprzykład do implikacji odwrotnej.
- Realizacja skalarna: zastosowano kryterium PBH do p i q także dla wielokrotnych pierwiastków p; brak niejawnego założenia diagonalizowalności A. Przypadek q=0 wymaga i otrzymuje osobną interpretację.
- Szacunki: wykładniczy zanik e^{tA} i geometryczny zanik A^k wynikają z ujemnych części rzeczywistych lub promienia spektralnego <1; wykorzystano całkę/sumę szeregu geometrycznego.

## Wykryta nieprecyzyjność i poprawka
- **II.1:** Wniosek o równoważności parametrów Markowa dla dwóch realizacji pozostawiał niejawny rozmiar obu przestrzeni stanu. W sformułowaniu podano teraz niezależne wymiary n₁,n₂ oraz pełne rozmiary A_i,B_i,C_i,D_i; m,p≥1. Umożliwia to odwołanie się do realizacji o różnych wymiarach i odpowiada standardowi kwantyfikacji.
- Pozostałe sprawdzone tożsamości nie wymagały poprawki.

## Kontrola techniczna
- Pierwotny pełny workflow [44952985571](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44952985571) zakończony **SUCCESS**, PDF rozdziału miał 7 stron; wszystkie zostały obejrzane, nie stwierdzono ucięć ani bloków poza stroną.
- Poprawka audytu I ma osobną walidację w [workflow](https://github.com/dariusz-piekarz/mathematical_scipts/actions); po zmianie II.1 wymagana jest ponowna kontrola CI i nowego PDF.

## Decyzja
**Audyt II nie jest czysty** z uwagi na poprawkę II.1. Rozdział 28 pozostaje otwarty. Do stabilizacji potrzeba dwóch kolejnych czystych audytów na niezmienionym tekście, z zielonym CI i zweryfikowanym samodzielnym PDF.
