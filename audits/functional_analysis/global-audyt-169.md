# Audyt globalny 169 — spójność między rozdziałami

Kontynuacja audytu 168. Wyłącznie gałąź biblioteka-matematyczna-iteracja-6.

## Kontrola
Przed zmianą porównano commit pełnego CI 05b52d96968ea7af5bf5ec69e1f8f139e597377f z fab4a0b987c530de419a3511ef19bd4cc9030834: w zakresie analizy funkcjonalnej tylko raporty 167 i 168. CI 45588182885 potwierdzony, wszystkie kroki success, 440 metod w 36 plikach, 278 stron (wyniki odczytane w audycie 168).

Przeprowadzono ukierunkowaną kontrolę źródeł 06,08,12–16 (z 15A/15B),17,20–25,26–33. Sprawdzono konwencje przestrzeni sprzężonej i zanurzenia kanonicznego, liniowość iloczynu skalarnego i antyliniowość drugiego argumentu w 13,16,32,33, miary w całkach (wybrane wystąpienia), normalizację Fouriera i znaki pochodnych w 17,22,23,33, czynnik splotu w 17 i odsyłacze do twierdzenia o jądrze w 23–25 oraz związki teorii operatorów zwartych, Fredholma, algebr Banacha i rachunku spektralnego w 28–33. Nie jest to ponowna weryfikacja wszystkich dowodów ani pełny przegląd wszystkich oznaczeń.

## Wykryta niespójność i poprawka
Rozdział 31 definiował R_a(z)=(z1_A-a)^(-1), podczas gdy rozdział 33 nazywał rezolwentą R(z,A)=(A-zI)^(-1). Obie konwencje poprawne osobno, ale różnią się znakiem tożsamości rezolwenty. Ujednolicono trzy bloki rozdziału 33: definicja R_A(z)=(zI-A)^(-1) z odsyłaczem do def:spectrum31; jawna zależność (A-zI)^(-1)=-R_A(z); wzór R_A(z)=integral (z-t)^(-1)dE(t), obok dotychczasowego wzoru na odwrotność A-zI. Oszacowania normowe, dowody Cayleya i Stone'a oraz dziedziny nie zmienione. Commit 7bf9a81703c2ba9ebb349e7803e873aff020440d, blob c7b87ea750505fc5d72f5d141678d2c10f63b1c0. Zachowano 15 etykiet, odsyłaczy w 33 jest teraz 16, cel nowego odsyłacza zweryfikowano w 31.

Dodano trwałą metodę FA33_resolvent_convention_03 (048c8223f7caaa72e7beb995a0ac5464067de9d2, blob 9a8b90e99e90a78e522057a239871d3831c5ce43). 10 metod w pliku rozdziału 33. Test sprawdza zgodność źródeł oraz skalarną tożsamość rezolwenty w arytmetyce wymiernej. Niezależnie wykonano 14400 przypadków skalarnych w JS, sprawdzając tożsamość po sprowadzeniu do wspólnego mianownika i przeciwny znak odwrotności; wszystkie poprawne. Nie stanowi to dowodu ogólnego ani Lean.

## Status
CI pełnej książki 45589017223 (źródło), 45589041822 (źródło i test), CI rozdziału 33 45589016907 i 45589041703 oraz CI kontekstu 31/32 w toku przy odczycie. Nie przypisano wyniku PASS nowemu testowi ani nowej kompilacji. PDF 278 stron z audytu 168 dotyczy poprzedniej wersji i nie może być nazwany finalnym po tej poprawce. Nie wykonywano nowej kontroli wizualnej ani Lean.

## Decyzja
Nie zamykać jeszcze książki. Audyt 170: sprawdzić najnowsze CI, regresję konwencji, pobrać nowy PDF, porównać z poprzednim na wszystkich stronach i obejrzeć zmienione strony; następnie kontrola poprawionych fragmentów 33 i ponowna kontrola spójności przed formalnym zamknięciem. Nie resetuje się audytów pozostałych rozdziałów z powodu lokalnej zmiany konwencji, ale konieczna jest ponowna kontrola poprawionego rozdziału i bramki globalnej.
