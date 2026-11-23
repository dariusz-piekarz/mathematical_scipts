# Analiza funkcjonalna — rozdział 05 — audyt 04 (pierwsza kontrola stabilizacyjna)

**Data:** 23 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Źródło:** chapters/pl/functional_analysis/05-przestrzenie-lokalnie-wypukle-i-seminormy.tex.  
**SHA źródła:** 2b72d6c88f413021d695024481b1a4a5c466476c.  
**Wynik matematyczno-redakcyjny:** **CZYSTY** — nie wprowadzono żadnych zmian do rozdziału; pierwszy kandydat do 1/2 czystych audytów od ostatniej korekty 05/03. **Rozdział 05 nadal NIE jest stabilny.**

## Metoda audytu

Ponowna, niezależna analiza aktualnej (po audycie 05/03) treści wszystkich 13 środowisk dowodowych, pięciu środowisk przykładów i rysunku Minkowskiego. Sprawdzono definicje i jawność założeń, logikę obydwu implikacji twierdzeń, skrajne przypadki dla zerowych współczynników oraz pustych zbiorów, sprawdzalność odsyłaczy, nazewnictwo i poprawność wariantu nad ciałem zespolonym. Testy kodowe uzupełniają kontrolę, ale nie zastępują dowodów matematycznych.

## Matematyka: 13/13 dowodów PASS

1. **Charakteryzacja absolutnej wypukłości** — obie implikacje, kombinacje z sumą modułów współczynników nie większą niż jeden, przypadek obu współczynników zerowych; PASS.
2. **Absolutnie wypukła baza otoczeń** — przekrój otwartego zrównoważonego O z wypukłym otoczeniem V, otoczka wypukła O pozostaje otwarta (perturbacja dodatniego składnika reprezentacji wypukłej), wypukła i zrównoważona; PASS.
3. **Topologia generowana przez seminormy** — baza skończonej liczby nierówności p_j(x)<ε, ciągłość łączna działań, najmniejsza dopuszczalna topologia TVS, kryterium Hausdorffa i zbieżność sieci; PASS.
4. **Własności funkcjonału Minkowskiego** — pochłanianie, skalowanie w K=R i K=C, podaddytywność, przypadek λ=0; przy otwartym A równość A={p_A<1} i ciągłość, a przy nieotwartym tylko zawierania; PASS.
5. **Charakteryzacja lokalnej wypukłości przez ciągłe seminormy** — funkcjonały p_U otwartych absolutnie wypukłych otoczeń odtwarzają bazę; przy Hausdorffie rozdzielają punkty; PASS.
6. **Kryterium ciągłości odwzorowań liniowych** — jednorodne skalowanie wyprowadza q(Tx)≤C max_j p_j(x), także gdy maksimum znika; odwrotna ciągłość z bazy docelowej; PASS.
7. **Kryterium ograniczoności przez seminormy** — skończone podrodziny seminorm kontrolują każde otoczenie, a odwrotnie ograniczoność von Neumanna kontroluje poszczególne seminormy; B puste uwzględnione; PASS.
8. **Ograniczoność otoczki absolutnie wypukłej** — oszacowanie p(Σλ_jx_j)≤sup_B p, gdy Σ|λ_j|≤1, obejmuje oba typy otoczek; PASS.
9. **Twierdzenie Kolmogorowa** — do seminormy p_U stosuje się zarazem ograniczoność i otwartość U; niezerowe jądro wyklucza Hausdorff, a homotetie U odtwarzają topologię; PASS.
10. **Przeliczalne seminormy a metryzowalność** — suma ważonych min(1,p_n) jest metryką przy rodzinie rozdzielającej; dowiedziono równoważności topologii, nie tylko ciągowej, przez skończone prefiksy i kontrolę ogona; PASS.
11. **Kryterium Cauchy'ego dla seminorm** — z definicji kanonicznej struktury jednostajnej na TVS i skierowania zbioru indeksów; PASS.
12. **Zupełność C^\infty([0,1])** — pochodne mają jednostajne granice g_j, wzory Newtona–Leibniza dają g_j'=g_{j+1}, więc g_0 jest gładka i zbieżność zachodzi w każdej p_m; kompletność ciągowa implikuje zupełność dzięki metryzowalności; PASS.
13. **Podprzestrzenie, produkty, ilorazy lokalnie wypukłych** — baza wypukła przechodzi do podprzestrzeni, produktów i ilorazów przez otwarte rzutowanie; Hausdorff ilorazu dokładnie przy domkniętym M; PASS.

## Przykłady: 5/5 PASS

1. Seminormy współrzędnych w K^N, pochodnych w C^\infty i supremum na niepustych zwartych K⊂Ω. Konwencja p_∅=0 jest teraz jawna.
2. Otwarty pas w R² daje seminormę Minkowskiego p_A(x,y)=|x| z niezerowym jądrem.
3. Pochłaniający absolutnie wypukły, ale nieotwarty zbiór na c_00: x_n=e_n/n→0, natomiast p_A(x_n)=1.
4. K^N z topologią produktu: nienormowalna przestrzeń Frécheta.
5. C^\infty([0,1]) z rosnącą rodziną seminorm pochodnych: metryzowalna, zupełna, ale nienormowalna; sinusoidy f_N mają małe p_m i nieograniczone p_{m+1}.

Dodatkowo ponownie wyprowadzono nierówność dla L^p([0,1]), 0<p<1, wykorzystując nieatomowość miary ν_f(E)=∫_E|f|^p dλ. Równe masy w podziale na n części dają |L(f)|≤C n^(1-1/p)||f||_p→0, co jest poprawne również dla funkcji zespolonych.

## Kontrpróby i niezależne regresje

- Zbudowano w teście konkretny podział miary ν_f dla f(t)=t i p∈{0.25,0.5,0.8} na n części o równej masie: punkty t_k=(k/n)^(1/(p+1)), weryfikując relację norm przy p<1.
- Sprawdzono nad C jednorodność p_A(λz)=|λ|p_A(z) oraz nierówność trójkąta na przykładzie absolutnie wypukłej kuli |z₁|+2|z₂|<1, z λ zawierającymi niezerową część urojoną.
- Zbadano seminormy p₁(x,y)=|x| i p₂(x,y)=|y|: pierwsza nie rozdziela punktów, a rodzina {p₁,p₂} rozdziela wszystkie punkty R², zgodnie z kryterium Hausdorffa.
- Źródło bez zmian; dodano **3 nowe testy** w tools/tests/test_functional_analysis_ch05.py (**15 → 18**).
- Wykryte wcześniej nieścisłości z 05/03 pozostają poprawione: pusty K, dokładny odsyłacz do twierdzenia o zupełności oraz warunek p_A(x)>0 w podpisie.

## Redakcja, odsyłacze i struktura

- **13 par proof, 5 par przyklad, 19 unikatowych etykiet, 14 odsyłaczy**, wszystkie ich cele znajdują się w rzeczywistych rozdziałach 01–05.
- Słownictwo zgodne z ustalonymi konwencjami: „zupełność ciągowa”, „przestrzeń sprzężona”, oznaczenie funkcji charakterystycznych χ_A, bez niepożądanych anglicyzmów i niedozwolonych form.
- Sprawdzono matematyczne przesłanki diagramu Minkowskiego, w tym p_A(x)>0; nie wprowadzano zmian w TikZ ani opisie.
- W dedykowanym [CI 45171358837](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45171358837) etap **18 testów** przeszedł PASS, a przygotowanie dokumentu 01–05 PASS. Końcową kompilację, kontrolę odsyłaczy oraz PDF trzeba odnotować po potwierdzeniu całego przebiegu.

## Werdykt

**Czysty audyt matematyczno-redakcyjny bez zmian w rozdziale 05.** Po potwierdzonym pełnym CI może zostać zaliczony jako **1/2 kolejnych czystych audytów**. Do stabilizacji konieczny następny niezależny audyt 05/05. **Nie rozpoczynano rozdziału 06.**
