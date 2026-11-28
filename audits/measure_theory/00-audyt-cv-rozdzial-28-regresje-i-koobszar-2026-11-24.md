# Audyt CV (105) — koobszar, mierzalność i bramka regresji
Data: 2026-11-24. Gałąź biblioteka-matematyczna-iteracja-6.
Punkt startowy 24e9ac9bf054553e825f4a02b7bfc7bc1dd63751. Źródło 76708a29be0691c23e8a2a9e0976cb5ab41c16fa; regresje 0c3e2d70bb5c8f5874943a8758994b3f2cadae41; workflow 59f1aab40bd03b97ef6e977d10ff3f606c3b2dc3.

## Kontrola matematyczna
- Ponownie sprawdzono tożsamość blokową z CIV, macierz sprzężenia, przypadek pustego bloku, zgodność kalibracji Hausdorffa z rozdziałem 26. Porównanie odległości obejmuje krzywe opuszczające otoczenie, bez założenia zupełności.
- Dziewięć zmian źródła: borelowskość funkcji na obrazach immersji i jawna zbieżność monotoniczna; pełny dowód euklidesowego koobszaru dla równych wymiarów; odwracalny minor, współrzędne włóknowe, sprawdzenie rangi parametryzacji, mierzalność całki przez Tonellego na sigma-skończonych miarach borelowskich; rozłączny podział oraz funkcje ze znakiem i zespolone. Rozróżniono istnienie gęstości i zastosowanie twierdzenia Radona–Nikodyma przy sigma-skończoności.
- Wszystkie 28 etykiet zachowane w tej samej kolejności.

## Regresje i CI
Dodano 7 testów: etykiety, rachunek Grama, jakobian z niediagonalnymi metrykami i dopełnieniem Schura, przypadek równych wymiarów, niedostateczna ranga, skalowanie pokryć krytycznych oraz kontrola wybranych uzasadnień w źródle.
Dedykowany workflow oparto na działającym workflow rozdziału 27, z kompilacją całego tomu, importem zweryfikowanych odsyłaczy i izolowanym PDF rozdziału 28, podglądami wszystkich stron i publikacją statusów. Wyniki nowej bramki nie są jeszcze potwierdzone. Testy są regresjami skończonych modeli, nie formalną weryfikacją twierdzeń.
## Otwarte
Sprawdzić rzeczywisty wynik CI, logi, artefakt i wszystkie strony PDF. Niezależny audyt stabilizacyjny nowych dowodów i ewentualnych ostrzeżeń. Rozdział 28 nadal nieustabilizowany; stan 27/31. Nie przechodzić do 29.
