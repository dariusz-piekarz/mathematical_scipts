# Audyt CVI (106) — CI, PDF i kontrola stabilizacyjna
Data: 2026-11-24. Gałąź biblioteka-matematyczna-iteracja-6.
Punkt startowy 86e9a92612d1b3738e2b44c0d394d0851a191e1c; rozdział bez zmian od CV do tego punktu.

## Weryfikacja rzeczywistego CI i artefaktu
Przebieg 45349873117, commit 59f1aab40bd03b97ef6e977d10ff3f606c3b2dc3: wszystkie trzy zadania zakończone sukcesem. Testy rozdziału 7/7, integralność tomu 4/4. Pełny tom 275 stron, izolowany rozdział 20 stron. Zaimportowano 9 odsyłaczy zewnętrznych, zachowano 28 lokalnych etykiet. Pobrano artefakt 14900160640 (7746433 bajtów), zweryfikowano SHA-256 8c1c19060b5126ac27b379682fcce9d8a42bcfd19275bbedaba211dbd426f549. Logi: rozdział 1 Overfull (5.84549 pt w akapicie 1678–1683), 0 Underfull; cały tom 1 Overfull i 13 Underfull. Brak nierozwiązanych lub wielokrotnie zdefiniowanych odsyłaczy; tekst PDF rozdziału nie zawiera znaków ??.
Wyrenderowano i obejrzano wszystkie 20 stron izolowanego rozdziału w pięciu arkuszach po cztery strony. Wzory, macierze, nagłówki i odsyłacze czytelne; nie zauważono nakładania, ucięcia ani brakujących glifów. Ostatnia strona zawiera końcową uwagę o dżetach i dużo wolnej przestrzeni. Oględziny nie obejmowały wszystkich stron całego tomu.

## Zmiany
Commit a143b2c727bb5553d87566373c8de2dd2952ab48, blob 353d8f3ac6b4aad885b33cc928c0d64e499e5e01: cztery zmiany. Rozbito akapit generujący Overfull, zdefiniowano funkcję b i jej przedłużenie przez zero oraz jawnie wskazano borelowskość całki po z. Rozpisano odwrócenie kongruencji blokowej i wskazano blok S^{-1}. Doprecyzowano hipotezy zastosowania wzoru dla immersji na części regularnej. Zachowano wszystkie 28 etykiet.
Ponownie sprawdzono argument dopełnienia Schura, niezależność gęstości od parametryzacji, porównanie odległości na podrozmaitościach i sklejenie nierówności miar. Brak nowej stwierdzonej luki w tych argumentach.

## Otwarte
Po zmianach potrzebny nowy przebieg CI, kontrola logów i ponowne oględziny PDF; usunięcia ostrzeżenia nie potwierdzono jeszcze kompilacją. Następnie niezależny audyt stabilizacyjny rozdziału. Stan 27/31, rozdział 28 nadal otwarty. Nie przechodzić do 29.
