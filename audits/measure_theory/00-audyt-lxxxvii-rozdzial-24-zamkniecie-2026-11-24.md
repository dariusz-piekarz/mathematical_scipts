# Audyt LXXXVII (87) — rozdział 24: zamknięcie stabilizacji

Data: 2026-11-24. Gałąź: biblioteka-matematyczna-iteracja-6.

## Wersja i CI
Aktualny blob 804aecc03ac472a5bff0582387883c5dcd46b1da zgodny z wersją źródłową sprawdzoną w przebiegu https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45295585052, commit regresji 179cdd135e44b87164d84b7627d1557da1ae5406. Oba statusy measure-theory/ch24-regressions i measure-theory/ch24-pdf: success.
Rzeczywiste logi jobów 138115904177 i 138115904667: 5 testów rozdziału i 4 testy integralności tomu zaliczone. Pełny tom 262 strony, 1920228 bajtów; samodzielny rozdział 7 stron, 299265 bajtów; 19 lokalnych etykiet, 0 potrzebnych zewnętrznych. Naprawiony warunek CI nie wymaga sztucznego odsyłacza.

## Kontrola rzeczywistych artefaktów
Pobrano ZIP 14876581838 (3764505 bajtów); rzeczywiście obliczono SHA256 f4e6838ff7b9a2667d930fadcc7c14c6ea22342a70684c0103b67ac91cd8d519, zgodny z metadanymi GitHub. Rozpakowano oba PDF, oba logi i siedem obrazów CI. Niezależnie wyrenderowano wszystkie siedem stron samodzielnego rozdziału przez PyMuPDF i obejrzano wszystkie cztery pary/arkusze podglądu.
- Strony 1–2: definicje, 5r i rysunek; etykiety czytelne, okręgi nie nachodzą na napisy, skala 5:1 i geometria zgodne ze źródłem.
- Strony 3–4: dowód Vitaliego (skończony i nieskończony), przypadki wyjątkowe i lemat kątowy; wzory czytelne, nieucięte.
- Strony 5–6: trzy kroki wieloskalowego dowodu Besicovitcha i funkcja maksymalna; prawidłowy skład i numeracja.
- Strona 7: wniosek o skończoności prawie wszędzie i przejście do następnego rozdziału; krótsza strona końcowa, bez usterki.
Odczyt tekstu: 0 wystąpień ?? na każdej stronie rozdziału. Log samodzielnego PDF: 0 Overfull, 0 Underfull, 0 ostrzeżeń o nierozwiązanych odsyłaczach. Log pełnego tomu: 0 Overfull, 14 Underfull, 0 ostrzeżeń o nierozwiązanych odsyłaczach. Nie oglądano wszystkich 262 stron tomu.

## Końcowy przegląd
Potwierdzono zachowanie poprawek LXXXIV–LXXXV: rozdzielenie przypadków skończonego i nieskończonego wyboru w Vitalim, definicja zbioru wyjątkowego, rozdzielenie skal, oszacowanie kątowe, zbieżność zdominowana w dowodzie ciągłości średnich. W poprzednim audycie LXXXVI wykonano 4096 konfiguracji 2D i 1806336 punktowych kontroli krotności; nie zastępują one dowodów ogólnych. Brak nowych usterek wymagających modyfikacji. Źródło niezmienione w tej iteracji.

## Werdykt
Rozdział 24 ustabilizowany w zakresie audytów LXXXIV–LXXXVII, testów i składu. Stan 24/31. Następny audyt LXXXVIII: pierwszy przegląd rozdziału 25 — różniczkowanie całek i miar.
