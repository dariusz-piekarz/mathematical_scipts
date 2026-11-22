# Topologia ogólna — rozdział 14: audyt iteracja 01 (rozbudowa)

Data: 2026-11-22. Źródło: `chapters/pl/general_topology/14-zwartosc-lokalna.tex`.

## Zakres

Zachowano bez zmian oryginalne trzy główne elementy przeniesione z rozdziału 11: definicję lokalnej zwartości, lemat o zwartym domknięciu otoczenia i lokalnie zwartą wersję twierdzenia Baire'a. Dopisano:

- dziedziczenie zwartości lokalnej przez otwarte i domknięte podprzestrzenie lokalnie zwartej przestrzeni Hausdorffa (dowody obu kierunków);
- skończone iloczyny lokalnie zwartych przestrzeni Hausdorffa oraz pełne kryterium dla dowolnych iloczynów niepustych przestrzeni Hausdorffa;
- przykłady przestrzeni dyskretnych oraz przestrzeni euklidesowych;
- definicje przeliczalności w nieskończoności i `σ`-zwartości, z rozróżnieniem kwantyfikatorów;
- twierdzenie o równoważności `σ`-zwartości, przeliczalności w nieskończoności i istnienia wyczerpania `K_n⊂int K_(n+1)` w klasie lokalnie zwartych przestrzeni Hausdorffa;
- implikację od spełniania drugiego aksjomatu przeliczalności do `σ`-zwartości dla przestrzeni lokalnie zwartych Hausdorffa;
- kontrprzykład nieprzeliczalnej przestrzeni dyskretnej (lokalnie zwarta, ale nie `σ`-zwarta);
- kontrprzykład `Q` (`σ`-zwarta, lecz nieprzeliczalna w nieskończoności), pokazujący niezbędność lokalnej zwartości dla równoważności;
- wyczerpanie `R` przez przedziały `[-n,n]`.

## Matematyczny audyt kroków

1. W dowodzie dziedziczenia przez otwarte podprzestrzenie wykorzystano lemat o zwartym domknięciu zawartym w zadanym otwartym podzbiorze, zaś dla domkniętych przecięcie zbioru zwartego z domkniętym.
2. W dowodzie produktu iloczyn zwartych otoczeń ma niepuste otwarte otoczenie punktu; zwartość wynika z twierdzenia dla skończonych iloczynów z rozdziału 7.
3. Dla dowolnych iloczynów: przy lokalnej zwartości produktu zwarty zbiór $K$ zawierający podstawowe otwarte otoczenie produktu ma rzutowania pokrywające wszystkie czynniki poza skończoną liczbą; te czynniki muszą być zwarte. W drugą stronę użyto twierdzenia Tychonoffa oraz skończonego iloczynu przestrzeni lokalnie zwartych. Niepustość wszystkich czynników została jawnie założona.
4. W wyczerpaniu: każde zwarte `C` ma zwarty zbiór `K` z `C⊂int K` (skończone podpokrycie otoczeń o zwartym domknięciu). Następnie rekurencja stosowana do `K_n∪C_(n+1)` daje ścisłe zawieranie w kolejnych wnętrzach. Odwrotnie, rosnące otwarte pokrycie zwartego `C` daje jego zawieranie w jednym `K_N`.
5. Wnioski z drugiego aksjomatu przeliczalności opierają się na wcześniejszej własności Lindelöfa, bez użycia późniejszej parazwartości.
6. Przykład `Q`: każdy zwarty `K⊂Q` jest domknięty w `R` i nie może zawierać niepustego względnie otwartego przedziału; z każdej rzekomo współkońcowej rodziny `K_n` dobierany jest `q_n→q` poza `K_n`; zbiór granicy wraz z ciągiem jest zwarty, a nie mieści się w żadnym `K_n`.
7. Zachowano zasadę zależności: wszystkie wyniki potrzebne w rozdziale 14 pochodzą z rozdziałów 4, 5, 7, 9 i 11; nie korzysta się z rozdziałów 15–17 ani z teorii uzwarceń.

## Walidacja i stan

Test `tools/tests/test_general_topology_ch14.py` rozszerzono o kontrolę nowych etykiet i zachowania materiału z rozdziału 11.

Pierwsza kompilacja rozszerzenia przed dodaniem kryterium dowolnych iloczynów zakończyła się sukcesem (`45007966956`), lecz jej PDF miał prawie pustą ostatnią stronę. Z tego powodu dodano pełny wynik o dowolnych iloczynach i rozszerzono testy. Końcowy przebieg z kryterium dowolnych iloczynów i jego testem: **45008243682**, commit `43060190ff550cf852131ebaff81481633919a98`, `completed / success`, bez nieudanych kroków. https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45008243682 . Pobrano artefakt `14748916841`, zawierający `general_topology_ch14.pdf` (4 strony A4) oraz log. Sprawdzono log: brak `Overfull`, `Underfull`, `Missing character`, `LaTeX Warning`, `Undefined control sequence` i `Fatal error`. Wyrenderowano i obejrzano wszystkie 4 strony: brak ucięć, kolizji podpisów i wzorów; ostatnia strona jest wypełniona nowym szczegółowym kontrprzykładem i uwagą. **Nie uznawać wyniku CI ani kontroli graficznej za pozytywny przed rzeczywistym sprawdzeniem.**

| Warstwa | Status |
| --- | --- |
| Matematyka, dowody i zależności | Kontrola wstępna PASS |
| Szczegółowość przykładów i kontrprzykładów | Kontrola wstępna PASS |
| Terminologia i odsyłacze | Weryfikacja źródła wykonana |
| Testy CI, kompilacja samodzielna i całej książki | PASS — run 45008243682 |
| Render i kontrola PDF | PASS — wszystkie 4 strony |
| Stabilizacja rozdziału | **W AUDYCIE — ITERACJA 01** |

Następny krok: audyt niezależny po sprawdzeniu pełnego CI, w szczególności wyrównanie stron, ewentualne błędy dzielenia wyrazów i kompletność dowodów.

**Ważne:** jest to pierwsza iteracja audytu nowego materiału. Kolejna niezależna iteracja matematyczna powinna zweryfikować w szczególności kryterium dowolnych iloczynów i konstrukcję wyczerpania. Nie nadawać jeszcze statusu STABILNY.
