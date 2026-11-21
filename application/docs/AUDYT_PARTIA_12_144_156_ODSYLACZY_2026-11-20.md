# Audyt integralności odsyłaczy — partia XII (144–156)

Data: 20 listopada 2026 r.  
Repozytorium: `dariusz-piekarz/mathematical_scipts`  
Gałąź: `biblioteka-matematyczna-iteracja-6` (stan początkowy `40100dfd9a3738a8358527d4a8d149faec494314`).  
Materiał wejściowy: `reference_provenance_audit_355.json`, indeks 355 rozdziałów, wystąpienia `unresolved_references` 144–156 (licząc od 1).

## Wynik

**13/13** wystąpień w surowym indeksie ma status `missing`, lecz wszystkie są świadomymi odsyłaczami międzytomowymi z poprawnym prefiksem `I-`, `II-` lub `IV-` i mają **istniejący rozdział docelowy**. Skontrolowano pięć rozdziałów źródłowych z tomów III i IV oraz dwanaście różnych etykiet/docelowych rozdziałów w tomach I, II i IV. Nie ma podstaw do usuwania ani zmieniania oryginalnych etykiet i cytowań.

## Wszystkie wystąpienia

| Nr | Źródło | Oryginalne cytowanie | Rzeczywisty rozdział i jego oryginalna etykieta | Sens cytatu |
|---:|---|---|---|---|
| 144 | `P3-06:3` | `\ref{IV-ch:time-series}` | `P4-16`, `\label{ch:time-series}` | Wnioskowanie z procesów zależnych i szeregi czasowe |
| 145 | `P3-06:3` | `\ref{IV-ch:model-selection}` | `P4-15`, `\label{ch:model-selection}` | Wybór, walidacja i regularizacja modeli |
| 146 | `P3-10:3` | `\ref{IV-ch:glm}` | `P4-14`, `\label{ch:glm}` | Regresja Poissona i uogólnione modele liniowe |
| 147 | `P3-10:3` | `\ref{II-ch:poisson-process}` | `P2-04`, `\label{ch:poisson-process}` | Proces Poissona |
| 148 | `P3-11:3` | `\ref{II-ch:poisson-process}` | `P2-04`, `\label{ch:poisson-process}` | Proces Poissona |
| 149 | `P3-11:3` | `\ref{IV-ch:conjugate-families}` | `P4-18`, `\label{ch:conjugate-families}` | Estymacja i rodziny sprzężone |
| 150 | `P3-15:3` | `\ref{IV-ch:monte-carlo}` | `P4-23`, `\label{ch:monte-carlo}` | Monte Carlo i aproksymacja całek |
| 151 | `P4-00:11` | `\ref{I-ch:probability}` | `P1-02`, `\label{ch:probability}` | Przestrzeń probabilistyczna |
| 152 | `P4-00:11` | `\ref{I-ch:conditioning}` | `P1-03`, `\label{ch:conditioning}` | Warunkowanie i niezależność |
| 153 | `P4-00:11` | `\ref{I-ch:random-variables}` | `P1-04`, `\label{ch:random-variables}` | Zmienne losowe i rozkłady |
| 154 | `P4-00:11` | `\ref{I-ch:expectation}` | `P1-05`, `\label{ch:expectation}` | Wartość oczekiwana |
| 155 | `P4-00:11` | `\ref{I-ch:condexp}` | `P1-10`, `\label{ch:condexp}` | Warunkowa wartość oczekiwana |
| 156 | `P4-00:11` | `\ref{I-ch:lln}` | `P1-08`, `\label{ch:lln}` | Prawa wielkich liczb |

## Sprawdzenie matematyczne i techniczne

1. **`P3-06`, SDE i modele zależne.** Pierwszy cytat prowadzi do estymacji procesów zależnych (`P4-16`), a drugi do wyboru i walidacji modeli (`P4-15`). Oba są zgodne z deklaracją akapitu i tematyką rozdziałów, ale nie zastępują dowodu konkretnego twierdzenia.
2. **`P3-10` i `P3-11`, procesy Lévy'ego i miary skoków.** Odpowiednimi źródłami są model regresji Poissona (`P4-14`), konstrukcja procesu Poissona (`P2-04`) i rodziny sprzężone (`P4-18`). Zweryfikowano, że te rozdziały istnieją oraz deklarują oczekiwane etykiety.
3. **`P3-15`, całki po trajektoriach.** `IV-ch:monte-carlo` wskazuje na metody próbkowania służące do przybliżania całek, rzeczywiście opisane w `P4-23`.
4. **`P4-00`, wprowadzenie do statystyki.** Sześć odsyłaczy na linii 11 dotyczy kolejno przestrzeni probabilistycznej, warunkowania, zmiennych losowych, wartości oczekiwanej, warunkowej wartości oczekiwanej i praw wielkich liczb. Wszystkie odpowiednie rozdziały I tomu istnieją pod oryginalnymi etykietami bez prefiksu `I-`.
5. **`xr-hyper`.** `books/pl/probability_volume_iii.tex` ma `\externaldocument[I-]`, `\externaldocument[II-]` i `\externaldocument[IV-]`; `books/pl/probability_volume_iv.tex` ma analogiczny import dla tomu I. Prefiks użyty w cytowaniu powstaje w przestrzeni etykiet podczas importu pliku `.aux`; **nie stanowi części deklaracji `\label`** w cytowanym tomie. Importy są warunkowe (`\IfFileExists`), zatem dla faktycznej kompilacji wielotomowej trzeba dopilnować, by `.aux` istniały i były dostępne w odpowiednim katalogu. W tej iteracji nie wykonywano kompilacji PDF z `.aux`.
6. Zgodność cytowania z istniejącym rozdziałem potwierdza **właściciela semantycznego**, a nie dowodzi jeszcze działania linku `GoToR` w określonej przeglądarce PDF. Wymagany jest osobny test integracyjny.

## Proponowana zmiana aplikacji

Rozpoznawać międzytomowe `I-`, `II-`, `III-`, `IV-` na podstawie kontekstu tomu i deklaracji `\externaldocument` oraz oryginalnej etykiety w docelowym tomie, zwracając stan odrębny od prawdziwego `missing`. Nie dopasowywać do dowolnej identycznie nazwanej etykiety poza właściwym tomem. Zastosować regresję dla wszystkich czterech tomów i test kompilacji z rzeczywistymi plikami `.aux`; osobno przetestować sytuację bez `.aux`.

**Ograniczenia:** Nie modyfikowano `chapters/pl/`, `books/pl/`, oryginalnych `\label`, `\ref`, `\eqref`, ani gałęzi `main`. Nie przeprowadzano scalania żadnych działów matematyki. Audyt nie zmienia jeszcze licznika `missing` w aplikacji.

**Stan po XII partii: 156/257 przejrzanych, 101 pozostałych.** Następna partia: 157–169.