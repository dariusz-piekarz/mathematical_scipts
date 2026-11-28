# Analiza funkcjonalna — rozdział 05 — audyt 03 (kontrola niezależna po audycie 02)

**Data:** 23 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Źródło:** chapters/pl/functional_analysis/05-przestrzenie-lokalnie-wypukle-i-seminormy.tex.  
**SHA aktualnego źródła po zmianach:** 2b72d6c88f413021d695024481b1a4a5c466476c.  
**Wynik:** audyt z korektami — **NIE CZYSTY**, licznik aktualnej stabilizacji **0/2**.

## Współbieżny raport 05/02 i wersjonowanie

W czasie przeglądu równolegle opublikowano raport 05-audyt-2.md ze statusem „czysty”, odnoszący się do wcześniejszego SHA źródła 8f2a545cccf5e47395ded3d8f321e1574c916ce9. Nie jest to ten sam stan pliku: w bieżącej kontroli wprowadzono dalsze rzeczywiste doprecyzowania. **Zachowano raport 05/02 bez nadpisywania**, ale jego czysty wynik na starszym stanie nie wystarcza do ustabilizowania nowszej wersji; licznik dwóch kolejnych czystych kontroli wymaga ponownego rozpoczęcia.

## Niezależny przegląd wszystkich 13 dowodów

1. **Absolutna wypukłość:** współczynniki α,β, warunek |α|+|β|≤1, przypadek α=β=0 oraz przejście od sumy do kombinacji wypukłej. PASS.
2. **Baza absolutnie wypukłych otoczeń:** dla otwartego zrównoważonego O zbiór conv(O) jest otwarty (perturbacja składnika z t_j>0), wypukły i zrównoważony. PASS.
3. **Topologia seminorm:** ciągłość dodawania i mnożenia przez skalar, minimalność, kryterium Hausdorffa przez jądra, zbieżność sieci. PASS.
4. **Funkcjonał Minkowskiego:** jednorodność dla liczb rzeczywistych i zespolonych, podaddytywność przez kombinację wypukłą, otwartość A równoważna A={p_A<1} w założeniach twierdzenia, ciągłość seminormy. PASS.
5. **LCS a seminormy:** wszystkie otwarte absolutnie wypukłe otoczenia U mają ciągłe p_U, odtwarzające topologię; dla X Hausdorffa rodzina rozdziela punkty. PASS.
6. **Liniowe odwzorowania ciągłe:** oszacowanie q(Tx)≤C max p_j(x); konieczne rozpatrzenie r(x)=0, ciągłość w zerze w przeciwną stronę. PASS.
7. **Zbiory ograniczone przez seminormy:** kryterium sup_B p<∞ dla wszystkich p, także pusty B. PASS.
8. **Otoczki absolutnie wypukłe:** dla z=Σλ_j x_j z Σ|λ_j|≤1, p(z)≤sup_B p, więc otoczka ograniczona. PASS.
9. **Kolmogorow — normowalność:** dla ograniczonego otwartego absolutnie wypukłego U seminorma Minkowskiego ma trywialne jądro z Hausdorffa i ograniczoności U, a homotetie U generują topologię. PASS.
10. **Metryzowalność przez przeliczalną rodzinę seminorm:** dyadyczna metryka z min(1,p_n) jest translacyjnie niezmiennicza, rozdziela punkty i wyznacza tę samą topologię; przeciwny kierunek przez przeliczalną bazę. PASS.
11. **Sieci Cauchy'ego:** zgodność z kryteriami dla wszystkich seminorm generujących topologię, wspólny późny indeks dla skończonej liczby p_j. PASS.
12. **Zupełność C∞([0,1]):** jednostajna zbieżność każdej pochodnej w C([0,1]), tożsamości całkowe, przejście do granic i g_j'=g_{j+1}; redukcja zupełności sieci do ciągowej dzięki metryzowalności. PASS.
13. **LCS: podprzestrzenie, produkty, ilorazy:** przecięcia i skończone restrykcje współrzędnych zachowują wypukłość, a otwartość rzutu ilorazowego zapewnia bazę wypukłych otoczeń; warunek Hausdorffa ilorazu równoważny M domkniętej. PASS.

## Przykłady — 5/5 sprawdzonych

1. Seminormy na K^N, C∞([0,1]) i C(Ω). Dla K=∅ w definicji p_K brakowało konwencji: poprawiono.
2. Otwarty nieograniczony pas A w R² ma p_A(x,y)=|x|, funkcjonał jest seminormą, ale nie normą.
3. Pochłaniający nieotwarty zbiór w c_00 ma p_A(x)=sup_n n|x_n|, nieciągły w normie supremum (e_n/n).
4. Produkt K^N jest zupełną metryzowalną LCS, lecz nie jest normowalny.
5. C∞([0,1]) jest przestrzenią Frécheta i nienormowalną: oscylacyjne funkcje sinusoidalne mają małe p_m i nieograniczone p_{m+1}.

## Zmiany wymagane w audycie

1. Formuła p_K(f)=sup_{x∈K}|f(x)| dla „dowolnego zwartego” K nie określała skończonej seminormy w przypadku K=∅ bez konwencji supremum. Przyjęto **niepusty K**, a dla pustego **p_K=0**.
2. Zapowiedź „zupełność wykażemy w następnym stwierdzeniu” przy C∞ była myląca (bezpośrednio następny wynik dotyczy kryterium Cauchy'ego). Zastąpiono ją bezpośrednim odsyłaczem do **thm:smooth-complete**.
3. Poprawiono powtórzenie „dla” w podpisie rysunku Minkowskiego, zachowując niezbędny warunek **p_A(x)>0**.
4. Zmieniono komentarz wersji. Wszystkie **19 etykiet, 13 dowodów i 5 przykładów** zachowano.

## Regresje oraz PDF

- Rozszerzono tools/tests/test_functional_analysis_ch05.py **12→15 testów**: nowe kontrole niepustego K, oszacowań seminormy supremum i konwencji dla pustego K, jawnego odsyłacza do kompletności C∞ oraz punktu x/p_A(x) na brzegu elipsy.
- [Przebieg GitHub Actions 45170212776](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45170212776) zakończył się pełnym **SUCCESS**: 15/15 testów PASS, kompilacja LaTeX w dwóch przebiegach PASS, kontrola końcowego PDF i odsyłaczy PASS oraz zapis artefaktu PASS. Pierwsze przejście LaTeX sygnalizowało przejściowe nierozwiązane odsyłacze; **końcowy log po drugim przebiegu nie zawiera takich ostrzeżeń**.
- Pobrano i sprawdzono aktualny artefakt PDF z powyższego przebiegu: **33 strony A4, 482683 bajty**. Wyrenderowano i obejrzano komplet siedmiu stron rozdziału 05 (**strony 27–33**), ze szczególnym uwzględnieniem diagramu i podpisu Minkowskiego na stronie 29. Brak kolizji, ucięć i uszkodzonych znaków; kontrola współrzędnych bloków tekstu na stronach 27–33 wykazała **0 elementów poza obszarem strony**. Końcowy log nie zawiera błędów `Undefined control sequence`, nierozwiązanych odsyłaczy, `Overfull \\hbox` ani `Missing character`.

## Decyzja

**W tej iteracji znaleziono i poprawiono trzy nieścisłości, dlatego nie można zaliczyć jej jako czystej.** Po aktualizacji źródła wymagane są dwa kolejne niezależne czyste audyty. Następna iteracja: **05/04**, a nie przejście do rozdziału 06.
