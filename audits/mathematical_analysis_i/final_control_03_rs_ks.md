# MA1 — audyt końcowy 03: Riemann–Stieltjes i podstawy Kurzweila–Stieltjesa

Punkt odniesienia: be0d71bc59d4de5b08e15fce6a2edb775517b1f9, CI 45635044207, job 139278110245. Wszystkie kroki SUCCESS; z logu 37 grup testów, łącznie 481 testów (32 dodatkowe testy rozdziału 36). PDF 276 i 281 stron w dwóch przebiegach. Drugi przebieg bez ostrzeżeń o niezdefiniowanych odsyłaczach, dwa ostrzeżenia Overfull 1.74243pt i 0.59775pt oraz informacja o zmianie etykiet. PDF nie został obejrzany w tej iteracji.

Kontrola szczegółowa: rozdziały 29, 30 i fragment RS rozdziału 36 (wersja 9f8f15f9fcdb7d8756042cce4f59c9ee8a76643b), podstawienia, granice KH oraz KS: definicja, kryterium Cauchy'ego, lokalność, lemat Saksa–Henstocka, funkcje regulowane, punktowy wzór i funkcje charakterystyczne przedziałów, integrator schodkowy. Sprawdzono również algebraiczną tożsamość korekty skokowej i jej przypadki brzegowe, nie cały dowód ogólnego twierdzenia o całkowaniu przez części.

Poprawki:
- a6639f4265c94fce60b2d3826b34062ae6b350f0: rozwinięcie implikacji (iii) => (ii) kryterium oscylacyjnego RS, przeliczalność punktów o dodatniej masie, jawna konstrukcja podziału omijającego je wewnątrz, uwzględnienie końców i oszacowanie miary D_r.
- 3410ec0d34c4f859cf1d076a758a757274396799: szczegółowe uzasadnienie rozkładu schodkowego integratora KS, przypadek przedziału jednopunktowego, znaki poprawek na obu końcach, korekty składu dwóch wzorów. Usunięcia ostrzeżeń składu nie potwierdzono kompilacją.
- Blob 041a496e812698f701c1628d1c4482cd4c093c6b: 2557 wierszy, 128 etykiet, brak duplikatów w rozdziale, zgodne pary środowisk LaTeX; jedyny odsyłacz poza rozdział ma etykietę ma1:thm:riemann-darboux-equivalence w rozdziale 29. Brak nowych tematów i zmian etykiet.

Aktualne CI 45635875214 dla 3410ec0d34c4f859cf1d076a758a757274396799: queued w chwili sprawdzenia. Nowych zmian nie uznawać za zwalidowane. Brak nowego testu regresyjnego i uruchomienia Lean. Następny etap: niezależna kontrola tych poprawek, szczegółowy audyt twierdzeń o istnieniu KS i kryteriów miarowych, kontrola aktualnych logów oraz PDF; w dalszej kolejności pozostałe fragmenty rozszerzonego rozdziału 36 i bramka całego tomu. Nie deklarować stabilizacji na podstawie poprzedniego CI.
