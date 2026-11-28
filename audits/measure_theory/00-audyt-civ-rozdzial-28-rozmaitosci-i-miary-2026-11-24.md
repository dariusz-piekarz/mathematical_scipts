# Audyt CIV (104) — wzór koobszaru na rozmaitościach i identyfikacja miar
Data: 2026-11-24. Gałąź biblioteka-matematyczna-iteracja-6.
Punkt startowy 85809abe3b88c4e0be24502744838593fca4eec2, blob ca5e9afea0b90d652f62eb3ca94afe5b2fa65f29.
Commit źródłowy 89afce9466400efb65ce08e9532664dffdbef0f3, blob a716d2068deb71a6a7502b3b286f425075ccbead.

## Uzupełnienia dowodów
- Wzór koobszaru na rozmaitościach sformułowano jako samodzielne twierdzenie z pełnymi hipotezami, dodatnim jakobianem, mierzalnością całki po włóknie, pustymi włóknami i przypadkiem n=m.
- Skonstruowano współrzędne dostosowane do submersji C^1 przez odwracalny minor i twierdzenie o odwzorowaniu odwrotnym. Wyprowadzono macierz sprzężenia B^{-1}L^T H i tożsamość wyznacznikową przez dopełnienie Schura, z osobnym przypadkiem pustego bloku.
- Uzasadniono miarę indukowaną na włóknach klasy C^1 z ciągłą metryką, niezależność od parametrów, zamianę zmiennych i zastosowanie Tonellego na borelowskich przestrzeniach euklidesowych. Rozłączny przeliczalny podział daje globalny wzór i mierzalność.
- W identyfikacji miary riemannowskiej z Hausdorffa usunięto nieuzasadnione odwołanie do krzywych minimalizujących. Porównanie lokalne obejmuje wszystkie krzywe, także opuszczające większą kulę współrzędnościową. Argument nie wymaga zupełności metryki ani istnienia geodezyjnej minimalizującej.
- Dla osadzonej podrozmaitości zastosowano mapę spłaszczającą i normę zamrożonej metryki na podprzestrzeni. Jawnie uzyskano dwustronne oszacowanie dla odległości zewnętrznej, porównanie wyznaczników metryk, izometrię z przestrzenią euklidesową i zastosowanie oszacowań Lipschitza dla miar Hausdorffa.
- Rozpisano przeliczalne rozłączne sklejenie lokalnych nierówności dla dowolnego epsilon, przypadki miar nieskończonych, k=0 oraz niespójnych rozmaitości. Równość miar sformułowano na zbiorach borelowskich.
- Rozdział 1587 -> 1859 wierszy (+272 netto); zachowano wszystkie 28 etykiet w tej samej kolejności. Sprawdzono odsyłacze do definicji miary riemannowskiej w 27 i kalibracji oraz oszacowania Lipschitza w 26. Nie zmieniano innych rozdziałów.

## Otwarte
Następna iteracja: niezależna kontrola rachunku blokowego, miar na włóknach C^1 i argumentu odległościowego, powrót do wcześniejszych sekcji celem sprawdzenia normalizacji, terminologii i brakujących uzasadnień. Przygotować regresje rozdziału i dedykowaną bramkę CI, potem rzeczywista kompilacja i oględziny PDF. W tej iteracji nie wykonano testów, kompilacji ani oględzin. Stan 27/31, rozdział 28 pozostaje nieustabilizowany. Nie przechodzić do 29. Bez rozszerzania zakresu.
