# Analiza funkcjonalna — rozdział 13 — audyt 02 (niezależna kontrola i naprawa testu)

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6` (bez tworzenia nowej).  
**Źródło:** `chapters/pl/functional_analysis/13-przestrzenie-hilberta-reprezentacja-riesza-i-formy-poltoraliniowe.tex`.  
**SHA źródła:** `1ca8b2ee077f558e50412c5d74e116779ab44f31` (niezmieniony względem 13/01).  
**SHA testów przed zmianą:** `fa97449adfca69de43e80540613bc5fa1763ff14`.  
**SHA testów po zmianie:** `ea8ea6a5b82596705f5f717c57317a6a06268369`.  
**Werdykt:** wykryto i naprawiono wadliwą kontrolę regresyjną. **0/2 audytów stabilizacyjnych**; rozdział 14 pozostaje zablokowany.

## Stan przed iteracją

Odczytano rzeczywistą listę raportów na gałęzi: rozdział 12 ma audyty 01–03 i jest zamknięty; rozdział 13 ma dotychczas audyt 13/01. Odczytano cały rozdział 13, jego testy i workflow. GitHub API potwierdziło przebiegi dedykowanego CI: [#45254273546](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45254273546) `completed/success`, commit `3649b336496d54e350840522be7672b44679f8ae`, aktualizacja 2026-11-23 19:58:48 UTC, oraz [#45253868291](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45253868291) `completed/success`, commit `d62b02a0fc97d7a9abec88c2b9a869a5314f9aea`. Te przebiegi **poprzedzają** niniejszą zmianę testu; nie są dowodem zielonego CI dla nowego SHA.

## Niezależna kontrola matematyczna

Przeczytano ponownie **14/14 dowodów**: Cauchy–Schwarz i polaryzacja; istnienie, jednoznaczność i nieekspansywność rzutu na domknięty zbiór wypukły; rozkład ortogonalny; reprezentacja Riesza i antyliniowość identyfikacji zespolonej; Bessel; przeliczalność nośnika Fouriera; Parseval dla sieci skończonych sum; istnienie baz ortonormalnych; dolne ograniczenie mocy bazy Hamela przez rodzinę Vandermonde'a; izometria z `ell^2(I)`; operator sprzężony; reprezentacja form półtoraliniowych; Lax–Milgram bez założenia symetrii. Sprawdzono zwłaszcza zgodność znaków z liniowością iloczynu skalarnego w pierwszym argumencie oraz przejście od skończonych sum do sieci. W źródle nie znaleziono nowej fałszywej tezy.

Sprawdzono **5/5 przykładów**: `ell^2` i `L^2` oraz kontrprzykład dla normy supremum; rzut na stałe; szereg poza rozpięciem algebraicznym; Gram–Schmidt i eksponenty; słabe zagadnienie Poissona. Dla ostatniego zweryfikowano niezależnie konstrukcję `g=c-∫f`, `w=∫g`, warunki `w(0)=w(1)=0`, `w''=-f` prawie wszędzie, gęstość gładkich funkcji z zerowymi wartościami brzegowymi i zastosowanie jednoznaczności Laxa–Milgrama. Zwrócono uwagę, że gęstość aproksymantów pochodnej wymaga korekty średniej, którą źródło jawnie zawiera.

## Znaleziona usterka testowa i minimalna poprawka

W `test_weak_poisson_f_constant_one` była asercja `self.assertAlmostEqual(0.5-t, 0.5-t)`, porównująca wyrażenie z samym sobą. Nie mogła wykryć błędnej pochodnej rozwiązania. Zastąpiono ją niezależnymi różnicami centralnymi wielomianu `u(t)=t(1-t)/2` w **9 punktach wewnętrznych**: porównanie pochodnej pierwszej z `1/2-t` i kontrola `-u''=1`. Pozostawiono dotychczasowe testy warunków brzegowych i słabej tożsamości całkowej.

Zmiana testu: commit `0dc1faabc0fd26cf3dd6c247712a7c7a53a06f8f`. Lokalnie sprawdzono wartości centralnej drugiej różnicy dla 9 punktów: maksymalny błąd numeryczny poniżej `10^-8`; nie jest to wykonanie całego zestawu unittest ani CI. Źródła LaTeX i workflow nie zmieniano.

## Kontrola techniczna i decyzja

Struktura źródła zachowana: **14 środowisk proof, 5 przykładów**, 30 etykiet i 13 odsyłaczy według istniejącej kontroli z 13/01. W tej iteracji nie pobrano nowego PDF; poprzedni audyt 13/01 dokumentuje wizualną inspekcję stron 72–78 dla niezmienionego źródła. Po zmianie testu **nie potwierdzono jeszcze zakończonego CI dla nowego commita**. Nie należy oznaczać go PASS na podstawie starszych przebiegów.

**Decyzja: 13/02 Z POPRAWKĄ TESTU, 0/2.** Kolejna iteracja musi odczytać rzeczywisty wynik CI po zmianie, a następnie wykonać czysty niezależny audyt 13/03. Rozdziału 14 nie otwierać.
