# Topologia ogólna — rozdział 14: audyt iteracja 02

Data: 2026-11-22. Źródło: `chapters/pl/general_topology/14-zwartosc-lokalna.tex`.

## Kontrola matematyczna

Ponownie przeanalizowano definicję zwartości lokalnej, dowód lematu o zwartych domknięciach, wersję lokalnie zwartą twierdzenia Baire'a, dziedziczenie własności przez podprzestrzenie, iloczyny skończone i dowolne, `σ`-zwartość, przeliczalność w nieskończoności oraz wyczerpania zwarte.

### Wykryta istotna luka i naprawa

W poprzedniej wersji kontrprzykładu `Q` (etykieta `ex:topog-lokalna-q-sigma-nieskonczonosc`) z wyboru `q_n ∉ K_n` błędnie wyciągnięto wniosek, że kompakt `C={q}∪{q_n:n≥1}` nie jest zawarty w żadnym `K_m`. Dla rodziny nieuporządkowanej wybór `q_n∉K_n` nie gwarantuje tego wniosku.

Naprawa: zastępujemy rodzinę `K_n` przez rosnącą rodzinę `L_n=⋃_{j≤n}K_j`. Każde `L_n` jest zwarte, a rodzina `(L_n)` pozostaje współkońcowa. Wybieramy `q_n∉L_n` oraz `|q_n-q|<1/n`. Wtedy `C` jest zwarty jako zbiór granicy i wyrazów ciągu zbieżnego, ale `C⊄L_n` dla wszystkich `n`, a więc `C⊄K_n`. Otrzymujemy rzeczywistą sprzeczność z założeniem współkońcowości.

Poprawka źródła: `77f4628a8dcff9b32b7b89b5547d89a0da58f9c1`. Test regresyjny poszerzono o jawne sprawdzanie `L_n`, `q_n∉L_n` i `C⊄L_n`: commit `66ed20b08e70e4ab04c77ecf0cfcb4781a5fcada`.

### Pozostałe sprawdzenia

- Dla iloczynów niepustych przestrzeni Hausdorffa: w dowodzie konieczności zwarty zbiór `K` zawierający bazowy cylinder `B` ma rzutowania równe `X_i` dla wszystkich poza skończenie wieloma indeksami, a zatem czynniki te są zwarte. Rzutowania na pozostałe czynniki obejmują otwarte otoczenia wybranych współrzędnych, co daje lokalną zwartość każdego czynnika. Wystarczalność wynika z twierdzenia Tychonoffa i skończonych iloczynów.
- Dla wyczerpań: skończone pokrycie zwartego `C` wnętrzami zwartych otoczeń daje `C⊂int K`. Rekurencja zapewnia `K_n⊂int K_(n+1)`; monotoniczność wnętrz i skończone podpokrycie dają współkońcowość.
- Twierdzenie Baire'a: ciąg zstępujących niepustych zbiorów zwartych `K_n` ma niepuste przecięcie dzięki zwartości `K_1`; wszystkie wcześniejsze hipotezy są jawne.
- Drugi aksjomat przeliczalności i lokalna zwartość implikują `σ`-zwartość przez Lindelöfa i przeliczalne pokrycie otoczeniami o zwartych domknięciach.
- Brak zależności od rozdziałów 15–17.

## Weryfikacja

Właściwy CI dla zmodyfikowanego źródła i nowego testu:
https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45008598489

**Weryfikacja zakończona:** GitHub Actions run `45008598489` dla commita `66ed20b08e70e4ab04c77ecf0cfcb4781a5fcada`: `completed / success`, bez nieudanych kroków. Artefakt `14748314830` zawiera `general_topology_ch14.pdf` i `.log`. PDF ma 4 strony A4; wyrenderowano i obejrzano wszystkie strony (kontrola wzorów, podziału tekstu i odstępów). Log nie zawiera `Overfull`, `Underfull`, `Missing character`, `LaTeX Warning`, `Undefined control sequence` ani `Fatal error`. Nie stwierdzono ucięć ani kolizji w składzie. Artefakt: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45008598489/artifacts/14748314830

| Element | Status |
|---|---|
| Wykryty błąd w kontrprzykładzie `Q` | **NAPRAWIONY** |
| Dowód kryterium dowolnych iloczynów | PASS — audyt niezależny |
| Równoważność `σ`-zwartości, wyczerpania i przeliczalności w nieskończoności | PASS — audyt niezależny |
| Twierdzenie Baire'a i lemat o otoczeniach | PASS |
| Weryfikacja CI i PDF po poprawce | **PASS — run 45008598489; 4 strony sprawdzone** |
| Status rozdziału | **W AUDYCIE** — po istotnej poprawce nie oznaczać jako stabilny |
