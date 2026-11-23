# AA-49 — audyt I: konstrukcja i obowiązki dowodowe

**Data:** 23 listopada 2026 r.
**Status:** NIE STABILNY — oczekuje niezależnego audytu II, pełnego CI i kontroli PDF.
**Źródło:** chapters/pl/abstract_algebra/49-kwadratowy-przypadek-algorytmu-kovacica.tex.
**Zakres:** docs/pl/zakres_aa49_kovacic_kwadratowy.md.

## Kontrola I

1. Rozdział rozdziela dowody własne od pełnej lokalnej klasyfikacji E_a, E_∞, która wymaga klasycznego twierdzenia Kovacica. Zakres i cytat podano jawnie; nie fałszować deklaracji samodzielnej kompletności teorii lokalnej.
2. Derywacja zachowuje sprzężenie algebraiczne: automorfizm rozszerzenia stopnia 2 nad K komutuje z jedynym przedłużeniem derywacji. Ślad φ=r+rbar i wyróżnik Δ=(r−rbar)^2 należą do K.
3. Z równania Riccatiego wyprowadzono r rbar=(φ'+φ²−2q)/2, Δ=4q−2φ'−φ², Δ'=−2φΔ oraz równanie śladu φ''+3φφ'+φ³−4qφ−2q'=0. Odwrotny kierunek ma jawny dowód przez δ'=−φδ i r±=(φ±δ)/2.
4. Wyróżnik Δ musi być niezerowy i nie być kwadratem w K, aby uzyskać **ściśle** kwadratowe rozwiązania; bez tego mogłoby się otrzymać gałąź wymierną.
5. Symetryczny kwadrat: dla z1''=qz1 i z2''=qz2, v=z1z2 spełnia v'''−4qv'−2q'v=0. Następnie z v=P e^{∫θ} wprost wynika liniowy operator P''' +3θP''+(3θ²+3θ'−4q)P' +(θ''+3θθ'+θ³−4qθ−2q')P.
6. Kandydaci: lokalne E_a dla rzędów 1,2,>2 i E_∞ dla ord∞>2, =2, <2. Dla każdej kombinacji oblicza się całkowity stopień n=(e∞−Σe_a)/2≥0 i θ=1/2Σe_a/(x−a). Skończenie wiele kombinacji.
7. Wynik pozytywny musi przejść bezpośrednio test trzeciego rzędu i test wyróżnika. Wynik negatywny w klasie ścisłego stopnia 2 wykorzystuje **cytowaną konieczność** lokalnych kandydatów.
8. Przykłady obejmują n=0, n=1, drugi układ lokalnych list i negatywny wynik dla q=x. Sprawdzanie wartości n i niekwadratowości Δ nie jest opcjonalne.

## Testy i integracja

Dwa niezależne zestawy przygotowane (11 SymPy, 10 Fraction), obejmujące wzory śladu, wyróżnik, przykłady n=0/n=1 i odrzucenie Airy'ego. Raport II powinien sprawdzić konkretne linie rachunku na niezależnych modelach, a raport III dopiero po rzeczywistym finalnym CI i inspekcji każdej strony końcowego PDF.

**Werdykt:** W AUDYCIE. AA-50 nieotwarty.
