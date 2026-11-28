# Topologia algebraiczna — TOP-11, audyty I–III (drugi cykl)

**Data:** 2026-11-21  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`; bez tworzenia nowej gałęzi i bez zmian w `main`.  
**Rozdział:** `chapters/pl/algebraic_topology/11-przeciecia-dualnosc-i-klasy-charakterystyczne.tex`.

## Zakres audytu

Przeczytano cały dotychczasowy rozdział: iloczyn kubkowy i kapowy, klasa fundamentalna, dualność Poincarégo i Poincarégo–Lefschetza, przecięcia i koorientacje, systemy lokalne, dualność Aleksandra, funkcje sklejające wiązek, klasy Stiefela–Whitneya, Thoma i Eulera, wzór Poincarégo–Hopfa, forma przecięcia i elementarna chirurgia. Nie dodano żadnych nowych twierdzeń, lematów ani bloków tematycznych.

## Audyt I: korekta w wymiarze zero

Wcześniejsze zdanie `u_E=e(E)=1` dla każdej **zorientowanej** wiązki rzędu zero nie było zgodne z przyjętą w książce konwencją orientowania punktów przez znak ±1. Poprawiono je: klasa Thoma, a wraz z nią klasa Eulera rzędu zero, jest lokalnie stałą funkcją znaków orientacji `ε`, i wynosi `1` dopiero przy standardowym wyborze orientacji włókna.

Odpowiednio poprawiono początek dowodu Poincarégo–Hopfa w wymiarze zero. Dla orientacji punktów `ε_x` mamy klasę fundamentalną będącą sumą `ε_x[x]`, a wartość klasy Eulera na punkcie to `ε_x`; ich parowanie daje sumę `ε_x²=1` po wszystkich punktach, czyli liczbę punktów i `χ(M)`. Zgodnie z konwencją wszystkie indeksy w wymiarze zero są równe `1`.

**Commit:** `c2dd887aa34ae8fda323cf559c3dbb88a6e07681`.

Do testów dodano 420 deterministycznych przypadków całkowitoliczbowych kontrolujących znak w formule brzegu iloczynu kapowego, dla wymiarów sympleksów 1–7 i wszystkich stopni, oraz osobny test wartości parowania w wymiarze zero dla rozmaitych orientacji.

**Commity testów:** `bdb8f0bcc989bf1ee642c3f208b9a165113dc145`, `b3b31b9ec990808cfaeddf1cf2e76c855e22a1ee`.

## Audyt II: samodzielność stwierdzeń i terminologia

Do stwierdzeń o regule Leibniza i przemienności stopniowanej dopisano dziedziny, współczynniki i kwantyfikatory. W twierdzeniu identyfikującym przecięcie z iloczynem kubkowym jawnie założono: zamkniętą zorientowaną rozmaitość `M`, dwie zamknięte zorientowane gładkie podrozmaitości bez brzegu o dopełniających się wymiarach, ich transwersalność, inkluzje i właściwą wersję dualności Poincarégo. Poprawiono terminologię: „skończone sumy małych kul” zamiast „skończone unie małych kul”.

**Commity:** `23f06c168782227a695868baf659a4730482f649`, `aaac4113aa5667eec0d40858975238de22fea202`.

## Audyt III: definicja chirurgii

W istniejącej definicji sprecyzowano, że `M^n` jest gładką rozmaitością, `n≥1`, a obramowane gładkie osadzenie `S^k×D^{n−k}` ma obraz we wnętrzu `M`. Tym samym operacja nie przecina niejawnie zewnętrznego brzegu `M`.

**Commit:** `9efc4de60ea8ab8844552baa58fa26a969524f06`.

## Kontrola źródła i CI

- Zachowano wszystkie 50 unikalnych etykiet rozdziału, bez kolizji. Kontrola strukturalna nie znalazła niedomkniętych środowisk TeX.
- Dla commita `bdb8f0bc` workflow kompilacji TOP-01–12 i testy aplikacji miały `completed/success`: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44926056252 i https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44926056253.
- Dla commita `c2dd887a` kompilacja TOP-11–12, testy aplikacji i kontrola zależności międzytomowych miały `completed/success`: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44926129232, https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44926129270, https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44926129230.
- Uruchomienia po późniejszych modyfikacjach pozostawały w toku podczas sporządzania raportu. Nie oznaczono jeszcze najnowszej wersji rozdziału jako stabilnej.

**Następny krok:** audyt IV niezależnie kontrolujący ostatni blob i końcowe CI. Po jego zamknięciu możliwe przejście do TOP-12. Automatyzacje nie zostały włączone.
