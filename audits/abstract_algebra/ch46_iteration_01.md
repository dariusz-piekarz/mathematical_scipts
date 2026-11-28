# AA-46 — audyt I: opracowanie i kontrola logiczna rozdziału

**Data:** 23 listopada 2026 r. **Werdykt: W TRAKCIE / NIE STABILNY.**
**Gałąź:** biblioteka-matematyczna-iteracja-6.
**Źródło:** chapters/pl/abstract_algebra/46-rozszerzenia-picarda-vessiota-i-rozniczkowa-teoria-galois.tex.
**Poprzednik:** AA-45 STABILNY; raport audits/abstract_algebra/ch45_iteration_03.md.

## Audyt merytoryczny I — lista zobowiązań

1. Definicje: ciało różniczkowe, układ DY=AY, macierz fundamentalna, różniczkowa prostota pierścienia, pierścień i ciało Picarda–Vessiota, automorfizmy różniczkowe. Wszystkie hipotezy i pola stałych podano jawnie.
2. Udowodniono lemat o przestrzeni rozwiązań: D(U^{-1}y)=0; zmiany fundamentalnej macierzy są prawymi mnożeniami przez GL_n(C). Udowodniono równanie Abela.
3. Istnienie, jednoznaczność PV, zachowanie stałych, algebraiczność grupy, odpowiedniość Galois i kryterium liouvillowskie: **wyraźnie oznaczono jako klasyczne twierdzenia cytowane**, z osobnymi uwagami wyjaśniającymi, dlaczego nie są następstwami elementarnych lematów. Źródło: van der Put–Singer, Galois Theory of Linear Differential Equations.
4. Reprezentację grupy G→GL_n(C), homomorfizm i różnowartościowość udowodniono samodzielnie, stosując C_E=C i generowanie E przez elementy macierzy.
5. Przykład G_m: t=e^x, R=K[t,t^{-1}] ma dowód prostoty różniczkowej z minimalną liczbą wyrazów wielomianu Laurenta i nieistnieniem wymiernej pochodnej logarytmicznej równej -j.
6. Przykład G_a: logarytm, macierz układu drugiego rzędu, sprawdzenie DU=AU, dowód prostoty R=K[t] z najmniejszego stopnia i przeszkody resztowej.
7. Przykład skończony μ_m: irreducibility T^m−x, wymuszone Dt=t/(mx), zachowanie stałych i działanie automorfizmów t↦ζt. Przykład harmoniczny: dwa rozwiązania z jednym generatorem t oraz t^{-1}; grupa diagonalna, wyznacznik 1.
8. Definicja rozszerzenia liouvillowskiego odróżnia dowolne funkcje pierwotne od elementarnych dołączeń logarytmicznych. Przykład funkcji błędu nieelementarnej, ale liouvillowskiej, z kontrolą stałych.
9. Airy: brak rozwiązań algebraicznych Riccatiego wyprowadzony z braku skończonych rozgałęzień i przypadku wymiernego przy nieskończoności; jawnie wskazano nieelementarne narzędzie teorii przykryć. Grupa SL_2 wynika po zastosowaniu cytowanego kryterium liouvillowskiego i obserwacji, że każda właściwa spójna algebraiczna podgrupa SL_2 jest rozwiązalna.
10. Nie wolno przedstawiać skończonych sprawdzianów obliczeniowych jako dowodu głębokich twierdzeń strukturalnych.

## Integracja i regresje

Planowane: 46 plików kanonicznych, katalog zgodny z książką, zachowanie historycznego przekrojowego audytu AA-01–AA-42 i osobnych raportów AA-43–AA-46, dwa zestawy testów (SymPy oraz bez SymPy na fractions.Fraction), pełne CI i przegląd każdej nowej strony PDF. Pierwsze zestawy regresji obejmują macierze fundamentalne, równanie Abela, grupy Ga/Gm/μ_m, stopnie Riccatiego i etykiety źródła.

## Otwarte

Konieczne są: niezależny audyt II, rzeczywiste zdalne CI na końcowym źródle i testach, kompletna kontrola LaTeX/odsyłaczy oraz wizualne oględziny wszystkich stron AA-46. Do tego czasu status **NIE STABILNY** i nie otwieramy AA-47.
