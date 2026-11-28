# Audyt LXXXVI (86) — rozdział 24: kontrola geometryczna 2D i częściowa kontrola PDF

Data: 2026-11-24. Gałąź: biblioteka-matematyczna-iteracja-6.
Aktualny blob 804aecc03ac472a5bff0582387883c5dcd46b1da. Bez zmiany źródła w tej iteracji.

## Niezależne obliczenia
Wykonano rzeczywiście w JavaScript dokładne obliczenia na wektorach całkowitoliczbowych w R^2:
- 3160 nieuporządkowanych par 80 niezerowych wektorów z siatki [-4,4]^2; 1924 pary spełniają warunek kwadratu odległości większego od obu kwadratów norm. Dla wszystkich tych par sprawdzono nierówność kątową przez porównanie całkowitoliczbowe (gdy iloczyn skalarny jest nieujemny, cztery jego kwadraty są mniejsze od iloczynu kwadratów norm).
- 4096 przyporządkowań promieni 1,2,4,8 do sześciu różnych środków w R^2; sprawdzono pokrycie środków, 880 par między skalami, krotność pojedynczej skali <=25, liczbę aktywnych skal <=9 i krotność <=225 w 1806336 punktach kontrolnych (siatka całkowita [-10,10]^2 dla każdej konfiguracji).
- Wszystkie kontrole przeszły; zaobserwowana maksymalna krotność 6 nie jest optymalną stałą ani dowodem ogólnego twierdzenia. Siatka nie obejmuje wszystkich punktów płaszczyzny.

## PDF i CI
Najnowszy przebieg https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45295585052 dla 179cdd135e44b87164d84b7627d1557da1ae5406 przy ostatniej kontroli jeszcze bez konkluzji: testy queued, PDF in_progress. Nie poświadczono jego wyników.
Pobrano rzeczywisty artefakt 14875756638 starszego przebiegu 45294581904: SHA256 707debbc920b65bf82417d1610ceac1d712573e85f8ca2ae30fb4182f1071b11 zgodny z metadanymi; ZIP zawiera pełny PDF (262 strony) i log. Wyrenderowano fizyczne strony 179 i 180, obejrzano stronę 180 (drukowana 169) z rysunkiem 5r. Etykiety D, B, D', 5D, 5D' czytelne, nie nachodzą na okręgi; rzeczywiste proporcje promieni i zawieranie zgodne z podpisem. Kod TikZ rysunku identyczny w starszym i aktualnym źródle: true. Oględziny dotyczą starszego składu pełnego tomu, nie nowego PDF izolowanego.

## Werdykt
23/31 rozdziałów ustabilizowanych. Nie zamykać 24 przed aktualnym CI 5+4, pełnym i izolowanym PDF i oględzinami wszystkich stron najnowszego rozdziału. Następny audyt LXXXVII: zamknięcie bramki, jeżeli wyniki pozwolą.
