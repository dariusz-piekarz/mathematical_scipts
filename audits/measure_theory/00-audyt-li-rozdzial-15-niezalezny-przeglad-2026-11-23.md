# Audyt LI — rozdział 15 „Dualność, wypukłość i słaba zbieżność w przestrzeniach L^p”

Data: 2026-11-23. Repozytorium: `dariusz-piekarz/mathematical_scipts`.
Gałąź: `biblioteka-matematyczna-iteracja-6` (bez tworzenia nowej).
Audytowany plik: `chapters/pl/measure_theory/15-dualnosc-wypuklosc-i-slaba-zbieznosc-w-przestrzeniach-lp.tex`.
Niezmienny identyfikator audytowanego bloba: `075e6e30bc73a28450b7ffcb6af6b8fe9a76f8ab`.
Punkt odniesienia: po audytach wcześniejszych, w tym L; LI jest trzecim niezależnym przeglądem rozdziału 15.

## Zakres weryfikacji matematycznej

1. **Izometryczne parowanie `L^p-L^q`:** sprawdzono przypadki `1<p<∞`, `p=1` i funkcję `g=0`, poprawność normalizacji oraz jawnie potrzebną `σ`-skończoność dla lematu dotyczącego `p=1`. Przykład miary nieskończonej na jednym punkcie rzeczywiście wyklucza izometrię w pełnej ogólności.
2. **Nierówności punktu środkowego:** dla `p≥2` kontrola redukcji do nierówności skalarnych i Höldera/Clarks(o)na, dla `1<p<2` kontrola wartości własnych hesjanu `|z|^p`, całkowalności osobliwości przy przejściu przez zero i oszacowania całkowego z Höldera. Współczynniki oraz zależność od `p` zweryfikowane.
3. **Jednostajna wypukłość i metoda wariacyjna:** z `\|f-h\|_p≥ε` otrzymuje się dodatni ubytek normy środka, a ciąg minimalizujący energię jest Cauchy'ego. Sprawdzono również `Λ=0` i graniczny przypadek `R=0`.
4. **Reprezentacja `(L^p)^*=L^q` (`1<p<∞`):** kontrola różniczkowania pod całką przez dominację, zastosowania zmian `v↦iv`, całkowalności funkcji reprezentującej i jednoznaczności. Nie jest używane twierdzenie Radona–Nikodyma.
5. **Reprezentacja `(L^1)^*=L^∞` przy `σ`-skończoności:** kontrola funkcji wagowej `w>0` p.w., miary skończonej `P=wμ`, reprezentacji Hilbertowskiej, oszacowania `|g|≤\|Λ\|` oraz przejścia z funkcji obciętych do `L^1(μ)`.
6. **Dualna `L^∞`:** przykład funkcjonału granicy na ciągach zbieżnych i jego przedłużenia przez Hahna–Banacha; wektory `e_n` oraz ciąg stały wykazują, że nie jest reprezentowany przez `ℓ^1`.
7. **Refleksywność i zbieżność słaba:** zgodność kanonicznego zanurzenia `J:E→E^{**}` z obiema identyfikacjami, dolna półciągłość normy, kontrprzykład Rademachera, jawnie ograniczony separowalnością argument diagonalny oraz poprawność wzoru na jednoznaczny minimizator energii.

## Kontrole niezależne od dowodu

- Testy nierówności punktu środkowego na **13 500** deterministycznych próbach zespolonych sześciowymiarowych przestrzeni `L^p` dla `p = 1.05, 1.2, 1.5, 1.9, 2, 2.1, 3, 4, 8`: **0 naruszeń** przy względnej tolerancji `1e-9`. Maksymalne dodatnie `RHS-LHS` wyniosło `2.49e-14`, zgodne z błędem arytmetyki zmiennoprzecinkowej.
- Testy wzoru na punkt minimalny energii dla **16 000** deterministycznych prób na sześciu atomach i `p = 1.05, 1.2, 1.5, 1.9, 2, 3, 4, 8`: **0 naruszeń** dla stabilnego zakresu danych `|Re g|, |Im g| ≤ 0.5` i `1.5≤α≤3`; maksymalna reszta równania stacjonarności mniejsza niż `1.5e-15`. To testy skończeniewymiarowe, nie dowód twierdzenia na dowolnej przestrzeni z miarą.
- Struktura: **34 otwarcia / 34 zamknięcia** środowisk LaTeX (poprawna kolejność zagnieżdżeń), **17 etykiet / 17 unikalnych**, **17 wywołań ref/eqref / 17 rozwiązanych** na podstawie plików rozdziałów 10, 14 i 15. Zweryfikowane bloby zależności: rozdział 10 `2a5db02f83ae41a6ebabe30547d47080a75004cd`; rozdział 14 `b187bde8f8f0377a8a3e10f1aa5d19dea428147c`.

## Wynik i ograniczenia

**Wynik LI: PASS matematyczny i strukturalny dla zidentyfikowanego bloba.**
Nie stwierdzono nowej luki w dowodzie ani usterki, która uzasadniałaby zmianę kanonicznego źródła w tej iteracji; w szczególności żadnej nie dokonano.

**Otwarta walidacja techniczna:** w tej iteracji nie uruchomiono kompilacji całej książki, izolowanego PDF, testów CI GitHub Actions ani wizualnej inspekcji renderingu, ponieważ źródło badano przez interfejs odczytu repozytorium. Pusty odczyt statusów GitHub dla obserwowanej głowicy gałęzi nie stanowi sukcesu CI. Poprzedni audyt L raportował własną walidację PDF/CI; nie przenosimy jej automatycznie na nowy raport bez sprawdzenia tożsamości uruchomienia.

**Bramka stabilizacji:** rozdział 15 można traktować jako stabilny matematycznie/redakcyjnie w tym przebiegu 2+1, ale techniczna bramka pozostaje otwarta do potwierdzenia kompilacji oraz CI dla właściwego commitu. Do rozdziału 16 nie przechodzimy przed jej zamknięciem. Każda nowa zmiana kanonicznego źródła rozdziału 15 unieważnia status względem nowego bloba i wymaga ponownej kontroli.
